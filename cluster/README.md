# Kind

This `.yaml` file allows the creation of a local multi-node K8s cluster with KinD.

## CMDs

- Install:

```bash
kind create cluster --config=kind-cluster.yaml
```

- Tear down:

```bash
kind delete cluster -n learning-cluster
```
