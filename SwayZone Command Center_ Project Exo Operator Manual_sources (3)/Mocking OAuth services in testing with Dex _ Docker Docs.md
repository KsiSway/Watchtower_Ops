---
sourceFile: "Mocking OAuth services in testing with Dex | Docker Docs"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.663Z"
---

# Mocking OAuth services in testing with Dex | Docker Docs

c9c19747-6575-429b-874b-9f8759fad36d

Mocking OAuth services in testing with Dex | Docker Docs

920d4b91-4891-41d9-b19e-1d3cf08a9d9f

https://docs.docker.com/guides/dex/

Mocking OAuth services in testing with Dex | Docker Docs

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

Mocking OAuth services in testing with Dex

https://docs.docker.com/guides/dex/

Mocking OAuth services in testing with Dex

App development Distributed systems

« Back to all guides

https://docs.docker.com/guides/

https://docs.docker.com/

https://docs.docker.com/guides/

/ Mocking OAuth services with Dex

Mocking OAuth services in testing with Dex

Ask Gordon Copy Markdown View Markdown

Table of contents

Using Dex with Docker

https://docs.docker.com/guides/dex/#using-dex-with-docker

Prerequisites

https://docs.docker.com/guides/dex/#prerequisites

Setting Up Dex with Docker

https://docs.docker.com/guides/dex/#setting-up-dex-with-docker

Using Dex OAuth testing in GHA

https://docs.docker.com/guides/dex/#using-dex-oauth-testing-in-gha

https://docs.docker.com/guides/dex/#conclusion

Dex is an open-source OpenID Connect (OIDC) and OAuth 2.0 identity provider that can be configured to authenticate against various backend identity providers, such as LDAP, SAML, and OAuth. Running Dex in a Docker container allows developers to simulate an OAuth 2.0 server for testing and development purposes. This guide will walk you through setting up Dex as an OAuth mock server using Docker containers.

Nowadays OAuth is the preferred choice to authenticate in web services, the highest part of them give the possibility to access using popular OAuth services like GitHub, Google or Apple. Using OAuth guarantees a higher level of security and simplification since it is not necessary to create new profiles for each service. This means that, by allowing applications to access resources on behalf of users without sharing passwords, OAuth minimizes the risk of credential exposure.

#### In this guide, you'll learn how to:

Use Docker to launch up a Dex container.

Use mock OAuth in the GitHub Action (GHA) without relying on an external OAuth provider.

Using Dex with Docker

https://docs.docker.com/guides/dex/#using-dex-with-docker

The official

Docker image for Dex

https://hub.docker.com/r/dexidp/dex/

provides a convenient way to deploy and manage Dex instances. Dex is available for various CPU architectures, including amd64, armv7, and arm64, ensuring compatibility with different devices and platforms. You can learn more about Dex standalone on the

Dex docs site

https://dexidp.io/docs/getting-started/

Prerequisites

https://docs.docker.com/guides/dex/#prerequisites

Docker Compose

https://docs.docker.com/compose/

: Recommended for managing multi-container Docker applications.

Setting Up Dex with Docker

https://docs.docker.com/guides/dex/#setting-up-dex-with-docker

#### Begin by creating a directory for your Dex project:

mkdir dex-mock-server
cd dex-mock-server

#### Organize your project with the following structure:

dex-mock-server/
├── config.yaml
└── compose.yaml

Create the Dex Configuration File: The config.yaml file defines Dex's settings, including connectors, clients, and storage. For a mock server setup, you can use the following minimal configuration:

# config.yaml
issuer: http://localhost:5556/dex
storage:
  type: memory
web:
  http: 0.0.0.0:5556
staticClients:
  - id: example-app
    redirectURIs:
      - 'http://localhost:5555/callback'
    name: 'Example App'
    secret: ZXhhbXBsZS1hcHAtc2VjcmV0
enablePasswordDB: true
staticPasswords:
  - email: "admin@example.com"
    hash: "$2a$10$2b2cU8CPhOTaGrs1HRQuAueS7JTT5ZHsHSzYiFPm1leZck7Mc8T4W"
    username: "admin"
    userID: "1234"

#### Explanation:

issuer: The public URL of Dex.

storage: Using in-memory storage for simplicity.

web: Dex will listen on port 5556.

staticClients: Defines a client application (example-app) with its redirect URI and secret.

enablePasswordDB: Enables static password authentication.

staticPasswords: Defines a static user for authentication. The hash is a bcrypt hash of the password.

Ensure the hash is a valid bcrypt hash of your desired password. You can generate this using tools like

bcrypt-generator.com

https://bcrypt-generator.com/

. or use CLI tools like

https://httpd.apache.org/docs/2.4/programs/htpasswd.html

like in this following example:

echo password | htpasswd -BinC 10 admin | cut -d: -f2

#### With Docker Compose configured, start Dex:

# compose.yaml

services:
  dex:
    image: dexidp/dex:latest
    container\_name: dex
    ports:
      - "5556:5556"
    volumes:
      - ./config.yaml:/etc/dex/config.yaml
    command: \["dex", "serve", "/etc/dex/config.yaml"\]

Now it is possible to run the container using the

docker compose

docker compose up -d

This command will download the Dex Docker image (if not already available) and start the container in detached mode.

To verify that Dex is running, check the logs to ensure Dex started successfully:

docker compose logs -f dex

You should see output indicating that Dex is listening on the specified port.

Using Dex OAuth testing in GHA

https://docs.docker.com/guides/dex/#using-dex-oauth-testing-in-gha

To test the OAuth flow, you'll need a client application configured to authenticate against Dex. One of the most typical use cases is to use it inside GitHub Actions. Since Dex supports mock authentication, you can predefine test users as suggested in the

https://dexidp.io/docs

config.yaml

file should looks like:

issuer: http://127.0.0.1:5556/dex

storage:
  type: memory

web:
  http: 0.0.0.0:5556

oauth2:
  skipApprovalScreen: true

staticClients:
  - name: TestClient
    id: client\_test\_id
    secret: client\_test\_secret
    redirectURIs:
      - http://{ip-your-app}/path/to/callback/ # example: http://localhost:5555/callback

connectors:
# mockCallback connector always returns the user 'kilgore@kilgore.trout'.
- type: mockCallback
  id: mock
  name: Mock

Now you can insert the Dex service inside your

~/.github/workflows/ci.yaml

\[...\]
jobs:
  test-oauth:
    runs-on: ubuntu-latest
    steps:
      - name: Install Dex
        run: |
          curl -L https://github.com/dexidp/dex/releases/download/v2.37.0/dex\_linux\_amd64 -o dex
          chmod +x dex

      - name: Start Dex Server
        run: |
          nohup ./dex serve config.yaml > dex.log 2>&1 &
          sleep 5  # Give Dex time to start
\[...\]

https://docs.docker.com/guides/dex/#conclusion

By following this guide, you've set up Dex as an OAuth mock server using Docker. This setup is invaluable for testing and development, allowing you to simulate OAuth flows without relying on external identity providers. For more advanced configurations and integrations, refer to the

Dex documentation

https://dexidp.io/docs/

Edit this page

https://github.com/docker/docs/edit/main/content/guides/dex.md

Request changes

https://github.com/docker/docs/issues/new?template=doc\_issue.yml&location=https%3a%2f%2fdocs.docker.com%2fguides%2fdex%2f&labels=status%2Ftriage

Table of contents

Using Dex with Docker

https://docs.docker.com/guides/dex/#using-dex-with-docker

Prerequisites

https://docs.docker.com/guides/dex/#prerequisites

Setting Up Dex with Docker

https://docs.docker.com/guides/dex/#setting-up-dex-with-docker

Using Dex OAuth testing in GHA

https://docs.docker.com/guides/dex/#using-dex-oauth-testing-in-gha

https://docs.docker.com/guides/dex/#conclusion

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

