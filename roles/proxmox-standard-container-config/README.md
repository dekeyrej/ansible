# Terraform/OpenTofu + Proxmox-VE Containers

The bpg terraform/opentofu proxmox provider is a beatiful piece of work and nicely implements the Proxmox-VE 9.0.x API! Thanks Pavel!!

However, the Proxmox-VE API has some limitations (OK, one in particular) that cause me a bit of angst - there is no **simple** way to create a container with openssh-server, a non-root user, and ssh keys for that non-root user from a 'late-model', cloud-container image.  

My current workaround is to provision the container via Terraform/OpenTofu, and then 'ansible it' (this role) into shape. The 'normal' provisioning process requires and ssh-key for the root user.

for this playbook:
```yaml
# fix-terraformed-container.yaml
- name: fix terraformed proxmox containers
  hosts: bluepnode  # this is the host_group for all of the VMs and LXC Containers on the PVE node
  gather_facts: no
  roles:
    - proxmox-standard-container-config
```

call it with:
```bash
ansible-playbook fix-terraformed-container.yaml
```