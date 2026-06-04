---
sourceFile: "Secure a Backstage application with Docker Hardened Images | Docker Docs"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.693Z"
---

# Secure a Backstage application with Docker Hardened Images | Docker Docs

135bc586-c6df-4034-b468-6d27d2fd34db

Secure a Backstage application with Docker Hardened Images | Docker Docs

66769f35-40e2-4e98-a5c2-1e8c49e250b7

https://docs.docker.com/guides/dhi-backstage/

Secure a Backstage application with Docker Hardened Images | Docker Docs

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

Secure a Backstage application with Docker Hardened Images

https://docs.docker.com/guides/dhi-backstage/

Learn how to secure a Backstage developer portal using Docker Hardened Images (DHI), handle native module compilation with better-sqlite3, add Socket Firewall protection during dependency installation, and produce a distroless runtime image using DHI customizations.

Docker Hardened Images

« Back to all guides

https://docs.docker.com/guides/

https://docs.docker.com/

https://docs.docker.com/guides/

/ Secure a Backstage application with Docker Hardened Images

Secure a Backstage application with Docker Hardened Images

Ask Gordon Copy Markdown View Markdown

Table of contents

Prerequisites

https://docs.docker.com/guides/dhi-backstage/#prerequisites

Why Backstage needs customization

https://docs.docker.com/guides/dhi-backstage/#why-backstage-needs-customization

Step 1: Examine the original Dockerfile

https://docs.docker.com/guides/dhi-backstage/#step-1-examine-the-original-dockerfile

Step 2: Switch the build stages to DHI

https://docs.docker.com/guides/dhi-backstage/#step-2-switch-the-build-stages-to-dhi

Step 3: Add Socket Firewall protection

https://docs.docker.com/guides/dhi-backstage/#step-3-add-socket-firewall-protection

Step 4: Remove the shell and the package manager with DHI customizations

https://docs.docker.com/guides/dhi-backstage/#step-4-remove-the-shell-and-the-package-manager-with-dhi-customizations

Update the Dockerfile

https://docs.docker.com/guides/dhi-backstage/#update-the-dockerfile

Step 5: Verify the results

https://docs.docker.com/guides/dhi-backstage/#step-5-verify-the-results

What's next

https://docs.docker.com/guides/dhi-backstage/#whats-next

This guide shows how to secure a Backstage application using Docker Hardened Images (DHI). Backstage is a CNCF open source developer portal used by thousands of organizations to manage their software catalogs, templates, and developer tooling.

By the end of this guide, you'll have a Backstage container image that is distroless, runs as a non-root user by default, and has dramatically fewer CVEs than the standard

node:24-trixie-slim

base image while still supporting the native module compilation that Backstage requires.

Prerequisites

https://docs.docker.com/guides/dhi-backstage/#prerequisites

Docker Desktop or Docker Engine with BuildKit enabled

A Docker Hub account authenticated with

docker login

docker login dhi.io

A Backstage project created with

@backstage/create-app

Why Backstage needs customization

https://docs.docker.com/guides/dhi-backstage/#why-backstage-needs-customization

The DHI migration examples cover applications where you can swap the base image and everything works. Backstage is different. It uses

better-sqlite3

and other packages that compile native Node.js modules at install time, which means the build stage needs

— none of which are in the base

dhi.io/node

image. The runtime image only needs the shared library (

sqlite-libs

) that the compiled native module links against.

This is a common pattern. Any Node.js application that depends on native addons (such as

node-canvas

) faces the same challenge. The approach in this guide applies to all of them.

Step 1: Examine the original Dockerfile

https://docs.docker.com/guides/dhi-backstage/#step-1-examine-the-original-dockerfile

The official Backstage documentation recommends a multi-stage Dockerfile using

node:24-trixie-slim

(Debian). A typical setup looks like this:

# Stage 1 - Create yarn install skeleton layer
FROM node:24-trixie-slim AS packages
WORKDIR /app
COPY backstage.json package.json yarn.lock ./
COPY .yarn ./.yarn
COPY .yarnrc.yml ./
COPY packages packages
COPY plugins plugins
RUN find packages \! -name "package.json" -mindepth 2 -maxdepth 2 \
    -exec rm -rf {} \+

# Stage 2 - Install dependencies and build packages
FROM node:24-trixie-slim AS build
ENV PYTHON=/usr/bin/python3
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update && \
    apt-get install -y --no-install-recommends python3 g++ build-essential && \
    rm -rf /var/lib/apt/lists/\*
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update && \
    apt-get install -y --no-install-recommends libsqlite3-dev && \
    rm -rf /var/lib/apt/lists/\*
USER node
WORKDIR /app
COPY --from=packages --chown=node:node /app .
RUN --mount=type=cache,target=/home/node/.cache/yarn,sharing=locked,uid=1000,gid=1000 \
    yarn install --immutable
COPY --chown=node:node . .
RUN yarn tsc
RUN yarn --cwd packages/backend build
RUN mkdir packages/backend/dist/skeleton packages/backend/dist/bundle \
    && tar xzf packages/backend/dist/skeleton.tar.gz \
       -C packages/backend/dist/skeleton \
    && tar xzf packages/backend/dist/bundle.tar.gz \
       -C packages/backend/dist/bundle

# Stage 3 - Build the actual backend image
FROM node:24-trixie-slim
ENV PYTHON=/usr/bin/python3
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update && \
    apt-get install -y --no-install-recommends python3 g++ build-essential && \
    rm -rf /var/lib/apt/lists/\*
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update && \
    apt-get install -y --no-install-recommends libsqlite3-dev && \
    rm -rf /var/lib/apt/lists/\*
USER node
WORKDIR /app
COPY --from=build --chown=node:node /app/.yarn ./.yarn
COPY --from=build --chown=node:node /app/.yarnrc.yml ./
COPY --from=build --chown=node:node /app/backstage.json ./
COPY --from=build --chown=node:node /app/yarn.lock \
     /app/package.json \
     /app/packages/backend/dist/skeleton/ ./
RUN --mount=type=cache,target=/home/node/.cache/yarn,sharing=locked,uid=1000,gid=1000 \
    yarn workspaces focus --all --production
COPY --from=build --chown=node:node /app/packages/backend/dist/bundle/ ./
CMD \["node", "packages/backend", "--config", "app-config.yaml"\]

#### Run this image and inspect what's available inside the container:

docker build -t backstage:init .
docker run -d \
    -e APP\_CONFIG\_backend\_database\_client='better-sqlite3' \
    -e APP\_CONFIG\_backend\_database\_connection=':memory:' \
    -e APP\_CONFIG\_auth\_providers\_guest\_dangerouslyAllowOutsideDevelopment='true' \
    -p 7007:7007 \
    -u 1000 \
    --cap-drop=ALL \
    --read-only \
    --tmpfs /tmp \
    backstage:init

This works, but the runtime container has a shell, a package manager, and yarn. None of these are needed to run Backstage. Run

docker exec

to see what's accessible inside:

docker exec -it <container-id> sh
$ cat /etc/shells
# /etc/shells: valid login shells
/bin/sh
/usr/bin/sh
/bin/bash
/usr/bin/bash
/bin/rbash
/usr/bin/rbash
/usr/bin/dash
$ yarn --version
4.12.0
$ dpkg --version
dpkg version 1.22.11 (arm64).
$ whoami
node
$ id
uid=1000(node) gid=1000(node) groups=1000(node)

node:24-trixie-slim

image ships with three shells (

), a package manager (

. Each of these tools increases the attack surface. An attacker who gains access to this container could use them for lateral movement across your infrastructure.

Step 2: Switch the build stages to DHI

https://docs.docker.com/guides/dhi-backstage/#step-2-switch-the-build-stages-to-dhi

Replace all three stages with DHI equivalents. DHI Node.js images are available in both Alpine and Debian variants. This guide uses the Alpine variant (

dhi.io/node:24-alpine3.23

) because it produces a smaller image. If you need to stay on Debian for compatibility reasons, use

dhi.io/node:24-bookworm

# Stage 1: prepare packages
FROM --platform=$BUILDPLATFORM dhi.io/node:24-alpine3.23-dev AS packages
WORKDIR /app
COPY backstage.json package.json yarn.lock ./
COPY .yarn ./.yarn
COPY .yarnrc.yml ./
COPY packages packages
COPY plugins plugins
RUN find packages \! -name "package.json" -mindepth 2 -maxdepth 2 \
    -exec rm -rf {} \+

# Stage 2: build the application
FROM --platform=$BUILDPLATFORM dhi.io/node:24-alpine3.23-dev AS build
ENV PYTHON=/usr/bin/python3
RUN apk add --no-cache g++ make python3 sqlite-dev && \
    rm -rf /var/lib/apk/lists/\*
WORKDIR /app
COPY --from=packages --chown=node:node /app .
RUN --mount=type=cache,target=/home/node/.cache/yarn,sharing=locked,uid=1000,gid=1000 \
    yarn install --immutable
COPY --chown=node:node . .
RUN yarn tsc
RUN yarn --cwd packages/backend build
RUN mkdir packages/backend/dist/skeleton packages/backend/dist/bundle \
    && tar xzf packages/backend/dist/skeleton.tar.gz \
       -C packages/backend/dist/skeleton \
    && tar xzf packages/backend/dist/bundle.tar.gz \
       -C packages/backend/dist/bundle

# Final Stage: create the runtime image
FROM dhi.io/node:24-alpine3.23-dev
ENV PYTHON=/usr/bin/python3
RUN apk add --no-cache g++ make python3 sqlite-dev && \
    rm -rf /var/lib/apk/lists/\*
WORKDIR /app
COPY --from=build --chown=node:node /app/.yarn ./.yarn
COPY --from=build --chown=node:node /app/.yarnrc.yml ./
COPY --from=build --chown=node:node /app/backstage.json ./
COPY --from=build --chown=node:node /app/yarn.lock \
     /app/package.json \
     /app/packages/backend/dist/skeleton/ ./
RUN --mount=type=cache,target=/home/node/.cache/yarn,sharing=locked,uid=1000,gid=1000 \
    yarn workspaces focus --all --production \
    && rm -rf "$(yarn cache clean)"
COPY --from=build --chown=node:node /app/packages/backend/dist/bundle/ ./
CMD \["node", "packages/backend", "--config", "app-config.yaml"\]

#### Build and tag this version:

docker build -t backstage:dhi-dev .

variant includes a shell and package manager, which is why

works. Backstage requires

and native build tools in the runtime image because

yarn workspaces focus --all --production

recompiles native modules during the production install. This is specific to Backstage's build process — most Node.js applications can use the standard (non-dev) DHI runtime variant without additional packages.

The DHI images come with attestations that the original

node:24-trixie-slim

images don't have. Check what's attached:

docker scout attest list dhi.io/node:24-alpine3.23

DHI images ship with 15 attestations including CycloneDX SBOM, SLSA provenance, OpenVEX, Scout health reports, secret scans, virus/malware reports, and an SLSA verification summary.

Step 3: Add Socket Firewall protection

https://docs.docker.com/guides/dhi-backstage/#step-3-add-socket-firewall-protection

DHI provides

(Socket Firewall) variants for Node.js images. Socket Firewall intercepts

commands during the build to detect and block malicious packages before they execute install scripts.

To enable Socket Firewall, change the

in all three stages. The SFW version of the Dockerfile:

# Stage 1: prepare packages
FROM --platform=$BUILDPLATFORM dhi.io/node:24-alpine3.23-sfw-dev AS packages
WORKDIR /app
COPY backstage.json package.json yarn.lock ./
COPY .yarn ./.yarn
COPY .yarnrc.yml ./
COPY packages packages
COPY plugins plugins
RUN find packages \! -name "package.json" -mindepth 2 -maxdepth 2 \
    -exec rm -rf {} \+

# Stage 2: build the packages
FROM --platform=$BUILDPLATFORM dhi.io/node:24-alpine3.23-sfw-dev AS build-packages
ENV PYTHON=/usr/bin/python3
RUN apk add --no-cache g++ make python3 sqlite-dev && \
    rm -rf /var/lib/apk/lists/\*
WORKDIR /app
COPY --from=packages --chown=node:node /app .
RUN --mount=type=cache,target=/home/node/.cache/yarn,sharing=locked,uid=1000,gid=1000 \
    yarn install --immutable
COPY --chown=node:node . .
RUN yarn tsc
RUN yarn --cwd packages/backend build
RUN mkdir packages/backend/dist/skeleton packages/backend/dist/bundle \
    && tar xzf packages/backend/dist/skeleton.tar.gz \
       -C packages/backend/dist/skeleton \
    && tar xzf packages/backend/dist/bundle.tar.gz \
       -C packages/backend/dist/bundle

# Final Stage: create the runtime image
FROM dhi.io/node:24-alpine3.23-sfw-dev
ENV PYTHON=/usr/bin/python3
RUN apk add --no-cache g++ make python3 sqlite-dev && \
    rm -rf /var/lib/apk/lists/\*
WORKDIR /app
COPY --from=build-packages --chown=node:node /app/.yarn ./.yarn
COPY --from=build-packages --chown=node:node /app/.yarnrc.yml ./
COPY --from=build-packages --chown=node:node /app/backstage.json ./
COPY --from=build-packages --chown=node:node /app/yarn.lock \
     /app/package.json \
     /app/packages/backend/dist/skeleton/ ./
RUN --mount=type=cache,target=/home/node/.cache/yarn,sharing=locked,uid=1000,gid=1000 \
    yarn workspaces focus --all --production \
    && rm -rf "$(yarn cache clean)"
COPY --from=build-packages --chown=node:node /app/packages/backend/dist/bundle/ ./
CMD \["node", "packages/backend", "--config", "app-config.yaml"\]

#### Build this version:

docker build -t backstage:dhi-sfw-dev .

#### When you build, you'll see Socket Firewall messages in the build output:

Protected by Socket Firewall

commands executed in the Dockerfile or in the running containers.

variant is larger (1.9 GB versus 1.72 GB) because Socket Firewall adds monitoring tooling. The security benefit during

yarn install

outweighs the size increase.

Step 4: Remove the shell and the package manager with DHI customizations

https://docs.docker.com/guides/dhi-backstage/#step-4-remove-the-shell-and-the-package-manager-with-dhi-customizations

The previous steps still use the

variant as the runtime image, which includes a shell and package manager. DHI customizations let you start from the base (non-dev) image — which has no shell and no package manager — and add only the runtime libraries and language runtimes your application needs.

#### When creating a customization, only add what your application needs at runtime:

#### System packages

- add shared libraries (such as

sqlite-libs

) and language runtimes from the DHI catalog (such as

python-3.14

). Do not add build tools (such as

from Alpine).

#### Build tools

- keep these in the

build stage only. Never add them to the runtime customization.

Language runtimes installed from the DHI hardened package feed are patched and tracked in the image SBOM, which is why they are acceptable as system packages. Build tools from Alpine or Debian package feeds are not hardened and should never appear in the runtime image.

#### For Backstage, the runtime image needs:

sqlite-libs

- the shared library that the compiled

better-sqlite3

native module links against (added as a system package).

- if your Backstage plugins or configuration require Python at runtime. Added as the

python-3.14

system package from the DHI catalog. Unlike

installed via

, this package is patched by Docker and tracked in the image SBOM.

Docker will continuously build with SLSA Level 3 compliance and patch these customized images within the guaranteed SLA for CVE patching.

To create the customization, use one of the following methods.

Docker Hub UI dhictl CLI

#### After you mirror the Node.js DHI repository to your organization's namespace:

Open the mirrored Node.js repository in Docker Hub.

and choose the

node:24-alpine3.23

sqlite-libs

python-3.14

Create the customization.

For more information, see

Customize an image

https://docs.docker.com/dhi/how-to/customize/

is Docker's command-line tool for managing Docker Hardened Images. It lets you browse the DHI catalog, mirror images, and create customizations directly from your terminal. You can integrate

into CI/CD pipelines and infrastructure-as-code workflows. You can install

as a standalone binary or as a Docker CLI plugin (

); for installation instructions, see

Use the DHI CLI

https://docs.docker.com/dhi/how-to/cli/

Rather than writing the customization YAML by hand, use

to scaffold a starting point:

dhictl customization prepare --org YOUR\_ORG node 24-alpine3.23 \
    --destination YOUR\_ORG/dhi-node \
    --name "backstage" \
    --tag-suffix "\_backstage" \
    --output node-backstage.yaml

#### Edit the generated file to add the runtime libraries:

name: backstage

source: dhi/node
tag\_definition\_id: node/alpine-3.23/24

destination: YOUR\_ORG/dhi-node
tag\_suffix: \_backstage

platforms:
  - linux/amd64
  - linux/arm64

contents:
  packages:
    - sqlite-libs
    - python-3.14

accounts:
  root: true
  runs-as: node
  users:
    - name: node
      uid: 1000
  groups:
    - name: node
      gid: 1000

#### Then create the customization:

dhictl customization create --org YOUR\_ORG node-backstage.yaml

#### Monitor the build progress:

dhictl customization build list --org YOUR\_ORG YOUR\_ORG/dhi-node "backstage"

Docker builds the customized image on its secure infrastructure and publishes it as

YOUR\_ORG/dhi-node:24-alpine3.23\_backstage

If your Backstage configuration does not require Python at runtime, you can omit the

python-3.14

from the packages list. The

sqlite-libs

package alone is sufficient to run Backstage with

better-sqlite3

Update the Dockerfile

https://docs.docker.com/guides/dhi-backstage/#update-the-dockerfile

#### Update only the final stage of your Dockerfile to use the customized image:

# Final Stage: create the runtime image
FROM YOUR\_ORG/dhi-node:24-alpine3.23\_backstage
WORKDIR /app
COPY --from=build --chown=node:node /app/node\_modules ./node\_modules
COPY --from=build --chown=node:node /app/packages/backend/dist/bundle/ ./
CMD \["node", "packages/backend", "--config", "app-config.yaml"\]

#### Build this version:

docker build -t backstage:dhi .

Since the customization includes only runtime libraries and OCI artifacts — no build tools, no package manager, no shell — the resulting image is distroless:

docker run --rm YOUR\_ORG/dhi-node:24-alpine3.23\_backstage sh -c "echo hello"
docker: Error response from daemon: ... exec: "sh": executable file not found in $PATH

#### With the Enterprise customization:

The runtime image is distroless — no shell, no package manager.

Docker automatically rebuilds your customized image when the base Node.js image or any of its packages receive a security patch.

The full chain of trust is maintained, including SLSA Build Level 3 provenance.

Both the Node.js and Python runtimes are tracked in the image SBOM.

#### Confirm the container no longer has shell access:

docker exec -it <container-id> sh
OCI runtime exec failed: exec failed: unable to start container process: ...

Docker Debug

https://docs.docker.com/dhi/troubleshoot/#general-debugging

if you need to troubleshoot a running distroless container.

If your organization requires FIPS/STIG compliant images, that's also an option in DHI Enterprise.

Step 5: Verify the results

https://docs.docker.com/guides/dhi-backstage/#step-5-verify-the-results

#### Compare the DHI-based image against the original using Docker Scout:

docker scout compare backstage:dhi \
    --to backstage:init \
    --platform linux/amd64 \
    --ignore-unchanged

A typical comparison across the approaches shows results similar to the following:

DHI -sfw-dev

Content size

Shell in runtime

Package manager

Non-root default

Socket Firewall

Yes (build)

Yes (build) / No (runtime)

SLSA provenance

Full (Level 3)

variant is larger because Socket Firewall adds monitoring tooling to the image. The additional size is in the build stages, and the security benefit during

yarn install

outweighs the size increase.

#### For a more thorough assessment, scan with multiple tools:

trivy image backstage:dhi
grype backstage:dhi
docker scout quickview backstage:dhi

Different scanners detect different issues. Running all three gives you the most complete view of your security posture.

What's next

https://docs.docker.com/guides/dhi-backstage/#whats-next

Customize an image

https://docs.docker.com/dhi/how-to/customize/

— complete reference on the Enterprise customization UI.

Create and build a DHI

https://docs.docker.com/dhi/how-to/build/

— learn how to write a DHI definition file, build images locally.

Use the DHI CLI

https://docs.docker.com/dhi/how-to/cli/

— manage DHI images, mirrors, and customizations from the command line.

Migrate to DHI

https://docs.docker.com/dhi/migration/

— for applications that work with standard DHI images without additional packages.

Compare images

https://docs.docker.com/dhi/how-to/explore/#compare-and-evaluate-images

— evaluate security improvements between your original and hardened images.

Docker Debug

https://docs.docker.com/dhi/troubleshoot/#general-debugging

— troubleshoot distroless containers that have no shell.

Edit this page

https://github.com/docker/docs/edit/main/content/guides/dhi-backstage.md

Request changes

https://github.com/docker/docs/issues/new?template=doc\_issue.yml&location=https%3a%2f%2fdocs.docker.com%2fguides%2fdhi-backstage%2f&labels=status%2Ftriage

Table of contents

Prerequisites

https://docs.docker.com/guides/dhi-backstage/#prerequisites

Why Backstage needs customization

https://docs.docker.com/guides/dhi-backstage/#why-backstage-needs-customization

Step 1: Examine the original Dockerfile

https://docs.docker.com/guides/dhi-backstage/#step-1-examine-the-original-dockerfile

Step 2: Switch the build stages to DHI

https://docs.docker.com/guides/dhi-backstage/#step-2-switch-the-build-stages-to-dhi

Step 3: Add Socket Firewall protection

https://docs.docker.com/guides/dhi-backstage/#step-3-add-socket-firewall-protection

Step 4: Remove the shell and the package manager with DHI customizations

https://docs.docker.com/guides/dhi-backstage/#step-4-remove-the-shell-and-the-package-manager-with-dhi-customizations

Update the Dockerfile

https://docs.docker.com/guides/dhi-backstage/#update-the-dockerfile

Step 5: Verify the results

https://docs.docker.com/guides/dhi-backstage/#step-5-verify-the-results

What's next

https://docs.docker.com/guides/dhi-backstage/#whats-next

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

