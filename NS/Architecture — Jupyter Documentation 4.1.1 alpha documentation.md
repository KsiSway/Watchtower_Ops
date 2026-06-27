---
sourceFile: "Architecture — Jupyter Documentation 4.1.1 alpha documentation"
exportedBy: "Kortex"
exportDate: "2026-06-26T04:27:51.060Z"
---

# Architecture — Jupyter Documentation 4.1.1 alpha documentation

b089af45-5577-435a-bca3-9d75fa96e73c

Architecture — Jupyter Documentation 4.1.1 alpha documentation

bd6e8eda-3cd6-44f3-9dc0-6d613213a675

https://docs.jupyter.org/en/latest/projects/architecture/content-architecture.html

Architecture — Jupyter Documentation 4.1.1 alpha documentation

Skip to main content

https://docs.jupyter.org/en/latest/projects/architecture/content-architecture.html#main-content

Back to top

Jupyter Documentation 4.1.1 alpha documentation - HomeJupyter Documentation 4.1.1 alpha documentation - Home

https://docs.jupyter.org/en/latest/index.html

Try Jupyter

https://docs.jupyter.org/en/latest/start/index.html

https://docs.jupyter.org/en/latest/use/using.html

https://docs.jupyter.org/en/latest/projects/content-projects.html

https://docs.jupyter.org/en/latest/community/content-community.html

Contributing

https://docs.jupyter.org/en/latest/contributing/content-contributor.html

https://docs.jupyter.org/en/latest/reference/content-reference.html

jupyter.org

https://jupyter.org/

System Settings

https://github.com/jupyter/jupyter

https://discourse.jupyter.org/

Try Jupyter

https://docs.jupyter.org/en/latest/start/index.html

https://docs.jupyter.org/en/latest/use/using.html

https://docs.jupyter.org/en/latest/projects/content-projects.html

https://docs.jupyter.org/en/latest/community/content-community.html

Contributing

https://docs.jupyter.org/en/latest/contributing/content-contributor.html

https://docs.jupyter.org/en/latest/reference/content-reference.html

jupyter.org

https://jupyter.org/

System Settings

https://github.com/jupyter/jupyter

https://discourse.jupyter.org/

Collapse Sidebar Expand Sidebar

Section Navigation

Jupyter User Interfaces

https://docs.jupyter.org/en/latest/projects/user-interfaces.html

Kernels (Programming Languages)

https://docs.jupyter.org/en/latest/projects/kernels.html

https://docs.jupyter.org/en/latest/projects/education.html

https://docs.jupyter.org/en/latest/projects/execution.html

Deployment and infrastructure

https://docs.jupyter.org/en/latest/projects/deployment.html

Formatting and Conversion

https://docs.jupyter.org/en/latest/projects/conversion.html

https://docs.jupyter.org/en/latest/projects/ipython\_projects.html

Core Building Blocks

https://docs.jupyter.org/en/latest/projects/core.html

Incubator Projects

https://docs.jupyter.org/en/latest/projects/incubator.html

Architecture

https://docs.jupyter.org/en/latest/projects/architecture/content-architecture.html

Project Documentation

https://docs.jupyter.org/en/latest/projects/doc-proj-categories.html

Release Notes

https://docs.jupyter.org/en/latest/releases.html

$ lightcone run "what can I do for you?" — agents that actually act. Try the API →

https://server.ethicalads.io/proxy/click/10604/019f0192-d7e3-7cc2-8923-8ac28f3f32ae/

Ad by EthicalAds

https://www.ethicalads.io/advertisers/topics/data-science/?ref=rtd-sidebar-buy-ads

https://docs.jupyter.org/en/latest/projects/content-projects.html

Architecture

Architecture

https://docs.jupyter.org/en/latest/projects/architecture/content-architecture.html#architecture

This page has information about the different architectural designs of core pieces in the Jupyter ecosystem. Some of these are individual projects, and others show the relationships between projects.

Projects overview

https://docs.jupyter.org/en/latest/projects/architecture/content-architecture.html#projects-overview

Below is a high level visual overview of project relationships. It is current as of 2022.

IPython Kernel

https://docs.jupyter.org/en/latest/projects/architecture/content-architecture.html#ipython-kernel

This section focuses on IPython and kernels. When we discuss

, we talk about two fundamental roles:

Terminal IPython as the familiar REPL

The IPython kernel,

that provides computation and communication with the frontend interfaces, like the notebook

Terminal IPython

https://docs.jupyter.org/en/latest/projects/architecture/content-architecture.html#terminal-ipython

When you type

, you get the original IPython interface, running in the terminal. It does something like this:

while True:
    code = input(">>> ")
    exec(code)

Of course, it's much more complex, because it has to deal with multi-line code, tab completion using

, magic commands, and so on. But the model is like code example: prompt the user for some code, and when they've entered it, execute it in the same process. This model is often called a

https://docs.jupyter.org/en/latest/glossary.html#term-REPL

, or Read-Eval-Print-Loop.

The IPython Kernel

https://docs.jupyter.org/en/latest/projects/architecture/content-architecture.html#the-ipython-kernel

All the other interfaces —- the Notebook, the Qt console,

ipython console

in the terminal, and third party interfaces —- use the IPython Kernel. IPykernel is a separate process which is responsible for running user code, and things like computing possible completions. Frontends, like the notebook or the Qt console, communicate with the IPython Kernel using JSON messages sent over

http://zeromq.org/

sockets; the protocol used between the frontends and the IPython Kernel is described in

Messaging in Jupyter

https://jupyter-client.readthedocs.io/en/latest/messaging.html#messaging

The core execution machinery for the kernel is shared with terminal IPython.

A kernel process can be connected to more than one frontend simultaneously. In this case, the different frontends will have access to the same variables.

This design was intended to allow easy development of different frontends based on the same kernel, but it also made it possible to support new languages in the same frontends, by developing kernels in those languages, and we are refining IPython to make that more practical.

#### Today, there are three ways to develop a kernel for another language:

Wrapper kernels reuse the communications machinery from IPykernel, and implement only the core execution part.

Native kernels implement execution and communications in the target language.

Kernels based on

https://github.com/jupyter-xeus/xeus

, a native implementation of the protocol, implement the language-specific part of the kernels. Contrary to the wrapper approach, xeus does not depend on a python runtime.

Wrapper kernels are easier to write quickly for languages that have good Python wrappers, like

octave\_kernel

https://pypi.python.org/pypi/octave\_kernel

, or languages where it's impractical to implement the communications machinery, like

bash\_kernel

https://pypi.python.org/pypi/bash\_kernel

. Native kernels are likely to be better maintained by the community using them, like

https://github.com/JuliaLang/IJulia.jl

https://github.com/gibiansky/IHaskell

. Xeus kernels are easy to write when the language interpreter provides a C++ or a C API.

Making kernels for Jupyter

https://jupyter-client.readthedocs.io/en/latest/kernels.html#kernels

https://docs.jupyter.org/en/latest/projects/kernels.html#kernels-langs

The Jupyter Notebook format

https://docs.jupyter.org/en/latest/projects/architecture/content-architecture.html#the-jupyter-notebook-format

Jupyter Notebooks are structured data that represent your code, metadata, content, and outputs. When saved to disk, the notebook uses the extension

, and uses a JSON structure. For more information about the notebook format structure and specification, see

the nbformat documentation

https://nbformat.readthedocs.io/en/latest/format\_description.html

The Jupyter Notebook Interface

https://docs.jupyter.org/en/latest/projects/architecture/content-architecture.html#the-jupyter-notebook-interface

Jupyter Notebook and its flexible interface extends the notebook beyond code to visualization, multimedia, collaboration, and more. In addition to running your code, it stores code and output, together with markdown notes, in an editable document called a notebook. When you save it, this is sent from your browser to the Jupyter server, which saves it on disk as a JSON file with a

The Jupyter server is a communication hub. The browser, notebook file on disk, and kernel cannot talk to each other directly. They communicate through the Jupyter server. The Jupyter server, not the kernel, is responsible for saving and loading notebooks, so you can edit notebooks even if you don't have the kernel for that language—you just won't be able to run code. The kernel doesn't know anything about the notebook document: it just gets sent cells of code to execute when the user runs them.

Exporting Jupyter Notebooks to other formats

https://docs.jupyter.org/en/latest/projects/architecture/content-architecture.html#exporting-jupyter-notebooks-to-other-formats

Nbconvert tool

https://nbconvert.readthedocs.io/en/latest/index.html

in Jupyter converts notebook files to other formats, such as HTML, LaTeX, or reStructuredText. This conversion goes through a series of steps:

Preprocessors modify the notebook in memory. E.g. ExecutePreprocessor runs the code in the notebook and updates the output.

An exporter converts the notebook to another file format. Most of the exporters use templates for this.

Postprocessors work on the file produced by exporting.

http://nbviewer.jupyter.org/

website uses nbconvert with the HTML exporter. When you give it a URL, it fetches the notebook from that URL, converts it to HTML, and serves that HTML to you.

IPython.parallel

https://docs.jupyter.org/en/latest/projects/architecture/content-architecture.html#ipython-parallel

IPython also includes a parallel computing framework,

IPython.parallel

https://ipyparallel.readthedocs.io/en/latest/

. This allows you to control many individual engines, which are an extended version of the IPython kernel described above.

JupyterHub and Binder

https://docs.jupyter.org/en/latest/projects/architecture/content-architecture.html#jupyterhub-and-binder

JupyterHub is a multi-user Hub that spawns, manages, and proxies multiple instances of the single-user Jupyter notebook server. This can be used to serve a variety of interfaces and environments, and can be run on many kinds of infrastructure. JupyterHub on Kubernetes is a Helm Chart for running JupyterHub on kubernetes infrastructure, and BinderHub is a customized JupyterHub deployment for shareable, reproducible interactive computing environments.

The links below describe the architecture of JupyterHub and several distributions of JupyterHub.

JupyterHub core architecture

https://jupyterhub.readthedocs.io/en/latest/reference/technical-overview.html

JupyterHub for Kubernetes architecture

BinderHub architecture

https://docs.jupyter.org/en/latest/projects/architecture/content-architecture.html#jupyterlab

JupyterLab is a flexible, extensible interface for interactive computing. Below are a few links that are useful for understanding the JupyterLab architecture.

JupyterLab document model

https://jupyterlab.readthedocs.io/en/latest/user/documents\_kernels.html#kernel-backed-documents

JupyterLab notebook model

https://jupyterlab.readthedocs.io/en/latest/user/commands.html#notebook

Design patterns in JupyterLab

https://jupyterlab.readthedocs.io/en/latest/developer/patterns.html

previous Incubator Projects

https://docs.jupyter.org/en/latest/projects/incubator.html

next Project Documentation

https://docs.jupyter.org/en/latest/projects/doc-proj-categories.html

On this page

Projects overview

https://docs.jupyter.org/en/latest/projects/architecture/content-architecture.html#projects-overview

IPython Kernel

https://docs.jupyter.org/en/latest/projects/architecture/content-architecture.html#ipython-kernel

Terminal IPython

https://docs.jupyter.org/en/latest/projects/architecture/content-architecture.html#terminal-ipython

The IPython Kernel

https://docs.jupyter.org/en/latest/projects/architecture/content-architecture.html#the-ipython-kernel

The Jupyter Notebook format

https://docs.jupyter.org/en/latest/projects/architecture/content-architecture.html#the-jupyter-notebook-format

The Jupyter Notebook Interface

https://docs.jupyter.org/en/latest/projects/architecture/content-architecture.html#the-jupyter-notebook-interface

Exporting Jupyter Notebooks to other formats

https://docs.jupyter.org/en/latest/projects/architecture/content-architecture.html#exporting-jupyter-notebooks-to-other-formats

IPython.parallel

https://docs.jupyter.org/en/latest/projects/architecture/content-architecture.html#ipython-parallel

JupyterHub and Binder

https://docs.jupyter.org/en/latest/projects/architecture/content-architecture.html#jupyterhub-and-binder

https://docs.jupyter.org/en/latest/projects/architecture/content-architecture.html#jupyterlab

Edit on GitHub

https://github.com/jupyter/jupyter/edit/master/docs/source/projects/architecture/content-architecture.rst

Show Source

https://docs.jupyter.org/en/latest/\_sources/projects/architecture/content-architecture.rst.txt

© Copyright 2015, Jupyter Team, https://jupyter.org.

Created using

https://www.sphinx-doc.org/

Built with the

PyData Sphinx Theme

https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html

https://docs.jupyter.org/es/latest/projects/architecture/content-architecture.html

https://docs.jupyter.org/pt-br/latest/projects/architecture/content-architecture.html

https://docs.jupyter.org/ru/latest/projects/architecture/content-architecture.html

https://docs.jupyter.org/en/stable/projects/architecture/content-architecture.html

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

