# ansible

I had two purposes when I started down the ansible path:
- Learn a bit about ansible, and
- Automate the deployment of my kubernetes environment and my apps

Along the way (of course) this uncovered subtle assumptions/decisions I had made when first assembling the environment which led to rewrites of various parts of my application and the libraries upon which they are built.

Currently (and I hope correctly) all of the interesting bits are contained in the roles. The prepoderance of these roles are related to the building of the cluster,
deploying the underlying infrastructure applications (postgres and redis), and the apps themselves onto a set of 'nodes'. There is one role (multipass) for provisioning a set of nodes under multipass which leverages multipass's prebuilt templates and cloud-init support. There are two additional roles (proxmox-template and proxmox-clone) for provisioning nodes on a Proxmox-VE server by creating a template from a cloud-init enabled OS image, and subsequently cloning that template with a clooud-init file.  

The deployment roles work consistently whether deplloying to AMD64 Ubuntu hosts, ARM64 Ubuntu hosts, or virtual machines provisioned under Multipass or Proxmox-VE.

# Multipass

```
- name: Provision Multipass hosts in inventory
  hosts: localhost
  connection: local
  gather_facts: no
  become: no
  vars_files: 
    - 01_sha_keys.yaml
  roles:
    - multipass
```

# Proxmox-VE 8.4.1

```
- name: Provision Proxmox VM hosts
  hosts: localhost
  connection: local
  become: no
  vars_files:
    - 03_host_list.yaml
  roles:
    - proxmox-template
    - proxmox-clone
  tasks:
    - name: Take a pause for cloud-init to complete
      ansible.builtin.pause:
        seconds: 90
```
Simpler (shell script) implementation -

run the following as root from the command prompt on your proxmox server

make_template.sh:

```
#!/usr/bin/env bash
wget https://cloud-images.ubuntu.com/noble/current/noble-server-cloudimg-amd64.img
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

[these userconfig files vary for each vmid only by hostname]

userconfig-120.yaml:

```
#cloud-config
hostname: host0
manage_etc_hosts: true
user: ubuntu
password: [a custom password for ubuntu, if you want to set it]
ssh_authorized_keys:
  - [id_rsa.pub for your ansible host]
chpasswd:
  expire: False
users:
  - default
package_update: true
package_upgrade: true
packages:
  - qemu-guest-agent
runcmd:
  - reboot
```

# Cluster Deployment

```
- name: Prepare all nodes (update, install packages, setup microceph and microk8s)
  hosts: allnodes
  become: yes
  vars_files:
    - 02_disk_list.yaml
  roles:
    - update_all              # not _really_ required if your cloud-init does an update/upgrade
    - postgresql_client       # installs the latest PostgreSQL client libraries/binaries
    - microceph               # installs snap, bootstraps cluster, adds node to cluster, and add disks
    - microk8s                # installs snaps, joins nodes to the cluster, 
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