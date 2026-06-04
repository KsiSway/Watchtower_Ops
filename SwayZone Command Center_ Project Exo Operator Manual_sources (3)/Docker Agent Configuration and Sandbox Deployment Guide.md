---
sourceFile: "Docker Agent Configuration and Sandbox Deployment Guide"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.277Z"
---

# Docker Agent Configuration and Sandbox Deployment Guide

57756a23-37f1-4ad7-9c83-de2dec0dc123

Docker Agent Configuration and Sandbox Deployment Guide

0773d5af-0b70-4a99-a2e1-42c005774bef

Docker Agent

#### Official documentation:

Docker Agent

https://docs.docker.com/ai/docker-agent/

Quick start

#### Create a sandbox and run Docker Agent for a project directory:

$ sbx run docker-agent ~/my-project

The workspace parameter defaults to the current directory, so

sbx run docker-agent

from inside your project works too.

Authentication

Docker Agent supports multiple providers. Store keys for the providers you want

to use with

stored secrets

/ai/sandboxes/security/credentials/#stored-secrets

$ sbx secret set -g openai
$ sbx secret set -g anthropic
$ sbx secret set -g google
$ sbx secret set -g xai
$ sbx secret set -g nebius
$ sbx secret set -g mistral

You only need to configure the providers you want to use. Docker Agent detects

available credentials and routes requests to the appropriate provider.

Alternatively, export the environment variables (

OPENAI\_API\_KEY

ANTHROPIC\_API\_KEY

GOOGLE\_API\_KEY

XAI\_API\_KEY

NEBIUS\_API\_KEY

MISTRAL\_API\_KEY

) in your shell before running the sandbox. See

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

The sandbox runs Docker Agent without approval prompts by default. Pass

additional CLI options after

$ sbx run docker-agent --name my-sandbox -- <options>

For example, to specify a custom

configuration file:

$ sbx run docker-agent -- agent.yml

The sandbox uses

docker/sandbox-templates:docker-agent

and launches Docker

Agent without approval prompts by default. See

/ai/sandboxes/customize/templates/

to build your own image on top of

