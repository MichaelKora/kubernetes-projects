# RBAC

When a request is created in K8s, it's submitted to the API Server then it has to successfuly go through Authentication, Authorization and Admission Control before being applied.

## Authentication

## CMDs

```shell
kubectl api-resources --sort-by name -o wide

# create ns
kubectl apply -f namespaces.yaml
# Create and bind Roles
kubectl apply -f roles.yaml
kubectl apply -f roleBindings.yaml

# create and bind clusterRoles
kubectl apply -f clusterRole.yaml

# create Role and bind them within a namespace
kubectl apply -f ns-clusterRoleBinding.yaml

# clean up
kubectl delete -f ns-clusterRoleBinding.yaml
kubectl delete -f clusterRole.yaml
kubectl delete -f roleBindings.yaml
kubectl delete -f roles.yaml
kubectl delete -f namespaces.yaml
```
