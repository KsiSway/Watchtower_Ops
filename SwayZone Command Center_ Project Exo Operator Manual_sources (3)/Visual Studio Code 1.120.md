---
sourceFile: "Visual Studio Code 1.120"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.866Z"
---

# Visual Studio Code 1.120

ff3c3fd8-87fc-47b2-afd2-d7e1ceff9166

Visual Studio Code 1.120

3982479c-9724-47bf-b8d0-347620a80f0a

https://code.visualstudio.com/updates#\_extension-authoring

Visual Studio Code 1.120

Visual Studio Code

https://code.visualstudio.com/

https://code.visualstudio.com/updates

https://code.visualstudio.com/features/agents

https://code.visualstudio.com/updates

Documentation

https://code.visualstudio.com/docs

https://code.visualstudio.com/api

https://code.visualstudio.com/updates

https://code.visualstudio.com/blogs

https://marketplace.visualstudio.com/VSCode

https://code.visualstudio.com/mcp

https://code.visualstudio.com/docs/supporting/faq

https://code.visualstudio.com/learn

https://aka.ms/vscode/live

https://code.visualstudio.com/Download

Search Ctrl+Shift+P

https://code.visualstudio.com/Download

Use the Agents window to build in an agent-first way.

https://code.visualstudio.com/docs/copilot/agents/agents-window?source=vsc-website-banner

Dismiss this update

https://code.visualstudio.com/updates/v1\_121

https://code.visualstudio.com/updates/v1\_120

https://code.visualstudio.com/updates/v1\_119

https://code.visualstudio.com/updates/v1\_118

https://code.visualstudio.com/updates/v1\_117

https://code.visualstudio.com/updates/v1\_116

https://code.visualstudio.com/updates/v1\_115

https://code.visualstudio.com/updates/v1\_114

https://code.visualstudio.com/updates/v1\_113

https://code.visualstudio.com/updates/v1\_112

https://code.visualstudio.com/updates/v1\_111

February 2026

https://code.visualstudio.com/updates/v1\_110

January 2026

https://code.visualstudio.com/updates/v1\_109

View All Releases

https://code.visualstudio.com/updates/archive

February 2026

January 2026

View All Releases

Visual Studio Code 1.120

Follow us on

https://www.linkedin.com/showcase/vs-code

https://go.microsoft.com/fwlink/?LinkID=533687

https://bsky.app/profile/vscode.dev

Release date: May 13, 2026

#### Downloads: Windows:

https://update.code.visualstudio.com/1.120.0/win32-x64-user/stable

https://update.code.visualstudio.com/1.120.0/win32-arm64-user/stable

https://update.code.visualstudio.com/1.120.0/darwin-universal-dmg/stable

https://update.code.visualstudio.com/1.120.0/darwin-x64-dmg/stable

https://update.code.visualstudio.com/1.120.0/darwin-arm64-dmg/stable

https://update.code.visualstudio.com/1.120.0/linux-deb-x64/stable

https://update.code.visualstudio.com/1.120.0/linux-rpm-x64/stable

https://update.code.visualstudio.com/1.120.0/linux-x64/stable

https://code.visualstudio.com/docs/supporting/faq#\_previous-release-versions

https://update.code.visualstudio.com/1.120.0/linux-snap-x64/stable

Welcome to the 1.120 release of Visual Studio Code. This release brings the Agents window to Stable, improves BYOK model visibility and control, and adds Markdown quality-of-life improvements and agent safety features. Here are the highlights for this release:

Agents window in Stable

https://code.visualstudio.com/updates#\_orchestrate-tasks-across-projects-with-the-agents-window-preview

: Work in an agents-first way across all your projects with the new Agents window.

BYOK improvements

https://code.visualstudio.com/updates#\_language-models

: Track and optimize token usage and configure thinking effort for your BYOK models.

Markdown improvements

https://code.visualstudio.com/updates#\_languages

: Review Markdown content instead of syntax with Markdown preview for diffs.

Command risk assessment

https://code.visualstudio.com/updates#\_risk-assessment-for-terminal-commands-experimental

: Assess the risk of terminal commands before they run.

Token optimization

https://code.visualstudio.com/updates#\_terminal-tool-output-compression-preview

: Reduce context window usage by compressing large terminal output.

Happy Coding!

https://code.visualstudio.com/updates#\_agents

Orchestrate tasks across projects with the Agents window (Preview)

https://code.visualstudio.com/updates#\_orchestrate-tasks-across-projects-with-the-agents-window-preview

While VS Code is already used by millions of developers for agentic coding, its editor layout is primarily optimized for single-task, single-workspace workflows. To enable our users (and ourselves!) to work with multiple agents across multiple projects, we created a new type of window:

The new Agents window is a companion to the editor you already know: purpose-built for agent-driven development, with a dedicated space to explore, iterate on, and review tasks across multiple projects, and seamlessly switch between them. And because VS Code is built for developer choice and flexibility, the Agents window lets you pick your agent harness, run agents on remote machines, and configure the environment the way you want it - color themes, keybindings, and extensions included.

The Agents window has been available as part of VS Code Insiders in our past few releases, and with this release, it's now available as a preview in VS Code Stable.

You can open the Agents window in several ways, including the "Open in Agents" button in the VS Code title bar. To learn more about how it works and what you can do with it, visit the

Agents window documentation

https://aka.ms/VSCode/Agents/docs

What's new?

https://code.visualstudio.com/updates#\_whats-new

If you've already been using the Agents window in Insiders, thank you! We've continued to act on your feedback, with the following improvements landing this week:

Preferences persist across new sessions

: Your last choices in dropdowns like agent harness and isolation mode are retained when you create new sessions.

Discard changes more easily

: You can discard edits directly from the Changes panel.

Sync upstream changes in new sessions

: A sync button on the Files panel lets you see upstream changes from the base branch and pull them in before the agent gets to work.

More deterministic changes interactions

: Actions in the Changes panel can complete more quickly as they're now deterministic.

View all changes by default for completed sessions

: When you open a session marked as done, you automatically get a view of the agent's full set of edits at a glance.

Navigate between recent sessions

: Use the arrow buttons in the top-left of the title bar to jump between recent sessions without leaving the window.

Override settings per window

: The Agents window now shares all of your VS Code settings, and you can override specific settings just for the Agents window when you want a different behavior there.

Your feedback continues to be a great help in shaping Agents. Please

file issues on GitHub

https://github.com/microsoft/vscode/issues

existing issues

https://github.com/microsoft/vscode/issues?q=state%3Aopen%20label%3A%22agents-window%22

Extensibility

https://code.visualstudio.com/updates#\_extensibility

Extensions that contribute only static content, such as themes, grammars, languages, and keybindings, activate in the Agents window automatically. We also tested the top 100 Marketplace extensions, and some of those activate as well when installed in your default VS Code profile.

For other extensions, you can opt them in by ID with the extensions.supportAgentsWindow Open in VS Code Open in VS Code Insiders setting. Any extension you enable this way needs to be installed in your default VS Code profile.

"extensions.supportAgentsWindow": {
    "myextension.id": true
}

While we're still working on the broader extension story, we're looking to collaborate with extension authors on what extension enablement in the Agents window unlocks and how various extensions should behave in this environment. Whether you'd like to ideate on new scenarios that take advantage of running agents across projects, or share feedback on how your existing extension behaves in the Agents window, we'd love to collaborate with you through

GitHub issues

https://github.com/microsoft/vscode/issues?q=state%3Aopen%20label%3A%22agents-window%22

Discover Copilot CLI plugins automatically

https://code.visualstudio.com/updates#\_discover-copilot-cli-plugins-automatically

Agent plugins

https://code.visualstudio.com/docs/copilot/customization/agent-plugins

installed with the GitHub Copilot CLI are picked up automatically by VS Code, so a single

copilot plugin install

covers both surfaces. Previously, you had to install the same plugin separately in VS Code or add its path to chat.plugins.paths Open in VS Code Open in VS Code Insiders .

Language models

https://code.visualstudio.com/updates#\_language-models

With Bring Your Own Key (BYOK), you can use your own API keys from providers like Anthropic, OpenAI, and others to take advantage of your own billing or model hosting options. To learn more, see the

BYOK documentation

https://code.visualstudio.com/docs/copilot/customization/language-models#\_bring-your-own-language-model-key

View BYOK model token usage

https://code.visualstudio.com/updates#\_view-byok-model-token-usage

Managing a model's context window is key to getting good results and controlling costs. The model can lose track of important details from the conversation, and token usage can increase costs. This release brings better visibility into token usage for BYOK models, so you can keep an eye on the context window.

Previously, when chatting with a model you brought via your own API key (Anthropic, OpenAI, or other), the control always displayed 0% and a zero-token count because token accounting was only working for built-in models.

The context window control in the Chat view now shows accurate token usage and percent-full for BYOK models.

Configure thinking effort for BYOK reasoning models

https://code.visualstudio.com/updates#\_configure-thinking-effort-for-byok-reasoning-models

Reasoning-capable language models allow you to configure their "thinking effort", which is a way to trade off between response quality and speed/cost. You can learn more in the

thinking effort

https://code.visualstudio.com/docs/copilot/concepts/language-models#\_thinking-effort

documentation.

In this release, you can now configure the thinking effort for BYOK reasoning models directly from the model picker in the Chat view. The selected effort is forwarded to the model on every request, letting you trade off latency and cost against answer quality.

Applies to: Bring-Your-Own-Key (BYOK) reasoning models served via OpenAI-compatible endpoints (OpenAI, xAI (Grok), OpenRouter, and custom OpenAI / Azure OpenAI deployments). Anthropic models already supported this; the control is now consistent across providers.

Model picker organized by provider

https://code.visualstudio.com/updates#\_model-picker-organized-by-provider

The model picker in the Chat view now groups models by their provider, making it easier to find the model you want when you have access to models from multiple sources. You can also search for models by name.

Recently used models now display the provider name in grey text alongside the model name, so you can quickly distinguish between similarly named models from different providers.

You can quickly access the models by typing

in the chat input.

https://code.visualstudio.com/updates#\_chat

Terminal tool output compression (Preview)

https://code.visualstudio.com/updates#\_terminal-tool-output-compression-preview

: chat.tools.compressOutput.enabled Open in VS Code Open in VS Code Insiders

Long terminal output from commands like

npm install

can consume a large share of the model's context window, which leaves less room for your code and the agent's reasoning.

When you enable the chat.tools.compressOutput.enabled Open in VS Code Open in VS Code Insiders setting, VS Code post-processes the output of these commands before sending it to the model. Large unchanged hunks in diffs are collapsed, lockfile and snapshot diffs are dropped,

is reduced to entry names, and

npm install

progress bars, deprecation warnings, and audit summaries are stripped.

A short banner is prepended to any compressed output, so the model can see which filters fired and how to disable compression if it needs the raw text.

Risk assessment for terminal commands (Experimental)

https://code.visualstudio.com/updates#\_risk-assessment-for-terminal-commands-experimental

: chat.tools.riskAssessment.enabled Open in VS Code Open in VS Code Insiders

To help you decide quickly whether a command is worth a closer look, terminal command confirmations now include a risk badge with an AI-generated explanation of what the command does.

Each badge shows one of three levels along with a one-sentence summary tailored to the specific command:

(green): reads files or prints output without making changes.

(orange): modifies the workspace, installs packages, or sends data over the network.

Review carefully

(red): performs an action that may be difficult or impossible to undo, such as force-pushing to a remote or deleting files outside the workspace.

Plan mode control for Claude and Copilot CLI

https://code.visualstudio.com/updates#\_plan-mode-control-for-claude-and-copilot-cli

: chat.planWidget.inlineEditor.enabled Open in VS Code Open in VS Code Insiders

When you use plan mode with the Claude agent or the Copilot CLI, VS Code shows an inline plan control that lets you review and shape the plan before the agent starts executing. This release brings several improvements to that flow:

Edit the plan inline

: Editing the plan now happens in an inline editor inside the control instead of opening a separate editor tab, so you can iterate on the plan without losing context.

Clearer feedback mode

: When you're providing feedback on a plan, the control shows clearer indications that you're in feedback mode and shows the feedback you've added so far.

Disable the inline editor

: Opt out of the inline editing experience and fall back to editing in a regular editor tab by configuring the chat.planWidget.inlineEditor.enabled Open in VS Code Open in VS Code Insiders setting.

https://code.visualstudio.com/updates#\_languages

Markdown preview for diffs (Preview)

https://code.visualstudio.com/updates#\_markdown-preview-for-diffs-preview

When you open a Markdown file from the

Source Control

view, you can view the diff using VS Code's rendered Markdown preview instead of the raw source.

This makes it much easier to spot meaningful changes, such as updated headings, new sections, modified images, or restructured lists, without having to mentally parse Markdown syntax line by line.

The diff Markdown preview supports both a side-by-side diff view and an inline view.

To try it, open a Markdown diff from Source Control (or any other diff editor) and use

Reopen Editor With...

to switch to the Markdown preview diff view. You can also open diffs in the Markdown preview by default with the workbench.diffEditorAssociations Open in VS Code Open in VS Code Insiders setting:

"workbench.diffEditorAssociations": {
  "\*.md": "vscode.markdown.preview.editor"
}

This feature is still a preview, so you might run into issues. We think it will be especially useful for reviewing documentation changes from agents or pull requests.

Markdown preview default changes

https://code.visualstudio.com/updates#\_markdown-preview-default-changes

VS Code's built-in Markdown preview has been around for a while and a few of the original features aren't as necessary as they once were. This iteration we decided to disable two of these features by default:

markdown.preview.doubleClickToSwitchToEditor Open in VS Code Open in VS Code Insiders : Double-clicking in the preview switches back to the source editor. Users often found it confusing as they wanted to use double click to make selections. We now have features like

Reopen With

that largely replace this functionality

markdown.preview.markEditorSelection Open in VS Code Open in VS Code Insiders : Marks the currently selected line in the editor. We think it's less useful for modern workflows.

You can re-enable these settings if you prefer the previous behavior.

HTML id support for Markdown path completions and validation

https://code.visualstudio.com/updates#\_html-id-support-for-markdown-path-completions-and-validation

Our built-in

Markdown path completions

https://code.visualstudio.com/docs/languages/markdown#\_path-completions

link validation

https://code.visualstudio.com/docs/languages/markdown#\_link-validation

now recognize

attributes from HTML elements in Markdown files.

<div id="install-guide">...</div>

See the \[installation steps\](#\_install-guide) for details.

#### Links for these IDs are now suggested in completions:

They are also used for

link validation

https://code.visualstudio.com/docs/languages/markdown#\_link-validation

Smart select for Markdown tables

https://code.visualstudio.com/updates#\_smart-select-for-markdown-tables

Markdown tables now support basic

smart selection

https://code.visualstudio.com/docs/editing/codebasics#\_shrinkexpand-selection

Expand Selection

( ⌃⇧⌘→ (Windows, Linux Shift+Alt+Right)) to grow the selection from a cell to its row and then to the full table, and

Shrink Selection

( ⌃⇧⌘← (Windows, Linux Shift+Alt+Left)) to step back down.

Proposed APIs

https://code.visualstudio.com/updates#\_proposed-apis

Custom editor diffs

https://code.visualstudio.com/updates#\_custom-editor-diffs

customEditorDiffs

proposed API lets custom editors render diffs with a dedicated diff UI. This is what powers the new

Markdown preview in the diff view

https://code.visualstudio.com/updates#\_markdown-preview-for-diffs-preview

, and it opens up a much nicer compare experience where a textual diff of the underlying source isn't useful.

A custom editor provider can opt in by implementing one or both of the following on

CustomReadonlyEditorProvider

CustomTextEditorProvider

resolveCustomEditorInlineDiff(documents, webviewPanel, token)

: render the diff in a single webview, with both the original and modified documents available to the extension.

resolveCustomEditorSideBySideDiff(documents, webviewPanels, token)

: render the diff using two webviews, one for each side, with VS Code coordinating layout and scroll sync.

Combined with

diffEditorPriority

https://code.visualstudio.com/updates#\_separate-custom-editor-priorities-diffs-and-merges

, extensions now have full control over whether their custom editor handles diffs and how those diffs are presented. See

issue #138525

https://github.com/microsoft/vscode/issues/138525

to follow along and provide feedback.

Separate custom editor priorities diffs and merges

https://code.visualstudio.com/updates#\_separate-custom-editor-priorities-diffs-and-merges

Custom editor extensions can now set different default priorities for editing, diffing, and merging a file type. The

customEditors

contribution accepts two new optional fields,

diffEditorPriority

mergeEditorPriority

, alongside the existing

"contributes": {
  "customEditors": \[
    {
      "viewType": "myExtension.editor",
      "displayName": "My Custom Editor",
      "selector": \[
        { "filenamePattern": "\*.custom" }
      \],
      "priority": "default",
      "diffEditorPriority": "option",
      "mergeEditorPriority": "option"
    }
  \]
}

The above contribution makes it so that opening a

file uses the custom editor, but opening a diff from source control uses the normal text diff view.

This API is still proposed. Try it out and share feedback in

issue #292379

https://github.com/microsoft/vscode/issues/292379

Document diff

https://code.visualstudio.com/updates#\_document-diff

documentDiff

proposed API exposes VS Code's built-in diff algorithm to extensions via

workspace.getTextDiff(original, modified, options?)

. It returns a streaming async iterable of line-level changes plus a

promise with summary information (identical, may-be-incomplete, and optional move detection). Inner character-level ranges are included on each change.

This is especially useful for custom diff editors (see

Custom editor diffs

https://code.visualstudio.com/updates#\_custom-editor-diffs

) so they can render exactly the same diffs as the built-in editor instead of shipping their own algorithm.

const diff = vscode.workspace.getTextDiff(originalDoc, modifiedDoc, {
  ignoreTrimWhitespace: true,
  computeMoves: false
});

for await (const change of diff.changes) {
  // change.originalRange, change.modifiedRange, change.innerChanges
}

const { identical, mayBeIncomplete, moves } = await diff.complete;

Track progress and provide feedback in

issue #315174

https://github.com/microsoft/vscode/issues/315174

Contributions to extensions

https://code.visualstudio.com/updates#\_contributions-to-extensions

GitHub Pull Requests

https://code.visualstudio.com/updates#\_github-pull-requests

There has been more progress on the

GitHub Pull Requests

https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github

extension, which enables you to work on, create, and manage pull requests and issues. New features include:

Uploading images to pull request comments through copy/paste and an upload button.

More descriptive folder name when checkout out pull requests in a worktree.

"githubIssues.issueBranchTitle"

now supports the

${issueType}

template variable.

changelog for the 0.144.0

https://github.com/microsoft/vscode-pull-request-github/blob/main/CHANGELOG.md#01440

release of the extension to learn about everything in the release.

Deprecated features and settings

https://code.visualstudio.com/updates#\_deprecated-features-and-settings

New deprecations in this release

https://code.visualstudio.com/updates#\_new-deprecations-in-this-release

Upcoming deprecations

https://code.visualstudio.com/updates#\_upcoming-deprecations

Notable fixes

https://code.visualstudio.com/updates#\_notable-fixes

microsoft/vscode #314545

https://github.com/microsoft/vscode/issues/314545

Include All-Interfaces links in integrated browser localhost targets

https://code.visualstudio.com/updates#\_thank-you

#### Contributions to our issue tracking:

@gjsjohnmurray (John Murray)

https://github.com/gjsjohnmurray

@RedCMD (RedCMD)

https://github.com/RedCMD

@IllusionMH (Andrii Dieiev)

https://github.com/IllusionMH

@albertosantini (Alberto Santini)

https://github.com/albertosantini

Contributions to

@damonxue (DamonXue)

https://github.com/damonxue

: Add File to Chat" does nothing when right-clicking a non-active editor tab

https://github.com/microsoft/vscode/pull/315197

@davidwengier (David Wengier)

https://github.com/davidwengier

: Update repository and path for Razor repo

https://github.com/microsoft/vscode/pull/313011

@Dmitriusan

https://github.com/Dmitriusan

: Fix gitignore negation in child files not overriding parent/global rules

https://github.com/microsoft/vscode/pull/300613

@EhabY (Ehab Younes)

https://github.com/EhabY

: Detect dead connections via keepalive timeout

https://github.com/microsoft/vscode/pull/310131

https://github.com/JeffreyCA

Update Fig spec for Azure Developer CLI (azd)

https://github.com/microsoft/vscode/pull/308613

Integrated terminal - fix stale OSC 8 link hover tooltip issues

https://github.com/microsoft/vscode/pull/309539

@kevin-m-kent

https://github.com/kevin-m-kent

Emit parentRequestId on response.\* events and from subagent loops

https://github.com/microsoft/vscode/pull/314309

Add X-Interaction-Type header and requestKind telemetry property for chat requests

https://github.com/microsoft/vscode/pull/312262

Ship stable symbol tool descriptions

https://github.com/microsoft/vscode/pull/315686

@Larsjep (Lars Jeppesen)

https://github.com/Larsjep

: fixes https://github.com/microsoft/vscode/issues/291188

https://github.com/microsoft/vscode/pull/314713

@n-gist (n-gist)

https://github.com/n-gist

: guarantee that return of TreeDataProvider.getChildren() is not mutated by vscode

https://github.com/microsoft/vscode/pull/306955

@Pengkun-ZHU (pzhu)

https://github.com/Pengkun-ZHU

: Pzhu/feature custom snooze time

https://github.com/microsoft/vscode/pull/298934

@pranavvaid-ac

https://github.com/pranavvaid-ac

Update chat inline references after late anchor resolution

https://github.com/microsoft/vscode/pull/314281

Improve linked symbol anchors with tree-sitter fallback

https://github.com/microsoft/vscode/pull/314864

@ruryu (ruryu)

https://github.com/ruryu

: fix(agentHost): await dbClose to resolve flaky session database tests

https://github.com/microsoft/vscode/pull/313810

@ShehabSherif0 (Shehab Sherif)

https://github.com/ShehabSherif0

: Fix incorrect inspect property usage in scope detection

https://github.com/microsoft/vscode/pull/301472

@SimonSiefke (Simon Siefke)

https://github.com/SimonSiefke

: fix: memory leak in utilityProcessWorkerMainService

https://github.com/microsoft/vscode/pull/294005

@Tyriar (Daniel Imms)

https://github.com/Tyriar

Put ambiguous options into interface

https://github.com/microsoft/vscode/pull/313953

Remove unused export const

https://github.com/microsoft/vscode/pull/315244

@yemohyleyemohyle

https://github.com/yemohyleyemohyle

: Yemohyle/response success gdpr blocks

https://github.com/microsoft/vscode/pull/315128

@yogeshwaran-c (Yogeshwaran C)

https://github.com/yogeshwaran-c

: Strip codicons from terminal quickpick filter matching

https://github.com/microsoft/vscode/pull/313197

Contributions to

vscode-pull-request-github

@MaxDNG (Maxime Guitet)

https://github.com/MaxDNG

: Fix: Re-parent pulled-up directory children to ensure proper checkbox refresh

https://github.com/microsoft/vscode-pull-request-github/pull/8679

We really appreciate people trying our new features as soon as they are ready, so check back here often and learn what's new.

If you'd like to read release notes for previous VS Code versions, go to

https://code.visualstudio.com/updates

code.visualstudio.com

https://code.visualstudio.com/

Help and support

Was this page helpful?

Yes , this page was helpful No , this page was not helpful

Still need help?

Ask the community

https://stackoverflow.com/questions/tagged/vscode

Request features

https://go.microsoft.com/fwlink/?LinkID=533482

Report issues

https://www.github.com/Microsoft/vscode/issues

Help us improve

Edit this page

On this page there are 9 sections On this page

https://code.visualstudio.com/updates#\_agents

Language models

https://code.visualstudio.com/updates#\_language-models

https://code.visualstudio.com/updates#\_chat

https://code.visualstudio.com/updates#\_languages

Proposed APIs

https://code.visualstudio.com/updates#\_proposed-apis

Contributions to extensions

https://code.visualstudio.com/updates#\_contributions-to-extensions

Deprecated features and settings

https://code.visualstudio.com/updates#\_deprecated-features-and-settings

Notable fixes

https://code.visualstudio.com/updates#\_notable-fixes

https://code.visualstudio.com/updates#\_thank-you

https://code.visualstudio.com/feed.xml

Ask questions

https://stackoverflow.com/questions/tagged/vscode

Follow @code

https://go.microsoft.com/fwlink/?LinkID=533687

Request features

https://go.microsoft.com/fwlink/?LinkID=533482

Report issues

https://www.github.com/Microsoft/vscode/issues

Watch videos

https://www.youtube.com/channel/UCs5Y5\_7XK8HLDX0SLNwkd3w

https://support.serviceshub.microsoft.com/supportforbusiness/create?sapId=d66407ed-3967-b000-4cfb-2c318cad363d

https://go.microsoft.com/fwlink/?LinkId=521839

Manage Cookies

https://code.visualstudio.com/updates

Terms of Use

https://www.microsoft.com/legal/terms-of-use

https://code.visualstudio.com/License

Your Privacy Choices

https://aka.ms/YourCaliforniaPrivacyChoices

Consumer Health Privacy

https://go.microsoft.com/fwlink/?linkid=2259814

