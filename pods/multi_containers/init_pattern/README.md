# Init container

## Project description

In this example, I am using a web server as main container and a container that runs before the main container(init container). One version of the init container is an app that downloads a page that will be served by the web server, the other generates the page that will be served. Both make use of a shared volume to the server to access the `.html` file.

## Deploy && destroy

```shell
kubectl apply -f  
kubectl delete pod multi-ctr-init-xpl 
```
