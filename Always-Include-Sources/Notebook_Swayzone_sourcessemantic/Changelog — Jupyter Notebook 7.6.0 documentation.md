---
sourceFile: "Changelog — Jupyter Notebook 7.6.0 documentation"
exportedBy: "Kortex"
exportDate: "2026-06-26T04:27:51.153Z"
---

# Changelog — Jupyter Notebook 7.6.0 documentation

3659aadf-f07d-4dbf-ab2d-fd2d6a9bce1c

Changelog — Jupyter Notebook 7.6.0 documentation

2ec4365f-c2da-453f-9c0e-cf4f60781f15

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html

Changelog — Jupyter Notebook 7.6.0 documentation

Skip to main content

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#main-content

Back to top

JupyterJupyter

https://jupyter-notebook.readthedocs.io/en/stable/index.html

Documentation

https://jupyter-notebook.readthedocs.io/en/stable/user-documentation.html

Configuration

https://jupyter-notebook.readthedocs.io/en/stable/configuration.html

https://jupyter-notebook.readthedocs.io/en/stable/migrate\_to\_notebook7.html

Contributing

https://jupyter-notebook.readthedocs.io/en/stable/contributor.html

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html

System Settings

https://github.com/jupyter/notebook

https://discourse.jupyter.org/c/notebook/31

Documentation

https://jupyter-notebook.readthedocs.io/en/stable/user-documentation.html

Configuration

https://jupyter-notebook.readthedocs.io/en/stable/configuration.html

https://jupyter-notebook.readthedocs.io/en/stable/migrate\_to\_notebook7.html

Contributing

https://jupyter-notebook.readthedocs.io/en/stable/contributor.html

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html

System Settings

https://github.com/jupyter/notebook

https://discourse.jupyter.org/c/notebook/31

Collapse Sidebar Expand Sidebar

Section Navigation

The Jupyter Notebook

https://jupyter-notebook.readthedocs.io/en/stable/notebook.html

User interface components

https://jupyter-notebook.readthedocs.io/en/stable/ui\_components.html

New features in Notebook 7

https://jupyter-notebook.readthedocs.io/en/stable/notebook\_7\_features.html

Notebook Examples

https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/examples\_index.html

What is the Jupyter Notebook?

https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/What%20is%20the%20Jupyter%20Notebook.html

Notebook Basics

https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Notebook%20Basics.html

Running Code

https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Running%20Code.html

Markdown Cells

https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Working%20With%20Markdown%20Cells.html

Keyboard Shortcut Customization

https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Custom%20Keyboard%20Shortcuts.html

Importing Jupyter Notebooks as Modules

https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Importing%20Notebooks.html

Connecting to an existing IPython kernel using the Qt Console

https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Connecting%20with%20the%20Qt%20Console.html

Motivating Examples

https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Typesetting%20Equations.html

Applying Custom CSS

https://jupyter-notebook.readthedocs.io/en/stable/custom\_css.html

Managing plugins

https://jupyter-notebook.readthedocs.io/en/stable/configuring/plugins.html

Interface Customization

https://jupyter-notebook.readthedocs.io/en/stable/configuring/interface\_customization.html

What to do when things go wrong

https://jupyter-notebook.readthedocs.io/en/stable/troubleshooting.html

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html

$ lightcone run "what can I do for you?" — agents that actually act. Try the API →

https://server.ethicalads.io/proxy/click/10604/019f0192-a135-71d3-b7a2-9c4242c9dea1/

Ad by EthicalAds

https://www.ethicalads.io/advertisers/topics/data-science/?ref=rtd-sidebar-buy-ads

Documentation

https://jupyter-notebook.readthedocs.io/en/stable/user-documentation.html

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#changelog

A summary of changes in the Jupyter notebook. For more detailed information, see

https://github.com/jupyter/notebook

pip install notebook --upgrade

conda upgrade notebook

to upgrade to the latest release.

We strongly recommend that you upgrade pip to version 9+ of pip before upgrading

pip install pip --upgrade

to upgrade pip. Check pip version with

pip --version

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id1

Jupyter Notebook 7.6 is based on JupyterLab 4.6, and includes a number of new features, bug fixes, and enhancements for extension developers. This release is compatible with extensions supporting JupyterLab 4.0. Extension authors are recommended to consult the

Extension Migration Guide

https://jupyterlab.readthedocs.io/en/latest/extension/extension\_migration.html#jupyterlab-4-5-to-4-6

which lists deprecations and changes to the public API.

Below are a few highlights for this new release. Most of the new features and improvements come from the update to JupyterLab 4.6, although they may not all be supported in Notebook 7.6.

For reference you may have a look at the

JupyterLab 4.6 changelog

https://jupyterlab.readthedocs.io/en/latest/getting\_started/changelog.html#v4-6

to learn more.

Scratchpad console

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#scratchpad-console

A scratchpad console can now be opened next to a notebook, sharing the same kernel. This makes it easy to run quick experiments or inspect variables without modifying the notebook itself.

The scratchpad console can be opened from the

Scratchpad console

menu, from the command palette, or with the Ctrl + B (or Cmd + B on macOS) keyboard shortcut, which toggles the console panel.

Confirmation dialog when closing and shutting down a notebook

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#confirmation-dialog-when-closing-and-shutting-down-a-notebook

The “Close and Shut Down Notebook” command now asks for confirmation before closing the browser tab and shutting down the kernel. The confirmation prompt can be disabled in the Settings Editor with the “Prompt for confirmation before closing and shutting down” setting.

Notebook improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#notebook-improvements

The cell toolbar delete button now shows a confirmation dialog to prevent accidental deletion. The “Do not ask me again” preference is persisted in the Cell Toolbar settings. The

keyboard shortcut is unaffected.

A new “Paste code cells without output” setting strips outputs and execution counts from code cells when pasting, producing clean cells without outputs which may be stale or untrusted.

Copy, cut, and paste text commands have been added to the notebook context menu. This feature requires permission to access the clipboard and may not work in Firefox depending on version and additional restrictions.

Two new navigation commands, “Select Last Modified Cell” and “Select Next Modified Cell”, allow jumping back and forward through recently edited cells. They are available from the command palette and as buttons in the Table of Contents toolbar.

Pressing Ctrl + B (or Cmd + B on macOS) while editing a Markdown cell wraps the selected text in bold formatting.

When exporting a notebook as HTML via

Save and Export Notebook As

, a dialog now asks whether to sanitize the HTML output before download.

File browser enhancements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#file-browser-enhancements

The breadcrumbs now support direct path editing with tab completion. Clicking the area behind the breadcrumbs opens an editable text field where pressing Tab completes the longest common prefix of matching subdirectories.

A new “Date Created” column can be enabled via the settings or by right-clicking the column headers. The latest

jupyter-server

+) is required for accurate values across operating systems.

A new “Open in Terminal” option in the context menu opens a terminal navigated to the selected directory.

Additional improvements include a configurable file name sort order and automatic clearing of the file filter when changing directories.

Debugger improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#debugger-improvements

An overlay with continue, step and stop buttons has been added, easing the control of the debugger steps. The Kernel Sources filter has been moved to the toolbar and now supports live filtering, making it easier to search through kernel source files while debugging.

Keyboard shortcuts

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#keyboard-shortcuts

Shortcuts can now be added from the Keyboard Shortcuts editor for any command, without having to write JSON in the Advanced Settings Editor.

“Find and Replace” has been added to the Edit menu with the Ctrl + H (or Cmd + H on macOS) keyboard shortcut.

Ctrl + Y has been added as a redo shortcut on Windows and Linux.

Pressing the 1 to 6 keys will no longer convert a focused code or raw cell to Markdown, avoiding accidental conversions. These shortcuts continue working on Markdown cells, switching the heading level.

Inline completion enhancements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#inline-completion-enhancements

Inline completion suggestions can now be rendered with syntax highlighting that matches the active editor language, with the “Ghost text syntax highlighting” setting. Ghost text is now also shown for all active cursors in a multi-cursor editing session.

Terminal enhancements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#terminal-enhancements

Pressing Shift + Enter in the terminal now inserts a newline without executing the current line.

Keyboard navigation and accessibility

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#keyboard-navigation-and-accessibility

The terminal no longer traps keyboard focus, allowing users to move focus away with the keyboard. Focus is now correctly restored after closing the command palette. Toolbar buttons now correctly reflect their pressed state for screen readers. The Keyboard Shortcuts settings panel has been updated to improve accessibility, and focus indicators have been improved across the interface.

Other improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#other-improvements

The “Launch Jupyter Notebook File Browser” command has been moved from the Help menu to the View menu.

Autocompletion heuristics were improved; the autocompletion (which remains opt-in) should no longer trigger in unexpected scenarios.

The output scroll overlay collapse icon is now visible regardless of the output size and scroll state.

The fonts used across components were standardized, and fonts specified by themes or overrides are respected in every component of the application.

Breaking changes

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#breaking-changes

Python 3.9 support has been dropped in this release.

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id2

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.5.1...ff72659087428132698ebe7ccfd7cf8a52ed9fba

Enhancements made

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#enhancements-made

Fix missing filebrowser features

https://github.com/jupyter/notebook/pull/7955

https://github.com/jtpio

Confirmation dialog before “Close and Shut Down Notebook”

https://github.com/jupyter/notebook/pull/7894

https://github.com/jtpio

Update to JupyterLab v4.6.0a3

https://github.com/jupyter/notebook/pull/7839

https://github.com/jtpio

Add PR template

https://github.com/jupyter/notebook/pull/7792

@KH-Coder865

https://github.com/KH-Coder865

https://github.com/andrii-i

Add a scratch-pad console to the notebook

https://github.com/jupyter/notebook/pull/7790

https://github.com/brichet

https://github.com/jtpio

Move launch-tree from help menu to view menu

https://github.com/jupyter/notebook/pull/7107

https://github.com/joaovml

https://github.com/jtpio

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#bugs-fixed

Prevent scratchpad console title to update

https://github.com/jupyter/notebook/pull/7843

https://github.com/brichet

https://github.com/jtpio

Fix toggling the side panels from menu

https://github.com/jupyter/notebook/pull/7799

https://github.com/brichet

https://github.com/jtpio

Maintenance and upkeep improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#maintenance-and-upkeep-improvements

Update to JupyterLab v4.6.0

https://github.com/jupyter/notebook/pull/7967

https://github.com/jtpio

Update to JupyterLab v4.6.0rc1

https://github.com/jupyter/notebook/pull/7966

https://github.com/jtpio

Bump form-data from 4.0.5 to 4.0.6

https://github.com/jupyter/notebook/pull/7961

https://github.com/jtpio

Bump dompurify from 3.4.0 to 3.4.10

https://github.com/jupyter/notebook/pull/7960

https://github.com/jtpio

Bump @babel/core from 7.23.0 to 7.29.6

https://github.com/jupyter/notebook/pull/7959

https://github.com/jtpio

Remove Python 3.15 pin on CI

https://github.com/jupyter/notebook/pull/7957

https://github.com/jtpio

Update to JupyterLab v4.6.0rc0

https://github.com/jupyter/notebook/pull/7949

https://github.com/jtpio

Pin GitHub Actions

https://github.com/jupyter/notebook/pull/7938

https://github.com/jtpio

https://github.com/Yann-P

Update to JupyterLab v4.6.0b1

https://github.com/jupyter/notebook/pull/7935

https://github.com/jtpio

Remove obsolete datetime warning filters

https://github.com/jupyter/notebook/pull/7933

https://github.com/Mirochill

https://github.com/goelakash

https://github.com/jtpio

Add UI test for opening file with editor factory

https://github.com/jupyter/notebook/pull/7931

https://github.com/goelakash

https://github.com/jtpio

Add UI test verifying no cell toolbar in file editor

https://github.com/jupyter/notebook/pull/7930

https://github.com/goelakash

https://github.com/jtpio

Update to JupyterLab 4.6.0b0

https://github.com/jupyter/notebook/pull/7923

https://github.com/jtpio

UI tests HTML report

https://github.com/jupyter/notebook/pull/7913

https://github.com/jtpio

@krassowski

https://github.com/krassowski

@jupyter/eslint-plugin

https://github.com/jupyter/notebook/pull/7911

@Darshan808

https://github.com/Darshan808

https://github.com/jtpio

Update to JupyterLab v4.6.0a5

https://github.com/jupyter/notebook/pull/7901

https://github.com/jtpio

Bump postcss

https://github.com/jupyter/notebook/pull/7899

https://github.com/jtpio

packageManager

package.json

https://github.com/jupyter/notebook/pull/7898

https://github.com/jtpio

jupyter-builder==0.0.8

@jupyterlab/builder

https://github.com/jupyter/notebook/pull/7895

https://github.com/jtpio

@Darshan808

https://github.com/Darshan808

@jupyter/builder

https://github.com/jupyter/notebook/pull/7893

https://github.com/jtpio

@krassowski

https://github.com/krassowski

Dependabot bumps

https://github.com/jupyter/notebook/pull/7892

https://github.com/jtpio

@jupyter/eslint-plugin

and fix lint

https://github.com/jupyter/notebook/pull/7891

@Darshan808

https://github.com/Darshan808

https://github.com/jtpio

https://github.com/jupyter/notebook/pull/7882

https://github.com/jtpio

https://github.com/Copilot

Fix lint warnings

https://github.com/jupyter/notebook/pull/7881

https://github.com/jtpio

@krassowski

https://github.com/krassowski

Add zizmor (github actions static analysis)

https://github.com/jupyter/notebook/pull/7880

https://github.com/Yann-P

https://github.com/Carreau

https://github.com/jtpio

@krassowski

https://github.com/krassowski

Update to JupyterLab v4.6.0a4

https://github.com/jupyter/notebook/pull/7859

https://github.com/jtpio

Fix check links

https://github.com/jupyter/notebook/pull/7857

https://github.com/jtpio

@jupyter/eslint-plugin

https://github.com/jupyter/notebook/pull/7856

@Darshan808

https://github.com/Darshan808

https://github.com/jtpio

@krassowski

https://github.com/krassowski

TypeScript 5.9

https://github.com/jupyter/notebook/pull/7855

https://github.com/jtpio

Bump the actions group with 2 updates

https://github.com/jupyter/notebook/pull/7846

https://github.com/jtpio

Fix PyO3 CI failure with Python 3.15

https://github.com/jupyter/notebook/pull/7836

https://github.com/jtpio

Update to ESLint 9, update other dependencies

https://github.com/jupyter/notebook/pull/7821

https://github.com/jtpio

Bump prefix-dev/setup-pixi from 0.9.3 to 0.9.4 in the actions group

https://github.com/jupyter/notebook/pull/7819

https://github.com/jtpio

Update to JupyterLab v4.6.0a2

https://github.com/jupyter/notebook/pull/7814

https://github.com/jtpio

Bump the actions group with 4 updates

https://github.com/jupyter/notebook/pull/7811

https://github.com/jtpio

Bump tar from 6.1.13 to 6.2.1 in /ui-tests

https://github.com/jupyter/notebook/pull/7810

https://github.com/jtpio

Update snapshots bot checkout and permission check

https://github.com/jupyter/notebook/pull/7806

@martinRenou

https://github.com/martinRenou

@krassowski

https://github.com/krassowski

Clean up node 24 install

https://github.com/jupyter/notebook/pull/7803

https://github.com/jtpio

Rename the token env variable

https://github.com/jupyter/notebook/pull/7802

https://github.com/brichet

https://github.com/jtpio

Update to JupyterLab v4.6.0a1

https://github.com/jupyter/notebook/pull/7801

https://github.com/jtpio

Minimize prod builds

https://github.com/jupyter/notebook/pull/7789

https://github.com/jtpio

Bump systeminformation from 5.23.14 to 5.27.14 in /ui-tests

https://github.com/jupyter/notebook/pull/7788

https://github.com/jtpio

Update to JupyterLab

https://github.com/jupyter/notebook/pull/7787

https://github.com/jtpio

Documentation improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#documentation-improvements

User facing changelog

https://github.com/jupyter/notebook/pull/7954

https://github.com/jtpio

@krassowski

https://github.com/krassowski

Fix typos in documentation

https://github.com/jupyter/notebook/pull/7865

@yangsong97

https://github.com/yangsong97

@krassowski

https://github.com/krassowski

docs: Fix broken links in troubleshooting and migration docs

https://github.com/jupyter/notebook/pull/7824

@RamiNoodle733

https://github.com/RamiNoodle733

https://github.com/jtpio

Fix grammar: join sentences in CONTRIBUTING.md

https://github.com/jupyter/notebook/pull/7813

@bodhisilberling

https://github.com/bodhisilberling

@krassowski

https://github.com/krassowski

Fix grammar in notebook documentation

https://github.com/jupyter/notebook/pull/7794

https://github.com/xlumzee

@krassowski

https://github.com/krassowski

Other merged PRs

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#other-merged-prs

Bump ws from 8.20.1 to 8.21.0 in /ui-tests

https://github.com/jupyter/notebook/pull/7965

https://github.com/jtpio

Bump form-data from 4.0.4 to 4.0.6 in /ui-tests

https://github.com/jupyter/notebook/pull/7964

https://github.com/jtpio

Bump dompurify from 3.4.0 to 3.4.10 in /ui-tests

https://github.com/jupyter/notebook/pull/7963

https://github.com/jtpio

Bump tar from 6.1.11 to 6.2.1

https://github.com/jupyter/notebook/pull/7962

https://github.com/jtpio

Bump ws from 7.5.9 to 7.5.11

https://github.com/jupyter/notebook/pull/7958

https://github.com/jtpio

Bump toshimaru/auto-author-assign from 3.0.2 to 3.0.3 in the actions group

https://github.com/jupyter/notebook/pull/7956

https://github.com/jtpio

Bump shell-quote from 1.8.3 to 1.8.4

https://github.com/jupyter/notebook/pull/7952

https://github.com/jtpio

Bump lodash-es from 4.17.23 to 4.18.1

https://github.com/jupyter/notebook/pull/7947

https://github.com/jtpio

Bump the actions group with 3 updates

https://github.com/jupyter/notebook/pull/7946

https://github.com/jtpio

Bump the actions group with 7 updates

https://github.com/jupyter/notebook/pull/7937

https://github.com/Yann-P

https://github.com/jtpio

Bump @tootallnate/once from 2.0.0 to 2.0.1

https://github.com/jupyter/notebook/pull/7926

https://github.com/jtpio

Bump @tootallnate/once from 2.0.0 to 2.0.1 in /ui-tests

https://github.com/jupyter/notebook/pull/7925

https://github.com/jtpio

Bump uuid from 11.1.0 to 11.1.1

https://github.com/jupyter/notebook/pull/7924

https://github.com/jtpio

Bump ws from 8.18.3 to 8.20.1

https://github.com/jupyter/notebook/pull/7919

https://github.com/jtpio

Bump ws from 8.13.0 to 8.20.1 in /ui-tests

https://github.com/jupyter/notebook/pull/7918

https://github.com/jtpio

Bump @babel/plugin-transform-modules-systemjs from 7.23.0 to 7.29.4

https://github.com/jupyter/notebook/pull/7910

https://github.com/jtpio

Bump fast-uri from 3.1.0 to 3.1.2 in /ui-tests

https://github.com/jupyter/notebook/pull/7909

https://github.com/jtpio

Bump fast-uri from 3.0.6 to 3.1.2

https://github.com/jupyter/notebook/pull/7908

https://github.com/jtpio

Bump uuid from 11.1.0 to 11.1.1 in /ui-tests

https://github.com/jupyter/notebook/pull/7907

https://github.com/jtpio

Bump postcss from 8.4.31 to 8.5.12 in /ui-tests

https://github.com/jupyter/notebook/pull/7900

https://github.com/jtpio

Bump lodash from 4.17.23 to 4.18.1 in /ui-tests

https://github.com/jupyter/notebook/pull/7887

https://github.com/jtpio

Bump brace-expansion from 1.1.12 to 1.1.13 in /ui-tests

https://github.com/jupyter/notebook/pull/7873

https://github.com/jtpio

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#contributors-to-this-release

The following people contributed discussions, new ideas, code and documentation contributions, and review. See

our definition of contributors

https://github-activity.readthedocs.io/en/latest/use/#how-does-this-tool-define-contributions-in-the-reports

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2025-12-16&to=2026-06-18&type=c

@andrii-i (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aandrii-i+updated%3A2025-12-16..2026-06-18&type=Issues

) | @bodhisilberling (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Abodhisilberling+updated%3A2025-12-16..2026-06-18&type=Issues

) | @brichet (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Abrichet+updated%3A2025-12-16..2026-06-18&type=Issues

) | @Carreau (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3ACarreau+updated%3A2025-12-16..2026-06-18&type=Issues

) | @Copilot (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3ACopilot+updated%3A2025-12-16..2026-06-18&type=Issues

) | @Darshan808 (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3ADarshan808+updated%3A2025-12-16..2026-06-18&type=Issues

) | @goelakash (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agoelakash+updated%3A2025-12-16..2026-06-18&type=Issues

) | @joaovml (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajoaovml+updated%3A2025-12-16..2026-06-18&type=Issues

) | @jtpio (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2025-12-16..2026-06-18&type=Issues

) | @KH-Coder865 (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AKH-Coder865+updated%3A2025-12-16..2026-06-18&type=Issues

) | @krassowski (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akrassowski+updated%3A2025-12-16..2026-06-18&type=Issues

) | @martinRenou (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AmartinRenou+updated%3A2025-12-16..2026-06-18&type=Issues

) | @minrk (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aminrk+updated%3A2025-12-16..2026-06-18&type=Issues

) | @Mirochill (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AMirochill+updated%3A2025-12-16..2026-06-18&type=Issues

) | @RamiNoodle733 (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3ARamiNoodle733+updated%3A2025-12-16..2026-06-18&type=Issues

) | @takluyver (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Atakluyver+updated%3A2025-12-16..2026-06-18&type=Issues

) | @xlumzee (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Axlumzee+updated%3A2025-12-16..2026-06-18&type=Issues

) | @yangsong97 (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ayangsong97+updated%3A2025-12-16..2026-06-18&type=Issues

) | @Yann-P (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AYann-P+updated%3A2025-12-16..2026-06-18&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#rc1

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.6.0-rc.0...0b827ef8d78d6363df4171a923c284e321b4b411

Enhancements made

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id3

Fix missing filebrowser features

https://github.com/jupyter/notebook/pull/7955

https://github.com/jtpio

Maintenance and upkeep improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id4

Update to JupyterLab v4.6.0rc1

https://github.com/jupyter/notebook/pull/7966

https://github.com/jtpio

Bump form-data from 4.0.5 to 4.0.6

https://github.com/jupyter/notebook/pull/7961

https://github.com/jtpio

Bump dompurify from 3.4.0 to 3.4.10

https://github.com/jupyter/notebook/pull/7960

https://github.com/jtpio

Bump @babel/core from 7.23.0 to 7.29.6

https://github.com/jupyter/notebook/pull/7959

https://github.com/jtpio

Remove Python 3.15 pin on CI

https://github.com/jupyter/notebook/pull/7957

https://github.com/jtpio

Documentation improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id5

User facing changelog

https://github.com/jupyter/notebook/pull/7954

https://github.com/jtpio

@krassowski

https://github.com/krassowski

Other merged PRs

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id6

Bump ws from 8.20.1 to 8.21.0 in /ui-tests

https://github.com/jupyter/notebook/pull/7965

https://github.com/jtpio

Bump form-data from 4.0.4 to 4.0.6 in /ui-tests

https://github.com/jupyter/notebook/pull/7964

https://github.com/jtpio

Bump dompurify from 3.4.0 to 3.4.10 in /ui-tests

https://github.com/jupyter/notebook/pull/7963

https://github.com/jtpio

Bump tar from 6.1.11 to 6.2.1

https://github.com/jupyter/notebook/pull/7962

https://github.com/jtpio

Bump ws from 7.5.9 to 7.5.11

https://github.com/jupyter/notebook/pull/7958

https://github.com/jtpio

Bump toshimaru/auto-author-assign from 3.0.2 to 3.0.3 in the actions group

https://github.com/jupyter/notebook/pull/7956

https://github.com/jtpio

Bump shell-quote from 1.8.3 to 1.8.4

https://github.com/jupyter/notebook/pull/7952

https://github.com/jtpio

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id7

The following people contributed discussions, new ideas, code and documentation contributions, and review. See

our definition of contributors

https://github-activity.readthedocs.io/en/latest/use/#how-does-this-tool-define-contributions-in-the-reports

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2026-06-10&to=2026-06-17&type=c

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2026-06-10..2026-06-17&type=Issues

) | @krassowski (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akrassowski+updated%3A2026-06-10..2026-06-17&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#rc0

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.6.0-beta.1...5f81fcaabb912bc36e194f6f3d3f0985f83d3223

Maintenance and upkeep improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id8

Update to JupyterLab v4.6.0rc0

https://github.com/jupyter/notebook/pull/7949

https://github.com/jtpio

Pin GitHub Actions

https://github.com/jupyter/notebook/pull/7938

https://github.com/jtpio

https://github.com/Yann-P

Add UI test for opening file with editor factory

https://github.com/jupyter/notebook/pull/7931

https://github.com/goelakash

https://github.com/jtpio

Add UI test verifying no cell toolbar in file editor

https://github.com/jupyter/notebook/pull/7930

https://github.com/goelakash

https://github.com/jtpio

Other merged PRs

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id9

Bump lodash-es from 4.17.23 to 4.18.1

https://github.com/jupyter/notebook/pull/7947

https://github.com/jtpio

Bump the actions group with 3 updates

https://github.com/jupyter/notebook/pull/7946

https://github.com/jtpio

Bump the actions group with 7 updates

https://github.com/jupyter/notebook/pull/7937

https://github.com/Yann-P

https://github.com/jtpio

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id10

The following people contributed discussions, new ideas, code and documentation contributions, and review. See

our definition of contributors

https://github-activity.readthedocs.io/en/latest/use/#how-does-this-tool-define-contributions-in-the-reports

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2026-05-29&to=2026-06-10&type=c

@goelakash (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agoelakash+updated%3A2026-05-29..2026-06-10&type=Issues

) | @jtpio (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2026-05-29..2026-06-10&type=Issues

) | @Yann-P (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AYann-P+updated%3A2026-05-29..2026-06-10&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#b1

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.6.0-beta.0...c723a2c96ee5d7170dcaeb4b5544573882493926

Maintenance and upkeep improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id11

Update to JupyterLab v4.6.0b1

https://github.com/jupyter/notebook/pull/7935

https://github.com/jtpio

Remove obsolete datetime warning filters

https://github.com/jupyter/notebook/pull/7933

https://github.com/Mirochill

https://github.com/goelakash

https://github.com/jtpio

Other merged PRs

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id12

Bump @tootallnate/once from 2.0.0 to 2.0.1

https://github.com/jupyter/notebook/pull/7926

https://github.com/jtpio

Bump @tootallnate/once from 2.0.0 to 2.0.1 in /ui-tests

https://github.com/jupyter/notebook/pull/7925

https://github.com/jtpio

Bump uuid from 11.1.0 to 11.1.1

https://github.com/jupyter/notebook/pull/7924

https://github.com/jtpio

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id13

The following people contributed discussions, new ideas, code and documentation contributions, and review. See

our definition of contributors

https://github-activity.readthedocs.io/en/latest/use/#how-does-this-tool-define-contributions-in-the-reports

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2026-05-21&to=2026-05-29&type=c

@goelakash (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agoelakash+updated%3A2026-05-21..2026-05-29&type=Issues

) | @jtpio (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2026-05-21..2026-05-29&type=Issues

) | @Mirochill (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AMirochill+updated%3A2026-05-21..2026-05-29&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#b0

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.6.0-alpha.5...0340149a5cdf41d2340b5b8c9ce8d388eeb8d9d5

Maintenance and upkeep improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id14

Update to JupyterLab 4.6.0b0

https://github.com/jupyter/notebook/pull/7923

https://github.com/jtpio

UI tests HTML report

https://github.com/jupyter/notebook/pull/7913

https://github.com/jtpio

@krassowski

https://github.com/krassowski

@jupyter/eslint-plugin

https://github.com/jupyter/notebook/pull/7911

@Darshan808

https://github.com/Darshan808

https://github.com/jtpio

Other merged PRs

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id15

Bump ws from 8.18.3 to 8.20.1

https://github.com/jupyter/notebook/pull/7919

https://github.com/jtpio

Bump ws from 8.13.0 to 8.20.1 in /ui-tests

https://github.com/jupyter/notebook/pull/7918

https://github.com/jtpio

Bump @babel/plugin-transform-modules-systemjs from 7.23.0 to 7.29.4

https://github.com/jupyter/notebook/pull/7910

https://github.com/jtpio

Bump fast-uri from 3.1.0 to 3.1.2 in /ui-tests

https://github.com/jupyter/notebook/pull/7909

https://github.com/jtpio

Bump fast-uri from 3.0.6 to 3.1.2

https://github.com/jupyter/notebook/pull/7908

https://github.com/jtpio

Bump uuid from 11.1.0 to 11.1.1 in /ui-tests

https://github.com/jupyter/notebook/pull/7907

https://github.com/jtpio

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id16

The following people contributed discussions, new ideas, code and documentation contributions, and review. See

our definition of contributors

https://github-activity.readthedocs.io/en/latest/use/#how-does-this-tool-define-contributions-in-the-reports

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2026-04-30&to=2026-05-21&type=c

@Darshan808 (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3ADarshan808+updated%3A2026-04-30..2026-05-21&type=Issues

) | @jtpio (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2026-04-30..2026-05-21&type=Issues

) | @krassowski (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akrassowski+updated%3A2026-04-30..2026-05-21&type=Issues

) | @minrk (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aminrk+updated%3A2026-04-30..2026-05-21&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#a5

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.6.0-alpha.4...4baffbc1ecf65c68b2ec776df62e0e18553d68cd

Enhancements made

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id17

Confirmation dialog before “Close and Shut Down Notebook”

https://github.com/jupyter/notebook/pull/7894

https://github.com/jtpio

Move launch-tree from help menu to view menu

https://github.com/jupyter/notebook/pull/7107

https://github.com/joaovml

https://github.com/jtpio

Maintenance and upkeep improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id18

Update to JupyterLab v4.6.0a5

https://github.com/jupyter/notebook/pull/7901

https://github.com/jtpio

Bump postcss

https://github.com/jupyter/notebook/pull/7899

https://github.com/jtpio

packageManager

package.json

https://github.com/jupyter/notebook/pull/7898

https://github.com/jtpio

jupyter-builder==0.0.8

@jupyterlab/builder

https://github.com/jupyter/notebook/pull/7895

https://github.com/jtpio

@Darshan808

https://github.com/Darshan808

@jupyter/builder

https://github.com/jupyter/notebook/pull/7893

https://github.com/jtpio

@krassowski

https://github.com/krassowski

Dependabot bumps

https://github.com/jupyter/notebook/pull/7892

https://github.com/jtpio

@jupyter/eslint-plugin

and fix lint

https://github.com/jupyter/notebook/pull/7891

@Darshan808

https://github.com/Darshan808

https://github.com/jtpio

https://github.com/jupyter/notebook/pull/7882

https://github.com/jtpio

https://github.com/Copilot

Fix lint warnings

https://github.com/jupyter/notebook/pull/7881

https://github.com/jtpio

@krassowski

https://github.com/krassowski

Add zizmor (github actions static analysis)

https://github.com/jupyter/notebook/pull/7880

https://github.com/Yann-P

https://github.com/Carreau

https://github.com/jtpio

@krassowski

https://github.com/krassowski

@jupyter/eslint-plugin

https://github.com/jupyter/notebook/pull/7856

@Darshan808

https://github.com/Darshan808

https://github.com/jtpio

@krassowski

https://github.com/krassowski

Minimize prod builds

https://github.com/jupyter/notebook/pull/7789

https://github.com/jtpio

Documentation improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id19

Fix typos in documentation

https://github.com/jupyter/notebook/pull/7865

@yangsong97

https://github.com/yangsong97

@krassowski

https://github.com/krassowski

Other merged PRs

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id20

Bump postcss from 8.4.31 to 8.5.12 in /ui-tests

https://github.com/jupyter/notebook/pull/7900

https://github.com/jtpio

Bump lodash from 4.17.23 to 4.18.1 in /ui-tests

https://github.com/jupyter/notebook/pull/7887

https://github.com/jtpio

Bump brace-expansion from 1.1.12 to 1.1.13 in /ui-tests

https://github.com/jupyter/notebook/pull/7873

https://github.com/jtpio

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id21

The following people contributed discussions, new ideas, code and documentation contributions, and review. See

our definition of contributors

https://github-activity.readthedocs.io/en/latest/use/#how-does-this-tool-define-contributions-in-the-reports

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2026-03-12&to=2026-04-30&type=c

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3ACarreau+updated%3A2026-03-12..2026-04-30&type=Issues

) | @Copilot (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3ACopilot+updated%3A2026-03-12..2026-04-30&type=Issues

) | @Darshan808 (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3ADarshan808+updated%3A2026-03-12..2026-04-30&type=Issues

) | @joaovml (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajoaovml+updated%3A2026-03-12..2026-04-30&type=Issues

) | @jtpio (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2026-03-12..2026-04-30&type=Issues

) | @krassowski (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akrassowski+updated%3A2026-03-12..2026-04-30&type=Issues

) | @minrk (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aminrk+updated%3A2026-03-12..2026-04-30&type=Issues

) | @takluyver (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Atakluyver+updated%3A2026-03-12..2026-04-30&type=Issues

) | @yangsong97 (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ayangsong97+updated%3A2026-03-12..2026-04-30&type=Issues

) | @Yann-P (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AYann-P+updated%3A2026-03-12..2026-04-30&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#a4

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.6.0-alpha.3...fc791fcb0af893e3ffe7563a4140ec6af8c9dbe2

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id22

Prevent scratchpad console title to update

https://github.com/jupyter/notebook/pull/7843

https://github.com/brichet

https://github.com/jtpio

Maintenance and upkeep improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id23

Update to JupyterLab v4.6.0a4

https://github.com/jupyter/notebook/pull/7859

https://github.com/jtpio

Fix check links

https://github.com/jupyter/notebook/pull/7857

https://github.com/jtpio

TypeScript 5.9

https://github.com/jupyter/notebook/pull/7855

https://github.com/jtpio

Bump the actions group with 2 updates

https://github.com/jupyter/notebook/pull/7846

https://github.com/jtpio

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id24

The following people contributed discussions, new ideas, code and documentation contributions, and review. See

our definition of contributors

https://github-activity.readthedocs.io/en/latest/use/#how-does-this-tool-define-contributions-in-the-reports

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2026-02-24&to=2026-03-12&type=c

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Abrichet+updated%3A2026-02-24..2026-03-12&type=Issues

) | @jtpio (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2026-02-24..2026-03-12&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#a3

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.6.0-alpha.2...767a30d1ec90e9baf4975023c7019c95d9fe8614

Enhancements made

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id25

Update to JupyterLab v4.6.0a3

https://github.com/jupyter/notebook/pull/7839

https://github.com/jtpio

Maintenance and upkeep improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id26

Fix PyO3 CI failure with Python 3.15

https://github.com/jupyter/notebook/pull/7836

https://github.com/jtpio

Update to ESLint 9, update other dependencies

https://github.com/jupyter/notebook/pull/7821

https://github.com/jtpio

Bump prefix-dev/setup-pixi from 0.9.3 to 0.9.4 in the actions group

https://github.com/jupyter/notebook/pull/7819

https://github.com/jtpio

Documentation improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id27

docs: Fix broken links in troubleshooting and migration docs

https://github.com/jupyter/notebook/pull/7824

@RamiNoodle733

https://github.com/RamiNoodle733

https://github.com/jtpio

Fix grammar: join sentences in CONTRIBUTING.md

https://github.com/jupyter/notebook/pull/7813

@bodhisilberling

https://github.com/bodhisilberling

@krassowski

https://github.com/krassowski

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id28

The following people contributed discussions, new ideas, code and documentation contributions, and review. See

our definition of contributors

https://github-activity.readthedocs.io/en/latest/use/#how-does-this-tool-define-contributions-in-the-reports

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2026-01-23&to=2026-02-24&type=c

@bodhisilberling (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Abodhisilberling+updated%3A2026-01-23..2026-02-24&type=Issues

) | @jtpio (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2026-01-23..2026-02-24&type=Issues

) | @krassowski (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akrassowski+updated%3A2026-01-23..2026-02-24&type=Issues

) | @RamiNoodle733 (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3ARamiNoodle733+updated%3A2026-01-23..2026-02-24&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#a2

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.6.0-alpha.1...209c7da02e8245ec96bf121a641802096ff8cbb3

Enhancements made

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id29

Add a scratch-pad console to the notebook

https://github.com/jupyter/notebook/pull/7790

https://github.com/brichet

https://github.com/jtpio

Maintenance and upkeep improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id30

Update to JupyterLab v4.6.0a2

https://github.com/jupyter/notebook/pull/7814

https://github.com/jtpio

Bump the actions group with 4 updates

https://github.com/jupyter/notebook/pull/7811

https://github.com/jtpio

Bump tar from 6.1.13 to 6.2.1 in /ui-tests

https://github.com/jupyter/notebook/pull/7810

https://github.com/jtpio

Update snapshots bot checkout and permission check

https://github.com/jupyter/notebook/pull/7806

@martinRenou

https://github.com/martinRenou

@krassowski

https://github.com/krassowski

Rename the token env variable

https://github.com/jupyter/notebook/pull/7802

https://github.com/brichet

https://github.com/jtpio

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id31

The following people contributed discussions, new ideas, code and documentation contributions, and review. See

our definition of contributors

https://github-activity.readthedocs.io/en/latest/use/#how-does-this-tool-define-contributions-in-the-reports

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2026-01-12&to=2026-01-23&type=c

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Abrichet+updated%3A2026-01-12..2026-01-23&type=Issues

) | @jtpio (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2026-01-12..2026-01-23&type=Issues

) | @krassowski (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akrassowski+updated%3A2026-01-12..2026-01-23&type=Issues

) | @martinRenou (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AmartinRenou+updated%3A2026-01-12..2026-01-23&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#a1

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.6.0-alpha.0...aa605fa66c6885d85a37c7ab3ba6e7f7a837a810

Enhancements made

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id32

Add PR template

https://github.com/jupyter/notebook/pull/7792

@KH-Coder865

https://github.com/KH-Coder865

https://github.com/andrii-i

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id33

Fix toggling the side panels from menu

https://github.com/jupyter/notebook/pull/7799

https://github.com/brichet

https://github.com/jtpio

Maintenance and upkeep improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id34

Clean up node 24 install

https://github.com/jupyter/notebook/pull/7803

https://github.com/jtpio

Update to JupyterLab v4.6.0a1

https://github.com/jupyter/notebook/pull/7801

https://github.com/jtpio

Documentation improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id35

Fix grammar in notebook documentation

https://github.com/jupyter/notebook/pull/7794

https://github.com/xlumzee

@krassowski

https://github.com/krassowski

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id36

The following people contributed discussions, new ideas, code and documentation contributions, and review. See

our definition of contributors

https://github-activity.readthedocs.io/en/latest/#how-does-this-tool-define-contributions-in-the-reports

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2025-12-17&to=2026-01-12&type=c

@andrii-i (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aandrii-i+updated%3A2025-12-17..2026-01-12&type=Issues

) | @brichet (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Abrichet+updated%3A2025-12-17..2026-01-12&type=Issues

) | @jtpio (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2025-12-17..2026-01-12&type=Issues

) | @KH-Coder865 (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AKH-Coder865+updated%3A2025-12-17..2026-01-12&type=Issues

) | @krassowski (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akrassowski+updated%3A2025-12-17..2026-01-12&type=Issues

) | @xlumzee (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Axlumzee+updated%3A2025-12-17..2026-01-12&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#a0

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.5.1...e7f5e5d50ea18b0b17fe8a9df674025fcc6ab5d1

Maintenance and upkeep improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id37

Bump systeminformation from 5.23.14 to 5.27.14 in /ui-tests

https://github.com/jupyter/notebook/pull/7788

https://github.com/jtpio

Update to JupyterLab

https://github.com/jupyter/notebook/pull/7787

https://github.com/jtpio

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id38

The following people contributed discussions, new ideas, code and documentation contributions, and review. See

our definition of contributors

https://github-activity.readthedocs.io/en/latest/#how-does-this-tool-define-contributions-in-the-reports

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2025-12-16&to=2025-12-17&type=c

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2025-12-16..2025-12-17&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id39

Jupyter Notebook 7.5 is based on JupyterLab 4.5, and includes a number of new features, bug fixes, and enhancements for extension developers. This release is compatible with extensions supporting JupyterLab 4.0. Extension authors are recommended to consult the

Extension Migration Guide

https://jupyterlab.readthedocs.io/en/latest/extension/extension\_migration.html#jupyterlab-4-4-to-4-5

which lists deprecations and changes to the public API.

Below are a few highlights for this new release. Most of the new features and improvements come from the update to JupyterLab 4.5, although they may not all be supported in Notebook 7.5.

For reference you may have a look at the

JupyterLab 4.5 changelog

https://jupyterlab.readthedocs.io/en/latest/getting\_started/changelog.html#v4-5

to learn more.

Notebook improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id40

The default windowing mode is now

contentVisibility

which improves cell rendering and alleviates previously reported issues. The minimap can be enabled for all windowing modes and all notebooks via the

menu, or by toggling the minimap per notebook with the

Show Minimap

Additional fixes improve layout containment and scrollbar behavior when working with long cells.

Debugger and console enhancements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#debugger-and-console-enhancements

The debugger's evaluate dialog has been replaced with an interactive console featuring syntax highlighting and code completion. The variables panel now preserves state when switching editors. Visual improvements include highlighted selected breakpoints, improved empty line handling, and a paused indicator. Debugger panels now reference cell execution counts.

Log Console users can configure default log levels and customize toolbars.

Terminal enhancements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id41

The terminal now includes search functionality, with search highlights that adapt to theme changes.

Media and content support

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#media-and-content-support

Built-in audio and video viewers allow direct file playback within Jupyter Notebook.

File browser enhancements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id42

There is a new

allowFileUploads

setting to control upload permissions.

Menu options for creating Python, R, or Julia files are now available from the New menu.

The “Select All” command is now available with the Ctrl + A (or Cmd + A on macOS) keyboard shortcut in the file browser.

Breadcrumbs are now configurable through

breadcrumbsLeftItems

breadcrumbsRightItems

Settings editor improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#settings-editor-improvements

addExtraLineOnCellMerge

setting removes extra lines when merging cells, matching classic notebook behavior.

Cell toolbar settings

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#cell-toolbar-settings

The cell toolbar settings are now exposed in the Settings Editor, making it easier to customize the cell toolbar appearance and behavior.

Keyboard shortcuts

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id43

key has been defined as the keyboard shortcut to toggle cell outputs, restoring this familiar functionality from the classic notebook.

User interface and accessibility

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#user-interface-and-accessibility

Automatic theme switching between light and dark modes is now available when system synchronization is enabled. Dialog components display buttons and checkboxes on separate lines for improved readability. Terminal selections show better visibility under high-contrast themes. Keyboard navigation and status bar tab ordering have been improved.

Breaking changes

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id44

Python 3.8 support has been dropped in this release.

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id45

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.5.0...fccf56801be0a27a3de76c00d2710a941f255b10

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id46

Fix selector for the

keyboard shortcut

https://github.com/jupyter/notebook/pull/7782

https://github.com/jtpio

@krassowski

https://github.com/krassowski

Fix missing debugger display provider in Notebook

https://github.com/jupyter/notebook/pull/7774

https://github.com/arjxn-py

https://github.com/jtpio

@martinRenou

https://github.com/martinRenou

Maintenance and upkeep improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id47

Update to JupyterLab v4.5.1

https://github.com/jupyter/notebook/pull/7785

https://github.com/jtpio

Fix link to the IPython install page

https://github.com/jupyter/notebook/pull/7783

https://github.com/jtpio

hatch build

, ignore links to

blog.jupyter.org

https://github.com/jupyter/notebook/pull/7780

https://github.com/jtpio

Bump the actions group with 4 updates

https://github.com/jupyter/notebook/pull/7773

https://github.com/jtpio

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id48

The following people contributed discussions, new ideas, code and documentation contributions, and review. See

our definition of contributors

https://github-activity.readthedocs.io/en/latest/#how-does-this-tool-define-contributions-in-the-reports

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2025-11-19&to=2025-12-16&type=c

@arjxn-py (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aarjxn-py+updated%3A2025-11-19..2025-12-16&type=Issues

) | @jtpio (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2025-11-19..2025-12-16&type=Issues

) | @krassowski (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akrassowski+updated%3A2025-11-19..2025-12-16&type=Issues

) | @martinRenou (

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AmartinRenou+updated%3A2025-11-19..2025-12-16&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id49

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.4.0...be53ec8bc96cdbcb64b6f1c5ec39c123c087a348

Enhancements made

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id50

Update to JupyterLab v4.5.0b1

https://github.com/jupyter/notebook/pull/7746

https://github.com/jtpio

Update to JupyterLab v4.5.0b0

https://github.com/jupyter/notebook/pull/7739

https://github.com/jtpio

Update to JupyterLab v4.5.0a4

https://github.com/jupyter/notebook/pull/7728

https://github.com/jtpio

Increase the checkpoint polling interval to 30s

https://github.com/jupyter/notebook/pull/7711

https://github.com/jtpio

as the keyboard shortcut to toggle cell outputs

https://github.com/jupyter/notebook/pull/7709

https://github.com/jtpio

Update to JupyterLab v4.5.0a3

https://github.com/jupyter/notebook/pull/7703

https://github.com/jtpio

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id51

Expose the cell toolbar settings

https://github.com/jupyter/notebook/pull/7766

https://github.com/jtpio

Handle file rename errors

https://github.com/jupyter/notebook/pull/7710

https://github.com/jtpio

Fix open file with “#” in the filename

https://github.com/jupyter/notebook/pull/7698

@itsmevichu

https://github.com/itsmevichu

Maintenance and upkeep improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id52

Update to JupyterLab v4.5.0

https://github.com/jupyter/notebook/pull/7768

https://github.com/jtpio

Update to JupyterLab v4.5.0rc1

https://github.com/jupyter/notebook/pull/7764

https://github.com/jtpio

Update to JupyterLab v4.5.0rc0

https://github.com/jupyter/notebook/pull/7755

https://github.com/jtpio

Bump the actions group across 1 directory with 3 updates

https://github.com/jupyter/notebook/pull/7751

@dependabot

https://github.com/dependabot

Use Node.js 24 / npm 11 to publish releases

https://github.com/jupyter/notebook/pull/7749

https://github.com/jtpio

Revert “Pin

https://github.com/jupyter/notebook/pull/7733

https://github.com/jtpio

Remove link to

https://github.com/jupyter/notebook/pull/7730

https://github.com/jtpio

https://github.com/jupyter/notebook/pull/7729

https://github.com/jtpio

Bump the actions group across 1 directory with 3 updates

https://github.com/jupyter/notebook/pull/7704

@dependabot

https://github.com/dependabot

Update to JupyterLab v4.5.0a2

https://github.com/jupyter/notebook/pull/7694

https://github.com/jtpio

https://github.com/jupyter/notebook/pull/7691

https://github.com/jtpio

Bump prefix-dev/setup-pixi from 0.8.10 to 0.8.11 in the actions group

https://github.com/jupyter/notebook/pull/7675

@dependabot

https://github.com/dependabot

Bump prefix-dev/setup-pixi from 0.8.8 to 0.8.10 in the actions group

https://github.com/jupyter/notebook/pull/7665

@dependabot

https://github.com/dependabot

Bump brace-expansion from 1.1.11 to 1.1.12 in /ui-tests

https://github.com/jupyter/notebook/pull/7664

@dependabot

https://github.com/dependabot

Revert “CI: pin to

jupyter-core<5.8.0

on Windows”

https://github.com/jupyter/notebook/pull/7657

https://github.com/minrk

Update to JupyterLab v4.5.0a1

https://github.com/jupyter/notebook/pull/7656

https://github.com/jtpio

jupyter-core<5.8.0

https://github.com/jupyter/notebook/pull/7655

https://github.com/jtpio

Update to JupyterLab v4.5.0a0

https://github.com/jupyter/notebook/pull/7650

https://github.com/jtpio

Run UI tests on

ubuntu-latest

https://github.com/jupyter/notebook/pull/7639

https://github.com/jtpio

Update to JupyterLab v4.4.1

https://github.com/jupyter/notebook/pull/7638

https://github.com/jtpio

Bump prefix-dev/setup-pixi from 0.8.5 to 0.8.8 in the actions group

https://github.com/jupyter/notebook/pull/7637

@dependabot

https://github.com/dependabot

chore: Fix UP006

https://github.com/jupyter/notebook/pull/7633

https://github.com/honnix

Bump prefix-dev/setup-pixi from 0.8.4 to 0.8.5 in the actions group

https://github.com/jupyter/notebook/pull/7632

@dependabot

https://github.com/dependabot

Drop support for Python 3.8

https://github.com/jupyter/notebook/pull/7628

https://github.com/honnix

Documentation improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id53

User facing changelog for 7.5

https://github.com/jupyter/notebook/pull/7770

https://github.com/jtpio

Clean up references to Gitpod

https://github.com/jupyter/notebook/pull/7767

https://github.com/jtpio

Fix link to Code of Conduct in CONTRIBUTING.md

https://github.com/jupyter/notebook/pull/7758

https://github.com/jtpio

Remove JupyterCon 2025 announcement banner

https://github.com/jupyter/notebook/pull/7757

@jasongrout

https://github.com/jasongrout

Update JupyterCon 2025 announcement links

https://github.com/jupyter/notebook/pull/7744

@krassowski

https://github.com/krassowski

Add JupyterCon banner and add Jupyter colors

https://github.com/jupyter/notebook/pull/7727

https://github.com/choldgraf

Fix grammatical issues in Contributing.md

https://github.com/jupyter/notebook/pull/7669

@sangampaudel530

https://github.com/sangampaudel530

Fixed grammar and typos in CONTRIBUTING.md

https://github.com/jupyter/notebook/pull/7645

https://github.com/jchen1223

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id54

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2025-04-09&to=2025-11-19&type=c

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aafshin+updated%3A2025-04-09..2025-11-19&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Acholdgraf+updated%3A2025-04-09..2025-11-19&type=Issues

@dependabot

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Adependabot+updated%3A2025-04-09..2025-11-19&type=Issues

@github-actions

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2025-04-09..2025-11-19&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ahonnix+updated%3A2025-04-09..2025-11-19&type=Issues

@itsmevichu

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aitsmevichu+updated%3A2025-04-09..2025-11-19&type=Issues

@jasongrout

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajasongrout+updated%3A2025-04-09..2025-11-19&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajchen1223+updated%3A2025-04-09..2025-11-19&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2025-04-09..2025-11-19&type=Issues

@krassowski

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akrassowski+updated%3A2025-04-09..2025-11-19&type=Issues

@lumberbot-app

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Alumberbot-app+updated%3A2025-04-09..2025-11-19&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aminrk+updated%3A2025-04-09..2025-11-19&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ankn2022+updated%3A2025-04-09..2025-11-19&type=Issues

@sangampaudel530

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Asangampaudel530+updated%3A2025-04-09..2025-11-19&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id55

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.5.0-rc.0...7533ccab5e4adc765e57a35b1791850daf952044

Maintenance and upkeep improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id56

Update to JupyterLab v4.5.0rc1

https://github.com/jupyter/notebook/pull/7764

https://github.com/jtpio

Bump the actions group across 1 directory with 3 updates

https://github.com/jupyter/notebook/pull/7751

@dependabot

https://github.com/dependabot

Documentation improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id57

Fix link to Code of Conduct in CONTRIBUTING.md

https://github.com/jupyter/notebook/pull/7758

https://github.com/jtpio

Remove JupyterCon 2025 announcement banner

https://github.com/jupyter/notebook/pull/7757

@jasongrout

https://github.com/jasongrout

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id58

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2025-11-03&to=2025-11-14&type=c

@dependabot

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Adependabot+updated%3A2025-11-03..2025-11-14&type=Issues

@github-actions

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2025-11-03..2025-11-14&type=Issues

@jasongrout

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajasongrout+updated%3A2025-11-03..2025-11-14&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2025-11-03..2025-11-14&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id59

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.5.0-beta.1...18ba796a58402999044b7e8c4401319b76fed0ce

Maintenance and upkeep improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id60

Update to JupyterLab v4.5.0rc0

https://github.com/jupyter/notebook/pull/7755

https://github.com/jtpio

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id61

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2025-10-20&to=2025-11-03&type=c

@dependabot

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Adependabot+updated%3A2025-10-20..2025-11-03&type=Issues

@github-actions

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2025-10-20..2025-11-03&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2025-10-20..2025-11-03&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id62

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.5.0-beta.0...7f84b95ed6550508f9de03d27cd8c2cb84777648

Enhancements made

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id63

Update to JupyterLab v4.5.0b1

https://github.com/jupyter/notebook/pull/7746

https://github.com/jtpio

Maintenance and upkeep improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id64

Use Node.js 24 / npm 11 to publish releases

https://github.com/jupyter/notebook/pull/7749

https://github.com/jtpio

Documentation improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id65

Update JupyterCon 2025 announcement links

https://github.com/jupyter/notebook/pull/7744

@krassowski

https://github.com/krassowski

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id66

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2025-09-29&to=2025-10-20&type=c

@github-actions

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2025-09-29..2025-10-20&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2025-09-29..2025-10-20&type=Issues

@krassowski

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akrassowski+updated%3A2025-09-29..2025-10-20&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ankn2022+updated%3A2025-09-29..2025-10-20&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id67

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.5.0-alpha.3...828708ec26cc4d2ff9f8b725b00024481ae42d2d

Enhancements made

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id68

Update to JupyterLab v4.5.0b0

https://github.com/jupyter/notebook/pull/7739

https://github.com/jtpio

Documentation improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id69

Add JupyterCon banner and add Jupyter colors

https://github.com/jupyter/notebook/pull/7727

https://github.com/choldgraf

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id70

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2025-09-24&to=2025-09-29&type=c

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Acholdgraf+updated%3A2025-09-24..2025-09-29&type=Issues

@github-actions

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2025-09-24..2025-09-29&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2025-09-24..2025-09-29&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id71

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.5.0-alpha.2...254b06ca4b232a0a96ad2dddde560e41df371e57

Enhancements made

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id72

Update to JupyterLab v4.5.0a4

https://github.com/jupyter/notebook/pull/7728

https://github.com/jtpio

Increase the checkpoint polling interval to 30s

https://github.com/jupyter/notebook/pull/7711

https://github.com/jtpio

as the keyboard shortcut to toggle cell outputs

https://github.com/jupyter/notebook/pull/7709

https://github.com/jtpio

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id73

Handle file rename errors

https://github.com/jupyter/notebook/pull/7710

https://github.com/jtpio

Maintenance and upkeep improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id74

Revert “Pin

https://github.com/jupyter/notebook/pull/7733

https://github.com/jtpio

Remove link to

https://github.com/jupyter/notebook/pull/7730

https://github.com/jtpio

https://github.com/jupyter/notebook/pull/7729

https://github.com/jtpio

Bump the actions group across 1 directory with 3 updates

https://github.com/jupyter/notebook/pull/7704

@dependabot

https://github.com/dependabot

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id75

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2025-08-18&to=2025-09-24&type=c

@dependabot

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Adependabot+updated%3A2025-08-18..2025-09-24&type=Issues

@github-actions

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2025-08-18..2025-09-24&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2025-08-18..2025-09-24&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ankn2022+updated%3A2025-08-18..2025-09-24&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id76

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.5.0-alpha.1...3100d879bfe09c629b4add998bd2ac408ffa2af8

Enhancements made

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id77

Update to JupyterLab v4.5.0a3

https://github.com/jupyter/notebook/pull/7703

https://github.com/jtpio

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id78

Fix open file with “#” in the filename

https://github.com/jupyter/notebook/pull/7698

@itsmevichu

https://github.com/itsmevichu

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id79

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2025-08-11&to=2025-08-18&type=c

@github-actions

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2025-08-11..2025-08-18&type=Issues

@itsmevichu

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aitsmevichu+updated%3A2025-08-11..2025-08-18&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2025-08-11..2025-08-18&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id80

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.5.0-alpha.0...f56a27c17bfd85f37a27dea9512c675120571e63

Maintenance and upkeep improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id81

Update to JupyterLab v4.5.0a2

https://github.com/jupyter/notebook/pull/7694

https://github.com/jtpio

https://github.com/jupyter/notebook/pull/7691

https://github.com/jtpio

Bump prefix-dev/setup-pixi from 0.8.10 to 0.8.11 in the actions group

https://github.com/jupyter/notebook/pull/7675

@dependabot

https://github.com/dependabot

Bump prefix-dev/setup-pixi from 0.8.8 to 0.8.10 in the actions group

https://github.com/jupyter/notebook/pull/7665

@dependabot

https://github.com/dependabot

Bump brace-expansion from 1.1.11 to 1.1.12 in /ui-tests

https://github.com/jupyter/notebook/pull/7664

@dependabot

https://github.com/dependabot

Revert “CI: pin to

jupyter-core<5.8.0

on Windows”

https://github.com/jupyter/notebook/pull/7657

https://github.com/minrk

Update to JupyterLab v4.5.0a1

https://github.com/jupyter/notebook/pull/7656

https://github.com/jtpio

jupyter-core<5.8.0

https://github.com/jupyter/notebook/pull/7655

https://github.com/jtpio

Documentation improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id82

Fix grammatical issues in Contributing.md

https://github.com/jupyter/notebook/pull/7669

@sangampaudel530

https://github.com/sangampaudel530

Fixed grammar and typos in CONTRIBUTING.md

https://github.com/jupyter/notebook/pull/7645

https://github.com/jchen1223

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id83

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2025-05-07&to=2025-08-11&type=c

@dependabot

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Adependabot+updated%3A2025-05-07..2025-08-11&type=Issues

@github-actions

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2025-05-07..2025-08-11&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajchen1223+updated%3A2025-05-07..2025-08-11&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2025-05-07..2025-08-11&type=Issues

@krassowski

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akrassowski+updated%3A2025-05-07..2025-08-11&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aminrk+updated%3A2025-05-07..2025-08-11&type=Issues

@sangampaudel530

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Asangampaudel530+updated%3A2025-05-07..2025-08-11&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id84

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.4.0...22e29fc41901ef8116670bc8a04eeb833858ff51

Maintenance and upkeep improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id85

Update to JupyterLab v4.5.0a0

https://github.com/jupyter/notebook/pull/7650

https://github.com/jtpio

Run UI tests on

ubuntu-latest

https://github.com/jupyter/notebook/pull/7639

https://github.com/jtpio

Update to JupyterLab v4.4.1

https://github.com/jupyter/notebook/pull/7638

https://github.com/jtpio

Bump prefix-dev/setup-pixi from 0.8.5 to 0.8.8 in the actions group

https://github.com/jupyter/notebook/pull/7637

@dependabot

https://github.com/dependabot

chore: Fix UP006

https://github.com/jupyter/notebook/pull/7633

https://github.com/honnix

Bump prefix-dev/setup-pixi from 0.8.4 to 0.8.5 in the actions group

https://github.com/jupyter/notebook/pull/7632

@dependabot

https://github.com/dependabot

Drop support for Python 3.8

https://github.com/jupyter/notebook/pull/7628

https://github.com/honnix

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id86

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2025-04-09&to=2025-05-07&type=c

@dependabot

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Adependabot+updated%3A2025-04-09..2025-05-07&type=Issues

@github-actions

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2025-04-09..2025-05-07&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ahonnix+updated%3A2025-04-09..2025-05-07&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2025-04-09..2025-05-07&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id87

Jupyter Notebook 7.4 is based on JupyterLab 4.4, and includes a number of new features, bug fixes, and enhancements for extension developers. This release is compatible with extensions supporting JupyterLab 4.0. Extension authors are recommended to consult the

Extension Migration Guide

https://jupyterlab.readthedocs.io/en/latest/extension/extension\_migration.html#jupyterlab-4-3-to-4-4

which lists deprecations and changes to the public API.

Below are a few highlights for this new release. Most of the new features and improvements come from the update to JupyterLab 4.4, although they may not all be supported in Notebook 7.4.

For reference you may have a look at the

JupyterLab 4.4 changelog

https://jupyterlab.readthedocs.io/en/latest/getting\_started/changelog.html#v4-4

to learn more.

Code console improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#code-console-improvements

The code console prompt can now be positioned on the top, left, or right side of the console, in addition to the default bottom placement. The placement is persisted in the Prompt Cell Position setting.

#### The console toolbar now includes buttons to:

Execute code

Restart the kernel

Clear the cells

Switch the kernel

#### Additional settings for console behavior have been added:

Clear Code Content on Execute (enabled by default) – When disabled, the code submitted for execution remains in the code editor, allowing for further edits.

Hide Code Input – When enabled, only the execution output is shown in the console.

Clear Cells on Execute – When enabled, only the last cell is displayed.

Toggling all the three new settings transforms the console into an interactive editor resembling an ephemeral notebook with a single cell.

Settings import and export

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#settings-import-and-export

Settings can now be exported to

overrides.json

from the Settings Editor, which can be used to pre-configure defaults in deployments or to restore settings.

Support for collaboration without

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#support-for-collaboration-without-rtc-drive

Real time collaboration in previous versions of JupyterLab and Jupyter Notebook (which can be enabled by installing jupyter-collaboration package) was implemented by swapping the default JupyterLab file system drive to a collaborative drive with the

prefix. This approach was incompatible with multiple extensions. JupyterLab 4.4 introduces the Content Providers API, which allows the next version of

jupyter-collaboration

to work without changing the drive prefix. This improves compatibility with extensions that do not support arbitrary drives.

Context menu opt-out

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#context-menu-opt-out

The context menu, available under right mouse click in browsers, can now be disabled globally by toggling the

Enable Context Menu

option available in the Command Palette, or via the JSON Settings Editor in the Application Context Menu.

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id88

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.3.2...fbfe36574e04b16ed7ba9303c5e819330f402f87

Highlights ✨

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#highlights

To learn more about the highlights of the 7.4.0 release: https://jupyter-notebook.readthedocs.io/en/latest/changelog.html

Enhancements made

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id89

Update to JupyterLab v4.4.0rc1

https://github.com/jupyter/notebook/pull/7622

https://github.com/jtpio

Add support for a

https://github.com/jupyter/notebook/pull/7619

https://github.com/jtpio

Update to JupyterLab v4.4.0rc0

https://github.com/jupyter/notebook/pull/7618

https://github.com/jtpio

ServiceManagerPlugin

https://github.com/jupyter/notebook/pull/7616

https://github.com/jtpio

Update to JupyterLab

https://github.com/jupyter/notebook/pull/7607

https://github.com/jtpio

Update to JupyterLab v4.4.0b0

https://github.com/jupyter/notebook/pull/7591

https://github.com/jtpio

Update to JupyterLab v4.4.0a3

https://github.com/jupyter/notebook/pull/7577

https://github.com/jtpio

Add active cell border padding, remove double cell padding

https://github.com/jupyter/notebook/pull/7570

https://github.com/andrii-i

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id90

Fix undefined error when checkpoints is empty

https://github.com/jupyter/notebook/pull/7567

https://github.com/jdavid

Maintenance and upkeep improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id91

Bump the actions group with 2 updates

https://github.com/jupyter/notebook/pull/7626

@dependabot

https://github.com/dependabot

Update to JupyterLab v4.4.0b2

https://github.com/jupyter/notebook/pull/7614

https://github.com/jtpio

Add pixi step to the update workflow

https://github.com/jupyter/notebook/pull/7608

https://github.com/jtpio

dependencies

https://github.com/jupyter/notebook/pull/7605

https://github.com/jtpio

Add devcontainer support, backed by pixi

https://github.com/jupyter/notebook/pull/7602

https://github.com/jtpio

Manual dependabot bumps

https://github.com/jupyter/notebook/pull/7599

https://github.com/jtpio

Bump vega-selections from 5.4.1 to 5.5.0 in /ui-tests

https://github.com/jupyter/notebook/pull/7592

@dependabot

https://github.com/dependabot

Improve handling of optional notebook tracker

https://github.com/jupyter/notebook/pull/7581

https://github.com/jtpio

Fix upgrade script

https://github.com/jupyter/notebook/pull/7579

https://github.com/jtpio

Allow owners/members/collab to trigger galata update on other's PR

https://github.com/jupyter/notebook/pull/7572

@krassowski

https://github.com/krassowski

https://github.com/jupyter/notebook/pull/7562

https://github.com/jtpio

Update pre-commit hooks

https://github.com/jupyter/notebook/pull/7561

https://github.com/jtpio

Update to JupyterLab v4.4.0a2

https://github.com/jupyter/notebook/pull/7559

https://github.com/jtpio

Bump the actions group across 1 directory with 2 updates

https://github.com/jupyter/notebook/pull/7558

@dependabot

https://github.com/dependabot

Improve update script

https://github.com/jupyter/notebook/pull/7556

https://github.com/jtpio

Disable cron scheduling for now

https://github.com/jupyter/notebook/pull/7555

https://github.com/jtpio

Update to JupyterLab v4.4.0a1

https://github.com/jupyter/notebook/pull/7554

https://github.com/jtpio

Update workflow improvements

https://github.com/jupyter/notebook/pull/7552

https://github.com/jtpio

Documentation improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id92

User facing changelog for 7.4

https://github.com/jupyter/notebook/pull/7612

https://github.com/jtpio

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id93

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2024-12-21&to=2025-04-09&type=c

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aandrii-i+updated%3A2024-12-21..2025-04-09&type=Issues

@dependabot

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Adependabot+updated%3A2024-12-21..2025-04-09&type=Issues

@github-actions

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2024-12-21..2025-04-09&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajdavid+updated%3A2024-12-21..2025-04-09&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2024-12-21..2025-04-09&type=Issues

@krassowski

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akrassowski+updated%3A2024-12-21..2025-04-09&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3ARRosio+updated%3A2024-12-21..2025-04-09&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id94

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.4.0-beta.3...7fa19999c9e01d713a684e0f25d8017dbc999528

Enhancements made

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id95

Update to JupyterLab v4.4.0rc1

https://github.com/jupyter/notebook/pull/7622

https://github.com/jtpio

Add support for a

https://github.com/jupyter/notebook/pull/7619

https://github.com/jtpio

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id96

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2025-03-26&to=2025-04-03&type=c

@github-actions

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2025-03-26..2025-04-03&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2025-03-26..2025-04-03&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#b3

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.4.0-beta.2...434221c0fe3de3df3b4b54ed1005712e07957352

Enhancements made

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id97

Update to JupyterLab v4.4.0rc0

https://github.com/jupyter/notebook/pull/7618

https://github.com/jtpio

ServiceManagerPlugin

https://github.com/jupyter/notebook/pull/7616

https://github.com/jtpio

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id98

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2025-03-20&to=2025-03-26&type=c

@github-actions

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2025-03-20..2025-03-26&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2025-03-20..2025-03-26&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#b2

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.4.0-beta.1...be2fd12f91a64796d9919ee8b8242f3093aac8a5

Maintenance and upkeep improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id99

Update to JupyterLab v4.4.0b2

https://github.com/jupyter/notebook/pull/7614

https://github.com/jtpio

Add pixi step to the update workflow

https://github.com/jupyter/notebook/pull/7608

https://github.com/jtpio

Documentation improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id100

User facing changelog for 7.4

https://github.com/jupyter/notebook/pull/7612

https://github.com/jtpio

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id101

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2025-03-14&to=2025-03-20&type=c

@github-actions

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2025-03-14..2025-03-20&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2025-03-14..2025-03-20&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id102

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.4.0-beta.0...6d06d97302bd1bb77e25864214ade2277f2e50d4

Enhancements made

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id103

Update to JupyterLab

https://github.com/jupyter/notebook/pull/7607

https://github.com/jtpio

Maintenance and upkeep improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id104

dependencies

https://github.com/jupyter/notebook/pull/7605

https://github.com/jtpio

Add devcontainer support, backed by pixi

https://github.com/jupyter/notebook/pull/7602

https://github.com/jtpio

Manual dependabot bumps

https://github.com/jupyter/notebook/pull/7599

https://github.com/jtpio

Bump vega-selections from 5.4.1 to 5.5.0 in /ui-tests

https://github.com/jupyter/notebook/pull/7592

@dependabot

https://github.com/dependabot

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id105

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2025-02-20&to=2025-03-14&type=c

@dependabot

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Adependabot+updated%3A2025-02-20..2025-03-14&type=Issues

@github-actions

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2025-02-20..2025-03-14&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2025-02-20..2025-03-14&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id106

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.4.0-alpha.3...48243197bbd004555008cd7cfa14c907147aceca

Enhancements made

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id107

Update to JupyterLab v4.4.0b0

https://github.com/jupyter/notebook/pull/7591

https://github.com/jtpio

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id108

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2025-02-05&to=2025-02-20&type=c

@github-actions

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2025-02-05..2025-02-20&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2025-02-05..2025-02-20&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id109

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.4.0-alpha.2...48e52c759ffec0cea47dfef59f48d8e9fa6112d3

Enhancements made

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id110

Add active cell border padding, remove double cell padding

https://github.com/jupyter/notebook/pull/7570

https://github.com/andrii-i

Maintenance and upkeep improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id111

Improve handling of optional notebook tracker

https://github.com/jupyter/notebook/pull/7581

https://github.com/jtpio

Fix upgrade script

https://github.com/jupyter/notebook/pull/7579

https://github.com/jtpio

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id112

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2025-02-03&to=2025-02-05&type=c

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aandrii-i+updated%3A2025-02-03..2025-02-05&type=Issues

@github-actions

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2025-02-03..2025-02-05&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2025-02-03..2025-02-05&type=Issues

@krassowski

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akrassowski+updated%3A2025-02-03..2025-02-05&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3ARRosio+updated%3A2025-02-03..2025-02-05&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id113

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.4.0-alpha.1...ef4f6346cd6b377ade271fcd61810b5d2a7d0f41

Enhancements made

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id114

Update to JupyterLab v4.4.0a3

https://github.com/jupyter/notebook/pull/7577

https://github.com/jtpio

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id115

Fix undefined error when checkpoints is empty

https://github.com/jupyter/notebook/pull/7567

https://github.com/jdavid

Maintenance and upkeep improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id116

Allow owners/members/collab to trigger galata update on other's PR

https://github.com/jupyter/notebook/pull/7572

@krassowski

https://github.com/krassowski

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id117

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2025-01-07&to=2025-02-03&type=c

@github-actions

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2025-01-07..2025-02-03&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajdavid+updated%3A2025-01-07..2025-02-03&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2025-01-07..2025-02-03&type=Issues

@krassowski

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akrassowski+updated%3A2025-01-07..2025-02-03&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3ARRosio+updated%3A2025-01-07..2025-02-03&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id118

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.4.0-alpha.0...18672b7e85ec5181e4c5c18d2e32c3e9eab7260c

Maintenance and upkeep improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id119

https://github.com/jupyter/notebook/pull/7562

https://github.com/jtpio

Update pre-commit hooks

https://github.com/jupyter/notebook/pull/7561

https://github.com/jtpio

Update to JupyterLab v4.4.0a2

https://github.com/jupyter/notebook/pull/7559

https://github.com/jtpio

Bump the actions group across 1 directory with 2 updates

https://github.com/jupyter/notebook/pull/7558

@dependabot

https://github.com/dependabot

Improve update script

https://github.com/jupyter/notebook/pull/7556

https://github.com/jtpio

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id120

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2024-12-21&to=2025-01-07&type=c

@dependabot

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Adependabot+updated%3A2024-12-21..2025-01-07&type=Issues

@github-actions

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2024-12-21..2025-01-07&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2024-12-21..2025-01-07&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id121

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.3.2...12efbe601858c317bf677dc835d314489357e20d

Maintenance and upkeep improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id122

Disable cron scheduling for now

https://github.com/jupyter/notebook/pull/7555

https://github.com/jtpio

Update to JupyterLab v4.4.0a1

https://github.com/jupyter/notebook/pull/7554

https://github.com/jtpio

Update workflow improvements

https://github.com/jupyter/notebook/pull/7552

https://github.com/jtpio

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id123

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2024-12-21&to=2024-12-21&type=c

@github-actions

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2024-12-21..2024-12-21&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2024-12-21..2024-12-21&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id124

Jupyter Notebook 7.3 is based on JupyterLab 4.3, and includes a number of new features, bug fixes, and enhancements for extension developers. This release is compatible with extensions supporting JupyterLab 4.0. Extension authors are recommended to consult the

Extension Migration Guide

https://jupyterlab.readthedocs.io/en/latest/extension/extension\_migration.html#jupyterlab-4-2-to-4-3

which lists deprecations and changes to the public API.

Below are a few highlights for this new release. Most of the new features and improvements come from the update to JupyterLab 4.3, although they may not all be supported in Notebook 7.3.

For reference you may have a look at the

JupyterLab 4.3 changelog

https://jupyterlab.readthedocs.io/en/latest/getting\_started/changelog.html#v4-3

to learn more.

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#minimap

The virtual scrollbar now acts as a minimap and exposes information on whether a cell:

is running/scheduled (

) or was already run (e.g.

was modified since it was last executed (“dirty”) - orange background

has an output that contains an error - red background

is markdown/code (

for code, nothing for markdown)

how much text/code it contains

To enable the minimap, click on the hamburger icon (≡) which appears in the notebook's toolbar. If you do not see the hamburger icon, go to

Settings → Notebook → Windowing mode

and choose “full”.

File browser enhancements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id125

#### The file browser now:

supports resizing the columns and remembers the column sizes after reloading JupyterLab

supports uploading folders by drag-and-drop

supports navigation with a single click

adds a file filter collapsed by default (funnel icon)

In Jupyter Notebook, the single click navigation is enabled by default. If you would like to disable it to get the same experience as in JupyterLab, go to

Settings → File Browser

and make sure “Navigate files and directories with single click” is unchecked.

Improved kernel and server interactions

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#improved-kernel-and-server-interactions

The previous release enabled connecting to external kernels, such as those spawned by a third-party application like Blender. In this release the kernel selector dialog was improved to also show the external kernels.

The previous release improved the awareness of the kernel/kernel specification distinction by providing both tree and list view in the kernels sidebar panel, but only the tree view featured the kernel identifiers. In this release both the list and tree view show the kernel identifier stub.

A new toolbar button was added in the kernel allowing to shut down unused kernels (kernels with no widget attached).

Full Width Notebook

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#full-width-notebook

It is now possible to configure the notebook to take up the full width of the page via:

a setting that can be defined by a user via the Settings Editor

View > Enable Full Width Notebook

the command palette, searching for

Enable Full Width Notebook

This is particularly useful on large displays, or for those who prefer working with a wider notebook.

It is also possible to use the JupyterLab interface for a more fully-featured experience, which allows for full-width notebooks too, and offers a “Simple Interface” mode for only showing a single notebook at a time.

You can open JupyterLab by clicking on

View > Open JupyterLab

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id126

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.3.1...7959ba0de553e9c541d2716d76108a8bc0bc2d6c

Maintenance and upkeep improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id127

Fix update script

https://github.com/jupyter/notebook/pull/7550

https://github.com/jtpio

Fix workflow to update the JupyterLab version

https://github.com/jupyter/notebook/pull/7548

https://github.com/jtpio

Bump nanoid from 3.3.7 to 3.3.8 in /ui-tests

https://github.com/jupyter/notebook/pull/7547

@dependabot

https://github.com/dependabot

Bump systeminformation from 5.21.8 to 5.23.14 in /ui-tests

https://github.com/jupyter/notebook/pull/7546

@dependabot

https://github.com/dependabot

Workflow to update JupyterLab dependencies automatically

https://github.com/jupyter/notebook/pull/7281

@itsmevichu

https://github.com/itsmevichu

Update to JupyterLab v4.3.4

https://github.com/jupyter/notebook/pull/7551

@github-actions

https://github.com/apps/github-actions

Documentation improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id128

Update chat links to Zulip.

https://github.com/jupyter/notebook/pull/7539

@ericsnekbytes

https://github.com/ericsnekbytes

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id129

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2024-12-04&to=2024-12-21&type=c

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3ACarreau+updated%3A2024-12-04..2024-12-21&type=Issues

@dependabot

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Adependabot+updated%3A2024-12-04..2024-12-21&type=Issues

@ericsnekbytes

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aericsnekbytes+updated%3A2024-12-04..2024-12-21&type=Issues

@github-actions

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2024-12-04..2024-12-21&type=Issues

@itsmevichu

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aitsmevichu+updated%3A2024-12-04..2024-12-21&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2024-12-04..2024-12-21&type=Issues

@krassowski

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akrassowski+updated%3A2024-12-04..2024-12-21&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id130

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.3.0...21d0306ecef93ea23bf063bc1d8a0580450cd4df

Maintenance and upkeep improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id131

Adds jupyter-ui-toolkit packages in shared scope

https://github.com/jupyter/notebook/pull/7530

https://github.com/brichet

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id132

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2024-12-04&to=2024-12-04&type=c

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Abrichet+updated%3A2024-12-04..2024-12-04&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2024-12-04..2024-12-04&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id133

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.2.0...b16eed26eff8e357eeccbef3f3434df77fb8ab48

Enhancements made

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id134

Fix for auto scroll output option

https://github.com/jupyter/notebook/pull/7511

https://github.com/gjmooney

Add a setting to enable the notebook to take up the full width

https://github.com/jupyter/notebook/pull/7487

https://github.com/jtpio

Add the file filter button to the file browser toolbar

https://github.com/jupyter/notebook/pull/7479

https://github.com/jtpio

Redirect paths from the notebooks route to the tree route if they are directories

https://github.com/jupyter/notebook/pull/7446

https://github.com/andyscho

Update to JupyterLab

https://github.com/jupyter/notebook/pull/7416

https://github.com/jtpio

Support custom page\_data\_hook function

https://github.com/jupyter/notebook/pull/7387

@bluestealth

https://github.com/bluestealth

Add missing “Open…” file menu

https://github.com/jupyter/notebook/pull/7385

@martinRenou

https://github.com/martinRenou

Duplicate notebook menu option

https://github.com/jupyter/notebook/pull/7374

@JasonWeill

https://github.com/JasonWeill

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id135

Move handling of the file browser settings to a separate plugin, enable file browser single click navigation

https://github.com/jupyter/notebook/pull/7481

https://github.com/jtpio

Remove pseudoelement obstructing the cell collapser

https://github.com/jupyter/notebook/pull/7392

@krassowski

https://github.com/krassowski

“Close and Shut Down Notebook” shuts down without the confirmation dialog

https://github.com/jupyter/notebook/pull/7384

@JasonWeill

https://github.com/JasonWeill

Adds message about building code before running 'develop'

https://github.com/jupyter/notebook/pull/7382

@JasonWeill

https://github.com/JasonWeill

Maintenance and upkeep improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id136

Bump Python version used on CI

https://github.com/jupyter/notebook/pull/7528

https://github.com/jtpio

Update to JupyterLab 4.3.2

https://github.com/jupyter/notebook/pull/7527

https://github.com/jtpio

Update to JupyterLab 4.3.1

https://github.com/jupyter/notebook/pull/7521

https://github.com/jtpio

Add webpack prod config

https://github.com/jupyter/notebook/pull/7513

https://github.com/gjmooney

Update to JupyterLab 4.3 final

https://github.com/jupyter/notebook/pull/7507

https://github.com/jtpio

Update to JupyterLab

https://github.com/jupyter/notebook/pull/7497

https://github.com/jtpio

file browser trick

https://github.com/jupyter/notebook/pull/7477

https://github.com/jtpio

Update to JupyterLab

https://github.com/jupyter/notebook/pull/7423

https://github.com/jtpio

Update to JupyterLab 4.3.0a0

https://github.com/jupyter/notebook/pull/7378

https://github.com/jtpio

Documentation improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id137

Fix link to the JupyterLab 4.3 changelog

https://github.com/jupyter/notebook/pull/7529

https://github.com/jtpio

Rename some header links to fit better

https://github.com/jupyter/notebook/pull/7508

https://github.com/gjmooney

Add user facing changelog for

https://github.com/jupyter/notebook/pull/7494

https://github.com/jtpio

https://github.com/jupyter/notebook/pull/7472

https://github.com/algonell

Adds message about building code before running 'develop'

https://github.com/jupyter/notebook/pull/7382

@JasonWeill

https://github.com/JasonWeill

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id138

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2024-05-16&to=2024-12-04&type=c

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aalgonell+updated%3A2024-05-16..2024-12-04&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aandyscho+updated%3A2024-05-16..2024-12-04&type=Issues

@bluestealth

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Abluestealth+updated%3A2024-05-16..2024-12-04&type=Issues

@github-actions

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2024-05-16..2024-12-04&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agjmooney+updated%3A2024-05-16..2024-12-04&type=Issues

@JasonWeill

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AJasonWeill+updated%3A2024-05-16..2024-12-04&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2024-05-16..2024-12-04&type=Issues

@krassowski

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akrassowski+updated%3A2024-05-16..2024-12-04&type=Issues

@martinRenou

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AmartinRenou+updated%3A2024-05-16..2024-12-04&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3ARRosio+updated%3A2024-05-16..2024-12-04&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id139

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.3.0-beta.2...b34449747a84fe0ba7951ae0fa8f2bb011444a60

Maintenance and upkeep improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id140

Update to JupyterLab 4.3.1

https://github.com/jupyter/notebook/pull/7521

https://github.com/jtpio

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id141

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2024-11-06&to=2024-11-18&type=c

@github-actions

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2024-11-06..2024-11-18&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2024-11-06..2024-11-18&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id142

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.3.0-beta.1...110e728e4a239ffc7217bd07b9a50cf4eff0dff5

Enhancements made

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id143

Fix for auto scroll output option

https://github.com/jupyter/notebook/pull/7511

https://github.com/gjmooney

Maintenance and upkeep improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id144

Add webpack prod config

https://github.com/jupyter/notebook/pull/7513

https://github.com/gjmooney

Update to JupyterLab 4.3 final

https://github.com/jupyter/notebook/pull/7507

https://github.com/jtpio

Documentation improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id145

Rename some header links to fit better

https://github.com/jupyter/notebook/pull/7508

https://github.com/gjmooney

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id146

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2024-10-24&to=2024-11-06&type=c

@github-actions

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2024-10-24..2024-11-06&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agjmooney+updated%3A2024-10-24..2024-11-06&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2024-10-24..2024-11-06&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id147

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.3.0-beta.0...f614f7c6387cc7da82e0307b70e10593b2cd6bff

Enhancements made

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id148

Add a setting to enable the notebook to take up the full width

https://github.com/jupyter/notebook/pull/7487

https://github.com/jtpio

Add the file filter button to the file browser toolbar

https://github.com/jupyter/notebook/pull/7479

https://github.com/jtpio

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id149

Move handling of the file browser settings to a separate plugin, enable file browser single click navigation

https://github.com/jupyter/notebook/pull/7481

https://github.com/jtpio

Maintenance and upkeep improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id150

Update to JupyterLab

https://github.com/jupyter/notebook/pull/7497

https://github.com/jtpio

Documentation improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id151

Add user facing changelog for

https://github.com/jupyter/notebook/pull/7494

https://github.com/jtpio

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id152

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2024-10-15&to=2024-10-24&type=c

@github-actions

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2024-10-15..2024-10-24&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2024-10-15..2024-10-24&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id153

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.3.0-alpha.1...fec4431305b2fd857ff81b7b60c2894dd125bec2

Enhancements made

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id154

Redirect paths from the notebooks route to the tree route if they are directories

https://github.com/jupyter/notebook/pull/7446

https://github.com/andyscho

Maintenance and upkeep improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id155

file browser trick

https://github.com/jupyter/notebook/pull/7477

https://github.com/jtpio

Update to JupyterLab

https://github.com/jupyter/notebook/pull/7423

https://github.com/jtpio

Documentation improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id156

https://github.com/jupyter/notebook/pull/7472

https://github.com/algonell

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id157

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2024-07-01&to=2024-10-15&type=c

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aalgonell+updated%3A2024-07-01..2024-10-15&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aandyscho+updated%3A2024-07-01..2024-10-15&type=Issues

@github-actions

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2024-07-01..2024-10-15&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2024-07-01..2024-10-15&type=Issues

@krassowski

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akrassowski+updated%3A2024-07-01..2024-10-15&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3ARRosio+updated%3A2024-07-01..2024-10-15&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id158

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.3.0-alpha.0...ff2b822d066dc8d733a259f955177da4bd4d668c

Enhancements made

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id159

Update to JupyterLab

https://github.com/jupyter/notebook/pull/7416

https://github.com/jtpio

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id160

Remove pseudoelement obstructing the cell collapser

https://github.com/jupyter/notebook/pull/7392

@krassowski

https://github.com/krassowski

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id161

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2024-05-31&to=2024-07-01&type=c

@github-actions

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2024-05-31..2024-07-01&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2024-05-31..2024-07-01&type=Issues

@krassowski

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akrassowski+updated%3A2024-05-31..2024-07-01&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id162

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.2.0...1a03b9d8e502f8177684e39d7b627bed1c772bb2

Enhancements made

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id163

Support custom page\_data\_hook function

https://github.com/jupyter/notebook/pull/7387

@bluestealth

https://github.com/bluestealth

Add missing “Open…” file menu

https://github.com/jupyter/notebook/pull/7385

@martinRenou

https://github.com/martinRenou

Duplicate notebook menu option

https://github.com/jupyter/notebook/pull/7374

@JasonWeill

https://github.com/JasonWeill

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id164

“Close and Shut Down Notebook” shuts down without the confirmation dialog

https://github.com/jupyter/notebook/pull/7384

@JasonWeill

https://github.com/JasonWeill

Adds message about building code before running 'develop'

https://github.com/jupyter/notebook/pull/7382

@JasonWeill

https://github.com/JasonWeill

Maintenance and upkeep improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id165

Update to JupyterLab 4.3.0a0

https://github.com/jupyter/notebook/pull/7378

https://github.com/jtpio

Documentation improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id166

Adds message about building code before running 'develop'

https://github.com/jupyter/notebook/pull/7382

@JasonWeill

https://github.com/JasonWeill

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id167

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2024-05-16&to=2024-05-31&type=c

@bluestealth

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Abluestealth+updated%3A2024-05-16..2024-05-31&type=Issues

@github-actions

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2024-05-16..2024-05-31&type=Issues

@JasonWeill

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AJasonWeill+updated%3A2024-05-16..2024-05-31&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2024-05-16..2024-05-31&type=Issues

@martinRenou

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AmartinRenou+updated%3A2024-05-16..2024-05-31&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id168

Jupyter Notebook 7.2 is based on JupyterLab 4.2, and includes a number of new features, bug fixes, and enhancements for extension developers. This release is compatible with extensions supporting JupyterLab 4.0. Extension authors are recommended to consult the

Extension Migration Guide

https://jupyterlab.readthedocs.io/en/latest/extension/extension\_migration.html#jupyterlab-4-0-to-4-1

which lists deprecations and changes to the public API.

Below are a few highlights for this new release. Most of the new features and improvements come from the update to JupyterLab 4.2, although they are not all supported in Notebook 7.2.

For reference you may have a look at the JupyterLab 4.2 changelog to learn more: https://jupyterlab.readthedocs.io/en/latest/getting\_started/changelog.html#v4-2

Full notebook windowing mode by default

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#full-notebook-windowing-mode-by-default

Notebooks in the

windowing mode only render the visible cells, significantly improving the performance of the application. One limitation of

mode is that the search function in your browser may produce false negatives; using the search function is recommended. To revert to the behaviour from Notebook 7.2, go to Settings → Settings Editor → Notebook, scroll to “Windowing mode”, and choose

Improved Shortcuts Editor

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#improved-shortcuts-editor

Among the numerous improvements and bug fixes for the keyboard shortcuts editor:

it is now possible to remove the default shortcuts,

shortcuts are correctly sorted when using a language pack,

shortcuts with different arguments are now correctly displayed as individual entries.

Dark high contrast theme

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#dark-high-contrast-theme

A new theme, JupyterLab Dark High Contrast, which is intended to benefit users with the need for higher contrast, following the WCAG AAA accessibility standard for color contrast. To select this theme, from the menu bar, choose Settings → Theme → JupyterLab Dark High Contrast. Please provide feedback and suggestions on further improvements to this theme.

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id169

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.1.2...31bf294e85175bbf39816a90dc8858dedaf73bde

Enhancements made

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id170

Update to JupyterLab 4.2.0

https://github.com/jupyter/notebook/pull/7357

https://github.com/jtpio

Update to JupyterLab 4.2.0rc0

https://github.com/jupyter/notebook/pull/7333

https://github.com/jtpio

@jupyterlab/theme-dark-high-contrast-extension

https://github.com/jupyter/notebook/pull/7331

https://github.com/jtpio

Update to JupyterLab 4.2.0a2

https://github.com/jupyter/notebook/pull/7307

https://github.com/jtpio

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id171

@jupyterlab/notebook-extension:copy-output

https://github.com/jupyter/notebook/pull/7353

https://github.com/jtpio

Fix CSS for

windowing mode

https://github.com/jupyter/notebook/pull/7337

https://github.com/jtpio

Force notebook windowing mode to

https://github.com/jupyter/notebook/pull/7335

https://github.com/jtpio

Fix scrollbar always showing up by default

https://github.com/jupyter/notebook/pull/7327

https://github.com/jtpio

Default to the

windowing mode

https://github.com/jupyter/notebook/pull/7321

https://github.com/jtpio

Maintenance and upkeep improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id172

Fix emoji in create issue screen

https://github.com/jupyter/notebook/pull/7363

@JasonWeill

https://github.com/JasonWeill

@jupyterlab/galata

https://github.com/jupyter/notebook/pull/7361

https://github.com/jtpio

on CI for now

https://github.com/jupyter/notebook/pull/7346

https://github.com/jtpio

Update to JupyterLab

https://github.com/jupyter/notebook/pull/7319

https://github.com/jtpio

Update to JupyterLab 4.2.0b0

https://github.com/jupyter/notebook/pull/7312

https://github.com/jtpio

Ignore links to GitHub user and organisation profiles

https://github.com/jupyter/notebook/pull/7308

https://github.com/jtpio

Documentation improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id173

Add user facing changelog for 7.2

https://github.com/jupyter/notebook/pull/7372

https://github.com/jtpio

Fix emoji in create issue screen

https://github.com/jupyter/notebook/pull/7363

@JasonWeill

https://github.com/JasonWeill

update RISE extension installation instructions

https://github.com/jupyter/notebook/pull/7299

https://github.com/afeld

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id174

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2024-03-14&to=2024-05-16&type=c

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aafeld+updated%3A2024-03-14..2024-05-16&type=Issues

@github-actions

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2024-03-14..2024-05-16&type=Issues

@JasonWeill

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AJasonWeill+updated%3A2024-03-14..2024-05-16&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2024-03-14..2024-05-16&type=Issues

@krassowski

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akrassowski+updated%3A2024-03-14..2024-05-16&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3ARRosio+updated%3A2024-03-14..2024-05-16&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Atakluyver+updated%3A2024-03-14..2024-05-16&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id175

Full Changelog

https://github.com/jupyter/notebook/compare/v7.2.0rc0...f5d8aea3bdc3eea25213792f9d101738f2a1f627

Enhancements made

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id176

Update to JupyterLab 4.2.0

https://github.com/jupyter/notebook/pull/7357

https://github.com/jtpio

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id177

@jupyterlab/notebook-extension:copy-output

https://github.com/jupyter/notebook/pull/7353

https://github.com/jtpio

Default to the

windowing mode

https://github.com/jupyter/notebook/pull/7321

https://github.com/jtpio

Documentation improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id178

update RISE extension installation instructions

https://github.com/jupyter/notebook/pull/7299

https://github.com/afeld

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id179

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2024-05-01&to=2024-05-13&type=c

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aafeld+updated%3A2024-05-01..2024-05-13&type=Issues

@github-actions

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2024-05-01..2024-05-13&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2024-05-01..2024-05-13&type=Issues

@krassowski

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akrassowski+updated%3A2024-05-01..2024-05-13&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Atakluyver+updated%3A2024-05-01..2024-05-13&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id180

Full Changelog

https://github.com/jupyter/notebook/compare/v7.2.0b1...49ddd0fe1e4d4bfa24f74042f2232c5b91d1c36e

Enhancements made

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id181

Update to JupyterLab 4.2.0rc0

https://github.com/jupyter/notebook/pull/7333

https://github.com/jtpio

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id182

Fix CSS for

windowing mode

https://github.com/jupyter/notebook/pull/7337

https://github.com/jtpio

Maintenance and upkeep improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id183

on CI for now

https://github.com/jupyter/notebook/pull/7346

https://github.com/jtpio

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id184

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2024-04-19&to=2024-05-01&type=c

@github-actions

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2024-04-19..2024-05-01&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2024-04-19..2024-05-01&type=Issues

@krassowski

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akrassowski+updated%3A2024-04-19..2024-05-01&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id185

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.2.0-beta.0...b45d666d5ee1ee053b55ac9cb6e9aecde5d53945

Enhancements made

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id186

@jupyterlab/theme-dark-high-contrast-extension

https://github.com/jupyter/notebook/pull/7331

https://github.com/jtpio

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id187

Force notebook windowing mode to

https://github.com/jupyter/notebook/pull/7335

https://github.com/jtpio

Fix scrollbar always showing up by default

https://github.com/jupyter/notebook/pull/7327

https://github.com/jtpio

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id188

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2024-04-12&to=2024-04-19&type=c

@github-actions

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2024-04-12..2024-04-19&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2024-04-12..2024-04-19&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3ARRosio+updated%3A2024-04-12..2024-04-19&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id189

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.2.0-alpha.0...09bcd99e6dfffce92acc9a7f9d11a2a2122131c0

Maintenance and upkeep improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id190

Update to JupyterLab

https://github.com/jupyter/notebook/pull/7319

https://github.com/jtpio

Update to JupyterLab 4.2.0b0

https://github.com/jupyter/notebook/pull/7312

https://github.com/jtpio

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id191

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2024-03-29&to=2024-04-12&type=c

@github-actions

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2024-03-29..2024-04-12&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2024-03-29..2024-04-12&type=Issues

@krassowski

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akrassowski+updated%3A2024-03-29..2024-04-12&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id192

Full Changelog

https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.1.2...80b582bce69e33e36e936af2ea981bcb22a4d285

Enhancements made

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id193

Update to JupyterLab 4.2.0a2

https://github.com/jupyter/notebook/pull/7307

https://github.com/jtpio

Maintenance and upkeep improvements

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id194

Ignore links to GitHub user and organisation profiles

https://github.com/jupyter/notebook/pull/7308

https://github.com/jtpio

Contributors to this release

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id195

GitHub contributors page for this release

https://github.com/jupyter/notebook/graphs/contributors?from=2024-03-14&to=2024-03-29&type=c

@github-actions

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2024-03-14..2024-03-29&type=Issues

https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2024-03-14..2024-03-29&type=Issues

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#v7-1

Jupyter Notebook 7.1 is based on JupyterLab 4.1, and includes a number of new features, bug fixes, and enhancements for extension developers. This release is compatible with extensions supporting JupyterLab 4.0. Extension authors are recommended to consult the

Extension Migration Guide

https://jupyterlab.readthedocs.io/en/latest/extension/extension\_migration.html#jupyterlab-4-0-to-4-1

which lists deprecations and changes to the public API.

Below are a few highlights for this new release. Most of the new features and improvements come from the update to JupyterLab 4.1, although they are not all supported in Notebook 7.1.

For reference you may have a look at the JupyterLab 4.1 changelog to learn more: https://jupyterlab.readthedocs.io/en/latest/getting\_started/changelog.html#v4-1

Diagrams in Markdown

https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#diagrams-in-markdown

Matching GitHub-Flavoured Markdown, JupyterLab 4.1 now supports

https://github.com/mermaid-js/mermaid

diagrams. To create a mermaid diagram use the

language specifier for a code block in a markdown cell or document, for example:

\`\`\`mermaid
flowchart LR

A\[Hard\] -->|Text| B(Round)
B --> C{Decision}
C -->|One| D\[Result 1\]
C -->|Two| E\[Result 2\]

which renders as:
!\[Rendered Mermaid diagram going from left to right with modern look; the diagram contains blueish square node with text Hard pointing to round square node with text Round; over the arrow connecting the two nodes there is a word Text; the second node further connects to a rhombus-shaped node with text Decision which then connects to two further nodes, Result 1 and Result 2.\](https://raw.githubusercontent.com/jupyterlab/jupyterlab/main/docs/source/getting\_started/changelog\_assets/4.1-merimad-diagram.png)

### Inline completer\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#inline-completer)

JupyterLab now supports completion presented as ghost text in the cell and file editors, allowing generative AI models to provide multi-line completions. This can now also be leveraged in Jupyter Notebook.

The suggestions are provided by plugins implementing the \`IInlineCompletionProvider\` API; by default a single provider which uses kernel history is available.
!\[In a code cell with \`def fac\` content a ghost text containing a suggestion representing further code of factorial function is shown; over the code cell there is a floating widget allowing to accept the suggestion and iterate between alternative suggestions\](https://raw.githubusercontent.com/jupyterlab/jupyterlab/main/docs/source/getting\_started/changelog\_assets/4.1-inline-completer.png)

The suggestions can be invoked as-you-type or manually using a configurable shortcut (by default \`Alt\` + \`\` ). The default keyboard shortcuts are displayed in the small widget shown when hovering over the ghost suggestion:

- \`Alt\` + \`End\` - accept suggestion
- \`Alt\` + \`\[\` - previous suggestion
- \`Alt\` + \`\]\` - next suggestion

To enable the inline suggestions based on the kernel history, go to Settings → Inline Completer → History provider → check the “enabled” checkbox.

In addition to the built-in history suggestions, the \[\`jupyter-ai\`\](https://github.com/jupyterlab/jupyter-ai) extension will provide suggestions from supported models.

Note that the Jupyter AI extension is not yet compatible with Jupyter Notebook 7.

### Keyboard navigation improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#keyboard-navigation-improvements)

Numerous improvements to keyboard navigation with focus on accessibility and usability are included in this release:

- the notebook cells now retain focus
- the focus can now be moved beyond the active notebook
- the toolbars can now be navigated using arrow keys

For more details, see \[this post on Jupyter Blog\](https://blog.jupyter.org/recent-keyboard-navigation-improvements-in-jupyter-4df32f97628d).

### Execution history in notebook\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#execution-history-in-notebook)

The code from previously executed cells can be used to populate empty cells, allowing to iterate on code from previous cells or even sessions (depending on how a specific kernel stores history).

To cycle between history items press \`Alt\` + \`Arrow Up\` and \`Alt\` + \`Arrow Down\` .

To enable execution history, go to Settings → Notebook → check the “Kernel history access” checkbox.

This feature was already available in the console in previous releases; it only works with kernels supporting execution history requests. To clear the execution history consult the documentation of the kernel you are using (e.g., IPython/ipykernel).

### Error indicator in the table of contents\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#error-indicator-in-the-table-of-contents)

When a cell fails during execution, an error indicator will be displayed by the corresponding heading, increasing awareness of the notebook state and enabling users to quickly navigate to the cell which requires attention.
!\[Error indicator in the shape of a triangle with exclamation sign (using ⚠ UTF character) shown next to one of the headings in the table of contents panel\](https://raw.githubusercontent.com/jupyterlab/jupyterlab/main/docs/source/getting\_started/changelog\_assets/4.1-toc-error-indicator.png)

### Search improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#search-improvements)

- The search box will now grow automatically to accommodate longer text
- Search in selection can now be toggled using \`Alt\` + \`L\` and automatic search in selection can be configured in settings
- Tooltips with shortcuts were added to the buttons in the search box to improve discoverability of the shortcuts

### Miscellaneous\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#miscellaneous)

- The current theme (dark/light) can now be synced with the browser/system preference (Settings menu → Theme → Synchronise with System Settings)
- A blue “read-only” status indicator is now displayed in the toolbar of documents which cannot be saved because their model is read-only.
- Native support for viewing jsonl/ndjson files was added
- Collapsing of breadcrumbs in the File Browser can be disabled in File Browser settings

## 7.1.2\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id196)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.1.1...ca41222a9c8d75356c6d67d3bd36e34d71cce2d8))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id197)

- Update Release Scripts \[#7295\](https://github.com/jupyter/notebook/pull/7295) (\[@blink1073\](https://github.com/blink1073))
- Fix jupyterlab install command in the releaser hook \[#7294\](https://github.com/jupyter/notebook/pull/7294) (\[@jtpio\](https://github.com/jtpio))
- Update to JupyterLab 4.1.5 packages \[#7291\](https://github.com/jupyter/notebook/pull/7291) (\[@jtpio\](https://github.com/jtpio))

### Documentation improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id198)

- Add a section to use local dependencies \[#7292\](https://github.com/jupyter/notebook/pull/7292) (\[@brichet\](https://github.com/brichet))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id199)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2024-02-26&amp;to=2024-03-14&amp;type=c))

\[@blink1073\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ablink1073+updated%3A2024-02-26..2024-03-14&amp;type=Issues) | \[@brichet\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Abrichet+updated%3A2024-02-26..2024-03-14&amp;type=Issues) | \[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2024-02-26..2024-03-14&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2024-02-26..2024-03-14&amp;type=Issues)

## 7.1.1\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id200)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.1.0...da7b8d400e96ceff0eec834badd891bc5d5f154d))

### Bugs fixed\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id201)

- Grayout “Edit Notebook Metadata” for other file formats. \[#7265\](https://github.com/jupyter/notebook/pull/7265) (\[@itsmevichu\](https://github.com/itsmevichu))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id202)

- Fix flaky mobile UI tests \[#7278\](https://github.com/jupyter/notebook/pull/7278) (\[@jtpio\](https://github.com/jtpio))
- Update to JupyterLab 4.1.2 packages \[#7277\](https://github.com/jupyter/notebook/pull/7277) (\[@jtpio\](https://github.com/jtpio))
- Ignore stackoverflow link \[#7274\](https://github.com/jupyter/notebook/pull/7274) (\[@jtpio\](https://github.com/jtpio))
- Expose \`version\_info\` \[#7273\](https://github.com/jupyter/notebook/pull/7273) (\[@jtpio\](https://github.com/jtpio))
- Bump ip from 2.0.0 to 2.0.1 in /ui-tests \[#7268\](https://github.com/jupyter/notebook/pull/7268) (\[@dependabot\](https://github.com/dependabot))
- Bump ip from 2.0.0 to 2.0.1 \[#7267\](https://github.com/jupyter/notebook/pull/7267) (\[@dependabot\](https://github.com/dependabot))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id203)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2024-02-13&amp;to=2024-02-26&amp;type=c))

\[@dependabot\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Adependabot+updated%3A2024-02-13..2024-02-26&amp;type=Issues) | \[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2024-02-13..2024-02-26&amp;type=Issues) | \[@itsmevichu\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aitsmevichu+updated%3A2024-02-13..2024-02-26&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2024-02-13..2024-02-26&amp;type=Issues)

## 7.1.0\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id204)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.0.6...b8ec7e4a8eda70a8d7dca19799acd3e96e019160))

### Enhancements made\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id205)

- Create a new notebook with a specific kernel from the new dropdown \[#7255\](https://github.com/jupyter/notebook/pull/7255) (\[@jtpio\](https://github.com/jtpio))
- Add the plugin manager \[#7198\](https://github.com/jupyter/notebook/pull/7198) (\[@jtpio\](https://github.com/jtpio))
- Fix toggle functionality for widgets. \[#7178\](https://github.com/jupyter/notebook/pull/7178) (\[@haok1402\](https://github.com/haok1402))
- Bump to JupyterLab 4.1.0a4 bis \[#7172\](https://github.com/jupyter/notebook/pull/7172) (\[@brichet\](https://github.com/brichet))
- Update to JupyterLab \`4.1.0a3\` \[#7161\](https://github.com/jupyter/notebook/pull/7161) (\[@jtpio\](https://github.com/jtpio))
- Added Lumino Plugin Description (#7008) \[#7127\](https://github.com/jupyter/notebook/pull/7127) (\[@Dilip-Jain\](https://github.com/Dilip-Jain))
- Added Edit Notebook Metadata Option (#6402) \[#7099\](https://github.com/jupyter/notebook/pull/7099) (\[@Dilip-Jain\](https://github.com/Dilip-Jain))
- Update to JupyterLab 4.1 \[#7096\](https://github.com/jupyter/notebook/pull/7096) (\[@jtpio\](https://github.com/jtpio))
- Add the JupyterLab resources plugin \[#6968\](https://github.com/jupyter/notebook/pull/6968) (\[@jtpio\](https://github.com/jtpio))

### Bugs fixed\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id206)

- Fix spurious kernel selection dialog on notebook creation \[#7258\](https://github.com/jupyter/notebook/pull/7258) (\[@jtpio\](https://github.com/jtpio))
- Workaround for the file browser tracker focus issue \[#7224\](https://github.com/jupyter/notebook/pull/7224) (\[@jtpio\](https://github.com/jtpio))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id207)

- Update to JupyterLab 4.1.1 \[#7256\](https://github.com/jupyter/notebook/pull/7256) (\[@jtpio\](https://github.com/jtpio))
- Follow JupyterLab minor versions \[#7250\](https://github.com/jupyter/notebook/pull/7250) (\[@jtpio\](https://github.com/jtpio))
- chore: update pre-commit hooks \[#7237\](https://github.com/jupyter/notebook/pull/7237) (\[@pre-commit-ci\](https://github.com/pre-commit-ci))
- Update to JupyterLab 4.1.0 final \[#7234\](https://github.com/jupyter/notebook/pull/7234) (\[@jtpio\](https://github.com/jtpio))
- Update to JupyterLab 4.1.0rc1 \[#7230\](https://github.com/jupyter/notebook/pull/7230) (\[@jtpio\](https://github.com/jtpio))
- Update to JupyterLab 4.1.0rc0 \[#7227\](https://github.com/jupyter/notebook/pull/7227) (\[@jtpio\](https://github.com/jtpio))
- Update to JupyterLab 4.1.0b2 \[#7222\](https://github.com/jupyter/notebook/pull/7222) (\[@jtpio\](https://github.com/jtpio))
- Fix \`check\_links\` on CI \[#7219\](https://github.com/jupyter/notebook/pull/7219) (\[@jtpio\](https://github.com/jtpio))
- Bump the actions group with 1 update \[#7218\](https://github.com/jupyter/notebook/pull/7218) (\[@dependabot\](https://github.com/dependabot))
- Bump the actions group with 2 updates \[#7207\](https://github.com/jupyter/notebook/pull/7207) (\[@dependabot\](https://github.com/dependabot))
- chore: update pre-commit hooks \[#7206\](https://github.com/jupyter/notebook/pull/7206) (\[@pre-commit-ci\](https://github.com/pre-commit-ci))
- Add nbviewer.jupyter.org to the ignore list \[#7197\](https://github.com/jupyter/notebook/pull/7197) (\[@jtpio\](https://github.com/jtpio))
- Update to JupyterLab 4.1.0b0 \[#7196\](https://github.com/jupyter/notebook/pull/7196) (\[@jtpio\](https://github.com/jtpio))
- Update ruff config \[#7190\](https://github.com/jupyter/notebook/pull/7190) (\[@blink1073\](https://github.com/blink1073))
- Bump @babel/traverse from 7.23.0 to 7.23.6 \[#7187\](https://github.com/jupyter/notebook/pull/7187) (\[@dependabot\](https://github.com/dependabot))
- Bump actions/setup-python from 4 to 5 \[#7180\](https://github.com/jupyter/notebook/pull/7180) (\[@dependabot\](https://github.com/dependabot))
- Update publish-release workflow for PyPI trusted publisher \[#7176\](https://github.com/jupyter/notebook/pull/7176) (\[@jtpio\](https://github.com/jtpio))
- chore: update pre-commit hooks \[#7174\](https://github.com/jupyter/notebook/pull/7174) (\[@pre-commit-ci\](https://github.com/pre-commit-ci))
- Update \`yarn.lock\` \[#7170\](https://github.com/jupyter/notebook/pull/7170) (\[@jtpio\](https://github.com/jtpio))
- Bump axios from 1.5.1 to 1.6.2 \[#7165\](https://github.com/jupyter/notebook/pull/7165) (\[@dependabot\](https://github.com/dependabot))
- Bump dessant/lock-threads from 4 to 5 \[#7159\](https://github.com/jupyter/notebook/pull/7159) (\[@dependabot\](https://github.com/dependabot))
- Update ruff config and typing \[#7145\](https://github.com/jupyter/notebook/pull/7145) (\[@blink1073\](https://github.com/blink1073))
- chore: update pre-commit hooks \[#7143\](https://github.com/jupyter/notebook/pull/7143) (\[@pre-commit-ci\](https://github.com/pre-commit-ci))
- Clean up lint handling \[#7142\](https://github.com/jupyter/notebook/pull/7142) (\[@blink1073\](https://github.com/blink1073))
- Adopt ruff format \[#7132\](https://github.com/jupyter/notebook/pull/7132) (\[@blink1073\](https://github.com/blink1073))
- Fix python bumping to \`minor\` \[#7131\](https://github.com/jupyter/notebook/pull/7131) (\[@jtpio\](https://github.com/jtpio))
- Add Python 3.12 classifier \[#7111\](https://github.com/jupyter/notebook/pull/7111) (\[@jtpio\](https://github.com/jtpio))
- Remove viewport workaround in the UI tests \[#6887\](https://github.com/jupyter/notebook/pull/6887) (\[@jtpio\](https://github.com/jtpio))

### Documentation improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id208)

- Add documentation for updating \`notebook\` imports \[#7244\](https://github.com/jupyter/notebook/pull/7244) (\[@jtpio\](https://github.com/jtpio))
- Fix link in \`CONTRIBUTING.md\` \[#7235\](https://github.com/jupyter/notebook/pull/7235) (\[@jtpio\](https://github.com/jtpio))
- Add user facing changelog for 7.1 \[#7232\](https://github.com/jupyter/notebook/pull/7232) (\[@jtpio\](https://github.com/jtpio))
- Clarify README about supported versions (post v7 release) \[#7193\](https://github.com/jupyter/notebook/pull/7193) (\[@akx\](https://github.com/akx))
- Set \`navigation\_with\_keys\` to \`False\` \[#7129\](https://github.com/jupyter/notebook/pull/7129) (\[@jtpio\](https://github.com/jtpio))
- Updated ui-tests Configuration in Contributing.md \[#7124\](https://github.com/jupyter/notebook/pull/7124) (\[@jayeshsingh9767\](https://github.com/jayeshsingh9767))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id209)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2023-10-17&amp;to=2024-02-13&amp;type=c))

\[@akx\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aakx+updated%3A2023-10-17..2024-02-13&amp;type=Issues) | \[@blink1073\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ablink1073+updated%3A2023-10-17..2024-02-13&amp;type=Issues) | \[@brichet\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Abrichet+updated%3A2023-10-17..2024-02-13&amp;type=Issues) | \[@d5423197\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ad5423197+updated%3A2023-10-17..2024-02-13&amp;type=Issues) | \[@dependabot\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Adependabot+updated%3A2023-10-17..2024-02-13&amp;type=Issues) | \[@Dilip-Jain\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3ADilip-Jain+updated%3A2023-10-17..2024-02-13&amp;type=Issues) | \[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2023-10-17..2024-02-13&amp;type=Issues) | \[@haok1402\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ahaok1402+updated%3A2023-10-17..2024-02-13&amp;type=Issues) | \[@jayeshsingh9767\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajayeshsingh9767+updated%3A2023-10-17..2024-02-13&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2023-10-17..2024-02-13&amp;type=Issues) | \[@krassowski\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akrassowski+updated%3A2023-10-17..2024-02-13&amp;type=Issues) | \[@pre-commit-ci\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Apre-commit-ci+updated%3A2023-10-17..2024-02-13&amp;type=Issues) | \[@Zsailer\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AZsailer+updated%3A2023-10-17..2024-02-13&amp;type=Issues)

## 7.1.0rc1\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id210)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/v7.1.0rc0...376a2f97c883e6e91f321d0a676e1ee9ff3b8d87))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id211)

- Follow JupyterLab minor versions \[#7250\](https://github.com/jupyter/notebook/pull/7250) (\[@jtpio\](https://github.com/jtpio))

### Documentation improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id212)

- Add documentation for updating \`notebook\` imports \[#7244\](https://github.com/jupyter/notebook/pull/7244) (\[@jtpio\](https://github.com/jtpio))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id213)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2024-02-07&amp;to=2024-02-09&amp;type=c))

\[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2024-02-07..2024-02-09&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2024-02-07..2024-02-09&amp;type=Issues)

## 7.1.0rc0\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id214)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/v7.1.0b0...2d717f5896a1d4310baa2499c7e6197d1914201d))

### Enhancements made\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id215)

- Added Edit Notebook Metadata Option (#6402) \[#7099\](https://github.com/jupyter/notebook/pull/7099) (\[@Dilip-Jain\](https://github.com/Dilip-Jain))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id216)

- chore: update pre-commit hooks \[#7237\](https://github.com/jupyter/notebook/pull/7237) (\[@pre-commit-ci\](https://github.com/pre-commit-ci))
- Update to JupyterLab 4.1.0 final \[#7234\](https://github.com/jupyter/notebook/pull/7234) (\[@jtpio\](https://github.com/jtpio))
- Update to JupyterLab 4.1.0rc1 \[#7230\](https://github.com/jupyter/notebook/pull/7230) (\[@jtpio\](https://github.com/jtpio))
- Update to JupyterLab 4.1.0rc0 \[#7227\](https://github.com/jupyter/notebook/pull/7227) (\[@jtpio\](https://github.com/jtpio))

### Documentation improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id217)

- Fix link in \`CONTRIBUTING.md\` \[#7235\](https://github.com/jupyter/notebook/pull/7235) (\[@jtpio\](https://github.com/jtpio))
- Add user facing changelog for 7.1 \[#7232\](https://github.com/jupyter/notebook/pull/7232) (\[@jtpio\](https://github.com/jtpio))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id218)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2024-01-26&amp;to=2024-02-07&amp;type=c))

\[@Dilip-Jain\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3ADilip-Jain+updated%3A2024-01-26..2024-02-07&amp;type=Issues) | \[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2024-01-26..2024-02-07&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2024-01-26..2024-02-07&amp;type=Issues) | \[@pre-commit-ci\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Apre-commit-ci+updated%3A2024-01-26..2024-02-07&amp;type=Issues)

## 7.1.0b0\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id219)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/v7.1.0a2...5d265b90ed5f097af4ca22d283ecdc705229ff92))

### Bugs fixed\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id220)

- Workaround for the file browser tracker focus issue \[#7224\](https://github.com/jupyter/notebook/pull/7224) (\[@jtpio\](https://github.com/jtpio))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id221)

- Update to JupyterLab 4.1.0b2 \[#7222\](https://github.com/jupyter/notebook/pull/7222) (\[@jtpio\](https://github.com/jtpio))
- Fix \`check\_links\` on CI \[#7219\](https://github.com/jupyter/notebook/pull/7219) (\[@jtpio\](https://github.com/jtpio))
- Bump the actions group with 1 update \[#7218\](https://github.com/jupyter/notebook/pull/7218) (\[@dependabot\](https://github.com/dependabot))
- Bump the actions group with 2 updates \[#7207\](https://github.com/jupyter/notebook/pull/7207) (\[@dependabot\](https://github.com/dependabot))
- chore: update pre-commit hooks \[#7206\](https://github.com/jupyter/notebook/pull/7206) (\[@pre-commit-ci\](https://github.com/pre-commit-ci))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id222)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2023-12-27&amp;to=2024-01-26&amp;type=c))

\[@dependabot\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Adependabot+updated%3A2023-12-27..2024-01-26&amp;type=Issues) | \[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2023-12-27..2024-01-26&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2023-12-27..2024-01-26&amp;type=Issues) | \[@pre-commit-ci\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Apre-commit-ci+updated%3A2023-12-27..2024-01-26&amp;type=Issues) | \[@Zsailer\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AZsailer+updated%3A2023-12-27..2024-01-26&amp;type=Issues)

## 7.1.0a2\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id223)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/v7.1.0a1...251e0e360603b6e63b280b3bd04a5406f7da28da))

### Enhancements made\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id224)

- Add the plugin manager \[#7198\](https://github.com/jupyter/notebook/pull/7198) (\[@jtpio\](https://github.com/jtpio))
- Fix toggle functionality for widgets. \[#7178\](https://github.com/jupyter/notebook/pull/7178) (\[@haok1402\](https://github.com/haok1402))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id225)

- Add nbviewer.jupyter.org to the ignore list \[#7197\](https://github.com/jupyter/notebook/pull/7197) (\[@jtpio\](https://github.com/jtpio))
- Update to JupyterLab 4.1.0b0 \[#7196\](https://github.com/jupyter/notebook/pull/7196) (\[@jtpio\](https://github.com/jtpio))
- Update ruff config \[#7190\](https://github.com/jupyter/notebook/pull/7190) (\[@blink1073\](https://github.com/blink1073))
- Bump @babel/traverse from 7.23.0 to 7.23.6 \[#7187\](https://github.com/jupyter/notebook/pull/7187) (\[@dependabot\](https://github.com/dependabot))
- Bump actions/setup-python from 4 to 5 \[#7180\](https://github.com/jupyter/notebook/pull/7180) (\[@dependabot\](https://github.com/dependabot))
- Update publish-release workflow for PyPI trusted publisher \[#7176\](https://github.com/jupyter/notebook/pull/7176) (\[@jtpio\](https://github.com/jtpio))
- chore: update pre-commit hooks \[#7174\](https://github.com/jupyter/notebook/pull/7174) (\[@pre-commit-ci\](https://github.com/pre-commit-ci))
- Remove viewport workaround in the UI tests \[#6887\](https://github.com/jupyter/notebook/pull/6887) (\[@jtpio\](https://github.com/jtpio))

### Documentation improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id226)

- Clarify README about supported versions (post v7 release) \[#7193\](https://github.com/jupyter/notebook/pull/7193) (\[@akx\](https://github.com/akx))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id227)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2023-12-04&amp;to=2023-12-27&amp;type=c))

\[@akx\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aakx+updated%3A2023-12-04..2023-12-27&amp;type=Issues) | \[@blink1073\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ablink1073+updated%3A2023-12-04..2023-12-27&amp;type=Issues) | \[@dependabot\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Adependabot+updated%3A2023-12-04..2023-12-27&amp;type=Issues) | \[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2023-12-04..2023-12-27&amp;type=Issues) | \[@haok1402\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ahaok1402+updated%3A2023-12-04..2023-12-27&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2023-12-04..2023-12-27&amp;type=Issues) | \[@pre-commit-ci\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Apre-commit-ci+updated%3A2023-12-04..2023-12-27&amp;type=Issues)

## 7.1.0a1\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id228)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.1.0-alpha.0...a74cd91871fcc6037d384fe59af8986557e783e5))

### Enhancements made\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id229)

- Bump to JupyterLab 4.1.0a4 bis \[#7172\](https://github.com/jupyter/notebook/pull/7172) (\[@brichet\](https://github.com/brichet))
- Update to JupyterLab \`4.1.0a3\` \[#7161\](https://github.com/jupyter/notebook/pull/7161) (\[@jtpio\](https://github.com/jtpio))
- Add the JupyterLab resources plugin \[#6968\](https://github.com/jupyter/notebook/pull/6968) (\[@jtpio\](https://github.com/jtpio))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id230)

- Update \`yarn.lock\` \[#7170\](https://github.com/jupyter/notebook/pull/7170) (\[@jtpio\](https://github.com/jtpio))
- Bump axios from 1.5.1 to 1.6.2 \[#7165\](https://github.com/jupyter/notebook/pull/7165) (\[@dependabot\](https://github.com/dependabot))
- Bump dessant/lock-threads from 4 to 5 \[#7159\](https://github.com/jupyter/notebook/pull/7159) (\[@dependabot\](https://github.com/dependabot))
- Update ruff config and typing \[#7145\](https://github.com/jupyter/notebook/pull/7145) (\[@blink1073\](https://github.com/blink1073))
- chore: update pre-commit hooks \[#7143\](https://github.com/jupyter/notebook/pull/7143) (\[@pre-commit-ci\](https://github.com/pre-commit-ci))
- Clean up lint handling \[#7142\](https://github.com/jupyter/notebook/pull/7142) (\[@blink1073\](https://github.com/blink1073))
- Adopt ruff format \[#7132\](https://github.com/jupyter/notebook/pull/7132) (\[@blink1073\](https://github.com/blink1073))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id231)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2023-10-27&amp;to=2023-12-04&amp;type=c))

\[@blink1073\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ablink1073+updated%3A2023-10-27..2023-12-04&amp;type=Issues) | \[@brichet\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Abrichet+updated%3A2023-10-27..2023-12-04&amp;type=Issues) | \[@dependabot\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Adependabot+updated%3A2023-10-27..2023-12-04&amp;type=Issues) | \[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2023-10-27..2023-12-04&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2023-10-27..2023-12-04&amp;type=Issues) | \[@krassowski\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akrassowski+updated%3A2023-10-27..2023-12-04&amp;type=Issues) | \[@pre-commit-ci\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Apre-commit-ci+updated%3A2023-10-27..2023-12-04&amp;type=Issues)

## 7.1.0a0\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id232)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/@jupyter-notebook/application-extension@7.0.6...0cd6104b926a398b419f2433538cef437592796f))

### Enhancements made\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id233)

- Added Lumino Plugin Description (#7008) \[#7127\](https://github.com/jupyter/notebook/pull/7127) (\[@Dilip-Jain\](https://github.com/Dilip-Jain))
- Update to JupyterLab 4.1 \[#7096\](https://github.com/jupyter/notebook/pull/7096) (\[@jtpio\](https://github.com/jtpio))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id234)

- Fix python bumping to \`minor\` \[#7131\](https://github.com/jupyter/notebook/pull/7131) (\[@jtpio\](https://github.com/jtpio))
- Add Python 3.12 classifier \[#7111\](https://github.com/jupyter/notebook/pull/7111) (\[@jtpio\](https://github.com/jtpio))

### Documentation improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id235)

- Set \`navigation\_with\_keys\` to \`False\` \[#7129\](https://github.com/jupyter/notebook/pull/7129) (\[@jtpio\](https://github.com/jtpio))
- Updated ui-tests Configuration in Contributing.md \[#7124\](https://github.com/jupyter/notebook/pull/7124) (\[@jayeshsingh9767\](https://github.com/jayeshsingh9767))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id236)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2023-10-17&amp;to=2023-10-27&amp;type=c))

\[@Dilip-Jain\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3ADilip-Jain+updated%3A2023-10-17..2023-10-27&amp;type=Issues) | \[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2023-10-17..2023-10-27&amp;type=Issues) | \[@jayeshsingh9767\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajayeshsingh9767+updated%3A2023-10-17..2023-10-27&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2023-10-17..2023-10-27&amp;type=Issues)

## v7.0\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#v7-0)

## 7.0.6\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id237)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/@jupyter-notebook/app@7.0.5...c62caffb02856737870cbc79a2cdb43b3e89c363))

### Bugs fixed\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id238)

- Updated fav-icon Base URL from JupyterLab PageConfig. \[#7109\](https://github.com/jupyter/notebook/pull/7109) (\[@jayeshsingh9767\](https://github.com/jayeshsingh9767))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id239)

- Fix typings \[#7110\](https://github.com/jupyter/notebook/pull/7110) (\[@jtpio\](https://github.com/jtpio))
- Bump postcss from 8.4.27 to 8.4.31 \[#7089\](https://github.com/jupyter/notebook/pull/7089) (\[@dependabot\](https://github.com/dependabot))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id240)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2023-10-12&amp;to=2023-10-17&amp;type=c))

\[@dependabot\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Adependabot+updated%3A2023-10-12..2023-10-17&amp;type=Issues) | \[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2023-10-12..2023-10-17&amp;type=Issues) | \[@jayeshsingh9767\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajayeshsingh9767+updated%3A2023-10-12..2023-10-17&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2023-10-12..2023-10-17&amp;type=Issues)

## 7.0.5\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id241)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/@jupyter-notebook/app@7.0.4...839193d07f0780ded6f559892517f061f3776b02))

### Enhancements made\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id242)

- Update to JupyterLab 4.0.7 \[#7103\](https://github.com/jupyter/notebook/pull/7103) (\[@jtpio\](https://github.com/jtpio))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id243)

- Update \`permissions\` in the galata snapshot workflow \[#7105\](https://github.com/jupyter/notebook/pull/7105) (\[@jtpio\](https://github.com/jtpio))
- Fix typings check on CI \[#7104\](https://github.com/jupyter/notebook/pull/7104) (\[@jtpio\](https://github.com/jtpio))
- Ignore yarn.lock for codespell \[#7098\](https://github.com/jupyter/notebook/pull/7098) (\[@jtpio\](https://github.com/jtpio))
- Remove link to the PDF documentation \[#7094\](https://github.com/jupyter/notebook/pull/7094) (\[@jtpio\](https://github.com/jtpio))
- Bump postcss from 8.4.23 to 8.4.31 in /ui-tests \[#7088\](https://github.com/jupyter/notebook/pull/7088) (\[@dependabot\](https://github.com/dependabot))
- React to the galata update comment \[#7086\](https://github.com/jupyter/notebook/pull/7086) (\[@jtpio\](https://github.com/jtpio))
- Switch from \`hub\` to \`gh\` in the Playwright snapshots update workflow \[#7085\](https://github.com/jupyter/notebook/pull/7085) (\[@jtpio\](https://github.com/jtpio))
- chore: update pre-commit hooks \[#7084\](https://github.com/jupyter/notebook/pull/7084) (\[@pre-commit-ci\](https://github.com/pre-commit-ci))
- Fix traitlets typing \[#7082\](https://github.com/jupyter/notebook/pull/7082) (\[@jtpio\](https://github.com/jtpio))
- Bump toshimaru/auto-author-assign from 2.0.0 to 2.0.1 \[#7080\](https://github.com/jupyter/notebook/pull/7080) (\[@dependabot\](https://github.com/dependabot))
- Bump toshimaru/auto-author-assign from 1.6.2 to 2.0.0 \[#7072\](https://github.com/jupyter/notebook/pull/7072) (\[@dependabot\](https://github.com/dependabot))
- ci: set minimal permissions to workflows \[#7070\](https://github.com/jupyter/notebook/pull/7070) (\[@diogoteles08\](https://github.com/diogoteles08))
- Bump systeminformation from 5.17.12 to 5.21.8 in /ui-tests \[#7064\](https://github.com/jupyter/notebook/pull/7064) (\[@dependabot\](https://github.com/dependabot))

### Documentation improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id244)

- Improve docs setup (SVG logos, repo links) \[#7074\](https://github.com/jupyter/notebook/pull/7074) (\[@krassowski\](https://github.com/krassowski))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id245)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2023-09-20&amp;to=2023-10-12&amp;type=c))

\[@dependabot\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Adependabot+updated%3A2023-09-20..2023-10-12&amp;type=Issues) | \[@diogoteles08\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Adiogoteles08+updated%3A2023-09-20..2023-10-12&amp;type=Issues) | \[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2023-09-20..2023-10-12&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2023-09-20..2023-10-12&amp;type=Issues) | \[@krassowski\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akrassowski+updated%3A2023-09-20..2023-10-12&amp;type=Issues) | \[@pre-commit-ci\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Apre-commit-ci+updated%3A2023-09-20..2023-10-12&amp;type=Issues)

## 7.0.4\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id246)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/@jupyter-notebook/app@7.0.3...0e62386fc71ed4bd424c989f9d5493ca346f1d9a))

### Enhancements made\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id247)

- Update to JupyterLab 4.0.6 \[#7049\](https://github.com/jupyter/notebook/pull/7049) (\[@jtpio\](https://github.com/jtpio))

### Bugs fixed\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id248)

- Fix \`app\_version\` \[#7061\](https://github.com/jupyter/notebook/pull/7061) (\[@jtpio\](https://github.com/jtpio))
- fix trusted status indication \[#7036\](https://github.com/jupyter/notebook/pull/7036) (\[@adigaboy\](https://github.com/adigaboy))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id249)

- Update Binder environment \[#7059\](https://github.com/jupyter/notebook/pull/7059) (\[@jtpio\](https://github.com/jtpio))
- Add \`deduplicate\` top-level script \[#7058\](https://github.com/jupyter/notebook/pull/7058) (\[@jtpio\](https://github.com/jtpio))
- Move opening path in new browser tabs to a separate plugin \[#7056\](https://github.com/jupyter/notebook/pull/7056) (\[@jtpio\](https://github.com/jtpio))
- Enable the Playwright trace \[#7050\](https://github.com/jupyter/notebook/pull/7050) (\[@jtpio\](https://github.com/jtpio))
- Bump actions/checkout from 3 to 4 \[#7040\](https://github.com/jupyter/notebook/pull/7040) (\[@dependabot\](https://github.com/dependabot))
- Adopt sp-repo-review \[#7039\](https://github.com/jupyter/notebook/pull/7039) (\[@blink1073\](https://github.com/blink1073))
- Add \`datetime.datetime.utc()\` to the filter list \[#7037\](https://github.com/jupyter/notebook/pull/7037) (\[@jtpio\](https://github.com/jtpio))
- Fix docs build on Gitpod \[#7026\](https://github.com/jupyter/notebook/pull/7026) (\[@jtpio\](https://github.com/jtpio))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id250)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2023-08-30&amp;to=2023-09-20&amp;type=c))

\[@adigaboy\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aadigaboy+updated%3A2023-08-30..2023-09-20&amp;type=Issues) | \[@blink1073\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ablink1073+updated%3A2023-08-30..2023-09-20&amp;type=Issues) | \[@dependabot\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Adependabot+updated%3A2023-08-30..2023-09-20&amp;type=Issues) | \[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2023-08-30..2023-09-20&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2023-08-30..2023-09-20&amp;type=Issues) | \[@pre-commit-ci\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Apre-commit-ci+updated%3A2023-08-30..2023-09-20&amp;type=Issues)

## 7.0.3\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id251)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/@jupyter-notebook/app@7.0.2...e2eb8f2a166ba7b339309b8bfbff40e6c9e0a9b9))

### Bugs fixed\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id252)

- Require importlib\_resources for testing on Python < 3.10 \[#7016\](https://github.com/jupyter/notebook/pull/7016) (\[@bnavigator\](https://github.com/bnavigator))
- Fix Python 3.12 compatibility \[#6965\](https://github.com/jupyter/notebook/pull/6965) (\[@frenzymadness\](https://github.com/frenzymadness))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id253)

- Update to JupyterLab 4.0.5 \[#7013\](https://github.com/jupyter/notebook/pull/7013) (\[@jtpio\](https://github.com/jtpio))
- Test against Python 3.12 \[#6999\](https://github.com/jupyter/notebook/pull/6999) (\[@jtpio\](https://github.com/jtpio))

### Documentation improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id254)

- Mention the nx graph in the contributing guide \[#7001\](https://github.com/jupyter/notebook/pull/7001) (\[@jtpio\](https://github.com/jtpio))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id255)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2023-08-04&amp;to=2023-08-30&amp;type=c))

\[@bnavigator\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Abnavigator+updated%3A2023-08-04..2023-08-30&amp;type=Issues) | \[@defjaf\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Adefjaf+updated%3A2023-08-04..2023-08-30&amp;type=Issues) | \[@frenzymadness\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Afrenzymadness+updated%3A2023-08-04..2023-08-30&amp;type=Issues) | \[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2023-08-04..2023-08-30&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2023-08-04..2023-08-30&amp;type=Issues) | \[@kevin-bates\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akevin-bates+updated%3A2023-08-04..2023-08-30&amp;type=Issues)

## 7.0.2\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id256)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/@jupyter-notebook/app@7.0.1...af5edd42374cadba65feed2e6828b1ef96295daf))

### Enhancements made\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id257)

- Update to JupyterLab 4.0.4 packages \[#6998\](https://github.com/jupyter/notebook/pull/6998) (\[@jtpio\](https://github.com/jtpio))
- Improve about dialog \[#6996\](https://github.com/jupyter/notebook/pull/6996) (\[@yjrab\](https://github.com/yjrab))
- Added documentation link in Help menu \[#6993\](https://github.com/jupyter/notebook/pull/6993) (\[@Mikil03\](https://github.com/Mikil03))

### Bugs fixed\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id258)

- Remove \`RedirectHandler\` \[#6997\](https://github.com/jupyter/notebook/pull/6997) (\[@jtpio\](https://github.com/jtpio))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id259)

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id260)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2023-07-31&amp;to=2023-08-04&amp;type=c))

\[@echarles\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aecharles+updated%3A2023-07-31..2023-08-04&amp;type=Issues) | \[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2023-07-31..2023-08-04&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2023-07-31..2023-08-04&amp;type=Issues) | \[@kevin-bates\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akevin-bates+updated%3A2023-07-31..2023-08-04&amp;type=Issues) | \[@Mikil03\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AMikil03+updated%3A2023-07-31..2023-08-04&amp;type=Issues) | \[@pre-commit-ci\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Apre-commit-ci+updated%3A2023-07-31..2023-08-04&amp;type=Issues) | \[@shaneknapp\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ashaneknapp+updated%3A2023-07-31..2023-08-04&amp;type=Issues) | \[@yjrab\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ayjrab+updated%3A2023-07-31..2023-08-04&amp;type=Issues) | \[@Zsailer\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AZsailer+updated%3A2023-07-31..2023-08-04&amp;type=Issues)

## 7.0.1\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id261)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/@jupyter-notebook/app@7.0.0...ac3c882a246b46c15c1963ef4b65427a4257b132))

### Enhancements made\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id262)

- Update accessibly compliance section in the docs \[#6982\](https://github.com/jupyter/notebook/pull/6982) (\[@andrii-i\](https://github.com/andrii-i))
- Update the browser tab favicon on kernel busy \[#6980\](https://github.com/jupyter/notebook/pull/6980) (\[@jtpio\](https://github.com/jtpio))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id263)

- Bump \`word-wrap\` and \`semver\` \[#6979\](https://github.com/jupyter/notebook/pull/6979) (\[@jtpio\](https://github.com/jtpio))
- Enable lerna caching for build scripts \[#6767\](https://github.com/jupyter/notebook/pull/6767) (\[@jtpio\](https://github.com/jtpio))

### Documentation improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id264)

- Update accessibly compliance section in the docs \[#6982\](https://github.com/jupyter/notebook/pull/6982) (\[@andrii-i\](https://github.com/andrii-i))
- Fix link in \`README.md\` \[#6973\](https://github.com/jupyter/notebook/pull/6973) (\[@jtpio\](https://github.com/jtpio))
- The future is now \[#6972\](https://github.com/jupyter/notebook/pull/6972) (\[@frenzymadness\](https://github.com/frenzymadness))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id265)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2023-07-19&amp;to=2023-07-31&amp;type=c))

\[@andrii-i\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aandrii-i+updated%3A2023-07-19..2023-07-31&amp;type=Issues) | \[@echarles\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aecharles+updated%3A2023-07-19..2023-07-31&amp;type=Issues) | \[@frenzymadness\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Afrenzymadness+updated%3A2023-07-19..2023-07-31&amp;type=Issues) | \[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2023-07-19..2023-07-31&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2023-07-19..2023-07-31&amp;type=Issues) | \[@prof-lupin\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aprof-lupin+updated%3A2023-07-19..2023-07-31&amp;type=Issues)

## 7.0.0\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id266)

Jupyter Notebook 7 is released :tada:

Check the changelog: https://jupyter-notebook.readthedocs.io/en/latest/changelog.html

And the new features in Notebook 7: https://jupyter-notebook.readthedocs.io/en/latest/notebook\_7\_features.html

Migration Guide: https://jupyter-notebook.readthedocs.io/en/latest/migrate\_to\_notebook7.html

For reference here is the changelog since the last \`7.0.0rc2\` release.

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/v7.0.0rc2...2be98e8f39af7f3ec2729006018f6baf0998f94b))

### Bugs fixed\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id267)

- Update Jupytext Notebook url path \[#6961\](https://github.com/jupyter/notebook/pull/6961) (\[@RRosio\](https://github.com/RRosio))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id268)

- Fix hatch version when going from rc \[#6971\](https://github.com/jupyter/notebook/pull/6971) (\[@jtpio\](https://github.com/jtpio))
- Update to JupyterLab 4.0.3 \[#6967\](https://github.com/jupyter/notebook/pull/6967) (\[@jtpio\](https://github.com/jtpio))
- Bump semver from 7.5.0 to 7.5.3 in /ui-tests \[#6950\](https://github.com/jupyter/notebook/pull/6950) (\[@dependabot\](https://github.com/dependabot))

### Documentation improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id269)

- fix: update link to troubleshooting guidelines \[#6964\](https://github.com/jupyter/notebook/pull/6964) (\[@emmanuel-ferdman\](https://github.com/emmanuel-ferdman))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id270)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2023-06-26&amp;to=2023-07-19&amp;type=c))

\[@dependabot\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Adependabot+updated%3A2023-06-26..2023-07-19&amp;type=Issues) | \[@emmanuel-ferdman\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aemmanuel-ferdman+updated%3A2023-06-26..2023-07-19&amp;type=Issues) | \[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2023-06-26..2023-07-19&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2023-06-26..2023-07-19&amp;type=Issues) | \[@parmentelat\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aparmentelat+updated%3A2023-06-26..2023-07-19&amp;type=Issues) | \[@pre-commit-ci\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Apre-commit-ci+updated%3A2023-06-26..2023-07-19&amp;type=Issues) | \[@RRosio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3ARRosio+updated%3A2023-06-26..2023-07-19&amp;type=Issues)

## 7.0.0rc2\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#rc2)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/v7.0.0rc1...27c00bc56afaa5b89713f760b0cc6eb88079224e))

### Bugs fixed\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id271)

- Fix opening files from the CLI \[#6946\](https://github.com/jupyter/notebook/pull/6946) (\[@jtpio\](https://github.com/jtpio))
- Fix handling of the base url \[#6943\](https://github.com/jupyter/notebook/pull/6943) (\[@jtpio\](https://github.com/jtpio))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id272)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2023-06-22&amp;to=2023-06-26&amp;type=c))

\[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2023-06-22..2023-06-26&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2023-06-22..2023-06-26&amp;type=Issues) | \[@parmentelat\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aparmentelat+updated%3A2023-06-22..2023-06-26&amp;type=Issues)

## 7.0.0rc1\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id273)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/v7.0.0rc0...8493e1ba21ebaca5c192d68bdc829ccc5b29a799))

### Enhancements made\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id274)

- Close the browser tab when clicking on “Close and Shut Down Notebook” \[#6937\](https://github.com/jupyter/notebook/pull/6937) (\[@jtpio\](https://github.com/jtpio))

### Bugs fixed\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id275)

- Fix the redirect handler \[#6941\](https://github.com/jupyter/notebook/pull/6941) (\[@jtpio\](https://github.com/jtpio))
- Make jupyter logo select properly (#6927) \[#6938\](https://github.com/jupyter/notebook/pull/6938) (\[@Cheukting\](https://github.com/Cheukting))

### Documentation improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id276)

- Update issue templates \[#6939\](https://github.com/jupyter/notebook/pull/6939) (\[@RRosio\](https://github.com/RRosio))
- Docs parity for find with JupyterLab. \[#6917\](https://github.com/jupyter/notebook/pull/6917) (\[@ericsnekbytes\](https://github.com/ericsnekbytes))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id277)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2023-06-19&amp;to=2023-06-22&amp;type=c))

\[@andrii-i\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aandrii-i+updated%3A2023-06-19..2023-06-22&amp;type=Issues) | \[@Cheukting\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3ACheukting+updated%3A2023-06-19..2023-06-22&amp;type=Issues) | \[@ericsnekbytes\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aericsnekbytes+updated%3A2023-06-19..2023-06-22&amp;type=Issues) | \[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2023-06-19..2023-06-22&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2023-06-19..2023-06-22&amp;type=Issues) | \[@RRosio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3ARRosio+updated%3A2023-06-19..2023-06-22&amp;type=Issues)

## 7.0.0rc0\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id278)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/v7.0.0b4...d0692112a4b2db20c2178205d4b5630184acbf7b))

### Enhancements made\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id279)

- Update JupyterLab, audit document viewers \[#6922\](https://github.com/jupyter/notebook/pull/6922) (\[@jtpio\](https://github.com/jtpio))
- Customize the shell layout with the settings \[#6921\](https://github.com/jupyter/notebook/pull/6921) (\[@jtpio\](https://github.com/jtpio))

### Bugs fixed\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id280)

- Fix default viewers override \[#6923\](https://github.com/jupyter/notebook/pull/6923) (\[@jtpio\](https://github.com/jtpio))
- Align JupyterHub config with JupyterLab \[#6918\](https://github.com/jupyter/notebook/pull/6918) (\[@jtpio\](https://github.com/jtpio))

### Documentation improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id281)

- Added example of custom css files \[#6919\](https://github.com/jupyter/notebook/pull/6919) (\[@RRosio\](https://github.com/RRosio))

### API and Breaking Changes\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#api-and-breaking-changes)

- Customize the shell layout with the settings \[#6921\](https://github.com/jupyter/notebook/pull/6921) (\[@jtpio\](https://github.com/jtpio))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id282)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2023-06-12&amp;to=2023-06-19&amp;type=c))

\[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2023-06-12..2023-06-19&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2023-06-12..2023-06-19&amp;type=Issues) | \[@RRosio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3ARRosio+updated%3A2023-06-12..2023-06-19&amp;type=Issues)

## 7.0.0b4\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#b4)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/v7.0.0b3...ee3e1c221226d482ca1c9bec6362c8af36f1da56))

### Enhancements made\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id283)

- Rename browser tab title to Home \[#6913\](https://github.com/jupyter/notebook/pull/6913) (\[@Cheukting\](https://github.com/Cheukting))
- Add the notification plugin \[#6900\](https://github.com/jupyter/notebook/pull/6900) (\[@jtpio\](https://github.com/jtpio))
- Configurable \`default\_url\` for JupyterNotebookApp \[#6899\](https://github.com/jupyter/notebook/pull/6899) (\[@paulgb\](https://github.com/paulgb))
- Enhancement: Added drop shadows to markdown, text, and tree views \[#6893\](https://github.com/jupyter/notebook/pull/6893) (\[@rielAsh24\](https://github.com/rielAsh24))
- Update to JupyterLab 4.0.1 \[#6892\](https://github.com/jupyter/notebook/pull/6892) (\[@jtpio\](https://github.com/jtpio))
- Add file browser actions to the file browser toolbar \[#6888\](https://github.com/jupyter/notebook/pull/6888) (\[@jtpio\](https://github.com/jtpio))
- Add option to open a notebook in NbClassic if it is installed; show “Open in…” dropdown menu if there are multiple options, show single button otherwise \[#6866\](https://github.com/jupyter/notebook/pull/6866) (\[@andrii-i\](https://github.com/andrii-i))
- Load custom CSS \[#6841\](https://github.com/jupyter/notebook/pull/6841) (\[@RRosio\](https://github.com/RRosio))

### Bugs fixed\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id284)

- Add an empty splash screen on notebook launch to avoid a flash of unstyled content \[#6911\](https://github.com/jupyter/notebook/pull/6911) (\[@andrii-i\](https://github.com/andrii-i))
- Fix for “find searches only part of the file” bug \[#6905\](https://github.com/jupyter/notebook/pull/6905) (\[@ericsnekbytes\](https://github.com/ericsnekbytes))
- Provide a custom rendermime plugin to handle local links \[#6885\](https://github.com/jupyter/notebook/pull/6885) (\[@jtpio\](https://github.com/jtpio))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id285)

- Fix check links on CI \[#6910\](https://github.com/jupyter/notebook/pull/6910) (\[@jtpio\](https://github.com/jtpio))
- Add \`JSONLicenseWebpackPlugin\` \[#6896\](https://github.com/jupyter/notebook/pull/6896) (\[@jtpio\](https://github.com/jtpio))
- Simplify Gitpod setup \[#6894\](https://github.com/jupyter/notebook/pull/6894) (\[@jtpio\](https://github.com/jtpio))
- Fix action name in update workflow \[#6884\](https://github.com/jupyter/notebook/pull/6884) (\[@jtpio\](https://github.com/jtpio))
- Fix playwright bot \[#6880\](https://github.com/jupyter/notebook/pull/6880) (\[@jtpio\](https://github.com/jtpio))

### Documentation improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id286)

- Document how to manage plugins and extensions \[#6909\](https://github.com/jupyter/notebook/pull/6909) (\[@jtpio\](https://github.com/jtpio))
- Jupyter Notebook ecosystem docs improvements \[#6877\](https://github.com/jupyter/notebook/pull/6877) (\[@ericsnekbytes\](https://github.com/ericsnekbytes))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id287)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2023-05-25&amp;to=2023-06-12&amp;type=c))

\[@andrii-i\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aandrii-i+updated%3A2023-05-25..2023-06-12&amp;type=Issues) | \[@Cheukting\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3ACheukting+updated%3A2023-05-25..2023-06-12&amp;type=Issues) | \[@echarles\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aecharles+updated%3A2023-05-25..2023-06-12&amp;type=Issues) | \[@ericsnekbytes\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aericsnekbytes+updated%3A2023-05-25..2023-06-12&amp;type=Issues) | \[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2023-05-25..2023-06-12&amp;type=Issues) | \[@henryiii\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ahenryiii+updated%3A2023-05-25..2023-06-12&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2023-05-25..2023-06-12&amp;type=Issues) | \[@krassowski\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akrassowski+updated%3A2023-05-25..2023-06-12&amp;type=Issues) | \[@paulgb\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Apaulgb+updated%3A2023-05-25..2023-06-12&amp;type=Issues) | \[@pre-commit-ci\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Apre-commit-ci+updated%3A2023-05-25..2023-06-12&amp;type=Issues) | \[@rielAsh24\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3ArielAsh24+updated%3A2023-05-25..2023-06-12&amp;type=Issues) | \[@RRosio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3ARRosio+updated%3A2023-05-25..2023-06-12&amp;type=Issues) | \[@yuvipanda\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ayuvipanda+updated%3A2023-05-25..2023-06-12&amp;type=Issues)

## 7.0.0b3\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id288)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/v7.0.0b2...93e4d5e1c6ed7a3a4875eed284255587ac293819))

### Enhancements made\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id289)

- Copy edits for \`migrate\_to\_notebook7\` \[#6879\](https://github.com/jupyter/notebook/pull/6879) (\[@JasonWeill\](https://github.com/JasonWeill))
- Enable add a cell button \[#6872\](https://github.com/jupyter/notebook/pull/6872) (\[@tuncbkose\](https://github.com/tuncbkose))
- Update to JupyterLab 4 final \[#6871\](https://github.com/jupyter/notebook/pull/6871) (\[@jtpio\](https://github.com/jtpio))
- Remove “Close Tab” menu entry \[#6843\](https://github.com/jupyter/notebook/pull/6843) (\[@timmerk3\](https://github.com/timmerk3))

### Bugs fixed\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id290)

- Fix handling of the default factory in the URL \[#6873\](https://github.com/jupyter/notebook/pull/6873) (\[@jtpio\](https://github.com/jtpio))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id291)

- Update to Playwright 1.33 \[#6874\](https://github.com/jupyter/notebook/pull/6874) (\[@jtpio\](https://github.com/jtpio))
- Fix check links on CI \[#6870\](https://github.com/jupyter/notebook/pull/6870) (\[@jtpio\](https://github.com/jtpio))

### Documentation improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id292)

- Copy edits for \`migrate\_to\_notebook7\` \[#6879\](https://github.com/jupyter/notebook/pull/6879) (\[@JasonWeill\](https://github.com/JasonWeill))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id293)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2023-05-09&amp;to=2023-05-25&amp;type=c))

\[@andrii-i\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aandrii-i+updated%3A2023-05-09..2023-05-25&amp;type=Issues) | \[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2023-05-09..2023-05-25&amp;type=Issues) | \[@JasonWeill\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AJasonWeill+updated%3A2023-05-09..2023-05-25&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2023-05-09..2023-05-25&amp;type=Issues) | \[@timmerk3\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Atimmerk3+updated%3A2023-05-09..2023-05-25&amp;type=Issues) | \[@tuncbkose\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Atuncbkose+updated%3A2023-05-09..2023-05-25&amp;type=Issues)

## 7.0.0b2\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id294)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/v7.0.0b1...c0071d796019c0221df4900313b51c0529438bcf))

### Enhancements made\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id295)

- Update to JupyterLab 4.0.0rc1 \[#6864\](https://github.com/jupyter/notebook/pull/6864) (\[@jtpio\](https://github.com/jtpio))
- Change “Interface” menu to “Open in…”, shorten names of menu items inside \[#6847\](https://github.com/jupyter/notebook/pull/6847) (\[@andrii-i\](https://github.com/andrii-i))
- Add Skip Link to Notebook \[#6844\](https://github.com/jupyter/notebook/pull/6844) (\[@seirani\](https://github.com/seirani))

### Bugs fixed\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id296)

- Fix top bar visibility not picking up settings overrides (#6833) \[#6836\](https://github.com/jupyter/notebook/pull/6836) (\[@yumyumqing\](https://github.com/yumyumqing))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id297)

- Update RTD image \[#6861\](https://github.com/jupyter/notebook/pull/6861) (\[@blink1073\](https://github.com/blink1073))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id298)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2023-04-28&amp;to=2023-05-09&amp;type=c))

\[@andrii-i\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aandrii-i+updated%3A2023-04-28..2023-05-09&amp;type=Issues) | \[@blink1073\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ablink1073+updated%3A2023-04-28..2023-05-09&amp;type=Issues) | \[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2023-04-28..2023-05-09&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2023-04-28..2023-05-09&amp;type=Issues) | \[@pre-commit-ci\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Apre-commit-ci+updated%3A2023-04-28..2023-05-09&amp;type=Issues) | \[@seirani\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aseirani+updated%3A2023-04-28..2023-05-09&amp;type=Issues) | \[@yumyumqing\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ayumyumqing+updated%3A2023-04-28..2023-05-09&amp;type=Issues)

## 7.0.0b1\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id299)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/v7.0.0b0...4b6af274b24bcc20e43ad2330c9243c8d2c7d552))

### Enhancements made\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id300)

- Update to JupyterLab 4.0.0rc0 \[#6853\](https://github.com/jupyter/notebook/pull/6853) (\[@jtpio\](https://github.com/jtpio))
- Update to JupyterLab \`4.0.0b1\` and \`4.0.0b2\` \[#6838\](https://github.com/jupyter/notebook/pull/6838) (\[@jtpio\](https://github.com/jtpio))

### Bugs fixed\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id301)

- Fixes the notebooktools \[#6834\](https://github.com/jupyter/notebook/pull/6834) (\[@brichet\](https://github.com/brichet))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id302)

- Use local coverage \[#6839\](https://github.com/jupyter/notebook/pull/6839) (\[@blink1073\](https://github.com/blink1073))

### Documentation improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id303)

- Added extra information and user-action summaries to 7 migration docs. \[#6850\](https://github.com/jupyter/notebook/pull/6850) (\[@ericsnekbytes\](https://github.com/ericsnekbytes))
- Rename migration file to \`migrate\_to\_notebook7\` \[#6831\](https://github.com/jupyter/notebook/pull/6831) (\[@jtpio\](https://github.com/jtpio))
- Use correct canonical URL while building docs \[#6829\](https://github.com/jupyter/notebook/pull/6829) (\[@ashwinvis\](https://github.com/ashwinvis))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id304)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2023-04-04&amp;to=2023-04-28&amp;type=c))

\[@ashwinvis\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aashwinvis+updated%3A2023-04-04..2023-04-28&amp;type=Issues) | \[@blink1073\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ablink1073+updated%3A2023-04-04..2023-04-28&amp;type=Issues) | \[@brichet\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Abrichet+updated%3A2023-04-04..2023-04-28&amp;type=Issues) | \[@ericsnekbytes\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aericsnekbytes+updated%3A2023-04-04..2023-04-28&amp;type=Issues) | \[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2023-04-04..2023-04-28&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2023-04-04..2023-04-28&amp;type=Issues)

## 7.0.0b0\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id305)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/v7.0.0a18...b99718f57a8beac7b4019901a57c94984781dd49))

### Enhancements made\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id306)

- Update to JupyterLab \`4.0.0b0\` \[#6803\](https://github.com/jupyter/notebook/pull/6803) (\[@jtpio\](https://github.com/jtpio))

### Bugs fixed\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id307)

- added white space to bottom of edit files \[#6804\](https://github.com/jupyter/notebook/pull/6804) (\[@jesuscastillx\](https://github.com/jesuscastillx))
- Hides 'micro' toolbars in notebook \[#6791\](https://github.com/jupyter/notebook/pull/6791) (\[@JasonWeill\](https://github.com/JasonWeill))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id308)

- Add missing singleton packages for RTC \[#6816\](https://github.com/jupyter/notebook/pull/6816) (\[@jtpio\](https://github.com/jtpio))

### Documentation improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id309)

- Improve the documentation for Notebook 7 \[#6813\](https://github.com/jupyter/notebook/pull/6813) (\[@jtpio\](https://github.com/jtpio))
- fix typo in the migration guide \[#6812\](https://github.com/jupyter/notebook/pull/6812) (\[@Tiksagol\](https://github.com/Tiksagol))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id310)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2023-03-24&amp;to=2023-04-04&amp;type=c))

\[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2023-03-24..2023-04-04&amp;type=Issues) | \[@j-publius\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aj-publius+updated%3A2023-03-24..2023-04-04&amp;type=Issues) | \[@JasonWeill\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AJasonWeill+updated%3A2023-03-24..2023-04-04&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2023-03-24..2023-04-04&amp;type=Issues) | \[@pre-commit-ci\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Apre-commit-ci+updated%3A2023-03-24..2023-04-04&amp;type=Issues) | \[@Tiksagol\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3ATiksagol+updated%3A2023-03-24..2023-04-04&amp;type=Issues)

## 7.0.0a18\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#a18)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/v7.0.0a17...253efe279f8c8005f016f3dfe28c22233ee1d2dd))

### Enhancements made\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id311)

- Add back the \`csvviewer-extension\` \[#6799\](https://github.com/jupyter/notebook/pull/6799) (\[@jtpio\](https://github.com/jtpio))
- Fix JSON setting editor not opening issue \[#6795\](https://github.com/jupyter/notebook/pull/6795) (\[@yumyumqing\](https://github.com/yumyumqing))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id312)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2023-03-20&amp;to=2023-03-24&amp;type=c))

\[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2023-03-20..2023-03-24&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2023-03-20..2023-03-24&amp;type=Issues) | \[@yumyumqing\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ayumyumqing+updated%3A2023-03-20..2023-03-24&amp;type=Issues)

## 7.0.0a17\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#a17)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/v7.0.0a16...7903de83e83a6ce342d71895dc1e8c2ec8128174))

### Highlights\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id313)

This major change in this release is the update to the latest JupyterLab \`4.0.0a37\` .

Check out the \[JupyterLab \`4.0.0a37\` release notes\](https://github.com/jupyterlab/jupyterlab/releases/tag/v4.0.0a37) for more details.

### Enhancements made\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id314)

- Update to JupyterLab 4.0.0a37 \[#6777\](https://github.com/jupyter/notebook/pull/6777) (\[@jtpio\](https://github.com/jtpio))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id315)

- Replace the use of \`toArray\` by \`Array.from\` \[#6775\](https://github.com/jupyter/notebook/pull/6775) ( \`@tarunsamanta2k20\` )

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id316)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2023-03-15&amp;to=2023-03-20&amp;type=c))

\[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2023-03-15..2023-03-20&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2023-03-15..2023-03-20&amp;type=Issues) | \[@tarunsamanta2k20\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Atarunsamanta2k20+updated%3A2023-03-15..2023-03-20&amp;type=Issues)

## 7.0.0a16\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#a16)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/v7.0.0a15...0faa88c8b65e0302f1904e4ca9cd2e551525f352))

### Enhancements made\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id317)

- Update to JupyterLab 4.0.0a36 \[#6773\](https://github.com/jupyter/notebook/pull/6773) (\[@jtpio\](https://github.com/jtpio))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id318)

- Clean up interface switcher plugin in preparation for release \[#6766\](https://github.com/jupyter/notebook/pull/6766) (\[@afshin\](https://github.com/afshin))
- Remove empty \`py.test\` file \[#6764\](https://github.com/jupyter/notebook/pull/6764) (\[@frenzymadness\](https://github.com/frenzymadness))

### Documentation improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id319)

- Add documentation for contributing to the docs \[#6771\](https://github.com/jupyter/notebook/pull/6771) (\[@jtpio\](https://github.com/jtpio))
- Convert docs to Markdown \[#6770\](https://github.com/jupyter/notebook/pull/6770) (\[@jtpio\](https://github.com/jtpio))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id320)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2023-03-08&amp;to=2023-03-15&amp;type=c))

\[@afshin\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aafshin+updated%3A2023-03-08..2023-03-15&amp;type=Issues) | \[@frenzymadness\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Afrenzymadness+updated%3A2023-03-08..2023-03-15&amp;type=Issues) | \[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2023-03-08..2023-03-15&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2023-03-08..2023-03-15&amp;type=Issues)

## 7.0.0a15\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#a15)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/v7.0.0a14...1ccb8f15d6bf3557eed2405438a9df3c1d6cd040))

### Enhancements made\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id321)

- Update to JupyterLab 4.0.0a35 \[#6757\](https://github.com/jupyter/notebook/pull/6757) (\[@jtpio\](https://github.com/jtpio))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id322)

- Bump vega from 5.22.1 to 5.23.0 in /ui-tests \[#6756\](https://github.com/jupyter/notebook/pull/6756) (\[@dependabot\](https://github.com/dependabot))
- Bump vega-functions from 5.13.0 to 5.13.1 in /ui-tests \[#6754\](https://github.com/jupyter/notebook/pull/6754) (\[@dependabot\](https://github.com/dependabot))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id323)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2023-03-01&amp;to=2023-03-08&amp;type=c))

\[@dependabot\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Adependabot+updated%3A2023-03-01..2023-03-08&amp;type=Issues) | \[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2023-03-01..2023-03-08&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2023-03-01..2023-03-08&amp;type=Issues) | \[@pre-commit-ci\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Apre-commit-ci+updated%3A2023-03-01..2023-03-08&amp;type=Issues)

## 7.0.0a14\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#a14)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/v7.0.0a13...f9e427cf4e92dbaa5794fe0331ca92b41d45d52c))

### Enhancements made\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id324)

- Fix loading of plugins \[#6750\](https://github.com/jupyter/notebook/pull/6750) (\[@jtpio\](https://github.com/jtpio))
- Add the extension manager \[#6747\](https://github.com/jupyter/notebook/pull/6747) (\[@jtpio\](https://github.com/jtpio))
- File browser CSS tweaks \[#6738\](https://github.com/jupyter/notebook/pull/6738) (\[@jtpio\](https://github.com/jtpio))
- Add trusted indicator \[#6736\](https://github.com/jupyter/notebook/pull/6736) (\[@jtpio\](https://github.com/jtpio))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id325)

- Clean up license \[#6743\](https://github.com/jupyter/notebook/pull/6743) (\[@dcsaba89\](https://github.com/dcsaba89))
- Update to TypeScript 5 \[#6735\](https://github.com/jupyter/notebook/pull/6735) (\[@jtpio\](https://github.com/jtpio))
- Enable \`nx\` \[#6718\](https://github.com/jupyter/notebook/pull/6718) (\[@jtpio\](https://github.com/jtpio))

### Documentation improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id326)

- Corrected “Recomment” to “Recommend” \[#6741\](https://github.com/jupyter/notebook/pull/6741) (\[@Tony-j77\](https://github.com/Tony-j77))
- Docs: add migrate to notebook7 page \[#6737\](https://github.com/jupyter/notebook/pull/6737) (\[@echarles\](https://github.com/echarles))
- Add section about updating reference snapshots \[#6733\](https://github.com/jupyter/notebook/pull/6733) (\[@jtpio\](https://github.com/jtpio))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id327)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2023-02-15&amp;to=2023-03-01&amp;type=c))

\[@dcsaba89\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Adcsaba89+updated%3A2023-02-15..2023-03-01&amp;type=Issues) | \[@echarles\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aecharles+updated%3A2023-02-15..2023-03-01&amp;type=Issues) | \[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2023-02-15..2023-03-01&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2023-02-15..2023-03-01&amp;type=Issues) | \[@RRosio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3ARRosio+updated%3A2023-02-15..2023-03-01&amp;type=Issues) | \[@Tony-j77\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3ATony-j77+updated%3A2023-02-15..2023-03-01&amp;type=Issues)

## 7.0.0a13\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#a13)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/v7.0.0a12...ef67879306b27dfa78b8d639d9cc142b50f8c7ba))

### Enhancements made\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id328)

- Update to JupyterLab 4.0.0a34 \[#6732\](https://github.com/jupyter/notebook/pull/6732) (\[@jtpio\](https://github.com/jtpio))
- Hide the debugger button on mobile \[#6731\](https://github.com/jupyter/notebook/pull/6731) (\[@jtpio\](https://github.com/jtpio))
- Adds translator to the NotebookShell \[#6725\](https://github.com/jupyter/notebook/pull/6725) (\[@brichet\](https://github.com/brichet))
- Resolving some accessibility issues \[#6719\](https://github.com/jupyter/notebook/pull/6719) (\[@brichet\](https://github.com/brichet))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id329)

- Fix Playwright snapshot update workflow \[#6724\](https://github.com/jupyter/notebook/pull/6724) (\[@jtpio\](https://github.com/jtpio))
- Add workflow to update snapshots \[#6723\](https://github.com/jupyter/notebook/pull/6723) (\[@jtpio\](https://github.com/jtpio))
- Use Playwright \`webServer\` \[#6720\](https://github.com/jupyter/notebook/pull/6720) (\[@jtpio\](https://github.com/jtpio))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id330)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2023-02-08&amp;to=2023-02-15&amp;type=c))

\[@brichet\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Abrichet+updated%3A2023-02-08..2023-02-15&amp;type=Issues) | \[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2023-02-08..2023-02-15&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2023-02-08..2023-02-15&amp;type=Issues) | \[@pre-commit-ci\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Apre-commit-ci+updated%3A2023-02-08..2023-02-15&amp;type=Issues)

## 7.0.0a12\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#a12)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/v7.0.0a11...27c2bfbb80d42a3fd2541b13fae6143e2e91e4dd))

### Enhancements made\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id331)

- Update to JupyterLab 4.0.0a33 \[#6713\](https://github.com/jupyter/notebook/pull/6713) (\[@jtpio\](https://github.com/jtpio))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id332)

- Add more lint checks \[#6706\](https://github.com/jupyter/notebook/pull/6706) (\[@blink1073\](https://github.com/blink1073))
- Reintroduce desktop file \[#6705\](https://github.com/jupyter/notebook/pull/6705) (\[@frenzymadness\](https://github.com/frenzymadness))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id333)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2023-01-19&amp;to=2023-02-08&amp;type=c))

\[@blink1073\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ablink1073+updated%3A2023-01-19..2023-02-08&amp;type=Issues) | \[@frenzymadness\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Afrenzymadness+updated%3A2023-01-19..2023-02-08&amp;type=Issues) | \[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2023-01-19..2023-02-08&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2023-01-19..2023-02-08&amp;type=Issues)

## 7.0.0a11\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#a11)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/v7.0.0a10...6d4eeed9d176e2523be7874ae4d9f46a99422d72))

### Enhancements made\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id334)

- Tree view enhancement \[#6588\](https://github.com/jupyter/notebook/pull/6588) (\[@brichet\](https://github.com/brichet))
- Add the Settings Editor to the landing page \[#6316\](https://github.com/jupyter/notebook/pull/6316) (\[@jtpio\](https://github.com/jtpio))

### Bugs fixed\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id335)

- Fix console error when adding a widget to a side panel \[#6694\](https://github.com/jupyter/notebook/pull/6694) (\[@jtpio\](https://github.com/jtpio))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id336)

- Help-extension split into multiple plugins \[#6700\](https://github.com/jupyter/notebook/pull/6700) (\[@RRosio\](https://github.com/RRosio))
- Add releaser workflows \[#6698\](https://github.com/jupyter/notebook/pull/6698) (\[@blink1073\](https://github.com/blink1073))
- Create \`auto\_author\_assign.yml\` workflow \[#6696\](https://github.com/jupyter/notebook/pull/6696) (\[@jtpio\](https://github.com/jtpio))
- Add back \`# type:ignore\` \[#6695\](https://github.com/jupyter/notebook/pull/6695) (\[@jtpio\](https://github.com/jtpio))
- Fix environment activation on Gitpod \[#6693\](https://github.com/jupyter/notebook/pull/6693) (\[@jtpio\](https://github.com/jtpio))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id337)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2023-01-09&amp;to=2023-01-19&amp;type=c))

\[@blink1073\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ablink1073+updated%3A2023-01-09..2023-01-19&amp;type=Issues) | \[@brichet\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Abrichet+updated%3A2023-01-09..2023-01-19&amp;type=Issues) | \[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2023-01-09..2023-01-19&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2023-01-09..2023-01-19&amp;type=Issues) | \[@RRosio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3ARRosio+updated%3A2023-01-09..2023-01-19&amp;type=Issues)

## 7.0.0a10\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#a10)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/v7.0.0a9...6205bf376f783b7202af71e1074f44086ee7056c))

### Enhancements made\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id338)

- Update to JupyterLab 4.0.0a32 \[#6678\](https://github.com/jupyter/notebook/pull/6678) (\[@jtpio\](https://github.com/jtpio))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id339)

- Bump json5 from 2.2.1 to 2.2.3 in /ui-tests \[#6684\](https://github.com/jupyter/notebook/pull/6684) (\[@dependabot\](https://github.com/dependabot))
- Bump json5 from 1.0.1 to 1.0.2 \[#6681\](https://github.com/jupyter/notebook/pull/6681) (\[@dependabot\](https://github.com/dependabot))
- Update the copyright date to 2023 in the about dialog \[#6679\](https://github.com/jupyter/notebook/pull/6679) (\[@jtpio\](https://github.com/jtpio))
- Fix \`check\_links\` and \`Test Lint\` CI failures \[#6675\](https://github.com/jupyter/notebook/pull/6675) (\[@jtpio\](https://github.com/jtpio))
- Add spelling and docstring enforcement \[#6669\](https://github.com/jupyter/notebook/pull/6669) (\[@blink1073\](https://github.com/blink1073))
- CI Cleanup \[#6667\](https://github.com/jupyter/notebook/pull/6667) (\[@blink1073\](https://github.com/blink1073))
- Adopt ruff and typing \[#6658\](https://github.com/jupyter/notebook/pull/6658) (\[@blink1073\](https://github.com/blink1073))
- Bump decode-uri-component from 0.2.0 to 0.2.2 \[#6651\](https://github.com/jupyter/notebook/pull/6651) (\[@dependabot\](https://github.com/dependabot))
- Bump dessant/lock-threads from 3 to 4 \[#6650\](https://github.com/jupyter/notebook/pull/6650) (\[@dependabot\](https://github.com/dependabot))
- Update to TypeScript 4.9 \[#6640\](https://github.com/jupyter/notebook/pull/6640) (\[@jtpio\](https://github.com/jtpio))
- Add more Python tests \[#6639\](https://github.com/jupyter/notebook/pull/6639) (\[@blink1073\](https://github.com/blink1073))
- use main branch for config \[#6638\](https://github.com/jupyter/notebook/pull/6638) (\[@blink1073\](https://github.com/blink1073))
- Clean up workflows \[#6635\](https://github.com/jupyter/notebook/pull/6635) (\[@blink1073\](https://github.com/blink1073))
- CI Cleanup \[#6631\](https://github.com/jupyter/notebook/pull/6631) (\[@blink1073\](https://github.com/blink1073))
- Fix issue template formatting \[#6626\](https://github.com/jupyter/notebook/pull/6626) (\[@jtpio\](https://github.com/jtpio))

### Documentation improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id340)

- Remove PDF link to Jupyter Notebook docs \[#6648\](https://github.com/jupyter/notebook/pull/6648) (\[@jtpio\](https://github.com/jtpio))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id341)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2022-11-21&amp;to=2023-01-09&amp;type=c))

\[@blink1073\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ablink1073+updated%3A2022-11-21..2023-01-09&amp;type=Issues) | \[@dependabot\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Adependabot+updated%3A2022-11-21..2023-01-09&amp;type=Issues) | \[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2022-11-21..2023-01-09&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2022-11-21..2023-01-09&amp;type=Issues) | \[@pre-commit-ci\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Apre-commit-ci+updated%3A2022-11-21..2023-01-09&amp;type=Issues) | \[@RRosio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3ARRosio+updated%3A2022-11-21..2023-01-09&amp;type=Issues) | \[@yacchin1205\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ayacchin1205+updated%3A2022-11-21..2023-01-09&amp;type=Issues)

## 7.0.0a9\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#a9)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/v7.0.0a8...b4006ce47bf37b31a7049a77971d7e5db1070660))

### Enhancements made\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id342)

- Update to JupyterLab 4.0.0a31 \[#6627\](https://github.com/jupyter/notebook/pull/6627) (\[@jtpio\](https://github.com/jtpio))

### Bugs fixed\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id343)

- Explicitly specify favicon for /tree view in Notebook \[#6608\](https://github.com/jupyter/notebook/pull/6608) (\[@mcrutch\](https://github.com/mcrutch))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id344)

- Add run-p (npm-run-all) to dev dependencies \[#6629\](https://github.com/jupyter/notebook/pull/6629) (\[@gabalafou\](https://github.com/gabalafou))
- Moves panel related objects to a dedicated module file \[#6625\](https://github.com/jupyter/notebook/pull/6625) (\[@brichet\](https://github.com/brichet))
- Use pathlib instead of os.path.join in \`tests/conftest.py\` \[#6624\](https://github.com/jupyter/notebook/pull/6624) (\[@kianelbo\](https://github.com/kianelbo))
- Bump loader-utils from 1.4.1 to 1.4.2 \[#6623\](https://github.com/jupyter/notebook/pull/6623) (\[@dependabot\](https://github.com/dependabot))
- Bump to Python 3.11 on CI \[#6600\](https://github.com/jupyter/notebook/pull/6600) (\[@jtpio\](https://github.com/jtpio))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id345)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2022-11-11&amp;to=2022-11-21&amp;type=c))

\[@brichet\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Abrichet+updated%3A2022-11-11..2022-11-21&amp;type=Issues) | \[@dependabot\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Adependabot+updated%3A2022-11-11..2022-11-21&amp;type=Issues) | \[@fcollonval\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Afcollonval+updated%3A2022-11-11..2022-11-21&amp;type=Issues) | \[@gabalafou\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agabalafou+updated%3A2022-11-11..2022-11-21&amp;type=Issues) | \[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2022-11-11..2022-11-21&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2022-11-11..2022-11-21&amp;type=Issues) | \[@kianelbo\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akianelbo+updated%3A2022-11-11..2022-11-21&amp;type=Issues) | \[@mcrutch\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Amcrutch+updated%3A2022-11-11..2022-11-21&amp;type=Issues) | \[@pre-commit-ci\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Apre-commit-ci+updated%3A2022-11-11..2022-11-21&amp;type=Issues)

## 7.0.0a8\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#a8)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/v7.0.0a7...9141f3eabb6a10a5bf742b26713405f9768cb6d2))

### Enhancements made\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id346)

- Restyle about dialog \[#6592\](https://github.com/jupyter/notebook/pull/6592) (\[@kostyafarber\](https://github.com/kostyafarber))

### Bugs fixed\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id347)

- Fix async contents handling and add test \[#6616\](https://github.com/jupyter/notebook/pull/6616) (\[@blink1073\](https://github.com/blink1073))
- Fix PDF renderer \[#6584\](https://github.com/jupyter/notebook/pull/6584) (\[@brichet\](https://github.com/brichet))
- Fix HTML viewer \[#6583\](https://github.com/jupyter/notebook/pull/6583) (\[@brichet\](https://github.com/brichet))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id348)

- Bump loader-utils from 1.4.0 to 1.4.1 \[#6615\](https://github.com/jupyter/notebook/pull/6615) (\[@dependabot\](https://github.com/dependabot))
- Bump dessant/lock-threads from 2 to 3 \[#6587\](https://github.com/jupyter/notebook/pull/6587) (\[@dependabot\](https://github.com/dependabot))
- Add dependabot config to update GitHub Actions \[#6586\](https://github.com/jupyter/notebook/pull/6586) (\[@jtpio\](https://github.com/jtpio))
- Update \`actions/checkout\` and \`actions/download-artifact\` \[#6585\](https://github.com/jupyter/notebook/pull/6585) (\[@jtpio\](https://github.com/jtpio))
- Maintenance cleanup \[#6581\](https://github.com/jupyter/notebook/pull/6581) (\[@blink1073\](https://github.com/blink1073))
- Update to lerna 6 \[#6579\](https://github.com/jupyter/notebook/pull/6579) (\[@jtpio\](https://github.com/jtpio))
- Remove the \`nbclassic\` explicit uninstall on Binder \[#6548\](https://github.com/jupyter/notebook/pull/6548) (\[@jtpio\](https://github.com/jtpio))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id349)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2022-10-13&amp;to=2022-11-11&amp;type=c))

\[@blink1073\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ablink1073+updated%3A2022-10-13..2022-11-11&amp;type=Issues) | \[@bnavigator\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Abnavigator+updated%3A2022-10-13..2022-11-11&amp;type=Issues) | \[@brichet\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Abrichet+updated%3A2022-10-13..2022-11-11&amp;type=Issues) | \[@dependabot\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Adependabot+updated%3A2022-10-13..2022-11-11&amp;type=Issues) | \[@echarles\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aecharles+updated%3A2022-10-13..2022-11-11&amp;type=Issues) | \[@fcollonval\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Afcollonval+updated%3A2022-10-13..2022-11-11&amp;type=Issues) | \[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2022-10-13..2022-11-11&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2022-10-13..2022-11-11&amp;type=Issues) | \[@kostyafarber\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akostyafarber+updated%3A2022-10-13..2022-11-11&amp;type=Issues) | \[@pre-commit-ci\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Apre-commit-ci+updated%3A2022-10-13..2022-11-11&amp;type=Issues) | \[@RRosio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3ARRosio+updated%3A2022-10-13..2022-11-11&amp;type=Issues) | \[@venkatasg\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Avenkatasg+updated%3A2022-10-13..2022-11-11&amp;type=Issues)

## 7.0.0a7\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#a7)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/v7.0.0a6...caa0a11e36901c08ae80100fe2bbc5161c47dfee))

### Enhancements made\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id350)

- Fixed user menu alignment \[#6565\](https://github.com/jupyter/notebook/pull/6565) (\[@Mieju\](https://github.com/Mieju))
- Support for Left and Right panels \[#6487\](https://github.com/jupyter/notebook/pull/6487) (\[@brichet\](https://github.com/brichet))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id351)

- Update to JupyterLab 4.0.0a30 \[#6566\](https://github.com/jupyter/notebook/pull/6566) (\[@jtpio\](https://github.com/jtpio))

### Documentation improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id352)

- Fix typo in CHANGELOG.md \[#6561\](https://github.com/jupyter/notebook/pull/6561) (\[@eltociear\](https://github.com/eltociear))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id353)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2022-10-03&amp;to=2022-10-13&amp;type=c))

\[@brichet\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Abrichet+updated%3A2022-10-03..2022-10-13&amp;type=Issues) | \[@eltociear\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aeltociear+updated%3A2022-10-03..2022-10-13&amp;type=Issues) | \[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2022-10-03..2022-10-13&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2022-10-03..2022-10-13&amp;type=Issues) | \[@kevin-bates\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akevin-bates+updated%3A2022-10-03..2022-10-13&amp;type=Issues) | \[@Mieju\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AMieju+updated%3A2022-10-03..2022-10-13&amp;type=Issues) | \[@pre-commit-ci\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Apre-commit-ci+updated%3A2022-10-03..2022-10-13&amp;type=Issues) | \[@RRosio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3ARRosio+updated%3A2022-10-03..2022-10-13&amp;type=Issues)

## 7.0.0a6\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#a6)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/v7.0.0a5...acbec17feca2ae8a0f56c5ec04ba2475a42619ee))

### Enhancements made\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id354)

- Add token on tree widget \[#6496\](https://github.com/jupyter/notebook/pull/6496) (\[@brichet\](https://github.com/brichet))
- Updates README to document maintained versions \[#6480\](https://github.com/jupyter/notebook/pull/6480) (\[@JasonWeill\](https://github.com/JasonWeill))
- Change the tab renderer to allow adding closable tab \[#6477\](https://github.com/jupyter/notebook/pull/6477) (\[@brichet\](https://github.com/brichet))

### Bugs fixed\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id355)

- Fix: No mouse pointer when hovering on the Jupyter icon \[#6550\](https://github.com/jupyter/notebook/pull/6550) (\[@hawkeyes21\](https://github.com/hawkeyes21))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id356)

- Switch to hatch for python version \[#6544\](https://github.com/jupyter/notebook/pull/6544) (\[@blink1073\](https://github.com/blink1073))
- Update to Lumino 2 and JupyterLab 4.0.0a29 \[#6539\](https://github.com/jupyter/notebook/pull/6539) (\[@afshin\](https://github.com/afshin))
- Update lerna version \[#6535\](https://github.com/jupyter/notebook/pull/6535) (\[@blink1073\](https://github.com/blink1073))
- Add task to auto activate the dev environment on Gitpod \[#6527\](https://github.com/jupyter/notebook/pull/6527) (\[@jtpio\](https://github.com/jtpio))
- Troubleshoot failing \`macos\` check on CI \[#6523\](https://github.com/jupyter/notebook/pull/6523) (\[@jtpio\](https://github.com/jtpio))
- Update reference snapshots \[#6520\](https://github.com/jupyter/notebook/pull/6520) (\[@jtpio\](https://github.com/jtpio))
- Add Gitpod files \[#6518\](https://github.com/jupyter/notebook/pull/6518) (\[@jtpio\](https://github.com/jtpio))
- Adding jupyterlab-probot yml file for labeling new issues \[#6506\](https://github.com/jupyter/notebook/pull/6506) (\[@RRosio\](https://github.com/RRosio))
- Uninstall \`nbclassic\` on Binder so Notebook v7 can load \[#6505\](https://github.com/jupyter/notebook/pull/6505) (\[@jtpio\](https://github.com/jtpio))
- Pin \`ypy-websocket\` to \`0.2\` \[#6499\](https://github.com/jupyter/notebook/pull/6499) (\[@jtpio\](https://github.com/jtpio))
- Bump moment from 2.29.3 to 2.29.4 \[#6483\](https://github.com/jupyter/notebook/pull/6483) (\[@dependabot\](https://github.com/dependabot))
- Bump moment from 2.29.2 to 2.29.4 in /ui-tests \[#6482\](https://github.com/jupyter/notebook/pull/6482) (\[@dependabot\](https://github.com/dependabot))
- Bump terser from 5.13.1 to 5.14.2 \[#6481\](https://github.com/jupyter/notebook/pull/6481) (\[@dependabot\](https://github.com/dependabot))
- Bump parse-url from 6.0.0 to 6.0.2 \[#6465\](https://github.com/jupyter/notebook/pull/6465) (\[@dependabot\](https://github.com/dependabot))
- Fix tests \[#6464\](https://github.com/jupyter/notebook/pull/6464) (\[@jtpio\](https://github.com/jtpio))
- Bump jpeg-js from 0.4.3 to 0.4.4 in /ui-tests \[#6455\](https://github.com/jupyter/notebook/pull/6455) (\[@dependabot\](https://github.com/dependabot))

### Documentation improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id357)

- Updates README to document maintained versions \[#6480\](https://github.com/jupyter/notebook/pull/6480) (\[@JasonWeill\](https://github.com/JasonWeill))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id358)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2022-06-14&amp;to=2022-10-03&amp;type=c))

\[@afshin\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aafshin+updated%3A2022-06-14..2022-10-03&amp;type=Issues) | \[@blink1073\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ablink1073+updated%3A2022-06-14..2022-10-03&amp;type=Issues) | \[@brichet\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Abrichet+updated%3A2022-06-14..2022-10-03&amp;type=Issues) | \[@dependabot\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Adependabot+updated%3A2022-06-14..2022-10-03&amp;type=Issues) | \[@echarles\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aecharles+updated%3A2022-06-14..2022-10-03&amp;type=Issues) | \[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2022-06-14..2022-10-03&amp;type=Issues) | \[@hawkeyes21\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ahawkeyes21+updated%3A2022-06-14..2022-10-03&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2022-06-14..2022-10-03&amp;type=Issues) | \[@JasonWeill\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AJasonWeill+updated%3A2022-06-14..2022-10-03&amp;type=Issues) | \[@pre-commit-ci\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Apre-commit-ci+updated%3A2022-06-14..2022-10-03&amp;type=Issues) | \[@RRosio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3ARRosio+updated%3A2022-06-14..2022-10-03&amp;type=Issues)

## 7.0.0a5\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id359)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/v7.0.0a4...614e4780b88f5cf5e2bfda39a55357a0be5ef161))

### Enhancements made\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id360)

- Add shadow to cells \[#6433\](https://github.com/jupyter/notebook/pull/6433) (\[@trungleduc\](https://github.com/trungleduc))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id361)

- Fix docs build \[#6447\](https://github.com/jupyter/notebook/pull/6447) (\[@jtpio\](https://github.com/jtpio))
- \[pre-commit.ci\] pre-commit autoupdate \[#6444\](https://github.com/jupyter/notebook/pull/6444) (\[@pre-commit-ci\](https://github.com/pre-commit-ci))
- \[pre-commit.ci\] pre-commit autoupdate \[#6439\](https://github.com/jupyter/notebook/pull/6439) (\[@pre-commit-ci\](https://github.com/pre-commit-ci))
- \[pre-commit.ci\] pre-commit autoupdate \[#6434\](https://github.com/jupyter/notebook/pull/6434) (\[@pre-commit-ci\](https://github.com/pre-commit-ci))
- Use hatch backend \[#6425\](https://github.com/jupyter/notebook/pull/6425) (\[@blink1073\](https://github.com/blink1073))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id362)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2022-05-20&amp;to=2022-06-14&amp;type=c))

\[@blink1073\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ablink1073+updated%3A2022-05-20..2022-06-14&amp;type=Issues) | \[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2022-05-20..2022-06-14&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2022-05-20..2022-06-14&amp;type=Issues) | \[@ofek\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aofek+updated%3A2022-05-20..2022-06-14&amp;type=Issues) | \[@pre-commit-ci\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Apre-commit-ci+updated%3A2022-05-20..2022-06-14&amp;type=Issues) | \[@trungleduc\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Atrungleduc+updated%3A2022-05-20..2022-06-14&amp;type=Issues)

## 7.0.0a4\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id363)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/v7.0.0a3...4bfaaac148a25ba76fcc7416e3a7b2c714b36fcd))

### Enhancements made\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id364)

- Update to JupyterLab 4.0.0a25 \[#6429\](https://github.com/jupyter/notebook/pull/6429) (\[@jtpio\](https://github.com/jtpio))
- Add cell toolbar extension \[#6418\](https://github.com/jupyter/notebook/pull/6418) (\[@jtpio\](https://github.com/jtpio))
- add the show header command to the command palette \[#6415\](https://github.com/jupyter/notebook/pull/6415) (\[@jeewonkoo\](https://github.com/jeewonkoo))
- Remove the “Appearance” menu entry \[#6412\](https://github.com/jupyter/notebook/pull/6412) (\[@jtpio\](https://github.com/jtpio))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id365)

- \[pre-commit.ci\] pre-commit autoupdate \[#6426\](https://github.com/jupyter/notebook/pull/6426) (\[@pre-commit-ci\](https://github.com/pre-commit-ci))
- Allow bot PRs to be automatically labeled \[#6414\](https://github.com/jupyter/notebook/pull/6414) (\[@blink1073\](https://github.com/blink1073))
- Add Visual Regression Test for the export submenu \[#6383\](https://github.com/jupyter/notebook/pull/6383) (\[@jtpio\](https://github.com/jtpio))
- Fix ESLint config for tests \[#6382\](https://github.com/jupyter/notebook/pull/6382) (\[@jtpio\](https://github.com/jtpio))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id366)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2022-04-27&amp;to=2022-05-20&amp;type=c))

\[@blink1073\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ablink1073+updated%3A2022-04-27..2022-05-20&amp;type=Issues) | \[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2022-04-27..2022-05-20&amp;type=Issues) | \[@jeewonkoo\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajeewonkoo+updated%3A2022-04-27..2022-05-20&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2022-04-27..2022-05-20&amp;type=Issues) | \[@ofek\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aofek+updated%3A2022-04-27..2022-05-20&amp;type=Issues) | \[@pre-commit-ci\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Apre-commit-ci+updated%3A2022-04-27..2022-05-20&amp;type=Issues)

## 7.0.0a3\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id367)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/v7.0.0a2...4076882c0e08875dd719945835f8cbe5b10eac9e))

### Enhancements made\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id368)

- Show file checkboxes by default in the file browser \[#6377\](https://github.com/jupyter/notebook/pull/6377) (\[@jtpio\](https://github.com/jtpio))
- Remove blank space at the bottom of the notebook \[#6376\](https://github.com/jupyter/notebook/pull/6376) (\[@jtpio\](https://github.com/jtpio))
- Add a label to the upload button \[#6374\](https://github.com/jupyter/notebook/pull/6374) (\[@jtpio\](https://github.com/jtpio))
- Update to JupyterLab 4.0.0a24 \[#6371\](https://github.com/jupyter/notebook/pull/6371) (\[@jtpio\](https://github.com/jtpio))
- Initialize handler page\_config from Server traitlets \[#6366\](https://github.com/jupyter/notebook/pull/6366) (\[@bollwyvl\](https://github.com/bollwyvl))
- Add project URLs to setup.cfg \[#6346\](https://github.com/jupyter/notebook/pull/6346) (\[@tlinhart\](https://github.com/tlinhart))
- Update to JupyterLab 4.0.0a23 \[#6336\](https://github.com/jupyter/notebook/pull/6336) (\[@jtpio\](https://github.com/jtpio))

### Bugs fixed\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id369)

- Fix opening JupyterLab from Notebook \[#6379\](https://github.com/jupyter/notebook/pull/6379) (\[@jtpio\](https://github.com/jtpio))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id370)

- Add UI tests for a simple notebook \[#6380\](https://github.com/jupyter/notebook/pull/6380) (\[@jtpio\](https://github.com/jtpio))
- Bump async from 2.6.3 to 2.6.4 in /ui-tests \[#6370\](https://github.com/jupyter/notebook/pull/6370) (\[@dependabot\](https://github.com/dependabot))
- Fix build workflow on CI \[#6369\](https://github.com/jupyter/notebook/pull/6369) (\[@jtpio\](https://github.com/jtpio))
- \[pre-commit.ci\] pre-commit autoupdate \[#6365\](https://github.com/jupyter/notebook/pull/6365) (\[@pre-commit-ci\](https://github.com/pre-commit-ci))
- \[pre-commit.ci\] pre-commit autoupdate \[#6355\](https://github.com/jupyter/notebook/pull/6355) (\[@pre-commit-ci\](https://github.com/pre-commit-ci))
- Bump moment from 2.29.1 to 2.29.2 \[#6352\](https://github.com/jupyter/notebook/pull/6352) (\[@dependabot\](https://github.com/dependabot))
- Bump moment from 2.29.1 to 2.29.2 in /ui-tests \[#6351\](https://github.com/jupyter/notebook/pull/6351) (\[@dependabot\](https://github.com/dependabot))
- Clean up pre-commit \[#6349\](https://github.com/jupyter/notebook/pull/6349) (\[@blink1073\](https://github.com/blink1073))
- Update to TypeScript 4.6 \[#6345\](https://github.com/jupyter/notebook/pull/6345) (\[@jtpio\](https://github.com/jtpio))
- \[pre-commit.ci\] pre-commit autoupdate \[#6343\](https://github.com/jupyter/notebook/pull/6343) (\[@pre-commit-ci\](https://github.com/pre-commit-ci))
- Add pytest and handle warnings \[#6338\](https://github.com/jupyter/notebook/pull/6338) (\[@blink1073\](https://github.com/blink1073))
- Add flake8 and git-blame-ignore-revs \[#6337\](https://github.com/jupyter/notebook/pull/6337) (\[@blink1073\](https://github.com/blink1073))
- Run Autoformatters \[#6335\](https://github.com/jupyter/notebook/pull/6335) (\[@blink1073\](https://github.com/blink1073))
- Bump minimist from 1.2.5 to 1.2.6 \[#6334\](https://github.com/jupyter/notebook/pull/6334) (\[@dependabot\](https://github.com/dependabot))
- Bump minimist from 1.2.5 to 1.2.6 in /ui-tests \[#6333\](https://github.com/jupyter/notebook/pull/6333) (\[@dependabot\](https://github.com/dependabot))
- Bump ansi-regex from 3.0.0 to 3.0.1 in /ui-tests \[#6332\](https://github.com/jupyter/notebook/pull/6332) (\[@dependabot\](https://github.com/dependabot))
- Adopt pre-commit \[#6331\](https://github.com/jupyter/notebook/pull/6331) (\[@blink1073\](https://github.com/blink1073))

### Documentation improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id371)

- Link to v6 plan in the README \[#6375\](https://github.com/jupyter/notebook/pull/6375) (\[@echarles\](https://github.com/echarles))
- Copy edits in config, edits bug report template \[#6364\](https://github.com/jupyter/notebook/pull/6364) (\[@JasonWeill\](https://github.com/JasonWeill))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id372)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2022-03-21&amp;to=2022-04-27&amp;type=c))

\[@blink1073\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ablink1073+updated%3A2022-03-21..2022-04-27&amp;type=Issues) | \[@bollwyvl\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Abollwyvl+updated%3A2022-03-21..2022-04-27&amp;type=Issues) | \[@dependabot\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Adependabot+updated%3A2022-03-21..2022-04-27&amp;type=Issues) | \[@echarles\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aecharles+updated%3A2022-03-21..2022-04-27&amp;type=Issues) | \[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2022-03-21..2022-04-27&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2022-03-21..2022-04-27&amp;type=Issues) | \[@JasonWeill\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AJasonWeill+updated%3A2022-03-21..2022-04-27&amp;type=Issues) | \[@pre-commit-ci\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Apre-commit-ci+updated%3A2022-03-21..2022-04-27&amp;type=Issues) | \[@tlinhart\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Atlinhart+updated%3A2022-03-21..2022-04-27&amp;type=Issues)

## 7.0.0a2\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id373)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/v7.0.0a1...9be03f5f27232d50b16dbbaa50a222260166694c))

### Enhancements made\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id374)

- Add support for opening a document with a different factory \[#6315\](https://github.com/jupyter/notebook/pull/6315) (\[@jtpio\](https://github.com/jtpio))
- Minor copy edit in README \[#6313\](https://github.com/jupyter/notebook/pull/6313) (\[@JasonWeill\](https://github.com/JasonWeill))

### Bugs fixed\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id375)

- Fix rendering of markdown \[#6318\](https://github.com/jupyter/notebook/pull/6318) (\[@jtpio\](https://github.com/jtpio))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id376)

- Update to JupyterLab 4.0.0a22 \[#6314\](https://github.com/jupyter/notebook/pull/6314) (\[@jtpio\](https://github.com/jtpio))

### Documentation improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id377)

- docs: fix spelling \[#6317\](https://github.com/jupyter/notebook/pull/6317) (\[@dijonkitchen\](https://github.com/dijonkitchen))
- Minor copy edit in README \[#6313\](https://github.com/jupyter/notebook/pull/6313) (\[@JasonWeill\](https://github.com/JasonWeill))
- Update example notebook on Binder \[#6306\](https://github.com/jupyter/notebook/pull/6306) (\[@jtpio\](https://github.com/jtpio))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id378)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2022-03-09&amp;to=2022-03-21&amp;type=c))

\[@dijonkitchen\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Adijonkitchen+updated%3A2022-03-09..2022-03-21&amp;type=Issues) | \[@fcollonval\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Afcollonval+updated%3A2022-03-09..2022-03-21&amp;type=Issues) | \[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2022-03-09..2022-03-21&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2022-03-09..2022-03-21&amp;type=Issues) | \[@JasonWeill\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AJasonWeill+updated%3A2022-03-09..2022-03-21&amp;type=Issues)

## 7.0.0a1\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id379)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/v6.4.8...22fe46f3e806aa346625f6ef2f2a024d030a068d))

### Enhancements made\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id380)

- Notebook v7 scaffolding \[#6294\](https://github.com/jupyter/notebook/pull/6294) (\[@jtpio\](https://github.com/jtpio))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id381)

- Clean up CI \[#6304\](https://github.com/jupyter/notebook/pull/6304) (\[@blink1073\](https://github.com/blink1073))
- Remove the custom run keyboard shortcut \[#6303\](https://github.com/jupyter/notebook/pull/6303) (\[@jtpio\](https://github.com/jtpio))
- Bump nanoid from 3.1.30 to 3.3.1 in /ui-tests \[#6302\](https://github.com/jupyter/notebook/pull/6302) (\[@dependabot\](https://github.com/dependabot))
- Bump simple-get from 3.1.0 to 3.1.1 in /ui-tests \[#6301\](https://github.com/jupyter/notebook/pull/6301) (\[@dependabot\](https://github.com/dependabot))
- Bump url-parse from 1.5.4 to 1.5.10 in /ui-tests \[#6300\](https://github.com/jupyter/notebook/pull/6300) (\[@dependabot\](https://github.com/dependabot))
- Bump node-fetch from 2.6.6 to 2.6.7 in /ui-tests \[#6299\](https://github.com/jupyter/notebook/pull/6299) (\[@dependabot\](https://github.com/dependabot))
- Bump follow-redirects from 1.14.5 to 1.14.9 in /ui-tests \[#6298\](https://github.com/jupyter/notebook/pull/6298) (\[@dependabot\](https://github.com/dependabot))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id382)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2022-01-25&amp;to=2022-03-09&amp;type=c))

\[@blink1073\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ablink1073+updated%3A2022-01-25..2022-03-09&amp;type=Issues) | \[@dependabot\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Adependabot+updated%3A2022-01-25..2022-03-09&amp;type=Issues) | \[@github-actions\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agithub-actions+updated%3A2022-01-25..2022-03-09&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2022-01-25..2022-03-09&amp;type=Issues) | \[@kevin-bates\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akevin-bates+updated%3A2022-01-25..2022-03-09&amp;type=Issues) | \[@Zsailer\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AZsailer+updated%3A2022-01-25..2022-03-09&amp;type=Issues)

## 6.4.8\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id383)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/v6.4.7...479902d83a691253e0cff8439a33577e82408317))

### Bugs fixed\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id384)

- Fix to remove potential memory leak on Jupyter Notebooks ZMQChannelHandler code \[#6251\](https://github.com/jupyter/notebook/pull/6251) (\[@Vishwajeet0510\](https://github.com/Vishwajeet0510))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id385)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2022-01-12&amp;to=2022-01-25&amp;type=c))

\[@Vishwajeet0510\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AVishwajeet0510+updated%3A2022-01-12..2022-01-25&amp;type=Issues)

## 6.4.7\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id386)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/v6.4.6...b77b5e38b8fa1a20150d7fa4d735dbf1c4f00418))

### Bugs fixed\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id387)

- Fix Chinese punctuation \[#6268\](https://github.com/jupyter/notebook/pull/6268) (\[@LiHua-Official\](https://github.com/LiHua-Official))
- Add date field to kernel message header \[#6265\](https://github.com/jupyter/notebook/pull/6265) (\[@kevin-bates\](https://github.com/kevin-bates))
- Fix deprecation warning \[#6253\](https://github.com/jupyter/notebook/pull/6253) (\[@tornaria\](https://github.com/tornaria))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id388)

- Enforce labels on PRs \[#6235\](https://github.com/jupyter/notebook/pull/6235) (\[@blink1073\](https://github.com/blink1073))
- Fix: CI error for python 3.6 & macOS \[#6215\](https://github.com/jupyter/notebook/pull/6215) (\[@penguinolog\](https://github.com/penguinolog))

### Other merged PRs\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id389)

- handle KeyError when get session \[#6245\](https://github.com/jupyter/notebook/pull/6245) (\[@ccw630\](https://github.com/ccw630))
- Updated doc for passwd \[#6209\](https://github.com/jupyter/notebook/pull/6209) (\[@antoinecarme\](https://github.com/antoinecarme))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id390)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2021-11-16&amp;to=2022-01-12&amp;type=c))

\[@antoinecarme\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aantoinecarme+updated%3A2021-11-16..2022-01-12&amp;type=Issues) | \[@blink1073\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ablink1073+updated%3A2021-11-16..2022-01-12&amp;type=Issues) | \[@ccw630\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Accw630+updated%3A2021-11-16..2022-01-12&amp;type=Issues) | \[@kevin-bates\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akevin-bates+updated%3A2021-11-16..2022-01-12&amp;type=Issues) | \[@LiHua-Official\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3ALiHua-Official+updated%3A2021-11-16..2022-01-12&amp;type=Issues) | \[@penguinolog\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Apenguinolog+updated%3A2021-11-16..2022-01-12&amp;type=Issues) | \[@tornaria\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Atornaria+updated%3A2021-11-16..2022-01-12&amp;type=Issues)

## 6.4.6\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id391)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/v6.4.5...160c27d3c23dafe8b42240571db21b0d5cbae2fe))

### Bugs fixed\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id392)

- Fix \`asyncio\` error when opening notebooks \[#6221\](https://github.com/jupyter/notebook/pull/6221) (\[@dleen\](https://github.com/dleen))
- Change to use a universal Chinese translation on certain words \[#6218\](https://github.com/jupyter/notebook/pull/6218) (\[@jackexu\](https://github.com/jackexu))
- Fix Chinese translation typo \[#6211\](https://github.com/jupyter/notebook/pull/6211) (\[@maliubiao\](https://github.com/maliubiao)
- Fix \`send2trash\` tests failing on Windows \[#6127\](https://github.com/jupyter/notebook/pull/6127) (\[@dolfinus\](https://github.com/dolfinus))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id393)

- TST: don't look in user site for serverextensions \[#6233\](https://github.com/jupyter/notebook/pull/6233) (\[@bnavigator\](https://github.com/bnavigator))
- Enable terminal tests as \`pywinpty\` is ported for python 3.9 \[#6228\](https://github.com/jupyter/notebook/pull/6228) ( \`@nsait-linaro\` )

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id394)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2021-10-19&amp;to=2021-11-16&amp;type=c))

\[@bnavigator\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Abnavigator+updated%3A2021-10-19..2021-11-16&amp;type=Issues) | \[@dleen\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Adleen+updated%3A2021-10-19..2021-11-16&amp;type=Issues) | \[@dolfinus\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Adolfinus+updated%3A2021-10-19..2021-11-16&amp;type=Issues) | \[@jackexu\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajackexu+updated%3A2021-10-19..2021-11-16&amp;type=Issues) | \[@kevin-bates\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akevin-bates+updated%3A2021-10-19..2021-11-16&amp;type=Issues) | \[@maliubiao\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Amaliubiao+updated%3A2021-10-19..2021-11-16&amp;type=Issues) | \`@nsait-linaro\` | \[@takluyver\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Atakluyver+updated%3A2021-10-19..2021-11-16&amp;type=Issues) | \[@Zsailer\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AZsailer+updated%3A2021-10-19..2021-11-16&amp;type=Issues)

## 6.4.5\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id395)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/v6.4.4...ccd9665571107e02a325a738b8baebd6532b2d3d))

### Bug fixes\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#bug-fixes)

- Recover from failure to render mimetype \[#6181\](https://github.com/jupyter/notebook/pull/6181) (\[@martinRenou\](https://github.com/martinRenou))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id396)

- Fix crypto handling \[#6197\](https://github.com/jupyter/notebook/pull/6197) (\[@blink1073\](https://github.com/blink1073))
- Fix \`jupyter\_client\` warning \[#6178\](https://github.com/jupyter/notebook/pull/6178) (\[@martinRenou\](https://github.com/martinRenou))

### Documentation improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id397)

- Fix nbsphinx settings \[#6200\](https://github.com/jupyter/notebook/pull/6200) (\[@mgeier\](https://github.com/mgeier))
- Fully revert the pinning of \`nbsphinx\` to 0.8.6 \[#6201\](https://github.com/jupyter/notebook/pull/6201) (\[@kevin-bates\](https://github.com/kevin-bates))
- Pin \`nbsphinx\` to 0.8.6, clean up orphaned resources \[#6194\](https://github.com/jupyter/notebook/pull/6194) (\[@kevin-bates\](https://github.com/kevin-bates))
- Fix typo in docstring \[#6188\](https://github.com/jupyter/notebook/pull/6188) (\[@jgarte\](https://github.com/jgarte))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id398)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2021-09-03&amp;to=2021-10-19&amp;type=c))

\[@blink1073\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ablink1073+updated%3A2021-09-03..2021-10-19&amp;type=Issues) | \[@jgarte\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajgarte+updated%3A2021-09-03..2021-10-19&amp;type=Issues) | \[@kevin-bates\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akevin-bates+updated%3A2021-09-03..2021-10-19&amp;type=Issues) | \[@martinRenou\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AmartinRenou+updated%3A2021-09-03..2021-10-19&amp;type=Issues) | \[@mgeier\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Amgeier+updated%3A2021-09-03..2021-10-19&amp;type=Issues)

## 6.4.4\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id399)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/v6.4.3...c06c340574e1d2207940c5bd1190eb73d82ab945))

### Documentation improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id400)

- Update Manual Release Instructions \[#6152\](https://github.com/jupyter/notebook/pull/6152) (\[@blink1073\](https://github.com/blink1073))

### Other merged PRs\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id401)

- Use default JupyterLab CSS sanitizer options for Markdown \[#6160\](https://github.com/jupyter/notebook/pull/6160) (\[@krassowski\](https://github.com/krassowski))
- Fix syntax highlight \[#6128\](https://github.com/jupyter/notebook/pull/6128) (\[@massongit\](https://github.com/massongit))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id402)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2021-08-11&amp;to=2021-09-03&amp;type=c))

\[@blink1073\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ablink1073+updated%3A2021-08-11..2021-09-03&amp;type=Issues) | \[@kevin-bates\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akevin-bates+updated%3A2021-08-11..2021-09-03&amp;type=Issues) | \[@krassowski\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akrassowski+updated%3A2021-08-11..2021-09-03&amp;type=Issues) | \[@massongit\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Amassongit+updated%3A2021-08-11..2021-09-03&amp;type=Issues) | \[@minrk\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aminrk+updated%3A2021-08-11..2021-09-03&amp;type=Issues) | \[@Zsailer\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AZsailer+updated%3A2021-08-11..2021-09-03&amp;type=Issues)

## 6.4.3\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id403)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/v6.4.2...c373bd89adaaddffbb71747ebbcfe8a749cae0a8))

### Bugs fixed\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id404)

- Add @babel/core dependency \[#6133\](https://github.com/jupyter/notebook/pull/6133) (\[@afshin\](https://github.com/afshin))
- Switch webpack to production mode \[#6131\](https://github.com/jupyter/notebook/pull/6131) (\[@afshin\](https://github.com/afshin))

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id405)

- Clean up link checking \[#6130\](https://github.com/jupyter/notebook/pull/6130) (\[@blink1073\](https://github.com/blink1073))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id406)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2021-08-06&amp;to=2021-08-10&amp;type=c))

\[@afshin\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aafshin+updated%3A2021-08-06..2021-08-10&amp;type=Issues) | \[@blink1073\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ablink1073+updated%3A2021-08-06..2021-08-10&amp;type=Issues) | \[@Zsailer\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AZsailer+updated%3A2021-08-06..2021-08-10&amp;type=Issues)

## 6.4.2\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id407)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/v6.4.0...999e8322bcd24e0ed62b180c19ec13db3f48165b))

### Bugs fixed\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id408)

- Add missing file to manifest \[#6122\](https://github.com/jupyter/notebook/pull/6122) (\[@afshin\](https://github.com/afshin))
- Fix issue #3218 \[#6108\](https://github.com/jupyter/notebook/pull/6108) (\[@Nazeeh21\](https://github.com/Nazeeh21))
- Fix version of jupyter-packaging in pyproject.toml \[#6101\](https://github.com/jupyter/notebook/pull/6101) (\[@frenzymadness\](https://github.com/frenzymadness))
- “#element”.tooltip is not a function on home page fixed. \[#6070\](https://github.com/jupyter/notebook/pull/6070) @ilayh123

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id409)

- Enhancements to the desktop entry \[#6099\](https://github.com/jupyter/notebook/pull/6099) (\[@Amr-Ibra\](https://github.com/Amr-Ibra))
- Add missing spaces to help messages in config file \[#6085\](https://github.com/jupyter/notebook/pull/6085) (\[@saiwing-yeung\](https://github.com/saiwing-yeung))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id410)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2021-05-17&amp;to=2021-08-06&amp;type=c))

\[@afshin\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aafshin+updated%3A2021-05-17..2021-08-06&amp;type=Issues) | \[@Amr-Ibra\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AAmr-Ibra+updated%3A2021-05-17..2021-08-06&amp;type=Issues) | \[@frenzymadness\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Afrenzymadness+updated%3A2021-05-17..2021-08-06&amp;type=Issues) | \[@ilayh123\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ailayh123+updated%3A2021-05-17..2021-08-06&amp;type=Issues) | \[@kevin-bates\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akevin-bates+updated%3A2021-05-17..2021-08-06&amp;type=Issues) | \[@Nazeeh21\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3ANazeeh21+updated%3A2021-05-17..2021-08-06&amp;type=Issues) | \[@saiwing-yeung\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Asaiwing-yeung+updated%3A2021-05-17..2021-08-06&amp;type=Issues)

## 6.4.0\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id411)

( \[Full Changelog\](https://github.com/jupyter/notebook/compare/6.3.0...80eb286f316838afc76a9a84b06f54e7dccb6c86))

### Bugs fixed\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id412)

- Fix Handling of Encoded Paths in Save As Dialog \[#6030\](https://github.com/jupyter/notebook/pull/6030) (\[@afshin\](https://github.com/afshin))
- Fix: split\_cell doesn't always split cell \[#6017\](https://github.com/jupyter/notebook/pull/6017) (\[@gamestrRUS\](https://github.com/gamestrRUS))
- Correct 'Content-Type' headers \[#6026\](https://github.com/jupyter/notebook/pull/6026) (\[@faucct\](https://github.com/faucct))
- Fix skipped tests & remove deprecation warnings \[#6018\](https://github.com/jupyter/notebook/pull/6018) (\[@befeleme\](https://github.com/befeleme))
- \[Gateway\] Track only this server's kernels \[#5980\](https://github.com/jupyter/notebook/pull/5980) (\[@kevin-bates\](https://github.com/kevin-bates))
- Bind the HTTPServer in start \[#6061\](https://github.com/jupyter/notebook/pull/6061)

### Maintenance and upkeep improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id413)

- Revert “do not apply asyncio patch for tornado >=6.1” \[#6052\](https://github.com/jupyter/notebook/pull/6052) (\[@minrk\](https://github.com/minrk))
- Use Jupyter Releaser \[#6048\](https://github.com/jupyter/notebook/pull/6048) (\[@afshin\](https://github.com/afshin))
- Add Workflow Permissions for Lock Bot \[#6042\](https://github.com/jupyter/notebook/pull/6042) (\[@jtpio\](https://github.com/jtpio))
- Fixes related to the recent changes in the documentation \[#6021\](https://github.com/jupyter/notebook/pull/6021) (\[@frenzymadness\](https://github.com/frenzymadness))
- Add maths checks in CSS reference test \[#6035\](https://github.com/jupyter/notebook/pull/6035) (\[@stef4k\](https://github.com/stef4k))
- Add Issue Lock and Answered Bots \[#6019\](https://github.com/jupyter/notebook/pull/6019) (\[@afshin\](https://github.com/afshin))

### Documentation improvements\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id414)

- Spelling correction \[#6045\](https://github.com/jupyter/notebook/pull/6045) (\[@wggillen\](https://github.com/wggillen))
- Minor typographical and comment changes \[#6025\](https://github.com/jupyter/notebook/pull/6025) (\[@misterhay\](https://github.com/misterhay))
- Fixes related to the recent changes in the documentation \[#6021\](https://github.com/jupyter/notebook/pull/6021) (\[@frenzymadness\](https://github.com/frenzymadness))
- Fix readthedocs environment \[#6020\](https://github.com/jupyter/notebook/pull/6020) (\[@blink1073\](https://github.com/blink1073))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id415)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2021-03-22&amp;to=2021-05-12&amp;type=c))

\[@afshin\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aafshin+updated%3A2021-03-22..2021-05-12&amp;type=Issues) | \[@befeleme\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Abefeleme+updated%3A2021-03-22..2021-05-12&amp;type=Issues) | \[@blink1073\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ablink1073+updated%3A2021-03-22..2021-05-12&amp;type=Issues) | \[@faucct\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Afaucct+updated%3A2021-03-22..2021-05-12&amp;type=Issues) | \[@frenzymadness\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Afrenzymadness+updated%3A2021-03-22..2021-05-12&amp;type=Issues) | \[@gamestrRUS\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AgamestrRUS+updated%3A2021-03-22..2021-05-12&amp;type=Issues) | \[@jtpio\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajtpio+updated%3A2021-03-22..2021-05-12&amp;type=Issues) | \[@kevin-bates\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akevin-bates+updated%3A2021-03-22..2021-05-12&amp;type=Issues) | \[@minrk\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aminrk+updated%3A2021-03-22..2021-05-12&amp;type=Issues) | \[@misterhay\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Amisterhay+updated%3A2021-03-22..2021-05-12&amp;type=Issues) | \[@stef4k\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Astef4k+updated%3A2021-03-22..2021-05-12&amp;type=Issues) | \[@wggillen\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Awggillen+updated%3A2021-03-22..2021-05-12&amp;type=Issues)

## 6.3.0\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id416)

### Merged PRs\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#merged-prs)

- Add square logo and desktop entry files \[#6010\](https://github.com/jupyter/notebook/pull/6010) (\[@befeleme\](https://github.com/befeleme))
- Modernize Changelog \[#6008\](https://github.com/jupyter/notebook/pull/6008) (\[@afshin\](https://github.com/afshin))
- Add missing “import inspect” \[#5999\](https://github.com/jupyter/notebook/pull/5999) (\[@mgeier\](https://github.com/mgeier))
- Add Codecov badge to README \[#5989\](https://github.com/jupyter/notebook/pull/5989) (\[@thomasrockhu\](https://github.com/thomasrockhu))
- Remove configuration for nosetests from setup.cfg \[#5986\](https://github.com/jupyter/notebook/pull/5986) (\[@frenzymadness\](https://github.com/frenzymadness))
- Update security.rst \[#5978\](https://github.com/jupyter/notebook/pull/5978) (\[@dlrice\](https://github.com/dlrice))
- Docs-Translations: Updated Hindi and Chinese Readme.md \[#5976\](https://github.com/jupyter/notebook/pull/5976) (\[@rjn01\](https://github.com/rjn01))
- Allow /metrics by default if auth is off \[#5974\](https://github.com/jupyter/notebook/pull/5974) (\[@blairdrummond\](https://github.com/blairdrummond))
- Skip terminal tests on Windows 3.9+ (temporary) \[#5968\](https://github.com/jupyter/notebook/pull/5968) (\[@kevin-bates\](https://github.com/kevin-bates))
- Update GatewayKernelManager to derive from AsyncMappingKernelManager \[#5966\](https://github.com/jupyter/notebook/pull/5966) (\[@kevin-bates\](https://github.com/kevin-bates))
- Drop use of deprecated pyzmq.ioloop \[#5965\](https://github.com/jupyter/notebook/pull/5965) (\[@kevin-bates\](https://github.com/kevin-bates))
- Drop support for Python 3.5 \[#5962\](https://github.com/jupyter/notebook/pull/5962) (\[@kevin-bates\](https://github.com/kevin-bates))
- Allow jupyter\_server-based contents managers in notebook \[#5957\](https://github.com/jupyter/notebook/pull/5957) (\[@afshin\](https://github.com/afshin))
- Russian translation fixes \[#5954\](https://github.com/jupyter/notebook/pull/5954) (\[@insolor\](https://github.com/insolor))
- Increase culling test idle timeout \[#5952\](https://github.com/jupyter/notebook/pull/5952) (\[@kevin-bates\](https://github.com/kevin-bates))
- Re-enable support for answer\_yes flag \[#5941\](https://github.com/jupyter/notebook/pull/5941) (\[@afshin\](https://github.com/afshin))
- Replace Travis and Appveyor with Github Actions \[#5938\](https://github.com/jupyter/notebook/pull/5938) (\[@kevin-bates\](https://github.com/kevin-bates))
- DOC: Server extension, extra docs on configuration/authentication. \[#5937\](https://github.com/jupyter/notebook/pull/5937) (\[@Carreau\](https://github.com/Carreau))

### Contributors to this release\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id417)

( \[GitHub contributors page for this release\](https://github.com/jupyter/notebook/graphs/contributors?from=2021-01-13&amp;to=2021-03-18&amp;type=c))

\[@abielhammonds\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aabielhammonds+updated%3A2021-01-13..2021-03-18&amp;type=Issues) | \[@afshin\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aafshin+updated%3A2021-01-13..2021-03-18&amp;type=Issues) | \[@ajharry\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aajharry+updated%3A2021-01-13..2021-03-18&amp;type=Issues) | \[@Alokrar\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AAlokrar+updated%3A2021-01-13..2021-03-18&amp;type=Issues) | \[@befeleme\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Abefeleme+updated%3A2021-01-13..2021-03-18&amp;type=Issues) | \[@blairdrummond\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ablairdrummond+updated%3A2021-01-13..2021-03-18&amp;type=Issues) | \[@blink1073\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ablink1073+updated%3A2021-01-13..2021-03-18&amp;type=Issues) | \[@bollwyvl\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Abollwyvl+updated%3A2021-01-13..2021-03-18&amp;type=Issues) | \[@Carreau\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3ACarreau+updated%3A2021-01-13..2021-03-18&amp;type=Issues) | \[@ChenChenDS\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AChenChenDS+updated%3A2021-01-13..2021-03-18&amp;type=Issues) | \[@cosmoscalibur\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Acosmoscalibur+updated%3A2021-01-13..2021-03-18&amp;type=Issues) | \[@dlrice\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Adlrice+updated%3A2021-01-13..2021-03-18&amp;type=Issues) | \[@dwanneruchi\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Adwanneruchi+updated%3A2021-01-13..2021-03-18&amp;type=Issues) | \[@ElisonSherton\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AElisonSherton+updated%3A2021-01-13..2021-03-18&amp;type=Issues) | \[@FazeelUsmani\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AFazeelUsmani+updated%3A2021-01-13..2021-03-18&amp;type=Issues) | \[@frenzymadness\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Afrenzymadness+updated%3A2021-01-13..2021-03-18&amp;type=Issues) | \[@goerz\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Agoerz+updated%3A2021-01-13..2021-03-18&amp;type=Issues) | \[@insolor\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ainsolor+updated%3A2021-01-13..2021-03-18&amp;type=Issues) | \[@jasongrout\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ajasongrout+updated%3A2021-01-13..2021-03-18&amp;type=Issues) | \[@JianghuiDu\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AJianghuiDu+updated%3A2021-01-13..2021-03-18&amp;type=Issues) | \[@JuzerShakir\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AJuzerShakir+updated%3A2021-01-13..2021-03-18&amp;type=Issues) | \[@kevin-bates\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Akevin-bates+updated%3A2021-01-13..2021-03-18&amp;type=Issues) | \[@Khalilsqu\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AKhalilsqu+updated%3A2021-01-13..2021-03-18&amp;type=Issues) | \[@meeseeksdev\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ameeseeksdev+updated%3A2021-01-13..2021-03-18&amp;type=Issues) | \[@mgeier\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Amgeier+updated%3A2021-01-13..2021-03-18&amp;type=Issues) | \[@michaelpedota\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Amichaelpedota+updated%3A2021-01-13..2021-03-18&amp;type=Issues) | \[@mjbright\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Amjbright+updated%3A2021-01-13..2021-03-18&amp;type=Issues) | \[@MSeal\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AMSeal+updated%3A2021-01-13..2021-03-18&amp;type=Issues) | \[@ncoughlin\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ancoughlin+updated%3A2021-01-13..2021-03-18&amp;type=Issues) | \[@NTimmons\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3ANTimmons+updated%3A2021-01-13..2021-03-18&amp;type=Issues) | \[@ProsperousHeart\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AProsperousHeart+updated%3A2021-01-13..2021-03-18&amp;type=Issues) | \[@rjn01\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Arjn01+updated%3A2021-01-13..2021-03-18&amp;type=Issues) | \[@slw07g\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Aslw07g+updated%3A2021-01-13..2021-03-18&amp;type=Issues) | \[@stenivan\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Astenivan+updated%3A2021-01-13..2021-03-18&amp;type=Issues) | \[@takluyver\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Atakluyver+updated%3A2021-01-13..2021-03-18&amp;type=Issues) | \[@thomasrockhu\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Athomasrockhu+updated%3A2021-01-13..2021-03-18&amp;type=Issues) | \[@wgilpin\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Awgilpin+updated%3A2021-01-13..2021-03-18&amp;type=Issues) | \[@wxtt522\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Awxtt522+updated%3A2021-01-13..2021-03-18&amp;type=Issues) | \[@yuvipanda\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3Ayuvipanda+updated%3A2021-01-13..2021-03-18&amp;type=Issues) | \[@Zsailer\](https://github.com/search?q=repo%3Ajupyter%2Fnotebook+involves%3AZsailer+updated%3A2021-01-13..2021-03-18&amp;type=Issues)

## 6.2.0\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id418)

## Merged PRs\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id419)

- Increase minimum tornado version ( \[5933\](https://github.com/jupyter/notebook/pull/5933))
- Adjust skip decorators to avoid remaining dependency on nose ( \[5932\](https://github.com/jupyter/notebook/pull/5932))
- Ensure that cell ids persist after save ( \[5928\](https://github.com/jupyter/notebook/pull/5928))
- Add reconnection to Gateway (form nb2kg) ( \[5924\](https://github.com/jupyter/notebook/pull/5924))
- Fix some typos ( \[5917\](https://github.com/jupyter/notebook/pull/5917))
- Handle TrashPermissionError, now that it exist ( \[5894\](https://github.com/jupyter/notebook/pull/5894))

Thank you to all the contributors:

- @kevin-bates
- @mishaschwartz
- @oyvsyo
- @user202729
- @stefanor

## 6.1.6\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id420)

## Merged PRs\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id421)

- do not require nose for testing ( \[5826\](https://github.com/jupyter/notebook/pull/5826))
- \[docs\] Update Chinese and Hindi readme.md ( \[5823\](https://github.com/jupyter/notebook/pull/5823))
- Add support for creating terminals via GET ( \[5813\](https://github.com/jupyter/notebook/pull/5813))
- Made doc translations in Hindi and Chinese ( \[5787\](https://github.com/jupyter/notebook/pull/5787))

Thank you to all the contributors:

- @pgajdos
- @rjn01
- @kevin-bates
- @virejdasani

## 6.1.5\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id422)

6.1.5 is a security release, fixing one vulnerability:

- Fix open redirect vulnerability GHSA-c7vm-f5p4-8fqh (CVE to be assigned)

## 6.1.4\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id423)

- Fix broken links to jupyter documentation ( \[5686\](https://github.com/jupyter/notebook/pull/5686))
- Add additional entries to troubleshooting section ( \[5695\](https://github.com/jupyter/notebook/pull/5695))
- Revert change in page alignment ( \[5703\](https://github.com/jupyter/notebook/pull/5703))
- Bug fix: remove double encoding in download files ( \[5720\](https://github.com/jupyter/notebook/pull/5720))
- Fix typo for Check in zh\_CN ( \[5730\](https://github.com/jupyter/notebook/pull/5730))
- Require a file name in the “Save As” dialog ( \[5733\](https://github.com/jupyter/notebook/pull/5733))

Thank you to all the contributors:

- bdbai
- Jaipreet Singh
- Kevin Bates
- Pavel Panchekha
- Zach Sailer

## 6.1.3\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id424)

- Title new buttons with label if action undefined ( \[5676\](https://github.com/jupyter/notebook/pull/5676))

Thank you to all the contributors:

- Kyle Kelley

## 6.1.2\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id425)

- Fix russian message format for delete/duplicate actions ( \[5662\](https://github.com/jupyter/notebook/pull/5662))
- Remove unnecessary import of bind\_unix\_socket ( \[5666\](https://github.com/jupyter/notebook/pull/5666))
- Tooltip style scope fix ( \[5672\](https://github.com/jupyter/notebook/pull/5672))

Thank you to all the contributors:

- Dmitry Akatov
- Kevin Bates
- Magda Stenius

## 6.1.1\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id426)

- Prevent inclusion of requests\_unixsocket on Windows ( \[5650\](https://github.com/jupyter/notebook/pull/5650))

Thank you to all the contributors:

- Kevin Bates

## 6.1.0\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id427)

Please note that this repository is currently maintained by a skeleton crew of maintainers from the Jupyter community. For our approach moving forward, please see this \[notice\](https://github.com/jupyter/notebook#notice) from the README. Thank you.

Here is an enumeration of changes made since the last release and included in 6.1.0.

- Remove deprecated encoding parameter for Python 3.9 compatibility. ( \[5174\](https://github.com/jupyter/notebook/pull/5174))
- Add support for async kernel management ( \[4479\](https://github.com/jupyter/notebook/pull/4479))
- Fix typo in password\_required help message ( \[5320\](https://github.com/jupyter/notebook/pull/5320))
- Gateway only: Ensure launch and request timeouts are in sync ( \[5317\](https://github.com/jupyter/notebook/pull/5317))
- Update Markdown Cells example to HTML5 video tag ( \[5411\](https://github.com/jupyter/notebook/pull/5411))
- Integrated LoginWidget into edit to enable users to logout from the t… ( \[5406\](https://github.com/jupyter/notebook/pull/5406))
- Update message about minimum Tornado version ( \[5222\](https://github.com/jupyter/notebook/pull/5222))
- Logged notebook type ( \[5425\](https://github.com/jupyter/notebook/pull/5425))
- Added nl language ( \[5354\](https://github.com/jupyter/notebook/pull/5354))
- Add UNIX socket support to notebook server. ( \[4835\](https://github.com/jupyter/notebook/pull/4835))
- Update CodeMirror dependency ( \[5198\](https://github.com/jupyter/notebook/pull/5198))
- Tree added download multiple files ( \[5351\](https://github.com/jupyter/notebook/pull/5351))
- Toolbar buttons tooltip: show help instead of label ( \[5107\](https://github.com/jupyter/notebook/pull/5107))
- Remove unnecessary import of requests\_unixsocket ( \[5451\](https://github.com/jupyter/notebook/pull/5451))
- Add ability to cull terminals and track last activity ( \[5372\](https://github.com/jupyter/notebook/pull/5372))
- Code refactoring notebook.js ( \[5352\](https://github.com/jupyter/notebook/pull/5352))
- Install terminado for docs build ( \[5462\](https://github.com/jupyter/notebook/pull/5462))
- Convert notifications JS test to selenium ( \[5455\](https://github.com/jupyter/notebook/pull/5455))
- Add cell attachments to markdown example ( \[5412\](https://github.com/jupyter/notebook/pull/5412))
- Add Japanese document ( \[5231\](https://github.com/jupyter/notebook/pull/5231))
- Migrate Move multiselection test to selenium ( \[5158\](https://github.com/jupyter/notebook/pull/5158))
- Use \`cmdtrl-enter\` to run a cell ( \[5120\](https://github.com/jupyter/notebook/pull/5120))
- Fix broken “Raw cell MIME type” dialog ( \[5385\](https://github.com/jupyter/notebook/pull/5385))
- Make a notebook writable after successful save-as ( \[5296\](https://github.com/jupyter/notebook/pull/5296))
- Add actual watch script ( \[4738\](https://github.com/jupyter/notebook/pull/4738))
- Added \`--autoreload\` flag to \`NotebookApp\` ( \[4795\](https://github.com/jupyter/notebook/pull/4795))
- Enable check\_origin on gateway websocket communication ( \[5471\](https://github.com/jupyter/notebook/pull/5471))
- Restore detection of missing terminado package ( \[5465\](https://github.com/jupyter/notebook/pull/5465))
- Culling: ensure \`last\_activity\` attr exists before use ( \[5355\](https://github.com/jupyter/notebook/pull/5355))
- Added functionality to allow filter kernels by Jupyter Enterprise Gat… ( \[5484\](https://github.com/jupyter/notebook/pull/5484))
- 'Play' icon for run-cell toolbar button ( \[2922\](https://github.com/jupyter/notebook/pull/2922))
- Bump minimum version of jQuery to 3.5.0 ( \[5491\](https://github.com/jupyter/notebook/pull/5491))
- Remove old JS markdown tests, add a new one in selenium ( \[5497\](https://github.com/jupyter/notebook/pull/5497))
- Add support for more RTL languages ( \[5036\](https://github.com/jupyter/notebook/pull/5036))
- Make markdown cells stay RTL in edit mode ( \[5037\](https://github.com/jupyter/notebook/pull/5037))
- Unforce RTL output display ( \[5039\](https://github.com/jupyter/notebook/pull/5039))
- Fixed multicursor backspacing ( \[4880\](https://github.com/jupyter/notebook/pull/4880))
- Implemented Split Cell for multicursor ( \[4824\](https://github.com/jupyter/notebook/pull/4824))
- Alignment issue \[FIXED\] ( \[3173\](https://github.com/jupyter/notebook/pull/3173))
- MathJax: Support for \`\gdef\` ( \[4407\](https://github.com/jupyter/notebook/pull/4407))
- Another (Minor) Duplicate Code Reduction ( \[5316\](https://github.com/jupyter/notebook/pull/5316))
- Update readme regarding maintenance ( \[5500\](https://github.com/jupyter/notebook/pull/5500))
- Document contents chunks ( \[5508\](https://github.com/jupyter/notebook/pull/5508))
- Backspace deletes empty line ( \[5516\](https://github.com/jupyter/notebook/pull/5516))
- The dropdown submenu at notebook page is not keyboard accessible ( \[4732\](https://github.com/jupyter/notebook/pull/4732))
- Tooltips visible through keyboard navigation for specified buttons ( \[4729\](https://github.com/jupyter/notebook/pull/4729))
- Fix for recursive symlink ( \[4670\](https://github.com/jupyter/notebook/pull/4670))
- Fix for the terminal shutdown issue ( \[4180\](https://github.com/jupyter/notebook/pull/4180))
- Add japanese translation files ( \[4490\](https://github.com/jupyter/notebook/pull/4490))
- Workaround for socket permission errors on Cygwin ( \[4584\](https://github.com/jupyter/notebook/pull/4584))
- Implement optional markdown header and footer files ( \[4043\](https://github.com/jupyter/notebook/pull/4043))
- Remove double link when using \`custom\_display\_url\` ( \[5544\](https://github.com/jupyter/notebook/pull/5544))
- Respect \`cell.is\_editable\` during find-and-replace ( \[5545\](https://github.com/jupyter/notebook/pull/5545))
- Fix exception causes all over the codebase ( \[5556\](https://github.com/jupyter/notebook/pull/5556)
- Improve login shell heuristics ( \[5588\](https://github.com/jupyter/notebook/pull/5588))
- Added support for \`JUPYTER\_TOKEN\_FILE\` ( \[5587\](https://github.com/jupyter/notebook/pull/5587))
- Kill notebook itself when server cull idle kernel ( \[5593\](https://github.com/jupyter/notebook/pull/5593))
- Implement password hashing with bcrypt ( \[3793\](https://github.com/jupyter/notebook/pull/3793))
- Fix broken links ( \[5600\](https://github.com/jupyter/notebook/pull/5600))
- Russian internationalization support ( \[5571\](https://github.com/jupyter/notebook/pull/5571))
- Add a metadata tag to override notebook direction (ltr/rtl) ( \[5052\](https://github.com/jupyter/notebook/pull/5052))
- Paste two images from clipboard in markdown cell ( \[5598\](https://github.com/jupyter/notebook/pull/5598))
- Add keyboard shortcuts to menu dropdowns ( \[5525\](https://github.com/jupyter/notebook/pull/5525))
- Update codemirror to \`5.56.0+components1\` ( \[5637\](https://github.com/jupyter/notebook/pull/5637))

Thank you to all the contributors:

- Aaron Myatt
- Adam Blake
- Afshin Taylor Darian
- Aman Bansal
- Ben Thayer
- berendjan
- Bruno P. Kinoshita
- bzinberg
- Christophe Cadilhac
- Daiki Katsuragawa
- David Lukes
- Dmitriy Q
- dmpe
- dylanzjy
- dSchurch
- E. M. Bray
- ErwinRussel
- Felix Mönckemeyer
- Grant Nestor
- Jarrad Whitaker
- Jesus Panales Castillo
- Joshua Zeltser
- Karthikeyan Singaravelan
- Kenichi Ito
- Kevin Bates
- Koki Nishihara
- Kris Wilson
- Kyle Kelley
- Laura Merlo
- levinxo
- Luciano Resende
- Luis Cabezon Manchado
- Madhusudhan Srinivasa
- Matthias Geier
- mattn
- Max Klein
- Min RK
- Mingxuan Lin
- Mohammad Mostafa Farzan
- Niko Felger
- Norah Abanumay
- Onno Broekmans
- PierreMB
- pinarkavak
- Ram Rachum
- Reece Hart
- Remi Rampin
- Rohit Sanjay
- Shane Canon
- Simon Li
- Steinar Sturlaugsson
- Steven Silvester
- taohan16
- Thew Dhanat
- Thomas Kluyver
- Toon Baeyens
- Vidar Tonaas Fauske
- Zachary Sailer

## 6.0.3\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id428)

- Dependency updates to fix startup issues on Windows platform
- Add support for nbconvert 6.x
- Creation of recent tab

Thanks for all the contributors:

- Luciano Resende
- Kevin Bates
- ahangsleben
- Zachary Sailer
- Pallavi Bharadwaj
- Thomas Kluyver
- Min RK
- forest0
- Bibo Hao
- Michal Charemza
- Sergey Shevelev
- Shuichiro MAKIGAKI
- krinsman
- TPartida
- Landen McDonald
- Tres DuBiel

## 6.0.2\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id429)

- Update JQuery dependency to version 3.4.1 to fix security vulnerability (CVE-2019-11358)
- Update CodeMirror to version 5.48.4 to fix Python formatting issues
- Continue removing obsolete Python 2.x code/dependencies
- Multiple documentation updates

Thanks for all the contributors:

- David Robles
- Jason Grout
- Kerwin Sun
- Kevin Bates
- Kyle Kelley
- Luciano Resende
- Marcus D Sherman
- Sasaki Takeru
- Tom Jarosz
- Vidar Tonaas Fauske
- Wes Turner
- Zachary Sailer

## 6.0.1\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id430)

- Attempt to re-establish websocket connection to Gateway ( \[4777\](https://github.com/jupyter/notebook/pull/4777))
- Add missing react-dom js to package data ( \[4772\](https://github.com/jupyter/notebook/pull/4772))

Thanks for all the contributors:

- Eunsoo Park
- Min RK

## 6.0\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id431)

This is the first major release of the Jupyter Notebook since version 5.0 (March 2017).

We encourage users to start trying JupyterLab, which has just announced it's 1.0 release in preparation for a future transition.

- Remove Python 2.x support in favor of Python 3.5 and higher.
- Multiple accessibility enhancements and bug-fixes.
- Multiple translation enhancements and bug-fixes.
- Remove deprecated ANSI CSS styles.
- Native support to forward requests to Jupyter Gateway(s) (Embedded NB2KG).
- Use JavaScript to redirect users to notebook homepage.
- Enhanced SSL/TLS security by using PROTOCOL\_TLS which selects the highest ssl/tls protocol version available that both the client and server support. When PROTOCOL\_TLS is not available use PROTOCOL\_SSLv23.
- Add \`?no\_track\_activity=1\` argument to allow API requests. to not be registered as activity (e.g. API calls by external activity monitors).
- Kernels shutting down due to an idle timeout is no longer considered an activity-updating event.
- Further improve compatibility with tornado 6 with improved checks for when websockets are closed.
- Launch the browser with a local file which redirects to the server address including the authentication token. This prevents another logged-in user from stealing the token from command line arguments and authenticating to the server. The single-use token previously used to mitigate this has been removed. Thanks to Dr. Owain Kenway for suggesting the local file approach.
- Respect nbconvert entrypoints as sources for exporters
- Update to CodeMirror to 5.37, which includes f-string syntax for Python 3.6.
- Update jquery-ui to 1.12
- Execute cells by clicking icon in input prompt.
- New “Save as” menu option.
- When serving on a loopback interface, protect against DNS rebinding by checking the \`Host\` header from the browser. This check can be disabled if necessary by setting \`NotebookApp.allow\_remote\_access\` . (Disabled by default while we work out some Mac issues in \[3754\](https://github.com/jupyter/notebook/issues/3754)).
- Add kernel\_info\_timeout traitlet to enable restarting slow kernels.
- Add \`custom\_display\_host\` config option to override displayed URL.
- Add /metrics endpoint for Prometheus Metrics.
- Optimize large file uploads.
- Allow access control headers to be overridden in jupyter\_notebook\_config.py to support greater CORS and proxy configuration flexibility.
- Add support for terminals on windows.
- Add a “restart and run all” button to the toolbar.
- Frontend/extension-config: allow default json files in a .d directory.
- Allow setting token via jupyter\_token env.
- Cull idle kernels using \`--MappingKernelManager.cull\_idle\_timeout\` .
- Allow read-only notebooks to be trusted.
- Convert JS tests to Selenium.

Security Fixes included in previous minor releases of Jupyter Notebook and also included in version 6.0.

- Fix Open Redirect vulnerability (CVE-2019-10255) where certain malicious URLs could redirect from the Jupyter login page to a malicious site after a successful login.
- Contains a security fix for a cross-site inclusion (XSSI) vulnerability (CVE-2019–9644), where files at a known URL could be included in a page from an unauthorized website if the user is logged into a Jupyter server. The fix involves setting the \`X-Content-Type-Options: nosniff\` header, and applying CSRF checks previously on all non-GET API requests to GET requests to API endpoints and the /files/ endpoint.
- Check Host header to more securely protect localhost deployments from DNS rebinding. This is a pre-emptive measure, not fixing a known vulnerability. Use \`.NotebookApp.allow\_remote\_access\` and \`.NotebookApp.local\_hostnames\` to configure access.
- Upgrade bootstrap to 3.4, fixing an XSS vulnerability, which has been assigned \[CVE-2018-14041\](https://nvd.nist.gov/vuln/detail/CVE-2018-14041).
- Contains a security fix preventing malicious directory names from being able to execute javascript.
- Contains a security fix preventing nbconvert endpoints from executing javascript with access to the server API. CVE request pending.

Thanks for all the contributors:

- AAYUSH SINHA
- Aaron Hall, MBA
- Abhinav Sagar
- Adam Rule
- Adeel Ahmad
- Alex Rothberg
- Amy Skerry-Ryan
- Anastasis Germanidis
- Andrés Sánchez
- Arjun Radhakrishna
- Arovit Narula
- Benda Xu
- Björn Grüning
- Brian E. Granger
- Carol Willing
- Celina Kilcrease
- Chris Holdgraf
- Chris Miller
- Ciaran Langton
- Damian Avila
- Dana Lee
- Daniel Farrell
- Daniel Nicolai
- Darío Hereñú
- Dave Aitken
- Dave Foster
- Dave Hirschfeld
- Denis Ledoux
- Dmitry Mikushin
- Dominic Kuang
- Douglas Hanley
- Elliott Sales de Andrade
- Emilio Talamante Lugo
- Eric Perry
- Ethan T. Hendrix
- Evan Van Dam
- Francesco Franchina
- Frédéric Chapoton
- Félix-Antoine Fortin
- Gabriel
- Gabriel Nützi
- Gabriel Ruiz
- Gestalt LUR
- Grant Nestor
- Gustavo Efeiche
- Harsh Vardhan
- Heng GAO
- Hisham Elsheshtawy
- Hong Xu
- Ian Rose
- Ivan Ogasawara
- J Forde
- Jason Grout
- Jessica B. Hamrick
- Jiaqi Liu
- John Emmons
- Josh Barnes
- Karthik Balakrishnan
- Kevin Bates
- Kirit Thadaka
- Kristian Gregorius Hustad
- Kyle Kelley
- Leo Gallucci
- Lilian Besson
- Lucas Seiki Oshiro
- Luciano Resende
- Luis Angel Rodriguez Guerrero
- M Pacer
- Maarten Breddels
- Mac Knight
- Madicken Munk
- Maitiú Ó Ciaráin
- Marc Udoff
- Mathis HAMMEL
- Mathis Rosenhauer
- Matthias Bussonnier
- Matthias Geier
- Max Vovshin
- Maxime Mouchet
- Michael Chirico
- Michael Droettboom
- Michael Heilman
- Michael Scott Cuthbert
- Michal Charemza
- Mike Boyle
- Milos Miljkovic
- Min RK
- Miro Hrončok
- Nicholas Bollweg
- Nitesh Sawant
- Ondrej Jariabka
- Park Hae Jin
- Paul Ivanov
- Paul Masson
- Peter Parente
- Pierre Tholoniat
- Remco Verhoef
- Roland Weber
- Roman Kornev
- Rosa Swaby
- Roy Hyunjin Han
- Sally
- Sam Lau
- Samar Sultan
- Shiti Saxena
- Simon Biggs
- Spencer Park
- Stephen Ward
- Steve (Gadget) Barnes
- Steven Silvester
- Surya Prakash Susarla
- Syed Shah
- Sylvain Corlay
- Thomas Aarholt
- Thomas Kluyver
- Tim
- Tim Head
- Tim Klever
- Tim Metzler
- Todd
- Tom Jorquera
- Tyler Makaro
- Vaibhav Sagar
- Victor
- Vidar Tonaas Fauske
- Vu Minh Tam
- Vít Tuček
- Will Costello
- Will Starms
- William Hosford
- Xiaohan Li
- Yuvi Panda
- ashley teoh
- nullptr

## 5.7.8\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id432)

- Fix regression in restarting kernels in 5.7.5. The restart handler would return before restart was completed.
- Further improve compatibility with tornado 6 with improved checks for when websockets are closed.
- Fix regression in 5.7.6 on Windows where .js files could have the wrong mime-type.
- Fix Open Redirect vulnerability (CVE-2019-10255) where certain malicious URLs could redirect from the Jupyter login page to a malicious site after a successful login. 5.7.7 contained only a partial fix for this issue.

## 5.7.6\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id433)

5.7.6 contains a security fix for a cross-site inclusion (XSSI) vulnerability (CVE-2019–9644), where files at a known URL could be included in a page from an unauthorized website if the user is logged into a Jupyter server. The fix involves setting the \`X-Content-Type-Options: nosniff\` header, and applying CSRF checks previously on all non-GET API requests to GET requests to API endpoints and the /files/ endpoint.

The attacking page is able to access some contents of files when using Internet Explorer through script errors, but this has not been demonstrated with other browsers.

## 5.7.5\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id434)

- Fix compatibility with tornado 6 ( \[4392\](https://github.com/jupyter/notebook/pull/4392), \[4449\](https://github.com/jupyter/notebook/pull/4449)).
- Fix opening integer filedescriptor during startup on Python 2 ( \[4349\](https://github.com/jupyter/notebook/pull/4349))
- Fix compatibility with asynchronous \[KernelManager.restart\_kernel\]{.title-ref} methods ( \[4412\](https://github.com/jupyter/notebook/pull/4412))

## 5.7.4\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id435)

5.7.4 fixes a bug introduced in 5.7.3, in which the \`list\_running\_servers()\` function attempts to parse HTML files as JSON, and consequently crashes ( \[4284\](https://github.com/jupyter/notebook/pull/4284)).

## 5.7.3\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id436)

5.7.3 contains one security improvement and one security fix:

- Launch the browser with a local file which redirects to the server address including the authentication token ( \[4260\](https://github.com/jupyter/notebook/pull/4260)). This prevents another logged-in user from stealing the token from command line arguments and authenticating to the server. The single-use token previously used to mitigate this has been removed. Thanks to Dr. Owain Kenway for suggesting the local file approach.
- Upgrade bootstrap to 3.4, fixing an XSS vulnerability, which has been assigned \[CVE-2018-14041\](https://nvd.nist.gov/vuln/detail/CVE-2018-14041) ( \[4271\](https://github.com/jupyter/notebook/pull/4271)).

## 5.7.2\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id437)

5.7.2 contains a security fix preventing malicious directory names from being able to execute javascript. CVE request pending.

## 5.7.1\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id438)

5.7.1 contains a security fix preventing nbconvert endpoints from executing javascript with access to the server API. CVE request pending.

## 5.7.0\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id439)

New features:

- Update to CodeMirror to 5.37, which includes f-string syntax for Python 3.6 ( \[3816\](https://github.com/jupyter/notebook/pull/3816))
- Update jquery-ui to 1.12 ( \[3836\](https://github.com/jupyter/notebook/pull/3836))
- Check Host header to more securely protect localhost deployments from DNS rebinding. This is a pre-emptive measure, not fixing a known vulnerability ( \[3766\](https://github.com/jupyter/notebook/pull/3766)). Use \`.NotebookApp.allow\_remote\_access\` and \`.NotebookApp.local\_hostnames\` to configure access.
- Allow access-control-allow-headers to be overridden ( \[3886\](https://github.com/jupyter/notebook/pull/3886))
- Allow configuring max\_body\_size and max\_buffer\_size ( \[3829\](https://github.com/jupyter/notebook/pull/3829))
- Allow configuring get\_secure\_cookie keyword-args ( \[3778\](https://github.com/jupyter/notebook/pull/3778))
- Respect nbconvert entrypoints as sources for exporters ( \[3879\](https://github.com/jupyter/notebook/pull/3879))
- Include translation sources in source distributions ( \[3925\](https://github.com/jupyter/notebook/pull/3925), \[3931\](https://github.com/jupyter/notebook/pull/3931))
- Various improvements to documentation ( \[3799\](https://github.com/jupyter/notebook/pull/3799), \[3800\](https://github.com/jupyter/notebook/pull/3800), \[3806\](https://github.com/jupyter/notebook/pull/3806), \[3883\](https://github.com/jupyter/notebook/pull/3883), \[3908\](https://github.com/jupyter/notebook/pull/3908))

Fixing problems:

- Fix breadcrumb link when running with a base url ( \[3905\](https://github.com/jupyter/notebook/pull/3905))
- Fix possible type error when closing activity stream ( \[3907\](https://github.com/jupyter/notebook/pull/3907))
- Disable metadata editing for non-editable cells ( \[3744\](https://github.com/jupyter/notebook/pull/3744))
- Fix some styling and alignment of prompts caused by regressions in 5.6.0.
- Enter causing page reload in shortcuts editor ( \[3871\](https://github.com/jupyter/notebook/pull/3871))
- Fix uploading to the same file twice ( \[3712\](https://github.com/jupyter/notebook/pull/3712))

See the 5.7 milestone on GitHub for a complete list of \[pull requests\](https://github.com/jupyter/notebook/pulls?utf8=%E2%9C%93&amp;q=is%3Apr%20milestone%3A5.7) involved in this release.

Thanks to the following contributors:

- Aaron Hall
- Benjamin Ragan-Kelley
- Bill Major
- bxy007
- Dave Aitken
- Denis Ledoux
- Félix-Antoine Fortin
- Gabriel
- Grant Nestor
- Kevin Bates
- Kristian Gregorius Hustad
- M Pacer
- Madicken Munk
- Maitiu O Ciarain
- Matthias Bussonnier
- Michael Boyle
- Michael Chirico
- Mokkapati, Praneet(ES)
- Peter Parente
- Sally Wilsak
- Steven Silvester
- Thomas Kluyver
- Walter Martin

## 5.6.0\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id440)

New features:

- Execute cells by clicking icon in input prompt ( \[3535\](https://github.com/jupyter/notebook/pull/3535), \[3687\](https://github.com/jupyter/notebook/pull/3687))
- New “Save as” menu option ( \[3289\](https://github.com/jupyter/notebook/pull/3289))
- When serving on a loopback interface, protect against DNS rebinding by checking the \`Host\` header from the browser ( \[3714\](https://github.com/jupyter/notebook/pull/3714)). This check can be disabled if necessary by setting \`NotebookApp.allow\_remote\_access\` . (Disabled by default while we work out some Mac issues in \[3754\](https://github.com/jupyter/notebook/issues/3754)).
- Add kernel\_info\_timeout traitlet to enable restarting slow kernels ( \[3665\](https://github.com/jupyter/notebook/pull/3665))
- Add \`custom\_display\_host\` config option to override displayed URL ( \[3668\](https://github.com/jupyter/notebook/pull/3668))
- Add /metrics endpoint for Prometheus Metrics ( \[3490\](https://github.com/jupyter/notebook/pull/3490))
- Update to MathJax 2.7.4 ( \[3751\](https://github.com/jupyter/notebook/pull/3751))
- Update to jQuery 3.3 ( \[3655\](https://github.com/jupyter/notebook/pull/3655))
- Update marked to 0.4 ( \[3686\](https://github.com/jupyter/notebook/pull/3686))

Fixing problems:

- Don't duplicate token in displayed URL ( \[3656\](https://github.com/jupyter/notebook/pull/3656))
- Clarify displayed URL when listening on all interfaces ( \[3703\](https://github.com/jupyter/notebook/pull/3703))
- Don't trash non-empty directories on Windows ( \[3673\](https://github.com/jupyter/notebook/pull/3673))
- Include LICENSE file in wheels ( \[3671\](https://github.com/jupyter/notebook/pull/3671))
- Don't show “0 active kernels” when starting the notebook ( \[3696\](https://github.com/jupyter/notebook/pull/3696))

Testing:

- Add find replace test ( \[3630\](https://github.com/jupyter/notebook/pull/3630))
- Selenium test for deleting all cells ( \[3601\](https://github.com/jupyter/notebook/pull/3601))
- Make creating a new notebook more robust ( \[3726\](https://github.com/jupyter/notebook/pull/3726))

Thanks to the following contributors:

- Arovit Narula ( \[arovit\](https://github.com/arovit))
- lucasoshiro ( \[lucasoshiro\](https://github.com/lucasoshiro))
- M Pacer ( \[mpacer\](https://github.com/mpacer))
- Thomas Kluyver ( \[takluyver\](https://github.com/takluyver))
- Todd ( \[toddrme2178\](https://github.com/toddrme2178))
- Yuvi Panda ( \[yuvipanda\](https://github.com/yuvipanda))

See the 5.6 milestone on GitHub for a complete list of \[pull requests\](https://github.com/jupyter/notebook/pulls?utf8=%E2%9C%93&amp;q=is%3Apr%20milestone%3A5.6) involved in this release.

## 5.5.0\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id441)

New features:

- The files list now shows file sizes ( \[3539\](https://github.com/jupyter/notebook/pull/3539))
- Add a quit button in the dashboard ( \[3004\](https://github.com/jupyter/notebook/pull/3004))
- Display hostname in the terminal when running remotely ( \[3356\](https://github.com/jupyter/notebook/pull/3356), \[3593\](https://github.com/jupyter/notebook/pull/3593))
- Add slides exportation/download to the menu ( \[3287\](https://github.com/jupyter/notebook/pull/3287))
- Add any extra installed nbconvert exporters to the “Download as” menu ( \[3323\](https://github.com/jupyter/notebook/pull/3323))
- Editor: warning when overwriting a file that is modified on disk ( \[2783\](https://github.com/jupyter/notebook/pull/2783))
- Display a warning message if cookies are not enabled ( \[3511\](https://github.com/jupyter/notebook/pull/3511))
- Basic \`\_\_version\_\_\` reporting for extensions ( \[3541\](https://github.com/jupyter/notebook/pull/3541))
- Add \`NotebookApp.terminals\_enabled\` config option ( \[3478\](https://github.com/jupyter/notebook/pull/3478))
- Make buffer time between last modified on disk and last modified on last save configurable ( \[3273\](https://github.com/jupyter/notebook/pull/3273))
- Allow binding custom shortcuts for 'close and halt' ( \[3314\](https://github.com/jupyter/notebook/pull/3314))
- Add description for 'Trusted' notification ( \[3386\](https://github.com/jupyter/notebook/pull/3386))
- Add \`settings\['activity\_sources'\]\` ( \[3401\](https://github.com/jupyter/notebook/pull/3401))
- Add an \`output\_updated.OutputArea\` event ( \[3560\](https://github.com/jupyter/notebook/pull/3560))

Fixing problems:

- Fixes to improve web accessibility ( \[3507\](https://github.com/jupyter/notebook/pull/3507))
- Fixed color contrast issue in tree.less ( \[3336\](https://github.com/jupyter/notebook/pull/3336))
- Allow cancelling upload of large files ( \[3373\](https://github.com/jupyter/notebook/pull/3373))
- Don't clear login cookie on requests without cookie ( \[3380\](https://github.com/jupyter/notebook/pull/3380))
- Don't trash files on different device to home dir on Linux ( \[3304\](https://github.com/jupyter/notebook/pull/3304))
- Clear waiting asterisks when restarting kernel ( \[3494\](https://github.com/jupyter/notebook/pull/3494))
- Fix output prompt when \`execution\_count\` missing ( \[3236\](https://github.com/jupyter/notebook/pull/3236))
- Make the 'changed on disk' dialog work when displayed twice ( \[3589\](https://github.com/jupyter/notebook/pull/3589))
- Fix going back to root directory with history in notebook list ( \[3411\](https://github.com/jupyter/notebook/pull/3411))
- Allow defining keyboard shortcuts for missing actions ( \[3561\](https://github.com/jupyter/notebook/pull/3561))
- Prevent default on pageup/pagedown when completer is active ( \[3500\](https://github.com/jupyter/notebook/pull/3500))
- Prevent default event handling on new terminal ( \[3497\](https://github.com/jupyter/notebook/pull/3497))
- ConfigManager should not write out default values found in the .d directory ( \[3485\](https://github.com/jupyter/notebook/pull/3485))
- Fix leak of iopub object in activity monitoring ( \[3424\](https://github.com/jupyter/notebook/pull/3424))
- Javascript lint in notebooklist.js ( \[3409\](https://github.com/jupyter/notebook/pull/3409))
- Some Javascript syntax fixes ( \[3294\](https://github.com/jupyter/notebook/pull/3294))
- Convert native for loop to \`Array.forEach()\` ( \[3477\](https://github.com/jupyter/notebook/pull/3477))
- Disable cache when downloading nbconvert output ( \[3484\](https://github.com/jupyter/notebook/pull/3484))
- Add missing digestmod arg to HMAC ( \[3399\](https://github.com/jupyter/notebook/pull/3399))
- Log OSErrors failing to create less-critical files during startup ( \[3384\](https://github.com/jupyter/notebook/pull/3384))
- Use powershell on Windows ( \[3379\](https://github.com/jupyter/notebook/pull/3379))
- API spec improvements, API handler improvements ( \[3368\](https://github.com/jupyter/notebook/pull/3368))
- Set notebook to dirty state after change to kernel metadata ( \[3350\](https://github.com/jupyter/notebook/pull/3350))
- Use CSP header to treat served files as belonging to a separate origin ( \[3341\](https://github.com/jupyter/notebook/pull/3341))
- Don't install gettext into builtins ( \[3330\](https://github.com/jupyter/notebook/pull/3330))
- Add missing \`import \_\` ( \[3316\](https://github.com/jupyter/notebook/pull/3316), \[3326\](https://github.com/jupyter/notebook/pull/3326))
- Write \`notebook.json\` file atomically ( \[3305\](https://github.com/jupyter/notebook/pull/3305))
- Fix clicking with modifiers, page title updates ( \[3282\](https://github.com/jupyter/notebook/pull/3282))
- Upgrade jQuery to version 2.2 ( \[3428\](https://github.com/jupyter/notebook/pull/3428))
- Upgrade xterm.js to 3.1.0 ( \[3189\](https://github.com/jupyter/notebook/pull/3189))
- Upgrade moment.js to 2.19.3 ( \[3562\](https://github.com/jupyter/notebook/pull/3562))
- Upgrade CodeMirror to 5.35 ( \[3372\](https://github.com/jupyter/notebook/pull/3372))
- “Require” pyzmq>=17 ( \[3586\](https://github.com/jupyter/notebook/pull/3586))

Documentation:

- Documentation updates and organisation ( \[3584\](https://github.com/jupyter/notebook/pull/3584))
- Add section in docs about privacy ( \[3571\](https://github.com/jupyter/notebook/pull/3571))
- Add explanation on how to change the type of a cell to Markdown ( \[3377\](https://github.com/jupyter/notebook/pull/3377))
- Update docs with confd implementation details ( \[3520\](https://github.com/jupyter/notebook/pull/3520))
- Add more information for where \`jupyter\_notebook\_config.py\` is located ( \[3346\](https://github.com/jupyter/notebook/pull/3346))
- Document options to enable nbextensions in specific sections ( \[3525\](https://github.com/jupyter/notebook/pull/3525))
- jQuery attribute selector value MUST be surrounded by quotes ( \[3527\](https://github.com/jupyter/notebook/pull/3527))
- Do not execute special notebooks with nbsphinx ( \[3360\](https://github.com/jupyter/notebook/pull/3360))
- Other minor fixes in \[3288\](https://github.com/jupyter/notebook/pull/3288), \[3528\](https://github.com/jupyter/notebook/pull/3528), \[3293\](https://github.com/jupyter/notebook/pull/3293), \[3367\](https://github.com/jupyter/notebook/pull/3367)

Testing:

- Testing with Selenium & Sauce labs ( \[3321\](https://github.com/jupyter/notebook/pull/3321))
- Selenium utils + markdown rendering tests ( \[3458\](https://github.com/jupyter/notebook/pull/3458))
- Convert insert cell tests to Selenium ( \[3508\](https://github.com/jupyter/notebook/pull/3508))
- Convert prompt numbers tests to Selenium ( \[3554\](https://github.com/jupyter/notebook/pull/3554))
- Convert delete cells tests to Selenium ( \[3465\](https://github.com/jupyter/notebook/pull/3465))
- Convert undelete cell tests to Selenium ( \[3475\](https://github.com/jupyter/notebook/pull/3475))
- More selenium testing utilities ( \[3412\](https://github.com/jupyter/notebook/pull/3412))
- Only check links when build is trigger by Travis Cron job ( \[3493\](https://github.com/jupyter/notebook/pull/3493))
- Fix Appveyor build errors ( \[3430\](https://github.com/jupyter/notebook/pull/3430))
- Undo patches in teardown before attempting to delete files ( \[3459\](https://github.com/jupyter/notebook/pull/3459))
- Get tests running with tornado 5 ( \[3398\](https://github.com/jupyter/notebook/pull/3398))
- Unpin ipykernel version on Travis ( \[3223\](https://github.com/jupyter/notebook/pull/3223))

Thanks to the following contributors:

- Arovit Narula ( \[arovit\](https://github.com/arovit))
- Ashley Teoh ( \[ashleytqy\](https://github.com/ashleytqy))
- Nicholas Bollweg ( \[bollwyvl\](https://github.com/bollwyvl))
- Alex Rothberg ( \[cancan101\](https://github.com/cancan101))
- Celina Kilcrease ( \[ckilcrease\](https://github.com/ckilcrease))
- dabuside ( \[dabuside\](https://github.com/dabuside))
- Damian Avila ( \[damianavila\](https://github.com/damianavila))
- Dana Lee ( \[danagilliann\](https://github.com/danagilliann))
- Dave Hirschfeld ( \[dhirschfeld\](https://github.com/dhirschfeld))
- Heng GAO ( \[ehengao\](https://github.com/ehengao))
- Leo Gallucci ( \[elgalu\](https://github.com/elgalu))
- Evan Van Dam ( \[evandam\](https://github.com/evandam))
- forbxy ( \[forbxy\](https://github.com/forbxy))
- Grant Nestor ( \[gnestor\](https://github.com/gnestor))
- Ethan T. Hendrix ( \[hendrixet\](https://github.com/hendrixet))
- Miro Hrončok ( \[hroncok\](https://github.com/hroncok))
- Paul Ivanov ( \[ivanov\](https://github.com/ivanov))
- Darío Hereñú ( \[kant\](https://github.com/kant))
- Kevin Bates ( \[kevin-bates\](https://github.com/kevin-bates))
- Maarten Breddels ( \[maartenbreddels\](https://github.com/maartenbreddels))
- Michael Droettboom ( \[mdboom\](https://github.com/mdboom))
- Min RK ( \[minrk\](https://github.com/minrk))
- M Pacer ( \[mpacer\](https://github.com/mpacer))
- Peter Parente ( \[parente\](https://github.com/parente))
- Paul Masson ( \[paulmasson\](https://github.com/paulmasson))
- Philipp Rudiger ( \[philippjfr\](https://github.com/philippjfr))
- Mac Knight (Shels1909)
- Hisham Elsheshtawy ( \[Sheshtawy\](https://github.com/Sheshtawy))
- Simon Biggs ( \[SimonBiggs\](https://github.com/SimonBiggs))
- Sunil Hari ( \`@sunilhari\` )
- Thomas Kluyver ( \[takluyver\](https://github.com/takluyver))
- Tim Klever ( \[tklever\](https://github.com/tklever))
- Gabriel Ruiz ( \[unnamedplay-r\](https://github.com/unnamedplay-r))
- Vaibhav Sagar ( \[vaibhavsagar\](https://github.com/vaibhavsagar))
- William Hosford ( \[whosford\](https://github.com/whosford))
- Hong ( \[xuhdev\](https://github.com/xuhdev))

See the 5.5 milestone on GitHub for a complete list of \[pull requests\](https://github.com/jupyter/notebook/pulls?utf8=%E2%9C%93&amp;q=is%3Apr%20milestone%3A5.5) involved in this release.

## 5.4.1\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id442)

A security release to fix \[CVE-2018-8768\](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8768).

Thanks to \[Alex\](https://hackerone.com/pisarenko) for identifying this bug, and Jonathan Kamens and Scott Sanderson at Quantopian for verifying it and bringing it to our attention.

## 5.4.0\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id443)

- Fix creating files and folders after navigating directories in the dashboard ( \[3264\](https://github.com/jupyter/notebook/pull/3264)).
- Enable printing notebooks in colour, removing the CSS that made everything black and white ( \[3212\](https://github.com/jupyter/notebook/pull/3212)).
- Limit the completion options displayed in the notebook to 1000, to avoid performance issues with very long lists ( \[3195\](https://github.com/jupyter/notebook/pull/3195)).
- Accessibility improvements in \`tree.html\` ( \[3271\](https://github.com/jupyter/notebook/pull/3271)).
- Added alt-text to the kernel logo image in the notebook UI ( \[3228\](https://github.com/jupyter/notebook/pull/3228)).
- Added a test on Travis CI to flag if symlinks are accidentally introduced in the future. This should prevent the issue that necessitated \`release-5.3.1\` {.interpreted-text role=”ref”} ( \[3227\](https://github.com/jupyter/notebook/pull/3227)).
- Use lowercase letters for random IDs generated in our Javascript ( \[3264\](https://github.com/jupyter/notebook/pull/3264)).
- Removed duplicate code setting \`TextCell.notebook\` ( \[3256\](https://github.com/jupyter/notebook/pull/3256)).

Thanks to the following contributors:

- Alex Soderman ( \[asoderman\](https://github.com/asoderman))
- Matthias Bussonnier ( \[Carreau\](https://github.com/Carreau))
- Min RK ( \[minrk\](https://github.com/minrk))
- Nitesh Sawant ( \[ns23\](https://github.com/ns23))
- Thomas Kluyver ( \[takluyver\](https://github.com/takluyver))
- Yuvi Panda ( \[yuvipanda\](https://github.com/yuvipanda))

See the 5.4 milestone on GitHub for a complete list of \[pull requests\](https://github.com/jupyter/notebook/pulls?utf8=%E2%9C%93&amp;q=is%3Apr%20milestone%3A5.4) involved in this release.

## 5.3.1\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id444)

Replaced a symlink in the repository with a copy, to fix issues installing on Windows ( \[3220\](https://github.com/jupyter/notebook/pull/3220)).

## 5.3.0\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id445)

This release introduces a couple notable improvements, such as terminal support for Windows and support for OS trash (files deleted from the notebook dashboard are moved to the OS trash vs. deleted permanently).

- Add support for terminals on windows ( \[3087\](https://github.com/jupyter/notebook/pull/3087)).
- Add a “restart and run all” button to the toolbar ( \[2965\](https://github.com/jupyter/notebook/pull/2965)).
- Send files to os trash mechanism on delete ( \[1968\](https://github.com/jupyter/notebook/pull/1968)).
- Allow programmatic copy to clipboard ( \[3088\](https://github.com/jupyter/notebook/pull/3088)).
- Use DOM History API for navigating between directories in the file browser ( \[3115\](https://github.com/jupyter/notebook/pull/3115)).
- Add translated files to folder(docs-translations) ( \[3065\](https://github.com/jupyter/notebook/pull/3065)).
- Allow non empty dirs to be deleted ( \[3108\](https://github.com/jupyter/notebook/pull/3108)).
- Set cookie on base\_url ( \[2959\](https://github.com/jupyter/notebook/pull/2959)).
- Allow token-authenticated requests cross-origin by default ( \[2920\](https://github.com/jupyter/notebook/pull/2920)).
- Change cull\_idle\_timeout\_minimum to 1 from 300 ( \[2910\](https://github.com/jupyter/notebook/pull/2910)).
- Config option to shut down server after n seconds with no kernels ( \[2963\](https://github.com/jupyter/notebook/pull/2963)).
- Display a “close” button on load notebook error ( \[3176\](https://github.com/jupyter/notebook/pull/3176)).
- Add action to command palette to run CodeMirror's “indentAuto” on selection ( \[3175\](https://github.com/jupyter/notebook/pull/3175)).
- Add option to specify extra services ( \[3158\](https://github.com/jupyter/notebook/pull/3158)).
- Warn\_bad\_name should not use global name ( \[3160\](https://github.com/jupyter/notebook/pull/3160)).
- Avoid overflow of hidden form ( \[3148\](https://github.com/jupyter/notebook/pull/3148)).
- Fix shutdown trans loss ( \[3147\](https://github.com/jupyter/notebook/pull/3147)).
- Find available kernelspecs more efficiently ( \[3136\](https://github.com/jupyter/notebook/pull/3136)).
- Don't try to translate missing help strings ( \[3122\](https://github.com/jupyter/notebook/pull/3122)).
- Frontend/extension-config: allow default json files in a .d directory ( \[3116\](https://github.com/jupyter/notebook/pull/3116)).
- Use \[requirejs\]{.title-ref} vs. \[require\]{.title-ref} ( \[3097\](https://github.com/jupyter/notebook/pull/3097)).
- Fixes some ui bugs in firefox #3044 ( \[3058\](https://github.com/jupyter/notebook/pull/3058)).
- Compare non-specific language code when choosing to use arabic numerals ( \[3055\](https://github.com/jupyter/notebook/pull/3055)).
- Fix save-script deprecation ( \[3053\](https://github.com/jupyter/notebook/pull/3053)).
- Include moment locales in package\_data ( \[3051\](https://github.com/jupyter/notebook/pull/3051)).
- Fix moment locale loading in bidi support ( \[3048\](https://github.com/jupyter/notebook/pull/3048)).
- Tornado 5: periodiccallback loop arg will be removed ( \[3034\](https://github.com/jupyter/notebook/pull/3034)).
- Use \[/files\]{.title-ref} prefix for pdf-like files ( \[3031\](https://github.com/jupyter/notebook/pull/3031)).
- Add folder for document translation ( \[3022\](https://github.com/jupyter/notebook/pull/3022)).
- When login-in via token, let a chance for user to set the password ( \[3008\](https://github.com/jupyter/notebook/pull/3008)).
- Switch to jupyter\_core implementation of ensure\_dir\_exists ( \[3002\](https://github.com/jupyter/notebook/pull/3002)).
- Send http shutdown request on 'stop' subcommand ( \[3000\](https://github.com/jupyter/notebook/pull/3000)).
- Work on loading ui translations ( \[2969\](https://github.com/jupyter/notebook/pull/2969)).
- Fix ansi inverse ( \[2967\](https://github.com/jupyter/notebook/pull/2967)).
- Add send2trash to requirements for building docs ( \[2964\](https://github.com/jupyter/notebook/pull/2964)).
- I18n readme.md improvement ( \[2962\](https://github.com/jupyter/notebook/pull/2962)).
- Add 'reason' field to json error responses ( \[2958\](https://github.com/jupyter/notebook/pull/2958)).
- Add some padding for stream outputs ( \[3194\](https://github.com/jupyter/notebook/pull/3194)).
- Always use setuptools in \`setup.py\` ( \[3206\](https://github.com/jupyter/notebook/pull/3206)).
- Fix clearing cookies on logout when \`base\_url\` is configured ( \[3207\](https://github.com/jupyter/notebook/pull/3207)).

Thanks to the following contributors:

- bacboc ( \[bacboc\](https://github.com/bacboc))
- Steven Silvester ( \[blink1073\](https://github.com/blink1073))
- Matthias Bussonnier ( \[Carreau\](https://github.com/Carreau))
- ChungJooHo ( \[ChungJooHo\](https://github.com/ChungJooHo))
- edida ( \[edida\](https://github.com/edida))
- Francesco Franchina ( \`ferdas\` )
- forbxy ( \[forbxy\](https://github.com/forbxy))
- Grant Nestor ( \[gnestor\](https://github.com/gnestor))
- Josh Barnes ( \[jcb91\](https://github.com/jcb91))
- JocelynDelalande ( \[JocelynDelalande\](https://github.com/JocelynDelalande))
- Karthik Balakrishnan ( \[karthikb351\](https://github.com/karthikb351))
- Kevin Bates ( \[kevin-bates\](https://github.com/kevin-bates))
- Kirit Thadaka ( \[kirit93\](https://github.com/kirit93))
- Lilian Besson ( \[Naereen\](https://github.com/Naereen))
- Maarten Breddels ( \[maartenbreddels\](https://github.com/maartenbreddels))
- Madhu94 ( \[Madhu94\](https://github.com/Madhu94))
- Matthias Geier ( \[mgeier\](https://github.com/mgeier))
- Michael Heilman ( \[mheilman\](https://github.com/mheilman))
- Min RK ( \[minrk\](https://github.com/minrk))
- PHaeJin ( \[PHaeJin\](https://github.com/PHaeJin))
- Sukneet ( \[Sukneet\](https://github.com/Sukneet))
- Thomas Kluyver ( \[takluyver\](https://github.com/takluyver))

See the 5.3 milestone on GitHub for a complete list of \[pull requests\](https://github.com/jupyter/notebook/pulls?utf8=%E2%9C%93&amp;q=is%3Apr%20milestone%3A5.3) involved in this release.

## 5.2.1\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id446)

- Fix invisible CodeMirror cursor at specific browser zoom levels ( \[2983\](https://github.com/jupyter/notebook/pull/2983)).
- Fix nbconvert handler causing broken export to PDF ( \[2981\](https://github.com/jupyter/notebook/pull/2981)).
- Fix the prompt\_area argument of the output area constructor. ( \[2961\](https://github.com/jupyter/notebook/pull/2961)).
- Handle a compound extension in new\_untitled ( \[2949\](https://github.com/jupyter/notebook/pull/2949)).
- Allow disabling offline message buffering ( \[2916\](https://github.com/jupyter/notebook/pull/2916)).

Thanks to the following contributors:

- Steven Silvester ( \[blink1073\](https://github.com/blink1073))
- Grant Nestor ( \[gnestor\](https://github.com/gnestor))
- Jason Grout ( \[jasongrout\](https://github.com/jasongrout))
- Min RK ( \[minrk\](https://github.com/minrk))
- M Pacer ( \[mpacer\](https://github.com/mpacer))

See the 5.2.1 milestone on GitHub for a complete list of \[pull requests\](https://github.com/jupyter/notebook/pulls?utf8=%E2%9C%93&amp;q=is%3Apr%20milestone%3A5.2.1) involved in this release.

## 5.2.0\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id447)

- Allow setting token via jupyter\_token env ( \[2921\](https://github.com/jupyter/notebook/pull/2921)).
- Fix some errors caused by raising 403 in get\_current\_user ( \[2919\](https://github.com/jupyter/notebook/pull/2919)).
- Register contents\_manager.files\_handler\_class directly ( \[2917\](https://github.com/jupyter/notebook/pull/2917)).
- Update viewable\_extensions ( \[2913\](https://github.com/jupyter/notebook/pull/2913)).
- Show edit shortcuts modal after shortcuts modal is hidden ( \[2912\](https://github.com/jupyter/notebook/pull/2912)).
- Improve edit/view behavior ( \[2911\](https://github.com/jupyter/notebook/pull/2911)).
- The root directory of the notebook server should never be hidden ( \[2907\](https://github.com/jupyter/notebook/pull/2907)).
- Fix notebook require config to match tools/build-main ( \[2888\](https://github.com/jupyter/notebook/pull/2888)).
- Give page constructor default arguments ( \[2887\](https://github.com/jupyter/notebook/pull/2887)).
- Fix codemirror.less to match codemirror's expected padding layout ( \[2880\](https://github.com/jupyter/notebook/pull/2880)).
- Add x-xsrftoken to access-control-allow-headers ( \[2876\](https://github.com/jupyter/notebook/pull/2876)).
- Buffer messages when websocket connection is interrupted ( \[2871\](https://github.com/jupyter/notebook/pull/2871)).
- Load locale dynamically only when not en-us ( \[2866\](https://github.com/jupyter/notebook/pull/2866)).
- Changed key strength to 2048 bits ( \[2861\](https://github.com/jupyter/notebook/pull/2861)).
- Resync jsversion with python version ( \[2860\](https://github.com/jupyter/notebook/pull/2860)).
- Allow copy operation on modified, read-only notebook ( \[2854\](https://github.com/jupyter/notebook/pull/2854)).
- Update error handling on apihandlers ( \[2853\](https://github.com/jupyter/notebook/pull/2853)).
- Test python 3.6 on travis, drop 3.3 ( \[2852\](https://github.com/jupyter/notebook/pull/2852)).
- Avoid base64-literals in image tests ( \[2851\](https://github.com/jupyter/notebook/pull/2851)).
- Upgrade xterm.js to 2.9.2 ( \[2849\](https://github.com/jupyter/notebook/pull/2849)).
- Changed all python variables named file to file\_name to not override built\_in file ( \[2830\](https://github.com/jupyter/notebook/pull/2830)).
- Add more doc tests ( \[2823\](https://github.com/jupyter/notebook/pull/2823)).
- Typos fix ( \[2815\](https://github.com/jupyter/notebook/pull/2815)).
- Rename and update license \[ci skip\] ( \[2810\](https://github.com/jupyter/notebook/pull/2810)).
- Travis builds doc ( \[2808\](https://github.com/jupyter/notebook/pull/2808)).
- Pull request i18n ( \[2804\](https://github.com/jupyter/notebook/pull/2804)).
- Factor out output\_prompt\_function, as is done with input prompt ( \[2774\](https://github.com/jupyter/notebook/pull/2774)).
- Use rfc5987 encoding for filenames ( \[2767\](https://github.com/jupyter/notebook/pull/2767)).
- Added path to the resources metadata, the same as in from\_filename(…) in nbconvert.exporters.py ( \[2753\](https://github.com/jupyter/notebook/pull/2753)).
- Make “extrakeys” consistent for notebook and editor ( \[2745\](https://github.com/jupyter/notebook/pull/2745)).
- Bidi support ( \[2357\](https://github.com/jupyter/notebook/pull/2357)).

Special thanks to \[samarsultan\](https://github.com/samarsultan) and the Arabic Competence and Globalization Center Team at IBM Egypt for adding RTL (right-to-left) support to the notebook!

See the 5.2 milestone on GitHub for a complete list of \[issues\](https://github.com/jupyter/notebook/issues?utf8=%E2%9C%93&amp;q=is%3Aissue%20milestone%3A5.2) and \[pull requests\](https://github.com/jupyter/notebook/pulls?utf8=%E2%9C%93&amp;q=is%3Apr%20milestone%3A5.2) involved in this release.

## 5.1.0\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id448)

- Preliminary i18n implementation ( \[2140\](https://github.com/jupyter/notebook/pull/2140)).
- Expose URL with auth token in notebook UI ( \[2666\](https://github.com/jupyter/notebook/pull/2666)).
- Fix search background style ( \[2387\](https://github.com/jupyter/notebook/pull/2387)).
- List running notebooks without requiring \`--allow-root\` ( \[2421\](https://github.com/jupyter/notebook/pull/2421)).
- Allow session of type other than notebook ( \[2559\](https://github.com/jupyter/notebook/pull/2559)).
- Fix search background style ( \[2387\](https://github.com/jupyter/notebook/pull/2387)).
- Fix some Markdown styling issues ( \[2571\](https://github.com/jupyter/notebook/pull/2571)), ( \[2691\](https://github.com/jupyter/notebook/pull/2691)) and ( \[2534\](https://github.com/jupyter/notebook/pull/2534)).
- Remove keymaps that conflict with non-English keyboards ( \[2535\](https://github.com/jupyter/notebook/pull/2535)).
- Add session-specific favicons (notebook, terminal, file) ( \[2452\](https://github.com/jupyter/notebook/pull/2452)).
- Add /api/shutdown handler ( \[2507\](https://github.com/jupyter/notebook/pull/2507)).
- Include metadata when copying a cell ( \[2349\](https://github.com/jupyter/notebook/pull/2349)).
- Stop notebook server from command line ( \[2388\](https://github.com/jupyter/notebook/pull/2388)).
- Improve “View” and “Edit” file handling in dashboard ( \[2449\](https://github.com/jupyter/notebook/pull/2449)) and ( \[2402\](https://github.com/jupyter/notebook/pull/2402)).
- Provide a promise to replace use of the \`app\_initialized.NotebookApp\` event ( \[2710\](https://github.com/jupyter/notebook/pull/2710)).
- Fix disabled collapse/expand output button ( \[2681\](https://github.com/jupyter/notebook/pull/2681)).
- Cull idle kernels using \`--MappingKernelManager.cull\_idle\_timeout\` ( \[2215\](https://github.com/jupyter/notebook/pull/2215)).
- Allow read-only notebooks to be trusted ( \[2718\](https://github.com/jupyter/notebook/pull/2718)).

See the 5.1 milestone on GitHub for a complete list of \[issues\](https://github.com/jupyter/notebook/issues?utf8=%E2%9C%93&amp;q=is%3Aissue%20milestone%3A5.1) and \[pull requests\](https://github.com/jupyter/notebook/pulls?utf8=%E2%9C%93&amp;q=is%3Apr%20milestone%3A5.1) involved in this release.

## 5.0.0\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id449)

This is the first major release of the Jupyter Notebook since version 4.0 was created by the “Big Split” of IPython and Jupyter.

We encourage users to start trying JupyterLab in preparation for a future transition.

We have merged more than 300 pull requests since 4.0. Some of the major user-facing changes are described here.

### File sorting in the dashboard\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#file-sorting-in-the-dashboard)

Files in the dashboard may now be sorted by last modified date or name ( \[943\](https://github.com/jupyter/notebook/pull/943)):

### Cell tags\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#cell-tags)

There is a new cell toolbar for adding \*cell tags\* ( \[2048\](https://github.com/jupyter/notebook/pull/2048)):

Cell tags are a lightweight way to customise the behaviour of tools working with notebooks; we're working on building support for them into tools like \[nbconvert\](https://nbconvert.readthedocs.io/en/latest/) and \[nbval\](https://github.com/computationalmodelling/nbval). To start using tags, select \`Tags\` in the \`View > Cell Toolbar\` menu in a notebook.

The UI for editing cell tags is basic for now; we hope to improve it in future releases.

### Table style\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#table-style)

The default styling for tables in the notebook has been updated ( \[1776\](https://github.com/jupyter/notebook/pull/1776)).

### Customise keyboard shortcuts\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#customise-keyboard-shortcuts)

You can now edit keyboard shortcuts for \*Command Mode\* within the UI ( \[1347\](https://github.com/jupyter/notebook/pull/1347)):

See the \`Help > Edit Keyboard Shortcuts\` menu item and follow the instructions.

### Other additions\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#other-additions)

- You can copy and paste cells between notebooks, using \`Ctrl-C\` {.interpreted-text role=”kbd”} and \`Ctrl-V\` {.interpreted-text role=”kbd”} ( \`Cmd-C\` {.interpreted-text role=”kbd”} and \`Cmd-V\` {.interpreted-text role=”kbd”} on Mac).
- It's easier to configure a password for the notebook with the new \`jupyter notebook password\` command ( \[2007\](https://github.com/jupyter/notebook/pull/2007)).
- The file list can now be ordered by \*last modified\* or by \*name\* ( \[943\](https://github.com/jupyter/notebook/pull/943)).
- Markdown cells now support attachments. Simply drag and drop an image from your desktop to a markdown cell to add it. Unlike relative links that you enter manually, attachments are embedded in the notebook itself. An unreferenced attachment will be automatically scrubbed from the notebook on save ( \[621\](https://github.com/jupyter/notebook/pull/621)).
- Undoing cell deletion now supports undeleting multiple cells. Cells may not be in the same order as before their deletion, depending on the actions you did in the meantime, but this should help reduce the impact of accidentally deleting code.
- The file browser now has \*Edit\* and \*View\* buttons.
- The file browser now supports moving multiple files at once ( \[1088\](https://github.com/jupyter/notebook/pull/1088)).
- The Notebook will refuse to run as root unless the \`--allow-root\` flag is given ( \[1115\](https://github.com/jupyter/notebook/pull/1115)).
- Keyboard shortcuts are now declarative ( \[1234\](https://github.com/jupyter/notebook/pull/1234)).
- Toggling line numbers can now affect all cells ( \[1312\](https://github.com/jupyter/notebook/pull/1312)).
- Add more visible \*Trusted\* and \*Untrusted\* notifications ( \[1658\](https://github.com/jupyter/notebook/pull/1658)).
- The favicon (browser shortcut icon) now changes to indicate when the kernel is busy ( \[1837\](https://github.com/jupyter/notebook/pull/1837)).
- Header and toolbar visibility is now persisted in nbconfig and across sessions ( \[1769\](https://github.com/jupyter/notebook/pull/1769)).
- Load server extensions with ConfigManager so that merge happens recursively, unlike normal config values, to make it load more consistently with frontend extensions( \[2108\](https://github.com/jupyter/notebook/pull/2108)).
- The notebook server now supports the bundler API from the \[jupyter\_cms incubator project\](https://github.com/jupyter-incubator/contentmanagement) ( \[1579\](https://github.com/jupyter/notebook/pull/1579)).
- The notebook server now provides information about kernel activity in its kernel resource API ( \[1827\](https://github.com/jupyter/notebook/pull/1827)).

Remember that upgrading \`notebook\` only affects the user interface. Upgrading kernels and libraries may also provide new features, better stability and integration with the notebook interface.

## 4.4.0\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id450)

- Allow override of output callbacks to redirect output messages. This is used to implement the ipywidgets Output widget, for example.
- Fix an async bug in message handling by allowing comm message handlers to return a promise which halts message processing until the promise resolves.

See the 4.4 milestone on GitHub for a complete list of \[issues\](https://github.com/jupyter/notebook/issues?utf8=%E2%9C%93&amp;q=is%3Aissue%20milestone%3A4.4) and \[pull requests\](https://github.com/jupyter/notebook/pulls?utf8=%E2%9C%93&amp;q=is%3Apr%20milestone%3A4.4) involved in this release.

## 4.3.2\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id451)

4.3.2 is a patch release with a bug fix for CodeMirror and improved handling of the “editable” cell metadata field.

- Monkey-patch for CodeMirror that resolves \[#2037\](https://github.com/jupyter/notebook/issues/2037) without breaking \[#1967\](https://github.com/jupyter/notebook/issues/1967)
- Read-only ( \`"editable": false\` ) cells can be executed but cannot be split, merged, or deleted

See the 4.3.2 milestone on GitHub for a complete list of \[issues\](https://github.com/jupyter/notebook/issues?utf8=%E2%9C%93&amp;q=is%3Aissue%20milestone%3A4.3.2) and \[pull requests\](https://github.com/jupyter/notebook/pulls?utf8=%E2%9C%93&amp;q=is%3Apr%20milestone%3A4.3.2) involved in this release.

## 4.3.1\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id452)

4.3.1 is a patch release with a security patch, a couple bug fixes, and improvements to the newly-released token authentication.

\*\*Security fix\*\*:

- CVE-2016-9971. Fix CSRF vulnerability, where malicious forms could create untitled files and start kernels (no remote execution or modification of existing files) for users of certain browsers (Firefox, Internet Explorer / Edge). All previous notebook releases are affected.

Bug fixes:

- Fix carriage return handling
- Make the font size more robust against fickle browsers
- Ignore resize events that bubbled up and didn't come from window
- Add Authorization to allowed CORS headers
- Downgrade CodeMirror to 5.16 while we figure out issues in Safari

Other improvements:

- Better docs for token-based authentication
- Further highlight token info in log output when autogenerated

See the 4.3.1 milestone on GitHub for a complete list of \[issues\](https://github.com/jupyter/notebook/issues?utf8=%E2%9C%93&amp;q=is%3Aissue%20milestone%3A4.3.1) and \[pull requests\](https://github.com/jupyter/notebook/pulls?utf8=%E2%9C%93&amp;q=is%3Apr%20milestone%3A4.3.1) involved in this release.

## 4.3.0\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id453)

4.3 is a minor release with many bug fixes and improvements. The biggest user-facing change is the addition of token authentication, which is enabled by default. A token is generated and used when your browser is opened automatically, so you shouldn't have to enter anything in the default circumstances. If you see a login page (e.g. by switching browsers, or launching on a new port with \`--no-browser\` ), you get a login URL with the token from the command \`jupyter notebook list\` , which you can paste into your browser.

Highlights:

- API for creating mime-type based renderer extensions using \`OutputArea.register\_mime\_type\` and \`Notebook.render\_cell\_output\` methods. See \[mimerender-cookiecutter\](https://github.com/jupyterlab/mimerender-cookiecutter) for reference implementations and cookiecutter.
- Enable token authentication by default. See \`server\_security\` {.interpreted-text role=”ref”} for more details.
- Update security docs to reflect new signature system
- Switched from term.js to xterm.js

Bug fixes:

- Ensure variable is set if exc\_info is falsey
- Catch and log handler exceptions in \`events.trigger\`
- Add debug log for static file paths
- Don't check origin on token-authenticated requests
- Remove leftover print statement
- Fix highlighting of Python code blocks
- \`json\_errors\` should be outermost decorator on API handlers
- Fix remove old nbserver info files
- Fix notebook mime type on download links
- Fix carriage symbol behavior
- Fix terminal styles
- Update dead links in docs
- If kernel is broken, start a new session
- Include cross-origin check when allowing login URL redirects

Other improvements:

- Allow JSON output data with mime type \`application/\*+json\`
- Allow kernelspecs to have spaces in them for backward compat
- Allow websocket connections from scripts
- Allow \`None\` for post\_save\_hook
- Upgrade CodeMirror to 5.21
- Upgrade xterm to 2.1.0
- Docs for using comms
- Set \`dirty\` flag when output arrives
- Set \`ws-url\` data attribute when accessing a notebook terminal
- Add base aliases for nbextensions
- Include \`@\` operator in CodeMirror IPython mode
- Extend mathjax\_url docstring
- Load nbextension in predictable order
- Improve the error messages for nbextensions
- Include cross-origin check when allowing login URL redirects

See the 4.3 milestone on GitHub for a complete list of \[issues\](https://github.com/jupyter/notebook/issues?utf8=%E2%9C%93&amp;q=is%3Aissue%20milestone%3A4.3%20) and \[pull requests\](https://github.com/jupyter/notebook/pulls?utf8=%E2%9C%93&amp;q=is%3Apr%20milestone%3A4.3%20) involved in this release.

## 4.2.3\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id454)

4.2.3 is a small bugfix release on 4.2.

Highlights:

- Fix regression in 4.2.2 that delayed loading custom.js until after \`notebook\_loaded\` and \`app\_initialized\` events have fired.
- Fix some outdated docs and links.

## 4.2.2\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id455)

4.2.2 is a small bugfix release on 4.2, with an important security fix. All users are strongly encouraged to upgrade to 4.2.2.

Highlights:

- \*\*Security fix\*\*: CVE-2016-6524, where untrusted latex output could be added to the page in a way that could execute javascript.
- Fix missing POST in OPTIONS responses.
- Fix for downloading non-ascii filenames.
- Avoid clobbering ssl\_options, so that users can specify more detailed SSL configuration.
- Fix inverted load order in nbconfig, so user config has highest priority.
- Improved error messages here and there.

## 4.2.1\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id456)

4.2.1 is a small bugfix release on 4.2. Highlights:

- Compatibility fixes for some versions of ipywidgets
- Fix for ignored CSS on Windows
- Fix specifying destination when installing nbextensions

## 4.2.0\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id457)

Release 4.2 adds a new API for enabling and installing extensions. Extensions can now be enabled at the system-level, rather than just per-user. An API is defined for installing directly from a Python package, as well.

Highlighted changes:

- Upgrade MathJax to 2.6 to fix vertical-bar appearing on some equations.
- Restore ability for notebook directory to be root (4.1 regression)
- Large outputs are now throttled, reducing the ability of output floods to kill the browser.
- Fix the notebook ignoring cell executions while a kernel is starting by queueing the messages.
- Fix handling of url prefixes (e.g. JupyterHub) in terminal and edit pages.
- Support nested SVGs in output.

And various other fixes and improvements.

## 4.1.0\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id458)

Bug fixes:

- Properly reap zombie subprocesses
- Fix cross-origin problems
- Fix double-escaping of the base URL prefix
- Handle invalid unicode filenames more gracefully
- Fix ANSI color-processing
- Send keepalive messages for web terminals
- Fix bugs in the notebook tour

UI changes:

- Moved the cell toolbar selector into the \*View\* menu. Added a button that triggers a “hint” animation to the main toolbar so users can find the new location. (Click here to see a \[screencast\](https://cloud.githubusercontent.com/assets/335567/10711889/59665a5a-7a3e-11e5-970f-86b89592880c.gif) )
- Added \*Restart & Run All\* to the \*Kernel\* menu. Users can also bind it to a keyboard shortcut on action \`restart-kernel-and-run-all-cells\` .
- Added multiple-cell selection. Users press \`Shift-Up/Down\` or \`Shift-K/J\` to extend selection in command mode. Various actions such as cut/copy/paste, execute, and cell type conversions apply to all selected cells.
- Added a command palette for executing Jupyter actions by name. Users press \`Cmd/Ctrl-Shift-P\` or click the new command palette icon on the toolbar.
- Added a \*Find and Replace\* dialog to the \*Edit\* menu. Users can also press \`F\` in command mode to show the dialog.

Other improvements:

- Custom KernelManager methods can be Tornado coroutines, allowing async operations.
- Make clearing output optional when rewriting input with \`set\_next\_input(replace=True)\` .
- Added support for TLS client authentication via \`--NotebookApp.client-ca\` .
- Added tags to \`jupyter/notebook\` releases on DockerHub. \`latest\` continues to track the master branch.

See the 4.1 milestone on GitHub for a complete list of \[issues\](https://github.com/jupyter/notebook/issues?page=3&amp;q=milestone%3A4.1+is%3Aclosed+is%3Aissue&amp;utf8=%E2%9C%93) and \[pull requests\](https://github.com/jupyter/notebook/pulls?q=milestone%3A4.1+is%3Aclosed+is%3Apr) handled.

## 4.0.x\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#x)

### 4.0.6\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id459)

- fix installation of mathjax support files
- fix some double-escape regressions in 4.0.5
- fix a couple of cases where errors could prevent opening a notebook

### 4.0.5\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id460)

Security fixes for maliciously crafted files.

- \[CVE-2015-6938\](http://www.openwall.com/lists/oss-security/2015/09/02/3): malicious filenames
- \[CVE-2015-7337\](http://www.openwall.com/lists/oss-security/2015/09/16/3): malicious binary files in text editor.

Thanks to Jonathan Kamens at Quantopian and Juan Broullón for the reports.

### 4.0.4\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id461)

- Fix inclusion of mathjax-safe extension

### 4.0.2\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id462)

- Fix launching the notebook on Windows
- Fix the path searched for frontend config

### 4.0.0\[#\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id463)

First release of the notebook as a standalone package.

\[previous What to do when things go wrong\](https://jupyter-notebook.readthedocs.io/en/stable/troubleshooting.html)

\[next Configuration\](https://jupyter-notebook.readthedocs.io/en/stable/configuration.html)

On this page

- \[7.6\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id1)

    - \[Scratchpad console\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#scratchpad-console)
    - \[Confirmation dialog when closing and shutting down a notebook\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#confirmation-dialog-when-closing-and-shutting-down-a-notebook)
    - \[Notebook improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#notebook-improvements)
    - \[File browser enhancements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#file-browser-enhancements)
    - \[Debugger improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#debugger-improvements)
    - \[Keyboard shortcuts\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#keyboard-shortcuts)
    - \[Inline completion enhancements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#inline-completion-enhancements)
    - \[Terminal enhancements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#terminal-enhancements)
    - \[Keyboard navigation and accessibility\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#keyboard-navigation-and-accessibility)
    - \[Other improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#other-improvements)
    - \[Breaking changes\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#breaking-changes)
- \[7.6.0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id2)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#enhancements-made)
    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#bugs-fixed)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#maintenance-and-upkeep-improvements)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#documentation-improvements)
    - \[Other merged PRs\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#other-merged-prs)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#contributors-to-this-release)
- \[7.6.0rc1\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#rc1)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id3)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id4)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id5)
    - \[Other merged PRs\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id6)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id7)
- \[7.6.0rc0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#rc0)

    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id8)
    - \[Other merged PRs\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id9)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id10)
- \[7.6.0b1\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#b1)

    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id11)
    - \[Other merged PRs\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id12)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id13)
- \[7.6.0b0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#b0)

    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id14)
    - \[Other merged PRs\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id15)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id16)
- \[7.6.0a5\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#a5)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id17)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id18)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id19)
    - \[Other merged PRs\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id20)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id21)
- \[7.6.0a4\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#a4)

    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id22)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id23)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id24)
- \[7.6.0a3\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#a3)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id25)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id26)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id27)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id28)
- \[7.6.0a2\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#a2)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id29)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id30)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id31)
- \[7.6.0a1\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#a1)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id32)
    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id33)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id34)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id35)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id36)
- \[7.6.0a0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#a0)

    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id37)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id38)
- \[7.5\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id39)

    - \[Notebook improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id40)
    - \[Debugger and console enhancements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#debugger-and-console-enhancements)
    - \[Terminal enhancements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id41)
    - \[Media and content support\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#media-and-content-support)
    - \[File browser enhancements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id42)
    - \[Settings editor improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#settings-editor-improvements)
    - \[Cell toolbar settings\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#cell-toolbar-settings)
    - \[Keyboard shortcuts\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id43)
    - \[User interface and accessibility\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#user-interface-and-accessibility)
    - \[Breaking changes\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id44)
- \[7.5.1\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id45)

    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id46)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id47)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id48)
- \[7.5.0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id49)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id50)
    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id51)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id52)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id53)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id54)
- \[7.5.0rc1\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id55)

    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id56)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id57)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id58)
- \[7.5.0rc0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id59)

    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id60)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id61)
- \[7.5.0b1\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id62)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id63)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id64)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id65)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id66)
- \[7.5.0b0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id67)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id68)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id69)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id70)
- \[7.5.0a3\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id71)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id72)
    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id73)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id74)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id75)
- \[7.5.0a2\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id76)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id77)
    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id78)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id79)
- \[7.5.0a1\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id80)

    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id81)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id82)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id83)
- \[7.5.0a0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id84)

    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id85)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id86)
- \[7.4\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id87)

    - \[Code console improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#code-console-improvements)
    - \[Settings import and export\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#settings-import-and-export)
    - \[Support for collaboration without \`RTC:\` drive\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#support-for-collaboration-without-rtc-drive)
    - \[Context menu opt-out\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#context-menu-opt-out)
- \[7.4.0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id88)

    - \[Highlights ✨\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#highlights)
    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id89)
    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id90)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id91)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id92)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id93)
- \[7.4.0rc0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id94)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id95)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id96)
- \[7.4.0b3\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#b3)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id97)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id98)
- \[7.4.0b2\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#b2)

    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id99)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id100)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id101)
- \[7.4.0b1\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id102)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id103)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id104)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id105)
- \[7.4.0b0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id106)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id107)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id108)
- \[7.4.0a3\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id109)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id110)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id111)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id112)
- \[7.4.0a2\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id113)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id114)
    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id115)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id116)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id117)
- \[7.4.0a1\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id118)

    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id119)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id120)
- \[7.4.0a0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id121)

    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id122)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id123)
- \[7.3\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id124)

    - \[Minimap\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#minimap)
    - \[File browser enhancements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id125)
    - \[Improved kernel and server interactions\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#improved-kernel-and-server-interactions)
    - \[Full Width Notebook\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#full-width-notebook)
- \[7.3.2\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id126)

    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id127)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id128)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id129)
- \[7.3.1\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id130)

    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id131)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id132)
- \[7.3.0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id133)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id134)
    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id135)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id136)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id137)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id138)
- \[7.3.0rc0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id139)

    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id140)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id141)
- \[7.3.0b2\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id142)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id143)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id144)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id145)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id146)
- \[7.3.0b1\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id147)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id148)
    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id149)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id150)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id151)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id152)
- \[7.3.0b0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id153)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id154)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id155)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id156)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id157)
- \[7.3.0a1\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id158)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id159)
    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id160)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id161)
- \[7.3.0a0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id162)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id163)
    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id164)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id165)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id166)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id167)
- \[7.2\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id168)

    - \[Full notebook windowing mode by default\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#full-notebook-windowing-mode-by-default)
    - \[Improved Shortcuts Editor\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#improved-shortcuts-editor)
    - \[Dark high contrast theme\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#dark-high-contrast-theme)
- \[7.2.0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id169)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id170)
    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id171)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id172)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id173)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id174)
- \[7.2.0rc1\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id175)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id176)
    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id177)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id178)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id179)
- \[7.2.0rc0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id180)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id181)
    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id182)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id183)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id184)
- \[7.2.0b1\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id185)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id186)
    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id187)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id188)
- \[7.2.0b0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id189)

    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id190)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id191)
- \[7.2.0a0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id192)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id193)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id194)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id195)
- \[v7.1\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#v7-1)

    - \[Diagrams in Markdown\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#diagrams-in-markdown)
    - \[Inline completer\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#inline-completer)
    - \[Keyboard navigation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#keyboard-navigation-improvements)
    - \[Execution history in notebook\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#execution-history-in-notebook)
    - \[Error indicator in the table of contents\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#error-indicator-in-the-table-of-contents)
    - \[Search improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#search-improvements)
    - \[Miscellaneous\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#miscellaneous)
- \[7.1.2\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id196)

    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id197)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id198)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id199)
- \[7.1.1\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id200)

    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id201)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id202)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id203)
- \[7.1.0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id204)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id205)
    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id206)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id207)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id208)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id209)
- \[7.1.0rc1\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id210)

    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id211)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id212)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id213)
- \[7.1.0rc0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id214)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id215)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id216)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id217)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id218)
- \[7.1.0b0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id219)

    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id220)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id221)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id222)
- \[7.1.0a2\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id223)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id224)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id225)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id226)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id227)
- \[7.1.0a1\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id228)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id229)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id230)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id231)
- \[7.1.0a0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id232)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id233)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id234)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id235)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id236)
- \[v7.0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#v7-0)
- \[7.0.6\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id237)

    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id238)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id239)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id240)
- \[7.0.5\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id241)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id242)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id243)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id244)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id245)
- \[7.0.4\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id246)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id247)
    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id248)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id249)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id250)
- \[7.0.3\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id251)

    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id252)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id253)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id254)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id255)
- \[7.0.2\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id256)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id257)
    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id258)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id259)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id260)
- \[7.0.1\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id261)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id262)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id263)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id264)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id265)
- \[7.0.0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id266)

    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id267)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id268)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id269)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id270)
- \[7.0.0rc2\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#rc2)

    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id271)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id272)
- \[7.0.0rc1\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id273)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id274)
    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id275)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id276)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id277)
- \[7.0.0rc0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id278)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id279)
    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id280)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id281)
    - \[API and Breaking Changes\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#api-and-breaking-changes)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id282)
- \[7.0.0b4\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#b4)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id283)
    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id284)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id285)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id286)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id287)
- \[7.0.0b3\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id288)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id289)
    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id290)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id291)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id292)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id293)
- \[7.0.0b2\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id294)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id295)
    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id296)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id297)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id298)
- \[7.0.0b1\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id299)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id300)
    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id301)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id302)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id303)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id304)
- \[7.0.0b0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id305)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id306)
    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id307)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id308)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id309)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id310)
- \[7.0.0a18\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#a18)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id311)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id312)
- \[7.0.0a17\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#a17)

    - \[Highlights\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id313)
    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id314)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id315)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id316)
- \[7.0.0a16\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#a16)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id317)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id318)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id319)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id320)
- \[7.0.0a15\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#a15)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id321)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id322)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id323)
- \[7.0.0a14\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#a14)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id324)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id325)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id326)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id327)
- \[7.0.0a13\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#a13)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id328)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id329)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id330)
- \[7.0.0a12\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#a12)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id331)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id332)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id333)
- \[7.0.0a11\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#a11)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id334)
    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id335)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id336)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id337)
- \[7.0.0a10\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#a10)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id338)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id339)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id340)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id341)
- \[7.0.0a9\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#a9)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id342)
    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id343)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id344)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id345)
- \[7.0.0a8\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#a8)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id346)
    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id347)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id348)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id349)
- \[7.0.0a7\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#a7)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id350)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id351)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id352)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id353)
- \[7.0.0a6\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#a6)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id354)
    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id355)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id356)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id357)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id358)
- \[7.0.0a5\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id359)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id360)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id361)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id362)
- \[7.0.0a4\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id363)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id364)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id365)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id366)
- \[7.0.0a3\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id367)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id368)
    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id369)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id370)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id371)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id372)
- \[7.0.0a2\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id373)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id374)
    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id375)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id376)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id377)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id378)
- \[7.0.0a1\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id379)

    - \[Enhancements made\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id380)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id381)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id382)
- \[6.4.8\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id383)

    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id384)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id385)
- \[6.4.7\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id386)

    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id387)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id388)
    - \[Other merged PRs\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id389)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id390)
- \[6.4.6\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id391)

    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id392)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id393)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id394)
- \[6.4.5\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id395)

    - \[Bug fixes\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#bug-fixes)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id396)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id397)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id398)
- \[6.4.4\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id399)

    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id400)
    - \[Other merged PRs\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id401)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id402)
- \[6.4.3\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id403)

    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id404)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id405)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id406)
- \[6.4.2\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id407)

    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id408)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id409)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id410)
- \[6.4.0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id411)

    - \[Bugs fixed\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id412)
    - \[Maintenance and upkeep improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id413)
    - \[Documentation improvements\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id414)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id415)
- \[6.3.0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id416)

    - \[Merged PRs\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#merged-prs)
    - \[Contributors to this release\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id417)
- \[6.2.0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id418)
- \[Merged PRs\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id419)
- \[6.1.6\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id420)
- \[Merged PRs\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id421)
- \[6.1.5\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id422)
- \[6.1.4\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id423)
- \[6.1.3\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id424)
- \[6.1.2\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id425)
- \[6.1.1\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id426)
- \[6.1.0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id427)
- \[6.0.3\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id428)
- \[6.0.2\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id429)
- \[6.0.1\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id430)
- \[6.0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id431)
- \[5.7.8\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id432)
- \[5.7.6\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id433)
- \[5.7.5\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id434)
- \[5.7.4\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id435)
- \[5.7.3\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id436)
- \[5.7.2\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id437)
- \[5.7.1\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id438)
- \[5.7.0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id439)
- \[5.6.0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id440)
- \[5.5.0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id441)
- \[5.4.1\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id442)
- \[5.4.0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id443)
- \[5.3.1\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id444)
- \[5.3.0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id445)
- \[5.2.1\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id446)
- \[5.2.0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id447)
- \[5.1.0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id448)
- \[5.0.0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id449)

    - \[File sorting in the dashboard\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#file-sorting-in-the-dashboard)
    - \[Cell tags\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#cell-tags)
    - \[Table style\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#table-style)
    - \[Customise keyboard shortcuts\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#customise-keyboard-shortcuts)
    - \[Other additions\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#other-additions)
- \[4.4.0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id450)
- \[4.3.2\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id451)
- \[4.3.1\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id452)
- \[4.3.0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id453)
- \[4.2.3\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id454)
- \[4.2.2\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id455)
- \[4.2.1\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id456)
- \[4.2.0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id457)
- \[4.1.0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id458)
- \[4.0.x\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#x)

    - \[4.0.6\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id459)
    - \[4.0.5\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id460)
    - \[4.0.4\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id461)
    - \[4.0.2\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id462)
    - \[4.0.0\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#id463)

\[Edit on GitHub\](https://github.com/jupyter/notebook/edit/main/docs/source/changelog.md)

\[Show Source\](https://jupyter-notebook.readthedocs.io/en/stable/\_sources/changelog.md.txt)

© Copyright 2015, Jupyter Team, https://jupyter.org.

Created using \[Sphinx\](https://www.sphinx-doc.org/) 8.1.3.

Built with the \[PyData Sphinx Theme\](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.19.0.
!\[Read the Docs\](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+Cjxzdmc6c3ZnCiAgIHZlcnNpb249IjEuMSIKICAgaWQ9InN2ZyIKICAgeD0iMHB4IgogICB5PSIwcHgiCiAgIHZpZXdCb3g9IjY5NCAxOTcgMzQ2LjY5ODU1IDM5OS45ODQ3NyIKICAgc29kaXBvZGk6ZG9jbmFtZT0ibG9nby1saWdodC5zdmciCiAgIHdpZHRoPSIzNDYuNjk4NTUiCiAgIGhlaWdodD0iMzk5Ljk4NDc3IgogICBpbmtzY2FwZTp2ZXJzaW9uPSIxLjMuMiAoMDkxZTIwZWYwZiwgMjAyMy0xMS0yNSwgY3VzdG9tKSIKICAgeG1sbnM6aW5rc2NhcGU9Imh0dHA6Ly93d3cuaW5rc2NhcGUub3JnL25hbWVzcGFjZXMvaW5rc2NhcGUiCiAgIHhtbG5zOnNvZGlwb2RpPSJodHRwOi8vc29kaXBvZGkuc291cmNlZm9yZ2UubmV0L0RURC9zb2RpcG9kaS0wLmR0ZCIKICAgeG1sbnM6c3ZnPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPHN2ZzpkZWZzCiAgICAgaWQ9ImRlZnMxMiIgLz4KICA8c29kaXBvZGk6bmFtZWR2aWV3CiAgICAgaWQ9Im5hbWVkdmlldzEyIgogICAgIHBhZ2Vjb2xvcj0iI2ZmZmZmZiIKICAgICBib3JkZXJjb2xvcj0iIzAwMDAwMCIKICAgICBib3JkZXJvcGFjaXR5PSIwLjI1IgogICAgIGlua3NjYXBlOnNob3dwYWdlc2hhZG93PSIyIgogICAgIGlua3NjYXBlOnBhZ2VvcGFjaXR5PSIwLjAiCiAgICAgaW5rc2NhcGU6cGFnZWNoZWNrZXJib2FyZD0iMCIKICAgICBpbmtzY2FwZTpkZXNrY29sb3I9IiNkMWQxZDEiCiAgICAgaW5rc2NhcGU6em9vbT0iMS4yNTIiCiAgICAgaW5rc2NhcGU6Y3g9Ijk5OC40MDI1NiIKICAgICBpbmtzY2FwZTpjeT0iMTk5LjY4MDUxIgogICAgIGlua3NjYXBlOndpbmRvdy13aWR0aD0iMzQ0MCIKICAgICBpbmtzY2FwZTp3aW5kb3ctaGVpZ2h0PSIxMzg5IgogICAgIGlua3NjYXBlOndpbmRvdy14PSIwIgogICAgIGlua3NjYXBlOndpbmRvdy15PSIyNyIKICAgICBpbmtzY2FwZTp3aW5kb3ctbWF4aW1pemVkPSIxIgogICAgIGlua3NjYXBlOmN1cnJlbnQtbGF5ZXI9InN2ZyIgLz4KICA8c3ZnOmcKICAgICBpZD0ibG9nbyIKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjU1NzUzNjQ0LDAsMCwwLjU1NzUzNjQ0LDY2LjUzMTgxMiwxMDUwLjEyNjIpIj4KICAgIDxzdmc6cGF0aAogICAgICAgc3R5bGU9ImZpbGw6I2ZjZmNmYyIKICAgICAgIGQ9Im0gMTQwOC4xLC0xMTgxLjcgYyAtNy41LDEgLTEyLjcsNy44IC0xMS43LDE1LjMgMC43LDUuNCA0LjYsOS45IDkuOSwxMS4zIDAsMCAzMy4yLDExIDg5LjcsMTUuNiA0NS40LDMuNyA5Ni45LC0zLjIgOTYuOSwtMy4yIDcuNSwtMC4yIDEzLjUsLTYuNSAxMy4yLC0xNCAtMC4zLC03LjUgLTYuNSwtMTMuNSAtMTQsLTEzLjIgLTAuOSwwIC0xLjgsMC4xIC0yLjYsMC4zIDAsMCAtNTAuNCw2LjIgLTkxLjMsMi45IC01NCwtNC40IC04My40LC0xNC4zIC04My40LC0xNC4zIC0yLjIsLTAuNyAtNC41LC0xIC02LjcsLTAuNyB6IG0gMCwtNjcuNiBjIC03LjUsMSAtMTIuNyw3LjggLTExLjcsMTUuMyAwLjcsNS40IDQuNiw5LjkgOS45LDExLjMgMCwwIDMzLjIsMTEgODkuNywxNS42IDQ1LjQsMy43IDk2LjksLTMuMiA5Ni45LC0zLjIgNy41LC0wLjIgMTMuNSwtNi41IDEzLjIsLTE0IC0wLjMsLTcuNSAtNi41LC0xMy41IC0xNCwtMTMuMiAtMC45LDAgLTEuOCwwLjEgLTIuNiwwLjMgMCwwIC01MC40LDYuMiAtOTEuMywyLjkgLTU0LC00LjQgLTgzLjQsLTE0LjMgLTgzLjQsLTE0LjMgLTIuMiwtMC43IC00LjUsLTEgLTYuNywtMC43IHogbSAwLC02Ny42IGMgLTcuNSwxIC0xMi43LDcuOCAtMTEuNywxNS4zIDAuNyw1LjQgNC42LDkuOSA5LjksMTEuMyAwLDAgMzMuMiwxMSA4OS43LDE1LjYgNDUuNCwzLjcgOTYuOSwtMy4yIDk2LjksLTMuMiA3LjUsLTAuMiAxMy41LC02LjUgMTMuMiwtMTQgLTAuMywtNy41IC02LjUsLTEzLjUgLTE0LC0xMy4yIC0wLjksMCAtMS44LDAuMSAtMi42LDAuMyAwLDAgLTUwLjQsNi4yIC05MS4zLDIuOSAtNTQsLTQuNCAtODMuNCwtMTQuMyAtODMuNCwtMTQuMyAtMi4yLC0wLjcgLTQuNSwtMSAtNi43LC0wLjcgeiBtIDAsLTY3LjUgYyAtNy41LDEgLTEyLjcsNy44IC0xMS43LDE1LjMgMC43LDUuNCA0LjYsOS45IDkuOSwxMS4zIDAsMCAzMy4yLDExIDg5LjcsMTUuNiA0NS40LDMuNyA5Ni45LC0zLjIgOTYuOSwtMy4yIDcuNSwtMC4yIDEzLjUsLTYuNSAxMy4yLC0xNCAtMC4zLC03LjUgLTYuNSwtMTMuNSAtMTQsLTEzLjIgLTAuOSwwIC0xLjgsMC4xIC0yLjYsMC4zIDAsMCAtNTAuNCw2LjIgLTkxLjMsMi45IC01NCwtNC40IC04My40LC0xNC4zIC04My40LC0xNC4zIC0yLjIsLTAuOCAtNC41LC0xIC02LjcsLTAuNyB6IG0gLTk0LjcsLTcxLjMgYyAtNzEsMC41IC05Ny41LDIyLjMgLTk3LjUsMjIuMyB2IDUzMC4zIGMgMCwwIDI1LjgsLTIyLjMgMTA5LC0xOC45IDgzLjIsMy40IDEwMC4zLDMyLjYgMjAyLjUsMzQuNiAxMDIuMiwyLjEgMTI3LjksLTE1LjcgMTI3LjksLTE1LjcgbCAxLjUsLTU0MC42IGMgMCwwIC00NiwxMyAtMTM1LjUsMTMuNyAtODkuNSwwLjcgLTExMSwtMjIuOCAtMTkzLjIsLTI1LjUgLTUuMSwtMC4xIC0xMCwtMC4yIC0xNC43LC0wLjIgeiBtIDU5LjQsMzQuNiBjIDAsMCA0MywxNC4yIDEyMi41LDE4LjIgNjcuMiwzLjMgMTM0LjUsLTYuNiAxMzQuNSwtNi42IFYgLTkyOSBjIDAsMCAtMzQuMSwxNy45IC0xMTkuMywxMS44IC02NiwtNC43IC0xMzguNywtMjkuNyAtMTM4LjcsLTI5LjcgeiBtIC00MS41LDEyLjUgYyA3LjYsMCAxMy43LDYuMiAxMy43LDEzLjcgMCw3LjUgLTYuMiwxMy43IC0xMy43LDEzLjcgMCwwIC0yMi4zLDAuMSAtMzUuOCwxLjUgLTIyLjgsMi4zIC0zOC4zLDEwLjYgLTM4LjMsMTAuNiAtNi43LDMuNSAtMTUsMSAtMTguNSwtNS43IC0zLjUsLTYuNyAtMSwtMTUgNS43LC0xOC41IDAsMCAwLDAgMCwwIDAsMCAyMC4yLC0xMC43IDQ4LjQsLTEzLjUgMTYuMywtMS43IDM4LjUsLTEuOCAzOC41LC0xLjggeiBtIC0xMy4yLDY3LjggYyA3LjYsLTAuMiAxMy4zLDAgMTMuMywwIDcuNSwwLjkgMTIuOSw3LjggMTIsMTUuMyAtMC44LDYuMyAtNS43LDExLjIgLTEyLDEyIDAsMCAtMjIuMywwLjEgLTM1LjgsMS41IC0yMi44LDIuMyAtMzguMywxMC42IC0zOC4zLDEwLjYgLTYuNywzLjUgLTE1LDAuOSAtMTguNSwtNS44IC0zLjUsLTYuNyAtMC45LC0xNSA1LjgsLTE4LjUgMCwwIDIwLjIsLTEwLjcgNDguNCwtMTMuNSA3LjksLTAuOSAxNy41LC0xLjQgMjUuMSwtMS42IHogbSAxMy4yLDY3LjUgYyA3LjYsMCAxMy43LDYuMiAxMy43LDEzLjcgMCw3LjYgLTYuMiwxMy43IC0xMy43LDEzLjcgMCwwIC0yMi4zLC0wLjEgLTM1LjgsMS4yIC0yMi44LDIuMyAtMzguMywxMC42IC0zOC4zLDEwLjYgLTYuNywzLjUgLTE1LDAuOSAtMTguNSwtNS44IC0zLjUsLTYuNyAtMC45LC0xNSA1LjgsLTE4LjUgMCwwIDIwLjIsLTEwLjcgNDguNCwtMTMuNSAxNi4yLC0xLjUgMzguNCwtMS40IDM4LjQsLTEuNCB6IgogICAgICAgaWQ9InBhdGgxIiAvPgogIDwvc3ZnOmc+CiAgPGRpdgogICAgIGlkPSJzYWthLWd1aS1yb290Ij4KICAgIDxkaXY+CiAgICAgIDxkaXY+CiAgICAgICAgPHN0eWxlIC8+CiAgICAgIDwvZGl2PgogICAgPC9kaXY+CiAgPC9kaXY+Cjwvc3ZnOnN2Zz4K)

stable

Versions

\[master\](https://jupyter-notebook.readthedocs.io/en/master/changelog.html)

\[latest\](https://jupyter-notebook.readthedocs.io/en/latest/changelog.html)

\*\*\[stable\](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html)\*\*

\[v7.6.0\](https://jupyter-notebook.readthedocs.io/en/v7.6.0/changelog.html)

\[v7.5.7\](https://jupyter-notebook.readthedocs.io/en/v7.5.7/changelog.html)

\[v7.5.6\](https://jupyter-notebook.readthedocs.io/en/v7.5.6/changelog.html)

\[v7.5.5\](https://jupyter-notebook.readthedocs.io/en/v7.5.5/changelog.html)

\[v7.5.4\](https://jupyter-notebook.readthedocs.io/en/v7.5.4/changelog.html)

\[v7.5.3\](https://jupyter-notebook.readthedocs.io/en/v7.5.3/changelog.html)

\[v7.5.2\](https://jupyter-notebook.readthedocs.io/en/v7.5.2/changelog.html)

\[v7.5.1\](https://jupyter-notebook.readthedocs.io/en/v7.5.1/changelog.html)

\[v7.5.0\](https://jupyter-notebook.readthedocs.io/en/v7.5.0/changelog.html)

\[v7.4.7\](https://jupyter-notebook.readthedocs.io/en/v7.4.7/changelog.html)

\[v7.4.6\](https://jupyter-notebook.readthedocs.io/en/v7.4.6/changelog.html)

\[v7.4.5\](https://jupyter-notebook.readthedocs.io/en/v7.4.5/changelog.html)

\[v7.4.4\](https://jupyter-notebook.readthedocs.io/en/v7.4.4/changelog.html)

\[v7.4.3\](https://jupyter-notebook.readthedocs.io/en/v7.4.3/changelog.html)

\[v7.4.2\](https://jupyter-notebook.readthedocs.io/en/v7.4.2/changelog.html)

\[v7.4.1\](https://jupyter-notebook.readthedocs.io/en/v7.4.1/changelog.html)

\[v7.4.0\](https://jupyter-notebook.readthedocs.io/en/v7.4.0/changelog.html)

\[v7.3.3\](https://jupyter-notebook.readthedocs.io/en/v7.3.3/changelog.html)

\[v7.3.2\](https://jupyter-notebook.readthedocs.io/en/v7.3.2/changelog.html)

\[v7.3.1\](https://jupyter-notebook.readthedocs.io/en/v7.3.1/changelog.html)

\[v7.3.0\](https://jupyter-notebook.readthedocs.io/en/v7.3.0/changelog.html)

\[v7.2.2\](https://jupyter-notebook.readthedocs.io/en/v7.2.2/changelog.html)

\[v7.2.1\](https://jupyter-notebook.readthedocs.io/en/v7.2.1/changelog.html)

\[v7.2.0\](https://jupyter-notebook.readthedocs.io/en/v7.2.0/changelog.html)

\[v7.1.3\](https://jupyter-notebook.readthedocs.io/en/v7.1.3/changelog.html)

\[v7.1.2\](https://jupyter-notebook.readthedocs.io/en/v7.1.2/changelog.html)

\[v7.1.1\](https://jupyter-notebook.readthedocs.io/en/v7.1.1/changelog.html)

\[v7.0.8\](https://jupyter-notebook.readthedocs.io/en/v7.0.8/changelog.html)

\[v7.0.7\](https://jupyter-notebook.readthedocs.io/en/v7.0.7/changelog.html)

\[v7.0.6\](https://jupyter-notebook.readthedocs.io/en/v7.0.6/changelog.html)

\[v7.0.5\](https://jupyter-notebook.readthedocs.io/en/v7.0.5/changelog.html)

\[v7.0.4\](https://jupyter-notebook.readthedocs.io/en/v7.0.4/changelog.html)

\[v7.0.3\](https://jupyter-notebook.readthedocs.io/en/v7.0.3/changelog.html)

\[v7.0.2\](https://jupyter-notebook.readthedocs.io/en/v7.0.2/changelog.html)

\[v7.0.1\](https://jupyter-notebook.readthedocs.io/en/v7.0.1/changelog.html)

\[v7.0.0\](https://jupyter-notebook.readthedocs.io/en/v7.0.0/changelog.html)

\[v6.5.4\](https://jupyter-notebook.readthedocs.io/en/v6.5.4/changelog.html)

\[v6.5.3\](https://jupyter-notebook.readthedocs.io/en/v6.5.3/changelog.html)

\[v6.5.2\](https://jupyter-notebook.readthedocs.io/en/v6.5.2/changelog.html)

\[v6.5.1\](https://jupyter-notebook.readthedocs.io/en/v6.5.1/changelog.html)

\[v6.5.0\](https://jupyter-notebook.readthedocs.io/en/v6.5.0/changelog.html)

\[6.4.12\](https://jupyter-notebook.readthedocs.io/en/6.4.12/changelog.html)

\[v6.4.11\](https://jupyter-notebook.readthedocs.io/en/v6.4.11/changelog.html)

\[6.4.10\](https://jupyter-notebook.readthedocs.io/en/6.4.10/changelog.html)

\[v6.4.9\](https://jupyter-notebook.readthedocs.io/en/v6.4.9/changelog.html)

\[v6.4.8\](https://jupyter-notebook.readthedocs.io/en/v6.4.8/changelog.html)

\[v6.4.7\](https://jupyter-notebook.readthedocs.io/en/v6.4.7/changelog.html)

\[v6.4.6\](https://jupyter-notebook.readthedocs.io/en/v6.4.6/changelog.html)

\[v6.4.5\](https://jupyter-notebook.readthedocs.io/en/v6.4.5/changelog.html)

\[v6.4.4\](https://jupyter-notebook.readthedocs.io/en/v6.4.4/changelog.html)

\[6.2.0\](https://jupyter-notebook.readthedocs.io/en/6.2.0/changelog.html)

\[5.7.6\](https://jupyter-notebook.readthedocs.io/en/5.7.6/changelog.html)

\[5.7.5\](https://jupyter-notebook.readthedocs.io/en/5.7.5/changelog.html)

\[5.7.4\](https://jupyter-notebook.readthedocs.io/en/5.7.4/changelog.html)

\[5.7.3\](https://jupyter-notebook.readthedocs.io/en/5.7.3/changelog.html)

\[5.7.2\](https://jupyter-notebook.readthedocs.io/en/5.7.2/changelog.html)

\[5.7.1\](https://jupyter-notebook.readthedocs.io/en/5.7.1/changelog.html)

\[5.7.0\](https://jupyter-notebook.readthedocs.io/en/5.7.0/changelog.html)

\[5.6.0\](https://jupyter-notebook.readthedocs.io/en/5.6.0/changelog.html)

\[5.5.0\](https://jupyter-notebook.readthedocs.io/en/5.5.0/changelog.html)

\[5.4.1\](https://jupyter-notebook.readthedocs.io/en/5.4.1/changelog.html)

\[5.4.0\](https://jupyter-notebook.readthedocs.io/en/5.4.0/changelog.html)

\[5.3.1\](https://jupyter-notebook.readthedocs.io/en/5.3.1/changelog.html)

\[5.2.2\](https://jupyter-notebook.readthedocs.io/en/5.2.2/changelog.html)

\[5.1.0\](https://jupyter-notebook.readthedocs.io/en/5.1.0/changelog.html)

\[5.0.0\](https://jupyter-notebook.readthedocs.io/en/5.0.0/changelog.html)

\[4.x\](https://jupyter-notebook.readthedocs.io/en/4.x/changelog.html)

On Read the Docs

\[Project Home\](https://app.readthedocs.org/projects/jupyter-notebook/?utm\_source=jupyter-notebook&utm\_content=flyout)

\[Builds\](https://app.readthedocs.org/projects/jupyter-notebook/builds/?utm\_source=jupyter-notebook&utm\_content=flyout)

Search

\[Addons documentation\](https://docs.readthedocs.io/page/addons.html?utm\_source=jupyter-notebook&utm\_content=flyout) ― Hosted by \[Read the Docs\](https://about.readthedocs.com/?utm\_source=jupyter-notebook&utm\_content=flyout)

No recent searches

- \`Enter\` to select
- \`Up\` / \`Down\` to navigate
- \`Esc\` to close

Search powered by

\[!\[Read the Docs\](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB2ZXJzaW9uPSIxLjEiIGlkPSJzdmciIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4IiB2aWV3Qm94PSI2OTQgMTk3IDIwMDAgNDAwIj4KPGcgaWQ9ImxvZ28iIHRyYW5zZm9ybT0ibWF0cml4KDAuNTU3NTM2NDQsMCwwLDAuNTU3NTM2NDQsNjguMzA4MTM1LDEwNTAuMTI2MikiPgoJPHBhdGggc3R5bGU9ImZpbGw6IzMyMzIyQSIgZD0iTTE0MDguMS0xMTgxLjdjLTcuNSwxLTEyLjcsNy44LTExLjcsMTUuMyAgIGMwLjcsNS40LDQuNiw5LjksOS45LDExLjNjMCwwLDMzLjIsMTEsODkuNywxNS42YzQ1LjQsMy43LDk2LjktMy4yLDk2LjktMy4yYzcuNS0wLjIsMTMuNS02LjUsMTMuMi0xNHMtNi41LTEzLjUtMTQtMTMuMiAgIGMtMC45LDAtMS44LDAuMS0yLjYsMC4zYzAsMC01MC40LDYuMi05MS4zLDIuOWMtNTQtNC40LTgzLjQtMTQuMy04My40LTE0LjNDMTQxMi42LTExODEuNywxNDEwLjMtMTE4MiwxNDA4LjEtMTE4MS43eiAgICBNMTQwOC4xLTEyNDkuM2MtNy41LDEtMTIuNyw3LjgtMTEuNywxNS4zYzAuNyw1LjQsNC42LDkuOSw5LjksMTEuM2MwLDAsMzMuMiwxMSw4OS43LDE1LjZjNDUuNCwzLjcsOTYuOS0zLjIsOTYuOS0zLjIgICBjNy41LTAuMiwxMy41LTYuNSwxMy4yLTE0cy02LjUtMTMuNS0xNC0xMy4yYy0wLjksMC0xLjgsMC4xLTIuNiwwLjNjMCwwLTUwLjQsNi4yLTkxLjMsMi45Yy01NC00LjQtODMuNC0xNC4zLTgzLjQtMTQuMyAgIEMxNDEyLjYtMTI0OS4zLDE0MTAuMy0xMjQ5LjYsMTQwOC4xLTEyNDkuM3ogTTE0MDguMS0xMzE2LjljLTcuNSwxLTEyLjcsNy44LTExLjcsMTUuM2MwLjcsNS40LDQuNiw5LjksOS45LDExLjMgICBjMCwwLDMzLjIsMTEsODkuNywxNS42YzQ1LjQsMy43LDk2LjktMy4yLDk2LjktMy4yYzcuNS0wLjIsMTMuNS02LjUsMTMuMi0xNHMtNi41LTEzLjUtMTQtMTMuMmMtMC45LDAtMS44LDAuMS0yLjYsMC4zICAgYzAsMC01MC40LDYuMi05MS4zLDIuOWMtNTQtNC40LTgzLjQtMTQuMy04My40LTE0LjNDMTQxMi42LTEzMTYuOSwxNDEwLjMtMTMxNy4yLDE0MDguMS0xMzE2Ljl6IE0xNDA4LjEtMTM4NC40ICAgYy03LjUsMS0xMi43LDcuOC0xMS43LDE1LjNjMC43LDUuNCw0LjYsOS45LDkuOSwxMS4zYzAsMCwzMy4yLDExLDg5LjcsMTUuNmM0NS40LDMuNyw5Ni45LTMuMiw5Ni45LTMuMmM3LjUtMC4yLDEzLjUtNi41LDEzLjItMTQgICBzLTYuNS0xMy41LTE0LTEzLjJjLTAuOSwwLTEuOCwwLjEtMi42LDAuM2MwLDAtNTAuNCw2LjItOTEuMywyLjljLTU0LTQuNC04My40LTE0LjMtODMuNC0xNC4zICAgQzE0MTIuNi0xMzg0LjUsMTQxMC4zLTEzODQuNywxNDA4LjEtMTM4NC40eiBNMTMxMy40LTE0NTUuN2MtNzEsMC41LTk3LjUsMjIuMy05Ny41LDIyLjN2NTMwLjNjMCwwLDI1LjgtMjIuMywxMDktMTguOSAgIGM4My4yLDMuNCwxMDAuMywzMi42LDIwMi41LDM0LjZjMTAyLjIsMi4xLDEyNy45LTE1LjcsMTI3LjktMTUuN2wxLjUtNTQwLjZjMCwwLTQ2LDEzLTEzNS41LDEzLjdzLTExMS0yMi44LTE5My4yLTI1LjUgICBDMTMyMy0xNDU1LjYsMTMxOC4xLTE0NTUuNywxMzEzLjQtMTQ1NS43eiBNMTM3Mi44LTE0MjEuMWMwLDAsNDMsMTQuMiwxMjIuNSwxOC4yYzY3LjIsMy4zLDEzNC41LTYuNiwxMzQuNS02LjZ2NDgwLjUgICBjMCwwLTM0LjEsMTcuOS0xMTkuMywxMS44Yy02Ni00LjctMTM4LjctMjkuNy0xMzguNy0yOS43TDEzNzIuOC0xNDIxLjF6IE0xMzMxLjMtMTQwOC42YzcuNiwwLDEzLjcsNi4yLDEzLjcsMTMuNyAgIHMtNi4yLDEzLjctMTMuNywxMy43YzAsMC0yMi4zLDAuMS0zNS44LDEuNWMtMjIuOCwyLjMtMzguMywxMC42LTM4LjMsMTAuNmMtNi43LDMuNS0xNSwxLTE4LjUtNS43cy0xLTE1LDUuNy0xOC41YzAsMCwwLDAsMCwwICAgYzAsMCwyMC4yLTEwLjcsNDguNC0xMy41QzEzMDkuMS0xNDA4LjUsMTMzMS4zLTE0MDguNiwxMzMxLjMtMTQwOC42eiBNMTMxOC4xLTEzNDAuOGM3LjYtMC4yLDEzLjMsMCwxMy4zLDAgICBjNy41LDAuOSwxMi45LDcuOCwxMiwxNS4zYy0wLjgsNi4zLTUuNywxMS4yLTEyLDEyYzAsMC0yMi4zLDAuMS0zNS44LDEuNWMtMjIuOCwyLjMtMzguMywxMC42LTM4LjMsMTAuNmMtNi43LDMuNS0xNSwwLjktMTguNS01LjggICBjLTMuNS02LjctMC45LTE1LDUuOC0xOC41YzAsMCwyMC4yLTEwLjcsNDguNC0xMy41QzEzMDAuOS0xMzQwLjEsMTMxMC41LTEzNDAuNiwxMzE4LjEtMTM0MC44eiBNMTMzMS4zLTEyNzMuMyAgIGM3LjYsMCwxMy43LDYuMiwxMy43LDEzLjdjMCw3LjYtNi4yLDEzLjctMTMuNywxMy43YzAsMC0yMi4zLTAuMS0zNS44LDEuMmMtMjIuOCwyLjMtMzguMywxMC42LTM4LjMsMTAuNiAgIGMtNi43LDMuNS0xNSwwLjktMTguNS01LjhjLTMuNS02LjctMC45LTE1LDUuOC0xOC41YzAsMCwyMC4yLTEwLjcsNDguNC0xMy41QzEzMDkuMS0xMjczLjQsMTMzMS4zLTEyNzMuMywxMzMxLjMtMTI3My4zeiIvPgo8L2c+CjxnIGlkPSJ0ZXh0Ij4KCTxwYXRoIHN0eWxlPSJmaWxsOiMzMjMyMkEiIGQ9Ik0xMTI4LjYsNDkxLjlWNDcwbDguOS0wLjhjNS4yLTAuNSw3LjgtMy4xLDcuOC03LjZWMzM2bC0xNS40LTAuOHYtMjNoNzMuOCAgIGMyMC45LDAsMzYuOSwzLjksNDguMSwxMS42YzExLjIsNy43LDE2LjgsMjAuNSwxNi44LDM4LjFjMCwxMi4zLTMuMiwyMi4zLTkuNywzMC4zYy02LjMsNy45LTEzLjksMTMuNy0yMi43LDE3LjMgICBjNi41LDIuMywxMS42LDcuOCwxNS40LDE2LjVsMTkuNSw0Mi40bDE1LjQsMC41djIzaC02Ni44VjQ3MGw3LjgtMC44YzQuMS0wLjUsNi4yLTIuMiw2LjItNC45YzAtMS4xLTAuNC0yLjMtMS4xLTMuOGwtMTIuNy0yNyAgIGMtMi00LjUtNC4yLTcuNy02LjgtOS41Yy0yLjMtMi01LjgtMy0xMC4zLTNoLTI0LjZ2NDdsMTcuNiwwLjh2MjNMMTEyOC42LDQ5MS45IE0xMTc4LjMsMzk1LjRoMjMuNWMyMi4yLDAsMzMuMi05LjksMzMuMi0yOS43ICAgYzAtMTEuNC0zLTE4LjctOC45LTIyLjJjLTUuOC0zLjQtMTUuMS01LjEtMjguMS01LjFoLTE5LjdWMzk1LjQiLz4KCTxwYXRoIHN0eWxlPSJmaWxsOiMzMjMyMkEiIGQ9Ik0xMzU2LDM1MS45YzEzLjUsMCwyNC4yLDMuMywzMi4yLDEwYzcuOSw2LjUsMTEuOSwxNS43LDExLjksMjcuNmMwLDcuOS0xLjcsMTUtNS4xLDIxLjEgICBjLTMuNCw1LjktNy43LDEwLjYtMTIuNywxNC4xYy01LDMuNC0xMS4yLDYuMi0xOC40LDguNGMtMTIuMSwzLjYtMjUuNyw1LjQtNDAuOCw1LjRjMC41LDkuNSwzLjUsMTcuMyw4LjksMjMuMiAgIGM1LjQsNS44LDEzLjcsOC42LDI0LjksOC42YzExLjIsMCwyMi4zLTQsMzMuNS0xMS45bDEwLjMsMjEuOWMtMy42LDMuMi05LjcsNi42LTE4LjQsMTBjLTguNSwzLjQtMTguMiw1LjEtMjkuMiw1LjEgICBjLTIyLDAtMzguMS02LTQ4LjQtMTguMWMtMTAuMy0xMi4zLTE1LjQtMjktMTUuNC01MC4zYzAtMjEuMyw1LjktMzkuMSwxNy42LTUzLjVDMTMxOC41LDM1OS4xLDEzMzQuOSwzNTEuOSwxMzU2LDM1MS45ICAgIE0xMzQzLjYsNDEzLjhjNi43LTEuMywxMi44LTMuOSwxOC40LTcuOGM1LjYtNC4xLDguNC05LDguNC0xNC42YzAtMTEtNS40LTE2LjUtMTYuMi0xNi41Yy0xMC4xLDAtMTcuOCw0LjEtMjMuMiwxMi4yICAgYy01LjQsNy45LTguNCwxNy41LTguOSwyOC42QzEzMjkuOSw0MTUuNSwxMzM3LjEsNDE0LjksMTM0My42LDQxMy44Ii8+Cgk8cGF0aCBzdHlsZT0iZmlsbDojMzIzMjJBIiBkPSJNMTUyOS42LDM2MS40djEwMC41YzAsMi45LDAuNSw0LjksMS40LDUuOWMxLjEsMS4xLDIuOSwxLjcsNS40LDEuOWw4LjYsMC41djIxLjZoLTQzdi0xNS43ICAgbC0wLjgtMC4zYy05LDEzLTIxLjQsMTkuNS0zNywxOS41Yy0xOC40LDAtMzItNS45LTQwLjgtMTcuNmMtOC44LTExLjctMTMuMi0yNy43LTEzLjItNDguMWMwLTI0LjUsNS45LTQzLjYsMTcuOC01Ny4zICAgYzExLjktMTMuNywyOS43LTIwLjUsNTMuNS0yMC41QzE0OTYuOCwzNTEuOSwxNTEyLjksMzU1LjEsMTUyOS42LDM2MS40IE0xNDk4LjMsNDQ4Ljl2LTcwYy01LTIuMy0xMi0zLjUtMjAuOC0zLjUgICBjLTEyLjEsMC0yMC44LDQuOS0yNi4yLDE0LjZjLTUuNCw5LjctOC4xLDIyLjYtOC4xLDM4LjdjMCwyOS4yLDkuNCw0My44LDI4LjEsNDMuOGM3LjksMCwxNC40LTIuMywxOS41LTcgICBDMTQ5NS43LDQ2MC42LDE0OTguMyw0NTUuMSwxNDk4LjMsNDQ4LjkiLz4KCTxwYXRoIHN0eWxlPSJmaWxsOiMzMjMyMkEiIGQ9Ik0xNjE2LjMsMzUxLjljNy43LDAsMTUuMSwxLjEsMjIuMiwzLjJ2LTI3LjNjMC00LTIuMy02LjEtNy02LjVsLTExLjYtMC44di0yMS40aDUwLjN2MTY0LjMgICBjMC4yLDQuMSwyLjQsNi4yLDYuOCw2LjJsOS41LDAuNXYyMS42aC00My44VjQ3NmwtMC44LTAuM2MtOC4xLDEzLjItMjAuNCwxOS43LTM2LjgsMTkuN2MtMjAuNSwwLTM1LTYuOC00My4yLTIwLjUgICBjLTcuNi0xMi40LTExLjQtMjcuNy0xMS40LTQ1LjdjMC0yMy40LDUuOC00Mi4yLDE3LjMtNTYuMkMxNTc5LjMsMzU4LjksMTU5NS41LDM1MS45LDE2MTYuMywzNTEuOSBNMTYzOC40LDQ0OS44di03MCAgIGMtNi41LTIuOS0xMy4zLTQuMy0yMC41LTQuM2MtMTEuOSwwLTIwLjYsNC44LTI2LjIsMTQuM2MtNS40LDkuNi04LjEsMjEuNy04LjEsMzYuNWMwLDMwLjMsOS43LDQ1LjQsMjkuMiw0NS40ICAgYzcuNCwwLDEzLjUtMi4xLDE4LjQtNi4yQzE2MzYsNDYxLjEsMTYzOC40LDQ1NS45LDE2MzguNCw0NDkuOCIvPgoJPHBhdGggc3R5bGU9ImZpbGw6IzMyMzIyQSIgZD0iTTE3OTEuNyw0NzAuNmMwLDAtMTIuNSw0LjctMTkuMiw0LjdzLTkuMi0zLjMtOS4yLTExLjhjMC0zLjgsMC41LTguOCwxLjQtMTQuOWwxMC4yLTYzLjFoMzIuNiAgIGwyLjgtMTcuN2gtMzIuNmw1LjctMzQuNUwxNzYwLDMzOGwtNC43LDI5LjhsLTIzLjYsMi40bC0yLjYsMTUuNGgyMy40TDE3NDIsNDUxYy0wLjksNS40LTEuNCwxMC42LTEuNCwxNS4xICAgYzAsMTguNyw3LjgsMjguMSwyMy45LDI4LjFjMTMuMiwwLDMxLTEwLjksMzEtMTAuOUwxNzkxLjcsNDcwLjYiLz4KCTxwYXRoIHN0eWxlPSJmaWxsOiMzMjMyMkEiIGQ9Ik0xODY1LDMwOS44bC00My4zLDEuMmwtMi4xLDEzbDE5LjksNC43bC0yNiwxNjMuMmgyMi41bDcuOC00Mi42YzAsMCwxOC43LTY1LDQ5LjQtNjUgICBjOS41LDAsMTIuMyw2LjksMTIuMywxNS42YzAsMy4zLTAuNSw2LjktMC45LDEwLjRsLTEzLjUsODEuNmw0My4zLTIuNGwyLjEtMTNsLTE5LjktMy41bDEwLjYtNjYuMmMwLjctNSwxLjItOS43LDEuMi0xNCAgIGMwLTE3LTYuOS0yOC42LTI1LjgtMjguNmMtMzUuOSwwLTU0LjksNDUuNi01NS44LDQ4LjJMMTg2NSwzMDkuOCIvPgoJPHBhdGggc3R5bGU9ImZpbGw6IzMyMzIyQSIgZD0iTTIwMzUsNDY0LjdjMCwwLTIxLjUsMTAuNi0zOC44LDEwLjZjLTE3LjcsMC0yNi03LjgtMjYtMjQuNmMwLTMuMSwwLjItNi42LDAuNy0xMC4yICAgYzQ5LDAsODMtMTguNCw4My00NS42YzAtMTguNy0xNS4xLTMwLjctMzktMzAuN2MtMzcuNiwwLTY4LjMsMzguNS02OC4zLDg3LjVjMCwyNiwxNi42LDQyLjYsNDIuNiw0Mi42YzI3LjksMCw1My0xNy41LDUzLTE3LjUgICBMMjAzNSw0NjQuNyBNMTk3Myw0MjRjNi4xLTI0LjgsMjMuNC00Mi4xLDQwLjctNDIuMWMxMi4xLDAsMTcuNyw1LDE3LjcsMTUuNEMyMDMxLjUsNDEyLjksMjAwNi42LDQyNCwxOTczLDQyNCIvPgoJPHBhdGggc3R5bGU9ImZpbGw6IzMyMzIyQSIgZD0iTTIwOTMuNyw0OTEuOVY0NzBsOC45LTAuOGM1LjItMC41LDcuOC0zLjEsNy44LTcuNlYzMzZsLTE1LjQtMC44di0yM2g3NC4xICAgYzI2LjUsMCw0Ny4xLDcsNjEuOSwyMS4xYzE1LDE0LjEsMjIuNCwzNC45LDIyLjQsNjIuNGMwLDE3LjEtMi4zLDMyLjEtNi44LDQ0LjljLTQuNSwxMi42LTEwLjYsMjIuNS0xOC40LDI5LjcgICBjLTE1LjUsMTQuNC0zNC44LDIxLjYtNTcuOCwyMS42TDIwOTMuNyw0OTEuOSBNMjE0My40LDMzOC40VjQ2NmgyNy42YzE1LjUsMCwyNy42LTUuNiwzNi4yLTE2LjhjOC42LTExLjIsMTMtMjcuNCwxMy00OC43ICAgYzAtNDEuNC0xNy42LTYyLjItNTIuNy02Mi4ySDIxNDMuNCIvPgoJPHBhdGggc3R5bGU9ImZpbGw6IzMyMzIyQSIgZD0iTTIzMzAsNDcyLjJjMTkuNiwwLDI5LjUtMTUuOSwyOS41LTQ3LjZjMC0xNi0yLjMtMjguMi02LjgtMzYuNWMtNC4zLTguMy0xMS43LTEyLjQtMjIuMi0xMi40ICAgYy0xMC4zLDAtMTcuOCw0LTIyLjcsMTEuOWMtNC45LDcuOS03LjMsMTguNy03LjMsMzIuNGMwLDI1LjQsNC43LDQxLjQsMTQuMSw0Ny44QzIzMTguOCw0NzAuNywyMzIzLjksNDcyLjIsMjMzMCw0NzIuMiAgICBNMjI2Ny45LDQyMy44YzAtMTMuMywyLTI0LjksNS45LTM0LjZjNC05LjksOS4zLTE3LjUsMTUuOS0yMi43YzEyLjgtOS43LDI2LjktMTQuNiw0Mi40LTE0LjZjMTAuOCwwLDE5LjksMS44LDI3LjMsNS40ICAgYzcuNiwzLjQsMTMuNCw3LjUsMTcuNiwxMi4yYzQuMyw0LjUsNy45LDExLjIsMTAuOCwyMGMzLjEsOC42LDQuNiwxOC45LDQuNiwzMC44YzAsMjQuOS02LDQzLjctMTguMSw1Ni41ICAgYy0xMi4xLDEyLjgtMjcuNiwxOS4yLTQ2LjUsMTkuMmMtMTguNywwLTMzLjQtNi00NC4xLTE4LjFDMjI3My4yLDQ2NS42LDIyNjcuOSw0NDcuNiwyMjY3LjksNDIzLjgiLz4KCTxwYXRoIHN0eWxlPSJmaWxsOiMzMjMyMkEiIGQ9Ik0yNDM4LjIsNDIyLjVjMCwxNS4zLDIuOSwyNy4yLDguNiwzNS43YzUuOCw4LjUsMTQuMSwxMi43LDI0LjksMTIuN2MxMSwwLDIxLjgtMy45LDMyLjQtMTEuNiAgIGwxMS42LDIwLjhjLTEyLjgsMTAuNS0yOC44LDE1LjctNDguMSwxNS43Yy0xOS4zLDAtMzQuNS02LTQ1LjctMTguMWMtMTEtMTIuMy0xNi41LTMwLjMtMTYuNS01NC4xczYuMy00MS42LDE4LjktNTMuNSAgIGMxMi44LTEyLjEsMjcuMS0xOC4xLDQzLTE4LjFjMTYsMCwzMC45LDMuNyw0NC42LDExLjF2MzUuMWwtMjQuOSwxLjl2LTEzYzAtNC45LTEuOC03LjgtNS40LTguOWMtMy40LTEuMy03LTEuOS0xMC44LTEuOSAgIEMyNDQ5LjEsMzc2LjIsMjQzOC4yLDM5MS42LDI0MzguMiw0MjIuNSIvPgoJPHBhdGggc3R5bGU9ImZpbGw6IzMyMzIyQSIgZD0iTTI1OTIuOSwzNzYuNWMtNC4zLTEuNi05LjYtMi40LTE1LjctMi40Yy02LjEsMC0xMS4xLDEuNC0xNC45LDQuM2MtMy42LDIuNy01LjQsNi4xLTUuNCwxMC4zICAgYzAsNCwwLjYsNy4xLDEuOSw5LjVjMS40LDIuMiwzLjYsNC4xLDYuNSw1LjdjNC41LDIuMyw5LjksNC40LDE2LjIsNi4yYzYuMywxLjYsMTEsMywxNC4xLDQuMWMzLjEsMC45LDYuOCwyLjUsMTEuNCw0LjkgICBjNC43LDIuMyw4LjIsNC45LDEwLjUsNy42YzYuMyw2LjcsOS41LDE1LjIsOS41LDI1LjdjMCwxMy41LTUsMjQuMS0xNC45LDMxLjljLTkuNyw3LjYtMjIuMiwxMS40LTM3LjMsMTEuNCAgIGMtMjIsMC0zOC42LTIuOC00OS43LTguNHYtMzcuNmwyNC4zLTEuOXYxM2MwLDcuOSw3LjYsMTEuOSwyMi43LDExLjlzMjIuNy01LjUsMjIuNy0xNi41YzAtNC0xLjQtNy4yLTQuMS05LjcgICBjLTIuNS0yLjUtNS00LjItNy42LTUuMWMtMi41LTAuOS01LjYtMS44LTkuMi0yLjdjLTMuNC0wLjktNi44LTEuOC0xMC4zLTIuN2MtMy4yLTAuOS02LjgtMi4xLTEwLjgtMy41Yy0zLjgtMS42LTgtMy45LTEyLjctNi44ICAgYy05LjItNS45LTEzLjgtMTUuOS0xMy44LTI5LjdjMC0xNC4xLDUtMjQuOSwxNC45LTMyLjRjOS45LTcuNiwyMi4zLTExLjQsMzcuMy0xMS40YzE1LjEsMCwzMC4xLDMuNiw0NC45LDEwLjh2MzIuNGwtMjQuMywxLjkgICB2LTExLjRDMjU5OS4xLDM4MS4yLDI1OTcsMzc4LjEsMjU5Mi45LDM3Ni41Ii8+CjwvZz4KPGRpdiB4bWxucz0iIiBpZD0ic2FrYS1ndWktcm9vdCI+PGRpdj48ZGl2PjxzdHlsZS8+PC9kaXY+PC9kaXY+PC9kaXY+PC9zdmc+)\](https://about.readthedocs.com/?utm\_source=jupyter-notebook&utm\_content=search)

