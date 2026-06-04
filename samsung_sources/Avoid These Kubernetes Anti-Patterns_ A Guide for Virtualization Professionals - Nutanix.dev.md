---
sourceFile: "Avoid These Kubernetes Anti-Patterns: A Guide for Virtualization Professionals - Nutanix.dev"
exportedBy: "Kortex"
exportDate: "2026-05-20T06:50:17.261Z"
---

# Avoid These Kubernetes Anti-Patterns: A Guide for Virtualization Professionals - Nutanix.dev

51426c03-2508-4d00-8f1d-4be99a9a866f

Avoid These Kubernetes Anti-Patterns: A Guide for Virtualization Professionals - Nutanix.dev

e1105d47-9c47-4b09-8c6a-3504529164be

https://www.nutanix.dev/2026/04/01/avoid-these-kubernetes-anti-patterns-a-guide-for-virtualization-professionals/

Avoid These Kubernetes Anti-Patterns: A Guide for Virtualization Professionals – Nutanix.dev

Nutanix.dev

https://www.nutanix.dev/

API Reference

https://www.nutanix.dev/api-reference

https://www.nutanix.dev/blog/

https://www.nutanix.dev/labs

Code Samples

https://www.nutanix.dev/2026/04/01/avoid-these-kubernetes-anti-patterns-a-guide-for-virtualization-professionals/

Grouped by Language

https://www.nutanix.dev/code\_samples

Single Page (All Code Samples)

https://www.nutanix.dev/code-samples-all

NutanixDev on GitHub

https://github.com/nutanixdev

Nutanix on GitHub

https://github.com/nutanix

https://www.nutanix.dev/2026/04/01/avoid-these-kubernetes-anti-patterns-a-guide-for-virtualization-professionals/

NCM Self Service DSL

https://www.nutanix.dev/self-service-dsl/

Playbooks Library

https://www.nutanix.dev/playbooks

Nutanix Bible

https://nutanixbible.com/

Hamburger Toggle Menu

Avoid These Kubernetes Anti-Patterns: A Guide for Virtualization Professionals

By Jose Gomez, Director Technical Marketing Engineering, NKP and Enterprise AI

April 1, 2026

https://www.nutanix.dev/2026/04/01/

Terms Of Use

https://www.nutanix.com/legal/terms-of-use

Table of Contents

Avoid These Kubernetes Anti-Patterns: A Guide for Virtualization Professionals

https://www.nutanix.dev/2026/04/01/avoid-these-kubernetes-anti-patterns-a-guide-for-virtualization-professionals/#elementor-toc\_\_heading-anchor-0

At a Glance: The Mindset Shift

https://www.nutanix.dev/2026/04/01/avoid-these-kubernetes-anti-patterns-a-guide-for-virtualization-professionals/#elementor-toc\_\_heading-anchor-1

Anti-Pattern 1 — Backing Up Nodes Instead of Protecting State

https://www.nutanix.dev/2026/04/01/avoid-these-kubernetes-anti-patterns-a-guide-for-virtualization-professionals/#elementor-toc\_\_heading-anchor-2

Anti-Pattern 2 — Manual SSH for Fixes Instead of Declarative Automation

https://www.nutanix.dev/2026/04/01/avoid-these-kubernetes-anti-patterns-a-guide-for-virtualization-professionals/#elementor-toc\_\_heading-anchor-3

Anti-Pattern 3 — CLI Push Instead of GitOps Pull

https://www.nutanix.dev/2026/04/01/avoid-these-kubernetes-anti-patterns-a-guide-for-virtualization-professionals/#elementor-toc\_\_heading-anchor-4

Anti-Pattern 4 — Static IPs Instead of Dynamic IPAM

https://www.nutanix.dev/2026/04/01/avoid-these-kubernetes-anti-patterns-a-guide-for-virtualization-professionals/#elementor-toc\_\_heading-anchor-5

Anti-Pattern 5 — Stretched Clusters Instead of Multi-Cluster DR

https://www.nutanix.dev/2026/04/01/avoid-these-kubernetes-anti-patterns-a-guide-for-virtualization-professionals/#elementor-toc\_\_heading-anchor-6

Anti-Pattern 6 — cluster-admin Instead of RBAC

https://www.nutanix.dev/2026/04/01/avoid-these-kubernetes-anti-patterns-a-guide-for-virtualization-professionals/#elementor-toc\_\_heading-anchor-7

Anti-Pattern 7 — Self-Signed Certs Instead of Automated PKI

https://www.nutanix.dev/2026/04/01/avoid-these-kubernetes-anti-patterns-a-guide-for-virtualization-professionals/#elementor-toc\_\_heading-anchor-8

Anti-Pattern 8 — Local Disks Instead of Persistent Storage

https://www.nutanix.dev/2026/04/01/avoid-these-kubernetes-anti-patterns-a-guide-for-virtualization-professionals/#elementor-toc\_\_heading-anchor-9

Frequently Asked Questions

https://www.nutanix.dev/2026/04/01/avoid-these-kubernetes-anti-patterns-a-guide-for-virtualization-professionals/#elementor-toc\_\_heading-anchor-10

https://www.nutanix.dev/2026/04/01/avoid-these-kubernetes-anti-patterns-a-guide-for-virtualization-professionals/#elementor-toc\_\_heading-anchor-11

If you're a virtualization or infrastructure administrator moving into Kubernetes, the biggest challenge isn't learning new tools; it's treating Kubernetes like a form of virtualization using VM-style operations.

Nutanix Kubernetes Platform (NKP)

https://www.nutanix.com/products/kubernetes-management-platform

is a CNCF-certified, 100% upstream-compatible Kubernetes platform designed to help platform teams transition from VM-style operations to fully automated, declarative platform engineering. NKP bundles lifecycle management, GitOps, disaster recovery, storage, networking, security, and multi-cluster operations into a single supported distribution, eliminating the need to assemble and operate a large DIY Kubernetes toolchain.

These practices are often referred to as

Day-2 Kubernetes operations

Kubernetes lifecycle management

platform engineering best practices

Before we dive into the anti-patterns, here are the most important mindset shifts to keep in mind.

Kubernetes nodes are

immutable and replaceable

, not assets to restore.

GitOps should be the

primary deployment model

, not manual

Production Kubernetes requires

multi-cluster disaster recovery

, not stretched clusters.

Enterprise Kubernetes platforms should include

RBAC, PKI, storage, and lifecycle automation

out of the box.

Let's walk through the anti-patterns we encounter most often when VM operations meet Kubernetes.

At a Glance: The Mindset Shift

Anti-Pattern

Risk Introduced

NKP Capability

Operational Outcome

VM snapshots for nodes

Configuration drift and failed restores

Cluster API lifecycle

Nodes replaced automatically

SSHing into nodes

Drift and non-reproducible fixes

Declarative config with CAPI

Consistent fleet configuration

“kubectl apply” deployments

No audit trail

Built-in Flux CD GitOps

Self-healing deployments

Static node IPs

Scale-out and upgrade failures

Dynamic IPAM and load balancing

Safe scaling and upgrades

Stretched clusters

etcd quorum risk

Multi-cluster DR with NDK

Site-level resiliency

“cluster-admin” everywhere

High blast radius

RBAC roles + IdP integration

Secure multi-tenancy

Manual certificates

Expiry outages

Auto-renewal with cert-manager

Automated PKI lifecycle

Local node storage

Nutanix CSI + NDK

Durable persistent storage

Anti-Pattern 1 — Backing Up Nodes Instead of Protecting State

#### The Anti-Pattern:

Treating a Kubernetes node like a traditional VM by taking snapshots and backups. In virtualization, a failed server is “restored” from a snapshot. In Kubernetes, nodes are

cattle, not pets

. The node itself is a disposable resource; its “soul” lives in

etcd and persistent storage

, not the local OS disk. Restoring node snapshots is not recommended, as it can introduce configuration drift and potentially destabilize the cluster.

Do this instead

#### Protect what actually matters:

#### The cluster state:

Back up your

database using

(included with NKP).

#### The application data:

Nutanix Data Services for Kubernetes (NDK)

to provide enterprise-grade storage-layer replication for your persistent volumes.

For your nodes

Nutanix Kubernetes Platform (NKP)

Cluster API (CAPI)

to manage the machine lifecycle. Instead of “restoring” an old snapshot, NKP uses a declarative manifest to define the desired state. If a node fails, CAPI simply deploys a fresh copy based on your defined OS image template.

The following snippet is an excerpt that describes the topology of an NKP cluster.

\[...\]
topology:
  controlPlane:
    replicas: 3
  variables:
    - name: clusterConfig
      value:
        nutanix:
          machineDetails:
            image:
              name: nkp-ubuntu-24.04-release-cis-gpu-1.34.1
            memorySize: 16Gi
            systemDiskSize: 80Gi
            vcpuSockets: 4
\[...\]

Anti-Pattern 2 — Manual SSH for Fixes Instead of Declarative Automation

#### The Anti-Pattern:

Logging into nodes to manually “fix” configurations or restart runtimes. Manual intervention creates

configuration drift

. Your manual fixes won't be applied to new nodes created during a scale-out or upgrade.

What is declarative automation?

In the VM world, we often use

commands (e.g.,

“Step 1: SSH in. Step 2: Update the config. Step 3: Restart.”

Declarative automation

flips this: you simply define the

desired state

“This node must have this specific OS version and memory.”

). The system (Kubernetes) then works continuously to ensure the current state always matches that definition. If a node drifts, the system automatically fixes it.

Do this instead

NKP treats nodes as declarative objects. If you need an OS-level change, update the NKP Cluster configuration.

ensures every node in the fleet matches that spec automatically.

: For collecting logs for troubleshooting or opening a support case, use

nkp diagnose

Anti-Pattern 3 — CLI Push Instead of GitOps Pull

#### The Anti-Pattern:

kubectl apply -f

as your primary deployment method. Manual “pushes” create a single point of truth failure and leave no audit trail.

What is GitOps?

Think of GitOps as “Infrastructure as Code” but with an autopilot.

You store your desired cluster state (YAML files) in a Git repository.

A software agent in your cluster (e.g., Flux) continuously compares the

cluster's actual state

state in Git.

If there is a difference (e.g., you commit a change or the cluster drifts), the agent automatically updates the cluster to match the Git state. No manual commands required.

Do this instead

Version control everything. Let Git be your “Undo” button.

In NKP, Flux CD is delivered as a supported, preconfigured component, enabling immediate GitOps adoption without additional platform integration work.

The following YAML is an example of a

GitRepository

resource in NKP that Flux is “watching” and synchronizes the cluster to keep it up to date.

apiVersion: source.toolkit.fluxcd.io/v1
kind: GitRepository
metadata:
  name: nkp-demo-catalog-applications
  namespace: kommander
spec:
  interval: 1m0s
  ref:
    branch: main
  timeout: 1m0s
  url: https://github.com/nutanixdev/nkp-demo-catalog-applications

Anti-Pattern 4 — Static IPs Instead of Dynamic IPAM

#### The Anti-Pattern:

Manually configuring static IP addresses on the node OS. Hardcoding IPs prevents auto-scaling and self-healing.

Why are static IPs a scaling and upgrade bottleneck?

In a virtualized environment, a server might keep its IP for years. In Kubernetes, nodes are ephemeral and frequently cycled. Designing for static IPs introduces three major risks:

#### The scaling friction:

Every time you want to scale out, you must manually “carve out” IPs from your subnet and hardcode them into your automation. This prevents the

Cluster Autoscaler

from working autonomously.

#### The upgrade trap:

During a cluster upgrade, NKP uses a

rolling update

strategy. Before CAPI decommissions an old node, it must deploy a brand-new node to prevent a capacity drop. If you are using static IPs, you must have additional addresses pre-reserved and ready for these new nodes, or the upgrade will fail for lack of available IPs.

#### The blast radius:

If a node fails, its replacement shouldn't have to wait for a human to reassign a “fixed” address. Static designs turn a sub-second self-healing process into a manual ticket.

Do this instead

Only use static IPs for the

control plane VIP

load balancer pool

(managed via

, included in NKP).

for your nodes. In NKP, you define an IP pool, and the platform handles the “plumbing.”

Anti-Pattern 5 — Stretched Clusters Instead of Multi-Cluster DR

#### The Anti-Pattern:

Stretching a single cluster across two sites for disaster avoidance. While this works for VMs, it creates a single point of failure (SPOF) in the

etcd quorum

. High latency between sites can take down your entire cluster API.

As a rule of thumb, Kubernetes clusters should remain

single-site control planes

. Site-level resilience should be achieved using

multiple independent clusters and replicated data

, not a stretched etcd quorum.

Do this instead

Detect site failures via

global server load balancing

(GSLB) and reroute traffic to a completely independent, healthy Kubernetes cluster.

While NKP components can be deployed across multiple failure domains, this often creates an SPOF if not well-architected. Instead, use a

multi-cluster, replicated-data

strategy. Deploy independent clusters at sites A and B. Use NDK for synchronous or asynchronous volume replication.

Tap to unmute

Your browser can't play this video.

https://www.youtube.com/supported\_browsers

https://www.youtube.com/

An error occurred.

Try watching this video on www.youtube.com

https://www.youtube.com/watch?v=1lHEgyf8JRY

, or enable JavaScript if it is disabled in your browser.

Anti-Pattern 6 — cluster-admin Instead of RBAC

#### The Anti-Pattern:

Using the high-privileged

cluster-admin

role for daily operations. An exposed admin token is far more dangerous than a stolen password; it can wipe your entire fleet of clusters in seconds.

Do this instead

Use Kubernetes roles to sandbox developers and automated processes, ensuring they see only what they need.

Multi-Tenancy

eliminates the complexity of manual Role-Based Access Control (RBAC) by providing a

library of pre-defined common roles

. Instead of writing complex security policies from scratch, you can apply curated permissions to

(for clusters) or

(for namespaces) directly from the UI.

NKP integrates with your existing identity providers (

Active Directory, Okta, GitHub, …

), allowing you to delegate admin power to specific project teams without ever handing over the “keys to the kingdom.”

Anti-Pattern 7 — Self-Signed Certs Instead of Automated PKI

#### The Anti-Pattern:

Manually generating self-signed certificates or ignoring expiration dates. Internal Kubernetes communication (API to Kubelet) relies on TLS. If a cert expires, the cluster goes “brain dead.”

Do this instead

Connect your cluster to a trusted CA (like your internal CA or Let's Encrypt).

NKP includes

cert-manager

, the industry standard for certificate lifecycle management. It automatically requests, issues, and renews certificates before they expire.

Anti-Pattern 8 — Local Disks Instead of Persistent Storage

#### The Anti-Pattern:

Avoiding stateful apps because containers are “ephemeral” or writing data to local node disks. If a pod restarts in a new node, local data is lost.

Do this instead

Persistent Volume Claims (PVCs)

backed by a storage backend and let the

StorageClass

handle disk provisioning.

NKP uses a high-performance

to connect pods to Nutanix AOS storage. With

, your persistent volumes are not only durable but protected by enterprise-grade snapshots and replication.

Frequently Asked Questions

When is SSH acceptable?

Limit SSH to exceptional troubleshooting scenarios. Routine changes should be declarative.

Does NKP include GitOps?

Yes, Flux CD is integrated and ready to use.

Does NKP include DR and backups?

Yes, Velero for cluster state and NDK for persistent volumes.

Do I need cluster-admin?

No, NKP provides RBAC roles integrated with enterprise identity providers.

Can NKP run stateful apps?

Yes, with CSI and NDK providing durable storage.

How are node failures handled?

Failed nodes are automatically recreated from the cluster template by Cluster API.

Ready to evaluate how an integrated Kubernetes platform simplifies Day-2 operations?

A Cloud Native Playbook for Platform Engineers

https://www.nutanix.com/library/ebooks/cloud-native-playbook-for-platform-engineers

Start a Nutanix Kubernetes Platform Test Drive

https://cloud.nutanixtestdrive.com/login?source=one-platform&type=nkp

Kubernetes Lifecycle Management with NKP and Cluster API

https://www.youtube.com/watch?v=jT6N2c32ETE

https://www.nutanix.dev/tag/kubernetes/

https://www.nutanix.dev/tag/nkp/

©2026 Nutanix, Inc. All rights reserved. Nutanix, the Nutanix logo and all Nutanix product and service names mentioned herein are registered trademarks or trademarks of Nutanix, Inc. in the United States and other countries. Kubernetes is a registered trademark of The Linux Foundation in the United States and other countries. All other brand names mentioned herein are for identification purposes only and may be the trademarks of their respective holder(s).

Our decision to link to or reference an external site should not be considered an endorsement of any content on such a site. Certain information contained in this post may relate to, or be based on, studies, publications, surveys and other data obtained from third-party sources and our own internal estimates and research. While we believe these third-party studies, publications, surveys and other data are reliable as of the date of this paper, they have not independently verified unless specifically stated, and we make no representation as to the adequacy, fairness, accuracy, or completeness of any information obtained from a third-party.

Code samples, snippets and/or methods that appear in this content are unofficial, are unsupported and will require extensive modification before use in a production environment. As such, the code samples, snippets and/or methods are provided AS IS and are not guaranteed to be complete, accurate, or up-to-date. Nutanix makes no representations or warranties of any kind, express or implied, as to the operation or content of the code samples, snippets, or methods. Nutanix expressly disclaims all other guarantees, warranties, conditions and representations of any kind, either express or implied, and whether arising under any statute, law, commercial use or otherwise, including implied warranties of merchantability, fitness for a particular purpose, title and non-infringement therein.

This content may reflect an experiment in a test environment. Results, benefits, savings, or other outcomes described depend on a variety of factors including use case, individual requirements, and operating environments, and this publication should not be construed as a promise or obligation to deliver specific outcomes.

https://next.nutanix.com/

Code Samples

https://www.nutanix.dev/code\_samples

API Reference

https://www.nutanix.dev/api-reference

https://www.nutanix.dev/blog

https://www.nutanix.dev/labs

https://next.nutanix.com/

https://www.linkedin.com/showcase/33243621/

© Nutanix 2025

Terms of Use

https://www.nutanix.com/legal/terms-of-use

Privacy Statement

https://www.nutanix.com/legal/privacy-statement

Do Not Sell or Share My Personal Information

https://www.nutanix.com/legal/do-not-sell-my-personal-information

