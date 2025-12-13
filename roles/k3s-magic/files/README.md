## K3s 'uniqueness' (compared to MicroK8s)
- K3s defaults to traefik. (MicroK8s defaults to nginx, my ingresses are written against nginx)
- K3s implements RBAC.  (MicroK8s does not (by default))
- K3s doesn't provide a dashboard out of the box.
- default API is on port 6443. (MicroK8s is 16443)

### Make the cluster
- install K3s on 'main' node without traefik
  - generate a random token: `cat /dev/urandom | tr -dc 'a-zA-Z0-9' | head -c 20`  # the output is 'somerandomvalue'
  - ```bash
    curl -sfL https://get.k3s.io | sh -s - server --cluster-init --token somerandomvalue --write-kubeconfig-mode 644 --disable traefik \
       --cluster-ca /tmp/k3s-custom-ca/ca.crt --cluster-ca-key /tmp/k3s-custom-ca/ca.key \
       --tls-san hostname --tls-san hostname.local
    ```
- install K3s and join cluster for 'other' nodes without traefik
  - `curl -sfL https://get.k3s.io | sh -s - server --server https://192.168.86.91:6443 --token somerandomvalue --write-kubeconfig-mode 644 --disable traefik`

### Change storage to longhorn (optional, but a good idea)
- 'undefault' local-path storage
  - `kubectl patch storageclass local-path -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"false"}}}'`
- add longhorn storage to cluster
  - `kubectl apply -f https://raw.githubusercontent.com/longhorn/longhorn/v1.8.1/deploy/longhorn.yaml`

### Add dashboard (with RBAC)
- files/dashboard.sh:
  - install nginx
    - `kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.10.0/deploy/static/provider/cloud/deploy.yaml`
  - manually add dashboard to cluster
    - `kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml`
  - create a clusterrole to manage cluster via dashboard, grant role to dashboard service account
    - `kubectl apply -f files/dashboard-clusterrole.yaml`
  - create a secret and apply it to the dashboard service account
    - `kubectl apply -f files/dashboard-secret.yaml`
    - `kubectl patch serviceaccount kubernetes-dashboard -n kubernetes-dashboard -p '{"secrets": [{"name": "admin-user-token"}]}'`
  - (common) dump dashboard token to login
    - `kubectl describe secret admin-user-token -n kubernetes-dashboard | grep token > dashboard.token`
  - (common) create an nginx ingress for the dashboard
    - `kubectl apply -f files/dashboard-ingress.yaml`

### Deploy Redis
- (common) deploy redis - redis-namespace.yaml, redis-config.yaml, redis-service.yaml, redis-statefulset.yaml

### Do RBAC for Vault/Kubernetes integration
- add role for vault to create token reviews, grant to vault-auth service account
  - `kubectl apply -f files/token-review-role-and-binding.yaml`
- add role for microservices to read secrets and create service account tokens, grant to default service account
  - `kubectl apply -f files/microservice-role-and-binding.yaml`

### Deploy Joey's workloads
- (common) bootstrap secrets - 
  - secrets: ghcr-login-secret, matrix-secrets (vault-encrypted secrets.json) [requires encryptonator]
  - configmaps: matrix-events (events.json), secretcfg (secretcfg.json), secretdef (secretdef.json)
- (common) deploy kv-updater    - kv-updater.yaml
- (common) deploy apiserver     - apiserver-deployment.yaml, apiserver-service.yaml, apiserver-ingress.yaml
- (common) deploy microservices - aqi.yaml, weather.yaml, moon.yaml, nfl.yaml, mlb.yaml, events.yaml, github.yaml, mycal.yaml
- (common) deploy webdisplay    - webdisplay-deployment.yaml, webdisplay-service.yaml, webdisplay-ingress.yaml
