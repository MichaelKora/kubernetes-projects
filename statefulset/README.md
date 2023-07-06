# StatefulSet

StatefulSets are apps that create and save valuable data. They can be compared to dps because of their cloud-native abilities (scaling, self healing...). However, Sts provide more, namly persistent pod names, persistent DNS and persistent volumes.

## Naming

Sts allow persistent names following this schema for each pods name: `<StatefulSet-name>-<integer>`

## Scaling

Sts create the pods one after the other(from 0 to the highest). Each Pod has to be running and ready before the controller starts deploying the next one.

If 3 pods are running (0-2) and they need to be scaled up to 5, then -3 is created first. The controller waits until its running and ready before starting deploying -4.

When scaling down, the highest has to be destroyed first then the second highest etc.

Unlike Dps who require Replicaset, Sts manage their own scalings.

### Volume

StatefulSets need to create volumes dynamically if they need them. This is archived by using VolumeClaimTemplates. When creating a new Pod, the controller creates a Pod and a Volume. The Volume is named so that it can be match to the correct Pod.

### Deletion

Deletion does not guarantee sequential destruction of the Pods, if we want sequential deletion then a scale down to 0 is needed. When deleting, Pods are deleted but not Volumes. Next time the same Pod is create, the controller picked up the existing Volume(the one used before the deletion) without creating a new one.

### Rollouts

Rollouts are done by posting the new version of the manifest to the API. The controller starts by updating the Pod with the highest index (-x). It waits until the Pod with the new version is running and ready before continuing with the next highest index.

### Test

```shell
kubectl apply - f gcp-sc.yaml
kubectl apply -f headless-svc.yaml
kubectl apply -f statefulset.yaml

# delete
kubectl delete - f gcp-sc.yaml
kubectl delete -f headless-svc.yaml
kubectl delete -f statefulset.yaml
```
