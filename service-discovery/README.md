# Service discovery

## Example

Here two namespaces are created: `dev` and `prod` they both have one Deployment(with the same name in each ns: `planets`) and one Service (with the same name in both ns: `telescope`). Now a Pod `remote-control` is deployed in only the dev namespace. After deploying all of this, we'll access both services from the `remote-control`.

There are planets in the universe to be seen. Depending on where you are on the earth you might see different planets. So this example is simulating that behavior by positioning two telescopes on the earth: one in the north pole(dev) and the other one in the south pole(prod). the remote control shows us pictures taken by each telescope.

### Deploy

```shell
# north pole
kubectl apply -f dev-stack.yaml
# south pole
kubectl apply -f prod-stack.yaml
# remote controle
kubectl apply -f remote-control.yaml
```

### Test

```shell
kubectl exec -it remote-ctl -n north-pole -- bash
cat /etc/resolv.conf
apt-get update && apt-get install curl -y

# connect to the telescope in the north pole(in the dev env) here the unqualified name is enough
curl telescope:8080

# connect to the telescope in the south pole(prod env) hier fully qualified domain name (FQDN) is required
curl telescope.south-pole.svc.cluster.local:8080

```

### Clean Up

```shell
# remote controle
kubectl delete -f remote-control.yaml
# north pole
kubectl delete -f dev-stack.yaml
# south pole
kubectl delete -f prod-stack.yaml
```
