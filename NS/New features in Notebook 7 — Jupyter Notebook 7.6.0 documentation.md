---
sourceFile: "New features in Notebook 7 — Jupyter Notebook 7.6.0 documentation"
exportedBy: "Kortex"
exportDate: "2026-06-26T04:27:51.479Z"
---

# New features in Notebook 7 — Jupyter Notebook 7.6.0 documentation

9ec5c0c8-686c-4997-9d5b-79b582bfa5b8

New features in Notebook 7 — Jupyter Notebook 7.6.0 documentation

bd6750e0-c423-4528-92d7-6544fe92d869

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html

New features in Notebook 7 — Jupyter Notebook 7.6.0 documentation

Skip to main content

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#main-content

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

The Jupyter Notebook

https://jupyter-notebook.readthedocs.io/en/stable/notebook.html

User interface components

https://jupyter-notebook.readthedocs.io/en/stable/ui\_components.html

New features in Notebook 7

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html

Notebook Examples

https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/examples\_index.html

What is the Jupyter Notebook?

https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/What%20is%20the%20Jupyter%20Notebook.html

Notebook Basics

https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Notebook%20Basics.html

Running Code

https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Running%20Code.html

Markdown Cells

https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Working%20With%20Markdown%20Cells.html

Keyboard Shortcut Customization

https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Custom%20Keyboard%20Shortcuts.html

Importing Jupyter Notebooks as Modules

https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Importing%20Notebooks.html

Connecting to an existing IPython kernel using the Qt Console

https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Connecting%20with%20the%20Qt%20Console.html

Motivating Examples

https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Typesetting%20Equations.html

Applying Custom CSS

https://jupyter-notebook.readthedocs.io/en/stable/custom\_css.html

Managing plugins

https://jupyter-notebook.readthedocs.io/en/stable/configuring/plugins.html

Interface Customization

https://jupyter-notebook.readthedocs.io/en/stable/configuring/interface\_customization.html

What to do when things go wrong

https://jupyter-notebook.readthedocs.io/en/stable/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html

$ lightcone run "what can I do for you?" — agents that actually act. Try the API →

https://server.ethicalads.io/proxy/click/10604/019f0192-a135-71d3-b7a2-9c4242c9dea1/

Ad by EthicalAds

https://www.ethicalads.io/advertisers/topics/data-science/?ref=rtd-sidebar-buy-ads

Documentation

https://jupyter-notebook.readthedocs.io/en/stable/user-documentation.html

New features in Notebook 7

New features in Notebook 7

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#new-features-in-notebook-7

This document describes the new features in Notebook 7 as originally mentioned in the related Jupyter Enhancement Proposal

https://jupyter.org/enhancement-proposals/79-notebook-v7/notebook-v7.html

Table of Contents

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

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#nbgrader

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#rise

A document-centric user experience

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#a-document-centric-user-experience

Compact View on Mobile Devices

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#compact-view-on-mobile-devices

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#references

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#id2

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#debugger

Notebook 7 includes a new debugger that allows you to step through your code cell by cell. You can also set breakpoints and inspect variables.

Real Time collaboration

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#id3

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#real-time-collaboration

Notebook 7 allows for using the real time collaboration extension so you can share your notebook with other users and edit it in real time.

The Real Time Collaboration feature is the same as in JupyterLab and is available as a JupyterLab extension. It is not enabled by default, but you can install with

pip install jupyter-collaboration

conda install -c conda-forge jupyter-collaboration

After installing the extension, restart the Jupyter Server so the extension can be loaded.

It is possible for two users to work on the same notebook using Notebook 7 or JupyterLab.

Table of Contents

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#id4

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#id1

Notebook 7 includes a new table of contents extension that allows you to navigate through your notebook using a sidebar. The Table of Contents is built-in and enabled by default, just like in JupyterLab.

Theming and Dark Mode

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#id5

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#theming-and-dark-mode

A Dark Theme is now available in the Jupyter Notebook by default. You can also install other themes as JupyterLab extensions.

You can also install many other JupyterLab themes. For example to install the

JupyterLab Night

https://github.com/martinRenou/jupyterlab-night

pip install jupyterlab-night

#### Then refresh the page and select the new theme in the settings:

Internationalization

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#id6

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#internationalization

Notebook 7 now provides the ability to set the display language of the user interface.

Users will need to install the language pack as a separate Python package. Language packs are grouped in the

language packs repository on GitHub

https://github.com/jupyterlab/language-packs/

, and can be installed with

. For example, it is possible to install the language pack for French (France) using the following command:

pip install jupyterlab-language-pack-fr-FR

After installing the language pack, reload the page and the new language should be available in the settings.

Notebook 7 and JupyterLab share the same language packs, so it is possible to use the same language pack in both applications.

Accessibility Improvements

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#id7

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#accessibility-improvements

The text editor underlying the Jupyter Notebook (CodeMirror 5) had major accessibility issues. Fortunately, this accessibility bottleneck has been unblocked as JupyterLab has been upgraded to use CodeMirror 6, a complete rewrite of the text editor with a strong focus on accessibility. Although this upgrade required extensive codebase modifications, the changes are available with JupyterLab 4. By being built on top of JupyterLab, Jupyter Notebook 7 directly benefits from the CodeMirror 6 upgrade.

Support for many JupyterLab extensions

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#id8

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#support-for-many-jupyterlab-extensions

Notebook 7 is based on JupyterLab and therefore supports many of the existing JupyterLab extensions.

You can install JupyterLab extensions with

. For example to install the LSP (Language Server Protocol) extension for enhanced code completion, you can use the following commands:

pip install jupyter-lsp

conda install -c conda-forge jupyter-lsp

Popular extensions like

have already been ported to work with Notebook 7.

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#id9

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#nbgrader

The nbgrader extension is still under active development and a version compatible with Notebook 7 is not yet available on PyPI. However a version compatible with Notebook 7 will be available before the final release of Notebook 7.

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#id10

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#rise

The RISE extension is another popular JupyterLab extension that has been ported to work with Notebook 7. It allows you to turn your Jupyter Notebooks into a slideshow. See the

installation instructions

https://github.com/jupyterlab-contrib/rise#install

A document-centric user experience

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#id11

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#a-document-centric-user-experience

Despite all the new features and as stated in

https://jupyter.org/enhancement-proposals/79-notebook-v7/notebook-v7.html

, Notebook 7 keeps the document-centric user experience of the Classic Notebook:

The Jupyter Notebook application offers a document-centric user experience. That is, in the Notebook application, the landing page that contains a file manager, running tools tab, and a few optional extras, is a launching point into opening standalone, individual documents. This document-centric experience is important for many users, and that is the first key point this proposal aims to preserve. Notebook v7 will be based on a different JavaScript implementation than v6, but it will preserve the document-centric experience, where each individual notebook opens in a separate browser tab and the visible tools and menus are focused on the open document.

Compact View on Mobile Devices

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#id12

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#compact-view-on-mobile-devices

Notebook 7 automatically switches to a more compact layout on mobile devices, making it convenient to run code on the go.

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#id13

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#references

This was just a quick overview of the new features in Notebook 7. For more details, you can check out the following resources:

JupyterLab Documentation

https://jupyterlab.readthedocs.io/en/latest/

is a great resource to learn more about JupyterLab and the extensions available. Since Notebook 7 is based on JupyterLab, many of the features and extensions available for JupyterLab are also available for Notebook 7.

Migration Guide

https://jupyter-notebook.readthedocs.io/en/stable/migrate\_to\_notebook7.html

for Notebook 7, which explains how to migrate from the Classic Notebook to Notebook 7.

previous User interface components

https://jupyter-notebook.readthedocs.io/en/stable/ui\_components.html

next Notebook Examples

https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/examples\_index.html

On this page

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

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#nbgrader

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#rise

A document-centric user experience

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#a-document-centric-user-experience

Compact View on Mobile Devices

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#compact-view-on-mobile-devices

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html#references

Edit on GitHub

https://github.com/jupyter/notebook/edit/main/docs/source/notebook\_7\_features.md

Show Source

https://jupyter-notebook.readthedocs.io/en/stable/\_sources/notebook\_7\_features.md.txt

© Copyright 2015, Jupyter Team, https://jupyter.org.

Created using

https://www.sphinx-doc.org/

Built with the

PyData Sphinx Theme

https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html

https://jupyter-notebook.readthedocs.io/en/master/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/latest/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v7.6.0/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v7.5.7/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v7.5.6/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v7.5.5/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v7.5.4/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v7.5.3/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v7.5.2/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v7.5.1/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v7.5.0/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v7.4.7/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v7.4.6/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v7.4.5/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v7.4.4/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v7.4.3/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v7.4.2/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v7.4.1/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v7.4.0/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v7.3.3/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v7.3.2/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v7.3.1/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v7.3.0/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v7.2.2/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v7.2.1/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v7.2.0/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v7.1.3/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v7.1.2/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v7.1.1/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v7.0.8/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v7.0.7/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v7.0.6/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v7.0.5/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v7.0.4/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v7.0.3/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v7.0.2/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v7.0.1/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v7.0.0/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v6.5.4/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v6.5.3/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v6.5.2/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v6.5.1/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v6.5.0/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/6.4.12/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v6.4.11/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/6.4.10/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v6.4.9/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v6.4.8/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v6.4.7/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v6.4.6/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v6.4.5/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/v6.4.4/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/6.2.0/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/5.7.6/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/5.7.5/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/5.7.4/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/5.7.3/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/5.7.2/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/5.7.1/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/5.7.0/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/5.6.0/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/5.5.0/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/5.4.1/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/5.4.0/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/5.3.1/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/5.2.2/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/5.1.0/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/5.0.0/notebook\_7\_features.html

https://jupyter-notebook.readthedocs.io/en/4.x/notebook\_7\_features.html

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

