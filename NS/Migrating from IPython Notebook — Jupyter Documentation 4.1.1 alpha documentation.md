---
sourceFile: "Migrating from IPython Notebook — Jupyter Documentation 4.1.1 alpha documentation"
exportedBy: "Kortex"
exportDate: "2026-06-26T04:27:51.465Z"
---

# Migrating from IPython Notebook — Jupyter Documentation 4.1.1 alpha documentation

971f788e-b22c-4bca-8698-2f6a43445f5e

Migrating from IPython Notebook — Jupyter Documentation 4.1.1 alpha documentation

57591888-db28-48d8-81e1-9e6b6bbb5946

https://docs.jupyter.org/en/latest/use/advanced/migrating.html

Migrating from IPython Notebook — Jupyter Documentation 4.1.1 alpha documentation

Skip to main content

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#main-content

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

The jupyter Command

https://docs.jupyter.org/en/latest/use/jupyter-command.html

Common Directories and File Locations

https://docs.jupyter.org/en/latest/use/jupyter-directories.html

Jupyter's Common Configuration Approach

https://docs.jupyter.org/en/latest/use/config.html

Narratives and Use Cases

https://docs.jupyter.org/en/latest/use/use-cases/content-user.html

Notebook Narratives

https://docs.jupyter.org/en/latest/use/use-cases/narrative-notebook.html

JupyterHub Narratives

https://docs.jupyter.org/en/latest/use/use-cases/narrative-hub.html

Narratives - Building blocks

https://docs.jupyter.org/en/latest/use/use-cases/narrative-other.html

Jupyter for Data Science

https://docs.jupyter.org/en/latest/use/use-cases/data\_science.html

Jupyter and Scientific Computing

https://docs.jupyter.org/en/latest/use/use-cases/science.html

Jupyter in Education

https://docs.jupyter.org/en/latest/use/use-cases/education.html

Jupyter in the Enterprise

https://docs.jupyter.org/en/latest/use/use-cases/enterprise.html

Advanced Use Cases

https://docs.jupyter.org/en/latest/use/advanced/content-advanced.html

Migrating from IPython Notebook

https://docs.jupyter.org/en/latest/use/advanced/migrating.html

Ship agents that actually work — real workflows across every desktop app. Get started →

https://server.ethicalads.io/proxy/click/10607/019f0193-4dc4-7a90-833d-85200b4d1423/

Ad by EthicalAds

https://www.ethicalads.io/advertisers/topics/data-science/?ref=rtd-sidebar-buy-ads

https://docs.jupyter.org/en/latest/use/using.html

Advanced Use Cases

https://docs.jupyter.org/en/latest/use/advanced/content-advanced.html

Migrating from IPython Notebook

Migrating from IPython Notebook

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#migrating-from-ipython-notebook

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#abstract

Understanding the Migration Process

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#understanding-the-migration-process

Automatic migration of files

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#automatic-migration-of-files

Where have my configuration files gone?

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#where-have-my-configuration-files-gone

Finding the Location of Important Files

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#finding-the-location-of-important-files

Configuration files

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#configuration-files

Data files: kernelspecs and notebook extensions

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#data-files-kernelspecs-and-notebook-extensions

Since Jupyter does not have profiles, how do I customize it?

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#since-jupyter-does-not-have-profiles-how-do-i-customize-it

Changing the Jupyter notebook configuration directory

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#changing-the-jupyter-notebook-configuration-directory

Changing the Jupyter notebook configuration file

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#changing-the-jupyter-notebook-configuration-file

Changing IPython's profile using custom kernelspecs

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#changing-ipython-s-profile-using-custom-kernelspecs

Understanding Installation Changes

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#understanding-installation-changes

Notebook extensions

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#notebook-extensions

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#kernels

Understanding Changes in imports

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#understanding-changes-in-imports

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#id1

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#abstract

The Big Split

https://blog.jupyter.org/the-big-split-9d7b88a031a7

moved IPython's various language-agnostic components under the Jupyter umbrella. Going forward, Jupyter will contain the language-agnostic projects that serve many languages. IPython will continue to focus on Python and its use with Jupyter.

This document describes what has changed, and how you may need to modify your code or configuration when migrating from IPython version 3 to Jupyter.

Understanding the Migration Process

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#id2

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#understanding-the-migration-process

Automatic migration of files

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#id3

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#automatic-migration-of-files

The first time you run any

command, it will perform an automatic migration of files. The automatic migration process

files, instead of moving files, leaving the originals in place and the copies in the Jupyter file locations. You can re-run the migration, if needed, by calling

jupyter migrate

. Your custom configuration will be migrated automatically and should work with Jupyter without further editing. When you update or modify your configuration in the future, please keep in mind that the file locations may have changed.

Where have my configuration files gone?

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#id4

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#where-have-my-configuration-files-gone

Also known as: “Why isn't my configuration having any effect anymore?”

Jupyter splitting out from IPython means that the locations of some files have moved, and Jupyter projects have not inherited everything from how IPython did it.

When you start your first Jupyter application, the relevant configuration files are automatically copied to their new Jupyter locations. The original configuration files in the IPython locations have no effect on Jupyter's execution. If you accidentally edit your original IPython config file, you may not see the desired effect with Jupyter now. You should check that you are editing Jupyter's configuration file, and you should see the expected effect after restarting the Jupyter server.

Finding the Location of Important Files

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#id5

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#finding-the-location-of-important-files

This section provides quick reference for common locations of IPython 3 files and the migrated Jupyter files.

Configuration files

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#id6

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#configuration-files

Configuration files customize Jupyter to the user's preferences. The migrated files should all be

automatically copied

to their new Jupyter locations. Here are the location changes:

IPython location

Jupyter location

~/.ipython/profile\_default/static/custom

~/.jupyter/custom

~/.ipython/profile\_default/ipython\_notebook\_config.py

~/.jupyter/jupyter\_notebook\_config.py

~/.ipython/profile\_default/ipython\_nbconvert\_config.py

~/.jupyter/jupyter\_nbconvert\_config.py

~/.ipython/profile\_default/ipython\_qtconsole\_config.py

~/.jupyter/jupyter\_qtconsole\_config.py

~/.ipython/profile\_default/ipython\_console\_config.py

~/.jupyter/jupyter\_console\_config.py

To choose a directory location other than the default

JUPYTER\_CONFIG\_DIR

environment variable. You may need to run

jupyter migrate

after setting the environment variable for files to be copied to the desired directory.

Data files: kernelspecs and notebook extensions

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#id7

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#data-files-kernelspecs-and-notebook-extensions

Data files include files, other than configuration files, which are user installed. Examples include kernelspecs and notebook extensions. Like the configuration files, data files are also

automatically migrated

to their new Jupyter locations.

, data files lived in

, data files use platform-appropriate locations:

~/Library/Jupyter

Windows: the location specified in

environment variable

$XDG\_DATA\_HOME

is respected, with the default of

~/.local/share/jupyter

In all cases, the

JUPYTER\_DATA\_DIR

environment variable can be used to set a location explicitly.

Data files installed system-wide (e.g. in

/usr/local/share/jupyter

) have not changed. Per-user installation of data files has changed location from

to the platform-appropriate Jupyter location.

Since Jupyter does not have profiles, how do I customize it?

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#id8

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#since-jupyter-does-not-have-profiles-how-do-i-customize-it

While IPython has the concept of

https://docs.jupyter.org/en/latest/glossary.html#term-profiles

Jupyter does not have profiles

In IPython, profiles are collections of configuration and runtime files. Inside the IPython directory (

), there are directories with names like

profile\_default

profile\_demo

. In each of these are configuration files (

ipython\_config.py

ipython\_notebook\_config.py

) and runtime files (

history.sqlite

security/kernel-\*.json

). Profiles could be used to switch between configurations of IPython.

Previously, people could use commands like

ipython notebook --profile demo

to set the profile for

the notebook server and the IPython kernel. This is no longer possible in one go with Jupyter, just like it wasn't possible in IPython 3 for any other kernels.

Changing the Jupyter notebook configuration directory

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#id9

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#changing-the-jupyter-notebook-configuration-directory

If you want to change the notebook configuration, you can set the

JUPYTER\_CONFIG\_DIR

JUPYTER\_CONFIG\_DIR=./jupyter\_config
jupyter notebook

Changing the Jupyter notebook configuration file

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#id10

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#changing-the-jupyter-notebook-configuration-file

#### If you just want to change the config file, you can do:

jupyter notebook --config=/path/to/myconfig.py

Changing IPython's profile using custom kernelspecs

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#id11

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#changing-ipython-s-profile-using-custom-kernelspecs

If you do want to change the IPython kernel's profile, you can't do this at the server command-line anymore. Kernel arguments must be changed by modifying the kernelspec. You can do this without relaunching the server. Kernelspec changes take effect every time you start a new kernel. However, there isn't a great way to modify the kernelspecs. One approach uses

jupyter kernelspec list

to find the

kernel.json

file and then modifies it, e.g.

kernels/python3/kernel.json

, by hand. Alternatively,

https://github.com/minrk/a2km

is an experimental project that tries to make these things easier.

For example, add the

option to a custom kernelspec under

kernels/mycustom/kernel.json

(see the Jupyter kernelspec directions

https://jupyter-client.readthedocs.io/en/latest/kernels.html#kernel-specs

{
 "argv": \["python", "-m", "ipykernel",
          "--profile=my-ipython-profile",
          "-f", "{connection\_file}"\],
 "display\_name": "Custom Profile Python",
 "language": "python"
}

#### You can then run Jupyter with the

--kernel=mycustom

command-line option and IPython will find the appropriate profile.

Understanding Installation Changes

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#id12

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#understanding-installation-changes

Install and Use

https://docs.jupyter.org/en/latest/install.html#install

page for more information about installing Jupyter. Jupyter automatically migrates some things, like Notebook extensions and kernels.

Notebook extensions

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#id13

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#notebook-extensions

Any IPython notebook extensions should be

automatically migrated

as part of the data files migration.

#### Notebook extensions were installed with:

ipython install-nbextension \[--user\] EXTENSION

#### Now, extensions are installed with:

jupyter nbextension install \[--user\] EXTENSION

The notebook extensions will be installed in a system-wide location (e.g.

/usr/local/share/jupyter/nbextensions

). If doing a

install, the notebook extensions will go in the

JUPYTER\_DATA\_DIR

location. Installation

be done manually by guessing where the files should go.

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#id14

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#kernels

Kernels are installed in much the same way as notebook extensions. They will also be

automatically migrated

#### Kernel specs used to be installed with:

ipython kernelspec install \[--user\] KERNEL

#### They are now installed with:

jupyter kernelspec install \[--user\] KERNEL

By default, kernel specs will go in a system-wide location (e.g.

/usr/local/share/jupyter/kernels

). If doing a

install, the kernel specs will go in the

JUPYTER\_DATA\_DIR

location. Installation

be done manually by guessing where the files should go.

Understanding Changes in imports

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#id15

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#understanding-changes-in-imports

IPython 4.0 includes shims to manage dependencies; so, all imports that work on IPython 3 should continue to work on IPython 4. If you find any differences, please

let us know

https://github.com/ipython/ipython/issues

#### Some changes include:

Jupyter and IPython 4.0

IPython.html

IPython.html.widgets

IPython.kernel

jupyter\_client

IPython.parallel

ipyparallel

IPython.qt.console

IPython.utils.traitlets

IPython.config

traitlets.config

IPython.kernel

IPython.kernel

became two packages:

jupyter\_client

for the Jupyter client-side APIs.

for Jupyter's IPython kernel

previous Advanced Use Cases

https://docs.jupyter.org/en/latest/use/advanced/content-advanced.html

next Projects

https://docs.jupyter.org/en/latest/projects/content-projects.html

On this page

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#abstract

Understanding the Migration Process

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#understanding-the-migration-process

Automatic migration of files

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#automatic-migration-of-files

Where have my configuration files gone?

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#where-have-my-configuration-files-gone

Finding the Location of Important Files

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#finding-the-location-of-important-files

Configuration files

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#configuration-files

Data files: kernelspecs and notebook extensions

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#data-files-kernelspecs-and-notebook-extensions

Since Jupyter does not have profiles, how do I customize it?

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#since-jupyter-does-not-have-profiles-how-do-i-customize-it

Changing the Jupyter notebook configuration directory

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#changing-the-jupyter-notebook-configuration-directory

Changing the Jupyter notebook configuration file

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#changing-the-jupyter-notebook-configuration-file

Changing IPython's profile using custom kernelspecs

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#changing-ipython-s-profile-using-custom-kernelspecs

Understanding Installation Changes

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#understanding-installation-changes

Notebook extensions

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#notebook-extensions

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#kernels

Understanding Changes in imports

https://docs.jupyter.org/en/latest/use/advanced/migrating.html#understanding-changes-in-imports

Edit on GitHub

https://github.com/jupyter/jupyter/edit/master/docs/source/use/advanced/migrating.rst

Show Source

https://docs.jupyter.org/en/latest/\_sources/use/advanced/migrating.rst.txt

© Copyright 2015, Jupyter Team, https://jupyter.org.

Created using

https://www.sphinx-doc.org/

Built with the

PyData Sphinx Theme

https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html

https://docs.jupyter.org/es/latest/use/advanced/migrating.html

https://docs.jupyter.org/pt-br/latest/use/advanced/migrating.html

https://docs.jupyter.org/ru/latest/use/advanced/migrating.html

https://docs.jupyter.org/en/stable/use/advanced/migrating.html

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

