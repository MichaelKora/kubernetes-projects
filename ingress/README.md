# Ingress

Ingress allows to use a single LoadBalancer to manage all the incoming traffic and then uses host-based & path-based routing to forward requests to the right Service.
Ingress is based on two constructs: a controller and an object spect. The object defines the routing rules and the controller applies them.

Unlike other Controllers (dps ...) Ingress Controllers are generally not preinstalled and need to be installed first.

## Ingress classes

```shell
kubectl apply -f ingress-classes.yaml
kubectl delete -f ingress-classes.yaml
```

## Install Ingress NGINX Controller

Here, I'm using the [NGINX Ingress Controller](https://github.com/kubernetes/ingress-nginx). The used manifest YAML has been downloaded [here](https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.0/deploy/static/provider/cloud/deploy.yaml).

```shell
# download manifest
wget https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.0/deploy/static/provider/cloud/deploy.yaml

# rename
mv nginx-ingress-controller.yaml ingress-nginx-controller.yaml

# deploy
kubectl apply -f ingress-nginx-controller.yaml

# destroy
kubectl delete -f ingress-nginx-controller.yaml
```

## Steps

- App

```shell
kubectl apply -f my-web-app.yaml
kubectl delete -f my-web-app.yaml
```

- Ingress objects

```shell
kubectl apply -f host-based.yaml
kubectl apply -f path-based.yaml

kubectl delete -f host-based.yaml
kubectl delete -f path-based.yaml
```

- Configure DNS

```shell
sudo vim /etc/hosts/
```

Past the following.(remove this while tearing down)

```yaml
<IP> universe.com
<IP> needle-galaxy.universe.com
<IP> milky-way.universe.com
<IP> fireworks-galaxy.universe.com
```
