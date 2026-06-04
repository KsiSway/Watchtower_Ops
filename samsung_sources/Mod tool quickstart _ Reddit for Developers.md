---
sourceFile: "Mod tool quickstart | Reddit for Developers"
exportedBy: "Kortex"
exportDate: "2026-05-20T06:50:17.459Z"
---

# Mod tool quickstart | Reddit for Developers

6614ac0d-f6a0-4092-8a0f-042231cffef7

Mod tool quickstart | Reddit for Developers

fcc0d4ba-39e6-4a10-97c3-b7a65700911a

https://developers.reddit.com/docs/quickstart/quickstart-mod-tool

Mod tool quickstart | Reddit for Developers

Skip to main content

https://developers.reddit.com/docs/quickstart/quickstart-mod-tool#\_\_docusaurus\_skipToContent\_fallback

https://developers.reddit.com/docs/quickstart/quickstart-mod-tool

https://developers.reddit.com/docs/next/quickstart/quickstart-mod-tool

https://developers.reddit.com/docs/quickstart/quickstart-mod-tool

https://developers.reddit.com/docs/0.11

https://developers.reddit.com/docs/quickstart/quickstart-mod-tool

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

https://developers.reddit.com/docs/quickstart/quickstart-mod-tool

Build Mod Tools

https://developers.reddit.com/docs/quickstart/quickstart-mod-tool

Introduction to Mod Tools

https://developers.reddit.com/docs/introduction/intro-mod-tools

Quickstart for Mod Tools

https://developers.reddit.com/docs/quickstart/quickstart-mod-tool

Launch Your App

Launch Guide

https://developers.reddit.com/docs/guides/launch/launch-guide

Feature Guide

https://developers.reddit.com/docs/guides/launch/feature-guide

Reddit Developer Funds

https://support.reddithelp.com/hc/en-us/articles/27958169342996-Reddit-Developer-Funds-2025-Terms

Capabilities

Devvit Setup Overview

https://developers.reddit.com/docs/quickstart/quickstart-mod-tool

Automation & Triggers

https://developers.reddit.com/docs/quickstart/quickstart-mod-tool

https://developers.reddit.com/docs/capabilities/http-fetch

In-App Purchases

https://developers.reddit.com/docs/quickstart/quickstart-mod-tool

Post Creation & Navigation

https://developers.reddit.com/docs/quickstart/quickstart-mod-tool

Realtime Apps

https://developers.reddit.com/docs/quickstart/quickstart-mod-tool

https://developers.reddit.com/docs/quickstart/quickstart-mod-tool

Saving Data

https://developers.reddit.com/docs/quickstart/quickstart-mod-tool

https://developers.reddit.com/docs/quickstart/quickstart-mod-tool

Best Practices

https://developers.reddit.com/docs/quickstart/quickstart-mod-tool

Development Tools

https://developers.reddit.com/docs/quickstart/quickstart-mod-tool

Migration Guides

https://developers.reddit.com/docs/quickstart/quickstart-mod-tool

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

Build Mod Tools

Quickstart for Mod Tools

On this page

Mod tool quickstart

Devvit allows you to build Mod Tools - subreddit-installed applications that help moderators of that community to take action on conversations, keeping their communities safe and engaged.

This tutorial should take about 10 minutes to complete. Once complete, you'll be able to run a version of

Comment Mop

https://developers.reddit.com/apps/comment-nuke

in your test subreddit from your own codebase.

What you'll need

https://developers.reddit.com/docs/quickstart/quickstart-mod-tool#what-youll-need

Node.JS (version 22.2.0+)

A code editor

Environment setup

https://developers.reddit.com/docs/quickstart/quickstart-mod-tool#environment-setup

Install Node.JS and NPM (

instructions

https://docs.npmjs.com/downloading-and-installing-node-js-and-npm

https://developers.reddit.com/new

https://developers.reddit.com/new

and choose Mod Tool under Other templates.

Go through the wizard. You will need to create a Reddit account and connect it to Reddit developers.

Follow the instructions on your terminal.

#### On success, you should see something like this:

Your Devvit authentication token has been saved to /Users/user.name/.devvit/token
Fetching and extracting the template...
Cutting the template to the target directory...
 🔧 Installing dependencies...
 🚀🚀🚀 Devvit app successfully initialized!
┌────────────────────────────────────────────────────┐
│ • \`cd my-app\` to open your project directory       │
│ • \`npm run dev\` to develop in your test community  │
└────────────────────────────────────────────────────┘

Understanding the template

https://developers.reddit.com/docs/quickstart/quickstart-mod-tool#understanding-the-template

This tutorial lets you build your own version of

Comment Mop

https://developers.reddit.com/apps/comment-nuke

. This tool allows moderators to remove and/or lock a full comment tree with a single menu action, avoiding repetitive mechanical tasks for community moderators.

Declare a menu action for moderators

https://developers.reddit.com/docs/quickstart/quickstart-mod-tool#declare-a-menu-action-for-moderators

Menu items are declared in

devvit.json

. Each entry points at a server endpoint that runs when a moderator clicks it. The template leverages

Menu Actions

https://developers.reddit.com/docs/capabilities/client/menu-actions

to enable moderators to Delete/Lock child comments of a post or comment.

devvit.json

{
  "menu": {
    "items": \[
      {
        "label": "Mop comments",
        "description": "Remove this comment and all child comments. This might take a few seconds to run.",
        "forUserType": "moderator",
        "location": \["comment"\],
        "endpoint": "/internal/menu/mop-comments"
      }
    \]
  },
  "forms": {
    "mopForm": "/internal/form/mop-submit"
  },
  "permissions": {
    "reddit": { "enable": true, "scope": "moderator" }
  }
}

Show a form from the menu action

https://developers.reddit.com/docs/quickstart/quickstart-mod-tool#show-a-form-from-the-menu-action

Some moderator tools need additional information before they execute. The menu endpoint can respond with a form using

menu responses

https://developers.reddit.com/docs/capabilities/client/menu-actions

. Comment Mop displays a form with options for the action to be taken:

server/index.ts

import type { MenuItemRequest, UiResponse } from '@devvit/web/shared';
app.post('/internal/menu/mop-comments', async (c) => {
  const \_input = await c.req.json<MenuItemRequest>();
  return c.json<UiResponse>({
    showForm: {
      name: 'mopForm',
      form: {
        title: 'Mop Comments',
        acceptLabel: 'Mop',
        cancelLabel: 'Cancel',
        fields: \[
          { name: 'remove', label: 'Remove comments', type: 'boolean', defaultValue: true },
          { name: 'lock', label: 'Lock comments', type: 'boolean', defaultValue: false },
          {
            name: 'skipDistinguished',
            label: 'Skip distinguished comments',
            type: 'boolean',
            defaultValue: false,
          },
        \],
      },
    },
  });
});

Handle the form submission with the Reddit API

https://developers.reddit.com/docs/quickstart/quickstart-mod-tool#handle-the-form-submission-with-the-reddit-api

Devvit apps can use the Reddit API to act on comments and posts. The form submission endpoint receives the moderator's selections and traverses the comment tree:

server/index.ts

import { reddit, context } from '@devvit/web/server';
import type { UiResponse } from '@devvit/web/shared';
type MopFormRequest = {
  remove: boolean;
  lock: boolean;
  skipDistinguished: boolean;
};
app.post('/internal/form/mop-submit', async (c) => {
  const { remove, lock, skipDistinguished } = await c.req.json<MopFormRequest>();
  const { commentId } = context;
  if (!remove && !lock) {
    return c.json<UiResponse>({ showToast: 'You must select either lock or remove.' });
  }
  if (!commentId) {
    return c.json<UiResponse>({ showToast: 'This action must be run on a comment.' });
  }
  try {
    const rootComment = await reddit.getCommentById(commentId);
    for await (const comment of walkReplies(rootComment, skipDistinguished)) {
      if (remove && !comment.removed) await comment.remove();
      if (lock && !comment.locked) await comment.lock();
    }
    return c.json<UiResponse>({
      showToast: 'Comments mopped! Refresh the page to see the cleanup.',
    });
  } catch (err) {
    console.error(err);
    return c.json<UiResponse>({ showToast: 'Mop failed! Please try again later.' });
  }
});
async function\* walkReplies(
  comment: Awaited<ReturnType<typeof reddit.getCommentById>>,
  skipDistinguished: boolean,
): AsyncGenerator<typeof comment> {
  if (skipDistinguished && comment.distinguishedBy) return;
  yield comment;
  const replies = await comment.replies.all();
  for (const reply of replies) {
    yield\* walkReplies(reply, skipDistinguished);
  }
}

Building and Testing

https://developers.reddit.com/docs/quickstart/quickstart-mod-tool#building-and-testing

#### To build and run your Mod tool, run the following commands on terminal:

npm run dev

If you didn't provide a test subreddit, one will be created for you. Once you run

npm run dev

, you will receive a link to test the mod tool in your test subreddit.

Note that this mod tool is intended to be run on comments, so you will need to create a post and comment in your subreddit to see it.

https://developers.reddit.com/docs/quickstart/quickstart-mod-tool#result

Now you have a mod tool running from the code that you deployed yourself. Feel free to experiment with the code and run

npm run dev

again to see the changes. Notice that you don't need to worry about running costs for your mod tool, because Reddit hosts all Devvit applications for free. Also, if your mod tool becomes popular and gets installed by many subreddits, you may become eligible to earn

Reddit Developer Funds

https://developers.reddit.com/docs/earn-money/reddit\_developer\_funds

Further reading

https://developers.reddit.com/docs/quickstart/quickstart-mod-tool#further-reading

launch guide

https://developers.reddit.com/docs/guides/launch/launch-guide

to guide you where to get your first users.

Devvit Forms

https://developers.reddit.com/docs/capabilities/client/forms

Menu Actions

https://developers.reddit.com/docs/capabilities/client/menu-actions

Reddit Developer Funds

https://developers.reddit.com/docs/earn-money/reddit\_developer\_funds

Previous Introduction to Mod Tools

https://developers.reddit.com/docs/introduction/intro-mod-tools

Next Launch Guide

https://developers.reddit.com/docs/guides/launch/launch-guide

https://developers.reddit.com/docs/blog

The Reddit Developer Fund

https://support.reddithelp.com/hc/en-us/articles/27958169342996-Reddit-Developer-Funds-2025-Terms

https://www.reddit.com/r/devvit

r/GamesOnReddit

https://www.reddit.com/r/GamesOnReddit

Join our Discord

https://developers.reddit.com/discord

Reddit, Inc. © 2026. Built with Docusaurus.

