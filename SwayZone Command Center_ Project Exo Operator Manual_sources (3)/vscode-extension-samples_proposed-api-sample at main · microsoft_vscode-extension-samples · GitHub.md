---
sourceFile: "vscode-extension-samples/proposed-api-sample at main · microsoft/vscode-extension-samples · GitHub"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.913Z"
---

# vscode-extension-samples/proposed-api-sample at main · microsoft/vscode-extension-samples · GitHub

43c67442-ffc5-4d82-b5a9-17c975a1ec7b

vscode-extension-samples/proposed-api-sample at main · microsoft/vscode-extension-samples · GitHub

08f7e6d5-3219-409f-84a4-86946e90a7eb

https://github.com/microsoft/vscode-extension-samples/tree/main/proposed-api-sample

Skip to content

Navigation Menu

Appearance settings

AI CODE CREATION

GitHub Copilot Write better code with AI

GitHub Spark Build and deploy intelligent apps

GitHub Models Manage and compare prompts

MCP Registry

Integrate external tools

DEVELOPER WORKFLOWS

Actions Automate any workflow

Codespaces Instant dev environments

Issues Plan and track work

Code Review Manage code changes

APPLICATION SECURITY

GitHub Advanced Security Find and fix vulnerabilities

Code security Secure your code as you build

Secret protection Stop leaks before they start

Documentation

Marketplace

View all features

BY COMPANY SIZE

Enterprises

Small and medium teams

BY USE CASE

App Modernization

View all use cases

BY INDUSTRY

Financial services

Manufacturing

View all industries

View all solutions

EXPLORE BY TOPIC

Software Development

View all topics

EXPLORE BY TYPE

Customer stories

Events & webinars

Ebooks & reports

Business insights

GitHub Skills

SUPPORT & SERVICES

Documentation

Customer support

Community forum

Trust center

View all resources

GitHub Sponsors Fund open source developers

Security Lab

Maintainer Community

Accelerator

GitHub Stars

Archive Program

REPOSITORIES

Collections

ENTERPRISE SOLUTIONS

Enterprise platform AI-powered developer platform

AVAILABLE ADD-ONS

GitHub Advanced Security Enterprise-grade security features

Copilot for Business Enterprise-grade AI features

Premium Support Enterprise-grade 24/7 support

Search code, repositories, users, issues, pull requests...

Search syntax tips

Provide feedback

We read every piece of feedback, and take your input very seriously.

Saved searches

Use saved searches to filter your results more quickly

To see all available qualifiers, see our

documentation

https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax

https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax

https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax

Appearance settings   You signed in with another tab or window.

https://github.com

to refresh your session.   You signed out in another tab or window.

https://github.com

to refresh your session.   You switched accounts on another tab or window.

https://github.com

to refresh your session.   Dismiss alert   {{ message }}

https://github.com/microsoft

vscode-extension-samples

Notifications

You must be signed in to change notification settings

Star  10.1k

Additional navigation options

Pull requests

Security and quality

Expand file tree

proposed-api-sample

/ Copy path

Directory actions

More options

More options

Directory actions

More options

More options

Latest commit

proposed-api-sample

Folders and files

Name Name Last commit message Last commit date

parent directory

eslint.config.mjs

eslint.config.mjs

package-lock.json

package-lock.json

package.json

package.json

tsconfig.json

tsconfig.json

Proposed API Sample

This sample demonstrates usage of

Proposed API

https://code.visualstudio.com/api/advanced-topics/using-proposed-api

The  postinstall  script uses  vscode-dts dev && vscode-dts main  to download latest version of

vscode.d.ts

https://github.com/microsoft/vscode/blob/main/src/vs/vscode.d.ts

vscode.proposed.<proposalName>.d.ts

https://github.com/microsoft/vscode/blob/main/src/vscode-dts

from the main branch of

microsoft/vscode

https://github.com/microsoft/vscode

#### You can read more about  vscode-dts  at:

https://github.com/microsoft/vscode-dts

https://github.com/microsoft/vscode-dts

⚠️  This sample can only be used for extension development in

Insider release

https://code.visualstudio.com/insiders/

. You cannot publish extensions using Proposed API.

You need  "enabledApiProposals": \["<proposalName>"\]  in  package.json .

VS Code API

vscode  module

commands.registerCommand

https://code.visualstudio.com/insiders/

window.showInformationMessage

https://code.visualstudio.com/insiders/

Contribution Points

contributes.commands

https://code.visualstudio.com/insiders/

Running the Sample

Run  npm install  in terminal to install dependencies

A  postinstall  script would download latest version of  vscode.proposed.<proposalName>.d.ts

#### Run the  Run Extension  target in the Debug View. This will:

Start a task  npm: watch  to compile the code

Run the extension in a new VS Code window

You can’t perform that action at this time.

