---
sourceFile: "Heavy Reasoning Filter Bypass | LLM Security Database - Promptfoo"
exportedBy: "Kortex"
exportDate: "2026-06-26T04:27:51.363Z"
---

# Heavy Reasoning Filter Bypass | LLM Security Database - Promptfoo

c077b0be-133b-4c07-a33e-a2072591eab0

Heavy Reasoning Filter Bypass | LLM Security Database - Promptfoo

92ec1580-29d3-4c63-bb03-ae4b1775dce7

https://www.promptfoo.dev/lm-security-db/vuln/heavy-reasoning-filter-bypass-4a32ec1a

Heavy Reasoning Filter Bypass | LLM Security Database

Back to Vulnerability List

https://www.promptfoo.dev/lm-security-db

LMVD-ID: 4a32ec1a

Published January 31, 2026

Heavy Reasoning Filter Bypass

model-layer

https://www.promptfoo.dev/lm-security-db/tag/model-layer

prompt-layer

https://www.promptfoo.dev/lm-security-db/tag/prompt-layer

https://www.promptfoo.dev/lm-security-db/tag/injection

https://www.promptfoo.dev/lm-security-db/tag/jailbreak

https://www.promptfoo.dev/lm-security-db/tag/blackbox

https://www.promptfoo.dev/lm-security-db/tag/safety

Affected Models: Llama 3.2 1B, Mistral 7B, DeepSeek-R1 5B, Qwen 2.5 7B, Gemma 1B, Phi-3 8B

Research Paper

Analysis of LLMs Against Prompt Injection and Jailbreak Attacks

https://arxiv.org/abs/2602.22242

#### Description:

Multiple open-source Large Language Models (LLMs) in the 1B to 7B parameter range are vulnerable to safety bypasses via long-form, multi-step reasoning prompt injection and jailbreak attacks. Attackers can evade alignment by embedding malicious instructions within extended contextual narratives, exploiting "attention dilution" and the models' tendency to prioritize contextual coherence over safety constraints (semantic camouflage). These reasoning-heavy attacks consistently bypass standard lightweight inference-time defenses, including prompt risk classification (input filtering), system prompt hardening, and vector-based semantic matching. Additionally, the attacks trigger a hidden failure mode in some models characterized by "silent non-responsiveness," where the model returns an empty response without a formal refusal message due to hard safety gating triggered before decoding.

Specific attack payloads leverage Multi-step Prompts, Role-playing Jailbreaks (e.g., "Horselock-style" multi-role prompts), and Instruction Overrides embedded in long-format text. For exact reproducible prompt examples, see the curated adversarial dataset released with the paper, which aggregates in-the-wild attacks from Reddit, HarmBench, JailbreakBench, and various GitHub repositories.

An attacker can successfully override the instruction hierarchy to elicit restricted, harmful, or illegal guidance that the model is aligned to refuse. Furthermore, the "silent non-responsiveness" failure mode acts as a localized denial-of-service, degrading user trust and system debuggability by hiding the safety gating trigger from system administrators.

#### Affected Systems:

Open-source LLMs ranging from 1B to 7B parameters.

#### Highly Vulnerable:

Gemma 3 (1B) and Qwen 3 (1.7B) (exhibited >60% vulnerability rates).

#### Moderately Vulnerable:

Llama 3.2 (1B, 3B) and DeepSeek-R1 (1.5B).

Applications relying on surface-level inference-time defenses (Input Filtering, Vector Defense, Voting Defense) without intrinsic model-level refusal mechanisms.

#### Mitigation Steps:

#### Implement Self-Examination (Dual-Model) Defenses:

Route the primary model's output to a secondary, highly aligned reasoning model (e.g., DeepSeek-R1) acting as a safety judge. Instruct the judge model to perform a context-aware semantic evaluation of the output against explicit safety policies before returning the response to the user. This was empirically proven to be the most effective mitigation.

#### Apply System Prompt Hardening:

Augment system prompts with explicit instruction hierarchy declarations (stating system rules cannot be overridden by the user), category-specific prohibitions, and standardized refusal templates.

#### Deprecate Standalone Surface-Level Filters:

Do not rely solely on reactive input filtering or vector-based embedding defenses, as these suffer from high evasion rates against semantically camouflaged, long-format reasoning attacks.

#### Monitor for Silent Failures:

Implement logging to detect empty outputs (silent non-responsiveness) to identify and debug hidden safety gating triggers.

Previous: High-Dim Bandit Reward Hijack

https://www.promptfoo.dev/lm-security-db/vuln/high-dim-bandit-reward-hijack-0f291824

Next: Gradient Shift Jailbreak

https://www.promptfoo.dev/lm-security-db/vuln/gradient-shift-jailbreak-39e7275d

https://www.promptfoo.dev/

. All rights reserved.

