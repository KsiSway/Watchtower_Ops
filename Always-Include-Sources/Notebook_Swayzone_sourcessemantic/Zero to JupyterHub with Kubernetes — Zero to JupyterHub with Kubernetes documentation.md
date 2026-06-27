---
sourceFile: "Zero to JupyterHub with Kubernetes — Zero to JupyterHub with Kubernetes documentation"
exportedBy: "Kortex"
exportDate: "2026-06-26T04:27:51.699Z"
---

# Zero to JupyterHub with Kubernetes — Zero to JupyterHub with Kubernetes documentation

3797a556-0e29-4bc4-8b45-2b91fd91c8cc

Zero to JupyterHub with Kubernetes — Zero to JupyterHub with Kubernetes documentation

e1b6f93f-abf9-47dd-8693-0c5a6ddcf665

https://zero-to-jupyterhub.readthedocs.io/en/latest/

Zero to JupyterHub with Kubernetes — Zero to JupyterHub with Kubernetes documentation

Skip to main content

https://zero-to-jupyterhub.readthedocs.io/en/latest/#main-content

Back to top

Zero to JupyterHub with Kubernetes documentation - HomeZero to JupyterHub with Kubernetes documentation - Home

https://zero-to-jupyterhub.readthedocs.io/en/latest/

Setup Kubernetes

https://zero-to-jupyterhub.readthedocs.io/en/latest/kubernetes/index.html

Setup JupyterHub

https://zero-to-jupyterhub.readthedocs.io/en/latest/jupyterhub/index.html

Administrator Guide

https://zero-to-jupyterhub.readthedocs.io/en/latest/administrator/index.html

https://zero-to-jupyterhub.readthedocs.io/en/latest/resources/index.html

https://zero-to-jupyterhub.readthedocs.io/en/latest/changelog.html

https://github.com/jupyterhub/zero-to-jupyterhub-k8s/

Setup Kubernetes

https://zero-to-jupyterhub.readthedocs.io/en/latest/kubernetes/index.html

Setup JupyterHub

https://zero-to-jupyterhub.readthedocs.io/en/latest/jupyterhub/index.html

Administrator Guide

https://zero-to-jupyterhub.readthedocs.io/en/latest/administrator/index.html

https://zero-to-jupyterhub.readthedocs.io/en/latest/resources/index.html

https://zero-to-jupyterhub.readthedocs.io/en/latest/changelog.html

https://github.com/jupyterhub/zero-to-jupyterhub-k8s/

$ lightcone run "what can I do for you?" — agents that actually act. Try the API →

https://server.ethicalads.io/proxy/click/10604/019f0192-d7e3-7cc2-8923-8ac28f3f32ae/

Ad by EthicalAds

https://www.ethicalads.io/advertisers/topics/data-science/?ref=rtd-sidebar-buy-ads

Zero to JupyterHub with Kubernetes

https://zero-to-jupyterhub.readthedocs.io/en/latest/#zero-to-jupyterhub-with-kubernetes

https://github.com/jupyterhub/jupyterhub

allows users to interact with a computing environment through a webpage. As most devices have access to a web browser, JupyterHub makes it is easy to provide and standardize the computing environment for a group of people (e.g., for a class of students or an analytics team).

This project will help you set up your own JupyterHub on a cloud/on-prem k8s environment and leverage its scalable nature to support a large group of users. Thanks to

https://zero-to-jupyterhub.readthedocs.io/en/latest/resources/glossary.html#term-Kubernetes

, we are not tied to a specific cloud provider.

This project is under active development so information and tools may change.

You can be a part of this change!

If you see anything that is incorrect or have any questions, feel free to post on the community

Discourse forum

https://discourse.jupyter.org/

or reach out in the

https://jupyter.zulipchat.com/#narrow/channel/469744-jupyterhub

or create an issue at the

issues page

https://github.com/jupyterhub/zero-to-jupyterhub-k8s/issues

. If you have tips or deployments that you would like to share, see the

Community Resources section

https://zero-to-jupyterhub.readthedocs.io/en/latest/resources/community.html#community-resources

This documentation is for Helm chart version 5.0.0-0.dev.git.201.h08ea88e that deploys JupyterHub version 5.5.0 and other components versioned in

hub/images/requirements.txt

https://github.com/jupyterhub/zero-to-jupyterhub-k8s/blob/08ea88e/images/hub/requirements.txt

. The Helm chart requires Kubernetes version >=1.32.0 and Helm >=3.5.

What To Expect

https://zero-to-jupyterhub.readthedocs.io/en/latest/#what-to-expect

This guide will help you deploy and customize your own JupyterHub on a cloud. While doing this, you will gain valuable experience with:

A cloud provider

such as Google Cloud, Microsoft Azure, Amazon EC2, IBM Cloud…

to manage resources on the cloud

to configure and control the packaged JupyterHub installation

to give users access to a Jupyter computing environment

A terminal interface

on some operating system

#### It's also possible you end up getting some experience with:

to build customized image for the users

Domain registration

to make the hub available at

https://your-domain-name.com

https://your-domain-name.com/

For a more elaborate introduction to the tools and services that JupyterHub depends upon, see our

page about that

https://zero-to-jupyterhub.readthedocs.io/en/latest/resources/tools.html#tools

Setup Kubernetes

https://zero-to-jupyterhub.readthedocs.io/en/latest/#setup-kubernetes

This section describes a how to setup a Kubernetes cluster on a selection of cloud providers and environments, as well as initialize Helm, a Kubernetes package manager, to work with it.

Setup Kubernetes

https://zero-to-jupyterhub.readthedocs.io/en/latest/kubernetes/index.html

Setup Kubernetes

https://zero-to-jupyterhub.readthedocs.io/en/latest/kubernetes/setup-kubernetes.html

Setting up helm

https://zero-to-jupyterhub.readthedocs.io/en/latest/kubernetes/setup-helm.html

Setup JupyterHub

https://zero-to-jupyterhub.readthedocs.io/en/latest/#setup-jupyterhub

This tutorial starts from

Step Zero: Your Kubernetes cluster

and describes the steps needed for you to create a complete initial JupyterHub deployment. Please ensure you have a working installation of Kubernetes and Helm before proceeding with this section.

Setup JupyterHub

https://zero-to-jupyterhub.readthedocs.io/en/latest/jupyterhub/index.html

Installing JupyterHub

https://zero-to-jupyterhub.readthedocs.io/en/latest/jupyterhub/installation.html

Customization Guide

https://zero-to-jupyterhub.readthedocs.io/en/latest/jupyterhub/customization.html

Uninstalling JupyterHub

https://zero-to-jupyterhub.readthedocs.io/en/latest/jupyterhub/uninstall.html

JupyterHub can be configured and customized to fit a variety of deployment requirements. If you would like to expand JupyterHub, customize its setup, increase the computational resources available for users, or change authentication services, this guide will walk you through the steps. See the

Configuration Reference

https://zero-to-jupyterhub.readthedocs.io/en/latest/resources/reference.html#helm-chart-configuration-reference

for a list of frequently used configurable helm chart fields.

Administrator Guide

https://zero-to-jupyterhub.readthedocs.io/en/latest/#administrator-guide

This section provides information on managing and maintaining a staging or production deployment of JupyterHub. It has considerations for managing cloud-based deployments and tips for maintaining your deployment.

Administrator Guide

https://zero-to-jupyterhub.readthedocs.io/en/latest/administrator/index.html

The JupyterHub Architecture

https://zero-to-jupyterhub.readthedocs.io/en/latest/administrator/architecture.html

https://zero-to-jupyterhub.readthedocs.io/en/latest/administrator/debug.html

Authentication and authorization

https://zero-to-jupyterhub.readthedocs.io/en/latest/administrator/authentication.html

https://zero-to-jupyterhub.readthedocs.io/en/latest/administrator/services.html

Optimizations

https://zero-to-jupyterhub.readthedocs.io/en/latest/administrator/optimization.html

https://zero-to-jupyterhub.readthedocs.io/en/latest/administrator/security.html

Upgrading JupyterHub for Kubernetes

https://zero-to-jupyterhub.readthedocs.io/en/latest/administrator/upgrading/index.html

Customization Guide

https://zero-to-jupyterhub.readthedocs.io/en/latest/jupyterhub/customization.html

https://zero-to-jupyterhub.readthedocs.io/en/latest/administrator/troubleshooting.html

Advanced Topics

https://zero-to-jupyterhub.readthedocs.io/en/latest/administrator/advanced.html

Appendix: Projecting deployment costs

https://zero-to-jupyterhub.readthedocs.io/en/latest/administrator/cost.html

https://zero-to-jupyterhub.readthedocs.io/en/latest/#resources

This section holds all the references and resources that helped make this project what it is today.

https://zero-to-jupyterhub.readthedocs.io/en/latest/resources/index.html

Community Resources

https://zero-to-jupyterhub.readthedocs.io/en/latest/resources/community.html

Configuration Reference

https://zero-to-jupyterhub.readthedocs.io/en/latest/resources/reference.html

Related Projects

https://zero-to-jupyterhub.readthedocs.io/en/latest/resources/reference-docs.html

Utilized Tools

https://zero-to-jupyterhub.readthedocs.io/en/latest/resources/tools.html

https://zero-to-jupyterhub.readthedocs.io/en/latest/resources/glossary.html

Community Resources

https://zero-to-jupyterhub.readthedocs.io/en/latest/#community-resources

This section gives the community a space to provide information on setting up, managing, and maintaining JupyterHub.

We recognize that Kubernetes has many deployment options. As a project team with limited resources to provide end user support, we rely on community members to share their collective Kubernetes knowledge and JupyterHub experiences.

Contributing

If you would like to help improve this guide or Helm chart, please see the

issues page

https://github.com/jupyterhub/zero-to-jupyterhub-k8s/issues

as well as the

contributor guide

https://github.com/jupyterhub/zero-to-jupyterhub-k8s/blob/HEAD/CONTRIBUTING.md

We hope that you will use this section to share deployments with on a variety of infrastructure and for different use cases. There is also a

community maintained list

https://zero-to-jupyterhub.readthedocs.io/en/latest/resources/community.html#community-resources

of users of this Guide and the JupyterHub Helm Chart.

Institutional support

https://zero-to-jupyterhub.readthedocs.io/en/latest/#institutional-support

This guide and the associated helm chart would not be possible without the amazing institutional support from the following organizations (and the organizations that support them!)

UC Berkeley Data Science Division

https://cdss.berkeley.edu/

Berkeley Institute for Data Science

https://bids.berkeley.edu/

Cal Poly, San Luis Obispo

https://www.calpoly.edu/

Simula Research Institute

https://www.simula.no/

https://2i2c.org/

https://zero-to-jupyterhub.readthedocs.io/en/latest/#changelog

This section holds describes the changes between versions and how to upgrade between them.

https://zero-to-jupyterhub.readthedocs.io/en/latest/changelog.html

next Setup Kubernetes

https://zero-to-jupyterhub.readthedocs.io/en/latest/kubernetes/index.html

On this page

What To Expect

https://zero-to-jupyterhub.readthedocs.io/en/latest/#what-to-expect

Setup Kubernetes

https://zero-to-jupyterhub.readthedocs.io/en/latest/#setup-kubernetes

Setup JupyterHub

https://zero-to-jupyterhub.readthedocs.io/en/latest/#setup-jupyterhub

Administrator Guide

https://zero-to-jupyterhub.readthedocs.io/en/latest/#administrator-guide

https://zero-to-jupyterhub.readthedocs.io/en/latest/#resources

Community Resources

https://zero-to-jupyterhub.readthedocs.io/en/latest/#community-resources

Institutional support

https://zero-to-jupyterhub.readthedocs.io/en/latest/#institutional-support

https://zero-to-jupyterhub.readthedocs.io/en/latest/#changelog

Edit on GitHub

https://github.com/jupyterhub/zero-to-jupyterhub-k8s/edit/main/docs/source/index.md

Show Source

https://zero-to-jupyterhub.readthedocs.io/en/latest/\_sources/index.md.txt

© Copyright 2026, Project Jupyter Contributors.

Created using

https://www.sphinx-doc.org/

Built with the

PyData Sphinx Theme

https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html

https://z2jh.jupyter.org/en/stable/

https://z2jh.jupyter.org/en/4.4.0/

https://z2jh.jupyter.org/en/4.3.5/

https://z2jh.jupyter.org/en/4.3.4/

https://z2jh.jupyter.org/en/4.3.3/

https://z2jh.jupyter.org/en/4.3.2/

https://z2jh.jupyter.org/en/4.3.1/

https://z2jh.jupyter.org/en/4.3.0/

https://z2jh.jupyter.org/en/4.2.0/

https://z2jh.jupyter.org/en/4.1.0/

https://z2jh.jupyter.org/en/4.0.0/

https://z2jh.jupyter.org/en/3.3.8/

https://z2jh.jupyter.org/en/3.3.7/

https://z2jh.jupyter.org/en/3.3.6/

https://z2jh.jupyter.org/en/3.3.5/

https://z2jh.jupyter.org/en/3.3.4/

https://z2jh.jupyter.org/en/3.3.3/

https://z2jh.jupyter.org/en/3.3.2/

https://z2jh.jupyter.org/en/3.3.1/

https://z2jh.jupyter.org/en/3.3.0/

https://z2jh.jupyter.org/en/3.2.1/

https://z2jh.jupyter.org/en/3.2.0/

https://z2jh.jupyter.org/en/3.1.0/

https://z2jh.jupyter.org/en/3.0.3/

https://z2jh.jupyter.org/en/3.0.2/

https://z2jh.jupyter.org/en/3.0.1/

https://z2jh.jupyter.org/en/3.0.0/

https://z2jh.jupyter.org/en/2.0.0/

https://z2jh.jupyter.org/en/1.x/

https://z2jh.jupyter.org/en/1.0.x/

https://z2jh.jupyter.org/en/0.11.x/

https://z2jh.jupyter.org/en/0.10.x/

https://z2jh.jupyter.org/en/0.9.x/

On Read the Docs

Project Home

https://app.readthedocs.org/projects/zero-to-jupyterhub/?utm\_source=zero-to-jupyterhub&utm\_content=flyout

https://app.readthedocs.org/projects/zero-to-jupyterhub/builds/?utm\_source=zero-to-jupyterhub&utm\_content=flyout

Addons documentation

https://docs.readthedocs.io/page/addons.html?utm\_source=zero-to-jupyterhub&utm\_content=flyout

― Hosted by

Read the Docs

https://about.readthedocs.com/?utm\_source=zero-to-jupyterhub&utm\_content=flyout

No recent searches

to navigate

Search powered by

