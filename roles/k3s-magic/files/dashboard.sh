kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.10.0/deploy/static/provider/cloud/deploy.yaml
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml
kubectl create serviceaccount admin-user -n kubernetes-dashboard
kubectl apply -f dashboard-clusterrole.yaml
kubectl apply -f dashboard-secret.yaml
kubectl patch serviceaccount kubernetes-dashboard -n kubernetes-dashboard -p '{"secrets": [{"name": "admin-user-token"}]}'
kubectl describe secret admin-user-token -n kubernetes-dashboard | grep token > dashboard.token
kubectl apply -f dashboard-ingress.yaml
