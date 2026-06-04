---
sourceFile: "Using the VS Code extension with self-signed certificates - GitLab Docs"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.824Z"
---

# Using the VS Code extension with self-signed certificates - GitLab Docs

d9e2930a-57a2-497c-a141-926959e87900

Using the VS Code extension with self-signed certificates - GitLab Docs

391c685c-019f-4229-828c-6a44f6b3416d

https://docs.gitlab.com/editor\_extensions/visual\_studio\_code/ssl/

Using the VS Code extension with self-signed certificates | GitLab Docs

Skip to main content

https://docs.gitlab.com/editor\_extensions/visual\_studio\_code/ssl/#skipTarget

Go to GitLab Docs homepage

https://docs.gitlab.com/

What's new?

https://about.gitlab.com/releases/whats-new/

19.0 (not yet released)

https://docs.gitlab.com/editor\_extensions/visual\_studio\_code/ssl/

18.11 (recently released)

https://docs.gitlab.com/18.11/editor\_extensions/visual\_studio\_code/ssl/

https://docs.gitlab.com/18.10/editor\_extensions/visual\_studio\_code/ssl/

https://archives.docs.gitlab.com/18.9/editor\_extensions/visual\_studio\_code/ssl/

https://archives.docs.gitlab.com/17.11/editor\_extensions/visual\_studio\_code/ssl/

https://archives.docs.gitlab.com/16.11/ee/editor\_extensions/visual\_studio\_code/ssl.html

https://docs.gitlab.com/archives

Select theme and layout

Fixed width

Fluid width

What's new?

https://about.gitlab.com/releases/whats-new/

Get free trial

https://gitlab.com/-/trial\_registrations/new?glm\_source=docs.gitlab.com&glm\_content=navigation-cta-docs

Toggle menu

https://docs.gitlab.com/user/

https://docs.gitlab.com/user/gitlab\_duo/

https://docs.gitlab.com/orbit/

https://docs.gitlab.com/api/

https://docs.gitlab.com/install/

https://docs.gitlab.com/administration/

https://docs.gitlab.com/subscriptions/

https://docs.gitlab.com/development/

https://docs.gitlab.com/solutions/

Select a topic

Getting started

https://docs.gitlab.com/api/get\_started/get\_started\_extending/

https://docs.gitlab.com/tutorials/develop/

Integrations

https://docs.gitlab.com/integration/

https://docs.gitlab.com/user/project/integrations/webhooks/

https://docs.gitlab.com/api/rest/

GraphQL API

https://docs.gitlab.com/api/graphql/

OAuth 2.0 identity provider API

https://docs.gitlab.com/api/oauth2/

GitLab Duo CLI (duo)

https://docs.gitlab.com/user/gitlab\_duo\_cli/

GitLab CLI (glab)

https://docs.gitlab.com/cli/

Editor and IDE extensions

https://docs.gitlab.com/editor\_extensions/

Visual Studio Code

https://docs.gitlab.com/editor\_extensions/visual\_studio\_code/

Install and set up

https://docs.gitlab.com/editor\_extensions/visual\_studio\_code/setup/

Work with projects

https://docs.gitlab.com/editor\_extensions/visual\_studio\_code/projects/

CI/CD pipelines

https://docs.gitlab.com/editor\_extensions/visual\_studio\_code/cicd/

Security scanning

https://docs.gitlab.com/editor\_extensions/visual\_studio\_code/security\_scanning/

Custom queries

https://docs.gitlab.com/editor\_extensions/visual\_studio\_code/custom\_queries/

GitLab remote URL format

https://docs.gitlab.com/editor\_extensions/visual\_studio\_code/remote\_urls/

Settings and commands

https://docs.gitlab.com/editor\_extensions/visual\_studio\_code/settings/

Troubleshooting

https://docs.gitlab.com/editor\_extensions/visual\_studio\_code/troubleshooting/

Using with self-signed certificates

https://docs.gitlab.com/editor\_extensions/visual\_studio\_code/ssl/

JetBrains IDEs

https://docs.gitlab.com/editor\_extensions/jetbrains\_ide/

Visual Studio

https://docs.gitlab.com/editor\_extensions/visual\_studio/

https://docs.gitlab.com/editor\_extensions/eclipse/

https://docs.gitlab.com/editor\_extensions/neovim/

Language Server

https://docs.gitlab.com/editor\_extensions/language\_server/

Security considerations

https://docs.gitlab.com/editor\_extensions/security\_considerations/

Show more breadcrumbs

GitLab Docs

https://docs.gitlab.com/

https://docs.gitlab.com/api/

Editor and IDE extension…

https://docs.gitlab.com/editor\_extensions/

Visual Studio Code

https://docs.gitlab.com/editor\_extensions/visual\_studio\_code/

Using with self-signed certificates

https://docs.gitlab.com/editor\_extensions/visual\_studio\_code/ssl/

Using the VS Code extension with self-signed certificates

You can still use the GitLab for VS Code extension even if your GitLab instance uses a self-signed SSL certificate.

If you also use a proxy to connect to your GitLab instance, let us know in

https://gitlab.com/gitlab-org/gitlab-vscode-extension/-/issues/314

. If you still have connection problems after completing these steps, review

https://gitlab.com/groups/gitlab-org/-/epics/6244

, which links to all existing SSL issues for the GitLab for VS Code extension.

Use the extension with a self-signed CA

#### Prerequisites:

Your GitLab instance uses a certificate signed with a self-signed certificate authority (CA).

Your GitLab for VS Code version is 6.51.1 or later.

Your VS Code version is 1.101.2 (May 2025) or later.

VS Code setting is

Ensure your CA certificate is correctly added to your system for the extension to work. VS Code reads the system certificate store, and changes all node

requests to trust the certificates:

Self-signed certificate chainShows a self-signed CA that signs the GitLab instance certificate.#mermaid-1778825688403{font-family:GitLab Sans;font-size:16px;fill:#000000;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-1778825688403 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-1778825688403 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-1778825688403 .error-icon{fill:#552222;}#mermaid-1778825688403 .error-text{fill:#552222;stroke:#552222;}#mermaid-1778825688403 .edge-thickness-normal{stroke-width:1px;}#mermaid-1778825688403 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-1778825688403 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-1778825688403 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-1778825688403 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-1778825688403 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-1778825688403 .marker{fill:#666;stroke:#666;}#mermaid-1778825688403 .marker.cross{stroke:#666;}#mermaid-1778825688403 svg{font-family:GitLab Sans;font-size:16px;}#mermaid-1778825688403 p{margin:0;}#mermaid-1778825688403 .label{font-family:GitLab Sans;color:#000000;}#mermaid-1778825688403 .cluster-label text{fill:#333;}#mermaid-1778825688403 .cluster-label span{color:#333;}#mermaid-1778825688403 .cluster-label span p{background-color:transparent;}#mermaid-1778825688403 .label text,#mermaid-1778825688403 span{fill:#000000;color:#000000;}#mermaid-1778825688403 .node rect,#mermaid-1778825688403 .node circle,#mermaid-1778825688403 .node ellipse,#mermaid-1778825688403 .node polygon,#mermaid-1778825688403 .node path{fill:#eee;stroke:#999;stroke-width:1px;}#mermaid-1778825688403 .rough-node .label text,#mermaid-1778825688403 .node .label text,#mermaid-1778825688403 .image-shape .label,#mermaid-1778825688403 .icon-shape .label{text-anchor:middle;}#mermaid-1778825688403 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-1778825688403 .rough-node .label,#mermaid-1778825688403 .node .label,#mermaid-1778825688403 .image-shape .label,#mermaid-1778825688403 .icon-shape .label{text-align:center;}#mermaid-1778825688403 .node.clickable{cursor:pointer;}#mermaid-1778825688403 .root .anchor path{fill:#666!important;stroke-width:0;stroke:#666;}#mermaid-1778825688403 .arrowheadPath{fill:#333333;}#mermaid-1778825688403 .edgePath .path{stroke:#666;stroke-width:2.0px;}#mermaid-1778825688403 .flowchart-link{stroke:#666;fill:none;}#mermaid-1778825688403 .edgeLabel{background-color:white;text-align:center;}#mermaid-1778825688403 .edgeLabel p{background-color:white;}#mermaid-1778825688403 .edgeLabel rect{opacity:0.5;background-color:white;fill:white;}#mermaid-1778825688403 .labelBkg{background-color:rgba(255, 255, 255, 0.5);}#mermaid-1778825688403 .cluster rect{fill:hsl(0, 0%, 98.9215686275%);stroke:#707070;stroke-width:1px;}#mermaid-1778825688403 .cluster text{fill:#333;}#mermaid-1778825688403 .cluster span{color:#333;}#mermaid-1778825688403 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:GitLab Sans;font-size:12px;background:hsl(-160, 0%, 93.3333333333%);border:1px solid #707070;border-radius:2px;pointer-events:none;z-index:100;}#mermaid-1778825688403 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#000000;}#mermaid-1778825688403 rect.text{fill:none;stroke-width:0;}#mermaid-1778825688403 .icon-shape,#mermaid-1778825688403 .image-shape{background-color:white;text-align:center;}#mermaid-1778825688403 .icon-shape p,#mermaid-1778825688403 .image-shape p{background-color:white;padding:2px;}#mermaid-1778825688403 .icon-shape rect,#mermaid-1778825688403 .image-shape rect{opacity:0.5;background-color:white;fill:white;}#mermaid-1778825688403 .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-1778825688403 .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-1778825688403 :root{--mermaid-font-family:GitLab Sans;}
signed
Self-signed CA
Your GitLab instance certificate

The GitLab instance certificate's CA must be explicitly specified as a trusted CA. If intermediate certificates are in use, these must be available on the system. If the entire chain does not validate successfully, network connections within the extension fail to authenticate. For more information, see

Self-signed certificate error when installing Python support in WSL

https://github.com/microsoft/vscode/issues/131836#issuecomment-909983815

in the Visual Studio Code issue tracker.

2. In your VS Code

settings.json

"http.systemCertificates": true

. The default value is

, so you might not need to change this value.

3. Complete the instructions in the following sections for your operating system.

These instructions were tested on Windows 10 and VS Code 1.60.0.

#### Make sure you can see your self-signed CA in your certificate store:

Open the command prompt.

Make sure you see your certificate in

Trusted Root Certification Authorities

Certificates

#### These instructions were tested on Arch Linux

5.14.3-arch1-1

and VS Code 1.60.0.

Use your operating system's tools to confirm you can add our self-signed CA to your system:

update-ca-trust

(Fedora, RHEL, CentOS)

update-ca-certificates

(Ubuntu, Debian, OpenSUSE, SLES)

Confirm the CA certificate is in

/etc/ssl/certs/ca-certificates.crt

/etc/ssl/certs/ca-bundle.crt

checks this location

https://github.com/microsoft/vscode/issues/131836#issuecomment-909983815

These instructions were tested on macOS Tahoe 26, VS Code 1.101.2, and GitLab for VS Code 6.51.1.

#### Make sure you see the self-signed CA in your keychain:

Applications

Keychain Access

In the left-hand column, select

Find your self-signed CA certificate in the list.

Right-click the certificate and select

Secure Sockets Layer (SSL)

option is set to 'Always Trust'.

Was this page helpful? Yes No

Edit this page

View page source Edit this file only.

https://gitlab.com/gitlab-org/gitlab/-/blob/master/doc/editor\_extensions/visual\_studio\_code/ssl.md

Open in Web IDE Edit multiple files.

https://gitlab.com/-/ide/project/gitlab-org/gitlab/edit/master/-/doc/editor\_extensions/visual\_studio\_code/ssl.md

Create an issue Suggest improvements.

https://gitlab.com/gitlab-org/gitlab/-/issues/new?issuable\_template=Documentation

Copy for LLM

Use the extension with a self-signed CA

https://docs.gitlab.com/editor\_extensions/visual\_studio\_code/ssl/#use-the-extension-with-a-self-signed-ca

https://docs.gitlab.com/editor\_extensions/visual\_studio\_code/ssl/#windows

https://docs.gitlab.com/editor\_extensions/visual\_studio\_code/ssl/#linux

https://docs.gitlab.com/editor\_extensions/visual\_studio\_code/ssl/#macos

https://www.facebook.com/gitlab

https://www.linkedin.com/company/gitlab-com

https://twitter.com/gitlab

https://www.youtube.com/channel/UCnMGQ8QHMAnVIsI3xJrihhg

About GitLab

https://about.gitlab.com/company/

View pricing

https://about.gitlab.com/pricing/

Try GitLab for free

https://about.gitlab.com/free-trial/

View page source

https://gitlab.com/gitlab-org/gitlab/-/blob/master/doc/editor\_extensions/visual\_studio\_code/ssl.md

Edit in Web IDE

https://gitlab.com/-/ide/project/gitlab-org/gitlab/edit/master/-/doc/editor\_extensions/visual\_studio\_code/ssl.md

Contribute to GitLab

https://about.gitlab.com/community/contribute/

Suggest updates

https://gitlab.com/gitlab-org/gitlab/-/issues/new?issuable\_template=Documentation

Help & Community

Get certified

https://university.gitlab.com/pages/certifications

Get support

https://about.gitlab.com/support/

Post on the GitLab forum

https://forum.gitlab.com/new-topic?title=topic%20title&body=topic%20body&tags=docs-feedback

https://about.gitlab.com/terms/

Privacy statement

https://about.gitlab.com/privacy/

Use of generative AI

https://docs.gitlab.com/legal/use\_generative\_ai/

Acceptable use of user licenses

https://docs.gitlab.com/legal/licensing\_policy/

Cookie Preferences

Privacy Preference Center

Privacy Preference Center

Your Privacy

Your Privacy

When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer.

Cookie Policy

https://about.gitlab.com/privacy/cookies/

ed9cba76-0839-4728-b7b4-1e098dcc365d

This User ID will be used as a unique identifier while storing and accessing your preferences for future.

Strictly Necessary Cookies

Strictly Necessary Cookies

Always Active These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, enabling you to securely log into the site, filling in forms, or using the customer checkout. GitLab processes any personal data collected through these cookies on the basis of our legitimate interest. Cookies Details

Functionality Cookies

Functionality Cookies

\[x\]  Functionality Cookies These cookies enable helpful but non-essential website functions that improve your website experience. By recognizing you when you return to our website, they may, for example, allow us to personalize our content for you or remember your preferences. If you do not allow these cookies then some or all of these services may not function properly. GitLab processes any personal data collected through these cookies on the basis of your consent Cookies Details

Performance and Analytics Cookies

Performance and Analytics Cookies

\[x\]  Performance and Analytics Cookies These cookies allow us and our third-party service providers to recognize and count the number of visitors on our websites and to see how visitors move around our websites when they are using it. This helps us improve our products and ensures that users can easily find what they need on our websites. These cookies usually generate aggregate statistics that are not associated with an individual. To the extent any personal data is collected through these cookies, GitLab processes that data on the basis of your consent. Cookies Details

Targeting and Advertising Cookies

Targeting and Advertising Cookies

\[x\]  Targeting and Advertising Cookies These cookies enable different advertising related functions. They may allow us to record information about your visit to our websites, such as pages visited, links followed, and videos viewed so we can make our websites and the advertising displayed on it more relevant to your interests. They may be set through our website by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other websites. GitLab processes any personal data collected through these cookies on the basis of your consent. Cookies Details

Ad User Data

Ad User Data

\[x\]  Ad User Data Sets consent for sending user data to Google for advertising purposes. Cookies Details

Ad Personalization

Ad Personalization

\[x\]  Ad Personalization Sets consent for personalized advertising. Cookies Details

Cookie List

Consent Leg.Interest

checkbox label label

checkbox label label

checkbox label label

checkbox label label

Apply Cancel

Confirm My Choices

0cAFcWeA4SDY61pyh84SsJYsc\_eXOeU1DFqu3znsWHLn7yuv3I\_4obWyGFs361tP7om8b6-XruLOSNiUYR-lVNAo0hS6mFyFrBzNO5biJlCRCfmeWkikDtGLzSd-S\_O4wfWI4jlk21CPzEuhW2HpU9CEEZE3eiAN6Y6BLqX45jbKq1PQ70dbgxyTd4qtvWEQ\_GfxUn1\_vn4FLpJsLDT9MQvHuK0D\_bUr\_\_B7C85kuiP5pjd6BqEqxkcquwfXUXVn9MqPmYvtlzu0NRCCVIBrzH8qymNu6Rvdsoe8bHckay9KCO5ATQNyLAaymH75pWiUYx5HY0xGBP3UsEXb77VHnjjh5DHiVKjzKJmX5mc6KoehoqFxKzBt4qkGiczryQWKWuZGD1MLnWzb4uJoqvAtCq6t\_EPwqi6dyFGYBxxtbR9KnYPM15szd5YIO\_KhrL2DxHP9IagW5xJvB98DBelZWcc7t8A\_GIYv9EF3bjBH4us3d4p0o3X5uhfdTPz-oFF2M4bAs1aOkVjWn19tPpwqoSfrR5o0s7P1aJoZepl-7sEqGk2AYyY-yhbfionOQV5P\_j5NQYNTvfgGv1bvcU3pBQcDYAy-wGA9UJ8dE-Bkm4BZS2j-EF2Fn05Hs2h0oP52SSmWh9\_DqhGQUvs-AON9ftorqamO14Mp8E57UR6ZSy3od05gGFyL1uryu2CgqhgHbwig2mO9jY7DxQ\_O9SBCIqOazBsT2HOXZqxDFJNoElC\_58-fw4q6z3Xswd5c3\_8V8KwaWo8XkCEhF0dCQoYFVpfHbRK6Lb9qn-nu7CK9tWMPylZIHrJqVvZqLjzOuK1\_UWFq3\_XsuGZLg3W-UfUQmurc3LS6O0SL1XcW85uHZvW9-a8VVM3ZvHtbJtJH84fLGSmteR20S-b7PXcRubISOZYPE2UJXwOTIiCaep8kFahsQC2HjSs0-2IErfVqLhaQf8VCbSUfAROvzBKjyvtguyGDdK895xYeZKx\_EmRUueVFYYrzARk0\_pk0HTZD0SgKRCCJKcI1kIpZWJGibVOnTFLldNH3xAMJXTETW6W\_qL5wwHZLU3goGEpSjyP1scVrMOMljB01Xy-H1SBT9SNqnlpM515oDOq1S5B\_lli0eu23KxfBd7CBuUT\_w7mfngv25EK1A0WRpIXlrfXGVechdQwYk7vdBm0nK8shyhMOnPI2u-5xngnJ7n\_AmhrXM6OaUn0\_uB1hXZR6OX5w\_dIjOsWiiLEVE0OS8wm8v6gI1gdgx6pIvFnEvrE3Joe-LxYByFcqE6X3sDSkpqLAyXBcllrq4mmWjasJp25S5XkJ1gWU6MlFuoK4rCNAY\_2CgMJhgyZEUNUikLUADc2z\_vXlir6TH60TNzd9zlLEyaRLmccOG2qG55cRQCj777qWxcq-HK2ZeOk2YiVH1ThuFJxlpOCALams8t0B5AB8pMuePRQXAQI-P4L8DwxpderbMgQhyFjfgsAxJaooBggYPCTJc0LHTYjf\_tm2T3e9CW7acS367iHnLAT9Fb6ttcqO\_CnElzOGp5n1sLnaVIO4PNJM4l3z0o5KgdEhOFl-Jnh52ydHSu0AQaNlhW2trWyCKmqkZTtfxdG4fZT\_yt4QkBDjyCG6RoylMjzYX-eLWUhqD9HsOPqsEdlea\_NLQW2ID362jDIFVebPno2UtxRpYzKvl2wCnAfLjZlWGscFc8oNO2OaADdivZuxgHuIlefaNK7O5tIpwM9HrdmsnIh4wlXhEdRJHh1EcpcutCi2oOGL1iKI0\_WPY0RKPAGccb2gthBUau\_26ONRxIZMgVeh4Ctmph2gBhSDS7r\_-1D7uH17seifDWMhyoQYteJLSYBiC55JiiV8nB-zCfOr77VPx-UZJQ1SCgKY09GDH7ejXJllirEXNM-fRDKI9S5GS6Mb5ey05Y4hEgODbmHl0vmxHj2V4vQLGyFSzYV8zuzOYgJahVxGMwp6QDX6vTmG1CVD35S7DAbUdnZMwPNiInK7gva9WVuyEuPeVc3t6PVTd6qIRhAqQ4HRDOd1pcXBY2YC3ArFT2UUAx9eKfLaGN55PLQCuYtNMA4UEQ6TBG9BnkMMfKyt-DkoGbnB9MUqDtQ8YFaM5mYuxU7qI3Ek1-CjTy87mk8ofJK697eM7ye1kxnqUKVz\_xaNyfDxvMgyjty4YY0qsTrgQKpgIbpFe1puICR8\_YwY03h7QevHsR6hNOtcsvyWhi5hiRWWW9uFk

