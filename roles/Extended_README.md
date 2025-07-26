# 🧩 Extended Role Catalog
This document provides a detailed breakdown of all roles used in this infrastructure. Roles are grouped by functional category, with notes on status and purpose. 
For a high-level overview, see [roles/README.md](./README.md).

But wait! There's more in [roles/Monolithic_role_list.md](./Monolithic_role_list.md)

## 📘 Index
- [🛠️ Core System Setup](#️-core-system-setup)
- [🔐 Certificate Authority & Secrets](#-certificate-authority--secrets)
- [🧬 Git & SSH Configuration](#-git--ssh-configuration)
- [☸️ Kubernetes & MicroK8s](#-kubernetes--microk8s)
- [🧙 MagicMirror & Node.js](#-magicmirror--nodejs)
- [🧠 LLM & AI Interfaces](#-llm--ai-interfaces)
- [🧱 Proxmox Infrastructure](#-proxmox-infrastructure)
- [🧪 Experimental / Deprecated](#-experimental--deprecated)

## 🛠️ Core System Setup
| Role Name | Status | Attributes | Notes | 
|---|---|---|---|
| apt-add-packages | ✅ Active | apt, core | Installs system packages | 
| apt-update-all | ✅ Active | apt, core | Updates and upgrades packages | 
| apt-add-source-nodejs | ✅ Active | apt, nodejs | Adds Node.js APT source | 
| apt-add-source-nvidia | ✅ Active | apt, gpu | Adds NVIDIA APT source | 
| apt-add-source-postgresql | ✅ Active | apt, db | Adds PostgreSQL APT source | 
| apt-add-source-vault | ✅ Active | apt, vault | Adds Vault APT source | 
| book-of-creation-delivery | ✅ Active | bootstrap, ansible | Places vault.password and manwe.sh | 


## 🔐 Certificate Authority & Secrets
| Role Name | Status | Attributes | Notes | 
|---|---|---|---|
| certificate-authority-create | ✅ Active | ca, security | Initializes RFC 5280 CA | 
| certificate-authority-copy-to-host | ✅ Active | ca, security | Distributes CA files | 
| certificate-authority-generate-certs | ✅ Active | ca, tls | Issues certs with IP SANs | 
| vault-configure | ✅ Active | vault, security | Configures Vault | 
| vault-initialize | ✅ Active | vault, security | Initializes Vault | 
| vault-configure-for-kubevault | ✅ Active | vault, kubernetes | Integrates Vault with Kubernetes | 


## 🧬 Git & SSH Configuration
| Role Name | Status | Attributes | Notes | 
|---|---|---|---|
| git-global-configure | ✅ Active | git, config | Sets global Git config | 
| git-clone-repositories | ✅ Active | git, repos | Clones Git repos | 
| git-add-sshkey | ✅ Active | git, ssh | Adds SSH key for Git | 
| host-ssh-keys-create | ✅ Active | ssh, host | Creates SSH keys for host | 
| host-ssh-keys-set | ✅ Active | ssh, host | Sets SSH keys on host | 
| known-hosts-clear | ✅ Active | ssh, host | Clears known hosts | 
| known-hosts-add | ✅ Active | ssh, host | Adds known hosts | 

## ☸️ Kubernetes & MicroK8s
Cluster Setup
| Role Name | Status | Attributes | Notes | 
|---|---|---|---|
| microceph-all | 💤 Dormant | storage, experimental | Not in use | 
| microk8s-install | ✅ Active | microk8s, setup | Installs MicroK8s | 
| microk8s-assemble-cluster | ✅ Active | microk8s, cluster | Assembles cluster | 
| microk8s-configure | ✅ Active | microk8s, config | Configures MicroK8s | 
| microk8s-enable-addons | ✅ Active | microk8s, addons | Enables addons | 

Secrets & Config
| Role Name | Status | Attributes | Notes | 
|---|---|---|---|
| ghcr-secret-create | ✅ Active | docker, secrets | Creates GHCR pull secret | 
| kubernetes-fetch-config | ✅ Active | config, k8s | Fetches kubeconfig | 
| kubernetes-secrets-bootstrap | ✅ Active | secrets, k8s | Bootstraps secrets | 
| kubernetes-encryptonator-build | ✅ Active | secrets, k8s | Builds encryption executable | 
| kubernetes-recryptonator-build | ✅ Active | secrets, k8s | Builds encryption key rotator | 
| kubernetes-recryptonator-deploy | ✅ Active | secrets, k8s | Deploys encryption key rotator |


 Workloads
| Role Name | Status | Attributes | Notes | 
|---|---|---|---|
| kubernetes-kubegres-deploy | 💤 Dormant | db, k8s | Deploys PostgreSQL via Kubegres | 
| kubernetes-redis-deploy | ✅ Active | cache, k8s | Deploys Redis | 
| kubernetes-tcp-ingresses-create | 💤 Dormant | networking, k8s | Creates TCP ingresses | 
| kubernetes-manifests-sync | ✅ Active | maintenance, k8s | Pulls current deplopyment manifests | 
| kubernetes-microservices-deploy | ✅ Active | apps, k8s | Deploys microservices | 
| kubernetes-mqtt-telegraf-influxdb-deploy | ✅ Active | iot, monitoring, k8s | Deploys MQTT stack | 
| kubernetes-grafana-deploy | ✅ Active | monitoring, k8s | Deploys Grafana | 


## 🧙 MagicMirror & Node.js
| Role Name | Status | Attributes | Notes | 
|---|---|---|---|
| magic-mirror-install | ✅ Active | frontend, display | Installs MagicMirror | 
| magic-mirror-update | ✅ Active | frontend, display | Updates MagicMirror | 
| nodejs-pm2-install | ✅ Active | nodejs, pm2 | Installs PM2 process manager | 

## 🧠 LLM & AI Interfaces
| Role Name | Status | Attributes | Notes | 
|---|---|---|---|
| ollama-install | ✅ Active | ai, gpu | Installs Ollama and NVIDIA deps | 
| open-webui-install | ✅ Active | ai, frontend | Installs Open-WebUI | 

## 🧱 Proxmox Infrastructure
 
Containers
| Role Name | Status | Attributes | Notes | 
|---|---|---|---|
| proxmox-container-create-cloud-init | ✅ Active | containers, proxmox | Creates container with cloud-init | 

VMs
| Role Name | Status | Attributes | Notes | 
|---|---|---|---|
| proxmox-vm-create | ✅ Active | vm, proxmox | Creates VM |
| proxmox-vm-create-template | 💤 Dormant | vm, template, proxmox | Creates VM template | 
| proxmox-vm-create-from-template | 💤 Dormant | vm, template, proxmox | Creates VM from template | 



## 🧪 Experimental / Deprecated
| Role Name | Status | Attributes | Notes | 
|---|---|---|---|
| microk8s | ❌ Deprecated | kubernetes, experimental | Superseded by modular roles | 
| multipass | ❌ Deprecated | vm, experimental | Not in use | 
| proxmox-node-setup | ❌ Deprecated | infra, proxmox | replaced by `creation.sh` |
| proxmox-container-create | ❌ Deprecated | containers, proxmox | Superseded by cloud-init variant | 
| proxmox-container-fetch-image | ❌ Deprecated | containers, proxmox | Subsumed into [`proxmox-container-create-cloud-init`](#Containers) | 
| proxmox-vm-fetch-image | ❌ Deprecated | vm, proxmox | Subsumed into [`proxmox-vm-create`](#VMs) | 

