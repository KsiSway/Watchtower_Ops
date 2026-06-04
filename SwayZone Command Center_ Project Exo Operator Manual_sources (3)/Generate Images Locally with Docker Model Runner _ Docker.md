---
sourceFile: "Generate Images Locally with Docker Model Runner | Docker"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.427Z"
---

# Generate Images Locally with Docker Model Runner | Docker

f43b54bd-58d1-4123-8764-20487c8d9fb6

Generate Images Locally with Docker Model Runner | Docker

e5fd77c3-a98f-4a70-b99e-d42a0dc00768

https://www.docker.com/blog/blog-generate-images-locally-dmr-open-webui/

Generate Images Locally with Docker Model Runner | Docker

Skip to content

https://www.docker.com/blog/blog-generate-images-locally-dmr-open-webui/#main-content

Insights on the state of AI agents from 800+ builders and leaders. Download your copy

https://www.docker.com/resources/the-state-of-agentic-ai-white-paper/

https://www.docker.com/

https://www.docker.com/products/

AI and Agents

Docker Sandboxes New Isolated environments for coding agents

https://www.docker.com/products/docker-sandboxes/

AI Governance New Govern agents and Claws across every team

https://www.docker.com/products/ai-governance/

Docker Model Runner Local-first LLM inference made easy

https://www.docker.com/products/model-runner/

Docker MCP Catalog and Toolkit Connect and manage MCP tools

https://www.docker.com/products/mcp-catalog-and-toolkit/

Application Security

Docker Hardened Images Ship with secure, enterprise-ready images

https://www.docker.com/products/hardened-images/

Docker Scout Simplify the software supply chain

https://www.docker.com/products/docker-scout/

Application Development

Docker Desktop Containerize your applications

https://www.docker.com/products/docker-desktop/

Docker Hub Discover and share container images

https://www.docker.com/products/docker-hub/

Docker Offload Break free of local constraints

https://www.docker.com/products/docker-offload/

Docker Build Cloud Speed up your image builds

https://www.docker.com/products/build-cloud/

Testcontainers Desktop Local testing with real dependencies

https://testcontainers.com/desktop/

https://www.docker.com/support/

Documentation Find guides for Docker products

https://docs.docker.com/

Getting Started Learn the Docker basics

https://www.docker.com/get-started/

Resources Search a library of helpful materials

https://www.docker.com/resources/

Training Skill up your Docker knowledge

https://www.docker.com/resources/trainings/

Extensions SDK Create and share your own extensions

https://www.docker.com/developers/sdk/

Community Connect with other Docker developers

https://www.docker.com/community/

Open Source Explore open source projects

https://www.docker.com/community/open-source/

Preview Program Help shape the future of Docker

https://www.docker.com/community/get-involved/developer-preview/

Customer Stories Get inspired with customer stories

https://www.docker.com/customer-stories/

Get the latest Docker news

https://www.docker.com/newsletter-subscription/

https://www.docker.com/pricing/

https://www.docker.com/blog/blog-generate-images-locally-dmr-open-webui/

https://www.docker.com/blog/blog-generate-images-locally-dmr-open-webui/

Docker Personal

For individual developers who need the essential tools to build and deploy containers.

Get started

https://app.docker.com/signup

Get started

https://app.docker.com/signup

Docker Desktop

Docker Engine + Kubernetes

Docker Scout

Docker Debug

#### Included usage:

1 Docker Scout-enabled repo\*

100 Docker Hub pulls/hr\*

1 private Docker Hub repo

Docker Build Cloud and Testcontainers Cloud free trial

per user/month For individual professionals who require more advanced features and additional resources.

https://app.docker.com/billing/\_/subscribe/?cycle=monthly&quantity=1&tier=pro&ref=wwwPricing&refAction=wwwPricingProClicked

https://app.docker.com/billing/\_/subscribe/?cycle=annual&quantity=1&tier=pro&ref=wwwPricing&refAction=wwwPricingProClicked

Docker Build Cloud

Testcontainers Cloud

Synchronized File Shares

Visibility into Docker Scout health scores

5 business day support response

#### Included usage:

2 Docker Scout-enabled repos

Unlimited Docker Hub pull rate

200 Docker Build Cloud build minutes\*\*

100 Testcontainers Cloud runtime minutes\*\*

MOST POPULAR

Docker Team

per user/month For small teams that need collaborative tools to make working together more efficient.

https://app.docker.com/billing/\_/subscribe/?cycle=monthly&quantity=1&tier=team&ref=wwwPricing&refAction=wwwPricingTeamClicked

https://app.docker.com/billing/\_/subscribe/?cycle=annual&quantity=1&tier=team&ref=wwwPricing&refAction=wwwPricingTeamClicked

Add users in bulk

Docker Hub role-based access control

2 business day support response

#### Included usage:

Up to 100 users

Unlimited Docker Scout-enabled repos

Unlimited Docker Hub pull rate

Unlimited private Docker Hub repos

500 Docker Build Cloud build minutes\*\*

500 Testcontainers Cloud runtime minutes\*\*

10 Organization access tokens

1 Docker Hub organization

Docker Business

per user/month For enterprises desiring robust security, control, and compliance features.

https://app.docker.com/billing/\_/subscribe/?quantity=1&tier=business&ref=wwwPricing&refAction=wwwPricingBusinessClicked

https://app.docker.com/billing/\_/subscribe/?quantity=1&tier=business&ref=wwwPricing&refAction=wwwPricingBusinessClicked

Contact sales

https://www.docker.com/pricing/contact-sales/

Contact sales

https://www.docker.com/pricing/contact-sales/

Hardened Docker Desktop

Single Sign-On (SSO)

SCIM user provisioning

Image and Registry Access Management

Desktop Insights Dashboard

Enhanced container Isolation (ECI)

Purchase via invoice

1 business day support response

#### Included usage:

No user cap

Unlimited Docker Scout-enabled repos

Unlimited Docker Hub pull rate

Unlimited private Docker Hub repos

1,500 Docker Build Cloud build minutes\*\*

1,500 Testcontainers Cloud runtime minutes\*\*

100 Organization access tokens

Unlimited Docker Hub organizations\*\*\*

Docker Hardened Images (DHI)

Secure, minimal container images for every team, free with enterprise features, if needed.

Start Free Trial

https://www.docker.com/products/hardened-images#getstarted

https://www.docker.com/blog/

https://docs.docker.com/

https://app.docker.com/login

Get Started

https://www.docker.com/get-started/

Toggle menu

Generate Images Locally with Docker Model Runner and Open WebUI

Posted May 5, 2026

Ignasi Lopez Luna

https://www.docker.com/contributors/ignasi-lopez-luna/

We've all been there: you need to generate a few images for a project, you fire up an AI image service, and suddenly you're wondering what happens to your prompts, how many credits you have left, or why that “safe content” filter rejected your perfectly reasonable request for a dragon wearing a business suit. What if you could skip all of that and run the whole thing on your own machine, with a slick chat UI on top?

That's exactly what Docker Model Runner now makes possible. With a couple of commands you can pull an image-generation model, connect it to

https://github.com/open-webui/open-webui

, and start generating images right from a chat interface fully local, fully private, fully yours.

Let's build it.

Your own private DALL-E, no cloud subscription required.

What You'll Need

Docker Desktop

Docker Engine

~8 GB of free RAM

for a small model (more is better)

: optional but highly recommended, NVIDIA (CUDA), Apple Silicon (MPS), or CPU fallback

If you can run docker model version without errors, you're good to go.

How Docker Model Runner works with Open WebUI

#### Before we dive in, here's the big picture:

Docker Model Runner acts as the control plane. It downloads the model, manages the inference backend lifecycle, and exposes a

100% OpenAI-compatible API

— including the POST /v1/images/generations endpoint that Open WebUI already knows how to talk to.

Step 1: Pull an Image Generation Model

Docker Model Runner uses a compact packaging format called

(Diffusers Unified Format) to distribute image generation models through Docker Hub, just like any other OCI artifact.

#### Pull a model to get started:

docker model pull stable-diffusion

#### You can confirm it's ready:

docker model inspect stable-diffusion

"id": "sha256:5f60862074a4c585126288d08555e5ad9ef65044bf490ff3a64855fc84d06823",

"docker.io/ai/stable-diffusion:latest"

"created": 1768470632,

"config": {

"format": "diffusers",

"architecture": "diffusers",

"size": "6.94GB",

"diffusers": {

"dduf\_file": "stable-diffusion-xl-base-1.0-FP16.dduf",

"layout": "dduf"

What's happening under the hood?

The model is stored locally as a DDUF file, a single-file format that bundles all the components of a diffusion model (text encoder, VAE, UNet/DiT, scheduler config) into one portable artifact. Docker Model Runner knows how to unpack it at runtime.

Step 2: Launch Open WebUI

This is a magic trick. Docker Model Runner has a built-in launch command that knows exactly how to wire up Open WebUI against the local inference endpoint:

docker model launch openwebui

#### That's it. Behind the scenes this runs:

docker run --

-p 3000:8080 \

-e OPENAI\_API\_BASE=http:

//model-runner

.docker.internal

/engines/v1

-e OPENAI\_BASE\_URL=http:

//model-runner

.docker.internal

/engines/v1

-e OPENAI\_API\_KEY=sk-docker-model-runner \

/open-webui/open-webui

The model-runner.docker.internal hostname is a special DNS entry that Docker Desktop containers use to reach the Model Runner running on the host, no port-forwarding gymnastics required. If you use Docker CE, you'll see the docker/model-runner container address instead of model-runner.docker.internal.

Open your browser at

http://localhost:3000

http://localhost:3000/

, create a local account (it stays offline), and you'll land on the chat interface.

#### Want to run it in the background? Add –detach:

docker model launch openwebui --detach

#### Prefer Docker Compose? See the full setup here:

https://docs.docker.com/ai/model-runner/openwebui-integration/

https://docs.docker.com/ai/model-runner/openwebui-integration/

Step 3: Configure Open WebUI for Image Generation

Open WebUI already uses Docker Model Runner for text chat automatically (it reads the OPENAI\_API\_BASE env var). For image generation you need to point it at the images endpoint too, a 30-second job in the settings UI.

http://localhost:3000/admin/settings/images

http://localhost:3000/admin/settings/images

Image Generation

#### Fill in the fields:

Value stable-diffusion

API Base URL

Value http://model-runner.docker.internal/engines/diffusers/v1

Value whatever-you-want

Why the dummy API key?

Docker Model Runner doesn't require authentication, it's a local service. The key is only there because Open WebUI's form requires one. Any non-empty string works.

Step 4: Pull a Chat Model

Open WebUI is also a full-featured chat interface, and one of its best tricks is letting you

ask the LLM to generate an image

right from the conversation. For that to work, you need a language model too.

# Lightweight option — runs on almost any machine

docker model pull smollm2

# Recommended — more capable, better at understanding creative prompts

docker model pull gpt-oss

Both will show up automatically in the Open WebUI model selector. Use smollm2 if you're tight on RAM, or gpt-oss if you want richer, more creative responses before image generation.

No extra configuration needed

, Open WebUI picks up text models from the same OPENAI\_API\_BASE endpoint it was already configured with.

Step 5: Generate Your First Image

Head back to the main chat view. You'll notice a small \*\* image icon\*\* in the message input bar.

Click it to toggle image generation mode, type your prompt, and send.

#### Try something like:

Create an image of a whale.

The first request takes a little longer while the backend loads the model into memory. After that, subsequent images generate much faster.

Open WebUI will automatically route image-generation requests to the diffusers backend and text requests to the language model, seamlessly, in the same conversation.

Step 6: Generate Images Directly via the API

For developers who want to integrate image generation into their own apps, Docker Model Runner exposes the standard OpenAI Images API directly:

curl -s -X POST http:

//localhost

/engines/diffusers/v1/images/generations

"Content-Type: application/json"

"stable-diffusion"

"A cat sitting on a couch"

#### The response follows the OpenAI Images API format exactly:

"created": 1742990400,

"b64\_json": "/9j/4AAQSkZJRgABAQAAAQABAAD/2wBD..."

#### Decode and save the image:

curl -s -X POST http:

//localhost

/engines/diffusers/v1/images/generations

"Content-Type: application/json"

"stable-diffusion"

"A cat sitting on a couch"

' | jq -r '

.data\[0\].b64\_json' |

Advanced Parameters

The API supports all the parameters you'd expect from a full diffusers pipeline:

//localhost

/engines/diffusers/v1/images/generations

"Content-Type: application/json"

"stable-diffusion"

"A serene Japanese zen garden, cherry blossoms, koi pond, photorealistic"

"negative\_prompt"

"blurry, low quality, distorted, watermark"

"num\_inference\_steps"

"guidance\_scale"

"response\_format"

.data\[0\].b64\_json' |

-d > garden.png

What it does

Parameter prompt

What it does What you want in the image

Parameter negative\_prompt

What it does What you want to

Parameter size

What it does Resolution as WIDTHxHEIGHT (e.g., 512×512, 768×512)

Parameter n

What it does Number of images to generate (1–10)

Parameter num\_inference\_steps

What it does More steps = higher quality, slower (default: 50)

Parameter guidance\_scale

What it does How closely to follow the prompt (1–20, default: 7.5)

Parameter seed

What it does Integer for reproducible results; omit for random

Set a seed while you're iterating on a prompt. Once you're happy with the composition, remove it to get unique variations.

Under the Hood: How the Diffusers Backend Works

#### When you first request an image, Docker Model Runner:

Unpacks the DDUF file

: extracts the model components and loads them via DiffusionPipeline.from\_pretrained()

#### Starts a FastAPI server:

this is the server that Open WebUI and your curl commands talk to through Docker Model Runner

The server is installed on first use by downloading a self-contained Python environment from Docker Hub (version-pinned, so updates are explicit). It lives at ~/.docker/model-runner/diffusers/ — no Python version conflicts, no virtualenv setup.

Troubleshooting

The model takes forever to load on first use.

That's normal, the model weights are being loaded from disk and transferred to GPU memory. Subsequent requests in the same session are much faster because the backend stays warm.

I get a “No model loaded” 503 error

Make sure the model is fully downloaded (docker model list) and that you're sending the correct model name in the model field.

Image quality is poor / generations are too fast

Increase num\_inference\_steps (try 20–50 steps). Higher values = slower but sharper results.

Open WebUI can't connect to the image endpoint

Double-check the URL in Admin Panel → Settings → Images. Inside a Docker container it must be http://model-runner.docker.internal/engines/diffusers/v1, not localhost.

Conclusion and What's Next

Docker Model Runner makes local image generation simple. It packages and serves image models through an OpenAI-compatible API, while Open WebUI provides an easy chat interface on top. Together, they let you generate images privately on your own machine, either through the browser or directly through the API, without relying on a cloud service.

#### This feature opens up a lot of possibilities:

Multimodal workflows

: Chat with a text model about an idea, then immediately generate an image of it — in the same Open WebUI conversation

RAG + image generation

: Build a pipeline that generates illustrations for your documents

Custom models

: The diffusers backend supports any DDUF-packaged model, so you can package your own fine-tuned models using Docker's model packaging tools

The Docker Model Runner team is actively expanding model support on Docker Hub. Check docker model search for the latest available models.

https://www.docker.com/blog/tag/artificial-intelligence-machine-learning/

Docker Model Runner

https://www.docker.com/blog/tag/docker-model-runner/

https://www.docker.com/blog/category/products/

Table of contents

What You'll Need

https://www.docker.com/blog/blog-generate-images-locally-dmr-open-webui/#what-you-ll-need

How Docker Model Runner works with Open WebUI

https://www.docker.com/blog/blog-generate-images-locally-dmr-open-webui/#how-docker-model-runner-works-with-open-webui

Step 1: Pull an Image Generation Model

https://www.docker.com/blog/blog-generate-images-locally-dmr-open-webui/#step-1-pull-an-image-generation-model

Step 2: Launch Open WebUI

https://www.docker.com/blog/blog-generate-images-locally-dmr-open-webui/#step-2-launch-open-webui

Step 3: Configure Open WebUI for Image Generation

https://www.docker.com/blog/blog-generate-images-locally-dmr-open-webui/#step-3-configure-open-webui-for-image-generation

Step 4: Pull a Chat Model

https://www.docker.com/blog/blog-generate-images-locally-dmr-open-webui/#step-4-pull-a-chat-model

Step 5: Generate Your First Image

https://www.docker.com/blog/blog-generate-images-locally-dmr-open-webui/#step-5-generate-your-first-image

Step 6: Generate Images Directly via the API

https://www.docker.com/blog/blog-generate-images-locally-dmr-open-webui/#step-6-generate-images-directly-via-the-api

Under the Hood: How the Diffusers Backend Works

https://www.docker.com/blog/blog-generate-images-locally-dmr-open-webui/#under-the-hood-how-the-diffusers-backend-works

Troubleshooting

https://www.docker.com/blog/blog-generate-images-locally-dmr-open-webui/#troubleshooting

Conclusion and What's Next

https://www.docker.com/blog/blog-generate-images-locally-dmr-open-webui/#conclusion-and-what-s-next

https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fwww.docker.com%2Fblog%2Fblog-generate-images-locally-dmr-open-webui%2F

https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.docker.com%2Fblog%2Fblog-generate-images-locally-dmr-open-webui%2F

https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.docker.com%2Fblog%2Fblog-generate-images-locally-dmr-open-webui%2F

Related Posts

\[May 12, 2026

Docker AI Governance: Unlock Agent Autonomy, Safely

Introducing Docker AI Governance: centralized control over how agents execute, what they can reach on the network, which credentials they can use, and which MCP tools they can call, so every developer in your company can run AI agents safely, wherever they work. Your laptop is the new prod Agents are the biggest productivity unlock…

Srini Sekaran Read now\](https://www.docker.com/blog/docker-ai-governance-unlock-agent-autonomy-safely/)

\[Docker Captain May 7, 2026

Comparing Different Approaches to Sandboxing

Docker Captain Siri Varma Vegiraju compares sandboxing methods for AI agents, from containers to microVMs. Learn how Docker Sandbox improves isolation, security, and performance.

Siri Varma Vegiraju Read now\](https://www.docker.com/blog/comparing-sandboxing-approaches-ai-agents/)

\[Scanner Integrations May 5, 2026

Precision Container Security with Docker and Black Duck

The complexity of modern containerized applications often leaves developers drowning in a sea of “noise”—vulnerabilities that exist in the file system but pose zero actual risk to the application. The integration between Black Duck and Docker Hardened Images (DHI) provides a definitive answer to this challenge. By combining Docker's secure-by-default foundations, using VEX (Vulnerability Exploitability…

Jessy McDermott and Dan Stelzer Read now\](https://www.docker.com/blog/precision-container-security-with-docker-and-black-duck/)

Products Overview

https://www.docker.com/products/

Docker Desktop

https://www.docker.com/products/docker-desktop/

https://www.docker.com/products/docker-hub/

Docker Scout

https://www.docker.com/products/docker-scout/

Docker Build Cloud

https://www.docker.com/products/build-cloud/

Testcontainers Desktop

https://testcontainers.com/desktop/

Testcontainers Cloud

https://testcontainers.com/cloud/

Docker MCP Catalog and Toolkit

https://www.docker.com/products/mcp-catalog-and-toolkit/

Docker Hardened Images

https://www.docker.com/products/hardened-images/

Command Line Interface

https://www.docker.com/products/cli/

IDE Extensions

https://www.docker.com/products/ide/

Container Runtime

https://www.docker.com/products/container-runtime/

Docker Extensions

https://www.docker.com/products/extensions/

Trusted Open Source Content

https://www.docker.com/products/trusted-content/open-source/

Secure Software Supply Chain

https://www.docker.com/solutions/security/

Documentation

https://docs.docker.com/

Getting Started

https://www.docker.com/get-started/

https://www.docker.com/resources/trainings

Extensions SDK

https://www.docker.com/developers/sdk/

https://www.docker.com/community/

Open Source

https://www.docker.com/community/open-source/

Preview Program

https://www.docker.com/community/get-involved/developer-preview/

https://www.docker.com/newsletter-subscription/

https://www.docker.com/products/personal/

https://www.docker.com/products/pro/

https://www.docker.com/products/team/

https://www.docker.com/products/business/

Premium Support and TAM

https://www.docker.com/pricing/premium-support-tam/

Pricing FAQ

https://www.docker.com/pricing/faq/

Contact Sales

https://www.docker.com/pricing/contact-sales/

https://www.docker.com/company/

What is a Container

https://www.docker.com/resources/what-container/

https://www.docker.com/blog/

https://www.docker.com/why-docker/

https://www.docker.com/trust/

Customer Success

https://www.docker.com/customer-success/

https://www.docker.com/partners/

https://www.docker.com/events/

Docker System Status

http://dockerstatus.com/

https://www.docker.com/company/newsroom/

https://stores.kotisdesign.com/docker

Brand Guidelines

https://www.docker.com/company/newsroom/media-resources/

Trademark Guidelines

https://www.docker.com/legal/trademark-guidelines/

https://www.docker.com/careers/

https://www.docker.com/company/contact/

https://www.docker.com/

https://www.docker.com/ja-jp/

© 2026 Docker Inc. All rights reserved

Terms of Service

https://www.docker.com/legal/docker-terms-service

https://www.docker.com/legal/privacy

https://www.docker.com/legal/

Cookies Settings

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

