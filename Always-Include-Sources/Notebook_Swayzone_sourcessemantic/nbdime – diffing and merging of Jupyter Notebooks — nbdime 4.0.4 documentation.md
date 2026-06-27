---
sourceFile: "nbdime – diffing and merging of Jupyter Notebooks — nbdime 4.0.4 documentation"
exportedBy: "Kortex"
exportDate: "2026-06-26T04:27:51.758Z"
---

# nbdime – diffing and merging of Jupyter Notebooks — nbdime 4.0.4 documentation

0358b147-27c4-46f2-84fd-22cecaa4f9b8

nbdime – diffing and merging of Jupyter Notebooks — nbdime 4.0.4 documentation

e40b2e7e-91dd-4951-9504-1945a469308f

https://nbdime.readthedocs.io/

nbdime – diffing and merging of Jupyter Notebooks — nbdime 4.0.4 documentation

nbdime – diffing and merging of Jupyter Notebooks

https://nbdime.readthedocs.io/#nbdime-diffing-and-merging-of-jupyter-notebooks

Version: 4.0.4

provides tools for diffing and merging

Jupyter notebooks

http://jupyter-notebook.readthedocs.io/en/latest/

Figure: nbdime example

https://nbdime.readthedocs.io/#id1

Why is nbdime needed?

https://nbdime.readthedocs.io/#why-is-nbdime-needed

Jupyter notebooks are useful, rich media documents stored in a plain text JSON format. This format is relatively easy to parse. However, primitive line-based diff and merge tools do not handle well the logical structure of notebook documents. These tools yield diffs like this:

Figure: diff using traditional line-based diff tool

https://nbdime.readthedocs.io/#id2

, on the other hand, provides “content-aware” diffing and merging of Jupyter notebooks. It understands the structure of notebook documents. Therefore, it can make intelligent decisions when diffing and merging notebooks, such as:

eliding base64-encoded images for terminal output

using existing diff tools for inputs and outputs

rendering image diffs in a web view

auto-resolving conflicts on generated values such as execution counters

nbdime yields diffs like this:

Figure: nbdime's content-aware diff

https://nbdime.readthedocs.io/#id3

https://nbdime.readthedocs.io/#quickstart

#### To get started with nbdime, install with pip:

pip install nbdime

And you can be off to the races by diffing notebooks in your terminal with

nbdiff notebook\_1.ipynb notebook\_2.ipynb

or viewing a rich web-based rendering of the diff with

nbdiff-web notebook\_1.ipynb notebook\_2.ipynb

For more information about nbdime's commands, see

Console commands

https://nbdime.readthedocs.io/cli.html

Git integration quickstart

https://nbdime.readthedocs.io/#git-integration-quickstart

Many of us who are writing and sharing notebooks do so with git and GitHub. Git doesn't handle diffing and merging notebooks very well by default, but you can configure git to use nbdime and it will get a lot better.

#### The quickest way to get set up for git integration is to call:

nbdime config-git --enable --global

#### Added in version 0.3:

nbdime config-git

. Prior to 0.3, each nbdime entrypoint had to enable git integration separately.

This will enable the both the drivers and the tools for both diff and merge.

Now when you do

with notebooks, you should see a nice diff view, like this:

Figure: nbdime's 'content-aware' command-line diff

https://nbdime.readthedocs.io/#id4

#### To use the web-based GUI viewers of notebook diffs, call:

nbdiff-web \[<commit> \[<commit>\]\] \[<path>\]

git diff documentation

https://git-scm.com/docs/git-diff

for further explanation of “

” for this command.

Added in version 0.3: support for passing git refs to nbdime commands

Figure: nbdime's content-aware diff

https://nbdime.readthedocs.io/#id5

If you have a merge conflict in a notebook, the merge driver will ensure that the conflicted notebook is a valid notebook that can be viewed in the normal notebook viewer. In it, the conflicts will be marked similarly to how git would normally indicate conflicts, and they can be resolved manually. Alternatively, nbdime provides a web-base mergetool for visualizing and resolving merge conflicts, and it can be launched by calling:

nbdime mergetool

Figure: nbdime's merge with web-based GUI viewer

https://nbdime.readthedocs.io/#id6

For more detailed information on integrating nbdime with version control, see

Version control integration

https://nbdime.readthedocs.io/vcs.html

https://nbdime.readthedocs.io/#contents

Installation and usage

Installation

https://nbdime.readthedocs.io/installing.html

Installing nbdime

https://nbdime.readthedocs.io/installing.html#installing-nbdime

Installing latest development version

https://nbdime.readthedocs.io/installing.html#installing-latest-development-version

Notebook Extensions

https://nbdime.readthedocs.io/extensions.html

Installation

https://nbdime.readthedocs.io/extensions.html#installation

https://nbdime.readthedocs.io/extensions.html#usage

https://nbdime.readthedocs.io/extensions.html#removal

Console commands

https://nbdime.readthedocs.io/cli.html

https://nbdime.readthedocs.io/cli.html#nbshow

https://nbdime.readthedocs.io/cli.html#diffing

https://nbdime.readthedocs.io/cli.html#merging

Version control integration

https://nbdime.readthedocs.io/vcs.html

Git integration

https://nbdime.readthedocs.io/vcs.html#git-integration

Mercurial integration

https://nbdime.readthedocs.io/vcs.html#mercurial-integration

Configuration

https://nbdime.readthedocs.io/config.html

https://nbdime.readthedocs.io/config.html#sections

Configuring ignores

https://nbdime.readthedocs.io/config.html#configuring-ignores

Front-end extensions

https://nbdime.readthedocs.io/config.html#front-end-extensions

https://nbdime.readthedocs.io/glossary.html

Development

https://nbdime.readthedocs.io/testing.html

Dependencies

https://nbdime.readthedocs.io/testing.html#dependencies

Running tests locally

https://nbdime.readthedocs.io/testing.html#running-tests-locally

Submitting test cases

https://nbdime.readthedocs.io/testing.html#submitting-test-cases

diff format

https://nbdime.readthedocs.io/diffing.html

https://nbdime.readthedocs.io/diffing.html#basics

Diff format for mappings

https://nbdime.readthedocs.io/diffing.html#diff-format-for-mappings

Diff format for sequences

https://nbdime.readthedocs.io/diffing.html#diff-format-for-sequences

Relation to JSONPatch

https://nbdime.readthedocs.io/diffing.html#relation-to-jsonpatch

https://nbdime.readthedocs.io/diffing.html#examples

Merge details

https://nbdime.readthedocs.io/merging.html

Merge Results

https://nbdime.readthedocs.io/merging.html#merge-results

Merge decision format

https://nbdime.readthedocs.io/merging.html#merge-decision-format

https://nbdime.readthedocs.io/restapi.html

Definitions

https://nbdime.readthedocs.io/restapi.html#definitions

https://nbdime.readthedocs.io/restapi.html#api-diff

https://nbdime.readthedocs.io/restapi.html#api-merge

https://nbdime.readthedocs.io/usecases.html

Basic diffing use cases

https://nbdime.readthedocs.io/usecases.html#basic-diffing-use-cases

Version control use cases

https://nbdime.readthedocs.io/usecases.html#version-control-use-cases

Regression testing use cases

https://nbdime.readthedocs.io/usecases.html#regression-testing-use-cases

Acknowledgements

https://nbdime.readthedocs.io/#acknowledgements

nbdime is developed with financial support from:

OpenDreamKit Horizon 2020 European Research Infrastructures project (

CORDIS 676541

https://cordis.europa.eu/project/id/676541

http://opendreamkit.org

http://opendreamkit.org/

The Gordon and Betty Moore Foundation through Grant

https://www.moore.org/grant-detail?grantId=GBMF4856

, by the Alfred P. Sloan Foundation and by the Helmsley Trust.

https://nbdime.readthedocs.io/

Installation and usage

Installation

https://nbdime.readthedocs.io/installing.html

Notebook Extensions

https://nbdime.readthedocs.io/extensions.html

Console commands

https://nbdime.readthedocs.io/cli.html

Version control integration

https://nbdime.readthedocs.io/vcs.html

Configuration

https://nbdime.readthedocs.io/config.html

https://nbdime.readthedocs.io/glossary.html

Development

https://nbdime.readthedocs.io/testing.html

diff format

https://nbdime.readthedocs.io/diffing.html

Merge details

https://nbdime.readthedocs.io/merging.html

https://nbdime.readthedocs.io/restapi.html

https://nbdime.readthedocs.io/usecases.html

Related Topics

Documentation overview

https://nbdime.readthedocs.io/

Installation

https://nbdime.readthedocs.io/installing.html

©2015, Martin Sandve Alnæs; 2016, Project Jupyter. | Powered by

Sphinx 9.0.4

https://www.sphinx-doc.org/

Alabaster 1.0.0

https://alabaster.readthedocs.io/

Page source

https://nbdime.readthedocs.io/\_sources/index.rst.txt

https://nbdime.readthedocs.io/en/stable/

On Read the Docs

Project Home

https://app.readthedocs.org/projects/nbdime/?utm\_source=nbdime&utm\_content=flyout

https://app.readthedocs.org/projects/nbdime/builds/?utm\_source=nbdime&utm\_content=flyout

Addons documentation

https://docs.readthedocs.io/page/addons.html?utm\_source=nbdime&utm\_content=flyout

― Hosted by

Read the Docs

https://about.readthedocs.com/?utm\_source=nbdime&utm\_content=flyout

Stop wasting tool calls See how you can use up to 80% fewer tokens with Airbyte Agents. Try it free

https://server.ethicalads.io/proxy/click/10569/019f0192-f7d5-7a22-b667-3b2fd4d2c749/

Ads by EthicalAds

https://www.ethicalads.io/advertisers/topics/data-science/?ref=ea-text

No recent searches

to navigate

Search powered by

