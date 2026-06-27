---
sourceFile: "Configuration Overview — Jupyter Notebook 7.6.0 documentation"
exportedBy: "Kortex"
exportDate: "2026-06-26T04:27:51.174Z"
---

# Configuration Overview — Jupyter Notebook 7.6.0 documentation

cdd010e7-b025-4b9b-86fa-b69e9fbcd2ad

Configuration Overview — Jupyter Notebook 7.6.0 documentation

9f1b9904-85fd-43f2-86bd-416144ba8c1b

https://jupyter-notebook.readthedocs.io/en/stable/configuring/config\_overview.html

Configuration Overview — Jupyter Notebook 7.6.0 documentation

Skip to main content

https://jupyter-notebook.readthedocs.io/en/stable/configuring/config\_overview.html#main-content

Back to top

JupyterJupyter

https://jupyter-notebook.readthedocs.io/en/stable/index.html

Documentation

https://jupyter-notebook.readthedocs.io/en/stable/user-documentation.html

Configuration

https://jupyter-notebook.readthedocs.io/en/stable/configuration.html

https://jupyter-notebook.readthedocs.io/en/stable/migrate\_to\_notebook7.html

Contributing

https://jupyter-notebook.readthedocs.io/en/stable/contributor.html

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html

System Settings

https://github.com/jupyter/notebook

https://discourse.jupyter.org/c/notebook/31

Documentation

https://jupyter-notebook.readthedocs.io/en/stable/user-documentation.html

Configuration

https://jupyter-notebook.readthedocs.io/en/stable/configuration.html

https://jupyter-notebook.readthedocs.io/en/stable/migrate\_to\_notebook7.html

Contributing

https://jupyter-notebook.readthedocs.io/en/stable/contributor.html

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html

System Settings

https://github.com/jupyter/notebook

https://discourse.jupyter.org/c/notebook/31

Collapse Sidebar Expand Sidebar

Section Navigation

Configuration

Configuration Overview

https://jupyter-notebook.readthedocs.io/en/stable/configuring/config\_overview.html

https://jupyter-server.readthedocs.io/en/stable/operators/security.html

Extending the Notebook

https://jupyter-notebook.readthedocs.io/en/stable/extending/index.html

Extending the Jupyter Server

https://jupyter-server.readthedocs.io/en/stable/developers/index.html

Custom front-end extensions

https://jupyter-notebook.readthedocs.io/en/stable/extending/frontend\_extensions.html

$ lightcone run "what can I do for you?" — agents that actually act. Try the API →

https://server.ethicalads.io/proxy/click/10604/019f0192-a135-71d3-b7a2-9c4242c9dea1/

Ad by EthicalAds

https://www.ethicalads.io/advertisers/topics/data-science/?ref=rtd-sidebar-buy-ads

Configuration

https://jupyter-notebook.readthedocs.io/en/stable/configuration.html

Configuration Overview

Configuration Overview

https://jupyter-notebook.readthedocs.io/en/stable/configuring/config\_overview.html#configuration-overview

Beyond the default configuration settings, you can configure a rich array of options to suit your workflow. Here are areas that are commonly configured when using Jupyter Notebook:

Jupyter's common configuration system

https://jupyter-notebook.readthedocs.io/en/stable/configuring/config\_overview.html#configure-common

Jupyter Server

https://jupyter-notebook.readthedocs.io/en/stable/configuring/config\_overview.html#configure-jupyter-server

Notebook extensions

https://jupyter-notebook.readthedocs.io/en/stable/configuring/config\_overview.html#configure-nbextensions

Let's look at highlights of each area.

Jupyter's Common Configuration system

https://jupyter-notebook.readthedocs.io/en/stable/configuring/config\_overview.html#jupyter-s-common-configuration-system

Jupyter applications, from the Notebook to JupyterHub to nbgrader, share a common configuration system. The process for creating a configuration file and editing settings is similar for all the Jupyter applications.

Jupyter's Common Configuration Approach

https://jupyter.readthedocs.io/en/latest/use/config.html

Common Directories and File Locations

https://jupyter.readthedocs.io/en/latest/use/jupyter-directories.html

Language kernels

https://jupyter.readthedocs.io/en/latest/projects/kernels.html

https://traitlets.readthedocs.io/en/latest/config.html#module-traitlets.config

provide a low-level architecture for configuration.

Disabling Custom CSS

https://jupyter-notebook.readthedocs.io/en/stable/configuring/config\_overview.html#disabling-custom-css

Custom CSS is loaded by default as was done with Jupyter Notebook 6. In the jupyter configuration directory, the

/.jupyter/custom/custom.css

file will be loaded unless the application is initialized with the

flag with the argument set to

--JupyterNotebookApp.custom\_css=False

Jupyter server

https://jupyter-notebook.readthedocs.io/en/stable/configuring/config\_overview.html#jupyter-server

The Jupyter Server runs the language kernel and communicates with the front-end Notebook client (i.e. the familiar notebook interface).

Configuring the Jupyter Server To create a

jupyter\_server\_config.py

file in the

directory, with all the defaults commented out, use the following command:

$ jupyter server --generate-config

Running a Jupyter Server

https://jupyter-server.readthedocs.io/en/stable/operators/public-server.html

Configuring a language kernel

https://ipython.readthedocs.io/en/latest/install/kernel\_install.html

to run in the Jupyter Server enables your server to run other languages, like R or Julia.

Jupyter Notebook 7 is now based on Jupyter Server. This may break some previous

imports you may have been using, such as

notebook.auth

notebook.notebookapp

Check out the

migration guide

https://jupyter-notebook.readthedocs.io/en/stable/migrating/server-imports.html

to learn more on how to update these server imports.

Notebook extensions

https://jupyter-notebook.readthedocs.io/en/stable/configuring/config\_overview.html#notebook-extensions

The Notebook frontend can be extended with JupyterLab extensions.

Frontend Extension Guide

https://jupyter-notebook.readthedocs.io/en/stable/extending/frontend\_extensions.html#frontend-extensions

for more information.

#### Security in Jupyter notebooks:

https://jupyter-server.readthedocs.io/en/stable/operators/security.html

Since security policies vary from organization to organization, we encourage you to consult with your security team on settings that would be best for your use cases. Our documentation offers some responsible security practices, and we recommend becoming familiar with the practices.

previous Configuration

https://jupyter-notebook.readthedocs.io/en/stable/configuration.html

next Extending the Notebook

https://jupyter-notebook.readthedocs.io/en/stable/extending/index.html

On this page

Jupyter's Common Configuration system

https://jupyter-notebook.readthedocs.io/en/stable/configuring/config\_overview.html#jupyter-s-common-configuration-system

Disabling Custom CSS

https://jupyter-notebook.readthedocs.io/en/stable/configuring/config\_overview.html#disabling-custom-css

Jupyter server

https://jupyter-notebook.readthedocs.io/en/stable/configuring/config\_overview.html#jupyter-server

Notebook extensions

https://jupyter-notebook.readthedocs.io/en/stable/configuring/config\_overview.html#notebook-extensions

Edit on GitHub

https://github.com/jupyter/notebook/edit/main/docs/source/configuring/config\_overview.md

Show Source

https://jupyter-notebook.readthedocs.io/en/stable/\_sources/configuring/config\_overview.md.txt

© Copyright 2015, Jupyter Team, https://jupyter.org.

Created using

https://www.sphinx-doc.org/

Built with the

PyData Sphinx Theme

https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html

https://jupyter-notebook.readthedocs.io/en/master/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/latest/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v7.6.0/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v7.5.7/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v7.5.6/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v7.5.5/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v7.5.4/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v7.5.3/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v7.5.2/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v7.5.1/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v7.5.0/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v7.4.7/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v7.4.6/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v7.4.5/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v7.4.4/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v7.4.3/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v7.4.2/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v7.4.1/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v7.4.0/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v7.3.3/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v7.3.2/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v7.3.1/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v7.3.0/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v7.2.2/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v7.2.1/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v7.2.0/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v7.1.3/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v7.1.2/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v7.1.1/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v7.0.8/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v7.0.7/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v7.0.6/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v7.0.5/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v7.0.4/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v7.0.3/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v7.0.2/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v7.0.1/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v7.0.0/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v6.5.4/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v6.5.3/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v6.5.2/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v6.5.1/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v6.5.0/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/6.4.12/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v6.4.11/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/6.4.10/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v6.4.9/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v6.4.8/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v6.4.7/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v6.4.6/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v6.4.5/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/v6.4.4/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/6.2.0/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/5.7.6/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/5.7.5/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/5.7.4/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/5.7.3/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/5.7.2/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/5.7.1/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/5.7.0/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/5.6.0/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/5.5.0/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/5.4.1/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/5.4.0/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/5.3.1/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/5.2.2/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/5.1.0/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/5.0.0/configuring/config\_overview.html

https://jupyter-notebook.readthedocs.io/en/4.x/configuring/config\_overview.html

On Read the Docs

Project Home

https://app.readthedocs.org/projects/jupyter-notebook/?utm\_source=jupyter-notebook&utm\_content=flyout

https://app.readthedocs.org/projects/jupyter-notebook/builds/?utm\_source=jupyter-notebook&utm\_content=flyout

Addons documentation

https://docs.readthedocs.io/page/addons.html?utm\_source=jupyter-notebook&utm\_content=flyout

― Hosted by

Read the Docs

https://about.readthedocs.com/?utm\_source=jupyter-notebook&utm\_content=flyout

No recent searches

to navigate

Search powered by

