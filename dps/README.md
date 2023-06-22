# Deployments

This dir examples about Deployments in K8s. Dp Yaml, rollout, rollback examples...

## Namespace

```shell
#create
kubectl apply -f dps-namespace.yaml
#delete
kubectl delete -f dps-namespace.yaml
#more cmds
kubectl config set-context --current --namespace=test-pds
kubectl get namespace
kubectl config view --minify | grep namespace:

```

## Deploy web-app

```shell
kubectl apply -f deployments.yaml
kubectl delete -f deployments.yaml
```

## Deploy web-svc

```shell
kubectl apply -f web-svc.yaml
kubectl delete -f web-svc.yaml
```

## Additional commands

```shell
kubectl get deploy webserver-dp -n dps-ns
kubectl describe deploy webserver-dp -n dps-ns
kubectl get rs -n dps-ns
kubectl describe rs  webserver-dp -n dps-ns
```
