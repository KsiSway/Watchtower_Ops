---
sourceFile: "Launch your app | Reddit for Developers"
exportedBy: "Kortex"
exportDate: "2026-05-20T06:50:17.451Z"
---

# Launch your app | Reddit for Developers

eb6eb4e0-0a90-486f-8bbc-ff85f091ee67

Launch your app | Reddit for Developers

5ba4cd4c-25c5-4df0-8b1b-ec4c4f881ad7

https://developers.reddit.com/docs/guides/launch/launch-guide

Launch your app | Reddit for Developers

Skip to main content

https://developers.reddit.com/docs/guides/launch/launch-guide#\_\_docusaurus\_skipToContent\_fallback

https://developers.reddit.com/docs/guides/launch/launch-guide

https://developers.reddit.com/docs/next/guides/launch/launch-guide

https://developers.reddit.com/docs/guides/launch/launch-guide

https://developers.reddit.com/docs/0.11

https://developers.reddit.com/docs/guides/launch/launch-guide

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

https://developers.reddit.com/docs/guides/launch/launch-guide

Build Mod Tools

https://developers.reddit.com/docs/guides/launch/launch-guide

Launch Your App

Launch Guide

https://developers.reddit.com/docs/guides/launch/launch-guide

Feature Guide

https://developers.reddit.com/docs/guides/launch/feature-guide

Reddit Developer Funds

https://support.reddithelp.com/hc/en-us/articles/27958169342996-Reddit-Developer-Funds-2025-Terms

Capabilities

Devvit Setup Overview

https://developers.reddit.com/docs/guides/launch/launch-guide

Automation & Triggers

https://developers.reddit.com/docs/guides/launch/launch-guide

https://developers.reddit.com/docs/capabilities/http-fetch

In-App Purchases

https://developers.reddit.com/docs/guides/launch/launch-guide

Post Creation & Navigation

https://developers.reddit.com/docs/guides/launch/launch-guide

Realtime Apps

https://developers.reddit.com/docs/guides/launch/launch-guide

https://developers.reddit.com/docs/guides/launch/launch-guide

Saving Data

https://developers.reddit.com/docs/guides/launch/launch-guide

https://developers.reddit.com/docs/guides/launch/launch-guide

Best Practices

https://developers.reddit.com/docs/guides/launch/launch-guide

Development Tools

https://developers.reddit.com/docs/guides/launch/launch-guide

Migration Guides

https://developers.reddit.com/docs/guides/launch/launch-guide

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

Launch Guide

On this page

Launch your app

Once your app is ready, you can launch it to users and moderators across Reddit. This guide outlines what “launch-ready” means and the steps you need to take to submit your app for review.

Polished apps may also apply for

Reddit featuring

, which includes on-platform promotion and distribution support. Make sure to read

https://developers.reddit.com/docs/guides/launch/feature-guide

before submitting your app.

Our team pauses all app reviews during certain holiday periods each year. Please see community announcements in r/Devvit and Discord for specific limited support dates.

When is an app ready to be launched?

https://developers.reddit.com/docs/guides/launch/launch-guide#when-is-an-app-ready-to-be-launched

Apps should be polished and stable before launch. Ensure your data schema is scalable and your UIs are clean and accessible, as

quality and performance directly impact organic distribution and adoption

#### Before submitting your app for review, be sure to:

Test all functionality across mobile and web.

Test from multiple accounts (developer, moderator, regular user), since permissions differ.

Have a stable prototype with clear UX flows.

#### We also recommend getting feedback from the community:

https://support.reddithelp.com/hc/en-us/articles/4835584113684-What-is-Crossposting

your post to

https://reddit.com/r/Devvit

Feedback Friday

Share your app in the

#ideas-and-feedback

channel in the Reddit Devs Discord.

Cross-post gameplay posts to

r/GamesOnReddit

https://reddit.com/r/GamesOnReddit

Share your app in the

Discord channel for moderator-specific feedback.

If your app is a

, ensure the experience:

Works across platforms with responsive design.

Includes a custom launch or first screen.

Avoids inline scrolling (scrolling inside inline webviews is prohibited).

Has a dedicated, non-test subreddit (e.g.,

https://www.reddit.com/r/Pixelary/

Is immediately understandable to new users.

Launching your app signals to Reddit's algorithmic feeds that it is ready for broader distribution. Engagement — clicks, dwell time, and voting — determines your organic reach.

How to launch an app

https://developers.reddit.com/docs/guides/launch/launch-guide#how-to-launch-an-app

#### Apps are submitted for review through the CLI. To launch your app:

Add a user-friendly overview in your app's

npx devvit publish

. You can optionally choose the version bump type with

npx devvit publish --bump major

npx devvit publish --bump minor

npx devvit publish --bump patch

accepts only

, and cannot be used with

. If you prefer to set a specific version directly, use

npx devvit publish --version 1.0.1

must be a stable version (for example,

), prerelease versions are not allowed, and it cannot be used with

Once submitted, your app enters Reddit's review queue. Our team evaluates your code, example posts, and app documentation.

You will receive email confirmation when your app is approved. If we need more information, a team member may contact you via Modmail or Reddit chat.

Because you must run

npx devvit publish

every version

you want to launch, we recommend batching updates into weekly (or less frequent) releases.

Review times vary. We aim to review most apps — especially version updates — within

1–2 business days

. New apps, apps with policy ambiguity, or apps using higher-risk features (e.g., payments, fetch) may require more time.

If you haven't heard from us after a week, please reach out in Discord or via

r/Devvit Modmail

https://www.reddit.com/message/compose/?to=r/Devvit

Ensuring your app complies with all

Devvit Rules

https://developers.reddit.com/docs/devvit\_rules

will streamline review.

By default, published apps are unlisted

, meaning other communities cannot install them. This is ideal for games and community-specific tools.

How to list your app for any community to install

https://developers.reddit.com/docs/guides/launch/launch-guide#how-to-list-your-app-for-any-community-to-install

If your app is a general-purpose moderation tool, community utility, or otherwise broadly applicable, you can request to list it in the

App Directory

https://developers.reddit.com/apps

. Listing makes your app installable by any moderator.

Publicly listed apps must include a detailed

A comprehensive app overview.

Installer-facing instructions.

Changelogs for major updates.

#### To list your app:

npx devvit publish --public

Once approved, it will appear in the Apps Directory for any community to install.

We do not recommend listing apps built for a single subreddit, as this may confuse moderators and clutter the directory.

https://developers.reddit.com/docs/guides/launch/launch-guide#resources

Questions? Join our Discord or post in

https://www.reddit.com/r/Devvit/

Devvit Rules

https://developers.reddit.com/docs/devvit\_rules

before publishing.

Learn more about

how to earn

https://developers.reddit.com/docs/earn-money/payments/payments\_overview

from your apps.

Previous Quickstart for Mod Tools

https://developers.reddit.com/docs/quickstart/quickstart-mod-tool

Next Feature Guide

https://developers.reddit.com/docs/guides/launch/feature-guide

https://developers.reddit.com/docs/blog

The Reddit Developer Fund

https://support.reddithelp.com/hc/en-us/articles/27958169342996-Reddit-Developer-Funds-2025-Terms

https://www.reddit.com/r/devvit

r/GamesOnReddit

https://www.reddit.com/r/GamesOnReddit

Join our Discord

https://developers.reddit.com/discord

Reddit, Inc. © 2026. Built with Docusaurus.

