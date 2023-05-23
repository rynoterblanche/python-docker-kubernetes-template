# Deployments

## Docker

## Kubernetes

### Some Useful Commands

Validate pod creation:

```commandline
kubectl create -f nginx.pod.yml --dry-run=client --validate=true
```

Create a pod:

```commandline
kubectl create -f nginx.pod.yml
```

Create a pod with saved config (you can then use `apply` for changes to that pod) :

```commandline
kubectl create -f nginx.pod.yml --save-config
```

Create or apply changes to a pod:

```commandline
kubectl apply -f nginx.pod.yml
```

Delete a pod:

```commandline
kubectl delete pod my-pod
```

or

```commandline
kubectl delete -f nginx.pod.yml
```

