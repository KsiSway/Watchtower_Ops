---
sourceFile: "Instrumenting a JavaScript App with OpenTelemetry | Docker Docs"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.500Z"
---

# Instrumenting a JavaScript App with OpenTelemetry | Docker Docs

5eeada76-4521-4473-934e-695ec3716a00

Instrumenting a JavaScript App with OpenTelemetry | Docker Docs

c85068b2-22a3-4e3c-a5db-3fc6b1d5cbd4

https://docs.docker.com/guides/opentelemetry/

Instrumenting a JavaScript App with OpenTelemetry | Docker Docs

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

Instrumenting a JavaScript App with OpenTelemetry

https://docs.docker.com/guides/opentelemetry/

Learn how to instrument a JavaScript application using OpenTelemetry in a Dockerized environment.

JavaScript App development Observability

« Back to all guides

https://docs.docker.com/guides/

https://docs.docker.com/

https://docs.docker.com/guides/

/ Instrumenting JS Apps with OpenTelemetry

Instrumenting a JavaScript App with OpenTelemetry

Ask Gordon Copy Markdown View Markdown

Table of contents

Using OpenTelemetry with Docker

https://docs.docker.com/guides/opentelemetry/#using-opentelemetry-with-docker

Prerequisites

https://docs.docker.com/guides/opentelemetry/#prerequisites

Project Structure

https://docs.docker.com/guides/opentelemetry/#project-structure

Create a Simple Node.js App

https://docs.docker.com/guides/opentelemetry/#create-a-simple-nodejs-app

Configure OpenTelemetry Tracing

https://docs.docker.com/guides/opentelemetry/#configure-opentelemetry-tracing

Configure the OpenTelemetry Collector

https://docs.docker.com/guides/opentelemetry/#configure-the-opentelemetry-collector

Add Docker Compose Configuration

https://docs.docker.com/guides/opentelemetry/#add-docker-compose-configuration

Start the Stack

https://docs.docker.com/guides/opentelemetry/#start-the-stack

Verify Traces in Jaeger

https://docs.docker.com/guides/opentelemetry/#verify-traces-in-jaeger

https://docs.docker.com/guides/opentelemetry/#conclusion

OpenTelemetry (OTel) is an open-source observability framework that provides a set of APIs, SDKs, and tools for collecting telemetry data, such as metrics, logs, and traces, from applications. With OpenTelemetry, developers can obtain valuable insights into how their services perform in production or during local development.

A key component of OpenTelemetry is the OpenTelemetry Protocol (OTLP) a general-purpose, vendor-agnostic protocol designed to transmit telemetry data efficiently and reliably. OTLP supports multiple data types (traces, metrics, logs) over HTTP or gRPC, making it the default and recommended protocol for communication between instrumented applications, the OpenTelemetry Collector, and backends such as Jaeger or Prometheus.

This guide walks you through how to instrument a simple Node.js application with OpenTelemetry and run both the app and a collector using Docker. This setup is ideal for local development and testing observability before integrating with external observability platforms like Prometheus, Jaeger, or Grafana.

#### In this guide, you'll learn how to:

How to set up OpenTelemetry in a Node.js app.

How to run an OpenTelemetry Collector in Docker.

How to visualize traces with Jaeger.

How to use Docker Compose to manage the full observability stack.

Using OpenTelemetry with Docker

https://docs.docker.com/guides/opentelemetry/#using-opentelemetry-with-docker

Docker Official Image for OpenTelemetry

https://hub.docker.com/r/otel/opentelemetry-collector-contrib

provides a convenient way to deploy and manage Dex instances. OpenTelemetry is available for various CPU architectures, including amd64, armv7, and arm64, ensuring compatibility with different devices and platforms. Same for the

Jaeger Docker image

https://hub.docker.com/r/jaegertracing/jaeger

Prerequisites

https://docs.docker.com/guides/opentelemetry/#prerequisites

Docker Compose

https://docs.docker.com/compose/

: Recommended for managing multi-container Docker applications.

Basic knowledge of Node.js and Docker.

Project Structure

https://docs.docker.com/guides/opentelemetry/#project-structure

#### Create the project directory:

mkdir otel-js-app
cd otel-js-app

otel-js-app/
├── docker-compose.yaml
├── collector-config.yaml
├── app/
│   ├── package.json
│   ├── app.js
│   └── tracer.js

Create a Simple Node.js App

https://docs.docker.com/guides/opentelemetry/#create-a-simple-nodejs-app

#### Initialize a basic Node.js app:

mkdir app && cd app
npm init -y
npm install express @opentelemetry/api @opentelemetry/sdk-node \
            @opentelemetry/auto-instrumentations-node \
            @opentelemetry/exporter-trace-otlp-http

#### Now, add the application logic:

// app/app.js
const express = require('express');
require('./tracer'); // Initialize OpenTelemetry

const app = express();

app.get('/', (req, res) => {
  res.send('Hello from OpenTelemetry demo app!');
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(\`App listening at http://localhost:${PORT}\`);
});

Configure OpenTelemetry Tracing

https://docs.docker.com/guides/opentelemetry/#configure-opentelemetry-tracing

#### Create the tracer configuration file:

// app/tracer.js
const { NodeSDK } = require('@opentelemetry/sdk-node');
const { getNodeAutoInstrumentations } = require('@opentelemetry/auto-instrumentations-node');
const { OTLPTraceExporter } = require('@opentelemetry/exporter-trace-otlp-http');

const sdk = new NodeSDK({
  traceExporter: new OTLPTraceExporter({
    url: 'http://collector:4318/v1/traces',
  }),
  instrumentations: \[getNodeAutoInstrumentations()\],
});

sdk.start();

Configure the OpenTelemetry Collector

https://docs.docker.com/guides/opentelemetry/#configure-the-opentelemetry-collector

#### Create a collector-config.yaml file at the root:

# collector-config.yaml
receivers:
  otlp:
    protocols:
      http:

exporters:
  logging:
    loglevel: debug
  jaeger:
    endpoint: jaeger:14250
    tls:
      insecure: true

service:
  pipelines:
    traces:
      receivers: \[otlp\]
      exporters: \[logging, jaeger\]

Add Docker Compose Configuration

https://docs.docker.com/guides/opentelemetry/#add-docker-compose-configuration

docker-compose.yaml

version: '3.9'

services:
  app:
    build: ./app
    ports:
      - "3000:3000"
    environment:
      - NODE\_ENV=development
    depends\_on:
      - collector

  collector:
    image: otel/opentelemetry-collector:latest
    volumes:
      - ./collector-config.yaml:/etc/otelcol/config.yaml
    command: \["--config=/etc/otelcol/config.yaml"\]
    ports:
      - "4318:4318" # OTLP

  jaeger:
    image: jaegertracing/all-in-one:latest
    ports:
      - "16686:16686" # UI
      - "14250:14250" # Collector gRPC

Now, add the

# app/Dockerfile
FROM node:18

WORKDIR /usr/src/app
COPY . .
RUN npm install

CMD \["node", "app.js"\]

Start the Stack

https://docs.docker.com/guides/opentelemetry/#start-the-stack

#### Start all services with Docker Compose:

docker compose up --build

#### Once the services are running:

Visit your app at

http://localhost:3000

http://localhost:3000/

View traces at

http://localhost:16686

http://localhost:16686/

in the Jaeger UI

Verify Traces in Jaeger

https://docs.docker.com/guides/opentelemetry/#verify-traces-in-jaeger

After visiting your app's root endpoint, open Jaeger's UI, search for the service (default is usually

unknown\_service

unless explicitly named), and check the traces.

You should see spans for the HTTP request, middleware, and auto-instrumented libraries.

https://docs.docker.com/guides/opentelemetry/#conclusion

You now have a fully functional OpenTelemetry setup using Docker Compose. You've instrumented a basic JavaScript app to export traces and visualized them using Jaeger. This architecture is extendable for more complex applications and observability pipelines using Prometheus, Grafana, or cloud-native exporters.

For advanced topics such as custom span creation, metrics, and logs, consult the OpenTelemetry JavaScript docs.

Edit this page

https://github.com/docker/docs/edit/main/content/guides/opentelemetry.md

Request changes

https://github.com/docker/docs/issues/new?template=doc\_issue.yml&location=https%3a%2f%2fdocs.docker.com%2fguides%2fopentelemetry%2f&labels=status%2Ftriage

Table of contents

Using OpenTelemetry with Docker

https://docs.docker.com/guides/opentelemetry/#using-opentelemetry-with-docker

Prerequisites

https://docs.docker.com/guides/opentelemetry/#prerequisites

Project Structure

https://docs.docker.com/guides/opentelemetry/#project-structure

Create a Simple Node.js App

https://docs.docker.com/guides/opentelemetry/#create-a-simple-nodejs-app

Configure OpenTelemetry Tracing

https://docs.docker.com/guides/opentelemetry/#configure-opentelemetry-tracing

Configure the OpenTelemetry Collector

https://docs.docker.com/guides/opentelemetry/#configure-the-opentelemetry-collector

Add Docker Compose Configuration

https://docs.docker.com/guides/opentelemetry/#add-docker-compose-configuration

Start the Stack

https://docs.docker.com/guides/opentelemetry/#start-the-stack

Verify Traces in Jaeger

https://docs.docker.com/guides/opentelemetry/#verify-traces-in-jaeger

https://docs.docker.com/guides/opentelemetry/#conclusion

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

