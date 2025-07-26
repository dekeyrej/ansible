| Role Name | Description | Called In | Depends On | Tested | Idempotent |
| --- | --- | --- | --- | --- | --- |
| `apt-add-packages` | Installs a list of system packages via APT. (Wraps ansible.builtin.apt in role) | Several | (none) | Tested | Yes |
| `apt-add-source-nodejs` | Adds Node.js APT source for version-controlled installs. | the-coming-of-stormcrow, the-creation-of-manwe | (none) | Tested | Yes |
| `apt-add-source-nvidia-container-toolkit` | Adds NVIDIA container toolkit repository. | 55_open-webui | (none) |  | Yes |
| `apt-add-source-postgresql` | Adds PostgreSQL APT source for database setup. | the-forming-of-the-fellowship (no longer in use) | (none) | Tested | Yes |
| `apt-add-source-vault` | Adds HashiCorp Vault APT source. | the-delving-of-moria | (none) | Tested | Yes |
| `apt-update-all` | Updates all APT package lists and upgrades installed packages. | Several | (none) | Tested | Yes |
| `certificate-authority-create` | Initializes a new RFC 5280 compliant certificate authority. |the-creation-of-manwe | (none) | Tested | Yes |
| `certificate-authority-copy-to-host` | Copies CA files to target hosts. | the-forming-of-the-fellowship, the-delving-of-moria | certificate-authority-create, or suitable ca.crt | Tested | Yes |
| `certificate-authority-generate-certs` | Issues RFC 2818 compliant certs and keys from the CA with IP SANs. | the-forming-of-the-fellowship, the-delving-of-moria | certificate-authority-create, or suitable ca.crt and ca.key | Tested | will overwrite key/crt |
| `ghcr-secret-create` | Creates Docker registry secrets for GitHub Container Registry. | the-forming-of-the-fellowship | microk8s-install | Tested | Yes |
| `git-global-configure` | Configures user's global git config (user.name, user.email). | the-creation-of-manwe | (none) | Tested | Yes |
| `git-clone-repositories` | Clones specified Git repositories to target hosts. | the-creation-of-manwe | (none) |  | fails on existing clones |
| `host-ssh-keys-create` | Creates ssh-keys for user, if they don't exist. | the-creation-of-manwe | (none) | Tested | Yes |
| `host-ssh-keys-set` | Sets ssh-keys for user, if they don't exist. | the-creation-of-manwe | (none) | Tested | Yes |
| `kubernetes-kubectl-install` | Installs latest kubectl binary. | the-creation-of-manwe | (none) | Tested | No |
| `kubernetes-secrets-bootstrap` | Bootstraps secrets for Kubernetes workloads. | the-forming-of-the-fellowship | vault-configure-for-kubevault, kubernetes-fetch-config | Tested | intentionally overwrites existing secret |
| `kubernetes-fetch-config` | Retrieves kubeconfig files from cluster nodes. | the-forming-of-the-fellowship | microk8s-configure | Tested | No |
| `kubernetes-kubegres-deploy` | Deploys Kubegres for PostgreSQL HA in Kubernetes. | the-forming-of-the-fellowship (no longer in use) | microk8s-enable-addons | Tested | Yes |
| `kubernetes-redis-deploy` | Deploys Redis workloads to Kubernetes. Note: group_vars/all/ceph_enabled. | the-forming-of-the-fellowship | microk8s-enable-addons |  | Yes |
| `kubernetes-manifests-sync` | Syncs manifests for components from across all of the source repos. | the-forming-of-the-fellowship |  | Tested | Yes |
| `kubernetes-microservices-deploy` | Deploys kv-updater, apiserver, microservices and webdisplay to Kubernetes. | the-forming-of-the-fellowship | microk8s-enable-addons, kubernetes-manifests-sync | Tested | Yes |
| `kubernetes-mqtt-telegraf-influxdb-deploy` | Deploys IOT backend services to Kubernetes. | the-forming-of-the-fellowship | microk8s-enable-addons, kubernetes-manifests-sync | Tested | Yes |
| `kubernetes-grafana-deploy` | Deploys IOT frontend grafana service to Kubernetes. | the-forming-of-the-fellowship | microk8s-enable-addons, kubernetes-manifests-sync | Tested | No* |
| `kubernetes-tcp-ingresses-create` | Creates TCP ingress rules for Kubernetes services. | the-forming-of-the-fellowship (no longer in use) | microk8s-enable-addons | Tested | Yes |
| `magic-mirror-install` | Installs MagicMirror² on target hosts. | the-coming-of-stormcrow | apt-nodejs-add-source | Tested | No |
| `magic-mirror-update` | Updates MagicMirror² modules and config. | the-coming-of-stormcrow | magic-mirror-install | Tested | No |
| `matrix-database-create` | Creates the Postgres 'state' database for my matrix microservices. | the-forming-of-the-fellowship (no longer in use) | kubernetes-kubegres-deploy | Tested | fails on existing database |
| `microceph-all` | Installs and configures a MicroCeph cluster. Note: group_vars/all/ceph_enabled. | the-forming-of-the-fellowship (not currently in use) | (none) | Tested | fails on existing cluster |
| `microk8s` | Meta-role for MicroK8s orchestration. | the-forming-of-the-fellowship (no longer in use) | (none) | Tested | No |
| `microk8s-install` | Installs MicroK8s on target hosts. | the-forming-of-the-fellowship | (none) | Tested | Yes |
| `microk8s-assemble-cluster` | Assembles a MicroK8s cluster from nodes. | the-forming-of-the-fellowship | microk8s-install | Tested | fails on existing cluster |
| `microk8s-configure` | Applies post-install configuration to MicroK8s. | the-forming-of-the-fellowship | microk8s-assemble-cluster | Tested | No |
| `microk8s-enable-addons` | Enables MicroK8s addons (e.g. DNS, ingress). Note: group_vars/all/ceph_enabled. | the-forming-of-the-fellowship | microk8s-configure |  | Yes |
| `multipass` | Provisions Multipass VMs. |  | (none) | Tested |  |
| `nodejs-pm2-install` | Installs PM2 process manager for Node.js apps. | the-coming-of-stormcrow | apt-nodejs-add-source | Tested | Yes |
| `proxmox-node-setup` | Prepares Proxmox nodes for automation. | (deprecated - functions moved to creation.sh) | (none) | Tested | Yes |
| `proxmox-container-create-cloud-init` | Creates cloud-init enabled containers. | manwe, moria, stormcrow | proxmox-node-setup | Tested | Yes |
| `proxmox-container-create` | Creates LXC containers in Proxmox based on Proxmox container templates. | (deprecated - replaced by `proxmox-container-create-cloud-init`) | proxmox-node-setup | Tested | Yes |
| `proxmox-container-fetch-image` | Fetches cloud-init enabled container images for Proxmox from linuxcontainers.org. | (deprecated - included in `proxmox-container-create-cloud-init`) | (none) | Tested | Yes |
| `proxmox-vm-fetch-image` | Fetches VM disk images for use in templates. | 00_proxmox | (none) | Tested | Yes |
| `proxmox-vm-create` | Creates virtual machines in Proxmox. | 00_proxmox | proxmox-node-setup | Tested | Yes |
| `proxmox-vm-create-template` | Creates reusable VM templates. | 00_proxmox (not currently in use) | proxmox-node-setup | Tested | Yes |
| `proxmox-vm-create-from-template` | Creates VMs from existing templates. | 00_proxmox (not currently in use) | proxmox-vm-create-template | Tested | Yes |
| `vault-configure` | Configures Vault policies, auth methods, auto-unseal, and secrets engines. | the-delving-of-moria | apt-vault-add-source | Tested |  |
| `vault-initialize` | Initializes Vault and stores recovery keys. | 00_proxmox, the-delving-of-moria | vault-configure | Tested |  |
| `vault-configure-for-kubevault` | Prepares Vault for Kubernetes authentication and Transit encrypt/decypt as a Service supporting my KubeVault pattern from SecretManager. | the-forming-of-the-fellowship, the-delving-of-moria | vault-initialize, microk8s-install | Tested | vault-auth secret |
