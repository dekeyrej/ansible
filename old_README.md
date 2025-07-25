# ansible

I had two purposes when I started down the ansible path:
- Learn a bit about ansible, and
- Automate the deployment of my kubernetes environment and my apps

Along the way (of course) this uncovered subtle assumptions/decisions I had made when first assembling the environment which led to rewrites of various parts of my application and the libraries upon which they are built.

Currently (and I hope correctly) all of the interesting bits are contained in the roles. The prepoderance of these roles are related to the building of the cluster, deploying the underlying infrastructure applications (postgres and redis), and the apps themselves onto a set of 'nodes'. There is one role (multipass) for provisioning a set of nodes under multipass which leverages multipass's prebuilt templates and cloud-init support. There are two additional roles (proxmox-template and proxmox-clone) for provisioning nodes on a Proxmox-VE server by creating a template from a cloud-init enabled OS image, and subsequently cloning that template with a cloud-init file.  

The deployment roles work consistently whether deploying to AMD64 Ubuntu hosts, ARM64 Ubuntu hosts, or virtual machines provisioned under Multipass or Proxmox-VE.

# Multipass

00_multipass.yaml:

```
- name: Provision Multipass hosts in inventory
  hosts: localhost
  gather_facts: no
  become: no
  vars_files: 
    - 01_sha_keys.yaml
  roles:
    - multipass
```

# Proxmox-VE 8.4.1

00_proxmox.yaml:

```
- name: Provision Proxmox VM hosts
  hosts: localhost
  become: no
  vars_files:
    - 01_sha_keys.yaml
    - 02_host_list.yaml
  roles:
    - proxmox-template
    - proxmox-clone
```
Simpler (shell script) implementation -

run the following as root from the command prompt on your proxmox server

make_template.sh:

```
#!/usr/bin/env bash
curl -I https://cloud-images.ubuntu.com/noble/current/noble-server-cloudimg-amd64.img | grep Last-Modified > current
if cmp -s current last; then
   echo "Image is current"
else
   echo "New image available. Fetching now"
   rm noble-server-cloudimg-amd64.img
   wget https://cloud-images.ubuntu.com/noble/current/noble-server-cloudimg-amd64.img
   cp current last
fi
qm create 9000 --balloon 2048 --memory 8192 --cores 2 --cpulimit 2 --cpu cputype=host --net0 virtio,bridge=vmbr0 --scsihw virtio-scsi-pci
qm set 9000 --scsi0 nvme_pool:0,import-from=/root/noble-server-cloudimg-amd64.img
qm set 9000 --ostype l26
qm set 9000 --ide2 nvme_pool:cloudinit
qm set 9000 --boot order=scsi0
qm set 9000 --agent enabled=1
qm template 9000
```

clone_hosts.sh:

```
#!/usr/bin/env bash
for i in {0..4}
do
   vmid="12$i"
   qm clone 9000 "$vmid" --name "host$i"
   qm resize "$vmid" scsi0 +47G
   qm set "$vmid" --cicustom "user=local:snippets/userconfig-$vmid.yaml"
   qm set "$vmid" --ipconfig0 ip=192.168.86.$((i+3))/24,gw=192.168.86.1
   qm start "$vmid"
done
```

[these userconfig files vary for each vmid only by hostname, and are autogenerated ]

userconfig-120.yaml:

```
#cloud-config
hostname: host0
manage_etc_hosts: true
users:
  - name: ubuntu
    sudo: ALL=(ALL) NOPASSWD:ALL
    ssh_authorized_keys: ['id_rsa.pub for your ansible host', 'and other hosts you may want to ssh in from']
apt:
  preserve_sources_list: true
  sources:
    # keyid is output from wget -qO- https://www.postgresql.org/media/keys/ACCC4CF8.asc | gpg --with-fingerprint --with-colons | awk -F: '/^fpr/ { print $10 }'
    keyid: B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8
    source: deb https://apt.postgresql.org/pub/repos/apt noble-pgdg main
package_update: true
package_upgrade: true
packages:
- qemu-guest-agent
- postgresql-client-17
- python3-psycopg2
- python3-kubernetes
snap:
  commands:
    0: snap install microceph
    1: snap install microk8s --classic
    2: snap install kubectl --classic
runcmd:
  - usermod -aG microk8s ubuntu
  - reboot                          # required to activate qemu-guest-agent and microk8s group membership
final_message: |
  cloud-init has finished
  version: $version
  timestamp: $timestamp
  datasource: $datasource
  uptime: $uptime
```

# Cluster Deployment

03_cluster.yaml:

```
- name: Prepare all nodes (update, install packages, setup microceph and microk8s)
  hosts: allnodes
  become: yes
  vars_files:
    - 04_disk_list.yaml
  roles:
    - microceph               # bootstraps storage cluster, adds nodes to cluster, and add disks
    - microk8s                # joins nodes to the kubernetes cluster, 
                              # enables necessary addons, including rook-ceph which provides
                              # ceph network storage to the cluster

- name: Deploy cluster services (kubegres, redis, tcp_ingresses)
  hosts: prime
  become: no
  roles:
    - kubegres                # installs 3 replica setup - one master (r/w), 2 backups (ro)
    - redis                   # single instance redis service
    - tcp_ingresses           # creates necessary TCP ingresses to support external connections

- name: Deploy application microservices
  hosts: prime
  become: no
  roles:
    - create_matrix_database  # creates necessary postgres database to support microservices
    - github_secret           # creates github container repository pull secret to pull containers
    - update_secrets          # creates config maps and secrets to support microservices
    - deploy_microservices    # depoloys actual microservices, api, and webdisplay
```