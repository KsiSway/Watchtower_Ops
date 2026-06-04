---
sourceFile: "Gemini Sandbox Integration and Configuration Guide"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.422Z"
---

# Gemini Sandbox Integration and Configuration Guide

e0c6669c-cad0-4215-bc24-8bc4f3ed49e0

Gemini Sandbox Integration and Configuration Guide

625314c8-bf04-4361-b123-2c94e7c57912

This guide covers authentication, configuration, and usage of Google Gemini in

a sandboxed environment.

#### Official documentation:

https://geminicli.com/docs/

Quick start

#### Create a sandbox and run Gemini for a project directory:

$ sbx run gemini ~/my-project

#### The workspace parameter is optional and defaults to the current directory:

$ cd ~/my-project
$ sbx run gemini

Authentication

Gemini requires either a Google API key or a Google account with Gemini access.

: Store your key using

stored secrets

/ai/sandboxes/security/credentials/#stored-secrets

$ sbx secret set -g google

Alternatively, export the

GEMINI\_API\_KEY

GOOGLE\_API\_KEY

environment

variable in your shell before running the sandbox. See

Credentials

/ai/sandboxes/security/credentials/

for details on both methods.

Google account

: If no API key is set, Gemini prompts you to sign in

interactively when it starts. Interactive authentication is scoped to the

sandbox and doesn't persist if you remove and recreate it.

Configuration

Sandboxes don't pick up user-level configuration from your host, such as

. Only project-level configuration in the working directory is

available inside the sandbox. See

Why doesn't the sandbox use my user-level agent configuration?

/ai/sandboxes/faq/#why-doesnt-the-sandbox-use-my-user-level-agent-configuration

for workarounds.

The sandbox runs Gemini without approval prompts by default and disables

Gemini's built-in sandbox tool (since the sandbox itself provides isolation).

Pass additional Gemini CLI options after

$ sbx run gemini --name <sandbox-name> -- <gemini-options>

docker/sandbox-templates:gemini

Gemini is configured to disable its built-in OAuth flow. Authentication is

managed through the proxy with API keys. Preconfigured to run without

approval prompts.

/ai/sandboxes/customize

to pre-install tools or customize this

environment.

