---
sourceFile: "Interface Customization — Jupyter Notebook 7.6.0 documentation"
exportedBy: "Kortex"
exportDate: "2026-06-26T04:27:51.395Z"
---

# Interface Customization — Jupyter Notebook 7.6.0 documentation

cc89cf7e-ac8b-470e-be2c-cf93f2f6c408

Interface Customization — Jupyter Notebook 7.6.0 documentation

f16f1dc2-b498-4727-9e56-f9ba2b3471d3

https://jupyter-notebook.readthedocs.io/en/stable/configuring/interface\_customization.html

Interface Customization — Jupyter Notebook 7.6.0 documentation

Skip to main content

https://jupyter-notebook.readthedocs.io/en/stable/configuring/interface\_customization.html#main-content

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

Interface Customization

Interface Customization

https://jupyter-notebook.readthedocs.io/en/stable/configuring/interface\_customization.html#interface-customization

Multiple elements in the Notebook interface can be customized via the Settings Editor.

https://jupyter-notebook.readthedocs.io/en/stable/configuring/interface\_customization.html#layout

By default some widgets are displayed in pre-defined parts of the user interface, which are often called “areas” or “regions”. For example the table of contents will be displayed in the

area by default, while the debugger will be displayed in the

However the positioning of some of these components can also be customized via the Settings Editor. Below are a few examples of how to do this.

Open the Markdown Preview on the left

https://jupyter-notebook.readthedocs.io/en/stable/configuring/interface\_customization.html#open-the-markdown-preview-on-the-left

It is often useful to be able to see a rendered preview of a Markdown document while editing it.

By default the Markdown Preview opens on the right side of the application. However it is also possible to open it on the left side by changing the Notebook Shell settings in the Advanced Settings Editor:

{
  "layout": {
    "Markdown Preview": {
      "area": "left"
    }
  }
}

Configuring a third-party widget

https://jupyter-notebook.readthedocs.io/en/stable/configuring/interface\_customization.html#configuring-a-third-party-widget

Third-party extensions can also add widgets to the application shell. This is for example the case with the

Voila extension

https://github.com/voila-dashboards/voila

, which adds a preview widget to visualize a notebook as a dashboard.

By default in JupyterLab the Voila Preview is added to the

area next to the corresponding notebook. With Notebook 7 it is possible to move the Voila Preview to the

area by changing the Notebook Shell setting in the Advanced Settings Editor as follows:

{
  "layout": {
    "Voila Preview": {
      "area": "right"
    }
  }
}

Refer to the

JupyterLab Layout Documentation

https://jupyterlab.readthedocs.io/en/latest/user/interface\_customization.html#layout

to learn more about the default positioning of other UI elements.

Toolbars, Menu bar and Context Menu

https://jupyter-notebook.readthedocs.io/en/stable/configuring/interface\_customization.html#toolbars-menu-bar-and-context-menu

It is also possible to customize toolbars, menus and context menu entries via the Settings Editor.

For example the items of the notebook toolbar can be reordered, or some menu entries can be hidden.

Refer to the

JupyterLab Documentation

https://jupyterlab.readthedocs.io/en/latest/user/interface\_customization.html

to learn more about general interface customization via the settings editor.

previous Managing plugins

https://jupyter-notebook.readthedocs.io/en/stable/configuring/plugins.html

next What to do when things go wrong

https://jupyter-notebook.readthedocs.io/en/stable/troubleshooting.html

On this page

https://jupyter-notebook.readthedocs.io/en/stable/configuring/interface\_customization.html#layout

Open the Markdown Preview on the left

https://jupyter-notebook.readthedocs.io/en/stable/configuring/interface\_customization.html#open-the-markdown-preview-on-the-left

Configuring a third-party widget

https://jupyter-notebook.readthedocs.io/en/stable/configuring/interface\_customization.html#configuring-a-third-party-widget

Toolbars, Menu bar and Context Menu

https://jupyter-notebook.readthedocs.io/en/stable/configuring/interface\_customization.html#toolbars-menu-bar-and-context-menu

Edit on GitHub

https://github.com/jupyter/notebook/edit/main/docs/source/configuring/interface\_customization.md

Show Source

https://jupyter-notebook.readthedocs.io/en/stable/\_sources/configuring/interface\_customization.md.txt

© Copyright 2015, Jupyter Team, https://jupyter.org.

Created using

https://www.sphinx-doc.org/

Built with the

PyData Sphinx Theme

https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html

https://jupyter-notebook.readthedocs.io/en/master/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/latest/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v7.6.0/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v7.5.7/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v7.5.6/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v7.5.5/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v7.5.4/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v7.5.3/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v7.5.2/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v7.5.1/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v7.5.0/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v7.4.7/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v7.4.6/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v7.4.5/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v7.4.4/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v7.4.3/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v7.4.2/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v7.4.1/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v7.4.0/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v7.3.3/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v7.3.2/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v7.3.1/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v7.3.0/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v7.2.2/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v7.2.1/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v7.2.0/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v7.1.3/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v7.1.2/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v7.1.1/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v7.0.8/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v7.0.7/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v7.0.6/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v7.0.5/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v7.0.4/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v7.0.3/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v7.0.2/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v7.0.1/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v7.0.0/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v6.5.4/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v6.5.3/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v6.5.2/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v6.5.1/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v6.5.0/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/6.4.12/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v6.4.11/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/6.4.10/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v6.4.9/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v6.4.8/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v6.4.7/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v6.4.6/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v6.4.5/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/v6.4.4/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/6.2.0/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/5.7.6/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/5.7.5/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/5.7.4/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/5.7.3/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/5.7.2/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/5.7.1/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/5.7.0/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/5.6.0/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/5.5.0/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/5.4.1/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/5.4.0/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/5.3.1/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/5.2.2/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/5.1.0/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/5.0.0/configuring/interface\_customization.html

https://jupyter-notebook.readthedocs.io/en/4.x/configuring/interface\_customization.html

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

