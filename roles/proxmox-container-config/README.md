# Terraform/OpenTofu + Proxmox-VE Containers

The bpg terraform/opentofu proxmox provider is a beatiful piece of work and nicely implements the Proxmox-VE 9.0.x API! Thanks Pavel!!

However, the Proxmox-VE API has some limitations (OK, one in particular) that cause me a bit of angst - there is no **simple** way to create a container with openssh-server, a non-root user, and ssh keys for that non-root user from a 'late-model', cloud-container image.  

My current workaround is to provision the container via Terraform/OpenTofu, and then 'ansible it' (this role) into shape.

To invoke this role, it needs two variables: the VMID of the container, and whether the template is a 'standard' one, or not.

for this playbook:
```yaml
# fix-terraformed-container.yaml
# call with -e "vmid=<vmid> standard=<true|false>"
- name: fix terraformed proxmox containers
  hosts: iluvatar   # this is the PVE node where the container is provisioned
  roles:
    - proxmox-container-config
```

call it with:
```bash
ansible-playbook fix-terraformed-container.yaml -e "vmid=107 standard=false"
```