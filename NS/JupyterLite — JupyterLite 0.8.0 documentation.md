---
sourceFile: "JupyterLite — JupyterLite 0.8.0 documentation"
exportedBy: "Kortex"
exportDate: "2026-06-26T04:27:51.451Z"
---

# JupyterLite — JupyterLite 0.8.0 documentation

a4d6fe1d-093b-499c-9c84-4275d4cbe7da

JupyterLite — JupyterLite 0.8.0 documentation

670857d3-05cc-444d-8d52-447359be2c52

https://jupyterlite.readthedocs.io/en/latest/

JupyterLite — JupyterLite 0.8.0 documentation

Skip to main content

https://jupyterlite.readthedocs.io/en/latest/#main-content

Back to top

JupyterLiteJupyterLite

https://jupyterlite.readthedocs.io/en/latest/

https://jupyterlite.readthedocs.io/en/latest/index.html

https://jupyterlite.readthedocs.io/en/stable/index.html

Get Started

https://jupyterlite.readthedocs.io/en/latest/quickstart/index.html

How-To Guides

https://jupyterlite.readthedocs.io/en/latest/howto/index.html

https://jupyterlite.readthedocs.io/en/latest/reference/index.html

Troubleshooting

https://jupyterlite.readthedocs.io/en/latest/troubleshooting.html

Migration Guide

https://jupyterlite.readthedocs.io/en/latest/migration.html

Contributing

https://jupyterlite.readthedocs.io/en/latest/contributing.html

https://jupyterlite.readthedocs.io/en/latest/changelog.html

System Settings

https://github.com/jupyterlite/jupyterlite

https://pypi.org/project/jupyterlite

Get Started

https://jupyterlite.readthedocs.io/en/latest/quickstart/index.html

How-To Guides

https://jupyterlite.readthedocs.io/en/latest/howto/index.html

https://jupyterlite.readthedocs.io/en/latest/reference/index.html

Troubleshooting

https://jupyterlite.readthedocs.io/en/latest/troubleshooting.html

Migration Guide

https://jupyterlite.readthedocs.io/en/latest/migration.html

Contributing

https://jupyterlite.readthedocs.io/en/latest/contributing.html

https://jupyterlite.readthedocs.io/en/latest/changelog.html

System Settings

https://github.com/jupyterlite/jupyterlite

https://pypi.org/project/jupyterlite

$ lightcone run "what can I do for you?" — agents that actually act. Try the API →

https://server.ethicalads.io/proxy/click/10604/019f0192-d7e3-7cc2-8923-8ac28f3f32ae/

Ad by EthicalAds

https://www.ethicalads.io/advertisers/topics/data-science/?ref=rtd-sidebar-buy-ads

Open demo in a new tab

https://jupyterlite.readthedocs.io/en/latest/\_static/lab/index.html

Jupyter Notebook

https://jupyterlite.readthedocs.io/en/latest/\_static/notebooks/index.html?path=intro.ipynb

https://jupyterlite.readthedocs.io/en/latest/\_static/repl/index.html?toolbar=1&kernel=python&code=import%20this

JupyterLite

https://jupyterlite.readthedocs.io/en/latest/#jupyterlite

JupyterLite is a JupyterLab distribution that

runs entirely in the browser

built from the ground-up using JupyterLab components and extensions.

https://jupyterlite.readthedocs.io/en/latest/#status

JupyterLite is part of the

Project Jupyter

https://jupyter.org/

Frontends subproject

https://jupyterlab-team-compass.readthedocs.io/

Not all the features available in JupyterLab and the Classic Notebook will work with JupyterLite, but many do!

Don't hesitate to check out the

documentation

https://jupyterlite.readthedocs.io/en/stable/howto/index.html

for more information and project updates.

✨ Try it in your browser ✨

https://jupyterlite.readthedocs.io/en/latest/#try-it-in-your-browser

JupyterLite works with both the

https://github.com/jupyterlab/jupyterlab

Jupyter Notebook

https://github.com/jupyter/notebook

interfaces.

Try it with JupyterLab

https://jupyterlite.readthedocs.io/en/stable/try/lab

Try it with Jupyter Notebook

https://jupyterlite.readthedocs.io/en/stable/try/tree

🏗 Build your own JupyterLite 🏗

https://jupyterlite.readthedocs.io/en/latest/#build-your-own-jupyterlite

You can build your own JupyterLite website in a couple of minutes, with custom extensions and packages.

documentation

https://jupyterlite.readthedocs.io/en/stable/quickstart/deploy.html

for more details.

Browser-based Interactive Computing

https://jupyterlite.readthedocs.io/en/latest/#browser-based-interactive-computing

#### JupyterLite is all about accessible browser-based interactive computing:

#### Python kernels running in a Web Worker:

https://pyodide.org/

jupyterlite-pyodide-kernel

https://github.com/jupyterlite/pyodide-kernel

Xeus Python

https://xeus-python.readthedocs.io/en/latest/

jupyterlite-xeus

https://github.com/jupyterlite/xeus

Support for interactive visualization libraries such as

View hosted example Notebooks and other files, then edit, save, and download from the browser's

localStorage

Support for saving settings for JupyterLab/Lite core and federated extensions

Basic session and kernel management to have multiple kernels running at the same time

Support for

Code Consoles

https://jupyterlab.readthedocs.io/en/stable/user/code\_console.html

Ease of Deployment

https://jupyterlite.readthedocs.io/en/latest/#ease-of-deployment

Served via well-cacheable, static HTTP(S), locally or on most static web hosts

Embeddable within larger applications

Requires no dedicated

application server

much less a container orchestrator

Fine-grained configurability of page settings, including reuse of federated JupyterLab extensions

Version Compatibility

https://jupyterlite.readthedocs.io/en/latest/#version-compatibility

The table below shows the versions of JupyterLab and Jupyter Notebook bundled with each JupyterLite core release.

jupyterlite-core

Only the last two releases are actively supported.

Development install

https://jupyterlite.readthedocs.io/en/latest/#development-install

contributing guide

https://github.com/jupyterlite/jupyterlite/blob/main/CONTRIBUTING.md

for a development installation.

https://jupyterlite.readthedocs.io/en/latest/#related

JupyterLite is a reboot of several attempts at making a full static Jupyter distribution that runs in the browser, without having to start the Python Jupyter Server on the host machine.

The goal is to provide a lightweight computing environment accessible in a matter of seconds with a single click, in a web browser and without having to install anything.

This project is a collection of packages that can be remixed together in variety of ways to create new applications and distributions. Most of the packages in this repo focus on providing server-like components that run in the browser (to manage kernels, files and settings), so existing JupyterLab extensions and plugins can be reused out of the box.

p5-notebook

https://github.com/jtpio/p5-notebook

: A minimal Jupyter Notebook UI for p5.js kernels running in the browser

https://github.com/deathbeds/jyve

: Jupyter Kernels, right inside JupyterLab

Starboard Notebook

https://github.com/gzuidhof/starboard-notebook

: In-browser literal notebooks

https://basthon.fr/

: A Jupyter notebook implementation using Pyodide

Notebook.link

https://notebook.link/

: A cloud-backed, in-browser notebook platform based on JupyterLite

👥 Contributors

https://jupyterlite.readthedocs.io/en/latest/#contributors

Join our community and become a contributor today! 🚀

Documentation Contents

https://jupyterlite.readthedocs.io/en/latest/#documentation-contents

Get Started

https://jupyterlite.readthedocs.io/en/latest/quickstart/index.html

Using an existing JupyterLite deployment

https://jupyterlite.readthedocs.io/en/latest/quickstart/using.html

Deploy your first JupyterLite website on GitHub Pages

https://jupyterlite.readthedocs.io/en/latest/quickstart/deploy.html

Embed a live REPL on a website

https://jupyterlite.readthedocs.io/en/latest/quickstart/embed-repl.html

Deploy JupyterLite on a standalone server or locally

https://jupyterlite.readthedocs.io/en/latest/quickstart/standalone.html

Configure a JupyterLite site

https://jupyterlite.readthedocs.io/en/latest/quickstart/configure.html

How-To Guides

https://jupyterlite.readthedocs.io/en/latest/howto/index.html

Configuring a JupyterLite deployment

https://jupyterlite.readthedocs.io/en/latest/howto/index.html#configuring-a-jupyterlite-deployment

https://jupyterlite.readthedocs.io/en/latest/howto/index.html#contents

Configuring the Pyodide kernel

https://jupyterlite.readthedocs.io/en/latest/howto/index.html#configuring-the-pyodide-kernel

Configuring the Xeus Python kernel

https://jupyterlite.readthedocs.io/en/latest/howto/index.html#configuring-the-xeus-python-kernel

Configuring the Xeus R kernel

https://jupyterlite.readthedocs.io/en/latest/howto/index.html#configuring-the-xeus-r-kernel

https://jupyterlite.readthedocs.io/en/latest/howto/index.html#deploying

https://jupyterlite.readthedocs.io/en/latest/howto/index.html#extensions

Advanced configuration

https://jupyterlite.readthedocs.io/en/latest/howto/index.html#advanced-configuration

https://jupyterlite.readthedocs.io/en/latest/reference/index.html

Runtime Configuration Files

https://jupyterlite.readthedocs.io/en/latest/reference/config.html

https://jupyterlite.readthedocs.io/en/latest/reference/schema.html

https://jupyterlite.readthedocs.io/en/latest/reference/cli.html

https://jupyterlite.readthedocs.io/en/latest/reference/api/index.html

Architecture

https://jupyterlite.readthedocs.io/en/latest/reference/architecture.html

https://jupyterlite.readthedocs.io/en/latest/reference/contents.html

https://jupyterlite.readthedocs.io/en/latest/reference/doit.html

About the Demo

https://jupyterlite.readthedocs.io/en/latest/reference/demo.html

Troubleshooting

https://jupyterlite.readthedocs.io/en/latest/troubleshooting.html

Not able to access files from the kernel

https://jupyterlite.readthedocs.io/en/latest/troubleshooting.html#not-able-to-access-files-from-the-kernel

Clear the browser data

https://jupyterlite.readthedocs.io/en/latest/troubleshooting.html#clear-the-browser-data

Package compatibility with WebAssembly kernels

https://jupyterlite.readthedocs.io/en/latest/troubleshooting.html#package-compatibility-with-webassembly-kernels

Access kernel logs

https://jupyterlite.readthedocs.io/en/latest/troubleshooting.html#access-kernel-logs

Migration Guide

https://jupyterlite.readthedocs.io/en/latest/migration.html

v0.7.0 to v0.8.0

https://jupyterlite.readthedocs.io/en/latest/migration.html#v0-7-0-to-v0-8-0

v0.6.0 to v0.7.0

https://jupyterlite.readthedocs.io/en/latest/migration.html#v0-6-0-to-v0-7-0

v0.5.0 to v0.6.0

https://jupyterlite.readthedocs.io/en/latest/migration.html#v0-5-0-to-v0-6-0

v0.4.0 to v0.5.0

https://jupyterlite.readthedocs.io/en/latest/migration.html#v0-4-0-to-v0-5-0

v0.3.0 to v0.4.0

https://jupyterlite.readthedocs.io/en/latest/migration.html#v0-3-0-to-v0-4-0

v0.2.0 to v0.3.0

https://jupyterlite.readthedocs.io/en/latest/migration.html#v0-2-0-to-v0-3-0

v0.1.0 to v0.2.0

https://jupyterlite.readthedocs.io/en/latest/migration.html#v0-1-0-to-v0-2-0

0.1.0b19 to 0.1.0b20

https://jupyterlite.readthedocs.io/en/latest/migration.html#b19-to-0-1-0b20

0.1.0b18 to 0.1.0b19

https://jupyterlite.readthedocs.io/en/latest/migration.html#b18-to-0-1-0b19

0.1.0b17 to 0.1.0b18

https://jupyterlite.readthedocs.io/en/latest/migration.html#b17-to-0-1-0b18

0.1.0b16 to 0.1.0b17

https://jupyterlite.readthedocs.io/en/latest/migration.html#b16-to-0-1-0b17

Contributing

https://jupyterlite.readthedocs.io/en/latest/contributing.html

https://jupyterlite.readthedocs.io/en/latest/contributing.html#setup

Development Workflow

https://jupyterlite.readthedocs.io/en/latest/contributing.html#development-workflow

https://jupyterlite.readthedocs.io/en/latest/contributing.html#testing

https://jupyterlite.readthedocs.io/en/latest/changelog.html

https://jupyterlite.readthedocs.io/en/latest/changelog.html#v0-8

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id1

https://jupyterlite.readthedocs.io/en/latest/changelog.html#rc0

https://jupyterlite.readthedocs.io/en/latest/changelog.html#b1

https://jupyterlite.readthedocs.io/en/latest/changelog.html#b0

https://jupyterlite.readthedocs.io/en/latest/changelog.html#a2

https://jupyterlite.readthedocs.io/en/latest/changelog.html#a1

https://jupyterlite.readthedocs.io/en/latest/changelog.html#a0

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id30

https://jupyterlite.readthedocs.io/en/latest/changelog.html#v0-7

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id35

https://jupyterlite.readthedocs.io/en/latest/changelog.html#rc2

https://jupyterlite.readthedocs.io/en/latest/changelog.html#rc1

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id48

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id54

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id58

https://jupyterlite.readthedocs.io/en/latest/changelog.html#a7

https://jupyterlite.readthedocs.io/en/latest/changelog.html#a6

https://jupyterlite.readthedocs.io/en/latest/changelog.html#a5

https://jupyterlite.readthedocs.io/en/latest/changelog.html#a4

https://jupyterlite.readthedocs.io/en/latest/changelog.html#a3

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id81

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id84

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id89

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id94

https://jupyterlite.readthedocs.io/en/latest/changelog.html#v0-6

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id104

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id108

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id114

https://jupyterlite.readthedocs.io/en/latest/changelog.html#a10

https://jupyterlite.readthedocs.io/en/latest/changelog.html#a9

https://jupyterlite.readthedocs.io/en/latest/changelog.html#a8

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id130

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id133

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id138

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id142

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id145

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id151

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id156

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id160

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id164

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id170

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id173

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id177

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id180

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id185

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id188

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id192

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id196

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id200

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id206

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id210

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id217

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id222

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id227

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id230

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id233

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id237

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id242

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id247

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id253

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id257

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id261

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id265

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id270

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id275

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id279

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id284

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id289

✨ Highlights ✨

https://jupyterlite.readthedocs.io/en/latest/changelog.html#highlights

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id296

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id300

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id305

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id309

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id314

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id319

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id323

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id328

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id333

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id338

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id343

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id348

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id351

https://jupyterlite.readthedocs.io/en/latest/changelog.html#b22

https://jupyterlite.readthedocs.io/en/latest/changelog.html#b21

https://jupyterlite.readthedocs.io/en/latest/changelog.html#b20

https://jupyterlite.readthedocs.io/en/latest/changelog.html#b19

https://jupyterlite.readthedocs.io/en/latest/changelog.html#b18

https://jupyterlite.readthedocs.io/en/latest/changelog.html#b17

https://jupyterlite.readthedocs.io/en/latest/changelog.html#b16

https://jupyterlite.readthedocs.io/en/latest/changelog.html#b15

https://jupyterlite.readthedocs.io/en/latest/changelog.html#b14

https://jupyterlite.readthedocs.io/en/latest/changelog.html#b13

https://jupyterlite.readthedocs.io/en/latest/changelog.html#b12

https://jupyterlite.readthedocs.io/en/latest/changelog.html#b11

https://jupyterlite.readthedocs.io/en/latest/changelog.html#b10

https://jupyterlite.readthedocs.io/en/latest/changelog.html#b9

https://jupyterlite.readthedocs.io/en/latest/changelog.html#b8

https://jupyterlite.readthedocs.io/en/latest/changelog.html#b7

https://jupyterlite.readthedocs.io/en/latest/changelog.html#b6

https://jupyterlite.readthedocs.io/en/latest/changelog.html#b5

https://jupyterlite.readthedocs.io/en/latest/changelog.html#b4

https://jupyterlite.readthedocs.io/en/latest/changelog.html#b3

https://jupyterlite.readthedocs.io/en/latest/changelog.html#b2

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id440

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id444

https://jupyterlite.readthedocs.io/en/latest/changelog.html#a24

https://jupyterlite.readthedocs.io/en/latest/changelog.html#a23

https://jupyterlite.readthedocs.io/en/latest/changelog.html#a22

https://jupyterlite.readthedocs.io/en/latest/changelog.html#a21

https://jupyterlite.readthedocs.io/en/latest/changelog.html#a20

https://jupyterlite.readthedocs.io/en/latest/changelog.html#a19

https://jupyterlite.readthedocs.io/en/latest/changelog.html#a18

https://jupyterlite.readthedocs.io/en/latest/changelog.html#a17

https://jupyterlite.readthedocs.io/en/latest/changelog.html#a16

https://jupyterlite.readthedocs.io/en/latest/changelog.html#a15

https://jupyterlite.readthedocs.io/en/latest/changelog.html#a14

https://jupyterlite.readthedocs.io/en/latest/changelog.html#a13

https://jupyterlite.readthedocs.io/en/latest/changelog.html#a12

https://jupyterlite.readthedocs.io/en/latest/changelog.html#a11

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id501

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id507

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id514

https://jupyterlite.readthedocs.io/en/latest/changelog.html#id518

https://jupyterlite.readthedocs.io/en/latest/changelog.html#v0-1-0a6

https://jupyterlite.readthedocs.io/en/latest/changelog.html#v0-1-0a5

https://jupyterlite.readthedocs.io/en/latest/changelog.html#v0-1-0a4

https://jupyterlite.readthedocs.io/en/latest/changelog.html#v0-1-0a3

https://jupyterlite.readthedocs.io/en/latest/changelog.html#v0-1-0a2

https://jupyterlite.readthedocs.io/en/latest/changelog.html#v0-1-0a1

https://jupyterlite.readthedocs.io/en/latest/changelog.html#v0-1-0a0

next Get Started

https://jupyterlite.readthedocs.io/en/latest/quickstart/index.html

On this page

https://jupyterlite.readthedocs.io/en/latest/#status

✨ Try it in your browser ✨

https://jupyterlite.readthedocs.io/en/latest/#try-it-in-your-browser

🏗 Build your own JupyterLite 🏗

https://jupyterlite.readthedocs.io/en/latest/#build-your-own-jupyterlite

Browser-based Interactive Computing

https://jupyterlite.readthedocs.io/en/latest/#browser-based-interactive-computing

Ease of Deployment

https://jupyterlite.readthedocs.io/en/latest/#ease-of-deployment

Version Compatibility

https://jupyterlite.readthedocs.io/en/latest/#version-compatibility

Development install

https://jupyterlite.readthedocs.io/en/latest/#development-install

https://jupyterlite.readthedocs.io/en/latest/#related

👥 Contributors

https://jupyterlite.readthedocs.io/en/latest/#contributors

Documentation Contents

https://jupyterlite.readthedocs.io/en/latest/#documentation-contents

Edit on GitHub

https://github.com/jupyterlite/jupyterlite/edit/main/docs/index.md

Show Source

https://jupyterlite.readthedocs.io/en/latest/\_sources/index.md.txt

© Copyright 2021-, JupyterLite Contributors.

Created using

https://www.sphinx-doc.org/

Built with the

PyData Sphinx Theme

https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html

