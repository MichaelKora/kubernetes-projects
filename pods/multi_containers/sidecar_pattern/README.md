# Sidecar pattern

## Description

In this example, the main app is an NGINX web server and serves a static web page. The sidecar container watches is a git sync container and watches for changes on [this repo](https://github.com/MichaelKora/ps-sidecar); forked from [here](https://github.com/nigelpoulton/ps-sidecar). The sidecar copies the new content to the shared volume and the web page serves the version.

## Deploy & destroy

```shell
kubectl apply -f side_car_pods.yaml 

# deploy pod and service
kubectl delete pod git-sync 
kubectl delete service svc-sidecar 
```
