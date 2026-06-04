---
sourceFile: "Live Preview - Visual Studio Marketplace"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.612Z"
---

# Live Preview - Visual Studio Marketplace

87693e9f-e273-4ba2-b94f-de5b7c693039

Live Preview - Visual Studio Marketplace

c28e8646-7a80-4b1e-87e3-2a3e5cd8fa2f

https://marketplace.visualstudio.com/items?itemName=ms-vscode.live-server

Live Preview - Visual Studio Marketplace

Skip to content

https://marketplace.visualstudio.com/items?itemName=ms-vscode.live-server#start-of-content

| Marketplace

https://marketplace.visualstudio.com/

https://app.vssps.visualstudio.com/\_signin?realm=marketplace.visualstudio.com&reply\_to=https%3A%2F%2Fmarketplace.visualstudio.com%2Fitems%3FitemName%3Dms-vscode.live-server&redirect=1&protocol=cookieless&context=eyJodCI6MywiaGlkIjoiMjY2M2IxM2YtNTBlMy1hNjU1LWExNTktMjJmNmY0NzI1ZmFiIiwicXMiOnt9LCJyciI6IiIsInZoIjoiIiwiY3YiOiIiLCJjcyI6IiJ90&lltid=34db2e74-5b79-449d-89e7-18a706acdeed&workflowId=marketplace&wt.mc\_id=o~msft~marketplace~signIn#ctx=eyJTaWduSW5Db29raWVEb21haW5zIjpbImh0dHBzOi8vbG9naW4ubWljcm9zb2Z0b25saW5lLmNvbSIsImh0dHBzOi8vbG9naW4ubWljcm9zb2Z0b25saW5lLmNvbSJdfQ2

Visual Studio Code

https://marketplace.visualstudio.com/vscode

https://marketplace.visualstudio.com/search?sortBy=Installs&category=Other&target=VSCode

> Live Preview New to Visual Studio Code?

Get it now.

https://go.microsoft.com/fwlink?linkid=846418&pub=ms-vscode&ext=live-server&utm\_source=vsmp&utm\_campaign=mpdetails

Live Preview

https://marketplace.visualstudio.com/publishers/Microsoft

microsoft.com

https://microsoft.com/

12,577,980 installs

https://marketplace.visualstudio.com/items?itemName=ms-vscode.live-server#review-details

Hosts a local server in your workspace for you to preview your webpages on.

Installation

Launch VS Code Quick Open (

), paste the following command, and press enter.

ext install ms-vscode.live-server

Copied to clipboard

http://go.microsoft.com/fwlink/?LinkID=691811&pub=ms-vscode&ext=live-server

ms-vscode.live-server

Overview Version History Q & A Rating & Review

This is the pre-release edition of Live Preview for early feedback and testing. It works best with VS Code Insiders.

Live Preview - VS Code Extension 📡

⚠ WARNING: This extension is still under development! ⚠

An extension that hosts a local server for you to preview your web projects on!

This extension is most useful for projects where a server is not already created (e.g. not for apps using React, Angular, etc.). To work with these, feel free to use the

integrated browser in VS Code

https://code.visualstudio.com/docs/debugtest/integrated-browser

Table of Contents

https://marketplace.visualstudio.com/items?itemName=ms-vscode.live-server#features

Running the Extension

https://marketplace.visualstudio.com/items?itemName=ms-vscode.live-server#running-the-extension

https://marketplace.visualstudio.com/items?itemName=ms-vscode.live-server#faq

Inspirations

https://marketplace.visualstudio.com/items?itemName=ms-vscode.live-server#inspirations

Issue Tracking

https://marketplace.visualstudio.com/items?itemName=ms-vscode.live-server#issue-tracking

https://marketplace.visualstudio.com/items?itemName=ms-vscode.live-server#changelog

HTML File Previewing

Preview your HTML files quickly by clicking the preview button in the top right corner of your editor or using the context menu.

Embedded Preview

A preview is available in-editor for the files hosted by the server.

#### The simple embedded browser features the following:

Page history tracking

URL bar for address-based navigation

#### Expandable menu, allowing users to:

Preview the current page in browser

Perform a page search

Tip: You can also use CTRL+F to open the find box and Enter to go to the next result

Open the editor's webview DevTools

Live Refreshing

See the changes as you make them. By default, changes appear as you make them in the editor. You can also change this in the extension settings (via

livePreview.autoRefreshPreview

) to refresh the preview on save or not at all.

Individual pages can opt out of live refreshing by adding the

data-server-no-reload

Persistent Server Task with Server Logging

If you're looking for a persistent server to run, you can run a

Live Preview

task, which also logs the server traffic. This can also be launched using the

Live Preview: Start Server Logging

command. You can click on the traffic to open the file location of the file returned by the server.

External Browser Previewing

Although all of the images above use the embedded browser, you can also experience the same features in an external browser.

You can edit the preview target in the extension settings.

External Browser Debugging

The external browser preview also supports debugging via the built-in

https://marketplace.visualstudio.com/items?itemName=ms-vscode.js-debug

extension and attaching to the

Edge Devtools Extension

https://marketplace.visualstudio.com/items?itemName=ms-edgedevtools.vscode-edge-devtools

. This allows support for features such as setting breakpoints and inspecting elements.

Live Preview: Show Debug Preview

in the command palette to get these debugging features.

Console Output Channel (For Embedded Preview)

For a simple view of the embedded preview's console messages, go to the

tab and select

Embedded Live Preview Console

in the dropdown.

Workspace-less Previewing

No workspace? No problem! For a quick preview of your file, the server can also access files outside of your workspace to preview.

#### Notes about workspace-less extension use:

Files without a workspace will be served on its own server instance and will use its absolute path as the file path.

Linked files for these pages may not be correct if they are relative to a specific root (e.g. a project root).

Tasks do not work outside of a workspace, so a server will just launch in the background upon external preview when outside of a workspace. You can use the

Live Preview: Stop Server

command to kill the server in this case.

Multi-root Support

Live Preview works cleanly with your multi-root workspaces! It will simply open an additional server for each root that you open a preview on.

You can view the ports that are open for Live Preview by hovering the status bar indicator (usually located in the bottom-right corner of the window).

Running the extension

You can install the extension

in the marketplace here

https://marketplace.visualstudio.com/items?itemName=ms-vscode.live-server

. To contribute, see the

contributing page

https://github.com/microsoft/vscode-livepreview/blob/main/CONTRIBUTING.md

Q. What does the "Previewing a file that is not a child of the server root. To see fully correct relative file links, please open a workspace at the project root or consider changing your server root settings for Live Preview." message mean?

You have no workspace open and opened a preview.

You opened a preview for a file that is not a part of your workspace(s).

You have the

livePreview.serverRoot

setting set to a sub-folder in your workspace and your file is not a child of that subfolder.

Why does this happen?

The server is hosted from the root of the workspace that the user opens (or a subfolder of the workspace based on

livePreview.serverRoot

). Files outside of this can be previewed, but some file paths (such as a link to the root) may not go to the right place.

If you are working on a web project, it is advised that you open a workspace at the root of the project.

Q. I'm trying to use Live Preview in Codespaces and the embedded preview isn't working.

A. Currently, you will need to manually navigate to the links host the forwarded port content before it works

In the area of the editor where the integrated terminal usually is, navigate to

and open the local addresses (usually at ports 3000 and 3001) in the browser. You can do this by using CTRL+Click on the URLs in the

Allow the browser to perform the necessary redirects, then close the windows. Re-open the preview window and it

Q. Why does my external browser preview look different than the preview in the embedded browser preview?

A. Aspects such as styling might look different based on the browser cache of your external browser or any other client-side state. Try clearing your cache and restarting your browser.

Inspirations

Special thanks to the following extensions for inspiring Live Preview! 💡

Live Server

https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer

Five Server

https://marketplace.visualstudio.com/items?itemName=yandeu.five-server

Issue Tracking

Please file issues against the

VS Code Live Preview repository

https://github.com/microsoft/vscode-livepreview/issues

See the project's changelog

https://github.com/microsoft/vscode-livepreview/blob/main/CHANGELOG.md

https://marketplace.visualstudio.com/search?sortBy=Installs&category=Other&target=VSCode

https://marketplace.visualstudio.com/search?term=tag%3Abrowser&target=VSCode

https://marketplace.visualstudio.com/search?term=tag%3Ahtml&target=VSCode

https://marketplace.visualstudio.com/search?term=tag%3Alive&target=VSCode

livepreview

https://marketplace.visualstudio.com/search?term=tag%3Alivepreview&target=VSCode

https://marketplace.visualstudio.com/search?term=tag%3Apreview&target=VSCode

https://marketplace.visualstudio.com/search?term=tag%3Arefresh&target=VSCode

https://marketplace.visualstudio.com/search?term=tag%3Areload&target=VSCode

https://github.com/microsoft/vscode-livepreview/issues

https://github.com/microsoft/vscode-livepreview.git

https://github.com/microsoft/vscode-livepreview#readme

https://marketplace.visualstudio.com/items/ms-vscode.live-server/license

https://marketplace.visualstudio.com/items/ms-vscode.live-server/changelog

Project Details

microsoft/vscode-livepreview

https://github.com/microsoft/vscode-livepreview

Last Commit: 3 days ago

https://github.com/microsoft/vscode-livepreview/commits

12 Pull Requests

https://github.com/microsoft/vscode-livepreview/pulls

105 Open Issues

https://github.com/microsoft/vscode-livepreview/issues

0.5.2026051301

Released on

6/21/2021, 1:33:59 PM

Last updated

5/13/2026, 2:22:18 AM

Unique Identifier

ms-vscode.live-server

Report a concern

mailto:vsmarketplace@microsoft.com?subject=Report%20abuse%20-%20ms-vscode.live-server&Body=https://marketplace.visualstudio.com/items?itemName=ms-vscode.live-server%0D%0A%3Cplease%20provide%20a%20brief%20description%20of%20the%20issue%3E

https://marketplace.visualstudio.com/items/ms-vscode.live-server/changelog

#### Last Updated

0.5.2026051301

0.5.2026043001

0.5.2026040702

0.5.2026040601

0.5.2026040201

https://www.visualstudio.com/support/support-overview-vs

https://careers.microsoft.com/

https://go.microsoft.com/fwlink/?LinkID=521839

Manage cookies

https://marketplace.visualstudio.com/items?itemName=ms-vscode.live-server

Terms of use

https://aka.ms/vsmarketplace-ToU

https://www.microsoft.com/trademarks

© 2026 Microsoft

