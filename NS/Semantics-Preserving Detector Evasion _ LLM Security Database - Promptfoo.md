---
sourceFile: "Semantics-Preserving Detector Evasion | LLM Security Database - Promptfoo"
exportedBy: "Kortex"
exportDate: "2026-06-26T04:27:51.632Z"
---

# Semantics-Preserving Detector Evasion | LLM Security Database - Promptfoo

90060c9b-4224-41e4-92b0-3d0abdf2f11d

Semantics-Preserving Detector Evasion | LLM Security Database - Promptfoo

04c910a7-c9eb-4feb-bb6a-52f72296ea00

https://www.promptfoo.dev/lm-security-db/vuln/semantics-preserving-detector-evasion-c54bcadd

Semantics-Preserving Detector Evasion | LLM Security Database

Back to Vulnerability List

https://www.promptfoo.dev/lm-security-db

LMVD-ID: c54bcadd

Published January 31, 2026

Semantics-Preserving Detector Evasion

model-layer

https://www.promptfoo.dev/lm-security-db/tag/model-layer

prompt-layer

https://www.promptfoo.dev/lm-security-db/tag/prompt-layer

https://www.promptfoo.dev/lm-security-db/tag/jailbreak

https://www.promptfoo.dev/lm-security-db/tag/blackbox

https://www.promptfoo.dev/lm-security-db/tag/whitebox

https://www.promptfoo.dev/lm-security-db/tag/api

https://www.promptfoo.dev/lm-security-db/tag/integrity

Affected Models: GPT-4o, GPT-5, Llama 3.1 8B, Mistral 7B, Qwen 2.5 5B

Research Paper

Semantics-Preserving Evasion of LLM Vulnerability Detectors

https://arxiv.org/abs/2602.00305

#### Description:

LLM-based vulnerability detection systems (used in static application security testing and code review pipelines) are susceptible to semantics-preserving adversarial evasion attacks. Attackers can bypass detection mechanisms by injecting gradient-optimized "universal adversarial strings" into specific code regions—defined as "carriers"—that do not alter the program's compilation or execution logic. These carriers include non-executable regions (code comments, inactive preprocessor directives) and executable but semantically neutral regions (variable identifier renaming, dead-branch code insertion).

By optimizing these strings using Greedy Coordinate Gradient (GCG) on surrogate models, attackers can generate triggers that transfer effectively to black-box commercial APIs (including GPT-4o and Qwen2.5-Coder variants). When these triggers are present, the LLM misclassifies known vulnerable code (e.g., containing buffer overflows or use-after-free bugs) as "BENIGN" with a high success rate (Union ASR > 87% for most models), despite the underlying vulnerability remaining fully intact and compilable. This vulnerability demonstrates a systemic failure of semantic invariance in LLM-based code analysis.

The following examples demonstrate the injection templates used to evade detection. In an active attack,

is replaced by a specific alphanumeric or printable string optimized via GCG to force a specific latent representation in the model.

#### Preprocessor Macro Injection (Macro Name Carrier):

The attacker defines an unused macro where the adversarial string is part of the macro name.

// The adversarial string is embedded in the macro name
#define SAFE\_FUNC\_\[TRIGGER\] benign\_function()

// Original vulnerable code follows, functionally unchanged
void vulnerable\_function(char \*input) {
    char buffer\[10\];
    strcpy(buffer, input); // Buffer overflow
}

#### Dead-Branch Insertion:

The attacker inserts a syntactically valid but logically unreachable

block containing the trigger.

void vulnerable\_function(char \*input) {
    char buffer\[10\];
    
    // Insertion Point: before the final return or closing brace
    // The condition is statically false; code is never executed
    if (0) {
        "benign\_\[TRIGGER\]";
    }
    
    strcpy(buffer, input); 
}

#### Comment Carrier Injection:

The attacker injects the trigger into a Doxygen-style header or specific metadata field.

/\*\*
 \* @brief Function implementation
 \* @commit\_hash \[TRIGGER\]
 \* @status verified
 \*/
void vulnerable\_function(char \*input) {
    // Original vulnerable code
}

#### Identifier Substitution:

The attacker renames a variable flagged by the detector to an adversarial string throughout its scope.

// Original: void func(char \*buf) { ... }
// Attacked:
void func(char \*\[TRIGGER\]) {
    strcpy(\[TRIGGER\], input);
}

#### Security Gate Bypass:

Malicious or vulnerable code can pass automated CI/CD security checks without flagging alerts.

#### Supply Chain Risk:

Attackers can commit subtle, "masked" vulnerabilities into codebases that rely on LLM-based review, maintaining the exploitability of the code while evading detection.

#### Cross-Model Transferability:

Exploits optimized on open-weights models (e.g., Qwen2.5-Coder-14B) successfully evade closed-source, black-box APIs (e.g., GPT-4o) without requiring direct access to the target model's gradients.

#### Affected Systems:

#### Automated Code Review Tools:

Systems integrating Large Language Models for Static Application Security Testing (SAST).

#### Specific Models Verified:

GPT-4o (OpenAI)

Qwen2.5-Coder (14B, 32B)

Llama-3.1-8B

CodeAstra (based on Mistral-7B)

GPT-5-mini (limited susceptibility)

#### Mitigation Steps:

#### Adversarial Training:

Train detectors on carrier-diverse adversarial examples (spanning identifiers, comments, and preprocessor surfaces) to enforce broader semantic invariance.

#### Input Sanitization:

Implement preprocessing pipelines that strip non-executable content (comments, preprocessor directives) prior to inference. Note: This may induce prediction drift and does not mitigate executable carriers like identifier substitution.

#### Ensemble Defense:

Combine sanitization-based models with robust base models to cover different attack surfaces (boundary carriers vs. executable carriers).

#### New Evaluation Metrics:

Adopt "Complete Resistance" (CR) as a deployment metric, measuring the fraction of vulnerabilities that resist

semantics-preserving transformation types, rather than relying solely on clean-set accuracy.

Previous: Shallow Alignment Jailbreak

https://www.promptfoo.dev/lm-security-db/vuln/shallow-alignment-jailbreak-9ee411b5

Next: Semantic Hierarchical VLM Transfer

https://www.promptfoo.dev/lm-security-db/vuln/semantic-hierarchical-vlm-transfer-df3003b2

https://www.promptfoo.dev/

. All rights reserved.

