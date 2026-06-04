---
sourceFile: "Lab: Migrating a Node App to Docker Hardened Images | Docker Docs"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.607Z"
---

# Lab: Migrating a Node App to Docker Hardened Images | Docker Docs

7b61dabd-be05-4133-ba93-43e29d2ce78f

Lab: Migrating a Node App to Docker Hardened Images | Docker Docs

daf2ab13-0ecd-4665-a6e4-55a47734c243

https://docs.docker.com/guides/lab-dhi-node/

Lab: Migrating a Node App to Docker Hardened Images | Docker Docs

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

Lab: Migrating a Node App to Docker Hardened Images

https://docs.docker.com/guides/lab-dhi-node/

Hands-on lab: Replace a Node.js base image with a Docker Hardened Image. Analyze CVEs with Docker Scout, rewrite the Dockerfile to use multi-stage builds with DHI, and explore SBOMs, VEX, and compliance attestations.

Labs Docker Hardened Images

Docker Hardened Images

https://docs.docker.com/dhi/

Docker Scout docs

https://docs.docker.com/scout/

Build attestations

https://docs.docker.com/build/metadata/attestations/

Labspace repository

https://github.com/dockersamples/labspace-dhi-node

« Back to all guides

https://docs.docker.com/guides/

https://docs.docker.com/

https://docs.docker.com/guides/

/ Lab: Migrating to DHI (Node)

Lab: Migrating a Node App to Docker Hardened Images

Ask Gordon Copy Markdown View Markdown

Table of contents

Launch the lab

https://docs.docker.com/guides/lab-dhi-node/#launch-the-lab

What you'll learn

https://docs.docker.com/guides/lab-dhi-node/#what-youll-learn

https://docs.docker.com/guides/lab-dhi-node/#modules

Migrate a Node.js application from a standard

node:24-trixie-slim

base image to a Docker Hardened Image. You'll measure the before-and-after impact on CVE count, image size, and policy compliance using Docker Scout, then explore the supply chain attestations DHI ships with every image.

Launch the lab

https://docs.docker.com/guides/lab-dhi-node/#launch-the-lab

#### Start the labspace:

$ docker compose -p labspace -f oci://dockersamples/labspace-dhi-node up -d

Open your browser to

http://localhost:3030

http://localhost:3030/

#### When you're done, tear down the labspace:

$ docker compose -p labspace down

What you'll learn

https://docs.docker.com/guides/lab-dhi-node/#what-youll-learn

#### By the end of this Labspace, you will have completed the following:

Analyze a Node.js container image with Docker Scout to identify CVE and policy failures

Rewrite a Dockerfile to use a multi-stage build with DHI dev and runtime variants

Compare image size and vulnerability counts before and after the migration

Inspect supply chain attestations included with Docker Hardened Images (SBOMs, SLSA, VEX)

Export VEX documents for integration with external scanners such as Grype or Trivy

https://docs.docker.com/guides/lab-dhi-node/#modules

Description

Introduction

Overview of Docker Hardened Images and their security benefits

Perform setup tasks required for the lab.

Analyzing the Starting Image

Build the app, scan it with Docker Scout, and review failing policies

Migrating to DHI

Rewrite the Dockerfile with multi-stage DHI build and compare results

DHI Attestations and Scanner Integration

Inspect SBOMs, FIPS attestations, STIG scans, and export VEX for external tools

Edit this page

https://github.com/docker/docs/edit/main/content/guides/lab-dhi-node.md

Request changes

https://github.com/docker/docs/issues/new?template=doc\_issue.yml&location=https%3a%2f%2fdocs.docker.com%2fguides%2flab-dhi-node%2f&labels=status%2Ftriage

Table of contents

Launch the lab

https://docs.docker.com/guides/lab-dhi-node/#launch-the-lab

What you'll learn

https://docs.docker.com/guides/lab-dhi-node/#what-youll-learn

https://docs.docker.com/guides/lab-dhi-node/#modules

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

