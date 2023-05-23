# Deployments

## Docker

## Kubernetes

### Useful Pod Commands

```bash
# Examples

# Validate pod creation
kubectl create -f nginx.pod.yml --dry-run=client --validate=true 

# Create a pod:
kubectl create -f nginx.pod.yml

# Create a pod with saved config (you can then use `apply` for changes to that pod) :
kubectl create -f nginx.pod.yml --save-config

# Create or apply changes to a pod:
kubectl apply -f nginx.pod.yml

# Delete a pod:
kubectl delete pod my-pod
# or
kubectl delete -f nginx.pod.yml
```

### Useful Deployment Commands

```bash
# Examples

# Create a deployment with saved config (you can then use `apply` for changes to that deployment):
kubectl create -f nginx.deployment.yml --save-config

# Describe deployment:
kubectl describe deployment nginx-server

# Get deployments:
kubectl get deployments --show-labels
kubectl get deployments -l app=nginx-server

# Scale deployments:
kubectl scale -f nginx.deployment.yml --replicas=5

# Delete a deployment:
kubectl delete -f nginx.deployment.yml
```