# Ambassador pattern

## Description

In this example, we are considering a caching case. We have redis DB deployed and we want to connect to them. When using just one instance, it is not hard to implement but in our case there are more then one instance. We are using the `malexer/twemproxy` image as ambassador to check which node is up and healthy and then connect to it.

## Deploy and destroy

- Redis DBs:

```shell
#deploy
kubectl apply -f redis-dbs.yaml 

#destroy
kubectl delete -f redis-dbs.yaml 
```

- Ambassador pods:

```shell
#deploy
kubectl apply -f ambasador_pods.yaml 

#destroy
kubectl delete -f ambasador_pods.yaml 
```
