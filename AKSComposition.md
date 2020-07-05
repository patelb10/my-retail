## Monitoring and alerting of Azure Kubernetes Service (AKS) cluster

 ### Kubernetes provide basic monitoring using Kubernetes Dashboard and Metrics server.
 You can use Dashboard to troubleshoot your containerized application, and manage the cluster resources.
 You can use Dashboard to get an overview of applications running on your cluster, as well as for creating or modifying individual Kubernetes resources
 You can check the detail log of a particular Pod.
 Metric server collects metrics from the Summary API, exposed by Kubelet on each node. Metrics Server registered in the main API server through Kubernetes aggregator. This API doesn’t store the metric values, so it’s not possible for example to get the amount of resources used by a given node 10 minutes ago.
 
 ### Prometheus and Grafana
 Prometheus joined the Cloud Native Computing Foundation in 2016 as the second hosted project, after Kubernetes.
 This document describes the  setup to collect and graph metrics using Prometheus and Grafana.
