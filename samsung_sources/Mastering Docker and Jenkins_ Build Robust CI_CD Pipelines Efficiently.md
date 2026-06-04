---
sourceFile: "Mastering Docker and Jenkins: Build Robust CI/CD Pipelines Efficiently"
exportedBy: "Kortex"
exportDate: "2026-05-20T06:50:17.455Z"
---

# Mastering Docker and Jenkins: Build Robust CI/CD Pipelines Efficiently

73ac9a94-5839-465a-818e-138a00c666ad

Mastering Docker and Jenkins: Build Robust CI/CD Pipelines Efficiently

153dd8fe-32e7-4aab-ab9b-76fd63ec3c50

https://www.docker.com/blog/docker-and-jenkins-build-robust-ci-cd-pipelines/

Mastering Docker and Jenkins: Build Robust CI/CD Pipelines Efficiently | Docker

Skip to content

https://www.docker.com/blog/docker-and-jenkins-build-robust-ci-cd-pipelines/#main-content

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

https://www.docker.com/blog/docker-and-jenkins-build-robust-ci-cd-pipelines/

https://www.docker.com/blog/docker-and-jenkins-build-robust-ci-cd-pipelines/

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

Mastering Docker and Jenkins: Build Robust CI/CD Pipelines Efficiently

Posted Jan 16, 2025

Vladimir Mikhalev

https://www.docker.com/contributors/vladimir-mikhalev/

Hey there, fellow engineers and tech enthusiasts! I'm excited to share one of my favorite strategies for modern software delivery: combining Docker and Jenkins to power up your CI/CD pipelines.

Throughout my career as a Senior DevOps Engineer and Docker Captain, I've found that these two tools can drastically streamline releases, reduce environment-related headaches, and give teams the confidence they need to ship faster.

In this post, I'll walk you through what Docker and Jenkins are, why they pair perfectly, and how you can build and maintain efficient pipelines. My goal is to help you feel right at home when automating your workflows. Let's dive in.

Brief overview of continuous integration and continuous delivery

Continuous integration (CI) and continuous delivery (CD) are key pillars of modern development. If you're new to these concepts, here's a quick rundown:

#### Continuous integration (CI):

Developers frequently commit their code to a shared repository, triggering automated builds and tests. This practice prevents conflicts and ensures defects are caught early.

#### Continuous delivery (CD):

With CI in place, organizations can then confidently automate releases. That means shorter release cycles, fewer surprises, and the ability to roll back changes quickly if needed.

Leveraging CI/CD can dramatically improve your team's velocity and quality. Once you experience the benefits of dependable, streamlined pipelines, there's no going back.

Why combine Docker and Jenkins for CI/CD?

https://www.docker.com/

allows you to containerize your applications, creating consistent environments across development, testing, and production. Jenkins, on the other hand, helps you automate tasks such as building, testing, and deploying your code. I like to think of Jenkins as the tireless “assembly line worker,” while Docker provides identical “containers” to ensure consistency throughout your project's life cycle.

#### Here's why blending these tools is so powerful:

#### Consistent environments:

Docker containers guarantee uniformity from a developer's laptop all the way to production. This consistency reduces errors and eliminates the dreaded “works on my machine” excuse.

#### Speedy deployments and rollbacks:

Docker images are lightweight. You can ship or revert changes at the drop of a hat — perfect for short delivery process cycles where minimal downtime is crucial.

#### Scalability:

Need to run 1,000 tests in parallel or support multiple teams working on microservices? No problem. Spin up multiple Docker containers whenever you need more build agents, and let Jenkins orchestrate everything with Jenkins pipelines.

https://www.docker.com/blog/docker-for-devops/

junkie like me, this synergy between Jenkins and Docker is a dream come true.

Setting up your CI/CD pipeline with Docker and Jenkins

#### Before you roll up your sleeves, let's cover the essentials you'll need:

Docker Desktop

https://www.docker.com/products/docker-desktop/

(or a Docker server environment) installed and running. You can

https://docs.docker.com/get-docker/

for various operating systems.

Jenkins downloaded from

https://hub.docker.com/r/jenkins/jenkins

or installed on your machine. These days, you'll want

jenkins/jenkins:lts

(the long-term support image) rather than the deprecated

library/jenkins

Proper permissions for Docker commands and the ability to manage Docker images on your system.

A GitHub or similar code repository where you can store your Jenkins pipeline configuration (optional, but recommended).

If you're planning a production setup, consider a container orchestration platform like

https://www.docker.com/resources/kubernetes-and-docker/

. This approach simplifies scaling Jenkins, updating Jenkins, and managing additional Docker servers for heavier workloads.

Building a robust CI/CD pipeline with Docker and Jenkins

After prepping your environment, it's time to create your first Jenkins-Docker pipeline. Below, I'll walk you through common steps for a typical pipeline — feel free to modify them to fit your stack.

1. Install necessary Jenkins plugins

Jenkins offers countless plugins, so let's start with a few that make configuring Jenkins with Docker easier:

Docker Pipeline Plugin

CloudBees Docker Build and Publish

#### How to install plugins:

Manage Jenkins

Manage Plugins

in Jenkins.

tab and search for the plugins listed above.

Install them (and restart Jenkins if needed).

#### Code example (plugin installation via CLI):

# Install plugins using Jenkins CLI

java -jar jenkins-cli.jar -s \[http://&lt;jenkins-server\](http://&lt;jenkins-server)>:8080/ install-plugin docker-pipeline

java -jar jenkins-cli.jar -s \[http://&lt;jenkins-server\](http://&lt;jenkins-server)>:8080/ install-plugin docker

java -jar jenkins-cli.jar -s \[http://&lt;jenkins-server\](http://&lt;jenkins-server)>:8080/ install-plugin docker-build-publish

#### Pro tip (advanced approach):

If you're aiming for a fully infrastructure-as-code setup, consider using

Jenkins configuration as code (JCasC)

https://plugins.jenkins.io/configuration-as-code/

. With JCasC, you can declare all your Jenkins settings — including plugins, credentials, and pipeline definitions — in a YAML file. This means your entire Jenkins configuration is version-controlled and reproducible, making it effortless to spin up fresh Jenkins instances or apply consistent settings across multiple environments. It's especially handy for large teams looking to manage Jenkins at scale.

Jenkins Plugin Installation Guide

https://www.jenkins.io/doc/book/managing/plugins/

Jenkins Configuration as Code Plugin

https://plugins.jenkins.io/configuration-as-code/

2. Set up your Jenkins pipeline

In this step, you'll define your pipeline. A Jenkins “pipeline” job uses a

Jenkinsfile

(stored in your code repository) to specify the steps, stages, and environment requirements.

#### Example Jenkinsfile:

stage('Checkout') {

git branch: 'main', url: ' \[https://github.com/your-org/your-repo.git\](https://github.com/your-org/your-repo.git)'

stage('Build') {

dockerImage = docker.build("your-org/your-app:${env.BUILD\_NUMBER}")

stage('Test') {

sh 'docker run --rm your-org/your-app:${env.BUILD\_NUMBER} ./run-tests.sh'

stage('Push') {

docker.withRegistry(' \[https://index.docker.io/v1/\](https://index.docker.io/v1/)', 'dockerhub-credentials') {

dockerImage.push()

#### Let's look at what's happening here:

: Pulls your repository.

: Creates a built docker image (

your-org/your-app

) with the build number as a tag.

: Runs your test suite inside a fresh container, ensuring Docker containers create consistent environments for every test run.

: Pushes the image to your Docker registry (e.g., Docker Hub) if the tests pass.

Jenkins Pipeline Documentation

https://www.jenkins.io/doc/book/pipeline/

3. Configure Jenkins for automated builds

#### Now that your pipeline is set up, you'll want Jenkins to run it automatically:

Webhook triggers

: Configure your source control (e.g., GitHub) to send a webhook whenever code is pushed. Jenkins will kick off a build immediately.

: Jenkins periodically checks your repo for new commits and starts a build if it detects changes.

Which trigger method should you choose?

Webhook triggers

are ideal if you want near real-time builds. As soon as you push to your repo, Jenkins is notified, and a new build starts almost instantly. This approach is typically more efficient, as Jenkins doesn't have to continuously check your repository for updates. However, it requires that your source control system and network environment support webhooks.

is useful if your environment can't support incoming webhooks — for example, if you're behind a corporate firewall or your repository isn't configured for outbound hooks. In that case, Jenkins routinely checks for new commits on a schedule you define (e.g., every five minutes), which can add a small delay and extra overhead but may simplify setup in locked-down environments.

Personal experience

: I love webhook triggers because they keep everything as close to real-time as possible. Polling works fine if webhooks aren't feasible, but you'll see a slight delay between code pushes and build starts. It can also generate extra network traffic if your polling interval is too frequent.

4. Build, test, and deploy with Docker containers

#### Here comes the fun part — automating the entire cycle from build to deploy:

Build Docker image

: After pulling the code, Jenkins calls

docker.build

to create a new image.

: Automated or automated acceptance testing runs inside a container spun up from that image, ensuring consistency.

to registry: Assuming tests pass, Jenkins pushes the tagged image to your Docker registry — this could be Docker Hub or a private registry.

: Optionally, Jenkins can then deploy the image to a remote server or a container orchestrator (Kubernetes, etc.).

This streamlined approach ensures every step — build, test, deploy — lives in one cohesive pipeline, preventing those “where'd that step go?” mysteries.

5. Optimize and maintain your pipeline

Once your pipeline is up and running, here are a few maintenance tips and enhancements to keep everything running smoothly:

#### Clean up images:

Routine cleanup of Docker images can reclaim space and reduce clutter.

#### Security updates:

Stay on top of updates for Docker, Jenkins, and any plugins. Applying patches promptly helps protect your CI/CD environment from vulnerabilities.

#### Resource monitoring:

Ensure Jenkins nodes have enough memory, CPU, and disk space for builds. Overworked nodes can slow down your pipeline and cause intermittent failures.

In large projects, consider separating your build agents from your Jenkins controller by running them in ephemeral Docker containers (also known as Jenkins agents). If an agent goes down or becomes stale, you can quickly spin up a fresh one — ensuring a clean, consistent environment for every build and reducing the load on your main Jenkins server.

Why use Declarative Pipelines for CI/CD?

Although Jenkins supports multiple pipeline syntaxes,

Declarative Pipelines

https://www.jenkins.io/doc/book/pipeline/#declarative-versus-scripted-pipeline-syntax

stand out for their clarity and resource-friendly design. Here's why:

#### Simplified, opinionated syntax:

Everything is wrapped in a single

pipeline { ... }

block, which minimizes “scripting sprawl.” It's perfect for teams who want a quick path to best practices without diving deeply into Groovy specifics.

#### Easier resource allocation:

By specifying an

at either the pipeline level or within each stage, you can offload heavyweight tasks (builds, tests) onto separate worker nodes or Docker containers. This approach helps prevent your main Jenkins controller from becoming overloaded.

#### Parallelization and matrix builds:

If you need to run multiple test suites or support various OS/browser combinations, Declarative Pipelines make it straightforward to define parallel stages or set up a matrix build. This tactic is incredibly handy for microservices or large test suites requiring different environments in parallel.

#### Built-in “escape hatch”:

Need advanced Groovy features? Just drop into a

block. This lets you access Scripted Pipeline capabilities for niche cases, while still enjoying Declarative's streamlined structure most of the time.

#### Cleaner parameterization:

Want to let users pick which tests to run or which Docker image to use? The

directive makes your pipeline more flexible. A single Jenkinsfile can handle multiple scenarios — like unit vs. integration testing — without duplicating stages.

Declarative Pipeline examples

Below are sample pipelines to illustrate how declarative syntax can simplify resource allocation and keep your Jenkins controller healthy.

Example 1: Basic Declarative Pipeline

stage('Build') {

echo 'Building...'

stage('Test') {

echo 'Testing...'

Runs on any available Jenkins agent (worker).

Uses two stages in a simple sequence.

Example 2: Stage-level agents for resource isolation

agent none // Avoid using a global agent at the pipeline level

stage('Build') {

agent { docker 'maven:3.9.3-eclipse-temurin-17' }

sh 'mvn clean package'

stage('Test') {

agent { docker 'openjdk:17-jdk' }

sh 'java -jar target/my-app-tests.jar'

Each stage runs in its own container, preventing any single node from being overwhelmed.

at the top ensures no global agent is allocated unnecessarily.

Example 3: Parallelizing test stages

stage('Test') {

stage('Unit Tests') {

agent { label 'linux-node' }

sh './run-unit-tests.sh'

stage('Integration Tests') {

agent { label 'linux-node' }

sh './run-integration-tests.sh'

Splits tests into two parallel stages.

Each stage can run on a different node or container, speeding up feedback loops.

Example 4: Parameterized pipeline

parameters {

choice(name: 'TEST\_TYPE', choices: \['unit', 'integration', 'all'\], description: 'Which test suite to run?')

stage('Build') {

echo 'Building...'

stage('Test') {

expression { return params.TEST\_TYPE == 'unit' || params.TEST\_TYPE == 'all' }

echo 'Running unit tests...'

stage('Integration') {

expression { return params.TEST\_TYPE == 'integration' || params.TEST\_TYPE == 'all' }

echo 'Running integration tests...'

Lets you choose which tests to run (unit, integration, or both).

Only executes relevant stages based on the chosen parameter, saving resources.

Example 5: Matrix builds

stage('Build and Test Matrix') {

label "${PLATFORM}-docker"

name 'PLATFORM'

values 'linux', 'windows'

name 'BROWSER'

values 'chrome', 'firefox'

stage('Build') {

echo "Build on ${PLATFORM} with ${BROWSER}"

stage('Test') {

echo "Test on ${PLATFORM} with ${BROWSER}"

Defines a matrix of PLATFORM x BROWSER, running each combination in parallel.

Perfect for testing multiple OS/browser combinations without duplicating pipeline logic.

Additional resources

Jenkins Pipeline Syntax

https://www.jenkins.io/doc/book/pipeline/syntax/#declarative-pipeline

: Official reference for sections, directives, and advanced features like matrix, parallel, and post conditions.

Jenkins Pipeline Steps Reference

https://www.jenkins.io/doc/pipeline/steps/

: Comprehensive list of steps you can call in your Jenkinsfile.

Jenkins Configuration as Code Plugin (JCasC)

https://github.com/jenkinsci/configuration-as-code-plugin

: Ideal for version-controlling your Jenkins configuration, including plugin installations and credentials.

Using Declarative Pipelines helps ensure your CI/CD setup is easier to maintain, scalable, and secure. By properly configuring agents — whether Docker-based or label-based — you can spread workloads across multiple worker nodes, minimize resource contention, and keep your Jenkins controller humming along happily.

Best practices for CI/CD with Docker and Jenkins

Ready to supercharge your setup? Here are a few tried-and-true habits I've cultivated:

#### Leverage Docker's layer caching:

Optimize your Dockerfiles so stable (less frequently changing) layers appear early. This drastically reduces build times.

#### Run tests in parallel:

Jenkins can run multiple containers for different services or microservices, letting you test them side by side. Declarative Pipelines make it easy to define parallel stages, each on its own agent.

#### Shift left on security:

Integrate security checks early in the pipeline. Tools like

Docker Scout

https://docs.docker.com/scout/

let you scan images for vulnerabilities, while Jenkins plugins can enforce compliance policies. Don't wait until production to discover issues.

#### Optimize resource allocation:

Properly configure CPU and memory limits for Jenkins and Docker containers to avoid resource hogging. If you're scaling Jenkins, distribute builds across multiple worker nodes or ephemeral agents for maximum efficiency.

#### Configuration management:

Store Jenkins jobs, pipeline definitions, and plugin configurations in source control. Tools like Jenkins Configuration as Code simplify versioning and replicating your setup across multiple Docker servers.

With these strategies — plus a healthy dose of Declarative Pipelines — you'll have a lean, high-octane CI/CD pipeline that's easier to maintain and evolve.

Troubleshooting Docker and Jenkins Pipelines

Even the best systems hit a snag now and then. Here are a few hurdles I've seen (and conquered):

#### Handling environment variability:

Keep Docker and Jenkins versions synced across different nodes. If multiple Jenkins nodes are in play, standardize Docker versions to avoid random build failures.

#### Troubleshooting build failures:

docker logs -f <container-id>

to see exactly what happened inside a container. Often, the logs reveal missing dependencies or misconfigured environment variables.

#### Networking challenges:

If your containers need to talk to each other — especially across multiple hosts — make sure you configure Docker networks or an orchestration platform properly.

Read Docker's networking documentation

https://docs.docker.com/network/

for details, and check out the

Jenkins diagnosing issues guide

https://www.jenkins.io/doc/book/troubleshooting/diagnosing-errors/

for more troubleshooting tips.

Pairing Docker and Jenkins offers a nimble, robust approach to CI/CD. Docker locks down consistent environments and lightning-fast rollouts, while Jenkins automates key tasks like building, testing, and pushing your changes to production. When these two are in harmony, you can expect shorter release cycles, fewer integration headaches, and more time to focus on developing awesome features.

A healthy pipeline also means your team can respond quickly to user feedback and confidently roll out updates — two crucial ingredients for any successful software project. And if you're concerned about security, there are plenty of tools and best practices to keep your applications safe.

I hope this guide helps you build (and maintain) a high-octane CI/CD pipeline that your team will love. If you have questions or need a hand, feel free to reach out on the

community forums

https://forums.docker.com/

, join the conversation on

https://dockr.ly/slack

, or open a ticket on

GitHub issues

https://github.com/docker/

. You'll find plenty of fellow Docker and Jenkins enthusiasts who are happy to help.

Thanks for reading, and happy building!

Subscribe to the

Docker Newsletter

https://www.docker.com/newsletter-subscription/

Take a deeper dive in Docker's official Jenkins integration documentation.

https://docs.docker.com/scout/integrations/ci/jenkins/

Docker Business

https://www.docker.com/products/business/

for comprehensive CI/CD security at scale.

Get the latest release of

Docker Desktop

https://www.docker.com/products/docker-desktop/

Have questions? The

Docker community is here to help

https://www.docker.com/community/

New to Docker?

https://docs.docker.com/desktop/

https://docs.docker.com/desktop/

https://docs.docker.com/desktop/

https://www.docker.com/blog/tag/cicd/

Docker Desktop

https://www.docker.com/blog/tag/docker-desktop/

https://www.docker.com/blog/tag/docker-hub/

Popular Topics

https://www.docker.com/blog/tag/popular-topics/

https://www.docker.com/blog/category/products/

Table of contents

Brief overview of continuous integration and continuous delivery

https://www.docker.com/blog/docker-and-jenkins-build-robust-ci-cd-pipelines/#brief-overview-of-continuous-integration-and-continuous-delivery

Why combine Docker and Jenkins for CI/CD?

https://www.docker.com/blog/docker-and-jenkins-build-robust-ci-cd-pipelines/#why-combine-docker-and-jenkins-for-ci-cd

Setting up your CI/CD pipeline with Docker and Jenkins

https://www.docker.com/blog/docker-and-jenkins-build-robust-ci-cd-pipelines/#setting-up-your-ci-cd-pipeline-with-docker-and-jenkins

Building a robust CI/CD pipeline with Docker and Jenkins

https://www.docker.com/blog/docker-and-jenkins-build-robust-ci-cd-pipelines/#building-a-robust-ci-cd-pipeline-with-docker-and-jenkins

Troubleshooting Docker and Jenkins Pipelines

https://www.docker.com/blog/docker-and-jenkins-build-robust-ci-cd-pipelines/#troubleshooting-docker-and-jenkins-pipelines

https://www.docker.com/blog/docker-and-jenkins-build-robust-ci-cd-pipelines/#conclusion

https://www.docker.com/blog/docker-and-jenkins-build-robust-ci-cd-pipelines/#learn-more

https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fwww.docker.com%2Fblog%2Fdocker-and-jenkins-build-robust-ci-cd-pipelines%2F

https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.docker.com%2Fblog%2Fdocker-and-jenkins-build-robust-ci-cd-pipelines%2F

https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.docker.com%2Fblog%2Fdocker-and-jenkins-build-robust-ci-cd-pipelines%2F

Related Posts

\[May 12, 2026

Docker AI Governance: Unlock Agent Autonomy, Safely

Introducing Docker AI Governance: centralized control over how agents execute, what they can reach on the network, which credentials they can use, and which MCP tools they can call, so every developer in your company can run AI agents safely, wherever they work. Your laptop is the new prod Agents are the biggest productivity unlock…

Srini Sekaran Read now\](https://www.docker.com/blog/docker-ai-governance-unlock-agent-autonomy-safely/)

\[May 18, 2026

Coding Agent Horror Stories: The Security Crisis Threatening Developer Infrastructure

Explore real AI coding agent security failures, from database wipes to secrets leakage, and learn how Docker Sandboxes reduce the blast radius.

Ajeet Singh Raina Read now\](https://www.docker.com/blog/ai-coding-agent-horror-stories-security-risks/)

\[May 15, 2026

Custom MCP Catalogs and Profiles: Advancing Enterprise MCP Adoption

Learn how to create your own custom MCP catalog and maintain separate server collections and configurations for smooth transitions between workflows.

Bobby House Read now\](https://www.docker.com/blog/create-custom-mcp-catalogs-and-profiles/)

\[May 13, 2026

NIST Narrows the NVD: What Container Security Programs Should Reassess

On April 15, NIST announced a prioritized enrichment model for the National Vulnerability Database. Most CVEs will still be published, but fewer will receive the CVSS scores, CPE mappings, and CWE classifications that container scanners and compliance programs have historically relied on. The change formalizes a drift that has been visible to anyone pulling NVD…

Dan Stelzer Read now\](https://www.docker.com/blog/nist-narrows-the-nvd-what-container-security-programs-should-reassess/)

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

