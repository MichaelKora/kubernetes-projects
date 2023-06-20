# Deployments

This dir examples about Deployments in K8s. Dp Yaml, rollout, rollback examples...

## Create a namespace

```shell
kubectl apply -f dps-namespace.yaml
```

## Additional commands

```shell
kubectl get deploy webserver-dp -n test-dps
kubectl describe deploy webserver-dp -n test-dps
kubectl get rs -n test-dps
kubectl describe rs  webserver-dp -n test-dps
```
