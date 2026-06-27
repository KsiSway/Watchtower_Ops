---
sourceFile: "Migrating — Jupyter Notebook 7.6.0 documentation"
exportedBy: "Kortex"
exportDate: "2026-06-26T04:27:51.471Z"
---

# Migrating — Jupyter Notebook 7.6.0 documentation

ea96738e-ff16-4cda-b0f4-9646d1a0bea8

Migrating — Jupyter Notebook 7.6.0 documentation

763697b5-5d61-4b10-9243-1ae80153a118

https://jupyter-notebook.readthedocs.io/en/stable/migrate\_to\_notebook7.html

Migrating — Jupyter Notebook 7.6.0 documentation

Skip to main content

https://jupyter-notebook.readthedocs.io/en/stable/migrate\_to\_notebook7.html#main-content

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

New features in Notebook 7

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html

Frontend Extensions in Notebook 7

https://jupyter-notebook.readthedocs.io/en/stable/migrating/frontend-extensions.html

Server Extensions in Notebook 7

https://jupyter-notebook.readthedocs.io/en/stable/migrating/server-extensions.html

Server Imports in Notebook 7

https://jupyter-notebook.readthedocs.io/en/stable/migrating/server-imports.html

Custom themes in Notebook 7

https://jupyter-notebook.readthedocs.io/en/stable/migrating/custom-themes.html

Simultaneous usage of different versions of Notebook 7 and the Classic Notebook UI

https://jupyter-notebook.readthedocs.io/en/stable/migrating/multiple-interfaces.html

$ lightcone run "what can I do for you?" — agents that actually act. Try the API →

https://server.ethicalads.io/proxy/click/10604/019f0192-a135-71d3-b7a2-9c4242c9dea1/

Ad by EthicalAds

https://www.ethicalads.io/advertisers/topics/data-science/?ref=rtd-sidebar-buy-ads

https://jupyter-notebook.readthedocs.io/en/stable/migrate\_to\_notebook7.html#migrating

Updated 2023-05-17

Version 7 of the Jupyter Notebook application might break your extensions or other customizations. Please read this page to find out if you need to take any actions to ensure a smooth, uninterrupted experience.

A major upgrade to the Jupyter Notebook interface is coming with Notebook 7! This upgrade will bring a heap of new features, but will also break backwards compatibility with many classic Notebook features and customizations.

This set of guides is here to help you migrate your Classic Notebook setup and extensions to the new Notebook 7.

What you need to do

https://jupyter-notebook.readthedocs.io/en/stable/migrate\_to\_notebook7.html#what-you-need-to-do

For users who don't use extensions or other customizations, you will seamlessly receive the new Notebook 7 when you

pip install notebook

once version 7 is released out of beta, along with all its new features, like realtime collaboration, debugger, and theming.

For users who need to use extensions or other customizations, you have a couple of options:

Look for Notebook 7 compatible versions of the extensions you already use, and

find replacements for those that are not available

https://jupyter-notebook.readthedocs.io/en/latest/migrating/frontend-extensions.html#jupyterlab-equivalent-extensions-to-the-classic-notebook

If you need to maintain compatibility with the Classic Notebook for extensions or other customizations that are critical to your workflows, you can switch to

https://github.com/jupyter/nbclassic

, which will provide compatibility with the old notebook interface and support during an intermediate transition period to Notebook 7

Why a new version?

https://jupyter-notebook.readthedocs.io/en/stable/migrate\_to\_notebook7.html#why-a-new-version

For the past few years, the Classic Jupyter Notebook has been in maintenance mode.

Development has mostly moved to alternative user interfaces like JupyterLab, which is a more modern and extensible web application. This has resulted in a lot of new features and improvements in JupyterLab, but also in a lot of new features and improvements that were not possible to integrate to the Classic Notebook.

For a while, the plan was to progressively

the Classic Notebook and not maintain it anymore. However, the Classic Notebook is still widely used and it is still the default user interface for Jupyter in many scenarios. Many users and organizations have not been able to switch to JupyterLab yet. For some users, JupyterLab can also be a more complex environment to use, especially for beginners.

Following the feedback from the community, it was decided in late 2021 to continue developing the Jupyter Notebook application and

it as Notebook 7.

You can find more details about the changes currently taking place in the Jupyter Ecosystem in the

https://jupyter.org/enhancement-proposals/79-notebook-v7/notebook-v7.html

team-compass note

https://github.com/jupyter/notebook-team-compass/issues/5#issuecomment-1085254000

New features in Notebook 7

https://jupyter-notebook.readthedocs.io/en/stable/migrate\_to\_notebook7.html#new-features-in-notebook-7

New features in Notebook 7

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#debugger

Real Time collaboration

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#real-time-collaboration

Table of Contents

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#id1

Theming and Dark Mode

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#theming-and-dark-mode

Internationalization

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#internationalization

Accessibility Improvements

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#accessibility-improvements

Support for many JupyterLab extensions

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#support-for-many-jupyterlab-extensions

A document-centric user experience

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#a-document-centric-user-experience

Compact View on Mobile Devices

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#compact-view-on-mobile-devices

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#references

Migration Guides

https://jupyter-notebook.readthedocs.io/en/stable/migrate\_to\_notebook7.html#migration-guides

Frontend Extensions in Notebook 7

https://jupyter-notebook.readthedocs.io/en/stable/migrating/frontend-extensions.html

List of available Notebook 7 extensions

https://jupyter-notebook.readthedocs.io/en/stable/migrating/frontend-extensions.html#list-of-available-notebook-7-extensions

JupyterLab equivalent extensions to the Classic Notebook

https://jupyter-notebook.readthedocs.io/en/stable/migrating/frontend-extensions.html#jupyterlab-equivalent-extensions-to-the-classic-notebook

Server Extensions in Notebook 7

https://jupyter-notebook.readthedocs.io/en/stable/migrating/server-extensions.html

Migration from the Notebook Server

https://jupyter-notebook.readthedocs.io/en/stable/migrating/server-extensions.html#migration-from-the-notebook-server

Authoring Server Extensions

https://jupyter-notebook.readthedocs.io/en/stable/migrating/server-extensions.html#authoring-server-extensions

Server Imports in Notebook 7

https://jupyter-notebook.readthedocs.io/en/stable/migrating/server-imports.html

Custom themes in Notebook 7

https://jupyter-notebook.readthedocs.io/en/stable/migrating/custom-themes.html

Using a custom theme

https://jupyter-notebook.readthedocs.io/en/stable/migrating/custom-themes.html#using-a-custom-theme

Creating a custom theme

https://jupyter-notebook.readthedocs.io/en/stable/migrating/custom-themes.html#creating-a-custom-theme

Simultaneous usage of different versions of Notebook 7 and the Classic Notebook UI

https://jupyter-notebook.readthedocs.io/en/stable/migrating/multiple-interfaces.html

Try it on Binder

https://jupyter-notebook.readthedocs.io/en/stable/migrating/multiple-interfaces.html#try-it-on-binder

Using the Interface dropdown

https://jupyter-notebook.readthedocs.io/en/stable/migrating/multiple-interfaces.html#using-the-interface-dropdown

NbClassic and Notebook 7

https://jupyter-notebook.readthedocs.io/en/stable/migrating/multiple-interfaces.html#nbclassic-and-notebook-7

NbClassic and Notebook 6.5.x

https://jupyter-notebook.readthedocs.io/en/stable/migrating/multiple-interfaces.html#nbclassic-and-notebook-6-5-x

NbClassic and Notebook <= 6.4.x

https://jupyter-notebook.readthedocs.io/en/stable/migrating/multiple-interfaces.html#nbclassic-and-notebook-6-4-x

NbClassic and JupyterLab 3.x

https://jupyter-notebook.readthedocs.io/en/stable/migrating/multiple-interfaces.html#nbclassic-and-jupyterlab-3-x

NbClassic and JupyterLab 4.x

https://jupyter-notebook.readthedocs.io/en/stable/migrating/multiple-interfaces.html#nbclassic-and-jupyterlab-4-x

NbClassic Independently

https://jupyter-notebook.readthedocs.io/en/stable/migrating/multiple-interfaces.html#nbclassic-independently

previous Custom front-end extensions

https://jupyter-notebook.readthedocs.io/en/stable/extending/frontend\_extensions.html

next Frontend Extensions in Notebook 7

https://jupyter-notebook.readthedocs.io/en/stable/migrating/frontend-extensions.html

On this page

What you need to do

https://jupyter-notebook.readthedocs.io/en/stable/migrate\_to\_notebook7.html#what-you-need-to-do

Why a new version?

https://jupyter-notebook.readthedocs.io/en/stable/migrate\_to\_notebook7.html#why-a-new-version

New features in Notebook 7

https://jupyter-notebook.readthedocs.io/en/stable/migrate\_to\_notebook7.html#new-features-in-notebook-7

Migration Guides

https://jupyter-notebook.readthedocs.io/en/stable/migrate\_to\_notebook7.html#migration-guides

Edit on GitHub

https://github.com/jupyter/notebook/edit/main/docs/source/migrate\_to\_notebook7.md

Show Source

https://jupyter-notebook.readthedocs.io/en/stable/\_sources/migrate\_to\_notebook7.md.txt

© Copyright 2015, Jupyter Team, https://jupyter.org.

Created using

https://www.sphinx-doc.org/

Built with the

PyData Sphinx Theme

https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html

https://jupyter-notebook.readthedocs.io/en/master/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/latest/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v7.6.0/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v7.5.7/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v7.5.6/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v7.5.5/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v7.5.4/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v7.5.3/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v7.5.2/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v7.5.1/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v7.5.0/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v7.4.7/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v7.4.6/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v7.4.5/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v7.4.4/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v7.4.3/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v7.4.2/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v7.4.1/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v7.4.0/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v7.3.3/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v7.3.2/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v7.3.1/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v7.3.0/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v7.2.2/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v7.2.1/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v7.2.0/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v7.1.3/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v7.1.2/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v7.1.1/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v7.0.8/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v7.0.7/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v7.0.6/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v7.0.5/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v7.0.4/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v7.0.3/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v7.0.2/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v7.0.1/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v7.0.0/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v6.5.4/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v6.5.3/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v6.5.2/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v6.5.1/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v6.5.0/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/6.4.12/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v6.4.11/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/6.4.10/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v6.4.9/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v6.4.8/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v6.4.7/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v6.4.6/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v6.4.5/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/v6.4.4/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/6.2.0/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/5.7.6/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/5.7.5/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/5.7.4/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/5.7.3/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/5.7.2/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/5.7.1/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/5.7.0/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/5.6.0/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/5.5.0/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/5.4.1/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/5.4.0/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/5.3.1/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/5.2.2/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/5.1.0/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/5.0.0/migrate\_to\_notebook7.html

https://jupyter-notebook.readthedocs.io/en/4.x/migrate\_to\_notebook7.html

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

