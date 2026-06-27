---
sourceFile: "JupyterHub — JupyterHub documentation"
exportedBy: "Kortex"
exportDate: "2026-06-26T04:27:51.416Z"
---

# JupyterHub — JupyterHub documentation

a1d5bd2e-b588-4bed-8948-001b4256460a

JupyterHub — JupyterHub documentation

ea55a4eb-d282-41b4-8c26-76ba3fe4fb7f

https://jupyterhub.readthedocs.io/en/latest

JupyterHub — JupyterHub documentation

Skip to main content

https://jupyterhub.readthedocs.io/en/latest#main-content

Back to top

JupyterHub documentation - HomeJupyterHub documentation - Home

https://jupyterhub.readthedocs.io/en/latest

https://jupyterhub.readthedocs.io/en/tutorial/index.html

https://jupyterhub.readthedocs.io/en/howto/index.html

Explanation

https://jupyterhub.readthedocs.io/en/explanation/index.html

https://jupyterhub.readthedocs.io/en/reference/index.html

https://jupyterhub.readthedocs.io/en/faq/index.html

Contributing

https://jupyterhub.readthedocs.io/en/contributing/index.html

System Settings

https://github.com/jupyterhub/jupyterhub

https://discourse.jupyter.org/

Team Compass

https://jupyterhub-team-compass.readthedocs.io/en/latest/

https://jupyterhub.readthedocs.io/en/tutorial/index.html

https://jupyterhub.readthedocs.io/en/howto/index.html

Explanation

https://jupyterhub.readthedocs.io/en/explanation/index.html

https://jupyterhub.readthedocs.io/en/reference/index.html

https://jupyterhub.readthedocs.io/en/faq/index.html

Contributing

https://jupyterhub.readthedocs.io/en/contributing/index.html

System Settings

https://github.com/jupyterhub/jupyterhub

https://discourse.jupyter.org/

Team Compass

https://jupyterhub-team-compass.readthedocs.io/en/latest/

$ lightcone run "what can I do for you?" — agents that actually act. Try the API →

https://server.ethicalads.io/proxy/click/10604/019f0192-d7e3-7cc2-8923-8ac28f3f32ae/

Ad by EthicalAds

https://www.ethicalads.io/advertisers/topics/data-science/?ref=rtd-sidebar-buy-ads

https://jupyterhub.readthedocs.io/en/latest#jupyterhub

https://github.com/jupyterhub/jupyterhub

is the best way to serve

Jupyter notebook

https://jupyter-notebook.readthedocs.io/en/latest/

for multiple users. Because JupyterHub manages a separate Jupyter environment for each user, it can be used in a class of students, a corporate data science group, or a scientific research group. It is a multi-user

that spawns, manages, and proxies multiple instances of the single-user

Jupyter notebook

https://jupyter-notebook.readthedocs.io/en/latest/

Distributions

https://jupyterhub.readthedocs.io/en/latest#distributions

JupyterHub can be used in a collaborative environment by both small (0-100 users) and large teams (more than 100 users) such as a class of students, corporate data science group or scientific research group. It has two main distributions which are developed to serve the needs of each of these teams respectively.

The Littlest JupyterHub

https://github.com/jupyterhub/the-littlest-jupyterhub

distribution is suitable if you need a small number of users (1-100) and a single server with a simple environment.

Zero to JupyterHub with Kubernetes

https://github.com/jupyterhub/zero-to-jupyterhub-k8s

allows you to deploy dynamic servers on the cloud if you need even more users. This distribution runs JupyterHub on top of

https://kubernetes.io/

It is important to evaluate these distributions before you can continue with the configuration of JupyterHub.

https://jupyterhub.readthedocs.io/en/latest#subsystems

#### JupyterHub is made up of four subsystems:

(tornado process) that is the heart of JupyterHub

configurable http proxy

(node-http-proxy) that receives the requests from the client's browser

single-user Jupyter notebook servers

(Python/IPython/tornado) that are monitored by Spawners

authentication class

that manages how users can access the system

Additionally, optional configurations can be added through a

file and manage users kernels on an admin panel. A simplification of the whole system is displayed in the figure below:

#### JupyterHub performs the following functions:

The Hub launches a proxy

The proxy forwards all requests to the Hub by default

The Hub handles user login and spawns single-user servers on demand

The Hub configures the proxy to forward URL prefixes to the single-user notebook servers

For convenient administration of the Hub, its users, and services, JupyterHub also provides a

https://jupyterhub.readthedocs.io/en/reference/rest-api.html

The JupyterHub team and Project Jupyter value our community, and JupyterHub follows the Jupyter

Community Guides

https://docs.jupyter.org/en/latest/community/content-community.html

Documentation structure

https://jupyterhub.readthedocs.io/en/latest#documentation-structure

https://jupyterhub.readthedocs.io/en/latest#tutorials

This section of the documentation contains step-by-step tutorials that help outline the capabilities of JupyterHub and how you can achieve specific aims, such as installing it. The tutorials are recommended if you do not have much experience with JupyterHub.

https://jupyterhub.readthedocs.io/en/tutorial/index.html

Installation

https://jupyterhub.readthedocs.io/en/tutorial/index.html#installation

Getting Started

https://jupyterhub.readthedocs.io/en/tutorial/index.html#getting-started

Working with the JupyterHub API

https://jupyterhub.readthedocs.io/en/tutorial/index.html#working-with-the-jupyterhub-api

Configuration

https://jupyterhub.readthedocs.io/en/tutorial/index.html#configuration

How-to guides

https://jupyterhub.readthedocs.io/en/latest#how-to-guides

guides provide more in-depth details than the tutorials. They are recommended for those already familiar with JupyterHub and have a specific goal. The guides help answer the question

“How do I …?”

based on a particular topic.

https://jupyterhub.readthedocs.io/en/howto/index.html

Deploying JupyterHub in “API only mode”

https://jupyterhub.readthedocs.io/en/howto/api-only.html

Writing a custom Proxy implementation

https://jupyterhub.readthedocs.io/en/howto/proxy.html

Using JupyterHub's REST API

https://jupyterhub.readthedocs.io/en/howto/rest.html

Running proxy separately from the hub

https://jupyterhub.readthedocs.io/en/howto/separate-proxy.html

Working with templates and UI

https://jupyterhub.readthedocs.io/en/howto/templates.html

Upgrading JupyterHub

https://jupyterhub.readthedocs.io/en/howto/upgrading.html

Interpreting common log messages

https://jupyterhub.readthedocs.io/en/howto/log-messages.html

Logging users in via URL

https://jupyterhub.readthedocs.io/en/howto/forced-login.html

Configuration

https://jupyterhub.readthedocs.io/en/howto/index.html#configuration

Explanation

https://jupyterhub.readthedocs.io/en/latest#explanation

Explanation

section provides further details that can be used to better understand JupyterHub, such as how it can be used and configured. They are intended for those seeking to expand their knowledge of JupyterHub.

Explanation

https://jupyterhub.readthedocs.io/en/explanation/index.html

JupyterHub: A conceptual overview

https://jupyterhub.readthedocs.io/en/explanation/concepts.html

Capacity planning

https://jupyterhub.readthedocs.io/en/explanation/capacity-planning.html

The Hub's Database

https://jupyterhub.readthedocs.io/en/explanation/database.html

Security Overview

https://jupyterhub.readthedocs.io/en/explanation/websecurity.html

JupyterHub and OAuth

https://jupyterhub.readthedocs.io/en/explanation/oauth.html

The JupyterHub single-user server

https://jupyterhub.readthedocs.io/en/explanation/singleuser.html

JupyterHub RBAC

https://jupyterhub.readthedocs.io/en/rbac/index.html

https://jupyterhub.readthedocs.io/en/latest#reference

section provides technical information about JupyterHub, such as monitoring the state of your installation and working with JupyterHub's API modules and classes.

https://jupyterhub.readthedocs.io/en/reference/index.html

Technical Overview

https://jupyterhub.readthedocs.io/en/reference/technical-overview.html

Authenticators

https://jupyterhub.readthedocs.io/en/reference/authenticators.html

https://jupyterhub.readthedocs.io/en/reference/spawners.html

Configuration Reference

https://jupyterhub.readthedocs.io/en/reference/config-reference.html

https://jupyterhub.readthedocs.io/en/reference/services.html

JupyterHub URL scheme

https://jupyterhub.readthedocs.io/en/reference/urls.html

Event logging and telemetry

https://jupyterhub.readthedocs.io/en/reference/event-logging.html

https://jupyterhub.readthedocs.io/en/reference/monitoring.html

Sharing access to user servers

https://jupyterhub.readthedocs.io/en/reference/sharing.html

A Gallery of JupyterHub Deployments

https://jupyterhub.readthedocs.io/en/reference/gallery-jhub-deployments.html

https://jupyterhub.readthedocs.io/en/reference/changelog.html

JupyterHub REST API

https://jupyterhub.readthedocs.io/en/reference/rest-api.html

JupyterHub API Reference

https://jupyterhub.readthedocs.io/en/reference/api/index.html

Frequently asked questions

https://jupyterhub.readthedocs.io/en/latest#frequently-asked-questions

Find answers to the most frequently asked questions about JupyterHub such as how to troubleshoot an issue.

https://jupyterhub.readthedocs.io/en/faq/index.html

Frequently asked questions

https://jupyterhub.readthedocs.io/en/faq/faq.html

Institutional FAQ

https://jupyterhub.readthedocs.io/en/faq/institutional-faq.html

Troubleshooting

https://jupyterhub.readthedocs.io/en/faq/troubleshooting.html

Contributing

https://jupyterhub.readthedocs.io/en/latest#contributing

JupyterHub welcomes all contributors, whether you are new to the project or know your way around. The

Contributing

section provides information on how you can make your contributions.

Contributing

https://jupyterhub.readthedocs.io/en/contributing/index.html

Community communication channels

https://jupyterhub.readthedocs.io/en/contributing/community.html

Setting up a development install

https://jupyterhub.readthedocs.io/en/contributing/setup.html

Contributing Documentation

https://jupyterhub.readthedocs.io/en/contributing/docs.html

Testing JupyterHub and linting code

https://jupyterhub.readthedocs.io/en/contributing/tests.html

The JupyterHub roadmap

https://jupyterhub.readthedocs.io/en/contributing/roadmap.html

Reporting security issues in Jupyter or JupyterHub

https://jupyterhub.readthedocs.io/en/contributing/security.html

Indices and tables

https://jupyterhub.readthedocs.io/en/latest#indices-and-tables

https://jupyterhub.readthedocs.io/en/genindex.html

Module Index

https://jupyterhub.readthedocs.io/en/py-modindex.html

Questions? Suggestions?

https://jupyterhub.readthedocs.io/en/latest#questions-suggestions

All questions and suggestions are welcome. Please feel free to use our

Jupyter Discourse Forum

https://discourse.jupyter.org/

to contact our team.

Looking forward to hearing from you!

next Tutorials

https://jupyterhub.readthedocs.io/en/tutorial/index.html

On this page

Distributions

https://jupyterhub.readthedocs.io/en/latest#distributions

https://jupyterhub.readthedocs.io/en/latest#subsystems

Documentation structure

https://jupyterhub.readthedocs.io/en/latest#documentation-structure

https://jupyterhub.readthedocs.io/en/latest#tutorials

How-to guides

https://jupyterhub.readthedocs.io/en/latest#how-to-guides

Explanation

https://jupyterhub.readthedocs.io/en/latest#explanation

https://jupyterhub.readthedocs.io/en/latest#reference

Frequently asked questions

https://jupyterhub.readthedocs.io/en/latest#frequently-asked-questions

Contributing

https://jupyterhub.readthedocs.io/en/latest#contributing

Indices and tables

https://jupyterhub.readthedocs.io/en/latest#indices-and-tables

Questions? Suggestions?

https://jupyterhub.readthedocs.io/en/latest#questions-suggestions

Edit on GitHub

https://github.com/jupyterhub/jupyterhub/edit/main/docs/source/index.md

Show Source

https://jupyterhub.readthedocs.io/en/\_sources/index.md.txt

© Copyright 2026, Project Jupyter Contributors.

Created using

https://www.sphinx-doc.org/

Built with the

PyData Sphinx Theme

https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html

https://jupyterhub.readthedocs.io/en/stable/

https://jupyterhub.readthedocs.io/en/5.5.0/

https://jupyterhub.readthedocs.io/en/5.4.0/

https://jupyterhub.readthedocs.io/en/5.3.0/

https://jupyterhub.readthedocs.io/en/5.2.1/

https://jupyterhub.readthedocs.io/en/5.2.0/

https://jupyterhub.readthedocs.io/en/5.1.0/

https://jupyterhub.readthedocs.io/en/5.0.0/

https://jupyterhub.readthedocs.io/en/4.x/

https://jupyterhub.readthedocs.io/en/4.1.5/

https://jupyterhub.readthedocs.io/en/4.1.4/

https://jupyterhub.readthedocs.io/en/4.1.3/

https://jupyterhub.readthedocs.io/en/4.1.2/

https://jupyterhub.readthedocs.io/en/4.1.1/

https://jupyterhub.readthedocs.io/en/4.1.0/

https://jupyterhub.readthedocs.io/en/4.0.2/

https://jupyterhub.readthedocs.io/en/4.0.1/

https://jupyterhub.readthedocs.io/en/4.0.0/

https://jupyterhub.readthedocs.io/en/3.1.1/

https://jupyterhub.readthedocs.io/en/3.1.0/

https://jupyterhub.readthedocs.io/en/3.0.0/

https://jupyterhub.readthedocs.io/en/2.3.1/

https://jupyterhub.readthedocs.io/en/2.3.0/

https://jupyterhub.readthedocs.io/en/2.2.2/

https://jupyterhub.readthedocs.io/en/2.2.1/

https://jupyterhub.readthedocs.io/en/2.2.0/

https://jupyterhub.readthedocs.io/en/2.1.1/

https://jupyterhub.readthedocs.io/en/2.1.0/

https://jupyterhub.readthedocs.io/en/2.0.2/

https://jupyterhub.readthedocs.io/en/2.0.1/

https://jupyterhub.readthedocs.io/en/2.0.0/

https://jupyterhub.readthedocs.io/en/1.5.0/

https://jupyterhub.readthedocs.io/en/1.4.2/

https://jupyterhub.readthedocs.io/en/1.2.2/

https://jupyterhub.readthedocs.io/en/1.2.1/

https://jupyterhub.readthedocs.io/en/1.2.0/

https://jupyterhub.readthedocs.io/en/1.1.0/

https://jupyterhub.readthedocs.io/en/1.0.0/

https://jupyterhub.readthedocs.io/en/0.9.5/

https://jupyterhub.readthedocs.io/en/0.9.4/

https://jupyterhub.readthedocs.io/en/0.9.3/

https://jupyterhub.readthedocs.io/en/0.9.2/

https://jupyterhub.readthedocs.io/en/0.9.1/

https://jupyterhub.readthedocs.io/en/0.9.0/

https://jupyterhub.readthedocs.io/en/0.8.1/

https://jupyterhub.readthedocs.io/en/0.8.0/

https://jupyterhub.readthedocs.io/en/0.7.2/

https://jupyterhub.readthedocs.io/en/0.7.1/

https://jupyterhub.readthedocs.io/en/0.7.0/

https://jupyterhub.readthedocs.io/en/0.6.1/

https://jupyterhub.readthedocs.io/\_/downloads/en/latest/htmlzip/

On Read the Docs

Project Home

https://app.readthedocs.org/projects/jupyterhub/?utm\_source=jupyterhub&utm\_content=flyout

https://app.readthedocs.org/projects/jupyterhub/builds/?utm\_source=jupyterhub&utm\_content=flyout

Addons documentation

https://docs.readthedocs.io/page/addons.html?utm\_source=jupyterhub&utm\_content=flyout

― Hosted by

Read the Docs

https://about.readthedocs.com/?utm\_source=jupyterhub&utm\_content=flyout

No recent searches

to navigate

Search powered by

