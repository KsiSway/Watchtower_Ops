---
sourceFile: "Running the Notebook — Jupyter Documentation 4.1.1 alpha documentation"
exportedBy: "Kortex"
exportDate: "2026-06-26T04:27:51.575Z"
---

# Running the Notebook — Jupyter Documentation 4.1.1 alpha documentation

91e49ef1-323b-4efd-a9a8-f67b6f334e8e

Running the Notebook — Jupyter Documentation 4.1.1 alpha documentation

c5c63c88-8fc9-441d-a495-9ccf302da10f

https://jupyter.readthedocs.io/en/latest/running.html

Running the Notebook — Jupyter Documentation 4.1.1 alpha documentation

Skip to main content

https://jupyter.readthedocs.io/en/latest/running.html#main-content

Back to top

Jupyter Documentation 4.1.1 alpha documentation - HomeJupyter Documentation 4.1.1 alpha documentation - Home

https://jupyter.readthedocs.io/en/latest/index.html

Try Jupyter

https://jupyter.readthedocs.io/en/latest/start/index.html

https://jupyter.readthedocs.io/en/latest/use/using.html

https://jupyter.readthedocs.io/en/latest/projects/content-projects.html

https://jupyter.readthedocs.io/en/latest/community/content-community.html

Contributing

https://jupyter.readthedocs.io/en/latest/contributing/content-contributor.html

https://jupyter.readthedocs.io/en/latest/reference/content-reference.html

jupyter.org

https://jupyter.org/

System Settings

https://github.com/jupyter/jupyter

https://discourse.jupyter.org/

Try Jupyter

https://jupyter.readthedocs.io/en/latest/start/index.html

https://jupyter.readthedocs.io/en/latest/use/using.html

https://jupyter.readthedocs.io/en/latest/projects/content-projects.html

https://jupyter.readthedocs.io/en/latest/community/content-community.html

Contributing

https://jupyter.readthedocs.io/en/latest/contributing/content-contributor.html

https://jupyter.readthedocs.io/en/latest/reference/content-reference.html

jupyter.org

https://jupyter.org/

System Settings

https://github.com/jupyter/jupyter

https://discourse.jupyter.org/

Collapse Sidebar Expand Sidebar

Section Navigation

Install and Use

https://jupyter.readthedocs.io/en/latest/install.html

Installing the classic Jupyter Notebook interface

https://jupyter.readthedocs.io/en/latest/install/notebook-classic.html

Upgrading Jupyter Notebook

https://jupyter.readthedocs.io/en/latest/use/upgrade-notebook.html

Installing Kernels

https://jupyter.readthedocs.io/en/latest/install/kernels.html

Running the Notebook

https://jupyter.readthedocs.io/en/latest/running.html

$ lightcone run "what can I do for you?" — agents that actually act. Try the API →

https://server.ethicalads.io/proxy/click/10604/019f0192-a135-71d3-b7a2-9c4242c9dea1/

Ad by EthicalAds

https://www.ethicalads.io/advertisers/topics/data-science/?ref=rtd-sidebar-buy-ads

Try Jupyter

https://jupyter.readthedocs.io/en/latest/start/index.html

Running the Notebook

Running the Notebook

https://jupyter.readthedocs.io/en/latest/running.html#running-the-notebook

Basic Steps

https://jupyter.readthedocs.io/en/latest/running.html#basic-steps

Starting the Notebook Server

https://jupyter.readthedocs.io/en/latest/running.html#starting-the-notebook-server

Introducing the Notebook Server's Command Line Options

https://jupyter.readthedocs.io/en/latest/running.html#introducing-the-notebook-server-s-command-line-options

How do I open a specific Notebook?

https://jupyter.readthedocs.io/en/latest/running.html#how-do-i-open-a-specific-notebook

How do I start the Notebook using a custom IP or port?

https://jupyter.readthedocs.io/en/latest/running.html#how-do-i-start-the-notebook-using-a-custom-ip-or-port

How do I start the Notebook server without opening a browser?

https://jupyter.readthedocs.io/en/latest/running.html#how-do-i-start-the-notebook-server-without-opening-a-browser

How do I get help about Notebook server options?

https://jupyter.readthedocs.io/en/latest/running.html#how-do-i-get-help-about-notebook-server-options

Using a command-line interface

https://jupyter.readthedocs.io/en/latest/running.html#using-a-command-line-interface

Basic Steps

https://jupyter.readthedocs.io/en/latest/running.html#id1

https://jupyter.readthedocs.io/en/latest/running.html#basic-steps

Start the notebook server from the

command line

https://jupyter.readthedocs.io/en/latest/glossary.html#term-command-line

jupyter notebook

You should see the notebook open in your browser.

Starting the Notebook Server

https://jupyter.readthedocs.io/en/latest/running.html#id2

https://jupyter.readthedocs.io/en/latest/running.html#starting-the-notebook-server

After you have installed the Jupyter Notebook on your computer, you are ready to run the notebook server. You can start the notebook server from the

command line

https://jupyter.readthedocs.io/en/latest/glossary.html#term-command-line

https://jupyter.readthedocs.io/en/latest/glossary.html#term-terminal

on Mac/Linux,

Command Prompt

https://jupyter.readthedocs.io/en/latest/glossary.html#term-Command-Prompt

on Windows) by running:

jupyter notebook

This will print some information about the notebook server in your terminal, including the URL of the web application (by default,

http://localhost:8888

$ jupyter notebook
\[I 08:58:24.417 NotebookApp\] Serving notebooks from local directory: /Users/catherine
\[I 08:58:24.417 NotebookApp\] 0 active kernels
\[I 08:58:24.417 NotebookApp\] The Jupyter Notebook is running at: http://localhost:8888/
\[I 08:58:24.417 NotebookApp\] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).

It will then open your default web browser to this URL.

When the notebook opens in your browser, you will see the

Notebook Dashboard

https://jupyter.readthedocs.io/en/latest/glossary.html#term-Notebook-Dashboard

, which will show a list of the notebooks, files, and subdirectories in the directory where the notebook server was started. Most of the time, you will wish to start a notebook server in the highest level directory containing notebooks. Often this will be your home directory.

Notebook Dashboard

Introducing the Notebook Server's Command Line Options

https://jupyter.readthedocs.io/en/latest/running.html#id3

https://jupyter.readthedocs.io/en/latest/running.html#introducing-the-notebook-server-s-command-line-options

How do I open a specific Notebook?

https://jupyter.readthedocs.io/en/latest/running.html#id4

https://jupyter.readthedocs.io/en/latest/running.html#how-do-i-open-a-specific-notebook

The following code should open the given notebook in the currently running notebook server, starting one if necessary.

jupyter notebook notebook.ipynb

How do I start the Notebook using a custom IP or port?

https://jupyter.readthedocs.io/en/latest/running.html#id5

https://jupyter.readthedocs.io/en/latest/running.html#how-do-i-start-the-notebook-using-a-custom-ip-or-port

By default, the notebook server starts on port 8888. If port 8888 is unavailable or in use, the notebook server searches the next available port. You may also specify a port manually. In this example, we set the server's port to 9999:

jupyter notebook --port 9999

How do I start the Notebook server without opening a browser?

https://jupyter.readthedocs.io/en/latest/running.html#id6

https://jupyter.readthedocs.io/en/latest/running.html#how-do-i-start-the-notebook-server-without-opening-a-browser

#### Start notebook server without opening a web browser:

jupyter notebook --no-browser

How do I get help about Notebook server options?

https://jupyter.readthedocs.io/en/latest/running.html#id7

https://jupyter.readthedocs.io/en/latest/running.html#how-do-i-get-help-about-notebook-server-options

The notebook server provides help messages for other command line arguments using the

jupyter notebook --help

Jupyter Installation, Configuration, and Usage

https://jupyter.readthedocs.io/en/latest/projects/content-projects.html#content-projects

Detailed information about command line arguments, configuration, and usage.

Using a command-line interface

https://jupyter.readthedocs.io/en/latest/running.html#id8

https://jupyter.readthedocs.io/en/latest/running.html#using-a-command-line-interface

Notebooks can be executed from your terminal using the

subcommand. It expects notebook paths as input arguments and accepts optional flags to modify the default behavior.

Running a notebook is this easy.

jupyter execute notebook.ipynb

You can pass more than one notebook as well.

jupyter execute notebook.ipynb notebook2.ipynb

By default, notebook errors will be raised and printed into the terminal. You can suppress them by passing the

--allow-errors

jupyter execute notebook.ipynb --allow-errors

For more sophisticated execution options, consider the

https://pypi.org/project/papermill/

previous Installing Kernels

https://jupyter.readthedocs.io/en/latest/install/kernels.html

https://jupyter.readthedocs.io/en/latest/use/using.html

On this page

Basic Steps

https://jupyter.readthedocs.io/en/latest/running.html#basic-steps

Starting the Notebook Server

https://jupyter.readthedocs.io/en/latest/running.html#starting-the-notebook-server

Introducing the Notebook Server's Command Line Options

https://jupyter.readthedocs.io/en/latest/running.html#introducing-the-notebook-server-s-command-line-options

How do I open a specific Notebook?

https://jupyter.readthedocs.io/en/latest/running.html#how-do-i-open-a-specific-notebook

How do I start the Notebook using a custom IP or port?

https://jupyter.readthedocs.io/en/latest/running.html#how-do-i-start-the-notebook-using-a-custom-ip-or-port

How do I start the Notebook server without opening a browser?

https://jupyter.readthedocs.io/en/latest/running.html#how-do-i-start-the-notebook-server-without-opening-a-browser

How do I get help about Notebook server options?

https://jupyter.readthedocs.io/en/latest/running.html#how-do-i-get-help-about-notebook-server-options

Using a command-line interface

https://jupyter.readthedocs.io/en/latest/running.html#using-a-command-line-interface

Edit on GitHub

https://github.com/jupyter/jupyter/edit/master/docs/source/running.rst

Show Source

https://jupyter.readthedocs.io/en/latest/\_sources/running.rst.txt

© Copyright 2015, Jupyter Team, https://jupyter.org.

Created using

https://www.sphinx-doc.org/

Built with the

PyData Sphinx Theme

https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html

https://docs.jupyter.org/es/latest/running.html

https://docs.jupyter.org/pt-br/latest/running.html

https://docs.jupyter.org/ru/latest/running.html

https://docs.jupyter.org/en/stable/running.html

On Read the Docs

Project Home

https://app.readthedocs.org/projects/jupyter/?utm\_source=jupyter&utm\_content=flyout

https://app.readthedocs.org/projects/jupyter/builds/?utm\_source=jupyter&utm\_content=flyout

Addons documentation

https://docs.readthedocs.io/page/addons.html?utm\_source=jupyter&utm\_content=flyout

― Hosted by

Read the Docs

https://about.readthedocs.com/?utm\_source=jupyter&utm\_content=flyout

No recent searches

to navigate

Search powered by

