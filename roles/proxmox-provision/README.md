# proxmox-provision 🛡️

A grand-unified Ansible role for declarative provisioning of Proxmox guests—LXC or KVM, Ubuntu or Debian—driven entirely by inventory logic. Minimal inputs, maximal clarity.

## ✨ Features

- 🧩 Modular logic for any guest type (`lxc`, `kvm`)
- 🧙‍♂️ OS-aware provisioning (`ubuntu`, `debian`)
- 🌐 Network mode inferred from inventory:
  - `ansible_host` present → static IP
  - `ansible_host` absent → DHCP
- 🔐 Optional VMID assignment:
  - If `vmid` is set → honored
  - If `vmid` is unset → next available assigned
- 📦 Cloud-init and network-config templating
- 🧪 Fully tested across all permutations
- 🛠️ Override defaults using host_vars

## 📦 Requirements

- Proxmox API access
- Ansible 2.14+
- Inventory structured with:
  ```yaml
  guest_name:
    type: lxc
    os: ubuntu
    ansible_host: 192.168.1.101  # optional; implies static IP
    vmid: 101                    # optional; auto-assigned if omitted
  ```

## 🚀 Usage
Include the role in your playbook:
```yaml
- hosts: all
  roles:
    - proxmox-provision
```

## 🧪 Test Matrix

| Type | OS | IP Mode Inferred | VMID Set | Status | 
|---|---|---|---|---|
| LXC | Ubuntu | Static | ✅ | ✅ | 
| LXC | Debian | DHCP | ❌ | ✅ | 
| KVM | Ubuntu | DHCP | ✅ | ✅ | 
| KVM | Debian | Static | ❌ | ✅ | 

## 🗺️ Philosophy
This role is designed for clarity, maintainability, and joy. It embodies a thematic infrastructure vision—where every guest is provisioned with purpose, and every line of logic tells a story.

## 🧙‍♂️ Author
Crafted by @dekeyrej, a meticulous architect of modular systems and thematic homelabs.
