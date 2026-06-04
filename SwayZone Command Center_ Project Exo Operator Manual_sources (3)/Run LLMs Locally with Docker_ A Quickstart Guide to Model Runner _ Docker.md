---
sourceFile: "Run LLMs Locally with Docker: A Quickstart Guide to Model Runner | Docker"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.690Z"
---

# Run LLMs Locally with Docker: A Quickstart Guide to Model Runner | Docker

542a1568-ef1f-4d13-a325-af370736706f

Run LLMs Locally with Docker: A Quickstart Guide to Model Runner | Docker

a81b8d3c-7740-496b-af8a-b6c32c6308a8

https://www.docker.com/blog/run-llms-locally/

Run LLMs Locally with Docker: A Quickstart Guide to Model Runner | Docker

Skip to content

https://www.docker.com/blog/run-llms-locally/#main-content

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

https://www.docker.com/blog/run-llms-locally/

https://www.docker.com/blog/run-llms-locally/

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

Run LLMs Locally with Docker: A Quickstart Guide to Model Runner

Posted Apr 4, 2025

Kevin Wittek

https://www.docker.com/contributors/kevin-wittek/

AI is quickly becoming a core part of modern applications, but running large language models (LLMs) locally can still be a pain. Between picking the right model, navigating hardware quirks, and optimizing for performance, it's easy to get stuck before you even start building. At the same time, more and more developers want the flexibility to run LLMs locally for development, testing, or even offline use cases. That's where

Docker Model Runner

https://docs.docker.com/desktop/features/model-runner/

Now available in Beta with

Docker Desktop 4.40

https://www.docker.com/blog/docker-desktop-4-40/

for macOS on Apple silicon, Model Runner makes it easy to pull, run, and experiment with LLMs on your local machine. No infrastructure headaches, no complicated setup. Here's what Model Runner offers in our initial beta release.

Local LLM inference powered by an integrated engine built on top of

https://github.com/ggml-org/llama.cpp

, exposed through an OpenAI-compatible API.

GPU acceleration on Apple silicon by executing the inference engine directly as a host process.

A growing collection of popular, usage-ready models packaged as standard OCI artifacts, making them easy to distribute and reuse across existing Container Registry infrastructure.

Keep reading to learn how to run an LLM locally on your own computer using Docker Model Runner!

Tap to unmute

Your browser can't play this video.

https://www.youtube.com/supported\_browsers

https://www.youtube.com/

An error occurred.

Try watching this video on www.youtube.com

https://www.youtube.com/watch?v=rGGZJT3ZCvo

, or enable JavaScript if it is disabled in your browser.

Enabling Docker Model Runner for LLMs

Docker Model Runner is enabled by default and shipped as part of Docker Desktop 4.40 for macOS on Apple silicon hardware. However, in case you've disabled it, you can easily enable it through the CLI with a single command:

docker desktop

model-runner

In its default configuration, the Model Runner will only be accessible through the Docker socket on the host, or to containers via the special

model-runner.docker.internal

endpoint. If you want to interact with it via TCP from a host process (maybe because you want to point some OpenAI SDK within your codebase straight to it), you can also enable it via CLI by specifying the intended port:

docker desktop

model-runner --tcp 12434

A first look at the command line interfaceCLI

The Docker Model Runner CLI will feel very similar to working with containers, but there are also some caveats regarding the execution model, so let's check it out. For this guide, I'm going to use a very small model to ensure it runs on hardware with limited resources and provides a fast and responsive user experience. To be more specific, we'll use the

SmolLM model

https://huggingface.co/blog/smollm

, published by HuggingFace in 2024.

We'll want to start by pulling a model. As with Docker Images, you can omit the specific tag, and it'll default to latest. But for this example, let's be specific:

docker model pull ai

:360M-Q4\_K\_M

Here I am pulling the SmolLM2 model with 360M parameters and 4-bit quantization. Tags for models distributed by Docker follow this scheme with regard to model metadata:

{model}:{parameters}-{quantization}

#### After having the model pulled, let's give it a spin by asking it a question:

docker model run ai

:360M-Q4\_K\_M

"Give me a fact about whales."

Whales are magnificent marine animals that have fascinated humans

centuries. They belong to the order Cetacea and have a unique body structure that allows them to swim and move around the ocean. Some species of whales, like the blue whale, can grow up to 100 feet (30 meters) long and weigh over 150 tons (140 metric tons) each. They are known

their powerful tails that propel them through the water, allowing them to dive deep to

food or escape predators.

Is this whale fact actually true? Honestly, I have no clue; I'm not a marine biologist. But it's a fun example to illustrate a broader point: LLMs can sometimes generate inaccurate or unpredictable information. As with anything, especially smaller local models with a limited number of parameters or small quantization values, it's important to verify what you're getting back.

happened when we ran the

docker model run

command? It makes sense to have a closer look at the technical underpinnings, since it differs from what you might expect after using

docker container run

commands for years. In the case of the Model Runner, this command won't spin up any kind of container. Instead, it'll call an Inference Server API endpoint, hosted by the Model Runner through Docker Desktop, and provide an OpenAI compatible API. The Inference Server will use

https://github.com/ggml-org/llama.cpp

as the Inference Engine, running as a native host process, load the requested model on demand, and then perform the inference on the received request. Then, the model will stay in memory until another model is requested, or until a pre-defined inactivity timeout (currently 5 minutes) is reached.

That also means that there isn't a need to perform a

docker model run

before interacting with a specific model from a host process or from within a container. Model Runner will transparently load the requested model on-demand, assuming it has been pulled beforehand and is locally available.

Speaking of interacting with models from other processes, let's have a look at how to integrate with Model Runner from within your application code.

Having fun with GenAI development

Model Runner exposes an OpenAI endpoint under

http://model-runner.docker.internal/engines/v1

http://model-runner.docker.internal/engines/v1

for containers, and under

http://localhost:12434/engines/v1

http://localhost:12434/engines/v1

for host processes (assuming you have enabled TCP host access on default port 12434). You can use this endpoint to hook up any OpenAI-compatible clients or frameworks.

In this example, I'm using Java and

LangChain4j

https://docs.langchain4j.dev/

. Since I develop and run my Java application directly on the host, all I have to do is configure the Model Runner OpenAI endpoint as the

and specify the model to use, following the Docker Model addressing scheme we've already seen in the CLI usage examples.

And that's all there is to it, pretty straightforward, right?

Please note that the model has to be already locally present for this code to work.

OpenAiChatModel model = OpenAiChatModel.builder()

" \[http://localhost:12434/engines/v1\](http://localhost:12434/engines/v1)"

.modelName(

"ai/smollm2:360M-Q4\_K\_M"

String answer = model.chat(

"Give me a fact about whales."

System.out.println(answer);

Finding more models

Now, you probably don't just want to use SmolLM models, so you might wonder what other models are currently available to use with Model Runner. The easiest way to get started is by checking out the ai/ namespace on

https://hub.docker.com/u/ai

On Docker Hub, you can find a curated list of the most popular models that are well-suited for local use cases. They're offered in different flavors to suit different hardware and performance needs. You can also find more details about each in the model card, available on the overview page of the model repository.

What's next?

Of course, this was just a first look at what Docker Model Runner can do. We have many more features in the works and can't wait to see what you build with it. For hands-on guidance, check out our latest

YouTube tutorial

https://www.youtube.com/watch?v=rGGZJT3ZCvo

on running LLMs locally with Model Runner. And be sure to keep an eye on the blog, we'll be sharing more updates, tips, and deep dives as we continue to expand Model Runner's capabilities.

Learn more on

Docker Docs

https://docs.docker.com/desktop/features/model-runner/

Discover how to

publish AI models

https://www.docker.com/blog/publish-ai-models-on-docker-hub/

to Docker Hub.

Subscribe to the

Docker Navigator Newsletter

https://www.docker.com/newsletter-subscription/

New to Docker?

Create an account

https://hub.docker.com/signup?\_gl=1\*452i3u\*\_ga\*MjEzNzc3Njk5MC4xNjgzNjY3NDkw\*\_ga\_XJWPQMJYHQ\*MTcwODcxNjA4Ni4zNjguMS4xNzA4NzE2MzE2LjUzLjAuMA..

Have questions? The

Docker community is here to help

https://www.docker.com/community/

https://www.docker.com/blog/category/products/

Table of contents

Enabling Docker Model Runner for LLMs

https://www.docker.com/blog/run-llms-locally/#enabling-docker-model-runner-for-llms

A first look at the command line interfaceCLI

https://www.docker.com/blog/run-llms-locally/#a-first-look-at-the-command-line-interfacecli

Having fun with GenAI development

https://www.docker.com/blog/run-llms-locally/#having-fun-with-genai-development

Finding more models

https://www.docker.com/blog/run-llms-locally/#finding-more-models

What's next?

https://www.docker.com/blog/run-llms-locally/#what-s-next

https://www.docker.com/blog/run-llms-locally/#resources

https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fwww.docker.com%2Fblog%2Frun-llms-locally%2F

https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.docker.com%2Fblog%2Frun-llms-locally%2F

https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.docker.com%2Fblog%2Frun-llms-locally%2F

Related Posts

\[May 12, 2026

Docker AI Governance: Unlock Agent Autonomy, Safely

Introducing Docker AI Governance: centralized control over how agents execute, what they can reach on the network, which credentials they can use, and which MCP tools they can call, so every developer in your company can run AI agents safely, wherever they work. Your laptop is the new prod Agents are the biggest productivity unlock…

Srini Sekaran Read now\](https://www.docker.com/blog/docker-ai-governance-unlock-agent-autonomy-safely/)

\[Docker Captain May 7, 2026

Comparing Different Approaches to Sandboxing

Docker Captain Siri Varma Vegiraju compares sandboxing methods for AI agents, from containers to microVMs. Learn how Docker Sandbox improves isolation, security, and performance.

Siri Varma Vegiraju Read now\](https://www.docker.com/blog/comparing-sandboxing-approaches-ai-agents/)

\[May 5, 2026

Generate Images Locally with Docker Model Runner and Open WebUI

Learn how to generate images locally with Docker Model Runner and Open WebUI using a private, OpenAI-compatible workflow on your own machine.

Ignasi Lopez Luna Read now\](https://www.docker.com/blog/blog-generate-images-locally-dmr-open-webui/)

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

