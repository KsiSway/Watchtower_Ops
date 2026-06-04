---
sourceFile: "HTTP routing with Traefik | Docker Docs"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.482Z"
---

# HTTP routing with Traefik | Docker Docs

44f7cd93-2bf7-4f2a-90c7-07271560e412

HTTP routing with Traefik | Docker Docs

5b1bdd82-0526-4fe3-8ab0-1cb726e886f5

https://docs.docker.com/guides/traefik/

HTTP routing with Traefik | Docker Docs

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

HTTP routing with Traefik

https://docs.docker.com/guides/traefik/

Use Traefik to easily route traffic between multiple containers or non-containerized workloads

Networking Docker Hardened Images

« Back to all guides

https://docs.docker.com/guides/

https://docs.docker.com/

https://docs.docker.com/guides/

/ HTTP routing with Traefik

HTTP routing with Traefik

Ask Gordon Copy Markdown View Markdown

Table of contents

Introduction

https://docs.docker.com/guides/traefik/#introduction

Prerequisites

https://docs.docker.com/guides/traefik/#prerequisites

Using Traefik with Docker

https://docs.docker.com/guides/traefik/#using-traefik-with-docker

Using Traefik in development

https://docs.docker.com/guides/traefik/#using-traefik-in-development

Sending traffic to non-containerized workloads

https://docs.docker.com/guides/traefik/#sending-traffic-to-non-containerized-workloads

Starting the example app

https://docs.docker.com/guides/traefik/#starting-the-example-app

https://docs.docker.com/guides/traefik/#recap

Introduction

https://docs.docker.com/guides/traefik/#introduction

During local development, it's quite common to need to run multiple HTTP services. You might have both an API and a frontend app, a WireMock service to mock data endpoints, or a database visualizer (such as phpMyAdmin or pgAdmin). In many development setups, these services are exposed on different ports, which then requires you to remember what's on what port but can also introduce other problems (such as CORS).

A reverse proxy can dramatically simplify this setup by being the single exposed service and then routing requests to the appropriate service based on the request URL (either by path or hostname).

https://traefik.io/traefik/

is a modern, cloud-native reverse proxy and load balancer that makes developing and deploying multi-service applications easier. This guide will show you how to use Traefik with Docker to enhance your development environment.

#### In this guide, you will learn how to:

Start Traefik with Docker

Configure routing rules to split traffic between two containers

Use Traefik in a containerized development environment

Use Traefik to send requests to non-containerized workloads

Prerequisites

https://docs.docker.com/guides/traefik/#prerequisites

The following prerequisites are required to follow along with this how-to guide:

Docker Desktop

https://www.docker.com/products/docker-desktop/

https://nodejs.org/en/download/package-manager

https://yarnpkg.com/

Basic of Docker

Using Traefik with Docker

https://docs.docker.com/guides/traefik/#using-traefik-with-docker

One of the unique features of Traefik is its ability to be configured in many ways. When using the Docker provider, Traefik gets its configuration from other running containers using

https://docs.docker.com/config/labels-custom-metadata/

. Traefik will watch engine events (for container starts and stops), extract the labels, and update its configuration.

While there are

many Traefik-monitored labels

https://doc.traefik.io/traefik/routing/providers/docker/

, the two most common will be:

traefik.http.routers.<service-name>.rule

- used to indicate the routing rule (

view all of the available rules here

https://doc.traefik.io/traefik/routing/routers/#rule

traefik.http.services.<service-name>.loadbalancer.server.port

- indicates the port Traefik should forward the request to. Note that this container port does not need to be exposed on your host machine (

read about port detection here

https://doc.traefik.io/traefik/providers/docker/#port-detection

Let's do a quick demo of starting Traefik and then configuring two additional containers to be accessible using different hostnames.

In order for two containers to be able to communicate with each other, they need to be on the same network. Create a network named

traefik-demo

docker network create

$ docker network create traefik-demo

Start a Traefik container using one of the following methods. These commands exposes Traefik on port 80, mounts the Docker socket (which is used to monitor containers to update configuration), and passes the

--providers.docker

argument to configure Traefik to use the Docker provider. Using Docker Hardened Images Using the official image Docker Hardened Images (DHI) for Traefik are available on

https://hub.docker.com/hardened-images/catalog/dhi/traefik

. If you haven't authenticated yet, first run:

$ docker login dhi.io

#### Then start a container using the Hardened image:

$ docker run -d --network=traefik-demo \
  -p 80:80 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  dhi.io/traefik:3.6.2 \
  --providers.docker

#### You can also use the official image from Docker Hub:

$ docker run -d --network=traefik-demo \
  -p 80:80 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  traefik:v3.6.2 \
  --providers.docker

Now, start a simple Nginx container and define the labels Traefik is watching for to configure the HTTP routing. Note that the Nginx container is not exposing any ports. Using Docker Hardened Images Using the official image Docker Hardened Images (DHI) for Nginx are available on

Nginx DHI image

https://hub.docker.com/hardened-images/catalog/dhi/nginx

. If you haven't authenticated yet, first run:

$ docker login dhi.io

$ docker run -d --network=traefik-demo \
  --label 'traefik.http.routers.nginx.rule=Host(\`nginx.localhost\`)' \
  dhi.io/nginx:1.29.3

#### You can also run the official Nginx image as follows:

$ docker run -d --network=traefik-demo \
  --label 'traefik.http.routers.nginx.rule=Host(\`nginx.localhost\`)' \
  nginx:1.29.3

Once the container starts, open your browser to

http://nginx.localhost

http://nginx.localhost/

to see the app (all Chromium-based browsers route \*.localhost requests locally with no additional setup).

4. Start a second application that will use a different hostname.

$ docker run -d --network=traefik-demo --label 'traefik.http.routers.welcome.rule=Host(\`welcome.localhost\`)' docker/welcome-to-docker

Once the container starts, open your browser to

http://welcome.localhost

http://welcome.localhost/

. You should see a “Welcome to Docker” website.

Using Traefik in development

https://docs.docker.com/guides/traefik/#using-traefik-in-development

Now that you've experienced Traefik, it's time to try using it in a development environment. In this example, you will use a sample application that has a split frontend and backend. This app stack has the following configuration:

All requests to /api to go to the API service

All other requests to localhost go to the frontend client

Since the app uses MySQL, db.localhost should provide phpMyAdmin to make it easy to access the database during development

The application can be accessed on GitHub at

dockersamples/easy-http-routing-with-traefik

https://github.com/dockersamples/easy-http-routing-with-traefik

compose.yaml

file, Traefik is using the following configuration: Using DHI image Using official image

services:
  proxy:
    image: dhi.io/traefik:3.6.2
    command: --providers.docker
    ports:
      - 80:80
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock

services:
  proxy:
    image: traefik:v3.6.2
    command: --providers.docker
    ports:
      - 80:80
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock

Note that this is essentially the same configuration as used earlier, but now in a Compose syntax.

2. The client service has the following configuration, which will start the container and provide it with the labels to receive requests at localhost. Using Docker Hardened Images Using the official image Docker Hardened Images (DHI) for Nginx are available on

Nginx DHI image

https://hub.docker.com/hardened-images/catalog/dhi/nginx

. If you haven't authenticated yet, first run:

$ docker login dhi.io

#### You can use it as your base image as shown following:

services:
  # …
  client:
    image: dhi.io/nginx:1.29.3-alpine3.21
    volumes:
      - "./client:/usr/share/nginx/html"
    labels:
      traefik.http.routers.client.rule: "Host(\`localhost\`)"

services:
  # …
  client:
    image: nginx:1.29.3-alpine3.22
    volumes:
      - "./client:/usr/share/nginx/html"
    labels:
      traefik.http.routers.client.rule: "Host(\`localhost\`)"

The api service has a similar configuration, but you'll notice the routing rule has two conditions - the host must be “localhost” and the URL path must have a prefix of “/api”. Since this rule is more specific, Traefik will evaluate it first compared to the client rule.

services:
  # …
  api:
    build: ./dev/api
    volumes:
      - "./api:/var/www/html/api"
    labels:
      traefik.http.routers.api.rule: "Host(\`localhost\`) && PathPrefix(\`/api\`)"

And finally, the

service is configured to receive requests for the hostname “db.localhost”. The service also has environment variables defined to automatically log in, making it a little easier to get into the app.

services:
  # …
  phpmyadmin:
    image: phpmyadmin:5.2.1
    labels:
      traefik.http.routers.db.rule: "Host(\`db.localhost\`)"
    environment:
      PMA\_USER: root
      PMA\_PASSWORD: password

Before starting the stack, stop the Nginx container if it is still running. And that's it. Now, you only need to spin up the Compose stack with a

docker compose up

and all of the services and applications will be ready for development.

Sending traffic to non-containerized workloads

https://docs.docker.com/guides/traefik/#sending-traffic-to-non-containerized-workloads

In some situations, you may want to forward requests to applications not running in containers. In the following architecture diagram, the same application from before is used, but the API and React apps are now running natively on the host machine.

To accomplish this, Traefik will need to use another method to configure itself. The

File provider

https://doc.traefik.io/traefik/providers/file/

lets you define the routing rules in a YAML document. Here is an example file:

http:
  routers:
    native-api:
      rule: "Host(\`localhost\`) && PathPrefix(\`/api\`)"
      service: native-api
    native-client:
      rule: "Host(\`localhost\`)"
      service: native-client

  services:
    native-api:
      loadBalancer:
        servers:
          - url: "http://host.docker.internal:3000/"
    native-client:
      loadBalancer:
        servers:
          - url: "http://host.docker.internal:5173/"

This configuration indicates that requests that for

localhost/api

will be forwarded to a service named

, which then forwards the request to

http://host.docker.internal:3000

http://host.docker.internal:3000/

. The hostname

host.docker.internal

is a name that Docker Desktop provides to send requests to the host machine.

With this file, the only change is to the Compose configuration for Traefik. There are specifically two things that have changed:

The configuration file is mounted into the Traefik container (the exact destination path is up to you)

is updated to add the file provider and point to the location of the configuration file

Using DHI image Using official image

services:
  proxy:
    image: dhi.io/traefik:3.6.2
    command: --providers.docker --providers.file.filename=/config/traefik-config.yaml --api.insecure
    ports:
      - 80:80
      - 8080:8080
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - ./dev/traefik-config.yaml:/config/traefik-config.yaml

services:
  proxy:
    image: traefik:v3.6.2
    command: --providers.docker --providers.file.filename=/config/traefik-config.yaml --api.insecure
    ports:
      - 80:80
      - 8080:8080
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - ./dev/traefik-config.yaml:/config/traefik-config.yaml

Starting the example app

https://docs.docker.com/guides/traefik/#starting-the-example-app

To run the example app that forwards requests from Traefik to native-running apps, use the following steps:

If you have the Compose stack still running, stop it with the following command:

$ docker compose down

Start the application using the provided

compose-native.yaml

$ docker compose -f compose-native.yaml up

http://localhost

http://localhost/

will return a 502 Bad Gateway because the other apps aren't running yet.

3. Start the API by running the following steps:

cd api
yarn install
yarn dev

Start the frontend by running the following steps in a new terminal (starting from the root of the project):

cd client
yarn install
yarn dev

Open the app at

http://localhost

http://localhost/

. You should see an app that fetches a message from

http://localhost/api/messages

http://localhost/api/messages

. You can also open

http://db.localhost

http://db.localhost/

to view or adjust the available messages directly from the Mongo database. Traefik will ensure the requests are properly routed to the correct container or application.

When you're done, run

docker compose down

to stop the containers and stop the Yarn apps by hitting

https://docs.docker.com/guides/traefik/#recap

Running multiple services doesn't have to require tricky port configuration and a good memory. With tools like Traefik, it's easy to launch the services you need and easily access them - whether they're for the app itself (such as the frontend and backend) or for additional development tooling (such as phpMyAdmin).

Edit this page

https://github.com/docker/docs/edit/main/content/guides/traefik.md

Request changes

https://github.com/docker/docs/issues/new?template=doc\_issue.yml&location=https%3a%2f%2fdocs.docker.com%2fguides%2ftraefik%2f&labels=status%2Ftriage

Table of contents

Introduction

https://docs.docker.com/guides/traefik/#introduction

Prerequisites

https://docs.docker.com/guides/traefik/#prerequisites

Using Traefik with Docker

https://docs.docker.com/guides/traefik/#using-traefik-with-docker

Using Traefik in development

https://docs.docker.com/guides/traefik/#using-traefik-in-development

Sending traffic to non-containerized workloads

https://docs.docker.com/guides/traefik/#sending-traffic-to-non-containerized-workloads

Starting the example app

https://docs.docker.com/guides/traefik/#starting-the-example-app

https://docs.docker.com/guides/traefik/#recap

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

Search this site Results will appear as you type Clear

Start typing to search the documentation

