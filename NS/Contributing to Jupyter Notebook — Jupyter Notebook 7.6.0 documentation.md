---
sourceFile: "Contributing to Jupyter Notebook — Jupyter Notebook 7.6.0 documentation"
exportedBy: "Kortex"
exportDate: "2026-06-26T04:27:51.177Z"
---

# Contributing to Jupyter Notebook — Jupyter Notebook 7.6.0 documentation

7898ce58-0000-4462-b84a-121e71f2d13c

Contributing to Jupyter Notebook — Jupyter Notebook 7.6.0 documentation

4e624fe0-8441-4e30-b3d7-1530a8435e8b

https://jupyter-notebook.readthedocs.io/en/stable/contributing.html

Contributing to Jupyter Notebook — Jupyter Notebook 7.6.0 documentation

Skip to main content

https://jupyter-notebook.readthedocs.io/en/stable/contributing.html#main-content

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

Contributor Documentation

Contributing to Jupyter Notebook

https://jupyter-notebook.readthedocs.io/en/stable/contributing.html

Developer FAQ

https://jupyter-notebook.readthedocs.io/en/stable/development\_faq.html

$ lightcone run "what can I do for you?" — agents that actually act. Try the API →

https://server.ethicalads.io/proxy/click/10604/019f0192-a135-71d3-b7a2-9c4242c9dea1/

Ad by EthicalAds

https://www.ethicalads.io/advertisers/topics/data-science/?ref=rtd-sidebar-buy-ads

Contributing

https://jupyter-notebook.readthedocs.io/en/stable/contributor.html

Contributing to Jupyter Notebook

Contributing to Jupyter Notebook

https://jupyter-notebook.readthedocs.io/en/stable/contributing.html#contributing-to-jupyter-notebook

Thanks for contributing to Jupyter Notebook!

Make sure to follow

Project Jupyter's Code of Conduct

https://jupyter.org/governance/conduct/code-of-conduct

for a friendly and welcoming collaborative environment.

Setting up a development environment

https://jupyter-notebook.readthedocs.io/en/stable/contributing.html#setting-up-a-development-environment

Note: You will need NodeJS to build the extension package.

command is Jupyter's pinned version of

https://yarnpkg.com/

that is installed with Jupyter Builder. You may use

: we recommend using

to speed up the creation of the environment.

# create a new environment
mamba create -n notebook -c conda-forge python nodejs -y

# activate the environment
mamba activate notebook

# Install package in development mode
pip install -e ".\[dev,docs,test\]"

# Install dependencies and build packages
jlpm
jlpm build

# Link the notebook extension and @jupyter-notebook schemas
jlpm develop

# Enable the server extension
jupyter server extension enable notebook

follows a monorepo structure. To build all the packages at once:

There is also a

script to watch for changes and rebuild the app automatically:

To make sure the

server extension is installed:

$ jupyter server extension list
Config dir: /home/username/.jupyter

Config dir: /home/username/miniforge3/envs/notebook/etc/jupyter
    jupyterlab enabled
    - Validating jupyterlab...
      jupyterlab 3.0.0 OK
    notebook enabled
    - Validating notebook...
      notebook 7.0.0a0 OK

Config dir: /usr/local/etc/jupyter

#### Then start Jupyter Notebook with:

jupyter notebook

Local changes in Notebook dependencies

https://jupyter-notebook.readthedocs.io/en/stable/contributing.html#local-changes-in-notebook-dependencies

The development installation described above fetches JavaScript dependencies from

, according to the versions in the

package.json

file. However, it is sometimes useful to be able to test changes in Notebook, with dependencies (e.g.

@jupyterlab

packages) that have not yet been published.

https://github.com/wclr/yalc

can help you use local JavaScript packages when building Notebook, acting as a local package repository.

#### Install yalc globally in your environment:

npm install -g yalc

#### Publish your dependency package:

yalc publish

, from the package root directory. For instance, if you are developing on

@jupyterlab/ui-components

, this command must be executed from

path\_to\_jupyterlab/packages/ui-components

#### Depend on this local repository in Notebook:

from the Notebook root directory:

yalc add your\_package

: this will create a

dependencies

entry in the main

package.json

file. With the previous example, it would be

yalc add @jupyterlab/ui-components

Notebook is a monorepo, so we want this dependency to be 'linked' as a resolution (for all sub-packages) instead of a dependency. The easiest way is to manually move the new entry in

package.json

dependencies

resolutions

#### Build Notebook with the local dependency:

jlpm install && jlpm build

Changes in the dependency must then be built and pushed using

jlpm build && yalc push

(from the package root directory), and fetched from Notebook using

yarn install

: you need to make sure that the dependencies of Notebook and the local package match correctly, otherwise there will be errors with webpack during build.

In the previous example, both

@jupyterlab/ui-components

and Notebook depend on

@jupyterlab/coreutils

. We strongly advise you to depend on the same version.

Running Tests

https://jupyter-notebook.readthedocs.io/en/stable/contributing.html#running-tests

#### To run the tests:

jlpm run build:test
jlpm run test

There are also end to end tests to cover higher level user interactions, located in the

folder. To run these tests:

cd ui-tests
#install required packages for jlpm
jlpm

#install playwright
jlpm playwright install

# start a new Jupyter server in a terminal
jlpm start

# in a new terminal, run the tests
jlpm test

script calls the Playwright test runner. You can pass additional arguments to

by appending parameters to the command. For example to run the test in headed mode,

jlpm test --headed

Check out the

Playwright Command Line Reference

https://playwright.dev/docs/test-cli/

for more information about the available command line options.

Running the end to end tests in headful mode will trigger something like the following:

Updating reference snapshots

https://jupyter-notebook.readthedocs.io/en/stable/contributing.html#updating-reference-snapshots

Often a PR might make changes to the user interface, which can cause the visual regression tests to fail.

If you want to update the reference snapshots while working on a PR you can post the following sentence as a GitHub comment:

bot please update playwright snapshots

This will trigger a GitHub Action that will run the UI tests automatically and push new commits to the branch if the reference snapshots have changed.

Code Styling

https://jupyter-notebook.readthedocs.io/en/stable/contributing.html#code-styling

All non-python source code is formatted using

https://prettier.io/

and python source code is formatted using

https://github.com/psf/black

. When code is modified and committed, all staged files will be automatically formatted using pre-commit git hooks (with help from

https://github.com/pre-commit/pre-commit

. The benefit of using code formatters like

is that it removes the topic of code style from the conversation when reviewing pull requests, thereby speeding up the review process.

As long as your code is valid, the pre-commit hook should take care of how it should look.

and its associated hooks will automatically be installed when you run

pip install -e ".\[dev,test\]"

manually, run the following:

pip install pre-commit
pre-commit install

#### You can invoke the pre-commit hook by hand at any time with:

pre-commit run

which should run any autoformatting on your code and tell you about any errors it couldn't fix automatically. You may also install

black integration

https://github.com/psf/black#editor-integration

into your text editor to format code automatically.

If you have already committed files before setting up the pre-commit hook with

pre-commit install

, you can fix everything up using

pre-commit run --all-files

. You need to make the fixing commit yourself after that.

You may also use the prettier npm script (e.g.

npm run prettier

yarn prettier

jlpm prettier

) to format the entire code base. We recommend installing a prettier extension for your code editor and configuring it to format your code with a keyboard shortcut, or automatically on save.

Some of the hooks only run on CI by default, but you can invoke them by running with the

--hook-stage manual

Documentation

https://jupyter-notebook.readthedocs.io/en/stable/contributing.html#documentation

First make sure you have set up a development environment as described above.

#### Then run the following command to build the docs:

hatch run docs:build

In a separate terminal window, run the following command to serve the documentation:

hatch run docs:serve

Now open a web browser and navigate to

http://localhost:8000

to access the documentation.

Contributing from the browser

https://jupyter-notebook.readthedocs.io/en/stable/contributing.html#contributing-from-the-browser

Alternatively you can also contribute to Jupyter Notebook without setting up a local environment, directly from a web browser:

GitHub CodeSpaces

https://github.com/codespaces

is directly integrated into GitHub. This repository uses the

https://pixi.sh/

package manager to set up the development environment. To contribute after the Codespace is started:

in a terminal to activate the development environment

Use the commands above for building the extension and running the tests, for example:

#### To start the application:

pixi run start

. A popup should appear with a button to open the Jupyter Notebook in a new browser tab. If the popup does not appear, you can navigate to the “Forwarded ports” panel to find the URL to the application.

built-in editor

https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files

is suitable for contributing small fixes.

A more advanced

https://docs.github.com/en/codespaces/the-githubdev-web-based-editor

editor can be accessed by pressing the dot (.) key while in the Jupyter Notebook GitHub repository

previous Contributing

https://jupyter-notebook.readthedocs.io/en/stable/contributor.html

next Developer FAQ

https://jupyter-notebook.readthedocs.io/en/stable/development\_faq.html

On this page

Setting up a development environment

https://jupyter-notebook.readthedocs.io/en/stable/contributing.html#setting-up-a-development-environment

Local changes in Notebook dependencies

https://jupyter-notebook.readthedocs.io/en/stable/contributing.html#local-changes-in-notebook-dependencies

Running Tests

https://jupyter-notebook.readthedocs.io/en/stable/contributing.html#running-tests

Updating reference snapshots

https://jupyter-notebook.readthedocs.io/en/stable/contributing.html#updating-reference-snapshots

Code Styling

https://jupyter-notebook.readthedocs.io/en/stable/contributing.html#code-styling

Documentation

https://jupyter-notebook.readthedocs.io/en/stable/contributing.html#documentation

Contributing from the browser

https://jupyter-notebook.readthedocs.io/en/stable/contributing.html#contributing-from-the-browser

Edit on GitHub

https://github.com/jupyter/notebook/edit/main/docs/source/contributing.md

Show Source

https://jupyter-notebook.readthedocs.io/en/stable/\_sources/contributing.md.txt

© Copyright 2015, Jupyter Team, https://jupyter.org.

Created using

https://www.sphinx-doc.org/

Built with the

PyData Sphinx Theme

https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html

https://jupyter-notebook.readthedocs.io/en/master/contributing.html

https://jupyter-notebook.readthedocs.io/en/latest/contributing.html

https://jupyter-notebook.readthedocs.io/en/v7.6.0/contributing.html

https://jupyter-notebook.readthedocs.io/en/v7.5.7/contributing.html

https://jupyter-notebook.readthedocs.io/en/v7.5.6/contributing.html

https://jupyter-notebook.readthedocs.io/en/v7.5.5/contributing.html

https://jupyter-notebook.readthedocs.io/en/v7.5.4/contributing.html

https://jupyter-notebook.readthedocs.io/en/v7.5.3/contributing.html

https://jupyter-notebook.readthedocs.io/en/v7.5.2/contributing.html

https://jupyter-notebook.readthedocs.io/en/v7.5.1/contributing.html

https://jupyter-notebook.readthedocs.io/en/v7.5.0/contributing.html

https://jupyter-notebook.readthedocs.io/en/v7.4.7/contributing.html

https://jupyter-notebook.readthedocs.io/en/v7.4.6/contributing.html

https://jupyter-notebook.readthedocs.io/en/v7.4.5/contributing.html

https://jupyter-notebook.readthedocs.io/en/v7.4.4/contributing.html

https://jupyter-notebook.readthedocs.io/en/v7.4.3/contributing.html

https://jupyter-notebook.readthedocs.io/en/v7.4.2/contributing.html

https://jupyter-notebook.readthedocs.io/en/v7.4.1/contributing.html

https://jupyter-notebook.readthedocs.io/en/v7.4.0/contributing.html

https://jupyter-notebook.readthedocs.io/en/v7.3.3/contributing.html

https://jupyter-notebook.readthedocs.io/en/v7.3.2/contributing.html

https://jupyter-notebook.readthedocs.io/en/v7.3.1/contributing.html

https://jupyter-notebook.readthedocs.io/en/v7.3.0/contributing.html

https://jupyter-notebook.readthedocs.io/en/v7.2.2/contributing.html

https://jupyter-notebook.readthedocs.io/en/v7.2.1/contributing.html

https://jupyter-notebook.readthedocs.io/en/v7.2.0/contributing.html

https://jupyter-notebook.readthedocs.io/en/v7.1.3/contributing.html

https://jupyter-notebook.readthedocs.io/en/v7.1.2/contributing.html

https://jupyter-notebook.readthedocs.io/en/v7.1.1/contributing.html

https://jupyter-notebook.readthedocs.io/en/v7.0.8/contributing.html

https://jupyter-notebook.readthedocs.io/en/v7.0.7/contributing.html

https://jupyter-notebook.readthedocs.io/en/v7.0.6/contributing.html

https://jupyter-notebook.readthedocs.io/en/v7.0.5/contributing.html

https://jupyter-notebook.readthedocs.io/en/v7.0.4/contributing.html

https://jupyter-notebook.readthedocs.io/en/v7.0.3/contributing.html

https://jupyter-notebook.readthedocs.io/en/v7.0.2/contributing.html

https://jupyter-notebook.readthedocs.io/en/v7.0.1/contributing.html

https://jupyter-notebook.readthedocs.io/en/v7.0.0/contributing.html

https://jupyter-notebook.readthedocs.io/en/v6.5.4/contributing.html

https://jupyter-notebook.readthedocs.io/en/v6.5.3/contributing.html

https://jupyter-notebook.readthedocs.io/en/v6.5.2/contributing.html

https://jupyter-notebook.readthedocs.io/en/v6.5.1/contributing.html

https://jupyter-notebook.readthedocs.io/en/v6.5.0/contributing.html

https://jupyter-notebook.readthedocs.io/en/6.4.12/contributing.html

https://jupyter-notebook.readthedocs.io/en/v6.4.11/contributing.html

https://jupyter-notebook.readthedocs.io/en/6.4.10/contributing.html

https://jupyter-notebook.readthedocs.io/en/v6.4.9/contributing.html

https://jupyter-notebook.readthedocs.io/en/v6.4.8/contributing.html

https://jupyter-notebook.readthedocs.io/en/v6.4.7/contributing.html

https://jupyter-notebook.readthedocs.io/en/v6.4.6/contributing.html

https://jupyter-notebook.readthedocs.io/en/v6.4.5/contributing.html

https://jupyter-notebook.readthedocs.io/en/v6.4.4/contributing.html

https://jupyter-notebook.readthedocs.io/en/6.2.0/contributing.html

https://jupyter-notebook.readthedocs.io/en/5.7.6/contributing.html

https://jupyter-notebook.readthedocs.io/en/5.7.5/contributing.html

https://jupyter-notebook.readthedocs.io/en/5.7.4/contributing.html

https://jupyter-notebook.readthedocs.io/en/5.7.3/contributing.html

https://jupyter-notebook.readthedocs.io/en/5.7.2/contributing.html

https://jupyter-notebook.readthedocs.io/en/5.7.1/contributing.html

https://jupyter-notebook.readthedocs.io/en/5.7.0/contributing.html

https://jupyter-notebook.readthedocs.io/en/5.6.0/contributing.html

https://jupyter-notebook.readthedocs.io/en/5.5.0/contributing.html

https://jupyter-notebook.readthedocs.io/en/5.4.1/contributing.html

https://jupyter-notebook.readthedocs.io/en/5.4.0/contributing.html

https://jupyter-notebook.readthedocs.io/en/5.3.1/contributing.html

https://jupyter-notebook.readthedocs.io/en/5.2.2/contributing.html

https://jupyter-notebook.readthedocs.io/en/5.1.0/contributing.html

https://jupyter-notebook.readthedocs.io/en/5.0.0/contributing.html

https://jupyter-notebook.readthedocs.io/en/4.x/contributing.html

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

