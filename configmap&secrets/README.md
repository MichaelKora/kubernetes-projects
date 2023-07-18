# Configmaps and Secrets

## Configmaps

There are two files: one deploying a single Configmap and another a multi Configmap.

### Using Configmap & env vars

`pod-using-multimap.yaml` showcases how Configmaps are used with env var.

### Using Configmap & startup cmds

`startup-cmd.yaml`

### Using Configmap & volume

The file `vol-configmap.yaml` create a secret and mounts the entries as files to the container.

```shell
# Deploy
kubectl apply -f vol-configmap.yaml

# see mounted vol
kubectl exec vol-pod -- ls /etc/name
kubectl exec vol-pod -- cat /etc/name/firstname

# edit
kubectl edit cm cm-names
    ## change the values to City: Berlin; Country Germany

# see changes
kubectl exec vol-pod -- ls /etc/name
kubectl exec vol-pod -- cat /etc/name/City

```

## Secrets

### Create secrets in an imperative way

```shell
kubectl create secret generic creds --from-literal user=michaelkora --from-literal pwd=secured
```

### Deploy secret using the declarative method

- Start by creating and encoding the secrets:

```shell
# uid
echo -n 'johnDoe' | base64

# pwd
echo -n 'strongpwd' | base64
```

- export var:

```shell
export K8S_UID="am9obkRvZQ=="
```

- deploy secret:

```shell
envsubst < secrets.yaml | kubectl apply -f -
```

### Use secret in Pod

```shell
# deploy
kubectl apply -f secret-pod.yaml

# test
kubectl exec secret-pod -- ls /etc/securedCreds
kubectl exec secret-pod -- cat /etc/securedCreds/username

# decode
echo <code> | base64 -d
```

### Tear down

```shell
kubectl delete -f secret-pod.yaml
kubectl delete -f secrets.yaml
```
