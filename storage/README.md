# StorageClass

StorageClasses allow us to dynamically create physical a backend storage and to map it to a PersistenVolume on K8s. The user defines a SC referencing CSI plugin, then the SC creates the volume on the physical backend storage and the StorageClass then surveils the API (waiting for PVCs). When a PVC(referencing the created StorageClass) is posted to the API, then the SC creates the resource; maps it to a PV on K8s. And now other apps can access the PV using the PVC name.

## Example

### Local cluster

The `pvc-local.yaml` creates a PVC based on a built-in SC, then deploy a Pod using the PVC. This example is deployed on a local cluster. (The setup of the cluster can be found [here](https://github.com/MichaelKora/kubernetes-projects/tree/main/cluster)).

```shell
kubectl apply -f pvc-local.yaml
kubectl delete -f pvc-local.yaml
```

### GKE

The `regional-gke-pvc.yaml` creates a SC, then references it in a PVC and the PVC is used in a Pod.
The `reclaimPolicy: Retain` causes the created PV to be created even after deleting the PVC.

```shell
#deploy
kubectl apply -f regional-gke-pvc.yaml

#tear down
kubectl delete -f regional-gke-pvc.yaml
kubectl delete pv <pv-name>
```

## CMDs

```shell
kubectl get sc
kubectl get pvc
kubectl get pv

kubectl describe sc <sc>
kubectl describe pvc <pvc>
kubectl describe pv <pv>
```
