---
sourceFile: "Droid Integration Guide for Factory Sandboxes"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.343Z"
---

# Droid Integration Guide for Factory Sandboxes

7e32d3dc-a406-497a-9f02-c6cc9d86fd14

Droid Integration Guide for Factory Sandboxes

681bd685-140f-435b-8922-037c46914853

This guide covers authentication, configuration, and usage of Droid, an AI

coding agent by Factory, in a sandboxed environment.

#### Official documentation:

https://docs.factory.ai/

Quick start

#### Create a sandbox and run Droid for a project directory:

$ sbx run droid ~/my-project

#### The workspace parameter is optional and defaults to the current directory:

$ cd ~/my-project
$ sbx run droid

Authentication

Droid requires a

Factory account

https://factory.ai

. Both authentication

methods authenticate you to Factory's service directly — unlike other agents

where you supply a model provider key, Factory manages model access through

your Factory account.

: Store your Factory API key using

stored secrets

/ai/sandboxes/security/credentials/#stored-secrets

$ sbx secret set -g droid

Alternatively, export the

FACTORY\_API\_KEY

environment variable in your shell

before running the sandbox. See

Credentials

/ai/sandboxes/security/credentials/

for details on both methods.

: If no API key is set, Droid prompts you to authenticate

interactively on first run. The proxy handles the OAuth flow, so credentials

aren't stored inside the sandbox.

Configuration

Sandboxes don't pick up user-level configuration from your host. Only

project-level configuration in the working directory is available inside the

sandbox. See

Why doesn't the sandbox use my user-level agent configuration?

/ai/sandboxes/faq/#why-doesnt-the-sandbox-use-my-user-level-agent-configuration

for workarounds.

The sandbox runs Droid without approval prompts by default. Pass additional

CLI options after

$ sbx run droid --name <sandbox-name> -- <droid-options>

docker/sandbox-templates:droid-docker

Preconfigured to run without approval prompts. Authentication state is

persisted across sandbox restarts.

/ai/sandboxes/customize

to pre-install tools or customize this

environment.

