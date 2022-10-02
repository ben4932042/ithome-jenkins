# Deploy Jenkins To Kubernetes
## Add Repo
The following command allows you to download and install all the charts from this repository:
```
helm repo add bitnami https://charts.bitnami.com/bitnami
```


## Test
```
helm install {{ RELEASE_NAME }} bitnami/jenkins -v ./values.yaml
```

## Production
```
helm install {{ RELEASE_NAME }} bitnami/jenkins \
    -v ./values.yaml \
    --set jenkinsUser={{ USER_NAME }} \
    --set jenkinsPassword={{ PASSWORD }} \
    --set persistence.enabled=true \ 
    --set persistence.storageClass={{ STORAGECLASS_NAME }}
```
