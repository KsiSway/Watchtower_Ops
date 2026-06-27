---
sourceFile: "What to do when things go wrong — Jupyter Notebook 7.6.0 documentation"
exportedBy: "Kortex"
exportDate: "2026-06-26T04:27:51.685Z"
---

# What to do when things go wrong — Jupyter Notebook 7.6.0 documentation

cfe43699-5a87-4b2b-8872-6bef629a5193

What to do when things go wrong — Jupyter Notebook 7.6.0 documentation

fa8e2157-12dd-443c-b768-1e168e84225b

https://jupyter-notebook.readthedocs.io/en/stable/troubleshooting.html

What to do when things go wrong — Jupyter Notebook 7.6.0 documentation

Skip to main content

https://jupyter-notebook.readthedocs.io/en/stable/troubleshooting.html#main-content

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

What to do when things go wrong

What to do when things go wrong

https://jupyter-notebook.readthedocs.io/en/stable/troubleshooting.html#what-to-do-when-things-go-wrong

First, have a look at the common problems listed below. If you can figure it out from these notes, it will be quicker than asking for help.

Check that you have the latest version of any packages that look relevant. Unfortunately it's not always easy to figure out what packages are relevant, but if there was a bug that's already been fixed, it's easy to upgrade and get on with what you wanted to do.

Jupyter fails to start

https://jupyter-notebook.readthedocs.io/en/stable/troubleshooting.html#jupyter-fails-to-start

installed it

https://jupyter.org/install.html

If you're using a menu shortcut or Anaconda launcher to start it, try opening a terminal or command prompt and running the command

jupyter notebook

If it can't find

, you may need to configure your

environment variable. If you don't know what that means, and don't want to find out, just (re)install Anaconda with the default settings, and it should set up PATH correctly.

If Jupyter gives an error that it can't find

, check with pip or conda that the

package is installed.

Try running

jupyter-notebook

(with a hyphen). This should normally be the same as

jupyter notebook

(with a space), but if there's any difference, the version with the hyphen is the 'real' launcher, and the other one wraps that.

Jupyter doesn't load or doesn't work in the browser

https://jupyter-notebook.readthedocs.io/en/stable/troubleshooting.html#jupyter-doesn-t-load-or-doesn-t-work-in-the-browser

Try in another browser (e.g. if you normally use Firefox, try with Chrome). This helps pin down where the problem is.

Try disabling any browser extensions and/or any Jupyter extensions you have installed.

Some internet security software can interfere with Jupyter. If you have security software, try turning it off temporarily, and look in the settings for a more long-term solution.

In the address bar, try changing between

. They should be the same, but in some cases it makes a difference.

Jupyter can't start a kernel

https://jupyter-notebook.readthedocs.io/en/stable/troubleshooting.html#jupyter-can-t-start-a-kernel

Files called

kernel specs

tell Jupyter how to start different kinds of kernels. To see where these are on your system, run

jupyter kernelspec list

$ jupyter kernelspec list
Available kernels:
  python3      /home/takluyver/.local/lib/python3.6/site-packages/ipykernel/resources
  bash         /home/takluyver/.local/share/jupyter/kernels/bash
  ir           /home/takluyver/.local/share/jupyter/kernels/ir

There's a special fallback for the Python kernel: if it doesn't find a real kernelspec, but it can import the

package, it provides a kernel which will run in the same Python environment as the notebook server. A path ending in

ipykernel/resources

, like in the example above, is this default kernel. The default often does what you want, so if the

kernelspec points somewhere else and you can't start a Python kernel, try deleting or renaming that kernelspec folder to expose the default.

If your problem is with another kernel, not the Python one we maintain, you may need to look for support about that kernel.

Python Environments

https://jupyter-notebook.readthedocs.io/en/stable/troubleshooting.html#python-environments

Multiple python environments, whether based on Anaconda or Python Virtual environments, are often the source of reported issues. In many cases, these issues stem from the Notebook server running in one environment, while the kernel and/or its resources, derive from another environment. Indicators of this scenario include:

statements within code cells producing

ImportError

ModuleNotFound

exceptions.

General kernel startup failures exhibited by nothing happening when attempting to execute a cell.

In these situations, take a close look at your environment structure and ensure all packages required by your notebook's code are installed in the correct environment. If you need to run the kernel from different environments than your Notebook server, check out

IPython's documentation

https://ipython.readthedocs.io/en/stable/install/kernel\_install.html#kernels-for-different-environments

for using kernels from different environments as this is the recommended approach. Anaconda's

nb\_conda\_kernels

https://github.com/Anaconda-Platform/nb\_conda\_kernels

package might also be an option for you in these scenarios.

Another thing to check is the

kernel.json

file that will be located in the aforementioned

kernel specs

directory identified by running

jupyter kernelspec list

. This file will contain an

stanza that includes the actual command to run when launching the kernel. Oftentimes, when reinstalling python environments, a previous

kernel.json

will reference an python executable from an old or non-existent location. As a result, it's always a good idea when encountering kernel startup issues to validate the

stanza to ensure all file references exist and are appropriate.

Windows Systems

https://jupyter-notebook.readthedocs.io/en/stable/troubleshooting.html#windows-systems

Although Jupyter Notebook is primarily developed on the various flavors of the Unix operating system it also supports Microsoft Windows - which introduces its own set of commonly encountered issues, particularly in the areas of security, process management and lower-level libraries.

pywin32 Issues

https://jupyter-notebook.readthedocs.io/en/stable/troubleshooting.html#pywin32-issues

The primary package for interacting with Windows' primitives is

Issues surrounding the creation of the kernel's communication file utilize

jupyter\_core

secure\_write()

function. This function ensures a file is created in which only the owner of the file has access. If libraries like

are not properly installed, issues can arise when it's necessary to use the native Windows libraries. Here's a portion of such a traceback:

File "c:\users\jovyan\python\myenv.venv\lib\site-packages\jupyter\_core\paths.py", line 424, in secure\_write
win32\_restrict\_file\_to\_user(fname)
File "c:\users\jovyan\python\myenv.venv\lib\site-packages\jupyter\_core\paths.py", line 359, in win32\_restrict\_file\_to\_user
import win32api
ImportError: DLL load failed: The specified module could not be found.

As noted earlier, the installation of

can be problematic on Windows configurations. When such an issue occurs, you may need to revisit how the environment was setup. Pay careful attention to whether you're running the 32 or 64 bit versions of Windows and be sure to install appropriate packages for that environment. Here's a portion of such a traceback:

File "C:\Users\jovyan\AppData\Roaming\Python\Python37\site-packages\jupyter\_core\paths.py", line 435, in secure\_write
win32\_restrict\_file\_to\_user(fname)
File "C:\Users\jovyan\AppData\Roaming\Python\Python37\site-packages\jupyter\_core\paths.py", line 361, in win32\_restrict\_file\_to\_user
import win32api
ImportError: DLL load failed: %1 is not a valid Win32 application

Resolving pywin32 Issues

https://jupyter-notebook.readthedocs.io/en/stable/troubleshooting.html#resolving-pywin32-issues

In this case, your

module may not be installed correctly and the following should be attempted:

pip install --upgrade pywin32

conda install --force-reinstall pywin32

followed by:

python.exe Scripts/pywin32\_postinstall.py -install

is located in the active Python's installation location.

Another common failure specific to Windows environments is the location of various python commands. On

systems, these typically reside in the

directory of the active Python environment. However, on Windows, these tend to reside in the

folder - which is a sibling to

. As a result, when encountering kernel startup issues, again, check the

stanza and verify it's pointing to a valid file. You may find that it's pointing in

is correct, or the referenced file does not include its

extension - typically resulting in

FileNotFoundError

exceptions.

This Worked An Hour Ago

https://jupyter-notebook.readthedocs.io/en/stable/troubleshooting.html#this-worked-an-hour-ago

The Jupyter stack is very complex and rightfully so, there's a lot going on. On occasion you might find the system working perfectly well, then, suddenly, you can't get past a certain cell due to

failures. In these situations, it's best to ask yourself if any new python files were added to your notebook development area.

These issues are usually evident by carefully analyzing the traceback produced in the notebook error or the Notebook server's command window. In these cases, you'll typically find the Python kernel code (from

) performing

imports and notice a file from your Notebook development error included in that traceback followed by an

AttributeError

File "C:\Users\jovyan\anaconda3\lib\site-packages\ipykernel\connect.py", line 13, in
from IPython.core.profiledir import ProfileDir
File "C:\Users\jovyan\anaconda3\lib\site-packages\IPython\_init.py", line 55, in
from .core.application import Application
...
File "C:\Users\jovyan\anaconda3\lib\site-packages\ipython\_genutils\path.py", line 13, in
import random
File "C:\Users\jovyan\Desktop\Notebooks\random.py", line 4, in
rand\_set = random.sample(english\_words\_lower\_set, 12)
AttributeError: module 'random' has no attribute 'sample'

What has happened is that you have named a file that conflicts with an installed package that is used by the kernel software and now introduces a conflict preventing the kernel's startup.

: You'll need to rename your file. A best practice would be to prefix or

your files so as not to conflict with any python package.

Asking for help

https://jupyter-notebook.readthedocs.io/en/stable/troubleshooting.html#asking-for-help

As with any problem, try searching to see if someone has already found an answer. If you can't find an existing answer, you can ask questions at:

Jupyter Discourse Forum

https://discourse.jupyter.org/

jupyter-notebook tag on Stackoverflow

https://stackoverflow.com/questions/tagged/jupyter-notebook

jupyter/help repository on Github

https://github.com/jupyter/help

(read-only)

Or in an issue on another repository, if it's clear which component is responsible. Typical repositories include:

jupyter\_core

https://github.com/jupyter/jupyter\_core

secure\_write()

and file path issues

jupyter\_client

https://github.com/jupyter/jupyter\_client

- kernel management issues found in Notebook server's command window.

https://github.com/ipython/ipython

https://github.com/ipython/ipykernel

- kernel runtime issues typically found in Notebook server's command window and/or Notebook cell execution.

Gathering Information

https://jupyter-notebook.readthedocs.io/en/stable/troubleshooting.html#gathering-information

Should you find that your problem warrants that an issue be opened in

https://github.com/jupyter/notebook

please don't forget to provide details like the following:

What error messages do you see (within your notebook and, more importantly, in the Notebook server's command window)?

What platform are you on?

How did you install Jupyter?

What have you tried already?

jupyter troubleshoot

command collects a lot of information about your installation, which can also be useful.

When providing textual information, it's most helpful if you can

the contents into the issue rather than providing a screenshot. This enables others to select pieces of that content so they can search more efficiently and try to help.

Remember that it's not anyone's job to help you. We want Jupyter to work for you, but we can't always help everyone individually.

previous Interface Customization

https://jupyter-notebook.readthedocs.io/en/stable/configuring/interface\_customization.html

next Changelog

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html

On this page

Jupyter fails to start

https://jupyter-notebook.readthedocs.io/en/stable/troubleshooting.html#jupyter-fails-to-start

Jupyter doesn't load or doesn't work in the browser

https://jupyter-notebook.readthedocs.io/en/stable/troubleshooting.html#jupyter-doesn-t-load-or-doesn-t-work-in-the-browser

Jupyter can't start a kernel

https://jupyter-notebook.readthedocs.io/en/stable/troubleshooting.html#jupyter-can-t-start-a-kernel

Python Environments

https://jupyter-notebook.readthedocs.io/en/stable/troubleshooting.html#python-environments

Windows Systems

https://jupyter-notebook.readthedocs.io/en/stable/troubleshooting.html#windows-systems

pywin32 Issues

https://jupyter-notebook.readthedocs.io/en/stable/troubleshooting.html#pywin32-issues

Resolving pywin32 Issues

https://jupyter-notebook.readthedocs.io/en/stable/troubleshooting.html#resolving-pywin32-issues

This Worked An Hour Ago

https://jupyter-notebook.readthedocs.io/en/stable/troubleshooting.html#this-worked-an-hour-ago

Asking for help

https://jupyter-notebook.readthedocs.io/en/stable/troubleshooting.html#asking-for-help

Gathering Information

https://jupyter-notebook.readthedocs.io/en/stable/troubleshooting.html#gathering-information

Edit on GitHub

https://github.com/jupyter/notebook/edit/main/docs/source/troubleshooting.md

Show Source

https://jupyter-notebook.readthedocs.io/en/stable/\_sources/troubleshooting.md.txt

© Copyright 2015, Jupyter Team, https://jupyter.org.

Created using

https://www.sphinx-doc.org/

Built with the

PyData Sphinx Theme

https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html

https://jupyter-notebook.readthedocs.io/en/master/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/latest/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v7.6.0/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v7.5.7/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v7.5.6/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v7.5.5/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v7.5.4/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v7.5.3/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v7.5.2/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v7.5.1/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v7.5.0/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v7.4.7/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v7.4.6/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v7.4.5/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v7.4.4/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v7.4.3/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v7.4.2/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v7.4.1/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v7.4.0/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v7.3.3/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v7.3.2/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v7.3.1/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v7.3.0/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v7.2.2/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v7.2.1/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v7.2.0/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v7.1.3/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v7.1.2/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v7.1.1/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v7.0.8/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v7.0.7/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v7.0.6/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v7.0.5/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v7.0.4/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v7.0.3/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v7.0.2/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v7.0.1/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v7.0.0/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v6.5.4/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v6.5.3/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v6.5.2/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v6.5.1/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v6.5.0/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/6.4.12/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v6.4.11/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/6.4.10/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v6.4.9/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v6.4.8/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v6.4.7/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v6.4.6/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v6.4.5/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/v6.4.4/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/6.2.0/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/5.7.6/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/5.7.5/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/5.7.4/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/5.7.3/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/5.7.2/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/5.7.1/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/5.7.0/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/5.6.0/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/5.5.0/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/5.4.1/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/5.4.0/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/5.3.1/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/5.2.2/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/5.1.0/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/5.0.0/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/4.x/troubleshooting.html

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

