---
sourceFile: "Build and run agentic AI applications with Docker | Docker Docs"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.166Z"
---

# Build and run agentic AI applications with Docker | Docker Docs

cc210372-f719-4b71-ba09-e4d0e141e222

Build and run agentic AI applications with Docker | Docker Docs

7e7685d4-bc6a-462a-8bbe-c64e11c9cad8

https://docs.docker.com/guides/agentic-ai/

Build and run agentic AI applications with Docker | Docker Docs

Insights on the state of AI agents from 800+ builders and leaders. Download your copy

https://www.docker.com/resources/the-state-of-agentic-ai-white-paper/

https://docs.docker.com/

Get started

https://docs.docker.com/get-started/

https://docs.docker.com/guides/

https://docs.docker.com/manuals/

https://docs.docker.com/reference/

Gordon, your AI assistant for Docker docs

Start a new chat

What can I help you with?

I'm Gordon, your AI assistant for Docker and documentation questions.

Get started with Docker

Docker Hardened Images

MCP Toolkit

Create an org

When enabled, Gordon considers the current page you're viewing to provide more relevant answers.

Share feedback

https://github.com/docker/docs/issues/23966

Answers are generated based on the documentation.

https://docs.docker.com/guides/

Get started

https://docs.docker.com/get-started/

https://docs.docker.com/manuals/

https://docs.docker.com/reference/

Build and run agentic AI applications with Docker

https://docs.docker.com/guides/agentic-ai/

Learn how to create AI agent applications using Docker Model Runner, and MCP Toolkit.

« Back to all guides

https://docs.docker.com/guides/

https://docs.docker.com/

https://docs.docker.com/guides/

/ Agentic AI applications

Build and run agentic AI applications with Docker

Ask Gordon Copy Markdown View Markdown

Table of contents

Introduction

https://docs.docker.com/guides/agentic-ai/#introduction

Prerequisites

https://docs.docker.com/guides/agentic-ai/#prerequisites

Step 1: Clone the sample application

https://docs.docker.com/guides/agentic-ai/#step-1-clone-the-sample-application

Step 2: Run the application locally

https://docs.docker.com/guides/agentic-ai/#step-2-run-the-application-locally

Step 3: Review the application environment

https://docs.docker.com/guides/agentic-ai/#step-3-review-the-application-environment

Step 4: Review the application

https://docs.docker.com/guides/agentic-ai/#step-4-review-the-application

https://docs.docker.com/guides/agentic-ai/#summary

This guide uses the familiar Docker Compose workflow to orchestrate agentic AI applications. For a smoother development experience, check out

Docker Agent

https://docs.docker.com/ai/docker-agent/

, a purpose-built agent runtime that simplifies running and managing AI agents.

Introduction

https://docs.docker.com/guides/agentic-ai/#introduction

Agentic applications are transforming how software gets built. These apps don't just respond, they decide, plan, and act. They're powered by models, orchestrated by agents, and integrated with APIs, tools, and services in real time.

All these new agentic applications, no matter what they do, share a common architecture. It's a new kind of stack, built from three core components:

Models: These are your GPTs, CodeLlamas, Mistrals. They're doing the reasoning, writing, and planning. They're the engine behind the intelligence.

Agent: This is where the logic lives. Agents take a goal, break it down, and figure out how to get it done. They orchestrate everything. They talk to the UI, the tools, the model, and the gateway.

MCP gateway: This is what links your agents to the outside world, including APIs, tools, and services. It provides a standard way for agents to call capabilities via the Model Context Protocol (MCP).

Docker makes this AI-powered stack simpler, faster, and more secure by unifying models, and tool gateways into a developer-friendly workflow that uses Docker Compose.

This guide walks you through the core components of agentic development and shows how Docker ties them all together with the following tools:

Docker Model Runner

https://docs.docker.com/ai/model-runner/

lets you run LLMs locally with simple command and OpenAI-compatible APIs.

Docker MCP Catalog and Toolkit

https://docs.docker.com/ai/mcp-catalog-and-toolkit/

helps you discover and securely run external tools, like APIs and databases, using the Model Context Protocol (MCP).

Docker MCP Gateway

https://docs.docker.com/ai/mcp-catalog-and-toolkit/mcp-gateway/

lets you orchestrate and manage MCP servers.

Docker Compose

https://docs.docker.com/ai/compose/models-and-compose/

is the tool that ties it all together, letting you define and run multi-container applications with a single file.

For this guide, you'll use the same Compose workflow you're already familiar with. Then, you'll dig into the Compose file, Dockerfile, and app to see how it all works together.

Prerequisites

https://docs.docker.com/guides/agentic-ai/#prerequisites

#### To follow this guide, you need to:

Install Docker Desktop 4.43 or later

https://docs.docker.com/get-started/get-docker/

Enable Docker Model Runner

https://docs.docker.com/ai/model-runner/#enable-dmr-in-docker-desktop

#### At least the following hardware specifications:

VRAM: 3.5 GB

Storage: 2.31 GB

Step 1: Clone the sample application

https://docs.docker.com/guides/agentic-ai/#step-1-clone-the-sample-application

You'll use an existing sample application that demonstrates how to connect a model to an external tool using Docker's AI features.

$ git clone https://github.com/docker/compose-for-agents.git
$ cd compose-for-agents/adk/

Step 2: Run the application locally

https://docs.docker.com/guides/agentic-ai/#step-2-run-the-application-locally

Your machine must meet the necessary hardware requirements to run the entire application stack locally using Docker Compose. This lets you test the application end-to-end, including the model and MCP gateway, without needing to run in the cloud. This particular example uses the

Gemma 3 4B model

https://hub.docker.com/r/ai/gemma3

with a context size of

#### Hardware requirements:

VRAM: 3.5 GB

Storage: 2.31 GB

If your machine exceeds those requirements, consider running the application with a larger context size or a larger model to improve the agents performance. You can easily update model and context size in the

compose.yaml

#### To run the application locally, follow these steps:

directory of the cloned repository, run the following command in a terminal to build and run the application:

$ docker compose up

The first time you run this command, Docker pulls the model from Docker Hub, which may take some time.

http://localhost:8080

http://localhost:8080/

. Enter a correct or incorrect fact in the prompt and hit enter. An agent searches DuckDuckGo to verify it and another agent revises the output.

3. Press ctrl-c in the terminal to stop the application when you're done.

Step 3: Review the application environment

https://docs.docker.com/guides/agentic-ai/#step-3-review-the-application-environment

You can find the

compose.yaml

file in the

directory. Open it in a text editor to see how the services are defined.

compose.yaml

services:
  adk:
    build:
      context: .
    ports:
      # expose port for web interface
      - "8080:8080"
    environment:
      # point adk at the MCP gateway
      - MCPGATEWAY\_ENDPOINT=http://mcp-gateway:8811/sse
    depends\_on:
      - mcp-gateway
    models:
      gemma3:
        endpoint\_var: MODEL\_RUNNER\_URL
        model\_var: MODEL\_RUNNER\_MODEL

  mcp-gateway:
    # mcp-gateway secures your MCP servers
    image: docker/mcp-gateway:latest
    use\_api\_socket: true
    command:
      - --transport=sse
      # add any MCP servers you want to use
      - --servers=duckduckgo

models:
  gemma3:
    # pre-pull the model when starting Docker Model Runner
    model: ai/gemma3:4B-Q4\_0
    context\_size: 10000 # 3.5 GB VRAM
    # increase context size to handle search results
    # context\_size: 131000 # 7.6 GB VRAM

#### The app consists of three main components:

service, which is the web application that runs the agentic AI application. This service talks to the MCP gateway and model.

mcp-gateway

service, which is the MCP gateway that connects the app to external tools and services.

block, which defines the model to use with the application.

When you examine the

compose.yaml

file, you'll notice two notable elements for the model:

A service‑level

block in the

A top-level

These two blocks together let Docker Compose automatically start and connect your ADK web app to the specified LLM.

Looking for more models to use? Check out the

Docker AI Model Catalog

https://hub.docker.com/catalogs/models/

When examining the

compose.yaml

file, you'll notice the gateway service is a Docker-maintained image,

docker/mcp-gateway:latest

https://hub.docker.com/r/docker/agents\_gateway

. This image is Docker's open source

MCP Gateway

https://github.com/docker/docker-mcp/

that enables your application to connect to MCP servers, which expose tools that models can call. In this example, it uses the

duckduckgo MCP server

https://hub.docker.com/mcp/server/duckduckgo/overview

to perform web searches.

Looking for more MCP servers to use? Check out the

Docker MCP Catalog

https://hub.docker.com/catalogs/mcp/

With only a few lines of instructions in a Compose file, you're able to run and connect all the necessary services of an agentic AI application.

In addition to the Compose file, the Dockerfile and the

entrypoint.sh

script it creates, play a role in wiring up the AI stack at build and runtime. You can find the

directory. Open it in a text editor.

# Use Python 3.11 slim image as base
FROM python:3.13-slim
ENV PYTHONUNBUFFERED=1

RUN pip install uv

WORKDIR /app
# Install system dependencies
COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv \
    UV\_COMPILE\_BYTECODE=1 UV\_LINK\_MODE=copy \
    uv pip install --system .
# Copy application code
COPY agents/ ./agents/
RUN python -m compileall -q .

COPY <<EOF /entrypoint.sh
#!/bin/sh
set -e

if test -f /run/secrets/openai-api-key; then
    export OPENAI\_API\_KEY=$(cat /run/secrets/openai-api-key)
fi

if test -n "\${OPENAI\_API\_KEY}"; then
    echo "Using OpenAI with \${OPENAI\_MODEL\_NAME}"
else
    echo "Using Docker Model Runner with \${MODEL\_RUNNER\_MODEL}"
    export OPENAI\_BASE\_URL=\${MODEL\_RUNNER\_URL}
    export OPENAI\_MODEL\_NAME=openai/\${MODEL\_RUNNER\_MODEL}
    export OPENAI\_API\_KEY=cannot\_be\_empty
fi
exec adk web --host 0.0.0.0 --port 8080 --log\_level DEBUG
EOF
RUN chmod +x /entrypoint.sh

# Create non-root user
RUN useradd --create-home --shell /bin/bash app \
    && chown -R app:app /app
USER app

ENTRYPOINT \[ "/entrypoint.sh" \]

entrypoint.sh

has five key environment variables:

MODEL\_RUNNER\_URL

: Injected by Compose (via the service-level

block) to point at your Docker Model Runner HTTP endpoint.

MODEL\_RUNNER\_MODEL

: Injected by Compose to select which model to launch in Model Runner.

OPENAI\_API\_KEY

: If you define an

openai-api-key

secret in your Compose file, Compose will mount it at

/run/secrets/openai-api-key

. The entrypoint script reads that file and exports it as

OPENAI\_API\_KEY

, causing the app to use hosted OpenAI instead of Model Runner.

OPENAI\_BASE\_URL

: When no real key is present, this is set to

MODEL\_RUNNER\_URL

so the ADK's OpenAI-compatible client sends requests to Docker Model Runner.

OPENAI\_MODEL\_NAME

: When falling back to Model Runner, the model is prefixed with

so the client picks up the right model alias.

Together, these variables let the same ADK web server code seamlessly target either:

Hosted OpenAI: if you supply

OPENAI\_API\_KEY

(and optionally

OPENAI\_MODEL\_NAME

Model Runner: by remapping

MODEL\_RUNNER\_URL

MODEL\_RUNNER\_MODEL

into the OpenAI client's expected variables

Step 4: Review the application

https://docs.docker.com/guides/agentic-ai/#step-4-review-the-application

web application is an agent implementation that connects to the MCP gateway and a model through environment variables and API calls. It uses the

ADK (Agent Development Kit)

https://github.com/google/adk-python

to define a root agent named Auditor, which coordinates two sub-agents, Critic and Reviser, to verify and refine model-generated answers.

#### The three agents are:

Critic: Verifies factual claims using the toolset, such as DuckDuckGo.

Reviser: Edits answers based on the verification verdicts provided by the Critic.

Auditor: A higher-level agent that sequences the Critic and Reviser. It acts as the entry point, evaluating LLM-generated answers, verifying them, and refining the final output.

All of the application's behavior is defined in Python under the

directory. Here's a breakdown of the notable files:

agents/agent.py

: Defines the Auditor, a SequentialAgent that chains together the Critic and Reviser agents. This agent is the main entry point of the application and is responsible for auditing LLM-generated content using real-world verification tools.

agents/sub\_agents/critic/agent.py

: Defines the Critic agent. It loads the language model (via Docker Model Runner), sets the agent's name and behavior, and connects to MCP tools (like DuckDuckGo).

agents/sub\_agents/critic/prompt.py

: Contains the Critic prompt, which instructs the agent to extract and verify claims using external tools.

agents/sub\_agents/critic/tools.py

: Defines the MCP toolset configuration, including parsing

strings, creating tool connections, and handling MCP gateway communication.

agents/sub\_agents/reviser/agent.py

: Defines the Reviser agent, which takes the Critic's findings and minimally rewrites the original answer. It also includes callbacks to clean up the LLM output and ensure it's in the right format.

agents/sub\_agents/reviser/prompt.py

: Contains the Reviser prompt, which instructs the agent to revise the answer text based on the verified claim verdicts.

The MCP gateway is configured via the

MCPGATEWAY\_ENDPOINT

environment variable. In this case,

http://mcp-gateway:8811/sse

. This allows the app to use Server-Sent Events (SSE) to communicate with the MCP gateway container, which itself brokers access to external tool services like DuckDuckGo.

https://docs.docker.com/guides/agentic-ai/#summary

Agent-based AI applications are emerging as a powerful new software architecture. In this guide, you explored a modular, chain-of-thought system where an Auditor agent coordinates the work of a Critic and a Reviser to fact-check and refine model-generated answers. This architecture shows how to combine local model inference with external tool integrations in a structured, modular way.

You also saw how Docker simplifies this process by providing a suite of tools that support agentic AI development:

Docker Model Runner

https://docs.docker.com/ai/model-runner/

: Run and serve open-source models locally via OpenAI-compatible APIs.

Docker MCP Catalog and Toolkit

https://docs.docker.com/ai/mcp-catalog-and-toolkit/

: Launch and manage tool integrations that follow the Model Context Protocol (MCP) standard.

Docker MCP Gateway

https://docs.docker.com/ai/mcp-catalog-and-toolkit/mcp-gateway/

: Orchestrate and manage MCP servers to connect agents to external tools and services.

Docker Compose

https://docs.docker.com/ai/compose/models-and-compose/

: Define and run multi-container agentic AI applications with a single file, using the same workflow.

With these tools, you can develop and test agentic AI applications efficiently, using the same consistent workflow throughout.

Edit this page

https://github.com/docker/docs/edit/main/content/guides/agentic-ai.md

Request changes

https://github.com/docker/docs/issues/new?template=doc\_issue.yml&location=https%3a%2f%2fdocs.docker.com%2fguides%2fagentic-ai%2f&labels=status%2Ftriage

Table of contents

Introduction

https://docs.docker.com/guides/agentic-ai/#introduction

Prerequisites

https://docs.docker.com/guides/agentic-ai/#prerequisites

Step 1: Clone the sample application

https://docs.docker.com/guides/agentic-ai/#step-1-clone-the-sample-application

Step 2: Run the application locally

https://docs.docker.com/guides/agentic-ai/#step-2-run-the-application-locally

Step 3: Review the application environment

https://docs.docker.com/guides/agentic-ai/#step-3-review-the-application-environment

Step 4: Review the application

https://docs.docker.com/guides/agentic-ai/#step-4-review-the-application

https://docs.docker.com/guides/agentic-ai/#summary

https://www.linkedin.com/company/docker

https://x.com/docker/

https://www.facebook.com/docker.run

http://www.youtube.com/user/dockerrun

https://www.instagram.com/dockerinc/

Product offerings

https://www.docker.com/

https://www.docker.com/pricing?ref=Docs&refAction=DocsFooter

https://www.docker.com/company/

https://docs.docker.com/llms.txt

llms-full.txt

https://docs.docker.com/llms-full.txt

Cookies Settings |

Terms of Service

https://www.docker.com/legal/docker-terms-service

https://www.dockerstatus.com/

https://www.docker.com/legal

Copyright © 2013-2026 Docker Inc. All rights reserved.

Search this site Results will appear as you type Clear

Start typing to search the documentation

By clicking “Accept All Cookies”, you agree to the storing of cookies on your device to enhance site navigation, analyze site usage, and assist in our marketing efforts.

Cookies Settings Reject All Accept All Cookies

Privacy Preference Center

When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer.

More information

https://cookiepedia.co.uk/giving-consent-to-cookies

Manage Consent Preferences

Functional Cookies

Functional Cookies

These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.

Strictly Necessary Cookies

Always Active

These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.

Performance Cookies

Performance Cookies

These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance.

Targeting Cookies

Targeting Cookies

These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.

Cookie List

checkbox label label

Apply Cancel

Consent Leg.Interest

checkbox label label

checkbox label label

checkbox label label

Reject All Confirm My Choices

