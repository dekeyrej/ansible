# 🧩 Role Overview

This repository contains modular Ansible roles for orchestrating my thematic homelab infrastructure. Roles are grouped by function and purpose:

- 🛠️ Core System Setup
- 🔐 Certificate Authority & Secrets
- 🧬 Git & SSH Configuration
- ☸️ Kubernetes & MicroK8s
- 🧙 MagicMirror & Node.js
- 🧠 LLM & AI Interfaces
- 🧱 Proxmox Infrastructure
- 🧪 Experimental / Deprecated

For a full breakdown of each role, including usage notes and dependencies, see the [Extended Role Table](./Extended_README.md).

---

### 🛠️ Core System Setup
These roles handle base system configuration and package management.
- apt-add-packages: Installs system packages via APT.
- apt-update-all: Updates and upgrades all APT packages.
- apt-add-source-*: Adds APT sources for Node.js, NVIDIA, PostgreSQL, Vault.
- book-of-creation-delivery: Places vault.password and manwe.sh in repo root.

### 🔐 Certificate Authority & Secrets
Roles for secure communication and secrets management.
- certificate-authority-create: Initializes RFC 5280 CA.
- certificate-authority-copy-to-host: Distributes CA files.
- certificate-authority-generate-certs: Issues certs with IP SANs.
- vault-configure, vault-initialize, vault-configure-for-kubevault: Full Vault lifecycle and Kubernetes integration.
- ghcr-secret-create: Creates Docker registry secrets.

### 🧬 Git & SSH Configuration
For repository access and secure host communication.
- git-global-configure, git-clone-repositories, git-add-sshkey
- host-ssh-keys-create, host-ssh-keys-set
- known-hosts-clear, known-hosts-add

### ☸️ Kubernetes & MicroK8s
Extensive roles for cluster setup, secrets, and workload deployment.
- Cluster Setup:
- microk8s-install, microk8s-assemble-cluster, microk8s-configure, microk8s-enable-addons
- Secrets & Config:
- kubernetes-encryptonator-build, kubernetes-secrets-bootstrap, kubernetes-fetch-config
- Workloads:
- kubernetes-kubegres-deploy, kubernetes-redis-deploy, kubernetes-microservices-deploy, kubernetes-mqtt-telegraf-influxdb-deploy, kubernetes-grafana-deploy
- Maintenance:
- kubernetes-manifests-sync, kubernetes-recryptonator-build, kubernetes-recryptonator-deploy, kubernetes-tcp-ingresses-create

### 🧙 MagicMirror & Node.js
For frontend and display services.
- magic-mirror-install, magic-mirror-update
- nodejs-pm2-install

### 🧠 LLM & AI Interfaces
Roles for deploying AI tools.
- ollama-install: Installs Ollama and NVIDIA dependencies.
- open-webui-install: Installs Open-WebUI frontend.

### 🧱 Proxmox Infrastructure
Roles for VM and container orchestration.
- Node Prep:
- proxmox-node-setup
- Containers:
- proxmox-container-create-cloud-init, proxmox-container-create, proxmox-container-fetch-image
- VMs:
- proxmox-vm-fetch-image, proxmox-vm-create, proxmox-vm-create-template, proxmox-vm-create-from-template

### 🧪 Experimental / Deprecated / Not in Use
Roles marked as deprecated or not currently active.
- microceph-all, microk8s, multipass
- Deprecated Proxmox roles: proxmox-container-create, proxmox-container-fetch-image, proxmox-vm-fetch-image

---

## 🤝 Contributions

This repository is a living system. If you spot improvements, edge cases, or want to extend functionality — PRs and issues are welcome.
