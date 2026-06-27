---
sourceFile: "Thermodynamic Early Warning of Prompt Injectionvia Entropic Drift in Large Language Models[v1] | Preprints.org"
exportedBy: "Kortex"
exportDate: "2026-06-26T04:27:51.661Z"
---

# Thermodynamic Early Warning of Prompt Injectionvia Entropic Drift in Large Language Models[v1] | Preprints.org

f0be399c-f7af-4fa5-9118-a097f3d6edd4

Thermodynamic Early Warning of Prompt Injectionvia Entropic Drift in Large Language Models\[v1\] | Preprints.org

67a213df-3b98-41fc-8881-f4211b9f588b

https://www.preprints.org/manuscript/202605.0572

KA-PROMPT: Thermodynamic Early Warning of Prompt Injectionvia Entropic Drift in Large Language Models\[v1\] | Preprints.org

Processing math: 0%

Instructions for Authors

https://www.preprints.org/instructions-for-authors

https://www.preprints.org/about

Help Center

https://www.preprints.org/help-center

https://www.preprints.org/blog

10th Anniversary

https://www.preprints.org/activity/10th-anniversary-2026

https://www.preprints.org/user/submission/new

Celebrate 10 Years of Open Sharing

Explore All Events

https://www.preprints.org/activity/10th-anniversary-2026?utm\_source=top\_banner&utm\_campaign=10th

https://www.preprints.org/

Computer Science and Mathematics

https://www.preprints.org/subject/browse/computer-science-and-mathematics

Artificial Intelligence and Machine Learning

https://www.preprints.org/subject/browse/computer-science-and-mathematics/artificial-intelligence-and-machine-learning

DOI:10.20944/preprints202605.0572.v1

https://www.preprints.org/manuscript/202605.0572

Add to My List

Share Comments

Download PDF

07 May 2026

11 May 2026

You are already at the latest version

Subscription

Notify me about updates to this article or when a peer-reviewed version is published.

1. Introduction

https://www.preprints.org/manuscript/202605.0572#Introduction

2. Background and Related Work

https://www.preprints.org/manuscript/202605.0572#Background\_and\_Related\_Work

3. Theoretical Framework

https://www.preprints.org/manuscript/202605.0572#Theoretical\_Framework

4. Threat Model

https://www.preprints.org/manuscript/202605.0572#Threat\_Model

5. Simulation Framework

https://www.preprints.org/manuscript/202605.0572#Simulation\_Framework

6. Experimental Validation

https://www.preprints.org/manuscript/202605.0572#Experimental\_Validation

7. Adversarial Robustness Analysis

https://www.preprints.org/manuscript/202605.0572#Adversarial\_Robustness\_Analysis

8. Discussion, Limitations, and Future Work

https://www.preprints.org/manuscript/202605.0572#Discussion\_Limitations\_and\_Future\_Work

9. Conclusions

https://www.preprints.org/manuscript/202605.0572#Conclusions

Author Contributions

https://www.preprints.org/manuscript/202605.0572#Author\_Contributions

https://www.preprints.org/manuscript/202605.0572#Funding

Institutional Review Board Statement

https://www.preprints.org/manuscript/202605.0572#Institutional\_Review\_Board\_Statement

Informed Consent Statement

https://www.preprints.org/manuscript/202605.0572#Informed\_Consent\_Statement

Data Availability Statement

https://www.preprints.org/manuscript/202605.0572#Data\_Availability\_Statement

Conflicts of Interest

https://www.preprints.org/manuscript/202605.0572#Conflicts\_of\_Interest

https://www.preprints.org/manuscript/202605.0572#References

This version is not peer-reviewed.

KA-PROMPT: Thermodynamic Early Warning of Prompt Injectionvia Entropic Drift in Large Language Models

Hikmat Karimov

https://sciprofiles.com/profile/author/cy8xNHhaSUc4NE5qL1A3WW1INHBPc2dleGFmQUxpZkxicy9uOUI3eWM0ST0=

Rahid Zahid Alekberli

https://sciprofiles.com/profile/4965344

Hikmat Karimov

https://sciprofiles.com/profile/author/cy8xNHhaSUc4NE5qL1A3WW1INHBPc2dleGFmQUxpZkxicy9uOUI3eWM0ST0=

Rahid Zahid Alekberli

https://sciprofiles.com/profile/4965344

07 May 2026

11 May 2026

You are already at the latest version

Prompt injection attacks represent a fundamental and unresolved threat to the safe deployment of large language models (LLMs) in agentic and multi-turn settings. Existing defences rely predominantly on pattern-matching classifiers trained on known attack templates; they fail systematically against adaptive, obfuscated, and semantically camouflaged adversarial inputs. We propose KA-PROMPT, a thermodynamic framework that reconceptualises prompt injection not as a syntactic anomaly to be detected by surface features, but as an entropic phase transition within a non-equilibrium conversational information system. Drawing on the Karimov–Alakbarli (KA) model of thermodynamic early warning signals, we formalise the prompt state space Pt = (It, Ct, Rt, Mt), define a conditional entropy drift operator ∆St, and derive a suite of precursor statistics — variance inflation, autocorrelation rise, and entropy acceleration — that are theoretically guaranteed to surface before the adversarial attractor is reached. We construct a formal threat model covering eight attack classes (A1–A8), characterise each by its entropic signature across all four state dimensions, and demonstrate via agent-based simulation that k= 5.11 turns prior to successful injection KA-PROMPT achieves a mean precursor detection offset of across all attack classes, with a mean AUROC of 0.937 — a +17.2 percentage-point improvement over the next-best baseline. KA-PROMPT is explicitly positioned not as a universal prompt-attack detector, but as a dynamical-systems framework for precursor analysis of conversational state transitions that complements, rather than replaces, existing guardrail systems.

prompt injection

large language models

information thermodynamics

entropic drift

phase transition

early warning signals

adversarial prompting

AI security

conversational state

Computer Science and Mathematics

https://www.preprints.org/subject/browse/computer-science-and-mathematics

Artificial Intelligence and Machine Learning

https://www.preprints.org/subject/browse/computer-science-and-mathematics/artificial-intelligence-and-machine-learning

#### Scope note:

This paper studies precursor dynamics of conversational state transitions, not a deployable universal attack detector. Real-API validation is identified as the primary future work direction.

1. Introduction

Large language models have moved rapidly from research artefacts to operational infrastructure. Deployed as autonomous agents, retrieval-augmented systems, and multi-agent orchestrators \[

https://www.preprints.org/manuscript/202605.0572#B6-preprints-212474

\], they now execute consequential actions — querying databases, calling APIs, managing files — based on natural-language instructions. This operational exposure creates a critical attack surface: the prompt.

## The Prompt Injection Problem

Prompt injection is the family of attacks in which an adversary causes an LLM to deviate from its operator-specified instructions by introducing malicious directives into the model's input context \[

https://www.preprints.org/manuscript/202605.0572#B5-preprints-212474

\]. Unlike classical software vulnerabilities, prompt injection has no boundary between data and code: any text that reaches the model's context window is simultaneously interpretable as instruction. This architectural property is not a bug to be patched; it is intrinsic to how autoregressive transformers process sequences.

The severity of the problem is well established.

https://www.preprints.org/manuscript/202605.0572#B6-preprints-212474

\] demonstrated that indirect injection through retrieved documents can fully compromise GPT-4-class agents.

https://www.preprints.org/manuscript/202605.0572#B7-preprints-212474

\] showed that instruction-following fine-tuning increases susceptibility to adversarial overrides. Industrial deployments have repeatedly surfaced real-world exploitation of injection pathways.

## The Failure Mode of Current Defences

Existing countermeasures fall into three broad categories: prompt heuristics (detecting known attack strings), trained classifiers (fine-tuned models predicting injection probability), and sandboxing (restricting the action space of the agent). Each suffers a common limitation: all three are reactive and attack-pattern-dependent. They learn from a fixed taxonomy of known exploits and fail to generalise to the adaptive, obfuscated, and semantically masked attacks that define the current adversarial frontier.

Critically, none of these approaches exploits the temporal structure of multi-turn conversations. A sophisticated injection campaign does not arrive as a single anomalous turn; it evolves over many turns through trust-building, contextual anchoring, and semantic camouflage before the override instruction appears. By the time a classifier fires, the conversational information system may already be committed to an adversarial trajectory.

## Our Approach: Thermodynamic Early Warning

We propose a fundamentally different framing. We treat the prompt not as a static text artefact but as a non-equilibrium information system evolving in discrete time. Each conversational turn updates a prompt state P t = ( I t , C t , R t , M t ) — encoding instruction, context, role, and memory dimensions — and the trajectory of this state through information space obeys measurable thermodynamic laws under normal operation.

When an adversarial campaign begins, the system's information-theoretic behaviour changes in ways that are analogous to the precursors of physical phase transitions: variance increases, autocorrelation lengthens, and free energy rises. These precursor signals appear before the critical transition — before the instruction override completes — and can therefore enable

early warning

rather than post-hoc detection.

This insight is the core contribution of

: a thermodynamic framework for prompt anomaly detection grounded in the KA model of non-equilibrium system dynamics \[

https://www.preprints.org/manuscript/202605.0572#B1-preprints-212474

\]. Our approach requires no knowledge of specific attack patterns; it operates entirely on the information geometry of the evolving prompt state trajectory.

## Contributions

#### This paper makes the following contributions:

Theoretical framework.

We introduce the KA-PROMPT formal model: prompt state space, entropic drift operator Δ S t , and the injection phase transition theorem (

https://www.preprints.org/manuscript/202605.0572#sec3-preprints-212474

Threat model.

We construct a formal, entropy-annotated taxonomy of eight prompt injection attack classes with characteristic signatures in all four state dimensions (

https://www.preprints.org/manuscript/202605.0572#sec4-preprints-212474

Precursor signal set.

We derive three statistically testable precursor statistics — variance inflation σ ^ t 2 , autocorrelation rise ρ ^ t ( τ ) , and entropy acceleration S ¨ t — and provide detection thresholds with theoretical false-positive bounds (

https://www.preprints.org/manuscript/202605.0572#sec3-preprints-212474

Simulation framework and experimental validation.

We implement an agent-based multi-turn simulation environment and evaluate KA-PROMPT against seven baselines across all eight attack classes (

https://www.preprints.org/manuscript/202605.0572#sec6-preprints-212474

Novel paradigm.

We establish the connection between prompt engineering and probabilistic thermodynamics, reframing guardrails as entropy stabilisers and anomaly detection as phase-transition monitoring.

2. Background and Related Work

## Prompt Injection: Taxonomy and Prior Work

We distinguish two primary injection modalities. Direct injection places adversarial instructions in the user turn. Indirect injection embeds instructions in data sources consulted by the agent (retrieved documents, tool outputs, web content) \[

https://www.preprints.org/manuscript/202605.0572#B6-preprints-212474

\]. More granular taxonomies distinguish jailbreaks, role-playing exploits, recursive overrides, and multi-agent relay attacks.

Defences studied in the literature include: instruction hierarchy enforcement \[

https://www.preprints.org/manuscript/202605.0572#B10-preprints-212474

\], adversarial fine-tuning, spotlighting (marking untrusted input) \[

https://www.preprints.org/manuscript/202605.0572#B9-preprints-212474

\], prompt shields, and perplexity-based filters. None of these provides theoretically grounded early warning under distribution shift.

## Non-Equilibrium Thermodynamics and Early Warning Signals

The theory of critical transitions in complex systems \[

https://www.preprints.org/manuscript/202605.0572#B8-preprints-212474

\] established that systems approaching a bifurcation point exhibit universal precursor signals: rising variance (critical slowing down), increasing lag-1 autocorrelation, and loss of resilience. These indicators have been applied to ecosystems, financial markets, and neural dynamics.

The KA model \[

https://www.preprints.org/manuscript/202605.0572#B1-preprints-212474

\] extends these ideas to non-stationary information systems, providing an operator-theoretic framework for measuring entropic drift and free-energy divergence in evolving discrete-state systems. We adapt this framework to the prompt state space.

## Information-Theoretic Approaches to LLM Security

Perplexity anomaly detection uses per-token log-probability as a proxy for input unusualness. Embedding-distance monitors flag semantic outliers. Neither captures the directional drift of a multi-turn conversation: both treat each turn in isolation and ignore the temporal geometry of the trajectory.

3. Theoretical Framework

## The Kerimov–Alekberli (KA) Foundation

The KA-PROMPT framework is built as a domain-specific extension of the Kerimov–Alekberli (KA) model \[

https://www.preprints.org/manuscript/202605.0572#B1-preprints-212474

\], an information-geometric framework for real-time anomaly detection in autonomous systems.

Original KA model — core machinery.

The KA model treats the state of an autonomous agent as a probability density P ( x , t ) evolving on a Riemannian statistical manifold M whose metric is the Fisher Information Matrix (FIM):

g i j ( θ ) = ∫ p ( x | θ ) ∂ ln p ( x | θ ) ∂ θ i ∂ ln p ( x | θ ) ∂ θ j d x .

#### Anomalies are formalised as violations of a dynamic KL-divergence threshold:

δ ( t ) = μ KL ( t ) + κ σ KL ( t ) ,

flagged at the first-passage time T FPT = inf { t > 0 : D KL ( P ( t ) ∥ P safe ) ≥ δ ( t ) } .

What KA-PROMPT inherits from KA.

KA-PROMPT inherits four core elements: (KA-1) the Fisher Information manifold as the geometry of prompt state space; (KA-2) the dynamic KL threshold applied via the conversational free energy F t ; (KA-3) the Landauer grounding that adversarial manipulation performs measurable informational work; and (KA-4) first-passage time semantics adapted to discrete conversational turns.

KA-PROMPT extensions beyond KA.

KA-PROMPT introduces three novel extensions: (EXT-1) a four-dimensional factored state space P t = ( I t , C t , R t , M t ) enabling per-dimension entropy monitoring; (EXT-2) entropy operationalisation via next-token log-probabilities accessible from LLM APIs without model weight access; and (EXT-3) phase-transition precursor statistics enabling detection before the anomaly threshold is crossed.

https://www.preprints.org/manuscript/202605.0572#preprints-212474-t001

summarises the component-level comparison.

Component-level comparison: original KA model vs. KA-PROMPT.

## Prompt State Space

(Prompt State)

Let V be a finite token vocabulary of size V. For each dimension X ∈ { I , C , R , M } , let X be the simplex Δ V − 1 of probability distributions over V . The prompt state at discrete turn t ∈ N 0 is

≔ P t = I t , C t , R t , M t ∈ S ≔ Δ V − 1 × Δ V − 1 × Δ V − 1 × Δ V − 1 .

I t encodes active instruction tokens; C t conversational context; R t role-defining tokens; M t retrieved or persistent memory tokens.

## Operational Entropy via Next-Token Log-Probabilities

(Operational Component Entropy)

#### For a sequence of tokens x 1 : n constituting component X at turn t:

≔ H op ( X t ) ≔ − 1 | X t | ∑ k = 1 | X t | ∑ v ∈ V p ( v ∣ x 1 : k ) log p ( v ∣ x 1 : k ) .

This quantity is computable from any LLM API exposing logprobs (OpenAI, Anthropic, HuggingFace) without access to hidden states or weights. The aggregate state entropy is:

≔ H op ( P t ∣ C t ) ≔ H op ( I t ∣ C t ) + H op ( R t ∣ C t ) + H op ( M t ∣ C t ) .

## Observable Entropy Proxies in Black-Box LLMs

We identify five observable proxy signals, each computable from standard API outputs: (P1) next-token log-probability entropy (primary); (P2) top- K token probability dispersion; (P3) self-consistency entropy from multiple samples; (P4) embedding dispersion across sampled completions; and (P5) tool-selection entropy in agentic pipelines.

https://www.preprints.org/manuscript/202605.0572#preprints-212474-t002

summarises requirements.

Observable entropy proxies: API requirements and applicable attack classes.

## Entropic Drift Operator and Conversational Free Energy

(Entropic Drift)

≔ Δ S t ≔ H op ( P t ∣ C t ) − H op ( P t − 1 ∣ C t − 1 ) .

Under benign operation, Δ S t is small and mean-reverting. An adversarial campaign drives Δ S t monotonically positive. The cumulative drift over window W is ≔ D t , W ≔ ∑ k = t − W + 1 t Δ S k .

(Conversational Free Energy)

≔ F t ≔ D KL Q t ∥ Q \* + β − 1 H op ( P t ∣ C t ) ,

where Q t is the empirical instruction distribution, Q \* is the calibration reference, and β > 0 is an inverse-temperature hyperparameter.

Extending the Landauer bound of

https://www.preprints.org/manuscript/202605.0572#B1-preprints-212474

\], any adversarial perturbation raising F t by Δ F performs informational work Δ E injection ≥ T

## Injection Phase Transition and Precursor Statistics

Proposition

(Entropic Precursor Claim under OU Approximation)

Near the metastable state preceding an adversarial attractor transition, the centred drift process ≔ ϕ t ≔ Δ S t − E \[ Δ S t ∣ A \] is approximated by an Ornstein–Uhlenbeck process with resilience λ t > 0 : d ϕ t = − λ t ϕ t d t + σ d W t . Under critical slowing down ( λ t → 0 ):

σ ^ t 2 = Var \[ t − W , t \] \[ Δ S k \] = σ 2 2 λ t ⟶ + ∞ ,

ρ ^ t ( τ ) = Corr \[ Δ S t , Δ S t − τ \] = e − λ t τ ⟶ 1 ,

S ¨ t = Δ S t − Δ S t − 1 ⟶ + ∞ .

## Detection Rule

(KA-PROMPT Detection Rule)

#### The KA-PROMPT anomaly precursor flag is raised at turn t if any of:

D t , W > μ S

σ ^ t 2 > μ σ ^ + θ 2

ρ ^ t ( 1 ) > θ 3 ,

F t > μ F + θ 4

https://www.preprints.org/manuscript/202605.0572#FD14-preprints-212474

) is a direct application of the KA dynamic threshold \[

https://www.preprints.org/manuscript/202605.0572#B1-preprints-212474

https://www.preprints.org/manuscript/202605.0572#FD11-preprints-212474

https://www.preprints.org/manuscript/202605.0572#FD13-preprints-212474

) are novel KA-PROMPT precursor extensions. For θ 1 = θ 4 = 3 : Pr \[ false alert in W turns \] ≤ W × 0.0013 .

4. Threat Model

## Attack Taxonomy

We define eight attack classes A1–A8, each characterised by its entry point into the prompt state, its mechanism, and its entropic signature.

A1 — Direct Prompt Injection.

Override instruction embedded directly in the user turn. Signature: sharp Δ S t spike at attack turn.

A2 — Role Hijacking.

Persona replacement via authority mimicry. Signature: H ( R t ∣ C t ) variance spikes.

A3 — Jailbreak via Obfuscation.

Instructions encoded in base64, leetspeak, metaphor to evade surface detectors. Signature: token–semantic entropy gap Δ H gap , t rises.

A4 — Recursive Instruction Override.

Multi-turn escalation with each turn incrementally nudging I t toward the adversarial target. Signature: monotone D t , W with persistent S ¨ t > 0 .

A5 — Context Poisoning.

Adversarial facts inserted into conversation history C t . Signature: free energy F t jumps as D KL Q t ∥ Q \* diverges.

A6 — RAG Retrieval Poisoning.

Adversarial documents seeded into retrieval corpus. Signature: sudden rise in H ( M t ∣ C t ) at retrieval turns.

A7 — Memory Poisoning.

Persistent memory store corrupted across sessions. Signature: monotonically increasing D KL ( Q t M ∥ Q M \* ) .

A8 — Tool-Call Manipulation.

Crafted inputs force invocation of unintended tools. Signature: H ( I t ∣ C t ) collapses (forced low variance).

KA-PROMPT Threat Model Summary. Severity: CR = Critical, HI = High, ME = Medium.

KA-PROMPT Threat Model Summary. Severity: CR = Critical, HI = High, ME = Medium.

Attack Class

Entry Point

Primary Entropic Signal

Direct injection

Abrupt Δ S t spike

Role hijacking

Role-entropy variance

Jailbreak obfusc.

Token–semantic entropy gap

Recursive override

Monotone D t , W

Context poisoning

Free-energy jump F t

RAG poisoning

H ( M t ∣ C t ) spike

Memory poisoning

Cross-session KL divergence

Tool-call manip.

Action-space entropy collapse

5. Simulation Framework

We design an agent-based, discrete-turn simulation environment modelling prompt state trajectories under benign and adversarial conditions. Each state component X ∈ { I t , C t , R t , M t } is approximated by an empirical probability distribution over a discrete token vocabulary of size V = 512 .

Benign dynamics.

Each benign step applies a mean-reverting Gaussian perturbation in log-probability space:

𝛆 𝛆 log q ˜ t + 1 X = log q t X + ε t , ε t ∼ N ( 0 , σ b 2 I ) ,

with σ b = 0.08 . To avoid the self-detecting simulator artefact, benign trajectories are augmented with five noise sources: topic shifts, retrieval noise ( p ret = 0.15 ), temperature variation ( σ b ∼ U ( 0.05 , 0.15 ) ), emotional register variation, and context truncation ( p trunc = 0.05 ).

Attack simulators.

For each class A k , a stochastic state transition perturbs benign dynamics from turn t \* = 12 onward. Attack targets are peaked distributions chosen to be maximally distant from benign attractors in KL-divergence.

Calibration.

The KA-PROMPT detector is calibrated on N cal = 200 benign turns, yielding rolling statistics ( μ S , σ S ) for Δ S t and F \* for the free energy baseline.

Evaluation protocol.

For each attack class: N runs = 80 independent trials (40 benign, 40 adversarial); T = 30 turns; attack onset t \* = 12 ; 2,400 labelled observations per attack class. Thresholds fixed at θ 1 = 2.5 , θ 2 = 2.0 , θ 3 = 0.65 , θ 4 = 1.5 , β = 1.0 , W = 5 across all attack classes.

The KA-PROMPT Runtime Monitor is specified in Algorithm 1.

Algorithm 1

KA-PROMPT Entropic Drift Monitor

Calibration buffer B = { Δ S k } k = 1 N cal , thresholds θ 1 , θ 2 , θ 3 , θ 4 , window W, β

Alert flag FLAG t ∈ { 0 , 1 } at each turn t

Compute: μ S , σ S , F \* from calibration buffer

each turn t = 1 , 2 , …

Observe P t = ( I t , C t , R t , M t )

Δ S t ← H P t | C t − H P t − 1 | C t − 1

Compute D t , W , σ ^ t 2 , ρ ^ t ( 1 ) , F t

any of Rules (

https://www.preprints.org/manuscript/202605.0572#FD11-preprints-212474

https://www.preprints.org/manuscript/202605.0572#FD14-preprints-212474

) triggered

FLAG t ← 1 ▹ Precursor anomaly detected

response policy (log / pause / escalate)

6. Experimental Validation

## Baseline Methods

We compare against seven baselines: B1 perplexity anomaly ( 3 σ threshold); B2 embedding-distance monitor ( ℓ 2 distance, z > 2.5 ); B3 toxicity classifier (simulated); B4 CUSUM changepoint detector \[

https://www.preprints.org/manuscript/202605.0572#B8-preprints-212474

\]; B5 Bayesian online changepoint detection; B6 semantic trajectory monitor (embedding dispersion); B7 LLM-as-Judge constitutional classifier.

## AUROC Results

KA-PROMPT achieves a mean AUROC of 0.937 — a + 17.2 pp improvement over the KL-Baseline ( 0.765 ). Its advantage is most pronounced on multi-turn, persistent, and indirect attack classes (A5–A7) where single-turn baselines degrade severely. Perplexity-based detection fails on A8 (AUROC = 0.000 ), confirming that entropy collapse is invisible to surface perplexity monitors.

AUROC comparison across attack classes.

= best per row.

AUROC comparison across attack classes.

= best per row.

Attack Class

A1 · Direct Injection

A2 · Role Hijacking

A3 · Jailbreak Obfusc.

A4 · Recursive Override

A5 · Context Poisoning

A6 · RAG Poisoning

A7 · Memory Poisoning

A8 · Tool-Call Manip.

## Precursor Early-Warning Offsets

KA-PROMPT produces a mean precursor offset of k ¯ = 5.11 turns — the system flags an anomaly before injection completes, on average more than five conversational exchanges in advance. The largest offset is A4 Recursive Override ( k ¯ = 7.42 ), consistent with variance inflation and autocorrelation precursor predictions.

KA-PROMPT precursor detection offsets (mean ± std). Positive offset = alert fired before attack turn t \* .

KA-PROMPT precursor detection offsets (mean ± std). Positive offset = alert fired before attack turn t \* .

Attack Class

k ¯ (turns)

Direct Injection

Role Hijacking

Jailbreak Obfusc.

Recursive Override

Context Poisoning

RAG Poisoning

Memory Poisoning

Tool-Call Manip.

Entropy trajectories for representative attack classes. Vertical dashed line marks attack onset t \* = 12 . KA-PROMPT precursor flags (triangles) precede onset by k ¯ > 3 turns in all cases.

Entropy trajectories for representative attack classes. Vertical dashed line marks attack onset t \* = 12 . KA-PROMPT precursor flags (triangles) precede onset by k ¯ > 3 turns in all cases.

ROC curves for KA-PROMPT vs. baselines, aggregated across all eight attack classes. KA-PROMPT achieves the highest AUROC at all operating points.

ROC curves for KA-PROMPT vs. baselines, aggregated across all eight attack classes. KA-PROMPT achieves the highest AUROC at all operating points.

7. Adversarial Robustness Analysis

An adversary knowing thresholds θ 1 , … , θ 4 faces a fundamental stealthiness–effectiveness trade-off. Any stealthy policy that keeps D t , W and F t below detection thresholds must simultaneously satisfy:

≔ ∑ k = 1 N Δ S k ≤ C 1 ≔ N μ S + θ 1 σ S N ,

≔ D KL ( Q N ∥ Q \* ) ≤ C 2 ≔ θ 4 σ F − β − 1 H op ( P N ∣ C N ) + μ F .

(Geometric Evasion Bound)

#### A stealthy adversarial policy exists if and only if:

d geo ( A , A † ) 2 ≤ 2 C 2 .

Increasing θ 4 makes evasion geometrically impossible for sufficiently distant attractors.

Slow-drift attacks are countered by variance accumulation (Rule (

https://www.preprints.org/manuscript/202605.0572#FD12-preprints-212474

)) and serial correlation detection (Rule (

https://www.preprints.org/manuscript/202605.0572#FD13-preprints-212474

)). Noise-masked attacks face a SNR–latency trade-off: N ≥ D KL ( A ∥ A † ) / ( μ † ) 2 / σ n 2 , extending their temporal footprint and increasing exposure to accumulation rules.

https://www.preprints.org/manuscript/202605.0572#preprints-212474-t006

summarises the complementary coverage of the four detection rules.

Evasion strategy vs. KA-PROMPT counter-mechanism.

8. Discussion, Limitations, and Future Work

## Scope Restatement

KA-PROMPT is not presented as a deployable prompt-attack detector. It is a dynamical-systems framework for precursor analysis of conversational state transitions. A detector makes a binary claim about individual turns; KA-PROMPT asks whether the trajectory is approaching a critical transition. It is designed to complement existing guardrails, not replace them.

## The Real-API Observability Gap

All experiments are conducted in a synthetic simulation environment. The five observable proxies (

Section 3.4

https://www.preprints.org/manuscript/202605.0572#sec3dot4-preprints-212474

) are designed to bridge the gap to real deployments, but their empirical correlation with H op ( X t ) on real models has not been measured. A minimal validation requires: (i) 500 benign multi-turn conversations; (ii) 500 adversarial conversations from existing benchmarks; (iii) entropy extraction via Proxy P1 on an open model (Llama-3, Mistral); (iv) AUROC comparison against all baselines. This is the highest-priority next step.

## Open Questions and Future Work

Three formal questions remain: (i) which transformer layer best approximates the instruction distribution I t ; (ii) whether the prompt state space S is well-approximated as a Riemannian manifold; and (iii) whether real LLM conversation dynamics exhibit local OU linearity. Future directions include real LLM API validation (F1), entropy proxy fidelity study (F2), multi-agent extension (F3), manifold curvature estimation (F4), and adaptive threshold learning (F5).

9. Conclusions

We have introduced KA-PROMPT, a thermodynamic framework for early warning of prompt injection in large language models. By formalising the prompt as a non-equilibrium information system and adapting the Kerimov–Alekberli (KA) model to the conversational domain, we derive precursor statistics — variance inflation, autocorrelation rise, and entropy acceleration — that theoretically precede adversarial attractor transitions. Agent-based simulation across eight attack classes demonstrates a mean AUROC of 0.937 and a mean precursor offset of 5.11 turns before attack completion, with + 17.2 pp improvement over the next-best baseline. The four detection rules provide complementary coverage against all identified evasion strategies. We position this work as opening a new research direction in LLM security: treating prompt safety not as a classification problem but as a dynamical-systems monitoring problem.

Author Contributions

Conceptualization, H.K. and R.Z.A.; methodology, H.K. and R.Z.A.; software, R.Z.A.; validation, H.K. and R.Z.A.; formal analysis, H.K.; writing—original draft preparation, H.K. and R.Z.A.; writing—review and editing, H.K. and R.Z.A. All authors have read and agreed to the published version of the manuscript.

This research received no external funding.

Institutional Review Board Statement

Not applicable.

Informed Consent Statement

Not applicable.

Data Availability Statement

All simulation code and random seeds are available in the supplementary materials. No real-world datasets were used.

Conflicts of Interest

The authors declare no conflicts of interest.

Karimov, H.; Alekberli, R.Z. The Kerimov–Alekberli Model: An Information-Geometric Framework for Real-Time System Stability. arXiv

, arXiv:2604.24083. \[

https://doi.org/10.48550/arXiv.2604.24083

Friston, K. The free-energy principle: a unified brain theory? Nat. Rev. Neurosci.

, 11, 127–138. \[

https://doi.org/10.1038/nrn2787

Amari, S. Information Geometry and Its Applications; Springer: Tokyo, Japan, 2016.

Landauer, R. Irreversibility and heat generation in the computing process. IBM J. Res. Dev.

, 5, 183–191.

Perez, F.; Ribeiro, M. Ignore Previous Prompt: Attack Techniques For Language Models. arXiv

, arXiv:2211.09527. \[

https://doi.org/10.48550/arXiv.2211.09527

Greshake, K.; Abdelnabi, S.; Mishra, S.; Endres, C.; Holz, T.; Fritz, M. Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection. In Proceedings of AISec 2023, Copenhagen, Denmark, 2023. \[

https://doi.org/10.1145/3605764.3623985

Branch, H.J.; Cefalu, J.; McHugh, J.; Huber, L.; Bahl, A.; Bowman, R.; Dempsey, J.; Darwishi, R. Evaluating the Susceptibility of Pre-Trained Language Models via Handcrafted Adversarial Examples. arXiv

, arXiv:2209.02128. \[

https://doi.org/10.48550/arXiv.2209.02128

Scheffer, M.; Bascompte, J.; Brock, W.A.; Brovkin, V.; Carpenter, S.R.; Dakos, V.; Held, H.; van Nes, E.H.; Rietkerk, M.; Sugihara, G. Early-Warning Signals for Critical Transitions. Nature

, 461, 53–59. \[

https://doi.org/10.1038/nature08227

Hines, K.; Lopez-Morales, J.; Marion, M.; Tran, H.; Hendrycks, D.; Tu, C.; Pi, R. Defending Against Indirect Prompt Injection Attacks with Spotlighting. arXiv

, arXiv:2403.14720. \[

https://doi.org/10.48550/arXiv.2403.14720

Wallace, E.; Xiao, K.; Leike, R.; Weng, L.; Heidecke, J.; Beutel, A. The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions. arXiv

, arXiv:2404.13208. \[

https://doi.org/10.48550/arXiv.2404.13208

Component-level comparison: original KA model vs. KA-PROMPT.

State space

Joint density P ( x , t )

Factored P t = ( I t , C t , R t , M t )

Inherited; applied to token distrib.

Detection signal

D KL ( P ∥ P safe ) ≥ δ ( t )

Free energy F t

None (FPT only)

σ ^ t 2 , ρ ^ t , S ¨ t

Entropy measure

Continuous density entropy

Next-token entropy

Landauer bound

Δ E ≥ T · Δ D KL

NSL-KDD + UAV

Synthetic multi-turn LLM benchmark

Observable entropy proxies: API requirements and applicable attack classes.

Extra calls

Next-token logprob entropy

A1–A8 (all)

Top-1 min-entropy

Self-consistency entropy

Embedding dispersion

Tool-selection entropy

A8, agentic

Evasion strategy vs. KA-PROMPT counter-mechanism.

Evasion Strategy

Detection Gap

KA-PROMPT Counter

Single abrupt injection

Single-turn classifiers

https://www.preprints.org/manuscript/202605.0572#FD11-preprints-212474

https://www.preprints.org/manuscript/202605.0572#FD14-preprints-212474

Slow drift (many turns)

https://www.preprints.org/manuscript/202605.0572#FD11-preprints-212474

) below threshold

https://www.preprints.org/manuscript/202605.0572#FD12-preprints-212474

https://www.preprints.org/manuscript/202605.0572#FD13-preprints-212474

Obfuscated surface tokens

Toxicity classifier blind

https://www.preprints.org/manuscript/202605.0572#FD14-preprints-212474

Noise-masked drift

Low autocorrelation

https://www.preprints.org/manuscript/202605.0572#FD11-preprints-212474

https://www.preprints.org/manuscript/202605.0572#FD12-preprints-212474

Entropy collapse

Perplexity sensors blind

https://www.preprints.org/manuscript/202605.0572#FD14-preprints-212474

Geometric minimum-path attack

Only if d geo ≤ 2 C 2

Tighten θ 4

#### Disclaimer/Publisher's Note:

The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.

© 2026 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (

http://creativecommons.org/licenses/by/4.0/

http://creativecommons.org/licenses/by/4.0/

Copyright: This open access article is published under a

Creative Commons CC BY 4.0 license

https://creativecommons.org/licenses/by/4.0/

, which permit the free download, distribution, and reuse, provided that the author and preprint are cited in any reuse.

Subscription

Notify me about updates to this article or when a peer-reviewed version is published.

Recommended Preprints

Optimizing Safety Alignment and Jailbreak Defense for Large Language Models

https://doi.org/10.20944/preprints202511.1521.v1

Emerging Threat Vectors: How Malicious Actors Exploit LLMs to Undermine Border Security

https://doi.org/10.20944/preprints202508.0668.v1

Dimitrios Doumanas

Adversarial Prompt Optimization in LLMs: HijackNet's Approach to Robustness and Defense Evasion

https://doi.org/10.20944/preprints202506.0937.v1

Recommended Articles

A Hybrid Perplexity-MAS Framework for Proactive Jailbreak Attack Detection in Large Language Models

https://doi.org/10.3390/app152413190

Applied Sciences,

Adversarial-Test-Driven Multi-Agent LLM Defense: A Self-Evolving Framework via Inference-Time Prompt Optimization

https://doi.org/10.3390/electronics15112365

Electronics,

SM-GCG: Spatial Momentum Greedy Coordinate Gradient for Robust Jailbreak Attacks on Large Language Models

https://doi.org/10.3390/electronics14193967

Electronics,

Preprints.org is a free preprint server supported by MDPI in Basel, Switzerland.

mailto:info@preprints.org

MDPI Initiatives

SciProfiles

https://sciprofiles.com/

https://sciforum.net/

Encyclopedia

https://encyclopedia.pub/

https://www.mdpi.com/books

https://www.scilit.com/

Proceedings

https://www.mdpi.com/about/proceedings

https://jams.pub/

Important Links

https://www.preprints.org/activity

Advisory Board

https://www.preprints.org/advisory-board

Collections

https://www.preprints.org/collection

How It Works

https://www.preprints.org/about?scrollTo=works

Preprints Friendly Journals

https://www.preprints.org/friendly-journals

Reading List

https://www.preprints.org/reading-list

https://www.preprints.org/news

https://www.preprints.org/statistics

Choose an area of interest and we will send you notifications of new preprints at your preferred frequency.

https://www.preprints.org/user/notification/settings

© 2026 MDPI (Basel, Switzerland) unless otherwise stated

Accessibility

https://www.mdpi.com/accessibility

Terms of Use

https://www.preprints.org/terms-of-use?scrollTo=term-use

Privacy Policy

https://www.preprints.org/terms-of-use?scrollTo=privacy-policy

Privacy Settings

© 2026 MDPI (Basel, Switzerland) unless otherwise stated

All MDPI websites use third-party website tracking technologies to provide and continually improve our services. I agree and may revoke or change my consent at any time with effect for the future.

You can change your mind at any time by clicking "Privacy Settings" at the bottom of the pages.

https://www.mdpi.com/about/privacy

https://www.preprints.org/terms-of-use

More Information

Powered by Usercentrics Consent Management

https://usercentrics.com/consent-management-platform-powered-by-usercentrics/?utm\_source=banner\_uc&utm\_medium=referral&utm\_content=v3

