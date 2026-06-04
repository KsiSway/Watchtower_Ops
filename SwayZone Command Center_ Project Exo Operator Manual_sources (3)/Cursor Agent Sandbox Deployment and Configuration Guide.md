---
sourceFile: "Cursor Agent Sandbox Deployment and Configuration Guide"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.223Z"
---

# Cursor Agent Sandbox Deployment and Configuration Guide

afb4fb67-a0c8-4bb8-bc66-b98ecfb5477d

Cursor Agent Sandbox Deployment and Configuration Guide

8cf7722e-a3ce-4622-a208-f203f48558eb

This guide covers authentication, configuration, and usage of Cursor in a

sandboxed environment.

#### Official documentation:

https://cursor.com/cli

Quick start

#### Create a sandbox and run Cursor for a project directory:

$ sbx run cursor ~/my-project

#### The workspace parameter is optional and defaults to the current directory:

$ cd ~/my-project
$ sbx run cursor

Authentication

Cursor supports two authentication methods: an API key or OAuth.

: Store your Cursor API key using

stored secrets

/ai/sandboxes/security/credentials/#stored-secrets

$ sbx secret set -g cursor

Alternatively, export the

CURSOR\_API\_KEY

environment variable in your shell

before running the sandbox. See

Credentials

/ai/sandboxes/security/credentials/

for details on both methods.

: If no API key is set, Cursor prompts you to sign in interactively

on first run. The proxy intercepts the token exchange with

api2.cursor.sh/auth/poll

, so credentials are managed by the host and aren't

stored inside the sandbox.

Configuration

Sandboxes don't pick up user-level configuration from your host, such as

. Only project-level configuration in the working directory is

available inside the sandbox. See

Why doesn't the sandbox use my user-level agent configuration?

/ai/sandboxes/faq/#why-doesnt-the-sandbox-use-my-user-level-agent-configuration

for workarounds.

Cursor reads

from the workspace for agent-specific instructions.

The sandbox runs Cursor in YOLO mode by default, which executes commands

without approval prompts. Pass additional

cursor-agent

CLI options after

$ sbx run cursor --name <sandbox-name> -- <cursor-options>

docker/sandbox-templates:cursor-agent-docker

Preconfigured to run in YOLO mode with HTTP/1.1 and server-sent events for

agent traffic so requests flow through the host proxy. Authentication state

is persisted across sandbox restarts.

/ai/sandboxes/customize

to pre-install tools or customize this

environment.

