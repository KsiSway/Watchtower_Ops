---
sourceFile: "Kubespawner — Kubespawner"
exportedBy: "Kortex"
exportDate: "2026-06-26T04:27:51.455Z"
---

# Kubespawner — Kubespawner

eb6e02cd-57ea-4b16-a795-0833f0760a7f

Kubespawner — Kubespawner

dd9f5606-5375-4094-8328-ca914d489b51

https://jupyterhub-kubespawner.readthedocs.io/en/latest/

Kubespawner — Kubespawner

Skip to main content

https://jupyterhub-kubespawner.readthedocs.io/en/latest/#main-content

Back to top

Kubespawner

https://jupyterhub-kubespawner.readthedocs.io/en/latest/

API Documentation

KubeSpawner

https://jupyterhub-kubespawner.readthedocs.io/en/latest/spawner.html

https://jupyterhub-kubespawner.readthedocs.io/en/latest/objects.html

https://jupyterhub-kubespawner.readthedocs.io/en/latest/reflector.html

Internal SSL

https://jupyterhub-kubespawner.readthedocs.io/en/latest/ssl.html

https://jupyterhub-kubespawner.readthedocs.io/en/latest/utils.html

Templated fields

https://jupyterhub-kubespawner.readthedocs.io/en/latest/templates.html

Changes in KubeSpawner

https://jupyterhub-kubespawner.readthedocs.io/en/latest/changelog.html

https://github.com/jupyterhub/kubespawner

Suggest edit

https://github.com/jupyterhub/kubespawner/edit/main/index.md

https://github.com/jupyterhub/kubespawner/issues/new?title=Issue%20on%20page%20%2Findex.html&body=Your%20issue%20content%20here.

https://jupyterhub-kubespawner.readthedocs.io/en/latest/\_sources/index.md

Kubespawner

https://jupyterhub-kubespawner.readthedocs.io/en/latest/#features

Requirements

https://jupyterhub-kubespawner.readthedocs.io/en/latest/#requirements

https://jupyterhub-kubespawner.readthedocs.io/en/latest/#kubernetes

Kubespawner

https://jupyterhub-kubespawner.readthedocs.io/en/latest/#kubespawner

kubespawner

(also known as the JupyterHub Kubernetes Spawner) enables JupyterHub to spawn single-user notebook servers on a

https://kubernetes.io/

https://jupyterhub-kubespawner.readthedocs.io/en/latest/#features

Kubernetes is an open-source system for automating deployment, scaling, and management of containerized applications. If you want to run a JupyterHub setup that needs to scale across multiple nodes (anything with over ~50 simultaneous users), Kubernetes is a wonderful way to do it. Features include:

Easily and elastically run anywhere between 2 and thousands of nodes with the same set of powerful abstractions. Scale up and down as required by simply adding or removing nodes.

Run JupyterHub itself inside Kubernetes easily. This allows you to manage many JupyterHub deployments with only Kubernetes, without requiring an extra layer of Ansible / Puppet / Bash scripts. This also provides easy integrated monitoring and failover for the hub process itself.

Spawn multiple hubs in the same kubernetes cluster, with support for

https://kubernetes.io/docs/tasks/administer-cluster/namespaces/

. You can limit the amount of resources each namespace can use, effectively limiting the amount of resources a single JupyterHub (and its users) can use. This allows organizations to easily maintain multiple JupyterHubs with just one kubernetes cluster, allowing for easy maintenance & high resource utilization.

Provide guarantees and limits on the amount of resources (CPU / RAM) that single-user notebooks can use. Kubernetes has comprehensive

resource control

https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/

that can be used from the spawner.

Mount various types of

persistent volumes

https://kubernetes.io/docs/concepts/storage/persistent-volumes/

onto the single-user notebook's container.

Control various security parameters (such as userid/groupid, SELinux, etc) via flexible

Pod Security Policies

https://kubernetes.io/docs/concepts/policy/pod-security-policy/

Run easily in multiple clouds (or on your own machines). Helps avoid vendor lock-in. You can even spread out your cluster across

multiple clouds at the same time

https://kubernetes.io/docs/concepts/cluster-administration/federation/

Internal SSL configuration supported

In general, Kubernetes provides a ton of well thought out, useful features - and you can use all of them along with this spawner.

Requirements

https://jupyterhub-kubespawner.readthedocs.io/en/latest/#requirements

https://jupyterhub-kubespawner.readthedocs.io/en/latest/#kubernetes

Everything should work from Kubernetes v1.6+.

Kube DNS addon

https://kubernetes.io/docs/concepts/services-networking/connect-applications-service/#dns

is not strictly required - the spawner uses

environment variable

https://kubernetes.io/docs/concepts/services-networking/connect-applications-service/#environment-variables

based discovery instead. Your kubernetes cluster will need to be configured to support the types of volumes you want to use.

If you are just getting started and want a kubernetes cluster to play with,

Google Container Engine

https://cloud.google.com/kubernetes-engine/

is probably the nicest option. For AWS/Azure,

https://github.com/kubernetes/kops

is probably the way to go.

API Documentation

KubeSpawner

https://jupyterhub-kubespawner.readthedocs.io/en/latest/spawner.html

KubeSpawner

https://jupyterhub-kubespawner.readthedocs.io/en/latest/spawner.html#kubespawner.KubeSpawner

https://jupyterhub-kubespawner.readthedocs.io/en/latest/objects.html

https://jupyterhub-kubespawner.readthedocs.io/en/latest/objects.html#kubespawner.objects.make\_pod

https://jupyterhub-kubespawner.readthedocs.io/en/latest/objects.html#kubespawner.objects.make\_pvc

https://jupyterhub-kubespawner.readthedocs.io/en/latest/reflector.html

NamespacedResourceReflector

https://jupyterhub-kubespawner.readthedocs.io/en/latest/reflector.html#kubespawner.reflector.NamespacedResourceReflector

Internal SSL

https://jupyterhub-kubespawner.readthedocs.io/en/latest/ssl.html

https://jupyterhub-kubespawner.readthedocs.io/en/latest/ssl.html#setup

https://jupyterhub-kubespawner.readthedocs.io/en/latest/utils.html

generate\_hashed\_slug()

https://jupyterhub-kubespawner.readthedocs.io/en/latest/utils.html#kubespawner.utils.generate\_hashed\_slug

Templated fields

https://jupyterhub-kubespawner.readthedocs.io/en/latest/templates.html

templated properties

https://jupyterhub-kubespawner.readthedocs.io/en/latest/templates.html#templated-properties

https://jupyterhub-kubespawner.readthedocs.io/en/latest/templates.html#fields

Template tips

https://jupyterhub-kubespawner.readthedocs.io/en/latest/templates.html#template-tips

Changing template configuration

https://jupyterhub-kubespawner.readthedocs.io/en/latest/templates.html#changing-template-configuration

Upgrading from kubespawner < 7

https://jupyterhub-kubespawner.readthedocs.io/en/latest/templates.html#upgrading-from-kubespawner-7

Changes in KubeSpawner

https://jupyterhub-kubespawner.readthedocs.io/en/latest/changelog.html

https://jupyterhub-kubespawner.readthedocs.io/en/latest/changelog.html#unreleased

https://jupyterhub-kubespawner.readthedocs.io/en/latest/changelog.html#id1

https://jupyterhub-kubespawner.readthedocs.io/en/latest/changelog.html#id9

https://jupyterhub-kubespawner.readthedocs.io/en/latest/changelog.html#id16

https://jupyterhub-kubespawner.readthedocs.io/en/latest/changelog.html#id24

https://jupyterhub-kubespawner.readthedocs.io/en/latest/changelog.html#id33

https://jupyterhub-kubespawner.readthedocs.io/en/latest/changelog.html#id41

https://jupyterhub-kubespawner.readthedocs.io/en/latest/changelog.html#id47

https://jupyterhub-kubespawner.readthedocs.io/en/latest/changelog.html#id52

https://jupyterhub-kubespawner.readthedocs.io/en/latest/changelog.html#id60

https://jupyterhub-kubespawner.readthedocs.io/en/latest/changelog.html#id73

https://jupyterhub-kubespawner.readthedocs.io/en/latest/changelog.html#id81

https://jupyterhub-kubespawner.readthedocs.io/en/latest/changelog.html#id97

https://jupyterhub-kubespawner.readthedocs.io/en/latest/changelog.html#id106

https://jupyterhub-kubespawner.readthedocs.io/en/latest/changelog.html#id116

https://jupyterhub-kubespawner.readthedocs.io/en/latest/changelog.html#id122

https://jupyterhub-kubespawner.readthedocs.io/en/latest/changelog.html#id131

https://jupyterhub-kubespawner.readthedocs.io/en/latest/changelog.html#id135

https://jupyterhub-kubespawner.readthedocs.io/en/latest/changelog.html#id139

https://jupyterhub-kubespawner.readthedocs.io/en/latest/changelog.html#id147

https://jupyterhub-kubespawner.readthedocs.io/en/latest/changelog.html#id150

next KubeSpawner

https://jupyterhub-kubespawner.readthedocs.io/en/latest/spawner.html

https://jupyterhub-kubespawner.readthedocs.io/en/latest/#features

Requirements

https://jupyterhub-kubespawner.readthedocs.io/en/latest/#requirements

https://jupyterhub-kubespawner.readthedocs.io/en/latest/#kubernetes

By Project Jupyter Contributors

© Copyright 2026, Project Jupyter Contributors.

https://jupyterhub-kubespawner.readthedocs.io/en/stable/

https://jupyterhub-kubespawner.readthedocs.io/en/7.0.0/

https://jupyterhub-kubespawner.readthedocs.io/en/6.2.0/

https://jupyterhub-kubespawner.readthedocs.io/en/6.1.0/

https://jupyterhub-kubespawner.readthedocs.io/en/6.0.0/

https://jupyterhub-kubespawner.readthedocs.io/en/5.0.0/

https://jupyterhub-kubespawner.readthedocs.io/en/4.3.0/

https://jupyterhub-kubespawner.readthedocs.io/en/4.2.0/

https://jupyterhub-kubespawner.readthedocs.io/en/4.1.0/

https://jupyterhub-kubespawner.readthedocs.io/en/4.0.0/

https://jupyterhub-kubespawner.readthedocs.io/en/3.0.2/

https://jupyterhub-kubespawner.readthedocs.io/en/3.0.1/

https://jupyterhub-kubespawner.readthedocs.io/en/3.0.0/

https://jupyterhub-kubespawner.readthedocs.io/en/2.0.1/

https://jupyterhub-kubespawner.readthedocs.io/en/2.0.0/

https://jupyterhub-kubespawner.readthedocs.io/en/1.1.2/

https://jupyterhub-kubespawner.readthedocs.io/en/1.1.1/

https://jupyterhub-kubespawner.readthedocs.io/en/1.1.0/

https://jupyterhub-kubespawner.readthedocs.io/en/1.0.0/

https://jupyterhub-kubespawner.readthedocs.io/en/0.16.1/

https://jupyterhub-kubespawner.readthedocs.io/en/0.16.0/

https://jupyterhub-kubespawner.readthedocs.io/en/0.15.0/

https://jupyterhub-kubespawner.readthedocs.io/en/0.14.1/

https://jupyterhub-kubespawner.readthedocs.io/en/0.14.0/

https://jupyterhub-kubespawner.readthedocs.io/en/0.13.0/

https://jupyterhub-kubespawner.readthedocs.io/en/0.12.0/

https://jupyterhub-kubespawner.readthedocs.io/en/0.11.1/

https://jupyterhub-kubespawner.readthedocs.io/en/0.11.0/

On Read the Docs

Project Home

https://app.readthedocs.org/projects/jupyterhub-kubespawner/?utm\_source=jupyterhub-kubespawner&utm\_content=flyout

https://app.readthedocs.org/projects/jupyterhub-kubespawner/builds/?utm\_source=jupyterhub-kubespawner&utm\_content=flyout

Addons documentation

https://docs.readthedocs.io/page/addons.html?utm\_source=jupyterhub-kubespawner&utm\_content=flyout

― Hosted by

Read the Docs

https://about.readthedocs.com/?utm\_source=jupyterhub-kubespawner&utm\_content=flyout

Stop wasting tool calls See how you can use up to 80% fewer tokens with Airbyte Agents. Try it free

https://server.ethicalads.io/proxy/click/10569/019f0192-f7d5-7a22-b667-3b2fd4d2c749/

Ads by EthicalAds

https://www.ethicalads.io/advertisers/topics/data-science/?ref=ea-text

No recent searches

to navigate

Search powered by

