---
sourceFile: "Devvit Web | Reddit for Developers"
exportedBy: "Kortex"
exportDate: "2026-05-20T06:50:17.333Z"
---

# Devvit Web | Reddit for Developers

56be9497-ccab-4d48-ac07-b3b9907b1191

Devvit Web | Reddit for Developers

6fc18b6b-d3f3-4186-8385-24374fbbde84

https://developers.reddit.com/docs/capabilities/devvit-web/devvit\_web\_overview

Devvit Web | Reddit for Developers

Skip to main content

https://developers.reddit.com/docs/capabilities/devvit-web/devvit\_web\_overview#\_\_docusaurus\_skipToContent\_fallback

https://developers.reddit.com/docs/capabilities/devvit-web/devvit\_web\_overview

https://developers.reddit.com/docs/next/capabilities/devvit-web/devvit\_web\_overview

https://developers.reddit.com/docs/capabilities/devvit-web/devvit\_web\_overview

https://developers.reddit.com/docs/0.11

https://developers.reddit.com/docs/capabilities/devvit-web/devvit\_web\_overview

← Back to main menu

Introduction

Welcome to Devvit

https://developers.reddit.com/docs/

Devvit Technical Overview

https://developers.reddit.com/docs/capabilities/devvit-web/devvit\_web\_overview

App Showcase

https://developers.reddit.com/docs/examples/app-showcase

Build Your App

Build Games

https://developers.reddit.com/docs/capabilities/devvit-web/devvit\_web\_overview

Build Mod Tools

https://developers.reddit.com/docs/capabilities/devvit-web/devvit\_web\_overview

Launch Your App

Launch Guide

https://developers.reddit.com/docs/guides/launch/launch-guide

Feature Guide

https://developers.reddit.com/docs/guides/launch/feature-guide

Reddit Developer Funds

https://support.reddithelp.com/hc/en-us/articles/27958169342996-Reddit-Developer-Funds-2025-Terms

Capabilities

Devvit Setup Overview

https://developers.reddit.com/docs/capabilities/devvit-web/devvit\_web\_overview

Automation & Triggers

https://developers.reddit.com/docs/capabilities/devvit-web/devvit\_web\_overview

https://developers.reddit.com/docs/capabilities/http-fetch

In-App Purchases

https://developers.reddit.com/docs/capabilities/devvit-web/devvit\_web\_overview

Post Creation & Navigation

https://developers.reddit.com/docs/capabilities/devvit-web/devvit\_web\_overview

Realtime Apps

https://developers.reddit.com/docs/capabilities/devvit-web/devvit\_web\_overview

https://developers.reddit.com/docs/capabilities/devvit-web/devvit\_web\_overview

Saving Data

https://developers.reddit.com/docs/capabilities/devvit-web/devvit\_web\_overview

https://developers.reddit.com/docs/capabilities/devvit-web/devvit\_web\_overview

Best Practices

https://developers.reddit.com/docs/capabilities/devvit-web/devvit\_web\_overview

Development Tools

https://developers.reddit.com/docs/capabilities/devvit-web/devvit\_web\_overview

Migration Guides

https://developers.reddit.com/docs/capabilities/devvit-web/devvit\_web\_overview

Template Library

https://developers.reddit.com/docs/examples/template-library

Using AI Tools

https://developers.reddit.com/docs/guides/ai

https://developers.reddit.com/docs/guides/faq

https://developers.reddit.com/docs/changelog

Devvit Rules

https://developers.reddit.com/docs/devvit\_rules

https://developers.reddit.com/discord

https://www.reddit.com/r/Devvit

Devvit Technical Overview

On this page

Devvit Web includes an easy way to build Devvit apps using a standard web stack.

https://developers.reddit.com/docs/capabilities/devvit-web/devvit\_web\_overview#what-it-is

Devvit Web allows developers to build Devvit apps just like you would for the web. At the core, Devvit Web provides:

A standard web app

that allows you to build with industry-standard frameworks and technologies (like React, Three.js, or Phaser).

Server endpoints

that you define to communicate between the webview client and the Devvit server, using industry-standard frameworks and technologies (like Express.js, Hono, Koa, etc.).

Devvit configuration

with a traditional client/server split. Devvit capabilities are now in one of three places:

A configuration file in devvit.json for defining app metadata, permissions, and capabilities

Client capabilities in the @devvit/client SDK

Server capabilities, like Redis and Reddit API with the @devvit/server SDK

With Devvit Web, you have continued access to our hosting services, key capabilities like Redis and Reddit API, standard web technologies, and a typical client/server pattern to build your apps.

In addition, since you're working with standard web technologies your apps should work with AI tools more effectively.

https://developers.reddit.com/docs/capabilities/devvit-web/devvit\_web\_overview#examples

https://developers.reddit.com/new

https://developers.reddit.com/new

and choose one of our templates or take a look at the github repositories:

https://github.com/reddit/devvit-template-react

https://github.com/reddit/devvit-template-phaser

https://github.com/reddit/devvit-template-threejs

Hello World

https://github.com/reddit/devvit-template-hello-world

Limitations

https://developers.reddit.com/docs/capabilities/devvit-web/devvit\_web\_overview#limitations

As with most experimental features, there are some caveats.

What it means

Serverless endpoints

The node server will run just long enough to execute your endpoint function and return a response, which means you can't use packages that require long-running connections like streaming.

Package limitations

Developers cannot use

or external native packages. For now, we recommend using external services over the native dependencies, such as

https://streampot.io/

(instead of ffmpeg) and

https://platform.openai.com/docs/guides/embeddings

(instead of @xenova/transformers) .

Single request and single response handling only

Streaming or chunked responses and websockets are not supported. Long-polling is supported if it's under the max request time.

No external requests from your client

You can't have any external requests other than the app's webview domain. All backend responses are locked down to the webview domain via CSP. (Your backend can make external fetch requests though.)

localStorage clears on app updates

The iframe URL changes with each app version, so

localStorage

data is lost when you publish an update. Use

https://developers.reddit.com/docs/capabilities/server/redis

for data that needs to persist across app versions.

#### Devvit Web still has the same technical requirements:

Server endpoint calls

Max request time: 30s

Max payload size: 4MB

Max response size: 10MB

HTML/CSS/JS only

Devvit Web components

https://developers.reddit.com/docs/capabilities/devvit-web/devvit\_web\_overview#devvit-web-components

Devvit Web uses endpoints between the client and server to make communication similar to standard web apps. A Devvit Web app has three components:

Configuration

#### Devvit Web templates all have the same file structure:

.
├── src/
│   ├── client/     # contains the webview code
│   └── server/     # endpoints for the client
└── devvit.json     # the devvit config file

Your client talks to the server by calling

endpoints you define with

Client folder

https://developers.reddit.com/docs/capabilities/devvit-web/devvit\_web\_overview#client-folder

This folder includes client-side code. This includes any html/css/javascript and relevant web libraries, and it will appear in a webview inside of a post for Reddit users.

When you want to make server-side calls, or use server-side capabilities, you'll use fetch and define what happens in your server folder.

Server folder

https://developers.reddit.com/docs/capabilities/devvit-web/devvit\_web\_overview#server-folder

This folder includes server-side code. We provide a node server, and you can use typical node server frameworks like Hono, Koa, or Express. This is where you can access key capabilities like

https://developers.reddit.com/docs/capabilities/server/redis

, Reddit API client, and

https://developers.reddit.com/docs/capabilities/server/http-fetch

We also provide an authentication middleware so you don't have to worry about authentication.

All server endpoints must start with

/api/get-something

/api/widgets/42

Configuration in

devvit.json

https://developers.reddit.com/docs/capabilities/devvit-web/devvit\_web\_overview#configuration-in-devvitjson

devvit.json

is the configuration file for Devvit apps. It defines an app's post configuration, Node.js server configuration, permissions, scheduled jobs, event triggers, menu entries, payments configuration, and project settings.

devvit.json

replaces the legacy

devvit.yaml

configuration. A project should have one or the other but not both.

Learn more about

devvit.json

https://developers.reddit.com/docs/capabilities/devvit-web/devvit\_web\_configuration

Previous Welcome to Devvit

https://developers.reddit.com/docs/

Next App Showcase

https://developers.reddit.com/docs/examples/app-showcase

https://developers.reddit.com/docs/blog

The Reddit Developer Fund

https://support.reddithelp.com/hc/en-us/articles/27958169342996-Reddit-Developer-Funds-2025-Terms

https://www.reddit.com/r/devvit

r/GamesOnReddit

https://www.reddit.com/r/GamesOnReddit

Join our Discord

https://developers.reddit.com/discord

Reddit, Inc. © 2026. Built with Docusaurus.

