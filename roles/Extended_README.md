| Role Name | Description | Called In | Depends On | Tested | Idempotent |
| --- | --- | --- | --- | --- | --- |
| `apt-add-packages` | Installs a list of system packages via APT. (Wraps ansible.builtin.apt in role) | Several | (none) | Tested | Yes |
| `apt-nodejs-add-source` | Adds Node.js APT source for version-controlled installs. | 10_magicmirror, 77_vscodeserver | (none) | Tested | Yes |
| `apt-nvidia-container-toolkit-add-source` | Adds NVIDIA container toolkit repository. | 55_open-webui | (none) |  | Yes |
| `apt-postgresql-add-source` | Adds PostgreSQL APT source for database setup. | 04_cluster (no longer in use) | (none) | Tested | Yes |
| `apt-vault-add-source` | Adds HashiCorp Vault APT source. | 00_proxmox, 06_vault | (none) | Tested | Yes |
| `apt-update-all` | Updates all APT package lists and upgrades installed packages. | Several | (none) | Tested | Yes |
| `certificate-authority-create` | Initializes a new RFC 5280 compliant certificate authority. | 00_proxmox | (none) | Tested | Yes |
| `certificate-authority-copy-to-host` | Copies CA files to target hosts. | 00_proxmox, 04_cluster, 06_vault | certificate-authority-create, or suitable ca.crt | Tested | Yes |
| `certificate-authority-generate-certs` | Issues RFC 2818 compliant certs and keys from the CA with IP SANs. | 00_proxmox, 04_cluster, 06_vault | certificate-authority-create, or suitable ca.crt and ca.key | Tested | will overwrite key/crt |
| `ghcr-secret-create` | Creates Docker registry secrets for GitHub Container Registry. | 04_cluster | microk8s-install | Tested | Yes |
| `git-global-configure` | Configures user's global git config (user.name, user.email). | 77_vscodeserver | (none) | Tested | Yes |
| `git-clone-repositories` | Clones specified Git repositories to target hosts. | 77_vscodeserver | (none) |  | fails on existing clones |
| `host-ssh-keys-create` | Creates ssh-keys for user, if they don't exist. | 77_vscodeserver | (none) | Tested | Yes |
| `kubernetes-kubectl-install` | Installs latest kubectl binary. | 77_vscodeserver | (none) | Tested | No |
| `kubernetes-secrets-bootstrap` | Bootstraps secrets for Kubernetes workloads. | 04_cluster | vault-configure-for-kubevault, kubernetes-fetch-config | Tested | intentionally overwrites existing secret |
| `kubernetes-fetch-config` | Retrieves kubeconfig files from cluster nodes. | 04_cluster | microk8s-configure | Tested | No |
| `kubernetes-kubegres-deploy` | Deploys Kubegres for PostgreSQL HA in Kubernetes. | 04_cluster (no longer in use) | microk8s-enable-addons | Tested | Yes |
| `kubernetes-redis-deploy` | Deploys Redis workloads to Kubernetes. Note: group_vars/all/ceph_enabled. | 04_cluster | microk8s-enable-addons |  | Yes |
| `kubernetes-manifests-sync` | Syncs manifests for components from across all of the source repos. | 04_cluster |  | Tested | Yes |
| `kubernetes-microservices-deploy` | Deploys kv-updater, apiserver, microservices and webdisplay to Kubernetes. | 04_cluster | microk8s-enable-addons, kubernetes-manifests-sync | Tested | Yes |
| `kubernetes-mqtt-telegraf-influxdb-deploy` | Deploys IOT backend services to Kubernetes. | 04_cluster | microk8s-enable-addons, kubernetes-manifests-sync | Tested | Yes |
| `kubernetes-grafana-deploy` | Deploys IOT frontend grafana service to Kubernetes. | 04_cluster | microk8s-enable-addons, kubernetes-manifests-sync | Tested | No* |
| `kubernetes-tcp-ingresses-create` | Creates TCP ingress rules for Kubernetes services. | 04_cluster (no longer in use) | microk8s-enable-addons | Tested | Yes |
| `magic-mirror-install` | Installs MagicMirror² on target hosts. | 10_magicmirror | apt-nodejs-add-source | Tested | No |
| `magic-mirror-update` | Updates MagicMirror² modules and config. | 10_magicmirror | magic-mirror-install | Tested | No |
| `matrix-database-create` | Creates the Postgres 'state' database for my matrix microservices. | 04_cluster (no longer in use) | kubernetes-kubegres-deploy | Tested | fails on existing database |
| `microceph-all` | Installs and configures a MicroCeph cluster. Note: group_vars/all/ceph_enabled. | 04_cluster (not currently in use) | (none) | Tested | fails on existing cluster |
| `microk8s` | Meta-role for MicroK8s orchestration. | 04_cluster (no longer in use) | (none) | Tested | No |
| `microk8s-install` | Installs MicroK8s on target hosts. | 04_cluster | (none) | Tested | Yes |
| `microk8s-assemble-cluster` | Assembles a MicroK8s cluster from nodes. | 04_cluster | microk8s-install | Tested | fails on existing cluster |
| `microk8s-configure` | Applies post-install configuration to MicroK8s. | 04_cluster | microk8s-assemble-cluster | Tested | No |
| `microk8s-enable-addons` | Enables MicroK8s addons (e.g. DNS, ingress). Note: group_vars/all/ceph_enabled. | 04_cluster | microk8s-configure |  | Yes |
| `multipass` | Provisions Multipass VMs. |  | (none) | Tested |  |
| `nodejs-pm2-install` | Installs PM2 process manager for Node.js apps. | 10_magicmirror | apt-nodejs-add-source | Tested | Yes |
| `proxmox-node-setup` | Prepares Proxmox nodes for automation. | 00_proxmox | (none) | Tested | Yes |
| `proxmox-container-create` | Creates LXC containers in Proxmox based on Proxmox container templates. | 00_proxmox | proxmox-node-setup | Tested | Yes |
| `proxmox-container-fetch-image` | Fetches cloud-init enabled container images for Proxmox from linuxcontainers.org. | 00_proxmox | (none) | Tested | Yes |
| `proxmox-container-create-cloud-init` | Creates cloud-init enabled containers. | 00_proxmox | proxmox-node-setup | Tested | Yes |
| `proxmox-vm-fetch-image` | Fetches VM disk images for use in templates. | 00_proxmox | (none) | Tested | Yes |
| `proxmox-vm-create` | Creates virtual machines in Proxmox. | 00_proxmox | proxmox-node-setup | Tested | Yes |
| `proxmox-vm-create-template` | Creates reusable VM templates. | 00_proxmox (not currently in use) | proxmox-node-setup | Tested | Yes |
| `proxmox-vm-create-from-template` | Creates VMs from existing templates. | 00_proxmox (not currently in use) | proxmox-vm-create-template | Tested | Yes |
| `vault-configure` | Configures Vault policies, auth methods, auto-unseal, and secrets engines. | 00_proxmox, 06_vault | apt-vault-add-source | Tested |  |
| `vault-initialize` | Initializes Vault and stores recovery keys. | 00_proxmox, 06_vault | vault-configure | Tested |  |
| `vault-configure-for-kubevault` | Prepares Vault for Kubernetes authentication and Transit encrypt/decypt as a Service supporting my KubeVault pattern from SecretManager. | 04_cluster, 06_vault | vault-initialize, microk8s-install | Tested | vault-auth secret |
