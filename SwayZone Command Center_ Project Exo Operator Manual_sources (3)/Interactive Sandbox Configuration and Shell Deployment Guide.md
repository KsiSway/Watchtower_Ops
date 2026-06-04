---
sourceFile: "Interactive Sandbox Configuration and Shell Deployment Guide"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.502Z"
---

# Interactive Sandbox Configuration and Shell Deployment Guide

e24f93cf-bf49-414a-a22b-5a822e8fb397

Interactive Sandbox Configuration and Shell Deployment Guide

94de74bb-cde4-4681-8087-1b8074d49c78

sbx run shell

drops you into a Bash login shell inside a sandbox with no

pre-installed agent binary. It's useful for installing and configuring

agents manually, testing custom implementations, or inspecting a running

environment.

$ sbx run shell ~/my-project

The workspace path defaults to the current directory. To run a one-off

command instead of an interactive shell, pass it after

$ sbx run shell -- -c "echo 'Hello from sandbox'"

Set your API keys as environment variables so the sandbox proxy can inject

them into API requests automatically. Credentials are never stored inside

$ export ANTHROPIC\_API\_KEY=sk-ant-xxxxx
$ export OPENAI\_API\_KEY=sk-xxxxx

Once inside the shell, you can install agents using their standard methods,

for example

npm install -g @continuedev/cli

. For complex setups, build a

custom template

/ai/sandboxes/customize/templates/

instead of installing

interactively each time.

The shell sandbox uses the

base image — the common base environment

without a pre-installed agent.

