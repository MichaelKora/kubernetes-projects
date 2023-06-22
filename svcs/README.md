# Deployments

This dir examples about Deployments in K8s. Dp Yaml, rollout, rollback examples...

## Namespace

```shell
#create
kubectl apply -f svc-namespace.yaml
#delete
kubectl delete -f svc-namespace.yaml
#more cmds
kubectl config set-context --current --namespace=test-pds
kubectl get namespace
kubectl config view --minify | grep namespace:

```

## Deploy web-app

```shell
kubectl apply -f webserver-dp.yaml
kubectl delete -f webserver-dp.yaml

```

## Deploy DualStack Service

```shell
kubectl apply -f dual-stack-web-svc.yaml
kubectl delete -f dual-stack-web-svc.yaml
```

## Deploy LB to the cloud

```shell
kubectl apply -f load-balancer-svc.yaml
kubectl delete -f load-balancer-svc.yaml
```

## Additional commands

```shell
# get EndpointSlices
kubectl get endpointslices -n svc-ns
# describe a specific endpointslice
kubectl describe endpointslice <name-of-the-endpointslice> -n svc-ns
```
