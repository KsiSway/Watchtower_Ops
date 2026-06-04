---
sourceFile: "Kubernetes Architecture: Control Plane, Pods and Namespaces - SFEIR Institute"
exportedBy: "Kortex"
exportDate: "2026-05-20T06:50:17.419Z"
---

# Kubernetes Architecture: Control Plane, Pods and Namespaces - SFEIR Institute

f7719f80-43d9-4d05-a1ea-b517003c1842

Kubernetes Architecture: Control Plane, Pods and Namespaces - SFEIR Institute

8ef9e231-2182-4c75-8b91-988baddcda28

https://institute.sfeir.com/en/kubernetes-training/architecture-kubernetes-control-plane-pods/

Kubernetes Architecture: Control Plane, Pods and Namespaces | SFEIR Institute

🏆 SFEIR is the Google Cloud EMEA Training Partner of the Year 2025

https://institute.sfeir.com/en/training/partnerships/google-cloud

🤝 New partnership: Official GitLab Training

https://institute.sfeir.com/en/training/partnerships/gitlab

🤖 New training: AI-Augmented Developer

https://institute.sfeir.com/en/training/ai-augmented-developer

🏆 SFEIR is the Google Cloud EMEA Training Partner of the Year 2025

https://institute.sfeir.com/en/training/partnerships/google-cloud

🤝 New partnership: Official GitLab Training

https://institute.sfeir.com/en/training/partnerships/gitlab

🤖 New training: AI-Augmented Developer

https://institute.sfeir.com/en/training/ai-augmented-developer

https://institute.sfeir.com/en/training/

Certifications

https://institute.sfeir.com/en/certifications/

https://institute.sfeir.com/en/articles/

https://institute.sfeir.com/en/contact/

Catalog 2026

https://institute.sfeir.com/en/training/

Kubernetes Training

https://institute.sfeir.com/en/kubernetes-training/

Kubernetes Fundamentals for Beginners

https://institute.sfeir.com/en/kubernetes-training/kubernetes-fundamentals-for-beginners/

/ Kubernetes Architecture: Control Plane, Pods and Namespaces

Kubernetes Architecture: Control Plane, Pods and Namespaces

#### SFEIR Institute

- March 4, 2026

In this section Kubernetes Architecture: Control Plane, Pods and Namespaces 5 / 10

Kubernetes Fundamentals for Beginners

https://institute.sfeir.com/en/kubernetes-training/kubernetes-fundamentals-for-beginners/

In this section

Comprehensive guide Install Kubernetes Locally: Complete Guide with Minikube, Kind and K3d

https://institute.sfeir.com/en/kubernetes-training/install-kubernetes-local-guide-minikube-kind-k3d/

quickstart Deploy Your First Kubernetes Pod in 15 Minutes

https://institute.sfeir.com/en/kubernetes-training/deploy-first-pod-kubernetes-tutorial-beginner/

Comparison Kubernetes vs Docker: Understanding the Essential Differences

https://institute.sfeir.com/en/kubernetes-training/kubernetes-vs-docker-differences-essential/

concept Docker and Containers: Why Use Them?

https://institute.sfeir.com/en/kubernetes-training/docker-containers-pourquoi-utiliser/

concept Kubernetes Architecture: Control Plane, Pods and Namespaces

https://institute.sfeir.com/en/kubernetes-training/architecture-kubernetes-control-plane-pods/

Cheatsheet kubectl: Essential Commands for Beginners

https://institute.sfeir.com/en/kubernetes-training/kubectl-commands-essential-beginners/

Comprehensive guide Kubernetes Deployments and ReplicaSets: Practical Guide

https://institute.sfeir.com/en/kubernetes-training/deployments-replicasets-kubernetes-guide/

Comprehensive guide Kubernetes Services: Expose Your Applications

https://institute.sfeir.com/en/kubernetes-training/services-kubernetes-expose-applications/

Comprehensive guide PersistentVolumes, ConfigMaps and Kubernetes Secrets

https://institute.sfeir.com/en/kubernetes-training/persistent-volumes-configmaps-secrets-kubernetes/

concept Kubernetes RBAC: Introduction to Access Control

https://institute.sfeir.com/en/kubernetes-training/rbac-kubernetes-control-access-introduction/

Key Takeaways

✓ Control plane orchestrates, worker nodes execute workloads

✓ etcd stores the entire cluster state - back it up regularly

✓ Pods + namespaces = isolation and organization of containerized applications

Kubernetes architecture

relies on a clear separation between the control plane and worker nodes. Understanding this architecture is the first step toward understanding container orchestration. According to the

CNCF Annual Survey 2025

https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/

82% of container users

run Kubernetes in production. This massive adoption requires a solid understanding of fundamental components.

: Kubernetes architecture revolves around the control plane (cluster brain) that orchestrates pods (execution units) organized in namespaces (isolated logical spaces). Mastering these three concepts enables efficient design, deployment, and maintenance of cloud-native applications.

To discover these concepts with hands-on exercises, explore the

Kubernetes Fundamentals training

https://institute.sfeir.com/en/training/kubernetes-les-fondamentaux/

What is Kubernetes architecture?

Kubernetes architecture

is a distributed system designed to orchestrate containerized applications at scale. It follows a declarative model: you define the desired state, Kubernetes maintains it.

Key takeaway: Kubernetes continuously compares the cluster's current state to the desired state and makes necessary adjustments automatically.

#### This architecture divides into two distinct layers:

Main Components

Control Plane

Decisions and orchestration

kube-apiserver, etcd, scheduler, controller-manager

Workload execution

kubelet, kube-proxy, container runtime

The first Kubernetes commit dates from

June 6, 2014

https://kubernetes.io/blog/2024/06/06/10-years-of-kubernetes/

, with 250 files and 47,501 lines of code. Version 1.0 was released on July 21, 2015.

How does the Kubernetes control plane work?

Kubernetes control plane

constitutes the cluster's brain. It makes all global decisions: pod scheduling, failure detection, event response.

kube-apiserver: the single entry point

kube-apiserver

is the control plane's frontend component. All communication goes through it:

# Check cluster state via the API
kubectl cluster-info

# Query the API server directly
kubectl get --raw /api/v1/namespaces

The API server validates each request, applies admission policies, and persists state in etcd.

etcd: the cluster's memory

is a distributed key-value database that stores the entire cluster state. Without etcd, Kubernetes cannot function.

# Typical etcd configuration
apiVersion: v1
kind: Pod
metadata:
name: etcd
spec:
containers:
- name: etcd
image: registry.k8s.io/etcd:3.5.10-0
command:
- etcd
- --data-dir=/var/lib/etcd

#### Key takeaway:

Back up etcd regularly

. Losing etcd means complete loss of cluster configuration.

kube-scheduler: intelligent assignment

kube-scheduler

determines which node to run each pod on. It evaluates available resources, affinity constraints, and priority policies.

kube-controller-manager: the reconciliation loop

#### This component runs controllers that maintain the desired state:

ReplicaSet controller

: maintains requested replica count

Node controller

: monitors node health

Endpoint controller

: populates Endpoints objects

Service Account controller

: creates default accounts

To deepen control plane administration, check our

complete Kubernetes Training guide

https://institute.sfeir.com/en/kubernetes-training/

What is a pod in Kubernetes architecture?

is the smallest deployable unit in Kubernetes. It encapsulates one or more containers that share network and storage.

apiVersion: v1
kind: Pod
metadata:
name: nginx-pod
namespace: production
spec:
containers:
- name: nginx
image: nginx:1.27
ports:
- containerPort: 80
resources:
requests:
memory: "64Mi"
cpu: "250m"
limits:
memory: "128Mi"
cpu: "500m"

Essential pod characteristics

Description

Pods can be deleted and recreated at any time

Unique IP address

Each pod receives an IP in the cluster network

Shared volumes

Containers in a pod access the same volumes

A pod belongs to a single namespace

Key takeaway: Never deploy pods directly in production. Use Deployments or StatefulSets that manage their lifecycle.

IT teams spend an average of

34 work days per year

resolving Kubernetes problems. Understanding pods significantly reduces this time.

To discover pod management, check

Kubernetes fundamentals for beginners

https://institute.sfeir.com/en/kubernetes-training/kubernetes-fundamentals-for-beginners/

How do namespaces organize Kubernetes architecture?

is a logical name space that segments cluster resources. It enables isolation, access control, and quota management.

# List existing namespaces
kubectl get namespaces

# Create a namespace
kubectl create namespace staging

# Deploy in a specific namespace
kubectl apply -f deployment.yaml -n staging

Default namespaces

#### Kubernetes creates four initial namespaces:

Resources without explicit namespace

kube-system

Kubernetes system components

kube-public

Publicly accessible resources

kube-node-lease

Lease objects for node health detection

Namespacing best practices

Isolate environments

: create distinct namespaces for dev, staging, and production.

apiVersion: v1
kind: ResourceQuota
metadata:
name: production-quota
namespace: production
spec:
hard:
requests.cpu: "10"
requests.memory: 20Gi
limits.cpu: "20"
limits.memory: 40Gi
pods: "50"

Apply Network Policies

to control inter-namespace traffic:

apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
name: deny-cross-namespace
namespace: production
spec:
podSelector: {}
policyTypes:
- Ingress
ingress:
- from:
- namespaceSelector:
matchLabels:
environment: production

What is the relationship between control plane and worker nodes?

Worker nodes

execute workloads orchestrated by the control plane. Each node contains three essential components.

kubelet: the node agent

runs on each worker node. It receives pod specifications from the control plane and ensures their execution.

# Check kubelet state
systemctl status kubelet

# kubelet logs
journalctl -u kubelet -f

kube-proxy: the service network

maintains network rules on each node. It enables communication between services via iptables or IPVS.

Container runtime: container execution

The runtime (containerd, CRI-O) actually executes containers. Kubernetes communicates with it via the CRI (Container Runtime Interface).

According to the

Spectro Cloud 2025

https://www.spectrocloud.com/state-of-kubernetes-2025

80% of organizations

run Kubernetes in production with an average of 20+ clusters per company.

How to visualize Kubernetes architecture in practice?

┌─────────────────────────────────────────────────────────────┐
│                      CONTROL PLANE                          │
│  ┌─────────────┐  ┌──────────┐  ┌──────────────────────┐   │
│  │ kube-apiserver │  │  etcd    │  │ controller-manager │   │
│  └─────────────┘  └──────────┘  └──────────────────────┘   │
│  ┌────────────────┐  ┌─────────────────────────────────┐   │
│  │ kube-scheduler │  │ cloud-controller-manager        │   │
│  └────────────────┘  └─────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────┐
│                      WORKER NODES                           │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Node 1                                               │   │
│  │  ┌─────────┐  ┌───────────┐  ┌─────────────────┐   │   │
│  │  │ kubelet │  │ kube-proxy│  │ container runtime│   │   │
│  │  └─────────┘  └───────────┘  └─────────────────┘   │   │
│  │  ┌─────────────────────────────────────────────┐   │   │
│  │  │ Pods (namespace: default, production, ...)  │   │   │
│  │  └─────────────────────────────────────────────┘   │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘

This architecture explains why

71% of Fortune 100 companies

https://kubernetes.io/blog/2024/06/06/10-years-of-kubernetes/

run Kubernetes in production.

Which commands to explore Kubernetes architecture?

# Control plane components
kubectl get --raw='/healthz?verbose'

# Node details
kubectl describe nodes

# All system pods
kubectl get pods -n kube-system

# Recent cluster events
kubectl get events --sort-by='.lastTimestamp' -A

# Resources by namespace
kubectl api-resources --namespaced=true

The Kubernetes market will reach

$8.41 billion by 2031

with a CAGR of 21.85% according to

Mordor Intelligence

https://www.mordorintelligence.com/industry-reports/kubernetes-market

. Mastering this architecture is a career investment.

Get Hands-on with SFEIR Institute

Understanding Kubernetes architecture theoretically is not enough. Chris Aniszczyk, CNCF CTO, states:

"Kubernetes is no longer experimental but foundational. Soon, it will be essential to AI as well." —

CNCF State of Cloud Native 2026

https://www.cncf.io/blog/2026/02/19/state-of-cloud-native-2026-cncf-ctos-insights-and-predictions/

Train with practitioner experts

Kubernetes Fundamentals

https://institute.sfeir.com/en/training/kubernetes-les-fondamentaux/

: discover architecture and key concepts in one intensive day

LFS458 Kubernetes Administration

https://institute.sfeir.com/en/training/administration-kubernetes/

: master the control plane and prepare for CKA certification

LFD459 Kubernetes for Developers

https://institute.sfeir.com/en/training/kubernetes-pour-les-developpeurs-d-applications/

: deploy your applications and prepare for CKAD

Contact our advisors

https://institute.sfeir.com/en/contact/

to define your Kubernetes training path.reading\_time: 6

Previous Docker and Containers: Why Use Them?

https://institute.sfeir.com/en/kubernetes-training/docker-containers-pourquoi-utiliser/

Next kubectl: Essential Commands for Beginners

https://institute.sfeir.com/en/kubernetes-training/kubectl-commands-essential-beginners/

The training organization by and for tech enthusiasts.

https://www.linkedin.com/showcase/sfeir-institute/

https://twitter.com/sfeir

https://www.youtube.com/c/SFEIRTV

SFEIR Ecosystem

https://www.sfeir.com/

https://sfeir.dev/

wenvision.com

https://www.wenvision.com/

AI & Gen AI Training

https://institute.sfeir.com/en/training/ai/

Kubernetes Training

https://institute.sfeir.com/en/training/kubernetes/

Cloud Training

https://institute.sfeir.com/en/training/cloud/

DevOps Training

https://institute.sfeir.com/en/training/devops/

Data Training

https://institute.sfeir.com/en/training/data/

Frontend Training

https://institute.sfeir.com/en/training/frontend/

Backend Training

https://institute.sfeir.com/en/training/backend/

Security Training

https://institute.sfeir.com/en/training/security/

FinOps Training

https://institute.sfeir.com/en/training/finops/

Partnerships

All partners

https://institute.sfeir.com/en/training/partnerships/

AWS Training

https://institute.sfeir.com/en/training/partnerships/aws/

Confluent Training

https://institute.sfeir.com/en/training/partnerships/confluent/

dbt Training

https://institute.sfeir.com/en/training/partnerships/dbt/

GitLab Training

https://institute.sfeir.com/en/training/partnerships/gitlab/

Google Cloud Training

https://institute.sfeir.com/en/training/partnerships/google-cloud/

Linux Foundation Training

https://institute.sfeir.com/en/training/partnerships/linux-foundation/

Microsoft Training

https://institute.sfeir.com/en/training/partnerships/microsoft/

SFEIR Institute Training

https://institute.sfeir.com/en/training/partnerships/sfeir-institute/

WEnvision Training

https://institute.sfeir.com/en/training/partnerships/wenvision/

https://institute.sfeir.com/en/about/

https://institute.sfeir.com/en/enterprise/

Training Calendar

https://institute.sfeir.com/en/training/calendar/

Training Centers

https://institute.sfeir.com/en/training-centers/

https://institute.sfeir.com/en/contact/

https://institute.sfeir.com/en/faq/

https://institute.sfeir.com/en/resources/

All our trainers

https://institute.sfeir.com/en/instructors/

Google Cloud Authorized Trainers

https://institute.sfeir.com/en/google-cloud-authorized-trainers/

Kubernetes Trainers

https://institute.sfeir.com/en/linux-foundation-certified-instructors/

Legal & Quality

Quality & Qualiopi

https://institute.sfeir.com/en/quality/

Accessibility & Disability

https://institute.sfeir.com/en/accessibility/

https://institute.sfeir.com/en/complaints/

Internal Rules

https://institute.sfeir.com/en/internal-rules/

Terms & Conditions

https://institute.sfeir.com/en/terms-and-conditions/

The Qualiopi certification has been awarded for the following category of action: Training Actions for the SFEIR training organization.

© 2025 SFEIR Institute. Part of SFEIR Group.

Privacy Policy

https://institute.sfeir.com/en/privacy-policy/

Legal Notice

https://institute.sfeir.com/en/legal-notice/

- Designed with ❤ by SFEIR

Privacy Matters

We use Matomo Analytics to improve your experience. These cookies help us understand how you use our site. You can accept or decline at any time.

https://institute.sfeir.com/en/privacy-policy/

Accept Decline

