---
sourceFile: "Docker Desktop 4.40 Release | Docker"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.292Z"
---

# Docker Desktop 4.40 Release | Docker

a1b82e8c-0319-4cd8-a1b6-019a3ad0fb09

Docker Desktop 4.40 Release | Docker

3cccb839-0e02-40ac-abe0-226c8a46048d

https://www.docker.com/blog/docker-desktop-4-40/

Docker Desktop 4.40 Release | Docker

Skip to content

https://www.docker.com/blog/docker-desktop-4-40/#main-content

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

https://www.docker.com/blog/docker-desktop-4-40/

https://www.docker.com/blog/docker-desktop-4-40/

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

Docker Desktop 4.40: Model Runner to run LLMs locally, more powerful Docker AI Agent, and expanded AI Tools Catalog

Posted Apr 1, 2025

https://www.docker.com/contributors/yiwen-xu/

At Docker, we're focused on making life easier for developers and teams building high-quality applications, including those powered by generative AI. That's why, in the

Docker Desktop 4.40

https://docs.docker.com/desktop/release-notes/#4400

release, we're introducing new tools that simplify GenAI app development and support secure, scalable development.

Keep reading to find updates on new tooling like Model Runner and a more powerful Docker AI Agent with MCP capabilities. Plus, with the AI Tool Catalog, teams can now easily build smarter AI-powered applications and agents with MCPs. And with Docker Desktop Setting Reporting, admins now get greater visibility into compliance and policy enforcement.

Docker Model Runner (Beta): Bringing local AI model execution to developers

Now in beta with Docker Desktop 4.40, Docker Model Runner makes it easier for developers to run AI models locally. No extra setup, no jumping between tools, and no need to wrangle infrastructure. This first iteration is all about helping developers quickly experiment and iterate on models right from their local machines.

#### The beta includes three core capabilities:

Local model execution

, right out of the box

GPU acceleration

on Apple Silicon for faster performance

Standardized model packaging

using OCI Artifacts

and accessible via the OpenAI API, the built-in inference engine makes running models feel as simple as running a container. On Mac, Model Runner uses host-based execution to tap directly into your hardware — speeding things up with zero extra effort.

Models are also packaged as OCI Artifacts, so you can version, store, and ship them using the same trusted registries and CI/CD workflows you already use. Check out our

https://docs.docker.com/desktop/features/model-runner/

for more detailed info!

Figure 1: Using Docker Model Runner and CLI commands to experiment with models locally

This release lays the groundwork for what's ahead: support for additional platforms like Windows with GPU, the ability to customize and publish your own models, and deeper integration into the development loop. We're just getting started with Docker Model Runner and look forward to sharing even more updates and enhancements in the coming weeks.

Docker AI Agent: Smarter and more powerful with MCP integration + AI Tool Catalog

Our vision for the Docker AI Agent is simple: be context-aware, deeply knowledgeable, and available wherever developers build. With this release, we're one step closer! The Docker AI Agent is now even more capable, making it easier for developers to tap into the Docker ecosystem and streamline their workflows beyond Docker.

Your trusted AI Agent for all things Docker

The Docker AI agent now has built-in support for many new popular developer capabilities like:

Running shell commands

Performing Git operations

Downloading resources

Managing local files

Thanks to a Docker Scout integration, we also now support other tools from the Docker ecosystem, such as performing security analysis on your Dockerfiles or images.

Expanding the Docker AI Agent beyond Docker

The Docker AI Agent now fully embraces the Model Context Protocol (MCP). This new standard for connecting AI agents and models to external data and tools makes them more powerful and tailored to specific needs. In addition to acting as an MCP client, many of Docker AI Agent's capabilities are now exposed as MCP Servers. This means you can interact with the agent in Docker Desktop GUI or CLI or your favorite client, such as Claude Desktop and Cursor.

Figure 2: Extending Docker AI Agent's capabilities with many tools, including the MCP Catalog.

AI Tool Catalog: Your launchpad for experimenting with MCP servers

Thanks to the AI Tool Catalog extension in Docker Desktop, you can explore different MCP servers and seamlessly connect the Docker AI agent to other tools or other LLMs to the Docker ecosystem. No more manually configuring multiple MCP servers! We've also added secure handling and injection of MPC servers' secrets, such as API keys, to simplify log-ins and credential management.

The AI Tool Catalog includes containerized servers that have been pushed to Docker Hub, and we'll continue to expand them. If you're working in this space or have an MCP server that you'd like to distribute, please reach out

in our public GitHub repo

https://github.com/docker/labs-ai-tools-for-devs

. To install the AI Tool Catalog, go to the extensions menu of Docker Desktop or use

https://open.docker.com/extensions/marketplace?extensionId=docker/labs-ai-tools-for-devs

for installation.

Figure 3: Explore and discover MCP servers in the AI Tools Catalog extension in Docker Desktop

Bring compliance into focus with Docker Desktop Setting Reporting

Building on the Desktop Settings Management capabilities introduced in

Docker Desktop 4.36

https://www.docker.com/blog/docker-desktop-4-36/

, Docker Desktop 4.40 brings robust compliance reporting for

Docker Business

https://www.docker.com/products/business/

customers. This new powerful feature gives administrators comprehensive visibility into user compliance with assigned settings policies across the organization.

Key benefits

Real-time compliance tracking

: Easily monitor which users are compliant with their assigned settings policies. This allows administrators to quickly identify and address non-compliant systems and users.

Streamlined troubleshooting

: Detailed compliance status information helps administrators diagnose why certain users might be non-compliant, reducing resolution time and IT overhead.

Figure 4: Desktop settings reporting provides an overview of policy assignment and compliance status, helping organizations stay compliant.

Get started with Docker Desktop Setting Reporting

The Desktop Setting Reporting dashboard is currently being rolled out through Early Access. Administrators can see which settings policies are assigned to each user and whether those policies are being correctly applied.

Soon, administrators will be able to access the reporting dashboard by navigating to the Admin Console > Docker Desktop > Reporting. The dashboard provides a clear view of all users' compliance status, with options to:

Search by username or email address

Filter by assigned policies

Toggle visibility of compliant users to focus on potential issues

View detailed compliance information for specific users

Download comprehensive compliance data as a CSV file

The dashboard also provides targeted resolution steps for non-compliant users to help administrators quickly address issues and ensure organizational compliance.

This new reporting capability underscores Docker's commitment to providing enterprise-grade management tools that simplify administration while maintaining security and compliance across diverse development environments. Learn more about Desktop settings reporting

https://docs.docker.com/security/for-admins/hardened-desktop/settings-management/compliance-reporting/

Wrapping up

Docker is expanding its AI tooling to simplify application development and improve team workflows. New additions like Model Runner, the Docker AI Agent with MCP server and client support, and the AI Tool Catalog extension in Docker Desktop help streamline how developers build with AI. We continue to make enterprise tools more useful and robust, giving admins better visibility into compliance and policy enforcement through Docker Desktop Settings Reporting. We can't wait to see what you build next!

Authenticate and update

https://www.docker.com/pricing/

today to receive your subscription level's newest Docker Desktop features.

Subscribe to the

Docker Navigator Newsletter

https://www.docker.com/newsletter-subscription/

Learn about our

sign-in enforcement options

https://docs.docker.com/security/for-admins/enforce-sign-in/methods/

New to Docker?

Create an account

https://hub.docker.com/signup?\_gl=1\*452i3u\*\_ga\*MjEzNzc3Njk5MC4xNjgzNjY3NDkw\*\_ga\_XJWPQMJYHQ\*MTcwODcxNjA4Ni4zNjguMS4xNzA4NzE2MzE2LjUzLjAuMA..

Have questions? The

Docker community is here to help

https://www.docker.com/community/

https://www.docker.com/blog/tag/artificial-intelligence-machine-learning/

Docker Business

https://www.docker.com/blog/tag/docker-business/

Docker Desktop

https://www.docker.com/blog/tag/docker-desktop/

Docker Desktop release

https://www.docker.com/blog/tag/docker-desktop-release/

https://www.docker.com/blog/category/products/

Table of contents

Docker Model Runner (Beta): Bringing local AI model execution to developers

https://www.docker.com/blog/docker-desktop-4-40/#docker-model-runner-beta-bringing-local-ai-model-execution-to-developers

Docker AI Agent: Smarter and more powerful with MCP integration + AI Tool Catalog

https://www.docker.com/blog/docker-desktop-4-40/#docker-ai-agent-smarter-and-more-powerful-with-mcp-integration-ai-tool-catalog

Bring compliance into focus with Docker Desktop Setting Reporting

https://www.docker.com/blog/docker-desktop-4-40/#bring-compliance-into-focus-with-docker-desktop-setting-reporting

Wrapping up

https://www.docker.com/blog/docker-desktop-4-40/#wrapping-up

https://www.docker.com/blog/docker-desktop-4-40/#learn-more

https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fwww.docker.com%2Fblog%2Fdocker-desktop-4-40%2F

https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.docker.com%2Fblog%2Fdocker-desktop-4-40%2F

https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.docker.com%2Fblog%2Fdocker-desktop-4-40%2F

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

