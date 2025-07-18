# 🛠️ Ansible Roles Overview

Welcome to the heart of my homelab automation engine. This directory contains modular, task-oriented Ansible roles designed to provision, configure, and orchestrate a wide range of infrastructure components — from containerized services to Kubernetes clusters, certificate authorities, and beyond.

Each role is purpose-built, idempotent, and scoped to a single responsibility. While some tasks may appear conceptually similar (e.g. image fetching, secret creation), their implementations are tailored to the specific systems they interact with.

---

## 📦 Role Index

| Role Name | Description |
|-----------|-------------|
| `apt-add-packages` | Installs a curated list of system packages via APT. |
| `apt-nodejs-add-source` | Adds Node.js APT source for version-controlled installs. |
| `apt-nvidia-container-toolkit-add-source` | Adds NVIDIA container toolkit repository. |
| `apt-postgresql-add-source` | Adds PostgreSQL APT source for database setup. |
| `apt-vault-add-source` | Adds HashiCorp Vault APT source. |
| `apt-update-all` | Updates all APT package lists and upgrades installed packages. |
| `certificate-authority-create` | Initializes a new RFC 5280 compliant certificate authority. |
| `certificate-authority-copy-to-host` | Copies CA files to target hosts. |
| `certificate-authority-generate-certs` | Issues RFC 2818 compliant certs and keys from the CA with IP SANs. |
| `ghcr-secret-create` | Creates Docker registry secrets for GitHub Container Registry. |
| `git-global-configure` | Configures user's global git config (user.name, user.email). |
| `git-clone-repositories` | Clones specified Git repositories to target hosts. |
| `host-ssh-keys-create` | Creates ssh-keys for user, if they don't exist.|
| `kubernetes-kubectl-install` | Installs latest kubectl binary. |
| `kubernetes-secrets-bootstrap` | Bootstraps secrets for Kubernetes workloads. |
| `kubernetes-fetch-config` | Retrieves kubeconfig files from cluster nodes. |
| `kubernetes-kubegres-deploy` | Deploys Kubegres for PostgreSQL HA in Kubernetes. |
| `kubernetes-redis-deploy` | Deploys Redis workloads to Kubernetes. |
| `kubernetes-manifests-sync` | Syncs manifests for components from across all of the source repos. |
| `kubernetes-microservices-deploy` | Deploys kv-updater, apiserver, microservices and webdisplay to Kubernetes. |
| `kubernetes-mqtt-telegraf-influxdb-deploy` | Deploys IOT backend services to Kubernetes.|
| `kubernetes-grafana-deploy` | Deploys IOT frontend grafana service to Kubernetes.|
| `kubernetes-tcp-ingresses-create` | Creates TCP ingress rules for Kubernetes services. |
| `magic-mirror-install` | Installs MagicMirror² on target hosts. |
| `magic-mirror-update` | Updates MagicMirror² modules and config. |
| `matrix-database-create` | Creates the Postgres 'state' database for my matrix microservices. |
| `microceph-all` | Installs and configures a MicroCeph cluster. |
| `microk8s` | Meta-role for MicroK8s orchestration. |
| `microk8s-install` | Installs MicroK8s on target hosts. |
| `microk8s-assemble-cluster` | Assembles a MicroK8s cluster from nodes. |
| `microk8s-configure` | Applies post-install configuration to MicroK8s. |
| `microk8s-enable-addons` | Enables MicroK8s addons (e.g. DNS, ingress). |
| `multipass` | Provisions Multipass VMs. |
| `nodejs-pm2-install` | Installs PM2 process manager for Node.js apps. |
| `proxmox-node-setup` | Prepares Proxmox nodes for automation. |
| `proxmox-container-create` | Creates LXC containers in Proxmox based on Proxmox container templates. |
| `proxmox-container-fetch-image` | Fetches cloud-init enabled container images for Proxmox from linuxcontainers.org. |
| `proxmox-container-create-cloud-init` | Creates cloud-init enabled containers. |
| `proxmox-vm-fetch-image` | Fetches VM disk images for use in templates. |
| `proxmox-vm-create` | Creates virtual machines in Proxmox. |
| `proxmox-vm-create-template` | Creates reusable VM templates. |
| `proxmox-vm-create-from-template` | Creates VMs from existing templates. |
| `vault-configure` | Configures Vault policies, auth methods, auto-unseal, and secrets engines. |
| `vault-initialize` | Initializes Vault and stores recovery keys. |
| `vault-configure-for-kubevault` | Prepares Vault for Kubernetes authentication and Transit encrypt/decypt as a Service supporting my KubeVault pattern from [SecretManager](https://github.com/dekeyrej/secretmanager). |

---

## 🧭 Usage Notes

- Roles are designed to be composable and declarative.
- Most roles assume root or elevated privileges.
- Secrets and sensitive data should be passed via Vault or Ansible Vault.
- For orchestration, use tagged playbooks or include roles conditionally.

---

## 🧪 Future Enhancements

- Add role tags and dependencies in `meta/main.yml`
- Introduce shared handlers for common tasks (e.g. restart services)
- Consider grouping roles into collections for better reuse

---

## 🤝 Contributions

This repository is a living system. If you spot improvements, edge cases, or want to extend functionality — PRs and issues are welcome.
