# docker-loki-distributed-minio
Distributed Loki setup with BoltDB and Minio using Docker

## About

There's options for using different ring backend storage:

- The `docker-compose.yml` provides a distributed loki stack with **etcd** as the backend kvstore
- The `docker-compose-consul.yml` provides a distrubuted loki stack with **consul** as the backend kvstore
- The `docker-compose-traefik.yml` provides a distrubuted loki stack with **etcd** as the backend kvstore

## Components

This stack consists of:

- loki-distributor (promtail or docker logging driver points to this component)
- loki-querier (grafana or logcli points to this component)
- loki-ingester
- loki-table-manager
- redis
- etcd or consul

The architecture document can be viewed [here](https://grafana.com/docs/loki/latest/fundamentals/architecture/)

## Pre-Requisites

For your containers to use to loki logging driver, you need to install it using:

```bash
$ docker plugin install grafana/loki-docker-driver:latest --alias loki --grant-all-permissions
```

## Logging Options

To use loki logging driveri (push logs directly to loki):

```yaml
    logging:
      driver: loki
      options:
        loki-url: http://localhost:3101/loki/api/v1/push
        loki-external-labels: job=dockerlogs,environment=development
```

To use json file logging driver (and let promtail scrape the logs):

```yaml
    logging:
      driver: "json-file"
      options:
        max-size: "1m"
        max-file: "1"
        tag: "{{.Name}}"
```

## Boot the Stack:

```bash
docker-compose -f docker-compose-consul.yml up -d --build
```

## Make HTTP Requests

Test the flask-app:

```bash
curl 'http://localhost:5000/?msg=hi'
```

Test the nginx-app:

```bash
curl 'http://localhost:8084/?msg=bye
```

## Example Queries

Query labels as k/v pairs using `logfmt`:

```
{container_name="flask-app"} | logfmt |= "scheme=http"
```

Metric Queries: Log Entries sum by `container_name`:

```
sum(rate({job="containerlogs"}[30s])) by (container_name)
```

## Resources

Extra credit goes to the ones in the below issues, as I retrieved most of the loki config from there:

- https://github.com/grafana/loki/issues/2155
- https://github.com/grafana/loki/issues/1434

Documentation on Loki:

- https://grafana.com/docs/loki/latest/configuration/examples/#almost-zero-dependencies-setup
- https://grafana.com/docs/loki/latest/operations/storage/boltdb-shipper/
- https://grafana.com/blog/2020/10/28/loki-2.0-released-transform-logs-as-youre-querying-them-and-set-up-alerts-within-loki/

Extra resources to add a Go app to this stack:

- https://medium.com/martinomburajr/building-a-go-web-app-from-scratch-to-deploying-on-google-cloud-part-4a-containerizing-our-go-e1ae2b152ee2
- https://semaphoreci.com/community/tutorials/how-to-deploy-a-go-web-application-with-docker
- https://github.com/shijuvar/golang-docker/blob/master/main.go

Similar:

- https://github.com/CloudXiaobai/loki-cluster-deploy/tree/master/demo/docker-compose and [blog](https://www.mdeditor.tw/pl/pFBb/zh-hk)
