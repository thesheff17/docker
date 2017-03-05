#!/bin/bash

# my images
docker pull thesheff17/dev:latest
docker pull thesheff17/dev-min:latest
docker pull thesheff17/apt-cacher-ng

# services
docker pull sameersbn/mysql:latest
docker pull jupyter/minimal-notebook:latest
docker pull mikesplain/openvas:latest
docker pull scylladb/scylla
docker pull redis
docker pull vitess/etcd:v2.0.13-lite

#k8s stuff
docker pull weaveworks/weave-npc:1.9.2
docker pull weaveworks/weave-kube:1.9.2
docker pull gcr.io/google_containers/kube-proxy-amd64:v1.5.3
docker pull gcr.io/google_containers/kube-controller-manager-amd64:v1.5.3
docker pull gcr.io/google_containers/kube-scheduler-amd64:v1.5.3
docker pull gcr.io/google_containers/kube-apiserver-amd64:v1.5.3
docker pull gcr.io/google_containers/etcd-amd64:3.0.14-kubeadm
docker pull gcr.io/google_containers/kubedns-amd64:1.9
docker pull gcr.io/google_containers/dnsmasq-metrics-amd64:1.0
docker pull gcr.io/google_containers/kube-dnsmasq-amd64:1.4
docker pull gcr.io/google_containers/kube-discovery-amd64:1.0
docker pull gcr.io/google_containers/exechealthz-amd64:1.2
docker pull gcr.io/google_containers/pause-amd64:3.0
