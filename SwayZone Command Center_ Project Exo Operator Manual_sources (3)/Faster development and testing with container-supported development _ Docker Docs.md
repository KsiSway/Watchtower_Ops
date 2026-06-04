---
sourceFile: "Faster development and testing with container-supported development | Docker Docs"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.414Z"
---

# Faster development and testing with container-supported development | Docker Docs

48f9553d-6891-41be-929b-4676f03d833e

Faster development and testing with container-supported development | Docker Docs

e2fab67f-c636-4adb-8c66-2c5994e2a7f0

https://docs.docker.com/guides/container-supported-development/

Faster development and testing with container-supported development | Docker Docs

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

Faster development and testing with container-supported development

https://docs.docker.com/guides/container-supported-development/

Containers don't have to be just for your app. Learn how to run your app's dependent services and other debugging tools to enhance your development environment.

App development

« Back to all guides

https://docs.docker.com/guides/

https://docs.docker.com/

https://docs.docker.com/guides/

/ Container-supported development

Faster development and testing with container-supported development

Ask Gordon Copy Markdown View Markdown

Table of contents

What you'll learn

https://docs.docker.com/guides/container-supported-development/#what-youll-learn

Who's this for?

https://docs.docker.com/guides/container-supported-development/#whos-this-for

Tools integration

https://docs.docker.com/guides/container-supported-development/#tools-integration

https://docs.docker.com/guides/container-supported-development/#modules

What is container-supported development?

https://docs.docker.com/guides/container-supported-development/#what-is-container-supported-development

Demo: running databases locally

https://docs.docker.com/guides/container-supported-development/#demo-running-databases-locally

Demo: mocking API endpoints

https://docs.docker.com/guides/container-supported-development/#demo-mocking-api-endpoints

Demo: developing the cloud locally

https://docs.docker.com/guides/container-supported-development/#demo-developing-the-cloud-locally

Demo: adding additional debug and troubleshooting tools

https://docs.docker.com/guides/container-supported-development/#demo-adding-additional-debug-and-troubleshooting-tools

Containers offer a consistent way to build, share, and run applications across different environments. While containers are typically used to containerize your application, they also make it incredibly easy to run essential services needed for development. Instead of installing or connecting to a remote database, you can easily launch your own database. But the possibilities don't stop there.

With container-supported development, you use containers to enhance your development environment by emulating or running your own instances of the services your app needs. This provides faster feedback loops, less coupling with remote services, and a greater ability to test error states.

And best of all, you can have these benefits regardless of whether the main app under development is running in containers.

What you'll learn

https://docs.docker.com/guides/container-supported-development/#what-youll-learn

The meaning of container-supported development

How to connect non-containerized applications to containerized services

Several examples of using containers to emulate or run local instances of services

How to use containers to add additional troubleshooting and debugging tools to your development environment

Who's this for?

https://docs.docker.com/guides/container-supported-development/#whos-this-for

Teams that want to reduce the coupling they have on shared or deployed infrastructure or remote API endpoints

Teams that want to reduce the complexity and costs associated with using cloud services directly during development

Developers that want to make it easier to visualize what's going on in their databases, queues, etc.

Teams that want to reduce the complexity of setting up their development environment without impacting the development of the app itself

Tools integration

https://docs.docker.com/guides/container-supported-development/#tools-integration

Works well with Docker Compose and Testcontainers.

https://docs.docker.com/guides/container-supported-development/#modules

What is container-supported development?

https://docs.docker.com/guides/container-supported-development/#what-is-container-supported-development

Container-supported development is the idea of using containers to enhance your development environment by running local instances or emulators of the services your application relies on. Once you're using containers, it's easy to add additional services to visualize or troubleshoot what's going on in your services.

Tap to unmute

Your browser can't play this video.

https://www.youtube.com/supported\_browsers

https://www.youtube.com/

An error occurred.

Try watching this video on www.youtube.com

https://www.youtube.com/watch?v=pNcrto\_wGi0

, or enable JavaScript if it is disabled in your browser.

Demo: running databases locally

https://docs.docker.com/guides/container-supported-development/#demo-running-databases-locally

With container-supported development, it's easy to run databases locally. In this demo, you'll see how to do so, as well as how to connect a non-containerized application to the database.

Learn more about running databases in containers in the

Use containerized databases

https://docs.docker.com/guides/databases/

Demo: mocking API endpoints

https://docs.docker.com/guides/container-supported-development/#demo-mocking-api-endpoints

Many APIs require data from other data endpoints. In development, this adds complexities such as the sharing of credentials, uptime/availability, and rate limiting. Instead of relying on those services directly, your application can interact with a mock API server.

This demo will demonstrate how using WireMock can make it easy to develop and test an application, including the APIs various error states.

Learn more about using WireMock to mock API in the

Mocking API services with WireMock

https://docs.docker.com/guides/wiremock/

Demo: developing the cloud locally

https://docs.docker.com/guides/container-supported-development/#demo-developing-the-cloud-locally

When developing apps, it's often easier to outsource aspects of the application to cloud services, such as Amazon S3. However, connecting to those services in local development introduces IAM policies, networking constraints, and provisioning complications. While these requirements are important in a production setting, they complicate development environments significantly.

With container-supported development, you can run local instances of these services during development and testing, removing the need for complex setups. In this demo, you'll see how LocalStack makes it easy to develop and test applications entirely from the developer's workstation.

Learn more about using LocalStack in the

Develop and test AWS Cloud applications using LocalStack

https://docs.docker.com/guides/localstack/

Demo: adding additional debug and troubleshooting tools

https://docs.docker.com/guides/container-supported-development/#demo-adding-additional-debug-and-troubleshooting-tools

Once you start using containers in your development environment, it becomes much easier to add additional containers to visualize the contents of the databases or message queues, seed document stores, or event publishers. In this demo, you'll see a few of these examples, as well as how you can connect multiple containers together to make testing even easier.

Edit this page

https://github.com/docker/docs/edit/main/content/guides/container-supported-development.md

Request changes

https://github.com/docker/docs/issues/new?template=doc\_issue.yml&location=https%3a%2f%2fdocs.docker.com%2fguides%2fcontainer-supported-development%2f&labels=status%2Ftriage

Table of contents

What you'll learn

https://docs.docker.com/guides/container-supported-development/#what-youll-learn

Who's this for?

https://docs.docker.com/guides/container-supported-development/#whos-this-for

Tools integration

https://docs.docker.com/guides/container-supported-development/#tools-integration

https://docs.docker.com/guides/container-supported-development/#modules

What is container-supported development?

https://docs.docker.com/guides/container-supported-development/#what-is-container-supported-development

Demo: running databases locally

https://docs.docker.com/guides/container-supported-development/#demo-running-databases-locally

Demo: mocking API endpoints

https://docs.docker.com/guides/container-supported-development/#demo-mocking-api-endpoints

Demo: developing the cloud locally

https://docs.docker.com/guides/container-supported-development/#demo-developing-the-cloud-locally

Demo: adding additional debug and troubleshooting tools

https://docs.docker.com/guides/container-supported-development/#demo-adding-additional-debug-and-troubleshooting-tools

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

