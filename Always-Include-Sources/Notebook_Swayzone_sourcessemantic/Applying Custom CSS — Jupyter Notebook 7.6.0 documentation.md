---
sourceFile: "Applying Custom CSS — Jupyter Notebook 7.6.0 documentation"
exportedBy: "Kortex"
exportDate: "2026-06-26T04:27:51.059Z"
---

# Applying Custom CSS — Jupyter Notebook 7.6.0 documentation

612e5a4d-7e3f-4fcc-a02f-cbbdd26b8d36

Applying Custom CSS — Jupyter Notebook 7.6.0 documentation

3477f5f5-f4f6-446d-8e89-0e3fad0cb270

https://jupyter-notebook.readthedocs.io/en/stable/custom\_css.html

Applying Custom CSS — Jupyter Notebook 7.6.0 documentation

Skip to main content

https://jupyter-notebook.readthedocs.io/en/stable/custom\_css.html#main-content

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

Applying Custom CSS

Applying Custom CSS

https://jupyter-notebook.readthedocs.io/en/stable/custom\_css.html#applying-custom-css

To apply custom CSS, you can add a

/custom/custom.css

file in the jupyter

directory. You can find the path,

, to this directory by running

jupyter --paths

. There you can create a folder named

and create a

file within the folder.

Jupyter Styling

https://jupyter-notebook.readthedocs.io/en/stable/custom\_css.html#jupyter-styling

You can use a custom CSS file to modify default Jupyter styling.

/\* Modify Jupyter Styles \*/
#top-panel-wrapper,
#jp-top-bar {
  background-color: #aecad4 !important;
}

#menu-panel-wrapper,
#jp-MainMenu,
#menu-panel {
  background-color: #aecad4 !important;
}

.jp-NotebookPanel-toolbar {
  background-color: #aecad4 !important;
}
.lm-MenuBar-content {
  color: #02484d;
}

https://jupyter-notebook.readthedocs.io/en/stable/custom\_css.html#markdown

Another potential application for custom CSS is styling markdown.

/\* Headings \*/
h1,
h2 {
  font-family: Impact, Charcoal, sans-serif;
  font-weight: bold;
  text-shadow: 2px 2px 4px #000000;
}

h1 {
  font-size: 52px;
  margin-bottom: 40px;
  color: #10929e;
  text-decoration: underline;
}

h2 {
  font-size: 448px;
  margin-bottom: 32px;
  color: #76b4be;
  text-transform: uppercase;
}

/\* Block Quotes \*/
blockquote {
  font-family: Georgia, serif;
  font-size: 16px;
  color: #19085c;
  border-left: 8px solid #effffc;
  background-color: #eafcff;
  padding: 20px;
}

/\* Lists \*/
ul,
ol {
  font-family: Verdana, Geneva, sans-serif;
  font-size: 18px;
  color: #333333;
  margin-bottom: 24px;
}

previous Motivating Examples

https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Typesetting%20Equations.html

next Managing plugins

https://jupyter-notebook.readthedocs.io/en/stable/configuring/plugins.html

On this page

Jupyter Styling

https://jupyter-notebook.readthedocs.io/en/stable/custom\_css.html#jupyter-styling

https://jupyter-notebook.readthedocs.io/en/stable/custom\_css.html#markdown

Edit on GitHub

https://github.com/jupyter/notebook/edit/main/docs/source/custom\_css.md

Show Source

https://jupyter-notebook.readthedocs.io/en/stable/\_sources/custom\_css.md.txt

© Copyright 2015, Jupyter Team, https://jupyter.org.

Created using

https://www.sphinx-doc.org/

Built with the

PyData Sphinx Theme

https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html

https://jupyter-notebook.readthedocs.io/en/master/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/latest/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v7.6.0/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v7.5.7/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v7.5.6/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v7.5.5/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v7.5.4/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v7.5.3/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v7.5.2/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v7.5.1/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v7.5.0/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v7.4.7/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v7.4.6/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v7.4.5/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v7.4.4/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v7.4.3/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v7.4.2/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v7.4.1/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v7.4.0/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v7.3.3/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v7.3.2/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v7.3.1/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v7.3.0/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v7.2.2/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v7.2.1/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v7.2.0/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v7.1.3/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v7.1.2/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v7.1.1/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v7.0.8/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v7.0.7/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v7.0.6/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v7.0.5/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v7.0.4/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v7.0.3/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v7.0.2/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v7.0.1/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v7.0.0/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v6.5.4/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v6.5.3/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v6.5.2/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v6.5.1/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v6.5.0/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/6.4.12/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v6.4.11/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/6.4.10/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v6.4.9/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v6.4.8/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v6.4.7/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v6.4.6/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v6.4.5/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/v6.4.4/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/6.2.0/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/5.7.6/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/5.7.5/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/5.7.4/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/5.7.3/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/5.7.2/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/5.7.1/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/5.7.0/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/5.6.0/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/5.5.0/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/5.4.1/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/5.4.0/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/5.3.1/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/5.2.2/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/5.1.0/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/5.0.0/custom\_css.html

https://jupyter-notebook.readthedocs.io/en/4.x/custom\_css.html

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

