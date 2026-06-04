---
sourceFile: "Weekly GitHub Report for Vscode: November 10, 2025 - Buttondown"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.879Z"
---

# Weekly GitHub Report for Vscode: November 10, 2025 - Buttondown

79503061-235b-4634-a4c7-e0eb5adc7028

Weekly GitHub Report for Vscode: November 10, 2025 - Buttondown

c9674cd4-d04c-4e0f-8755-cc9f3e3107c3

https://buttondown.com/weekly-project-news/archive/weekly-github-report-for-vscode-november-10-2025/

Weekly GitHub Report for Vscode: November 10, 2025 - November 17, 2025 (12:00:51) • Buttondown

Weekly Project News

https://buttondown.com/weekly-project-news

https://buttondown.com/weekly-project-news/archive/

Weekly GitHub Report for Vscode: November 10, 2025 - November 17, 2025 (12:00:51)

Weekly GitHub Report for Vscode

Thank you for subscribing to our weekly newsletter! Each week, we deliver a comprehensive summary of your GitHub project's latest activity right to your inbox, including an overview of your project's issues, pull requests, contributors, and commit activity.

Table of Contents

https://buttondown.com/weekly-project-news/archive/weekly-github-report-for-vscode-november-10-2025/#news

## Recent Version Releases

https://buttondown.com/weekly-project-news/archive/weekly-github-report-for-vscode-november-10-2025/#releases

## Other Noteworthy Updates

https://buttondown.com/weekly-project-news/archive/weekly-github-report-for-vscode-november-10-2025/#updates

https://buttondown.com/weekly-project-news/archive/weekly-github-report-for-vscode-november-10-2025/#issues

## Top 5 Active Issues

https://buttondown.com/weekly-project-news/archive/weekly-github-report-for-vscode-november-10-2025/#active

## Top 5 Stale Issues

https://buttondown.com/weekly-project-news/archive/weekly-github-report-for-vscode-november-10-2025/#stale

## Open Issues

https://buttondown.com/weekly-project-news/archive/weekly-github-report-for-vscode-november-10-2025/#open

## Closed Issues

https://buttondown.com/weekly-project-news/archive/weekly-github-report-for-vscode-november-10-2025/#closed

## Issue Discussion Insights

https://buttondown.com/weekly-project-news/archive/weekly-github-report-for-vscode-november-10-2025/#discussion

III. Pull Requests

https://buttondown.com/weekly-project-news/archive/weekly-github-report-for-vscode-november-10-2025/#prs

## Open Pull Requests

https://buttondown.com/weekly-project-news/archive/weekly-github-report-for-vscode-november-10-2025/#open-prs

## Closed Pull Requests

https://buttondown.com/weekly-project-news/archive/weekly-github-report-for-vscode-november-10-2025/#closed-prs

## Pull Request Discussion Insights

https://buttondown.com/weekly-project-news/archive/weekly-github-report-for-vscode-november-10-2025/#discussion-prs

IV. Contributors

https://buttondown.com/weekly-project-news/archive/weekly-github-report-for-vscode-november-10-2025/#contributors

## Contributors

https://buttondown.com/weekly-project-news/archive/weekly-github-report-for-vscode-november-10-2025/#active-contributors

1.1 Recent Version Releases:

The current version of this repository is 1.98.2

1.2 Version Information:

The version released on March 12, 2025, primarily focuses on resolving various issues as detailed in the linked GitHub milestone for "February 2025 Recovery 2." For a comprehensive overview of all updates and improvements, users are directed to the official release notes on the Visual Studio Code website.

2.1 Top 5 Active Issues:

We consider active issues to be issues that that have been commented on most frequently within the last week. Bot comments are omitted.

Extension host terminating on macOS with v1.106

https://github.com/microsoft/vscode/issues/277064?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

: This issue reports that on macOS with VS Code version 1.106, the extension host crashes immediately upon startup with the error "Extension host terminated unexpectedly 3 times within the last 5 minutes." The problem appears related to a native crash triggered when Node.js attempts to obtain system CA certificates, and users have found a temporary workaround by disabling this behavior via the

"http.systemCertificatesNode": false

Multiple users confirmed the crash occurs on macOS (and possibly Windows) after updating to version 1.106, with extensive troubleshooting including reinstalling VS Code and clearing extensions failing to resolve it. Crash dumps revealed the issue stems from Node.js certificate handling, and setting

"http.systemCertificatesNode": false

successfully prevents the crash, though the root cause is linked to a recent code change involving system certificate parsing; the setting has since been disabled in A/B testing to mitigate the problem.

Number of comments this week: 18

Extension Signature Verification Failed: GitHub Copilot Chat

https://github.com/microsoft/vscode/issues/276933?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

: This issue reports a bug where the GitHub Copilot Chat extension fails signature verification during installation, particularly affecting setups using WSL with Guix. Users also experience related problems such as extension host crashes, disabled GitHub login, and incompatibility errors with certain API proposals after updating VS Code to version 1.106.0.

The comments reveal that while the original issue concerns signature verification failures on Windows with VS Code 1.105.1, several users report a similar but distinct problem after upgrading to VS Code 1.106.0 on macOS, involving API incompatibilities causing extension host crashes and login failures; users suggest these are separate issues and recommend filing distinct bug reports.

Number of comments this week: 9

Incorrect warning "The model wants to edit files outside of your workspace"

https://github.com/microsoft/vscode/issues/276392?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

: This issue reports an incorrect warning message in the Copilot Chat extension for VS Code, where the user is prompted that the model wants to edit files outside of their workspace, even though the files are clearly within the workspace folder. The user provides environment details and reproduction steps, and the discussion in the comments investigates whether the workspace is symlinked and verifies the real paths of the workspace and files to confirm the paths match.

Multiple users confirm experiencing the same warning on different operating systems. The discussion rules out symlinked folders as the cause by checking real paths, which are consistent with the workspace location. The issue remains unresolved but is clearly identified as a false positive warning about file locations.

Number of comments this week: 7

Issue with Terminal Commands Not Being Executed in Copilot Chat

https://github.com/microsoft/vscode/issues/277130?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

: This issue describes a problem where terminal commands fail to execute when using GitHub Copilot Chat accessed through a VS Code tunnel, despite the ability to edit and inspect files. The user reports that the GitHub Pull Request extension never activates, repeatedly showing warnings that its API is unavailable, which appears to block terminal command execution and pull-request workflows in this remote setup.

The discussion involved requests for additional environment details, screenshots, and logs to diagnose the problem. The user provided detailed system information and evidence showing the extension failing to activate and terminal commands not running, while attempts to reload, restart, and verify CLI functionality via direct SSH did not resolve the issue.

Number of comments this week: 7

Allow changing default GitHub Copilot model for all users of an organization

https://github.com/microsoft/vscode/issues/276993?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

: This issue requests the ability to set a default GitHub Copilot model for all users within an organization, aiming to improve onboarding by ensuring everyone uses a premium model by default rather than the less effective 'auto' mode. The user highlights that many developers struggle with Copilot because they unknowingly use non-premium models, and switching to models like Claude Sonnet 4.5 significantly enhances their experience and productivity.

The discussion acknowledges the feature request but places it in the backlog pending further feedback. Commenters express frustration with the 'auto' mode reverting unexpectedly and prefer consistent use of premium models, while maintainers seek clarification on the reported bug and usage scenarios, with some investigation ongoing to reproduce the issue.

Number of comments this week: 6

2.2 Top 5 Stale Issues:

We consider stale issues to be issues that has had no activity within the last 30 days. The team should work together to get these issues resolved and closed as soon as possible.

Notebook>Outline: Show Code Cell Markdown

https://github.com/microsoft/vscode/issues/209166?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

: This issue is a feature request asking for the ability to display markdown generated by code cells in the notebook outline, similar to how JupyterLab handles dynamic titles rendered in the output of code cells. The requester highlights that this functionality would allow outlines to include dynamically generated content from code cells, improving usability by reflecting changes made through code rather than only static markdown cells.

Using a vscode:// link with ?new-window or ?reuse-window still hijacks existing window

https://github.com/microsoft/vscode/issues/209188?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

: This issue reports a bug in Visual Studio Code where using a vscode:// link with the query parameters ?new-window or ?reuse-window does not behave as expected when opening remote SSH connections. Instead of opening a new window or reusing the existing one, the current remote session is disconnected and replaced by the new connection, causing loss of the original window's context.

${userHome} in a task command creates bad paths

https://github.com/microsoft/vscode/issues/209218?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

: This issue describes a problem where using the

${userHome}

variable in a task command within VS Code's

file generates incorrect file paths when the task type is set to "process," causing the terminal process to fail to start due to invalid executable paths. The reporter notes that while

${userHome}

works correctly when the task type is "shell" with PowerShell as the default shell, it produces malformed paths in other contexts, and that using

${env:USERPROFILE}

serves as a functional workaround.

Terminal in Floating Window Does Not Echo Characters in Real Time When Remotely Connected

https://github.com/microsoft/vscode/issues/209234?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

: This issue describes a problem where the terminal in a floating window does not echo typed characters in real time when connected to a remote environment, such as WSL or SSH, if the main VS Code window is minimized. The characters only appear after restoring the main window, indicating that the remote connection may enter a sleep state when the main window is minimized, preventing immediate terminal updates despite no actual freeze occurring.

Unicode character displayed as a question mark ?

https://github.com/microsoft/vscode/issues/209274?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

: This issue reports that when a fullwidth quotation mark Unicode character (U+FF02) is pasted into Visual Studio Code, it is incorrectly rendered as a question mark instead of displaying the correct symbol. The problem occurs on Fedora 39 with VS Code version 1.87.2, and the character displays properly in other applications like Firefox, indicating a rendering bug specific to VS Code.

2.3 Open Issues

This section lists, groups, and then summarizes issues that were created within the last week in the repository.

#### Issues Opened This Week:

#### Summarized Issues:

#### Extension Unresponsiveness and No Response Issues:

Multiple reports indicate that various versions of the VS Code extension (notably 0.32.4, 0.32.5, 0.33.0, and 0.33.1) frequently become unresponsive or fail to return any response during use on Windows 10, macOS, and Linux systems. Users experience symptoms such as the extension being stuck on "Working," showing error messages like "Sorry, no response was returned," or the chat window freezing and not updating, severely disrupting workflows and causing frustration.

issues/276374

https://github.com/issues/276374?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276375

https://github.com/issues/276375?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276377

https://github.com/issues/276377?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276385

https://github.com/issues/276385?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276390

https://github.com/issues/276390?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276396

https://github.com/issues/276396?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276401

https://github.com/issues/276401?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276410

https://github.com/issues/276410?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276418

https://github.com/issues/276418?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276618

https://github.com/issues/276618?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276621

https://github.com/issues/276621?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276624

https://github.com/issues/276624?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276678

https://github.com/issues/276678?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276687

https://github.com/issues/276687?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276688

https://github.com/issues/276688?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276849

https://github.com/issues/276849?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276922

https://github.com/issues/276922?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276928

https://github.com/issues/276928?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276932

https://github.com/issues/276932?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276953

https://github.com/issues/276953?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277346

https://github.com/issues/277346?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277372

https://github.com/issues/277372?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277410

https://github.com/issues/277410?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277429

https://github.com/issues/277429?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277539

https://github.com/issues/277539?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### GitHub Copilot and Chat Feature Failures:

Numerous issues report that GitHub Copilot and Copilot Chat extensions fail to function correctly across various platforms and VS Code versions. Problems include failure to sign in, chat windows not appearing or freezing, incorrect or incomplete code suggestions, persistent 400 errors, and inability to use premium features despite payment. These failures often cause significant disruption to user productivity and trust in the tool.

issues/276394

https://github.com/issues/276394?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276431

https://github.com/issues/276431?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276494

https://github.com/issues/276494?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276525

https://github.com/issues/276525?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276593

https://github.com/issues/276593?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276596

https://github.com/issues/276596?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276624

https://github.com/issues/276624?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276638

https://github.com/issues/276638?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276639

https://github.com/issues/276639?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276690

https://github.com/issues/276690?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276693

https://github.com/issues/276693?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276700

https://github.com/issues/276700?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276707

https://github.com/issues/276707?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276730

https://github.com/issues/276730?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276733

https://github.com/issues/276733?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276745

https://github.com/issues/276745?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276749

https://github.com/issues/276749?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276900

https://github.com/issues/276900?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276910

https://github.com/issues/276910?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276918

https://github.com/issues/276918?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277053

https://github.com/issues/277053?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277074

https://github.com/issues/277074?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277183

https://github.com/issues/277183?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277201

https://github.com/issues/277201?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277214

https://github.com/issues/277214?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277257

https://github.com/issues/277257?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277280

https://github.com/issues/277280?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277335

https://github.com/issues/277335?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277370

https://github.com/issues/277370?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277381

https://github.com/issues/277381?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277384

https://github.com/issues/277384?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277405

https://github.com/issues/277405?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277421

https://github.com/issues/277421?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277426

https://github.com/issues/277426?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277427

https://github.com/issues/277427?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277528

https://github.com/issues/277528?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277637

https://github.com/issues/277637?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277643

https://github.com/issues/277643?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277644

https://github.com/issues/277644?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277645

https://github.com/issues/277645?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277652

https://github.com/issues/277652?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Performance and Resource Usage Problems:

Several issues highlight severe performance degradation in VS Code and its extensions, including high CPU and memory usage, freezing, slow responses, and unresponsiveness during normal operations or specific tasks like code completion, chat interactions, or running tests. These problems occur on multiple platforms and hardware configurations, often rendering the application unusable or causing significant delays.

issues/276408

https://github.com/issues/276408?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276415

https://github.com/issues/276415?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276422

https://github.com/issues/276422?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276523

https://github.com/issues/276523?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276650

https://github.com/issues/276650?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276681

https://github.com/issues/276681?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276782

https://github.com/issues/276782?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276786

https://github.com/issues/276786?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276943

https://github.com/issues/276943?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277161

https://github.com/issues/277161?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277337

https://github.com/issues/277337?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277418

https://github.com/issues/277418?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277426

https://github.com/issues/277426?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277490

https://github.com/issues/277490?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277573

https://github.com/issues/277573?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277645

https://github.com/issues/277645?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Network and Authorization Errors:

Users report frequent network-related errors such as ERR\_HTTP2\_PROTOCOL\_ERROR, ERR\_CERT\_COMMON\_NAME\_INVALID, ERR\_CONNECTION\_RESET, 400 and 403 HTTP errors, and authorization failures affecting extension functionality, sign-in processes, and API requests. These issues often relate to firewall settings, proxy configurations, or certificate problems, causing disruptions in normal operation.

issues/276393

https://github.com/issues/276393?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276441

https://github.com/issues/276441?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276784

https://github.com/issues/276784?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276799

https://github.com/issues/276799?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276863

https://github.com/issues/276863?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277071

https://github.com/issues/277071?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277326

https://github.com/issues/277326?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277463

https://github.com/issues/277463?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277465

https://github.com/issues/277465?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277470

https://github.com/issues/277470?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277508

https://github.com/issues/277508?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277659

https://github.com/issues/277659?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Code Modification and Edit Application Failures:

Multiple issues describe situations where the agent or extension indicates that code changes or file edits have been made, but no actual modifications occur in the files. This includes problems with edit pills showing combined diffs incorrectly, files being deleted unexpectedly, or changes not being applied despite confirmation messages, leading to confusion and loss of trust in the tool's reliability.

issues/276376

https://github.com/issues/276376?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276380

https://github.com/issues/276380?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276381

https://github.com/issues/276381?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276483

https://github.com/issues/276483?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276729

https://github.com/issues/276729?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277029

https://github.com/issues/277029?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277252

https://github.com/issues/277252?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277528

https://github.com/issues/277528?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### UI and Visual Bugs:

Several reports highlight UI inconsistencies and visual bugs such as misaligned paddings and margins, flickering chat views, invisible indentation guides, clipped confirmation dialogs, and broken or missing UI elements like model selectors or chat windows. These issues degrade the user experience and can cause confusion or hinder usability.

issues/276378

https://github.com/issues/276378?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276382

https://github.com/issues/276382?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276434

https://github.com/issues/276434?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276435

https://github.com/issues/276435?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276474

https://github.com/issues/276474?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276588

https://github.com/issues/276588?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276807

https://github.com/issues/276807?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277021

https://github.com/issues/277021?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277089

https://github.com/issues/277089?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277132

https://github.com/issues/277132?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277390

https://github.com/issues/277390?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277442

https://github.com/issues/277442?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277547

https://github.com/issues/277547?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Sign-In and Authentication Problems:

Users frequently encounter issues signing into GitHub Copilot or related services within VS Code, including missing browser windows for authentication, repeated sign-in prompts, and persistent login errors despite correct credentials and network connectivity. These problems prevent access to key features and cause user frustration.

issues/276414

https://github.com/issues/276414?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276596

https://github.com/issues/276596?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276730

https://github.com/issues/276730?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276855

https://github.com/issues/276855?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276859

https://github.com/issues/276859?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276863

https://github.com/issues/276863?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277515

https://github.com/issues/277515?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Model Selection and Configuration Issues:

Several issues report missing or broken model selection dropdowns, inability to set default models, unexpected model switching behavior, and requests for more flexible model configuration options. These problems limit user control over AI model usage and can lead to suboptimal or confusing experiences.

issues/276839

https://github.com/issues/276839?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276993

https://github.com/issues/276993?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277102

https://github.com/issues/277102?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277465

https://github.com/issues/277465?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277556

https://github.com/issues/277556?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Memory Leaks and Promise Accumulation:

Reports indicate memory leaks in VS Code related to unresolved promises accumulating during notebook scrolling, terminal creation and deletion, and text duplication and deletion, leading to increased resource consumption and potential performance degradation over time.

issues/276605

https://github.com/issues/276605?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276610

https://github.com/issues/276610?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276612

https://github.com/issues/276612?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276958

https://github.com/issues/276958?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Agent and Tool Integration Bugs:

Issues include agents entering infinite loops, refusing to use enabled tools, incorrectly flagging valid YAML as errors, and problems with tool confirmation editors and delegation workflows. These bugs disrupt the expected AI-assisted workflows and cause user confusion or wasted resources.

issues/276589

https://github.com/issues/276589?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276811

https://github.com/issues/276811?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276854

https://github.com/issues/276854?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276662

https://github.com/issues/276662?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277313

https://github.com/issues/277313?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Feature Requests for Improved Usability and Functionality:

Users request enhancements such as standardized UI bug report templates, support for new AI models, improved chat export options, better model and tool configuration interfaces, inline refactoring support, and more intuitive UI elements like run-to-cursor icons and multi-line status bars to improve overall user experience and productivity.

issues/276378

https://github.com/issues/276378?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276397

https://github.com/issues/276397?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276629

https://github.com/issues/276629?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276465

https://github.com/issues/276465?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276977

https://github.com/issues/276977?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277143

https://github.com/issues/277143?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277200

https://github.com/issues/277200?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277217

https://github.com/issues/277217?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277231

https://github.com/issues/277231?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277325

https://github.com/issues/277325?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277547

https://github.com/issues/277547?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277638

https://github.com/issues/277638?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Crash and Stability Issues:

Several reports describe crashes of VS Code or its extension host triggered by specific actions such as opening files, using certain extensions, or during startup, often requiring workarounds or disabling features to regain stability.

issues/276574

https://github.com/issues/276574?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276577

https://github.com/issues/276577?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277064

https://github.com/issues/277064?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277137

https://github.com/issues/277137?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277392

https://github.com/issues/277392?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277657

https://github.com/issues/277657?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Localization and Accessibility Concerns:

Some issues highlight problems with localization such as untranslated strings, incorrect text direction for RTL languages, and accessibility issues like screen readers not announcing dialogs or keyboard shortcuts not working as expected, impacting usability for diverse user groups.

issues/277089

https://github.com/issues/277089?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277170

https://github.com/issues/277170?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277578

https://github.com/issues/277578?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277186

https://github.com/issues/277186?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Miscellaneous Bugs and User Experience Problems:

Additional issues include problems with keyboard shortcuts, terminal behavior, file drag-and-drop, and unexpected UI behaviors such as persistent undo UI or incorrect git blame decorations, all contributing to a less smooth user experience.

issues/276495

https://github.com/issues/276495?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276507

https://github.com/issues/276507?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276999

https://github.com/issues/276999?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277017

https://github.com/issues/277017?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277083

https://github.com/issues/277083?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277186

https://github.com/issues/277186?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277390

https://github.com/issues/277390?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277593

https://github.com/issues/277593?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

2.4 Closed Issues

This section lists, groups, and then summarizes issues that were closed within the last week in the repository. This section also links the associated pull requests if applicable.

#### Issues Closed This Week:

#### Summarized Issues:

#### Agent and Model Identification Issues:

Several reports indicate that the Claude Sonnet 4.5 agent and related AI models incorrectly identify themselves as older versions (e.g., Claude 3.5 Sonnet), causing user confusion and bug reports. Additionally, the agent sometimes hangs or becomes stuck waiting indefinitely during command execution or git operations, leading to stalled workflows and requiring manual intervention.

issues/276328

https://github.com/issues/276328?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276338

https://github.com/issues/276338?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276710

https://github.com/issues/276710?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276404

https://github.com/issues/276404?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276405

https://github.com/issues/276405?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276566

https://github.com/issues/276566?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276567

https://github.com/issues/276567?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277315

https://github.com/issues/277315?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276500

https://github.com/issues/276500?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Terminal Command Execution and Interaction Bugs:

Multiple issues report that GitHub Copilot and AI agents fail to correctly handle terminal commands, including omitting the first letter of commands, failing to detect terminal state, merging command histories across terminals, and terminal output being blank or cut off. These bugs cause commands to be entered incorrectly, indefinite waiting, and loss of terminal session context.

issues/276355

https://github.com/issues/276355?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276398

https://github.com/issues/276398?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276403

https://github.com/issues/276403?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276489

https://github.com/issues/276489?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276760

https://github.com/issues/276760?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276714

https://github.com/issues/276714?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276516

https://github.com/issues/276516?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Performance and Responsiveness Problems:

Users frequently experience slow or unresponsive behavior in VS Code extensions, including long delays in summarizing conversation history, repeated "Sorry, no response was returned" errors, and severe performance degradation after updates or plan upgrades. These issues affect multiple platforms and extension versions, causing frustration and loss of productivity.

issues/276829

https://github.com/issues/276829?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276418

https://github.com/issues/276418?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276593

https://github.com/issues/276593?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277594

https://github.com/issues/277594?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277333

https://github.com/issues/277333?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277636

https://github.com/issues/277636?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276783

https://github.com/issues/276783?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Quota, Rate Limiting, and Subscription Access Issues:

Several reports highlight problems with quota resets not occurring as expected, users being incorrectly rate limited despite having active Pro subscriptions, and extensions showing messages about reaching monthly chat message limits erroneously. These issues cause confusion and restrict access to paid features.

issues/276383

https://github.com/issues/276383?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276391

https://github.com/issues/276391?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276530

https://github.com/issues/276530?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276536

https://github.com/issues/276536?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276482

https://github.com/issues/276482?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276594

https://github.com/issues/276594?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276706

https://github.com/issues/276706?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277503

https://github.com/issues/277503?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277483

https://github.com/issues/277483?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277484

https://github.com/issues/277484?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277916

https://github.com/issues/276916?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Request Failures Due to Invalid JSON or Attachment Issues:

Numerous bugs report requests failing with 400 errors caused by invalid JSON format in tool call arguments or inaccessible attachments, leading to failed operations and error messages like "vision\_attachment\_not\_accessible." These failures occur across various extension versions and platforms, disrupting normal usage.

issues/276412

https://github.com/issues/276412?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276436

https://github.com/issues/276436?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276467

https://github.com/issues/276467?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276701

https://github.com/issues/276701?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276925

https://github.com/issues/276925?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277018

https://github.com/issues/277018?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277361

https://github.com/issues/277361?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277466

https://github.com/issues/277466?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277478

https://github.com/issues/277478?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277600

https://github.com/issues/277600?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277111

https://github.com/issues/277111?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277475

https://github.com/issues/277475?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Chat History and Session Persistence Problems:

Users report that chat histories do not save or persist correctly, with TODO tasks leaking between sessions and resumed chats losing context, causing loss of conversation continuity and user frustration.

issues/276445

https://github.com/issues/276445?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276573

https://github.com/issues/276573?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277476

https://github.com/issues/277476?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277328

https://github.com/issues/277328?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Extension Host and Crash Issues:

Several reports describe the VS Code extension host or the entire application crashing or becoming unresponsive, sometimes linked to specific extension versions or system configurations, causing loss of work and requiring restarts.

issues/276379

https://github.com/issues/276379?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276399

https://github.com/issues/276399?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277355

https://github.com/issues/277355?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277527

https://github.com/issues/277527?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277647

https://github.com/issues/277647?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### User Interface and Usability Bugs:

Problems include the Up Arrow key in Agent mode deleting unsubmitted messages without recovery, suggestion overlays blocking views, missing or hidden UI buttons (e.g., commit button, terminal tabs), and cluttered context menus, all negatively impacting user experience.

issues/276373

https://github.com/issues/276373?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276711

https://github.com/issues/276711?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277409

https://github.com/issues/277409?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277174

https://github.com/issues/277174?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276841

https://github.com/issues/276841?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

, \[issues/277317\](https://github.com/issues/277317\]

#### Security Vulnerabilities and Data Exposure:

A critical remote code execution vulnerability was found where prompt injection in agent mode could bypass file editing guards to modify sensitive files, which was fixed by validating file paths. Additionally, accidental exposure of sensitive data in public repositories was reported.

issues/276771

https://github.com/issues/276771?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276772

https://github.com/issues/276772?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277267

https://github.com/issues/277267?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Model and Feature Functionality Failures:

GPT-5 and other advanced models sometimes fail to respond or cut off mid-response, and features like "plan mode" disappear after updates. The Copilot extension also sometimes generates destructive or nonsensical code, reducing trust and usability.

issues/276386

https://github.com/issues/276386?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276432

https://github.com/issues/276432?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276456

https://github.com/issues/276456?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276481

https://github.com/issues/276481?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276780

https://github.com/issues/276780?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277178

https://github.com/issues/277178?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

, \[issues/277616\](https://github.com/issues/277616\],

issues/277491

https://github.com/issues/277491?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277627

https://github.com/issues/277627?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Rate Limiting and Token Expiry Errors:

Users encounter frequent rate limiting and token expiration errors (403), causing failed requests and interruptions in service despite active subscriptions, leading to repeated error messages and blocked usage.

issues/277039

https://github.com/issues/277039?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277159

https://github.com/issues/277159?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276936

https://github.com/issues/276936?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277891

https://github.com/issues/276891?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

, \[issues/277916\](https://github.com/issues/276916\]

#### File and Code Corruption Issues:

Bugs include corrupted files due to overlapping replacements, incomplete or truncated code snippets, and destructive behavior by the Copilot extension, causing loss of code integrity and user trust.

issues/276705

https://github.com/issues/276705?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277113

https://github.com/issues/277113?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277154

https://github.com/issues/277154?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277146

https://github.com/issues/277146?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

, \[issues/277639\](https://github.com/issues/277639\]

#### Authentication and Account Management Problems:

Users report repeated logouts from Microsoft Account Authentication, issues with GitHub sign-in for Copilot, and incorrect subscription status displays, complicating access and usage.

issues/276522

https://github.com/issues/276522?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276527

https://github.com/issues/276527?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276692

https://github.com/issues/276692?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

, \[issues/277098\](https://github.com/issues/277098\]

#### Miscellaneous Bugs and Feature Requests:

Other issues include requests for keyboard shortcuts, UI improvements like nested peek windows, manual file reordering, and better error message handling, as well as bugs in syntax highlighting, terminal suggestions, and extension installation.

issues/276460

https://github.com/issues/276460?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276466

https://github.com/issues/276466?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276520

https://github.com/issues/276520?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276512

https://github.com/issues/276512?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/276579

https://github.com/issues/276579?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

, \[issues/276647\](https://github.com/issues/276647\],

issues/277443

https://github.com/issues/277443?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

issues/277470

https://github.com/issues/276470?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

2.5 Issue Discussion Insights

This section will analyze the tone and sentiment of discussions within this project's open and closed issues that occurred within the past week. It aims to identify potentially heated exchanges and to maintain a constructive project environment.

https://github.com/microsoft/vscode/issues/276782?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

Toxicity Score: 0.75 (Rapid escalation potential, aggressive language, strong negative sentiment)

This GitHub conversation consists of a single initial comment by one user expressing extreme frustration and anger about a performance issue, using aggressive and profane language. There are no responses or further comments, so the tone remains highly negative but unchallenged. The lack of interaction leaves the situation unresolved, with potential for escalation if others respond.

https://github.com/microsoft/vscode/issues/276786?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

Toxicity Score: 0.65 (Rapid escalation, aggressive language, explicit frustration)

This GitHub conversation involves a single user expressing strong dissatisfaction with a tool, using explicit language to convey frustration. The tone is negative and blunt, with no responses or further discussion visible to moderate or escalate the sentiment. The lack of engagement suggests a stagnant conversation with potential for increased negativity if others respond defensively or dismissively.

https://github.com/microsoft/vscode/issues/276417?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

Toxicity Score: 0.75 (Rapid escalation potential, aggressive language, lack of moderation)

This GitHub conversation consists of a single initial comment by one user expressing strong negative sentiment with aggressive and repetitive language, without any responses or further interaction. The tone is highly confrontational and dismissive, but no dialogue or escalation occurs due to the absence of replies.

Princess Lala

https://github.com/microsoft/vscode/issues/276424?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

Toxicity Score: 0.65 (Rapid escalation, dismissive response, potential trolling)

This GitHub conversation involves a user expressing personal difficulty and frustration in understanding a concept due to platform limitations, using a lighthearted and self-deprecating tone. Another participant responds with a brief, dismissive comment that could be interpreted as spam or trolling, potentially escalating tension. The interaction shows a contrast between a vulnerable expression and a curt, possibly antagonistic reply, which may trigger further negative exchanges.

DESTRUCTIVE CODE

https://github.com/microsoft/vscode/issues/276780?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

Toxicity Score: 0.55 (Moderate possibility, escalating frustration, dismissive responses)

This GitHub conversation involves a user expressing dissatisfaction with the service and another user responding with frustration, indicating a breakdown in communication and mutual understanding. The tone is increasingly confrontational, with both parties showing signs of impatience and dissatisfaction, triggered by perceived neglect and unmet expectations.

https://github.com/microsoft/vscode/issues/277146?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

Toxicity Score: 0.85 (Rapid escalation, aggressive language, offensive slurs)

This GitHub conversation involves a user posting a highly offensive and aggressive issue report, followed by a bot responding with a standard, neutral message suggesting an update. The initial comment sets a hostile and toxic tone, but the bot's reply is calm and procedural, without escalation. There is no evidence of further human interaction or de-escalation attempts.

You guys are really stupid. Why did you hide the quick icon for the Git commit panel?”

https://github.com/microsoft/vscode/issues/277317?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

Toxicity Score: 0.75 (Rapid escalation potential, aggressive language, insulting tone)

This GitHub conversation begins with a single user posting a highly critical and insulting comment directed at the development team, expressing strong dissatisfaction in a confrontational tone. There are no subsequent comments or responses, so the conversation remains one-sided with a negative sentiment. The initial post's aggressive language and direct insults create a tense atmosphere, but without further interaction, the conversation does not escalate.

https://github.com/microsoft/vscode/issues/277553?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

Toxicity Score: 0.65 (Rapid escalation, accusatory tone, user frustration)

This GitHub conversation involves a user expressing significant frustration and confusion regarding an upgrade process and billing issues, with a tone that is urgent and somewhat accusatory. The initial comment sets a tense atmosphere by highlighting dissatisfaction and perceived malfunction, which may provoke defensive or clarifying responses from maintainers or other users. The sentiment is predominantly negative, and the language used suggests a high level of user distress, potentially escalating tensions if responses are not empathetic or clear.

Github Copilt is useless

https://github.com/microsoft/vscode/issues/277639?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

Toxicity Score: 0.85 (Rapid escalation, aggressive language, repeated accusations, one-sided negativity)

This GitHub conversation consists solely of repeated comments from the same user expressing intense frustration and dissatisfaction with a software feature, using accusatory and emotionally charged language. The tone is highly negative and confrontational, with no engagement or responses from other participants, indicating a one-sided venting rather than a dialogue. The repetition of identical comments suggests escalating agitation and a lack of constructive interaction.

III. Pull Requests

3.1 Open Pull Requests

This section provides a summary of pull requests that were opened in the repository over the past week. The top three pull requests with the highest number of commits are highlighted as 'key' pull requests. Other pull requests are grouped based on similar characteristics for easier analysis. Up to 25 pull requests are displayed in this section, while any remaining pull requests beyond this limit are omitted for brevity.

#### Pull Requests Opened This Week:

#### Key Open Pull Requests

1. Align tool names and add support for legacy reference identification:

This pull request aims to unify tool names within the project by introducing a system that supports deprecating old names while maintaining backwards compatibility, thereby enabling extension authors to adopt similar capabilities.

pull/277047

https://github.com/microsoft/vscode/pull/277047?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Associated Commits:

https://github.com/microsoft/vscode/commit/216668b973152e10fc19687f2513e7e624185b49?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/4e9bc9471f9d96bb597191fbaf2fccc0986440a2?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/eaeecb4c3f55114dae9bd479033447c65b4d3db6?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/24d4aff806ff3de063e0ed04df95ecb274e1578a?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/eaa81ca9390dc5e42e8597c62478eb838dcd702f?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/9f9aaa73d04849ebbf9f9696bac1f717a71fe8ed?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/ec3378fdb9152f44a6885b136c5487c239206bd5?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/16eefd82ace6973170b4c0e0fbdd521c12fd8e32?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/b2e361eb061ab24687a7f36327fd03951e77c10c?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/4accf61948a50460f9f2e7edf4018ed317200de2?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/296e5db3280571fb7c5b9b24bc813dddb27bfab2?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/5be166787261af9942ba5a5e1298d8ad25e000e9?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/6f6737f11f2025d41684dacb62b6ec2461eba08d?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/d675bf2acbf09e80c2b0bac940cf8826210dc1f6?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/e48cb722b20f1d1d16af4c322a841d59201b867d?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/cdddba749e85632257ed049af58b1d043138521c?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

2. Insider builds should have an auto increasing version number:

This pull request proposes implementing an automatic version number incrementing system for Insider builds in the Visual Studio Code project to ensure each build has a unique, sequential version identifier.

pull/277497

https://github.com/microsoft/vscode/pull/277497?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Associated Commits:

https://github.com/microsoft/vscode/commit/4e815fcdc6a45a8951e3f8f551b53fa6af6ba6cf?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/97db8cba2221d78ef0e38f5868b456f74e5f85fb?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/23c5e9e6634bbd7fdc7783ace2436954777d01cd?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/a32a5fb97402f7112d03242587e27dd06dcc6f56?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/527cebeefc671dc6078cc6ea2ab62394534e9bc2?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/0e1b43021dc02e803b035b1664e903ccd09f1c51?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/f7c06f491ca376a9d288259d7e62e51c1a7c7a3d?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/082f78f2a54d94a7dbf8630feab1321174629b28?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/57b2714944c0d72c307923dd982bdd096d99ae29?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/edf655055ddf614a42a871567b7830580c2b6ab4?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/7cb22a5afaead2361eab5ac175272c7c2b54ed0a?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/317bdef068b6b692775e16924dc5b210f86127e9?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/0f159c2ff3fafde1491f3340fd14910c874c56a8?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

3. Run our build scripts directly as typescript:

This pull request updates the project's build scripts to run directly as TypeScript by converting files to ES modules, replacing Node.js-specific patterns like

import.meta

, enabling syntax-only mode for TypeScript files, updating script references to use

extensions, and removing all checked-in compiled JavaScript files to streamline future script conversions and improve build management.

pull/277567

https://github.com/microsoft/vscode/pull/277567?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Associated Commits:

https://github.com/microsoft/vscode/commit/54999f05f3995d63095249f6b771b8176a82b63a?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/aa3c180433bb74772bc761af914f77a632c66656?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/639e5169cf259ba9fbd34615826e88d6c51131db?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/9e03b7a10b68e16a7f3d3c878141f660d344e8d8?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/dcc9edbbd3c972fed20d1783351e81125ced8dfa?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/4d8859b784447a14c9f375cbb0d8bee1cae7e510?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/b724bdea2e5b1a6f271fa15532f6a51e072abbd2?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/31f73ebef4354dbbcb9385d0f1a93366f1786edc?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/d6728e6dd4aaa2dd4533bc205f69afba4a43dfb8?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/eef7eb5bad7d75f4cd337ce3417ee8554e94a02b?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/fdba5bc19941c0eeed6fe8d7e6f92ee2998edc59?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/b13a3d141e0587b0fbd6c160c542a5f591b508f2?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

Other Open Pull Requests

#### Node.js and npm version enforcement:

This pull request adds an "engines" field to the root package.json to specify minimum required versions of Node.js (>=18.0.0) and npm (>=9.0.0), ensuring users and contributors are warned if their environment does not meet these requirements. This change addresses issue #252372 to improve environment consistency.

pull/276957

https://github.com/pull/276957?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Diff mode stdin argument handling:

This pull request fixes the handling of the

argument representing stdin in diff mode by replacing it in-place with the stdin temporary file path, preserving its original position. It also improves support for multiple

occurrences, backward compatibility, and chat mode behavior.

pull/277601

https://github.com/pull/277601?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Update notification progress enhancements:

This pull request enhances VS Code update notifications by displaying real-time download progress with percentage and estimated time remaining. It implements state management, platform-specific tracking for macOS and Windows, dynamic UI updates, edge case handling, and comprehensive unit tests.

pull/277331

https://github.com/pull/277331?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Tree component twistie customization and bug fix:

These pull requests introduce an option to specify an additional CSS class for the twistie element to enhance appearance customization and fix a bug where clicking expand/collapse icons caused multiple tree items to retain focus styling. The fix changes focus update logic to ensure only a single item shows focus after expand/collapse actions.

pull/276895

https://github.com/pull/276895?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

pull/276847

https://github.com/pull/276847?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Security and performance improvements in parsing and chat sessions:

This pull request refactors the parseLsFiles function to eliminate regular expressions and prevent ReDoS vulnerabilities using safer string methods. It also introduces a feature to prevent persistence of inline editor chat sessions.

pull/277051

https://github.com/pull/277051?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Terminal tabs memory leak fix:

This pull request addresses a memory leak in the terminal tabs list by changing TabsRenderer from Disposable to non-Disposable and adopting templateDisposables and elementDisposables for element disposal, eliminating the leak as confirmed by testing.

pull/277225

https://github.com/pull/277225?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Simple browser console error logging enhancement:

This pull request reintroduces and enhances logging for console errors within the simple browser feature, incorporating extensive Chrome DevTools work to enable console logs to be displayed in the chat interface.

pull/277293

https://github.com/pull/277293?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Terminal clipboard copyOnSelection fix:

This pull request prevents the terminal's copyOnSelection feature from overwriting the clipboard when the find widget highlights search results by adding a guard in TerminalClipboardContribution to block copying if the selection originates from the find widget rather than user action.

pull/276641

https://github.com/pull/276641?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### TypeScript language features tsconfig "extends" path resolution fix:

This pull request updates TypeScript language features to correctly resolve tsconfig.json "extends" paths that use package exports subpath remapping, fixing module resolution failures and aligning with TypeScript's logic.

pull/276959

https://github.com/pull/276959?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Microsoft-authentication extension cleanup:

This pull request removes deprecated migration code and async factory methods from the microsoft-authentication extension, simplifying public client application construction and storage handling by eliminating legacy upgrade logic and updating calling code.

pull/277022

https://github.com/pull/277022?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Hot reload launch configuration and CI updates:

This pull request introduces a hot reload launch configuration along with environment setting updates and continuous integration fixes.

pull/277123

https://github.com/pull/277123?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Editor word wrap visual indicators and minified file wrapping control:

These pull requests add an optional editor feature displaying a subtle visual indicator (↩) at soft word wrap points controlled by

editor.renderWordWrapIndicator

, and introduce

editor.wordWrapMinified

to control automatic word wrapping for files with very long lines, fixing unwanted forced wrapping.

pull/277516

https://github.com/pull/277516?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

pull/277521

https://github.com/pull/277521?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Accessibility fix for filter input in panels:

This pull request fixes an accessibility issue where filter inputs become unclickable due to overlapping badges blocking pointer events by disabling pointer events on the badge container while preserving toolbar button interactivity.

pull/276476

https://github.com/pull/276476?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Type definition update for getWorker functions:

This pull request updates type definitions for getWorker and getWorkerUrl functions to include undefined as a possible return type, ensuring type correctness after rebasing and conflict resolution.

pull/276555

https://github.com/pull/276555?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Hover widget layout and style improvements:

This pull request improves the hover widget layout and spacing by refactoring styles, removing unused CSS rules, and adjusting codicon sizes for better UI alignment.

pull/276702

https://github.com/pull/276702?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Experimental Copilot terminal command history exclusion:

This pull request implements a new experimental setting to prevent Copilot-generated terminal commands from being recorded in shell history by prefixing them with a leading space, supporting Bash, Zsh, and Fish shells, and modifies command execution strategies accordingly.

pull/276718

https://github.com/pull/276718?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Welcome/Getting Started SVG files standardization:

This pull request standardizes and refactors 18 Welcome/Getting Started SVG files by adding over 475 missing fallback colors, normalizing hex color casing, fixing malformed syntax, and ensuring consistent fallback values aligned with the Dark Modern theme to prevent rendering issues.

pull/276939

https://github.com/pull/276939?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Enterprise deployment policies for admin contact info:

This pull request introduces new enterprise deployment policies allowing admins to configure hidden contact information settings displayed in system policy lock messages to provide actionable admin support details when settings are blocked.

pull/277232

https://github.com/pull/277232?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Tools Picker expand/collapse state preservation:

This pull request fixes the Tools Picker to preserve expand/collapse state of tool buckets between invocations by introducing a stable identity provider for tree elements, enabling consistent state across data updates.

pull/277348

https://github.com/pull/277348?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### VSBuffer BOM preservation regression test:

This pull request adds a regression test to verify that the VSBuffer class correctly preserves the Byte Order Mark (BOM) character in filenames when converting buffers to strings, validating the fix for issue #251527.

pull/277608

https://github.com/pull/277608?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Extensions marketplace @allowed filter:

This pull request introduces a new

filter to the extensions marketplace, enabling users to query and display only extensions permitted by organizational policy by integrating

IAllowedExtensionsService

and implementing corresponding filtering logic.

pull/276488

https://github.com/pull/276488?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Output filter toggle button styling fix:

This pull request adds minimal CSS to introduce spacing and a border around the output filter toggle button for visual consistency with the find widget across all FilterViewPane instances.

pull/276493

https://github.com/pull/276493?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

3.2 Closed Pull Requests

This section provides a summary of pull requests that were closed in the repository over the past week. The top three pull requests with the highest number of commits are highlighted as 'key' pull requests. Other pull requests are grouped based on similar characteristics for easier analysis. Up to 25 pull requests are displayed in this section, while any remaining pull requests beyond this limit are omitted for brevity.

#### Pull Requests Closed This Week:

#### Key Closed Pull Requests

1. Use ts-node to run our build scripts:

This pull request proposes running the project's build scripts directly as TypeScript using ts-node to simplify their conversion to TypeScript, eliminate checked-in compiled JavaScript files, and enable direct execution of these scripts with node, while making necessary adjustments such as adding a helper to run scripts with the ts-node loader, converting modules to ES modules, and removing compiled files, though it remains a work in progress with some platform-specific issues unresolved.

pull/276864

https://github.com/microsoft/vscode/pull/276864?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Associated Commits:

https://github.com/microsoft/vscode/commit/cd7063b1991db8f04c1b8a54fe1e5c62856e2159?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/7a3716c1d226761f119ea0f55076e254a0adb35b?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/24f49054e73ea1ab3d41576b4d257849978a2eca?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/9124e660187d72f68ecb199bd5675b74b0a5c003?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/b951fa69d3fb76e26a8fea6bc2f953f2b45f3b61?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/f40a03439725f1d3e0620a259e29d42d816ef777?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/a58e876515e7827d37edc280f4395f7f4448cc3a?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/207699d337197e2358a5391f4f8c32540ebd672e?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/117cff06bccf4dcaf68e6d75c489641e4f84fe6a?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/ff87cc3dbc814c987acd92754d2bb468c181728c?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/3bdc4c27efcaf3cb1b419fbab54146c6dd95ec47?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/b3af3e9c90b2763bc7df485d4bc51219e138a3b4?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/09d002641330395a0ca7e7d41aedf221f3f429a1?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/3ab4c7709be41f315dbe7edde4c3f8cf4b3691f5?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/8b602cd946edda82ca87e97cacf460779f0e5baa?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/d5fbeee5b101aa3f9366b393d18f5965d0b0a102?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/57eea59f505280e206cc1ccc5cc2359befd72e8d?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/cd9be9fadc6cc952f46c2eb04350f01264579f0e?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/839cd0c4f57bb8c32997553999e3915f2671cedc?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/7919c19531f74c2ec4fadc465e023bdeada607f8?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/a86be9fe800ae96251e8b0d9cb59aae397db4866?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/1122cf00821f4e141bfd6acaa3109fac52426c37?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/37e082424cd98d99eea71a00df644f203bb2b95b?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/c92c11e02592c9ede43bc9c9caa4cd4719dff174?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/83c4dcdbaa3d9548e72bd8b245cc7c0abedad032?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/f7f2e973b5eec82b0c8700da8ead4fa5389ac203?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/aa1e8ff76b3240c5998c555cac985f76dd299a3f?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/1325ac679f2b47a95defcbe64c8865e3ec9bb854?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/61c3c8c829f935d5b2e106f4c72969762cda184c?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

2. extract ChatTerminalToolOutputSection , fix a bug:

This pull request extracts the

ChatTerminalToolOutputSection

component and fixes a bug where focus could unexpectedly move to an incorrect terminal or output element due to list re-rendering by tracking each part's position in the list, ensuring that keyboard focus always targets the most recent response in the chat terminal.

pull/277234

https://github.com/microsoft/vscode/pull/277234?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Associated Commits:

https://github.com/microsoft/vscode/commit/04e52cd378a573f738f95586ec300e9ecf87c4a2?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/163d4afe97cb3830e33a1b9dd481c099818b5344?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/805caa51f8d4362c7cb3270d334bcecff5708888?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/071ede1804b7407d84175ec21f7b09f2d844bef7?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/fe548e2f5c4c2f2f59a266bf83b6b56f9b8a44f0?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/a758f612a1ce7f6335817552014e6f8e5440754b?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/280057743ede0650699203a2b7fc4db970ef4f21?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/1e7bd4245210118eabbf23464a635230f4f15ca0?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/cde3badda6b8b25806e2f5844916ed710d00c60e?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/63278d202f808a289e1de88845fd6ab1f9ec627f?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/b977f8bd120cd3561b22f5c7425cf8583cbf1d82?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/23dd171cb843b466dd81210d8ad04e528f623327?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/8da1c58f676974f733a598840c1ef87020eff04c?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/b45b232541bd2d662d3e8697fa18bf41011dcee6?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/ff79b47f049157f119392bf18ef0a3707671d588?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/7d0ad3e809158def3732e25e21fb5f0c8dc9b2bf?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/43f46bb4405334ba5b16708299de074b06914152?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/5664a1811329256ba236becef57576f10abb881c?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

3. Add eligibleForAutoApproval :

This pull request introduces the

eligibleForAutoApproval

setting to control which tools in VS Code are eligible for automatic approval, ensuring that tools marked as ineligible always require user confirmation and never offer auto-approval options, while maintaining default behavior for others and accounting for global auto-approve settings.

pull/277043

https://github.com/microsoft/vscode/pull/277043?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Associated Commits:

https://github.com/microsoft/vscode/commit/db4d0d3fb0ca7383bf9e2694e11ff5c79c4bca1f?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/3377eb6cad3db2e4057123c1fa0047bbc24073b7?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/1baa184c1c5943a73a214c48312e7cee3df66b17?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/5b78083fcb03aa408ece241edfbaa393befb0367?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/3e8a95516d54869386ac450427b2b02c38f348fc?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/94fd6ed2d1409adf4ec5578050e56647c0aaf9ef?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/142aae08b020b83fa1c284960e5404a33043afc1?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/ea28186ba3c5294ca003caa1192e1b4234efae17?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/d337f101e62fa6f65b88746133af46d088de8741?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/943acda15e192a68307bc9143ebbd59d8eeda2ac?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/eee7697d4fe7966526102b576b298fc87c7fe870?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

https://github.com/microsoft/vscode/commit/6c2a71030d5851518a56a096d64491c4e5332e7c?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

Other Closed Pull Requests

#### Versioning and Build Pipeline Enhancements:

This topic covers the implementation of an auto-incrementing patch versioning system for Insider builds in the Azure DevOps pipeline, introducing a pipeline-level counter scoped to the major.minor version and a ReadVersion job to validate version consistency with

package.json

. The patch number is incremented before building platform-specific distributables, ensuring unique Insider build versions while requiring manual updates of the major.minor parameter on version changes.

pull/277116

https://github.com/pull/277116?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Enterprise Policy Configuration for Chat Tools:

These pull requests add support for enterprise policy configuration of the

chat.tools.eligibleForAutoApproval

setting, allowing administrators to control auto-approval of chat tools via JSON-based policies. The changes update policy generation infrastructure and tests, ensuring policy overrides user settings to enforce confirmation for ineligible tools.

pull/277238

https://github.com/pull/277238?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Terminal Command Persistence and Output Improvements:

This group includes persistence of terminal commands and outputs after terminal termination and enhancements to terminal focus actions to navigate to relevant commands after reloads. Additionally, improvements in detecting questions and password requests in terminal output by analyzing more lines address longer outputs from tools like

pull/276601

https://github.com/pull/276601?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

pull/276572

https://github.com/pull/276572?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Terminal Suggest Widget and Suggestion Grouping Enhancements:

These pull requests fix layout issues in the terminal suggest widget by aligning its behavior with the content suggest widget and propose allowing the SimpleSuggestWidget detail pane to be set to the right side to prevent blocking terminal input. They also enhance terminal suggestions by including persistent options and improving logical grouping of suggestions.

pull/276631

https://github.com/pull/276631?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

pull/276409

https://github.com/pull/276409?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

pull/276622

https://github.com/pull/276622?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Code Quality and Type Safety Improvements:

This topic covers the removal of the 'any' type from terminal-related code to improve type safety and the cleanup of eslint exemptions to enhance code quality and maintain linting consistency.

pull/276490

https://github.com/pull/276490?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

pull/276581

https://github.com/pull/276581?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Build Process and Tooling Updates:

These pull requests update the build process to use the latest TypeScript version, remove deprecated settings, fix related smoke test issues, and add a TypeScript Go watcher with watch mode and localization support to enhance language features.

pull/276534

https://github.com/pull/276534?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

pull/276749

https://github.com/pull/276749?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

pull/276751

https://github.com/pull/276751?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Memory and Resource Leak Fixes:

This group addresses memory leak errors caused by asynchronous updates on disposed ChatThinkingContentParts and fixes proxy disposable issues to ensure proper resource management without breaking functionality. It also fixes a resource leak in the MainThreadTerminalService by extending Disposable and properly registering disposables.

pull/277264

https://github.com/pull/277264?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

pull/276556

https://github.com/pull/276556?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

pull/276538

https://github.com/pull/276538?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### UI and Styling Improvements:

These pull requests improve the editing pills feature by enhancing animation, CSS styling, layering, and clarity, and refactor the comment widget by replacing dynamic inline CSS with static CSS files using CSS variables to simplify theming and improve performance.

pull/276979

https://github.com/pull/276979?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

pull/276479

https://github.com/pull/276479?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Chat Sessions and Delegate Menu Enhancements:

This pull request introduces a

canDelegate

flag to the

IChatSessionsExtensionPoint

interface and schema, allowing extensions to opt out of appearing in the delegate menu and filtering out external agents like OpenAI Codex to prevent them from showing alongside coding agents.

pull/276991

https://github.com/pull/276991?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Git Worktree Command Enhancements:

This pull request enhances the

git.createWorktreeWithDefaults

command by adding a

migrateUncommittedChanges

parameter that migrates all uncommitted changes to a new worktree using stash-and-apply, while handling repository registration and merge conflicts.

pull/276985

https://github.com/pull/276985?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### OAuth Metadata Discovery Robustness:

This pull request improves OAuth metadata discovery by adding robust error handling to the

fetchAuthorizationServerMetadata

function, catching network errors, retrying all OAuth discovery endpoints before failing, and including comprehensive tests for various failure scenarios.

pull/276749

https://github.com/pull/276749?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Quick Pick and Editor Error Fixes:

These pull requests fix issue #275068 by ignoring double-click events on Quick Pick titles when the target is a button to prevent unintended interactions, and fix the "Illegal value for lineNumber" error by adjusting parameters and adding test coverage for out-of-bounds line and column values.

pull/276810

https://github.com/pull/276810?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

pull/276902

https://github.com/pull/276902?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Prompt Service Caching Improvements:

This pull request adds caching to the

listPromptFiles

function in the PromptsService to ensure consistency with existing caching for slash commands and custom agents.

pull/277258

https://github.com/pull/277258?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Agents View Cleanup:

This pull request removes the history custom node from the agents view and related code cleanups, including grouping and using archives instead.

pull/276642

https://github.com/pull/276642?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

#### Manage Accounts Navigation Improvement:

This pull request enables the Back button functionality on the Manage Accounts picker in the authentication workflow, improving navigation within account management.

pull/276622

https://github.com/pull/276622?utm\_source=weekly-project-news&utm\_medium=email&utm\_campaign=weekly-github-report-for-vscode-november-10-2025

3.3 Pull Request Discussion Insights

This section will analyze the tone and sentiment of discussions within this project's open and closed pull requests that occurred within the past week. It aims to identify potentially heated exchanges and to maintain a constructive project environment.

Based on our analysis, there are no instances of toxic discussions in the project's open or closed pull requests from the past week.

IV. Contributors

4.1 Contributors

#### Active Contributors:

We consider an active contributor in this project to be any contributor who has made at least 1 commit, opened at least 1 issue, created at least 1 pull request, or made more than 2 comments in the last month.

If there are more than 10 active contributors, the list is truncated to the top 10 based on contribution metrics for better clarity.

Contributor

Pull Requests

#### Don't miss what's next. Subscribe to Weekly Project News:

https://github.com/owner/public\_repo\* Your email (you@example.com) Subscribe

https://buttondown.com/refer/weekly-project-news

, the easiest way to start and grow your newsletter.

Subscribe to Weekly Project News

Unsubscribe

Are you sure you want to unsubscribe? You will no longer receive emails from this newsletter.

Cancel Unsubscribe

Almost there...

We just sent you an email to confirm your address at . Click it and you're in!

I've confirmed!

