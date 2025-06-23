

📘 Project: Proxmox to Vault-Hardened MicroK8s Cluster
A fully automated system for provisioning Kubernetes-ready nodes via Proxmox, configuring secure Vault-based secrets delivery, orchestrating microceph and microk8s clusters, and deploying services and applications—all with Ansible.

🛠️ Features
- Proxmox VM & LXC container automation via community.general.proxmox
- Cloud-init bootstrapping and cloud-capable templating
- Self-signed RFC-compliant CA and TLS cert generation
- Vault installation, configuration, auto-unseal with GCP KMS
- MicroK8s and MicroCeph clustering with node prep
- Secrets provisioning for K8s workloads using 
- Turnkey deployment of microservices & supporting infrastructure

📁 Repo Structure
.
├── 00_proxmox.yaml         # Proxmox CA creation, VM/container provisioning
├── 01_template_overrides.yaml
├── 03_sha_keys.yaml
├── 04_cluster.yaml         # microk8s & microceph orchestration
├── roles/
│   ├── proxmox-container/
│   ├── proxmox-template/
│   ├── vault-configure/
│   └── ...



🚦 Getting Started
1. Clone & configure
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo


Set your inventory and host_vars for:
- ctid, ansible_host, ip
- SSH key (sshkey) and Proxmox credentials
- Desired LXC and VM specs
2. Create the PKI infrastructure
ansible-playbook 00_proxmox.yaml --tags ca


3. Provision infrastructure
ansible-playbook 00_proxmox.yaml --tags provision


4. Bootstrap the cluster
ansible-playbook 04_cluster.yaml



🔐 Vault + Kubernetes Secrets
Secrets are injected using Vault's Kubernetes auth method and kubevault, a lightweight bridge for managing secrets access via annotations.
Roles involved:
- vault-configure-for-kubevault
- update_secrets
Sample K8s manifest:
annotations:
  vault.hashicorp.com/role: my-app-role
  vault.hashicorp.com/secret-path: secret/data/myapp/config



🌱 Extras
- MagicMirror2 container bootstrapped with Ansible
- Future support for deploy_mtig_stack, open-webui, and other microservices

🔭 Roadmap
- Improve cloud-init templating of base images
- Replace cert patching once MicroK8s supports modern key usages
- Add validation role to verify cluster and secrets bootstrapping
