---
sourceFile: "Intro | AI coding agent built for the terminal"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.502Z"
---

# Intro | AI coding agent built for the terminal

9460787f-019f-4b5d-8ad3-b844059afd69

Intro | AI coding agent built for the terminal

6188dd6b-912f-4234-aae2-783af675bc5c

https://opencode.ai/docs

Intro | AI coding agent built for the terminal

Skip to content

https://opencode.ai/docs#\_top

https://opencode.ai/docs/

app.header.home

https://opencode.ai/

app.header.docs

https://opencode.ai/docs/

https://github.com/anomalyco/opencode

https://opencode.ai/discord

https://opencode.ai/docs/

https://opencode.ai/docs/config/

https://opencode.ai/docs/providers/

https://opencode.ai/docs/network/

https://opencode.ai/docs/enterprise/

Troubleshooting

https://opencode.ai/docs/troubleshooting/

https://opencode.ai/docs/windows-wsl

https://opencode.ai/docs/go/

https://opencode.ai/docs/tui/

https://opencode.ai/docs/cli/

https://opencode.ai/docs/web/

https://opencode.ai/docs/ide/

https://opencode.ai/docs/zen/

https://opencode.ai/docs/share/

https://opencode.ai/docs/github/

https://opencode.ai/docs/gitlab/

https://opencode.ai/docs/tools/

https://opencode.ai/docs/rules/

https://opencode.ai/docs/agents/

https://opencode.ai/docs/models/

https://opencode.ai/docs/themes/

https://opencode.ai/docs/keybinds/

https://opencode.ai/docs/commands/

https://opencode.ai/docs/formatters/

Permissions

https://opencode.ai/docs/permissions/

LSP Servers

https://opencode.ai/docs/lsp/

MCP servers

https://opencode.ai/docs/mcp-servers/

ACP Support

https://opencode.ai/docs/acp/

Agent Skills

https://opencode.ai/docs/skills/

Custom Tools

https://opencode.ai/docs/custom-tools/

https://opencode.ai/docs/sdk/

https://opencode.ai/docs/server/

https://opencode.ai/docs/plugins/

https://opencode.ai/docs/ecosystem/

https://github.com/anomalyco/opencode

https://opencode.ai/discord

Select theme

Select language

Norsk Bokmål

Português (Brasil)

On this page

https://opencode.ai/docs#\_top

https://opencode.ai/docs#install

https://opencode.ai/docs#configure

https://opencode.ai/docs#initialize

https://opencode.ai/docs#usage

Ask questions

https://opencode.ai/docs#ask-questions

Add features

https://opencode.ai/docs#add-features

Make changes

https://opencode.ai/docs#make-changes

Undo changes

https://opencode.ai/docs#undo-changes

https://opencode.ai/docs#share

https://opencode.ai/docs#customize

On this page

https://opencode.ai/docs#\_top

https://opencode.ai/docs#install

https://opencode.ai/docs#configure

https://opencode.ai/docs#initialize

https://opencode.ai/docs#usage

Ask questions

https://opencode.ai/docs#ask-questions

Add features

https://opencode.ai/docs#add-features

Make changes

https://opencode.ai/docs#make-changes

Undo changes

https://opencode.ai/docs#undo-changes

https://opencode.ai/docs#share

https://opencode.ai/docs#customize

Get started with OpenCode.

https://opencode.ai/

is an open source AI coding agent. It's available as a terminal-based interface, desktop app, or IDE extension.

Let's get started.

Prerequisites

https://opencode.ai/docs#prerequisites

#### To use OpenCode in your terminal, you'll need:

#### A modern terminal emulator like:

https://wezterm.org/

, cross-platform

https://alacritty.org/

, cross-platform

https://ghostty.org/

, Linux and macOS

https://sw.kovidgoyal.net/kitty/

, Linux and macOS

API keys for the LLM providers you want to use.

https://opencode.ai/docs#install

The easiest way to install OpenCode is through the install script.

Terminal window

curl -fsSL https://opencode.ai/install | bash

#### You can also install it with the following commands:

Using Node.js

https://opencode.ai/docs#tab-panel-0

https://opencode.ai/docs#tab-panel-1

https://opencode.ai/docs#tab-panel-2

https://opencode.ai/docs#tab-panel-3

Terminal window

npm install -g opencode-ai

Terminal window

bun install -g opencode-ai

Terminal window

pnpm install -g opencode-ai

Terminal window

yarn global add opencode-ai

Using Homebrew on macOS and Linux

Terminal window

brew install anomalyco/tap/opencode

We recommend using the OpenCode tap for the most up to date releases. The official

brew install opencode

formula is maintained by the Homebrew team and is updated less frequently.

Installing on Arch Linux

Terminal window

sudo pacman -S opencode           # Arch Linux (Stable)
paru -S opencode-bin              # Arch Linux (Latest from AUR)

https://opencode.ai/docs#windows

Recommended: Use WSL

For the best experience on Windows, we recommend using

Windows Subsystem for Linux (WSL)

https://opencode.ai/docs/windows-wsl

. It provides better performance and full compatibility with OpenCode's features.

Using Chocolatey

Terminal window

choco install opencode

Using Scoop

Terminal window

scoop install opencode

Terminal window

npm install -g opencode-ai

Terminal window

mise use -g github:anomalyco/opencode

Using Docker

Terminal window

docker run -it --rm ghcr.io/anomalyco/opencode

Support for installing OpenCode on Windows using Bun is currently in progress.

You can also grab the binary from the

https://github.com/anomalyco/opencode/releases

https://opencode.ai/docs#configure

With OpenCode you can use any LLM provider by configuring their API keys.

If you are new to using LLM providers, we recommend using

OpenCode Zen

https://opencode.ai/docs/zen

. It's a curated list of models that have been tested and verified by the OpenCode team.

command in the TUI, select opencode, and head to

opencode.ai/auth

https://opencode.ai/auth

Sign in, add your billing details, and copy your API key.

Paste your API key.

┌ API key
│
│
└ enter

Alternatively, you can select one of the other providers.

https://opencode.ai/docs/providers#directory

https://opencode.ai/docs#initialize

Now that you've configured a provider, you can navigate to a project that you want to work on.

Terminal window

cd /path/to/project

And run OpenCode.

Terminal window

Next, initialize OpenCode for the project by running the following command.

This will get OpenCode to analyze your project and create an

file in the project root.

You should commit your project's

file to Git.

This helps OpenCode understand the project structure and the coding patterns used.

https://opencode.ai/docs#usage

You are now ready to use OpenCode to work on your project. Feel free to ask it anything!

If you are new to using an AI coding agent, here are some examples that might help.

Ask questions

https://opencode.ai/docs#ask-questions

You can ask OpenCode to explain the codebase to you.

key to fuzzy search for files in the project.

How is authentication handled in @packages/functions/src/api/index.ts

This is helpful if there's a part of the codebase that you didn't work on.

Add features

https://opencode.ai/docs#add-features

You can ask OpenCode to add new features to your project. Though we first recommend asking it to create a plan.

Create a plan

OpenCode has a

that disables its ability to make changes and instead suggest

it'll implement the feature. Switch to it using the

key. You'll see an indicator for this in the lower right corner.

Now let's describe what we want it to do.

When a user deletes a note, we'd like to flag it as deleted in the database.
Then create a screen that shows all the recently deleted notes.
From this screen, the user can undelete a note or permanently delete it.

You want to give OpenCode enough details to understand what you want. It helps to talk to it like you are talking to a junior developer on your team. Tip Give OpenCode plenty of context and examples to help it understand what you want.

Iterate on the plan

Once it gives you a plan, you can give it feedback or add more details.

We'd like to design this new screen using a design I've used before.
\[Image #1\] Take a look at this image and use it as a reference.

Tip Drag and drop images into the terminal to add them to the prompt. OpenCode can scan any images you give it and add them to the prompt. You can do this by dragging and dropping an image into the terminal.

Build the feature

Once you feel comfortable with the plan, switch back to

by hitting the

And asking it to make the changes.

Sounds good! Go ahead and make the changes.

Make changes

https://opencode.ai/docs#make-changes

For more straightforward changes, you can ask OpenCode to directly build it without having to review the plan first.

We need to add authentication to the /settings route. Take a look at how this is
handled in the /notes route in @packages/functions/src/notes.ts and implement
the same logic in @packages/functions/src/settings.ts

You want to make sure you provide a good amount of detail so OpenCode makes the right changes.

Undo changes

https://opencode.ai/docs#undo-changes

Let's say you ask OpenCode to make some changes.

Can you refactor the function in @packages/functions/src/api/index.ts?

But you realize that it is not what you wanted. You

the changes using the

OpenCode will now revert the changes you made and show your original message again.

Can you refactor the function in @packages/functions/src/api/index.ts?

From here you can tweak the prompt and ask OpenCode to try again.

You can run

multiple times to undo multiple changes.

the changes using the

https://opencode.ai/docs#share

The conversations that you have with OpenCode can be

shared with your team

https://opencode.ai/docs/share

This will create a link to the current conversation and copy it to your clipboard.

Conversations are not shared by default.

example conversation

https://opencode.ai/s/4XP1fce5

with OpenCode.

https://opencode.ai/docs#customize

And that's it! You are now a pro at using OpenCode.

To make it your own, we recommend

picking a theme

https://opencode.ai/docs/themes

customizing the keybinds

https://opencode.ai/docs/keybinds

configuring code formatters

https://opencode.ai/docs/formatters

creating custom commands

https://opencode.ai/docs/commands

, or playing around with the

OpenCode config

https://opencode.ai/docs/config

https://github.com/anomalyco/opencode/edit/dev/packages/web/src/content/docs/index.mdx

Found a bug? Open an issue

https://github.com/anomalyco/opencode/issues/new

Join our Discord community

https://opencode.ai/discord

Select language

Norsk Bokmål

Português (Brasil)

https://anoma.ly/

Last updated: May 13, 2026

