---
sourceFile: "Mastering Sandbox Templates and Custom Agent Environments"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.657Z"
---

# Mastering Sandbox Templates and Custom Agent Environments

b0638fd1-07d9-41df-8849-a18f87b7fc1c

Mastering Sandbox Templates and Custom Agent Environments

83022388-01d7-4f39-972b-5548f2789dfa

Every sandbox is customizable — agents install packages, pull images, and

configure tools as they work, and those changes persist for the sandbox's

lifetime. Templates capture a configured environment into a reusable image

so you don't have to set it up again every time.

Custom templates

Custom templates are reusable sandbox images that extend one of the built-in

agent environments with additional tools and configuration baked in. Instead

of asking the agent to install packages every time, build a template once and

reuse it across sandboxes and team members.

Templates make sense when multiple people need the same environment, when

setup involves steps that are tedious to repeat, or when you need pinned

versions of specific tools. For one-off work, the default image is fine —

ask the agent to install what's needed.

Custom templates customize an existing agent's environment — they don't

create new agent runtimes. The agent that launches inside the sandbox is

determined by the base image variant you extend and the agent you specify

command, not by binaries installed in the template. To

define a new agent from scratch, see

/ai/sandboxes/customize/templates/kits/#defining-an-agent

Base images

All sandbox templates are published as

docker/sandbox-templates:<variant>

. They are based on Ubuntu and run as a

user with sudo access. Most variants include Git, Docker

CLI, and common development tools like Node.js, Python, Go, and Java.

claude-code

Claude Code

https://claude.ai/download

claude-code-minimal

Claude Code with a minimal toolset (no Node.js, Python, Go, or Java)

OpenAI Codex

https://github.com/openai/codex

GitHub Copilot

https://github.com/github/copilot-cli

cursor-agent

https://cursor.com/cli

docker-agent

Docker Agent

https://github.com/docker/docker-agent

https://www.factory.ai

https://github.com/google-gemini/gemini-cli

https://kiro.dev

https://opencode.ai

No agent pre-installed. Use for manual agent setup.

Each variant also has a

version (for example,

claude-code-docker

that includes a full Docker Engine running inside the sandbox — no local Docker

daemon required. When you pick a built-in agent without specifying a custom

template variants by

The agent containers created from the

templates run in privileged

mode inside the microVM (not on your host), with a dedicated block volume at

/var/lib/docker

starts automatically inside the sandbox. The

block volume defaults to 50 GB and uses a sparse file, so it only consumes

disk space as Docker writes to it.

To override the volume size, set the

DOCKER\_SANDBOXES\_DOCKER\_SIZE

environment variable to a size string before starting the sandbox:

$ DOCKER\_SANDBOXES\_DOCKER\_SIZE=10g sbx run claude

Use the non-Docker variant if you don't need to build or run containers

inside the sandbox and want a lighter, non-privileged environment. Specify

it explicitly with

$ sbx run claude --template docker.io/docker/sandbox-templates:claude-code

Build a custom template

Building a custom template requires

Docker Desktop

https://docs.docker.com/desktop/

Write a Dockerfile that extends one of the base images. Pick the variant

that matches the agent you plan to run. For example, extend

claude-code

to customize a Claude Code environment, or

to customize an OpenAI

Codex environment.

The following example creates a Claude Code template with Rust and

protocol buffer tools pre-installed:

FROM docker/sandbox-templates:claude-code
USER root
RUN apt-get update && apt-get install -y protobuf-compiler
USER agent
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

for system-level package installations (

), and switch

before installing user-level tools. Tools that install into

the home directory, such as

, must run as

— otherwise they install under

and aren't available in

the sandbox.

#### Build the image and push it to an OCI registry, such as Docker Hub:

$ docker build -t my-org/my-template:v1 --push .

The Docker daemon used by Docker Sandboxes pulls templates from a

registry directly; it doesn't share the image store of your local Docker

daemon on the host.

\[!IMPORTANT\]

Private templates are only supported on Docker Hub.

reuses your

session to pull private images from Docker Hub. Other

registries (such as GitHub Container Registry, ECR, or a self-hosted

registry like Nexus) are pulled anonymously, so private images on those

registries fail to pull.

For locally-built images or private images on registries that

can't authenticate against, save the image to a tar and load it

directly into the sandbox runtime instead of pulling from a registry:

$ docker image save my-org/my-template:v1 -o my-template.tar
$ sbx template load my-template.tar
$ sbx run --template my-org/my-template:v1 claude

sbx template load

imports the tar into the sandbox runtime's image

store, so the image doesn't need to be reachable from a registry at

sandbox creation time.

Unless you use the permissive

network policy, you may also need

to allow-list any domains that your custom tools depend on:

$ sbx policy allow network -g "\*.example.com:443,example.com:443"

Then run a sandbox with your template. The agent you specify must match

the base image variant your template extends:

$ sbx run --template docker.io/my-org/my-template:v1 claude

Because this template extends the

claude-code

base image, you run it

. If you extend

; if you extend

(which drops you into a Bash shell with no agent).

Unlike Docker commands,

does not automatically resolve the Docker

Hub domain (

) in image references.

Template caching

Template images are cached locally. The first use pulls from the registry;

subsequent sandboxes reuse the cache. Cached images persist across sandbox

creation and deletion, and are cleared when you run

Saving a sandbox as a template

Instead of writing a Dockerfile, you can save a running sandbox's state as

a template. This captures installed packages, configuration changes, and

files into a reusable image — useful when you've set up an environment

interactively and want to preserve it.

Save and reuse

Stop the sandbox (or let the CLI prompt you), then save it with a name and

$ sbx template save my-sandbox my-template:v1

The image is stored in the sandbox runtime's local image store. Create a

new sandbox from it with the

$ sbx run -t my-template:v1 claude

List and remove templates

#### List all saved templates:

$ sbx template ls

#### Remove a template you no longer need:

$ sbx template rm my-template:v1

Export and import

To share a saved template or move it to another machine, export it as a

$ sbx template save my-sandbox my-template:v1 --output my-template.tar

#### On the other machine, load the tar file and use it:

$ sbx template load my-template.tar
$ sbx run -t my-template:v1 claude

Limitations

Agent configuration files are always recreated when a sandbox is created.

Changes to user-level agent configuration files, such as

/home/agent/.claude/settings.json

/home/agent/.claude.json

persist in saved templates.

If the saved template was built for a different agent than the one you

, you get a warning. For example, saving a Claude

sandbox and running it with

⚠ WARNING: template "my-template:v1" was built for the "claude" agent but you are using "codex".
  The sandbox may not work correctly. Consider using: sbx run -t my-template:v1 claude

