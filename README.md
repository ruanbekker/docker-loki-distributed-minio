# docker-loki-distributed-minio
Distributed Loki setup with BoltDB and Minio using Docker

## Resources

Extra credit goes to the ones in the below issues, as I retrieved most of the loki config from there:

- https://github.com/grafana/loki/issues/2155
- https://github.com/grafana/loki/issues/1434

Documentation on Loki:

- https://grafana.com/docs/loki/latest/configuration/examples/#almost-zero-dependencies-setup
- https://grafana.com/docs/loki/latest/operations/storage/boltdb-shipper/

Extra resources to add a Go app to this stack:

- https://medium.com/martinomburajr/building-a-go-web-app-from-scratch-to-deploying-on-google-cloud-part-4a-containerizing-our-go-e1ae2b152ee2
- https://semaphoreci.com/community/tutorials/how-to-deploy-a-go-web-application-with-docker
- https://github.com/shijuvar/golang-docker/blob/master/main.go

Similar:

- https://github.com/CloudXiaobai/loki-cluster-deploy/tree/master/demo/docker-compose
