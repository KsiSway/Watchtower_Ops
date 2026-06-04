---
sourceFile: "GitHub Pull Requests - Visual Studio Marketplace"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.474Z"
---

# GitHub Pull Requests - Visual Studio Marketplace

b58ecad1-1d23-452d-b9bd-49d93da295f1

GitHub Pull Requests - Visual Studio Marketplace

3bb79168-134b-470c-8c77-1ed848dc6d1b

https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github

GitHub Pull Requests - Visual Studio Marketplace

Skip to content

https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github#start-of-content

| Marketplace

https://marketplace.visualstudio.com/

https://app.vssps.visualstudio.com/\_signin?realm=marketplace.visualstudio.com&reply\_to=https%3A%2F%2Fmarketplace.visualstudio.com%2Fitems%3FitemName%3DGitHub.vscode-pull-request-github&redirect=1&protocol=cookieless&context=eyJodCI6MywiaGlkIjoiMjY2M2IxM2YtNTBlMy1hNjU1LWExNTktMjJmNmY0NzI1ZmFiIiwicXMiOnt9LCJyciI6IiIsInZoIjoiIiwiY3YiOiIiLCJjcyI6IiJ90&lltid=d482e24b-59dd-4946-b27c-738ce8e5b39e&workflowId=marketplace&wt.mc\_id=o~msft~marketplace~signIn#ctx=eyJTaWduSW5Db29raWVEb21haW5zIjpbImh0dHBzOi8vbG9naW4ubWljcm9zb2Z0b25saW5lLmNvbSIsImh0dHBzOi8vbG9naW4ubWljcm9zb2Z0b25saW5lLmNvbSJdfQ2

Visual Studio Code

https://marketplace.visualstudio.com/vscode

https://marketplace.visualstudio.com/search?sortBy=Installs&category=AI&target=VSCode

> GitHub Pull Requests New to Visual Studio Code?

Get it now.

https://go.microsoft.com/fwlink?linkid=846418&pub=GitHub&ext=vscode-pull-request-github&utm\_source=vsmp&utm\_campaign=mpdetails

GitHub Pull Requests

https://marketplace.visualstudio.com/publishers/GitHub

https://github.com/

34,516,605 installs

https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github#review-details

Pull Request and Issue Provider for GitHub

Installation

Launch VS Code Quick Open (

), paste the following command, and press enter.

ext install GitHub.vscode-pull-request-github

Copied to clipboard

http://go.microsoft.com/fwlink/?LinkID=691811&pub=GitHub&ext=vscode-pull-request-github

GitHub.vscode-pull-request-github

Overview Version History Q & A Rating & Review

Review and manage your GitHub pull requests and issues directly in VS Code

This extension allows you to review and manage GitHub pull requests and issues in Visual Studio Code. The support includes:

Authenticating and connecting VS Code to GitHub and GitHub Enterprise.

Listing and browsing PRs from within VS Code.

Reviewing PRs from within VS Code with in-editor commenting.

Validating PRs from within VS Code with easy checkouts.

Terminal integration that enables UI and CLIs to co-exist.

Listing and browsing issues from within VS Code.

Hover cards for "@" mentioned users and for issues.

Completion suggestions for users and issues.

A "Start working on issue" action which can create a branch for you.

Code actions to create issues from "todo" comments.

Getting Started

It's easy to get started with GitHub Pull Requests for Visual Studio Code. Simply follow these steps to get started.

Install the extension from within VS Code or download it from

the marketplace

https://aka.ms/vscodepr-download

Open your desired GitHub repository in VS Code.

A new viewlet will appear on the activity bar which shows a list of pull requests and issues.

Use the button on the viewlet to sign in to GitHub.

You may need to configure the

githubPullRequests.remotes

setting, by default the extension will look for PRs for

. If you have different remotes, add them to the remotes list.

You should be good to go!

https://www.youtube.com/watch?v=LdSwWxVzUpo

https://www.youtube.com/watch?v=LdSwWxVzUpo

for additional getting started tips!

Configuring the extension

There are several settings that can be used to configure the extension.

As mentioned above,

githubPullRequests.remotes

is used to specify what remotes the extension should try to fetch pull requests from.

To customize the pull request tree, you can use the

githubPullRequests.queries

setting. This setting is a list of labels and search queries which populate the categories of the tree. By default, these queries are "Waiting For My Review", "Assigned To Me", and "Created By Me". An example of adding a "Mentioned Me" category is to change the setting to the following:

"githubPullRequests.queries": \[
	{
		"label": "Waiting For My Review",
		"query": "is:open review-requested:${user}"
	},
	{
		"label": "Assigned To Me",
		"query": "is:open assignee:${user}"
	},
	{
		"label": "Created By Me",
		"query": "is:open author:${user}"
	},
	{
		"label": "Mentioned Me",
		"query": "is:open mentions:${user}"
	}
\]

#### Similarly, there is a setting to configure your issues queries:

githubIssues.queries

Queries use

GitHub search syntax

https://help.github.com/en/articles/understanding-the-search-syntax

To view additional settings for the extension, you can open VS Code settings and search for "github pull requests".

This extension is still in development, so please refer to our

issue tracker for known issues

https://github.com/Microsoft/vscode-pull-request-github/issues

, and please contribute with additional information if you encounter an issue yourself.

Questions? Authentication? GitHub Enterprise?

https://github.com/Microsoft/vscode-pull-request-github/wiki

for our FAQ.

Contributing

If you're interested in contributing, or want to explore the source code of this extension yourself, see our

contributing guide

https://github.com/Microsoft/vscode-pull-request-github/wiki/Contributing

, which includes:

How to Build and Run

https://github.com/Microsoft/vscode-pull-request-github/wiki/Contributing#build-and-run

Architecture

https://github.com/Microsoft/vscode-pull-request-github/wiki/Contributing#architecture

Making Pull Requests

https://github.com/Microsoft/vscode-pull-request-github/wiki/Contributing#pull-requests

Code of Conduct

https://github.com/Microsoft/vscode-pull-request-github/wiki/Contributing#code-of-conduct

https://marketplace.visualstudio.com/search?sortBy=Installs&category=AI&target=VSCode

https://marketplace.visualstudio.com/search?sortBy=Installs&category=Chat&target=VSCode

keybindings

https://marketplace.visualstudio.com/search?term=tag%3Akeybindings&target=VSCode

language-model-tools

https://marketplace.visualstudio.com/search?term=tag%3Alanguage-model-tools&target=VSCode

https://marketplace.visualstudio.com/search?term=tag%3Atools&target=VSCode

Universal, Web

https://github.com/Microsoft/vscode-pull-request-github/issues

https://github.com/Microsoft/vscode-pull-request-github.git

https://github.com/Microsoft/vscode-pull-request-github#readme

https://marketplace.visualstudio.com/items/GitHub.vscode-pull-request-github/license

https://marketplace.visualstudio.com/items/GitHub.vscode-pull-request-github/changelog

Project Details

Microsoft/vscode-pull-request-github

https://github.com/Microsoft/vscode-pull-request-github

Last Commit: 3 days ago

https://github.com/Microsoft/vscode-pull-request-github/commits

26 Pull Requests

https://github.com/Microsoft/vscode-pull-request-github/pulls

211 Open Issues

https://github.com/Microsoft/vscode-pull-request-github/issues

0.145.2026051504

Released on

9/7/2018, 4:09:31 PM

Last updated

5/14/2026, 9:28:31 PM

Unique Identifier

GitHub.vscode-pull-request-github

Report a concern

mailto:vsmarketplace@microsoft.com?subject=Report%20abuse%20-%20GitHub.vscode-pull-request-github&Body=https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github%0D%0A%3Cplease%20provide%20a%20brief%20description%20of%20the%20issue%3E

https://marketplace.visualstudio.com/items/GitHub.vscode-pull-request-github/changelog

#### Last Updated

0.145.2026051504

4 hours ago

0.145.2026051404

0.145.2026051304

0.145.2026051211

https://www.visualstudio.com/support/support-overview-vs

https://careers.microsoft.com/

https://go.microsoft.com/fwlink/?LinkID=521839

Manage cookies

https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github

Terms of use

https://aka.ms/vsmarketplace-ToU

https://www.microsoft.com/trademarks

© 2026 Microsoft

