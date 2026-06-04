---
sourceFile: "Technical Evolution of System Certificate Authority Integration in Modern JavaScript Runtimes and IDE Architectures"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.730Z"
---

# Technical Evolution of System Certificate Authority Integration in Modern JavaScript Runtimes and IDE Architectures

64394357-785f-4309-96fc-452ce95de333

Technical Evolution of System Certificate Authority Integration in Modern JavaScript Runtimes and IDE Architectures

0c03641a-d291-49c6-b82f-dbb6ab7140cd

Technical Evolution of System Certificate Authority Integration in Modern JavaScript Runtimes and IDE Architectures

The architectural transition from static, bundled certificate authority snapshots to dynamic, operating system-integrated trust models represents a significant shift in the security posture of modern software development environments. Historically, JavaScript runtimes like Node.js maintained a strict isolation from the host operating system's cryptographic stores to ensure cross-platform predictability. However, as enterprise network environments become increasingly complex—characterized by SSL-intercepting proxies, private Public Key Infrastructures (PKI), and rigorous compliance requirements—the limitations of this isolationist approach have become evident. The introduction of the

http.systemCertificatesNode

configuration in Visual Studio Code and the corresponding

--use-system-ca

flag in Node.js version 22 and higher addresses these challenges by facilitating a deeper synergy between the runtime environment and the native security frameworks of Windows, macOS, and Linux.\[1, 2\]

The Historical Paradigms of Node.js Certificate Management

For over a decade, Node.js adopted a design philosophy that prioritized consistency above system integration. By compiling a snapshot of the Mozilla CA trust store directly into the binary, typically defined within

src/node\_root\_certs.h

, Node.js ensured that TLS connections would behave identically whether they originated from a server in a public cloud or a developer's local workstation.\[3, 4\] This bundled approach simplified distribution but created significant friction in organizational settings. Administrators were frequently forced to manage trust manually using the

NODE\_EXTRA\_CA\_CERTS

environment variable, a mechanism that requires developers to point the runtime to a PEM-encoded file containing additional root or intermediate certificates.\[5, 6\]

The inherent difficulty of this legacy model is most apparent in large-scale corporate environments. In such settings, certificates are often distributed and updated automatically via Group Policy Objects (GPO) on Windows or Configuration Profiles on macOS. Because Node.js did not historically consult the Windows Certificate Store or the macOS Keychain, developers were required to manually extract these certificates and update their environment variables whenever the corporate PKI rotated a root or intermediate key.\[7, 8\] Failure to do so resulted in frequent and frustrating errors, such as

UNABLE\_TO\_VERIFY\_LEAF\_SIGNATURE

or the ubiquitous

self signed certificate in certificate chain

, particularly when attempting to connect to internal resources, corporate proxies, or private npm registries.\[2, 9\]

Architectural Integration of Native Trust Stores

The evolution toward system-level trust integration began with the recognition that the operating system should serve as the "source of truth" for security policy. Node.js version 22 introduced formal, native support for loading system certificates, a feature controlled by the

--use-system-ca

flag.\[1, 2\] This implementation relies on platform-specific APIs to enumerate and ingest certificates from the host's native stores, bridging the gap between the application runtime and the OS security layer.

Platform-Specific Retrieval Mechanisms

The complexity of implementing system-wide trust is rooted in the disparate ways operating systems manage cryptographic materials. Node.js implements a strategy similar to Chromium's certificate policy, utilizing native libraries to access the respective stores of each major platform.

Operating System

Implementation Mechanism

Primary Certificate Store

Windows Crypto API

Trusted Root Certification Authorities

Security.framework / Keychain Access

System and System Roots Keychains

OpenSSL Default Paths

/etc/ssl/certs

/etc/pki/ca-trust

On Windows, the implementation utilizes the Windows Crypto API to query the certificate store for roots that are trusted for server authentication.\[2, 7\] This is particularly critical for handling security appliances like ESET SSL protection or Zscaler proxies, which inject their own certificates into the Windows store to facilitate traffic inspection.\[7\] On macOS, the runtime interacts with the

Security.framework

to enumerate items in the Keychain, specifically identifying certificates that the user has marked as "Always Trust".\[10, 11\] Linux implementations remain somewhat more traditional, relying on the standard OpenSSL paths such as

SSL\_CERT\_FILE

SSL\_CERT\_DIR

, which are typically managed by distribution-level tools like

update-ca-certificates

update-ca-trust

Performance and Off-Thread Enumeration

A primary technical challenge in loading system certificates is the potential impact on application startup time. In enterprise environments, a system trust store may contain hundreds or even thousands of certificates, including numerous duplicates and legacy roots. To mitigate this, recent enhancements to Node.js (tracked under issue #58990) have moved the enumeration and parsing of system certificates off the main event loop thread.\[12\] This off-thread loading ensures that applications remain responsive even as the TLS subsystem performs the computationally expensive task of deserializing and validating the system's root certificates.\[12, 13\]

Visual Studio Code and the Experimental Extension Host Logic

Visual Studio Code, as an application built upon the Electron framework, inherits the complexities of both the Chromium network stack and the Node.js runtime. The "Extension Host" is a dedicated Node.js process where all third-party extension code is executed to preserve the stability of the main UI thread.\[14, 15\] Given that modern extensions—ranging from AI assistants like GitHub Copilot to cloud-based development tools like GitLab for VS Code—rely heavily on network connectivity, the handling of TLS certificates within this process is paramount.\[10, 16\]

The Role of http.systemCertificatesNode

The setting

http.systemCertificatesNode

is an experimental toggle in Visual Studio Code that enables the loading of system certificates specifically using the new native Node.js support, rather than the legacy proxy-based certificate handling implemented in earlier versions of the IDE.\[1\] This setting serves as a critical testbed for evaluating the reliability of the Node.js

--use-system-ca

implementation within the context of a highly complex, multi-platform application.

The telemetry collected by Visual Studio Code through the

additionalCertificates

event provides an empirical look at the success and failure rates of certificate loading across the global user base.\[1\] This data is used to determine whether the native Node.js path is sufficiently stable to eventually become the default behavior for all users. Currently, the setting defaults to

in stable releases, requiring an explicit opt-in from users who need system-level trust or who wish to participate in the experimental feedback loop.\[1\]

Comparative Setting Framework

Visual Studio Code provides several overlapping settings to manage certificate trust, which can occasionally lead to confusion in enterprise deployments.

VS Code Setting

Internal Mechanism

Intended Scope

http.systemCertificates

VS Code Custom Proxy Logic

Main process and standard extension requests.

http.systemCertificatesNode

Native Node.js

--use-system-ca

Experimental Node.js-native loading in the Extension Host.

http.proxyStrictSSL

Verification Bypass

Disabling validation (unstable/insecure).

http.systemCertificates

has been available for some time and handles general system-wide trust,

http.systemCertificatesNode

represents a more granular attempt to align the Extension Host directly with the evolving capabilities of the underlying Node.js runtime.\[1\]

Forensic Analysis of the macOS Extension Host Regressions

The risks inherent in moving from a controlled, bundled trust store to a dynamic, system-integrated model were highlighted during the release of Visual Studio Code version 1.106. Shortly after the update, a significant number of macOS users reported that the Extension Host was crashing immediately upon startup with exit code 6.\[1, 17, 18\] These crashes were persistent, surviving reinstallation and the clearing of extension caches, and effectively crippled the editor's functionality.\[1\]

DER Decoding Failures and Memory Safety

The root cause of the crashes was identified as a native failure within the Node.js certificate parsing logic. Specifically, the bump to Node.js version 22.20 in the Visual Studio Code 1.106 build introduced changes in the OpenSSL library that interacted poorly with certain certificates in the macOS Keychain.\[19\] When Node.js attempted to enumerate system roots on macOS Sequoia (version 15) and earlier versions, it encountered certificates that triggered DER (Distinguished Encoding Rules) decoding errors.\[1, 20\]

Rather than gracefully skipping these problematic certificates, the runtime in 1.106 would experience a fatal crash. Diagnostic logs from affected users showed that the system trust store on some machines contained hundreds of certificates, including many duplicates or non-standard objects that the new OpenSSL version found unparsable.\[19\] The temporary resolution for these users was to set

"http.systemCertificatesNode": false

, which forced the Extension Host to bypass the experimental native loading path and use the legacy, more tolerant certificate handling logic.\[17, 19\]

Refined Enumeration and Error Resilience

Following the 1.106 crisis, the Node.js and Visual Studio Code teams implemented several fixes to improve the resilience of system certificate loading. A key modification (PR #61784) updated the

X509sToArrayOfStrings

function to skip individual certificates that trigger parsing errors rather than failing the entire operation.\[12\] Additionally, PR #62576 refined the enumeration logic on macOS to more reliably interact with the

Security.framework

and correctly identify certificates in non-standard keychain locations.\[12\] These changes represent a critical shift toward "graceful degradation," where the runtime prioritizes connectivity for valid certificates even if a portion of the system trust store is malformed or unsupported.

Enterprise Networking and Proxy Interception

In the modern enterprise, the local trust store is not merely a collection of public roots; it is a dynamic policy engine. Security appliances such as Zscaler, Blue Coat, and Cisco Umbrella frequently perform SSL inspection by decrypting and re-encrypting traffic at the edge of the network.\[21, 22\] For this process to be transparent to the user, these appliances must inject a custom root or intermediate CA certificate into the host's trust store.\[9, 21\]

The Intermediate CA Challenge

A common failure point in enterprise certificate management occurs when security proxies utilize intermediate CA certificates rather than the primary organization root. While macOS is generally proficient at building trust chains from intermediates stored in the Keychain, the initial implementation of

--use-system-ca

on Windows had difficulty correctly reconciling these chains.\[22\] If the full chain—from the server leaf certificate back to the trusted root—cannot be validated through certificates available in either the system store or the bundled Mozilla store, the connection will fail.\[10, 21\]

Failure Condition

Technical Symptom

Primary Mitigation

Missing Root CA

UNABLE\_TO\_VERIFY\_LEAF\_SIGNATURE

Install Root CA to "Trusted Root" store.

Incomplete Intermediate Chain

unable to get local issuer certificate

Bundle intermediates or enable system trust.

Expired System Root

CERT\_HAS\_EXPIRED

Update OS roots or set

http.systemCertificatesNode: false

The interaction between the native

API (introduced in Node.js 18 and stabilized in 22) and system certificates has also been a source of friction. The

engine, which powers the native

implementation, sometimes fails to automatically inherit the system-level trust settings that are honored by the older

https.request

API.\[21, 23\] This has led to scenarios where extensions using the modern

API require

http.systemCertificatesNode

to be enabled to properly "see" the corporate CA certificates.\[21, 23\]

Case Study: GitLab for VS Code and API Connect

Extensions like GitLab for VS Code and IBM API Connect provide specific guidance for users operating behind self-signed CAs. Both require that the

http.systemCertificates

setting be set to

(its default) and that the root CA be explicitly added to the system trust store.\[10, 11\] For GitLab, if the certificate chain does not validate perfectly—including all intermediate certificates—network connections within the extension fail, preventing developers from accessing repositories or CI/CD pipelines.\[10\] This illustrates the high stakes of system certificate integration: it is not merely a convenience, but a prerequisite for functional development in secured environments.

Programmatic Control of CA Trust in Node.js 22+

The expansion of the TLS API in Node.js versions 22 and 24 provides developers with a high degree of programmatic control over trust settings. This is a significant improvement over the static environment variables of the past, allowing applications to adapt to their network environment at runtime.\[24\]

The getCACertificates and setDefaultCACertificates APIs

tls.getCACertificates(\[type\])

function allows a developer to query the current trust state of the process.\[24\] This function is particularly useful for debugging or for applications that need to selectively merge system certificates with application-specific ones.

type: "system"

: Retrieves all certificates from the host OS store, regardless of whether

--use-system-ca

was set at launch.\[24\]

type: "bundled"

: Retrieves the internal Mozilla roots.\[24\]

type: "default"

: Retrieves the aggregate set currently used by TLS clients in the thread.\[24\]

Complementing this is

tls.setDefaultCACertificates(certs)

, which allows an application to globally set the trust store for all subsequent TLS connections in the current thread.\[2, 24\] This API can be used to "patch" a process that was started without the correct command-line flags, as demonstrated in the following conceptual pattern:

const tls = require('node:tls');

// Explicitly retrieve and apply system certificates at runtime
try {
    const systemRoots = tls.getCACertificates('system');
    const existingRoots = tls.getCACertificates('default');
    
    // Deduplicate and apply as the new global default
    tls.setDefaultCACertificates();
} catch (err) {
    // Handle parsing errors from the system store gracefully
}

This pattern is highly effective for CLI tools and extensions that must function in "locked-down" environments where users cannot easily modify process startup flags.\[2, 24\] However, developers must be aware that these changes only affect the current thread and do not invalidate existing sessions already established by the

https.GlobalAgent

The Evolving Revocation Landscape: OCSP vs. CRL

As runtimes like Node.js move toward deeper integration with the operating system, they must also grapple with the complexities of certificate revocation. A certificate that is cryptographically valid may still be untrustworthy if its private key has been compromised or its owner's identity has changed.\[25\]

The Industry Pivot toward CRL

Historically, the Online Certificate Status Protocol (OCSP) was the preferred method for real-time revocation checking. OCSP allows a client to query a CA's responder for the status of a specific certificate serial number.\[25, 26\] However, the industry is currently shifting back toward Certificate Revocation Lists (CRLs) for several critical reasons. In August 2023, the CA/Browser Forum passed a ballot making CRLs mandatory and OCSP optional for publicly trusted CAs.\[26\] Major providers like Let's Encrypt have announced the sunsetting of OCSP URLs in newly issued certificates starting in early 2025.\[25\]

OCSP Protocol

CRL (Revocation Lists)

Low (CA sees every site the user visits).

High (Lists are downloaded/cached locally).

Reliability

"Soft-fail" behavior undermines security.

Tamper-evident; signed by the CA.

High per-request latency.

Large initial download; fast local lookup.

Connectivity

Requires real-time HTTP (not HTTPS) access.

Can be updated on a schedule.

This pivot has profound implications for Node.js applications. While many browsers use proprietary compressed revocation databases like CRLite (Firefox) or CRLSets (Chrome) to avoid the performance penalties of large CRL downloads, Node.js and its underlying OpenSSL library have traditionally had more limited support for automated revocation checking.\[25\] In enterprise drivers, such as the Snowflake.NET and Node.js drivers, the move to CRLs has introduced significant memory and performance considerations, adding up to two seconds of initial connection latency as lists are fetched and parsed.\[27\]

Revocation Challenges in Node.js

Node.js's implementation of

--use-system-ca

focuses primarily on the ingestion of certificates for chain building. It does not, by default, perform the intensive network operations required for OCSP or CRL checking unless explicitly configured via the

requestOCSP

option or through third-party libraries like

.\[28, 29\] This creates a "revocation gap" where a certificate revoked at the OS level might still be accepted by a Node.js process if the revocation status was not cached or checked through a native system call.\[27, 30\] Future iterations of the Node.js TLS subsystem (tracked in issue #58990) aim to match Chromium's policy more closely, which would involve better support for disallowed (revoked) certificates.\[12\]

Comparative Analysis of VS Code and Standalone Node.js Behavior

A critical insight gained from recent developer reports (Issue #314428) is the divergence between standalone Node.js and the Visual Studio Code Extension Host. Users have noted that setting the environment variable

NODE\_USE\_SYSTEM\_CA=1

before launching Visual Studio Code can result in different network outcomes than using the internal

http.systemCertificatesNode

setting.\[31\]

The Case of the Spurious Expiration

In certain configurations, extensions running in the VS Code 1.118 Extension Host reported

CERT\_HAS\_EXPIRED

errors for endpoints that were demonstrably valid.\[31\] Interestingly, these requests would succeed if the standalone Node.js runtime was used with the same environment variables, or if the

http.systemCertificatesNode

setting was disabled while

NODE\_USE\_SYSTEM\_CA=1

remained active.\[31\]

This suggests that the

http.systemCertificatesNode

implementation in Visual Studio Code is not merely a pass-through to the Node.js flag. Instead, the IDE appears to perform its own resolution and injection of system certificates, which may conflict with or duplicate the native Node.js logic.\[31\] This "double-loading" can lead to situations where an expired version of a certificate found in a legacy keychain takes precedence over a valid one, or where the validation logic in Electron's version of Node.js differs from the upstream release.\[20, 31\]

Runtime Discrepancies

The version of Node.js used by Visual Studio Code and Electron often lags behind or contains specific patches compared to the standalone versions available via managers like

.\[20\] For example, a fix backported to Node.js 22.21 might not yet be present in the Electron build used by a specific VS Code release, leading to inconsistent TLS behavior.\[20, 31\]

Runtime Context

Node.js Version

Observed TLS Outcome

Standalone (nvm)

Successful connection to internal OIDC.

VS Code Ext. Host

v22.22.1 (Electron 39)

CERT\_HAS\_EXPIRED

on identical endpoint.

VS Code w/ Flag Off

Successful connection (uses legacy path).

This discrepancy underscores the importance of the

http.systemCertificatesNode

setting as a diagnostic tool. By allowing users to toggle between the native Node.js logic and the VS Code legacy path, the team can isolate whether a connectivity failure is due to a runtime bug, a certificate chain issue, or an incompatibility with the host OS security framework.\[31\]

Security Best Practices for the Extension Ecosystem

The transition to system-level trust integration is fundamentally about reducing the prevalence of insecure workarounds. For years, the primary solution to certificate errors in corporate environments was to set

NODE\_TLS\_REJECT\_UNAUTHORIZED='0'

. This environment variable instructs the runtime to skip all certificate validation, rendering the connection vulnerable to man-in-the-middle attacks.\[7, 16, 21\]

Implementing Secure Alternatives

Modern extension developers are encouraged to move away from global bypasses and toward targeted trust management. This involves three primary strategies:

Leverage System Trust

: Support the

http.systemCertificates

http.systemCertificatesNode

settings to allow users to use their OS-level trust store.\[1, 21\]

Explicit CA Bundling

: If an extension must connect to a known private endpoint (e.g., a corporate Maven repository), it should allow users to specify a custom CA file path within the extension's own settings.\[16\]

Graceful Error Reporting

: When a TLS error occurs, extensions should check if the error is related to certificate trust and suggest that the user verify their system certificates or enable the appropriate VS Code settings.\[12, 23\]

The "Humly Control Panel" and "Cline" extensions provide excellent examples of this approach. Rather than suggesting an insecure global bypass, they provide specific documentation on how to export a root CA from a browser and configure the

NODE\_EXTRA\_CA\_CERTS

variable or enable the experimental system certificate settings.\[9, 21\]

Future Trajectories and Roadmap for System Trust

The ultimate goal of the Node.js and Visual Studio Code teams is to make system certificate integration so seamless and reliable that it can be enabled by default for all users. The roadmap for this transition (tracked in Issue #58990) includes several key milestones.\[12\]

Telemetry and Default Enablement

The ongoing collection of telemetry on certificate loading and parsing errors is the primary driver for future defaults.\[1\] Once the error rates for the native Node.js path fall below the threshold of the legacy implementation, the VS Code team will evaluate enabling

http.systemCertificatesNode

by default, likely starting with the Insiders channel.\[1\]

Build-Time Configuration and Environment Isolation

In the Node.js project, discussions are underway to provide a build-time option that enables

--use-system-ca

by default, allowing OS maintainers (such as Red Hat or Debian) to ship a version of Node.js that is pre-configured to trust the OS roots.\[12\] Additionally, work is being done to make

--use-system-ca

a per-environment option rather than a per-process flag. This would allow a main process to maintain a locked-down trust store while allowing specific worker threads—such as those performing network-heavy tasks—to opt into the system trust store.\[12\]

Alignment with Chromium Policy

As browsers continue to harden their certificate validation rules, Node.js aims to follow suit. This includes adopting Chromium's policies regarding certificate transparency, maximum certificate lifetimes (which are currently trending toward 47 days or shorter), and the disqualification of legacy roots that no longer meet modern security standards.\[2, 12, 25\] This alignment ensures that a certificate deemed untrustworthy by a browser will be treated with equal skepticism by a Node.js process, creating a unified security front across the development stack.

Summary of Technical Findings

The technical journey of

http.systemCertificatesNode

is a microcosm of the larger challenges facing modern development tools. The integration of system-level trust is a necessary evolution to support the complex, heterogeneous network environments of the modern enterprise, but it is an evolution fraught with technical pitfalls—from native crashes on macOS to subtle expiration discrepancies in Electron-based environments.

The evidence from the 2025-2026 development cycle demonstrates that while the native Node.js implementation is maturing rapidly, it still requires the robust error-handling and telemetry-driven refinement provided by the Visual Studio Code experimental framework. For developers, the move toward OS-integrated trust offers a future where "it works in my browser" finally translates to "it works in my IDE," provided that the underlying runtimes can navigate the disparate cryptographic legacies of the major operating systems. The transition from the static isolation of

node\_root\_certs.h

to the dynamic integration of the Windows Certificate Store and macOS Keychain is not merely a change in flags; it is a fundamental re-imagining of the trust boundary in modern software.

--------------------------------------------------------------------------------

Track loading system certificates with Node.js built-in support #287739 - GitHub,

https://github.com/microsoft/vscode/issues/287739

https://github.com/microsoft/vscode/issues/287739

Enterprise Network Configuration | Node.js Learn,

https://nodejs.org/learn/http/enterprise-network-configuration

https://nodejs.org/learn/http/enterprise-network-configuration

Where is the default CA certs used in nodejs? - Stack Overflow,

https://stackoverflow.com/questions/14619576/where-is-the-default-ca-certs-used-in-nodejs

https://stackoverflow.com/questions/14619576/where-is-the-default-ca-certs-used-in-nodejs

Use the system's CA certificates in the first instance · Issue #58198 · nodejs/node - GitHub,

https://github.com/nodejs/node/issues/58198

https://github.com/nodejs/node/issues/58198

How to add custom certificate authority (CA) to nodejs - Stack Overflow,

https://stackoverflow.com/questions/29283040/how-to-add-custom-certificate-authority-ca-to-nodejs

https://stackoverflow.com/questions/29283040/how-to-add-custom-certificate-authority-ca-to-nodejs

nodejs environment variable "NODE\_EXTRA\_CA\_CERTS" - Stack Overflow,

https://stackoverflow.com/questions/44459971/nodejs-environment-variable-node-extra-ca-certs

https://stackoverflow.com/questions/44459971/nodejs-environment-variable-node-extra-ca-certs

Use system certificate store when running under Windows · Issue #51537 · nodejs/node,

https://github.com/nodejs/node/issues/51537

https://github.com/nodejs/node/issues/51537

CA certificate trust stores - Nextstrain documentation,

https://docs.nextstrain.org/en/latest/reference/ca-certificates.html

https://docs.nextstrain.org/en/latest/reference/ca-certificates.html

Add Additional Certificate Authority for Node JS - Knowledge Base - Humly,

https://support.humly.com/add-additional-certificate-authority-for-node-js

https://support.humly.com/add-additional-certificate-authority-for-node-js

Using the VS Code extension with self-signed certificates - GitLab Docs,

https://docs.gitlab.com/editor\_extensions/visual\_studio\_code/ssl/

https://docs.gitlab.com/editor\_extensions/visual\_studio\_code/ssl/

Securing communication between the Visual Studio Code plug-in and API Connect - IBM,

https://www.ibm.com/docs/en/api-connect/software/12.1.0?topic=configuring-securing-communication-between-visual-studio-code-plug-in-api-connect

https://www.ibm.com/docs/en/api-connect/software/12.1.0?topic=configuring-securing-communication-between-visual-studio-code-plug-in-api-connect

Tracking issue: custom CA certificate support · Issue #58990 ...,

https://github.com/nodejs/node/issues/58990

https://github.com/nodejs/node/issues/58990

Node.js 23.9.0 (Current),

https://nodejs.org/en/blog/release/v23.9.0

https://nodejs.org/en/blog/release/v23.9.0

From Learner to Contributor: Navigating the VS Code Extensions Structure | by Cha Jesse | Medium,

https://medium.com/@chajesse/from-learner-to-contributor-navigating-the-vs-code-extensions-structure-ed150f9897e5

https://medium.com/@chajesse/from-learner-to-contributor-navigating-the-vs-code-extensions-structure-ed150f9897e5

Extension Host - Visual Studio Code,

https://code.visualstudio.com/api/advanced-topics/extension-host

https://code.visualstudio.com/api/advanced-topics/extension-host

Managing SSL Certificates in VS Code: Corporate AI Integration Made Simple - Medium,

https://medium.com/@frigato.luca97/mastering-ssl-certificates-a-developers-guide-to-vs-code-plugins-for-corporate-ai-backends-821dfca7dc26

https://medium.com/@frigato.luca97/mastering-ssl-certificates-a-developers-guide-to-vs-code-plugins-for-corporate-ai-backends-821dfca7dc26

Regression: Extension Host (Code 6) crash on macOS after updating to 26.4 · Issue #303371 · microsoft/vscode - GitHub,

https://github.com/microsoft/vscode/issues/303371

https://github.com/microsoft/vscode/issues/303371

Weekly GitHub Report for Vscode: November 10, 2025 - Buttondown,

https://buttondown.com/weekly-project-news/archive/weekly-github-report-for-vscode-november-10-2025/

https://buttondown.com/weekly-project-news/archive/weekly-github-report-for-vscode-november-10-2025/

After upgrade to 1.106 I'm unable to connect to MCP server · Issue #277297 · microsoft/vscode - GitHub,

https://github.com/microsoft/vscode/issues/277297

https://github.com/microsoft/vscode/issues/277297

Cannot open Dev Containers with Features - "Unable to get issuer certificate" on macOS Sequoia 15.7.3 (24G419) · Issue #11425 · microsoft/vscode-remote-release - GitHub,

https://github.com/microsoft/vscode-remote-release/issues/11425

https://github.com/microsoft/vscode-remote-release/issues/11425

Custom CA certificates (NODE\_EXTRA\_CA\_CERTS) not respected for API connections · Issue #8816 · cline/cline - GitHub,

https://github.com/cline/cline/issues/8816

https://github.com/cline/cline/issues/8816

--use-system-ca

support for intermediate certificates on Windows · Issue #57163 · nodejs/node - GitHub,

https://github.com/nodejs/node/issues/57163

https://github.com/nodejs/node/issues/57163

Gemini API requests fail with "fetch failed" error (v3.33.2+) #10628 - GitHub,

https://github.com/RooCodeInc/Roo-Code/issues/10628

https://github.com/RooCodeInc/Roo-Code/issues/10628

TLS (SSL) | Node.js v26.1.0 Documentation,

https://nodejs.org/api/tls.html#tlsgetcacertificates-type

https://nodejs.org/api/tls.html#tlsgetcacertificates-type

SSL Certificate Revocation Explained : What the End of OCSP Means for Website Security,

https://shop.trustico.com/blogs/stories/ssl-certificate-revocation-explained-what-the-end-of-ocsp-means-for-website-security

https://shop.trustico.com/blogs/stories/ssl-certificate-revocation-explained-what-the-end-of-ocsp-means-for-website-security

OCSP vs CRL Explained - Smallstep,

https://smallstep.com/blog/ocsp-vs-crl-explained/

https://smallstep.com/blog/ocsp-vs-crl-explained/

Replacing OCSP with CRL as the method of certificate revocation checking,

https://community.snowflake.com/s/article/Replacing-OCSP-with-CRL-as-the-method-of-certificate-revocation-checking

https://community.snowflake.com/s/article/Replacing-OCSP-with-CRL-as-the-method-of-certificate-revocation-checking

malta-slides/tls.d.ts at aeb4e73ab498dec7049f4a481cb9e23d9c30e37f - Gitea,

https://git.dailysh.it/public/malta-slides/src/commit/aeb4e73ab498dec7049f4a481cb9e23d9c30e37f/node\_modules/@types/node/tls.d.ts

https://git.dailysh.it/public/malta-slides/src/commit/aeb4e73ab498dec7049f4a481cb9e23d9c30e37f/node\_modules/@types/node/tls.d.ts

easy-ocsp - NPM,

https://npmjs.com/package/easy-ocsp

https://npmjs.com/package/easy-ocsp

MongoDB error "SSL peer certificate revocation status checking failed: Could not verify X509 certificate store for OCSP Stapling" - Stack Overflow,

https://stackoverflow.com/questions/75338163/mongodb-error-ssl-peer-certificate-revocation-status-checking-failed-could-not

https://stackoverflow.com/questions/75338163/mongodb-error-ssl-peer-certificate-revocation-status-checking-failed-could-not

http.systemCertificatesNode causes Extension Host TLS requests to fail with CERT\_HAS\_EXPIRED despite NODE\_USE\_SYSTEM\_CA working in standalone Node · Issue #314428 · microsoft/vscode - GitHub,

https://github.com/microsoft/vscode/issues/314428

https://github.com/microsoft/vscode/issues/314428

