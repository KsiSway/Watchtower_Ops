---
sourceFile: "Sandboxed GitHub Copilot CLI Configuration Guide"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.692Z"
---

# Sandboxed GitHub Copilot CLI Configuration Guide

c8263da3-46ad-4e72-b0de-fb74af7e7695

Sandboxed GitHub Copilot CLI Configuration Guide

198a510c-baec-4702-b930-9a9c847c270a

This guide covers authentication, configuration, and usage of GitHub Copilot

in a sandboxed environment.

#### Official documentation:

GitHub Copilot CLI

https://docs.github.com/en/copilot/how-tos/copilot-cli

Quick start

#### Create a sandbox and run Copilot for a project directory:

$ sbx run copilot ~/my-project

#### The workspace parameter is optional and defaults to the current directory:

$ cd ~/my-project
$ sbx run copilot

Authentication

Copilot requires a GitHub token with Copilot access. Store your token using

stored secrets

/ai/sandboxes/security/credentials/#stored-secrets

$ echo "$(gh auth token)" | sbx secret set -g github

Alternatively, export the

GITHUB\_TOKEN

environment variable in

your shell before running the sandbox. See

Credentials

/ai/sandboxes/security/credentials/

for details on both methods.

Configuration

Sandboxes don't pick up user-level configuration from your host. Only

project-level configuration in the working directory is available inside the

sandbox. See

Why doesn't the sandbox use my user-level agent configuration?

/ai/sandboxes/faq/#why-doesnt-the-sandbox-use-my-user-level-agent-configuration

for workarounds.

Copilot is configured to trust the workspace directory by default, so it

operates without repeated confirmations for workspace files.

Pass options at runtime

Pass Copilot CLI options after

$ sbx run copilot --name <sandbox-name> -- <copilot-options>

docker/sandbox-templates:copilot

Preconfigured to trust the workspace directory and run without approval prompts.

/ai/sandboxes/customize

to pre-install tools or customize this

environment.

