---
sourceFile: "Using Docker with Zscaler | Docker Docs"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.814Z"
---

# Using Docker with Zscaler | Docker Docs

eb237a9f-e857-4dae-af27-8cc898387867

Using Docker with Zscaler | Docker Docs

00286de8-81d5-4ab0-b93c-4ee484ee1296

https://docs.docker.com/guides/zscaler/

Using Docker with Zscaler | Docker Docs

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

Using Docker with Zscaler

https://docs.docker.com/guides/zscaler/

This guide explains how to embed Zscaler's root certificate into Docker images, allowing containers to operate securely with Zscaler proxies and avoid SSL errors.

Networking Administration

« Back to all guides

https://docs.docker.com/guides/

https://docs.docker.com/

https://docs.docker.com/guides/

/ Using Docker with Zscaler

Using Docker with Zscaler

Ask Gordon Copy Markdown View Markdown

Table of contents

The role of certificates in Docker

https://docs.docker.com/guides/zscaler/#the-role-of-certificates-in-docker

Configure Zscaler proxy for Docker Desktop

https://docs.docker.com/guides/zscaler/#configure-zscaler-proxy-for-docker-desktop

Install root certificates in Docker images

https://docs.docker.com/guides/zscaler/#install-root-certificates-in-docker-images

Obtaining the root certificate

https://docs.docker.com/guides/zscaler/#obtaining-the-root-certificate

Building with the certificate

https://docs.docker.com/guides/zscaler/#building-with-the-certificate

https://docs.docker.com/guides/zscaler/#conclusion

In many corporate environments, network traffic is intercepted and monitored using HTTPS proxies, such as Zscaler. While Zscaler ensures security compliance and network control, it can cause issues for developers using Docker, particularly during build processes, where SSL certificate validation errors might occur. This guide outlines how to configure Docker containers and builds to properly handle Zscaler's custom certificates, ensuring smooth operation in monitored environments.

The role of certificates in Docker

https://docs.docker.com/guides/zscaler/#the-role-of-certificates-in-docker

When Docker builds or runs containers, it often needs to fetch resources from the internet—whether it's pulling a base image from a registry, downloading dependencies, or communicating with external services. In a proxied environment, Zscaler intercepts HTTPS traffic and replaces the remote server's certificate with its own. However, Docker doesn't trust this Zscaler certificate by default, leading to SSL errors.

x509: certificate signed by unknown authority

These errors occur because Docker cannot verify the validity of the certificate presented by Zscaler. To avoid this, you must configure Docker to trust Zscaler's certificate.

Configure Zscaler proxy for Docker Desktop

https://docs.docker.com/guides/zscaler/#configure-zscaler-proxy-for-docker-desktop

Depending on how Zscaler is deployed, you may need to configure Docker Desktop proxy settings manually to use the Zscaler proxy.

If you're using Zscaler as a system-level proxy via the

Zscaler Client Connector

https://help.zscaler.com/zscaler-client-connector/what-is-zscaler-client-connector

, all traffic on the device is automatically routed through Zscaler, so Docker Desktop uses the Zscaler proxy automatically with no additional configuration necessary.

If you are not using Zscaler as a system-level proxy, manually configure proxy settings in Docker Desktop. Set up proxy settings for all clients in the organization using

Settings Management

https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/

, or edit proxy configuration in the Docker Desktop GUI under

Settings > Resources > Proxies

https://docs.docker.com/desktop/settings-and-maintenance/settings/#proxies

Install root certificates in Docker images

https://docs.docker.com/guides/zscaler/#install-root-certificates-in-docker-images

To enable containers to use and trust the Zscaler proxy, embed the certificate in the image and configure the image's trust store. Installing certificates at image build time is the preferred approach, as it removes the need for configuration during startup and provides an auditable, consistent environment.

Obtaining the root certificate

https://docs.docker.com/guides/zscaler/#obtaining-the-root-certificate

The easiest way to obtain the root certificate is to export it from a machine where an administrator has already installed it. You can use either a web browser or the system's certificate management service (for example, Windows Certificate Store).

Example: Exporting the certificate using Google Chrome

https://docs.docker.com/guides/zscaler/#example-exporting-the-certificate-using-google-chrome

In Google Chrome, navigate to

chrome://certificate-manager/

Local certificates

View imported certificates

Find the Zscaler root certificate, often labeled

Zscaler Root CA

Open the certificate details and select

Save the certificate in ASCII PEM format.

#### Open the exported file in a text editor to confirm it includes

-----BEGIN CERTIFICATE-----

-----END CERTIFICATE-----

When you have obtained the certificate, store it in an accessible repository, such as JFrog Artifactory or a Git repository. Alternatively, use generic storage like AWS S3.

Building with the certificate

https://docs.docker.com/guides/zscaler/#building-with-the-certificate

To install these certificates when building images, copy the certificate into the build container and update the trust store. An example Dockerfile looks like this:

FROM debian:bookworm
COPY zscaler-root-ca.crt /usr/local/share/ca-certificates/zscaler-root-ca.crt
RUN apt-get update && \
    apt-get install -y ca-certificates && \
    update-ca-certificates

zscaler-root-ca.crt

is the root certificate, located at the root of the build context (often within the application's Git repository).

If you use an artifact repository, you can fetch the certificate directly using the

instruction. You can also use the

flag to verify that the content digest of the certificate is correct.

FROM debian:bookworm
ADD --checksum=sha256:24454f830cdb571e2c4ad15481119c43b3cafd48dd869a9b2945d1036d1dc68d \
    https://artifacts.example/certs/zscaler-root-ca.crt /usr/local/share/ca-certificates/zscaler-root-ca.crt
RUN apt-get update && \
    apt-get install -y ca-certificates && \
    update-ca-certificates

Using multi-stage builds

https://docs.docker.com/guides/zscaler/#using-multi-stage-builds

For multi-stage builds where certificates are needed in the final runtime image, ensure the certificate installation occurs in the final stage.

FROM debian:bookworm AS build
WORKDIR /build
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    curl \
    git
RUN --mount=target=. cmake -B output/

FROM debian:bookworm-slim AS final
ADD --checksum=sha256:24454f830cdb571e2c4ad15481119c43b3cafd48dd869a9b2945d1036d1dc68d \
    https://artifacts.example/certs/zscaler-root-ca.crt /usr/local/share/ca-certificates/zscaler-root-ca.crt
RUN apt-get update && \
    apt-get install -y ca-certificates && \
    update-ca-certificates
WORKDIR /app
COPY --from=build /build/output/bin .
ENTRYPOINT \["/app/bin"\]

https://docs.docker.com/guides/zscaler/#conclusion

Embedding the Zscaler root certificate directly into your Docker images ensures that containers run smoothly within Zscaler-proxied environments. By using this approach, you reduce potential runtime errors and create a consistent, auditable configuration that allows for smooth Docker operations within a monitored network.

Edit this page

https://github.com/docker/docs/edit/main/content/guides/zscaler/index.md

Request changes

https://github.com/docker/docs/issues/new?template=doc\_issue.yml&location=https%3a%2f%2fdocs.docker.com%2fguides%2fzscaler%2f&labels=status%2Ftriage

Table of contents

The role of certificates in Docker

https://docs.docker.com/guides/zscaler/#the-role-of-certificates-in-docker

Configure Zscaler proxy for Docker Desktop

https://docs.docker.com/guides/zscaler/#configure-zscaler-proxy-for-docker-desktop

Install root certificates in Docker images

https://docs.docker.com/guides/zscaler/#install-root-certificates-in-docker-images

Obtaining the root certificate

https://docs.docker.com/guides/zscaler/#obtaining-the-root-certificate

Building with the certificate

https://docs.docker.com/guides/zscaler/#building-with-the-certificate

https://docs.docker.com/guides/zscaler/#conclusion

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

