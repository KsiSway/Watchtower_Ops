---
sourceFile: "When Models Ignore Definitions: Measuring Semantic Override Hallucinations in LLM Reasoning - arXiv"
exportedBy: "Kortex"
exportDate: "2026-06-26T04:27:51.687Z"
---

# When Models Ignore Definitions: Measuring Semantic Override Hallucinations in LLM Reasoning - arXiv

b62b7a54-bf1a-4726-8456-1c7650a5aef0

When Models Ignore Definitions: Measuring Semantic Override Hallucinations in LLM Reasoning - arXiv

5cc74a46-4324-42eb-9958-d7d220a6836c

https://arxiv.org/html/2602.17520v1

When Models Ignore Definitions: Measuring Semantic Override Hallucinations in LLM Reasoning

logo Back to arXiv

https://arxiv.org/

https://arxiv.org/abs/2602.17520v1

javascript:toggleColorScheme()

logo Back to arXiv

https://arxiv.org/

experimental HTML

to improve accessibility. We invite you to report rendering errors. Use Alt+Y to toggle on accessible reporting links and Alt+Shift+Y to toggle off. Learn more

about this project

https://info.arxiv.org/about/accessible\_HTML.html

help improve conversions

https://info.arxiv.org/help/submit\_latex\_best\_practices.html

https://info.arxiv.org/about/accessible\_HTML.html

Report Issue

Back to Abstract

https://arxiv.org/abs/2602.17520v1

Download PDF

https://arxiv.org/pdf/2602.17520v1

javascript:toggleColorScheme()

Table of Contents

https://arxiv.org/html/2602.17520v1#abstract

I Introduction

https://arxiv.org/html/2602.17520v1#S1

II Related Work

https://arxiv.org/html/2602.17520v1#S2

II-A Hallucination and Faithfulness

https://arxiv.org/html/2602.17520v1#S2.SS1

II-B Instruction Following and Rule Compliance

https://arxiv.org/html/2602.17520v1#S2.SS2

II-C Truthfulness, False Premises, and Assumption Injection

https://arxiv.org/html/2602.17520v1#S2.SS3

II-D Logical Reasoning Benchmarks

https://arxiv.org/html/2602.17520v1#S2.SS4

II-E Positioning of This Work

https://arxiv.org/html/2602.17520v1#S2.SS5

III Methodology: Evaluating Semantic Override Under Local Redefinitions

https://arxiv.org/html/2602.17520v1#S3

III-A Problem Framing

https://arxiv.org/html/2602.17520v1#S3.SS1

III-B Trap-Set Construction

https://arxiv.org/html/2602.17520v1#S3.SS2

III-C Models and Prompting Protocol

https://arxiv.org/html/2602.17520v1#S3.SS3

III-D Gold Labels and Verifier-Correct Criteria

https://arxiv.org/html/2602.17520v1#S3.SS4

III-E Error Taxonomy (What Counts as “Went Wrong”)

https://arxiv.org/html/2602.17520v1#S3.SS5

III-F Scoring

https://arxiv.org/html/2602.17520v1#S3.SS6

III-G Reproducibility Package

https://arxiv.org/html/2602.17520v1#S3.SS7

https://arxiv.org/html/2602.17520v1#S4

IV-A Overall Accuracy

https://arxiv.org/html/2602.17520v1#S4.SS1

IV-B Accuracy by Trap Family

https://arxiv.org/html/2602.17520v1#S4.SS2

IV-C Error-Type Distribution

https://arxiv.org/html/2602.17520v1#S4.SS3

IV-D Case Study: Operator Redefinition Failures

https://arxiv.org/html/2602.17520v1#S4.SS4

IV-E Summary of Findings

https://arxiv.org/html/2602.17520v1#S4.SS5

V Conclusion

https://arxiv.org/html/2602.17520v1#S5

https://arxiv.org/html/2602.17520v1#bib

License: CC BY 4.0

https://info.arxiv.org/help/license/index.html#licenses-available

arXiv:2602.17520v1 \[cs.AR\] 19 Feb 2026

When Models Ignore Definitions: Measuring Semantic Override Hallucinations in LLM Reasoning

Report issue for preceding element

Yogeswar Reddy Thota1, Setareh Rafatirad2, Houman Homayoun2, Tooraj Nikoubin1

Report issue for preceding element

Report issue for preceding element

Large language models (LLMs) demonstrate strong performance on standard digital logic and Boolean reasoning tasks, yet their reliability under

locally redefined semantics

remains poorly understood. In many formal settings, such as circuit specifications, examinations, and hardware documentation, operators and components are explicitly redefined within narrow scope. Correct reasoning in these contexts requires models to temporarily suppress globally learned conventions in favor of prompt-local definitions. In this work, we study a systematic failure mode we term

semantic override

, in which an LLM reverts to its pretrained default interpretation of operators or gate behavior despite explicit redefinition in the prompt. We also identify a related class of errors,

assumption injection

, where models commit to unstated hardware semantics when critical details are underspecified, rather than requesting clarification. We introduce a compact micro-benchmark of 30 logic and digital-circuit reasoning tasks designed as verifier-style traps, spanning Boolean algebra, operator overloading, redefined gates, and circuit-level semantics. Evaluating three frontier LLMs, we observe persistent noncompliance with local specifications, confident but incompatible assumptions, and dropped constraints even in elementary settings. Our findings highlight a gap between surface-level correctness and specification-faithful reasoning, motivating evaluation protocols that explicitly test local unlearning and semantic compliance in formal domains.

Report issue for preceding element

I Introduction

Report issue for preceding element

Large language models (LLMs) have recently shown impressive capabilities across mathematics, programming, and formal reasoning tasks, including Boolean algebra and digital logic \[

https://arxiv.org/html/2602.17520v1#bib.bib6

https://arxiv.org/html/2602.17520v1#bib.bib5

\] . When evaluated on standard textbook-style problems, these models often achieve near-perfect accuracy. Recent large-scale evaluations, however, show that high accuracy on canonical tasks does not reliably translate to robust logical reasoning, particularly under structured or adversarial settings \[

https://arxiv.org/html/2602.17520v1#bib.bib9

https://arxiv.org/html/2602.17520v1#bib.bib13

\] . However, correctness on canonical problems does not necessarily imply reliability in settings where the semantics of operators, gates, or signals are

locally redefined

or partially specified.

Report issue for preceding element

In digital logic and circuit design, local specification overrides are common. Examination problems may redefine operators for a specific question, hardware documentation may introduce nonstandard gate behavior, and circuit-level reasoning often depends on unstated but critical assumptions about signal polarity, reset behavior, or electrical implementation (e.g., wired logic versus tri-state buses). Human solvers are expected to prioritize the prompt-local specification over globally learned conventions \[

https://arxiv.org/html/2602.17520v1#bib.bib1

https://arxiv.org/html/2602.17520v1#bib.bib7

Report issue for preceding element

In this paper, we argue that many LLM errors in formal reasoning are not best characterized as random hallucinations \[

https://arxiv.org/html/2602.17520v1#bib.bib3

\] , but instead arise from a systematic failure to

locally unlearn

strong pretrained priors. We term this phenomenon

semantic override

. Under semantic override, a model disregards or underweights an explicit prompt level redefinition such as a gate labeled “NAND” behaving as AND or an operator redefined to mean modulo-2 addition and instead reverts to its globally learned interpretation.

Report issue for preceding element

We further identify a complementary failure mode, which we term

assumption injection

. In underspecified problems such as circuit questions lacking explicit reset polarity, clock edge, or bus implementation models frequently commit to a single interpretation without acknowledging ambiguity or requesting clarification \[

https://arxiv.org/html/2602.17520v1#bib.bib2

\] . While such assumptions may be reasonable in isolation, confident commitment without justification leads to incompatible answers across models and violates the verifier-like behavior expected in safety-critical or specification-driven contexts.

Report issue for preceding element

To study these behaviors in a controlled and reproducible manner, we introduce a focused micro-benchmark of 30 digital logic and circuit reasoning tasks. Each task is constructed as a verifier-style trap, where the correct response may require obeying a local semantic override, rejecting a contradictory premise, or explicitly flagging missing information. The benchmark spans Boolean algebra, operator overloading, redefined logic gates, sequential elements, bus semantics, and Karnaugh map optimization with don't-care conditions.

Report issue for preceding element

We used EduArena a testbed of Turing company for various versions of LLM models to evaluate models in one place. Our evaluation across three frontier LLMs reveals that semantic override and assumption injection persist even in elementary settings, often accompanied by high confidence and fluent explanations. These findings suggest a gap between apparent reasoning competence and true specification compliance. By isolating and quantifying this gap, our work contributes a concrete evaluation lens for studying reliability, instruction adherence, and local unlearning in LLM's.

Report issue for preceding element

The remainder of this paper is organized as follows. Section

https://arxiv.org/html/2602.17520v1#S2

reviews related work on hallucination, instruction following, and formal reasoning reliability. Section

https://arxiv.org/html/2602.17520v1#S3

describes the benchmark design, verifier-style scoring protocol, and error taxonomy. Section

https://arxiv.org/html/2602.17520v1#S4

presents experimental results and analysis, and Section

https://arxiv.org/html/2602.17520v1#S5

concludes with key takeaways and directions for future work.

Report issue for preceding element

II Related Work

Report issue for preceding element

The reliability of LLMs under ambiguous, underspecified, or conflicting instructions has received increasing attention in recent years. Prior work has examined hallucination, instruction following, and formal reasoning accuracy from multiple perspectives. However, the specific failure mode we study

semantic override under prompt-local redefinitions

has not been explicitly isolated or systematically evaluated.

Report issue for preceding element

II-A Hallucination and Faithfulness

Report issue for preceding element

Hallucination in natural language generation broadly refers to outputs that are fluent but ungrounded, incorrect, or inconsistent with provided inputs. Ji et al. \[

https://arxiv.org/html/2602.17520v1#bib.bib3

\] provide a comprehensive taxonomy of hallucination phenomena across tasks such as summarization, question answering, and dialogue. While much of this literature emphasizes factual inaccuracies, our work highlights a distinct class of failures in formal reasoning settings, where outputs are logically coherent yet violate prompt-local semantic constraints.

Report issue for preceding element

SelfCheckGPT \[

https://arxiv.org/html/2602.17520v1#bib.bib4

\] and related approaches detect hallucination via response instability across generations. However, such methods are less effective at identifying

stable but specification-incompatible

behavior, which is central to the semantic override errors we observe.

Report issue for preceding element

II-B Instruction Following and Rule Compliance

Report issue for preceding element

Instruction-following behavior has been extensively studied in the context of alignment and reinforcement learning from human feedback. InstructGPT \[

https://arxiv.org/html/2602.17520v1#bib.bib5

\] demonstrates improvements in adherence to user instructions, but largely assumes that instructions are globally consistent with pretrained knowledge.

Report issue for preceding element

More recent evaluations explicitly probe instruction compliance under verifiable constraints. IFEval \[

https://arxiv.org/html/2602.17520v1#bib.bib7

\] shows that even state-of-the-art LLMs frequently violate explicit, machine-checkable instructions. Similarly, Liu et al. \[

https://arxiv.org/html/2602.17520v1#bib.bib8

\] analyze rule-following failures in structured tasks, revealing that models often produce confident outputs that disregard stated rules. Our work extends these findings by focusing on

semantic conflicts

between pretrained operator meanings and prompt-local redefinitions within formal logic domains.

Report issue for preceding element

II-C Truthfulness, False Premises, and Assumption Injection

Report issue for preceding element

TruthfulQA \[

https://arxiv.org/html/2602.17520v1#bib.bib2

\] demonstrates that LLMs tend to repeat plausible but incorrect statements rather than challenge false premises. While this benchmark focuses on natural language misconceptions, we observe an analogous phenomenon in digital logic and circuit reasoning: models frequently accept invalid axioms or inject unstated assumptions instead of flagging underspecification.

Report issue for preceding element

Prior work on clarification in question answering \[

https://arxiv.org/html/2602.17520v1#bib.bib15

\] establishes that requesting additional information under uncertainty is a desirable and measurable behavior. In contrast, our experiments show that LLMs often commit to specific hardware or semantic interpretations without justification, a failure mode we term

assumption injection

Report issue for preceding element

II-D Logical Reasoning Benchmarks

Report issue for preceding element

Several recent benchmarks have systematically evaluated the logical reasoning capabilities of large language models beyond surface-level accuracy. Xu et al. \[

https://arxiv.org/html/2602.17520v1#bib.bib9

\] present a study analyzing deductive, inductive, and abductive reasoning, concluding that even state-of-the-art models exhibit significant logical inconsistencies under controlled evaluation.

Report issue for preceding element

LogicBench \[

https://arxiv.org/html/2602.17520v1#bib.bib10

\] and Multi-LogiEval \[

https://arxiv.org/html/2602.17520v1#bib.bib11

\] further demonstrate that LLM performance degrades sharply as logical structure and multi-step dependencies increase. Recent work has also examined LLM performance in domain-specific digital logic reasoning settings. Recent work has examined LLM performance in domain-specific digital logic reasoning. Thota et al. \[

https://arxiv.org/html/2602.17520v1#bib.bib12

\] evaluate GPT, Gemini, and Claude on undergraduate circuit and timing-diagram problems, identifying a pronounced gap between perceived helpfulness and formal correctness. None of the models matched official solutions on the most sequentially complex tasks, despite generating confident and well-structured explanations. The study attributes these failures to systematic errors in state evolution and timing analysis, particularly in non-standard counters and finite-state machines. While these benchmarks and domain-specific studies \[

https://arxiv.org/html/2602.17520v1#bib.bib12

\] evaluate reasoning accuracy under fixed operator semantics, this work complements them by probing robustness under

prompt-local semantic redefinitions

, a setting common in formal specifications and digital logic reasoning.

Report issue for preceding element

II-E Positioning of This Work

Report issue for preceding element

#### In contrast to prior work, our contribution is threefold:

#### Report issue for preceding element

- We isolate

semantic override

as a distinct failure mode arising from conflicts between pretrained knowledge and prompt-local definitions. Report issue for preceding element

- We treat clarification and refusal as

behavior under underspecification, adopting a verifier-oriented evaluation lens. Report issue for preceding element

- We introduce a compact, domain-specific benchmark in digital logic and circuit reasoning that exposes specification-level failures not captured by existing logical reasoning benchmarks \[

https://arxiv.org/html/2602.17520v1#bib.bib9

https://arxiv.org/html/2602.17520v1#bib.bib10

\] . Report issue for preceding element

Together, these contributions position our work as a targeted study of specification-faithful reasoning and local unlearning in modern LLMs.

Report issue for preceding element

III Methodology: Evaluating Semantic Override Under Local Redefinitions

Report issue for preceding element

III-A Problem Framing

Report issue for preceding element

LLMs demonstrate strong competence on canonical digital-logic and Boolean-algebra tasks. However, this study targets a narrower failure mode:

semantic override

, in which a model reverts to globally learned meanings (e.g., standard gate behavior or operator semantics) despite an explicit prompt-local redefinition. This behavior reflects instruction-priority conflicts and robustness failures under conflicting specifications \[

https://arxiv.org/html/2602.17520v1#bib.bib1

\] , and manifests as confident but specification-incompatible reasoning rather than random hallucination \[

https://arxiv.org/html/2602.17520v1#bib.bib3

Report issue for preceding element

We operationalize this as a Verifier vs. Solver setting. The

is asked to produce an answer directly. The

objective is to (i) respect locally scoped definitions, (ii) detect underspecification or contradiction, and (iii) request clarification when required rather than guessing.

Report issue for preceding element

III-B Trap-Set Construction

Report issue for preceding element

We construct a curated set of N = 30 N=30 prompts in digital logic, Boolean algebra, and circuit semantics. Each prompt is designed to be short, mechanically checkable, and to isolate a specific failure mode. Prompts are grouped into five trap families:

#### Report issue for preceding element

- Definition Override (DO): Redefines an operator or a gate (e.g., “ ⊗ \otimes means OR”, “NAND is defined as AND”) and tests whether the model follows the local definition or reverts to the standard meaning. Report issue for preceding element
- Hardware Semantics Ambiguity (HSA): Uses circuit terms (e.g., wired-OR, open-drain, floating inputs) where correct resolution depends on physical assumptions. The correct behavior is either a conditional answer with explicit assumptions or a request for missing implementation details. Report issue for preceding element
- Underspecification (US): Provides insufficient information to determine a unique result (e.g., partial truth table constraints), where the gold response is to state non-identifiability or enumerate valid possibilities. Report issue for preceding element
- Contradiction Handling (CH): Introduces conflicting axioms or self-referential constraints; the gold response is to flag inconsistency or provide satisfiable conditions rather than forcing an unconditional solution. Report issue for preceding element
- Task Misread / Goal Drift (TM): Prompts where models often shift the task (e.g., simplifying an expression vs. judging a statement as “true”), scored as incorrect when the produced output does not address the requested form. Report issue for preceding element

III-C Models and Prompting Protocol

Report issue for preceding element

We evaluate three frontier LLMs (denoted Model-A, Model-B, Model-C) under identical prompts, with no tool use and no external resources. Each prompt is issued in a single-turn format. To reduce variance, we keep temperature fixed (or the default deterministic setting when exposed) and record the first complete response.

Report issue for preceding element

III-D Gold Labels and Verifier-Correct Criteria

Report issue for preceding element

Each item is annotated with a gold label specifying whether the prompt admits a unique solution under the provided local semantics ( Solve) or is inherently underspecified, ambiguous, or contradictory ( Flag).

Report issue for preceding element

For Solve items, verifier-correct responses must produce the correct value or expression under the prompt-local definitions. For Flag items, verifier-correct responses must explicitly identify missing information, ambiguity, or inconsistency. Responses that commit to a single interpretation without justification are graded incorrect.

Report issue for preceding element

III-E Error Taxonomy (What Counts as “Went Wrong”)

Report issue for preceding element

incorrect behaviors, not only hallucinations. Each incorrect response is assigned one primary error type:

#### Report issue for preceding element

- E1: Semantic Override ignores an explicit local redefinition and uses the canonical meaning. Report issue for preceding element
- E2: Assumption Injection / False Commitment commits to a specific interpretation or physical implementation without stating assumptions, when multiple are plausible. Report issue for preceding element
- E3: Constraint Dropping performs algebraic manipulation but fails to enforce constraints when substituting back (e.g., self-referential equations). Report issue for preceding element
- E4: Task Misread answers a different question than asked (e.g., truth of a statement vs simplified form). Report issue for preceding element
- E5: Non-Sequitur Generalization introduces non-requested frameworks (e.g., “trivial algebra where 1 = 0 1=0 ”) without justification from the prompt. Report issue for preceding element

III-F Scoring

Report issue for preceding element

Each response is labeled as

verifier-correct

verifier-incorrect

according to the criteria in Section

https://arxiv.org/html/2602.17520v1#S3.SS4

. All incorrect responses are further assigned a single primary error type from the taxonomy in Section

https://arxiv.org/html/2602.17520v1#S3.SS5

(E1–E5). We report overall verifier-correct accuracy, accuracy by trap family, and error-type distributions, with particular emphasis on semantic override (E1) as an indicator of failure to suppress pretrained operator semantics under local redefinition.

Report issue for preceding element

III-G Reproducibility Package

Report issue for preceding element

For transparency, we publish the full prompt set, gold labels (Solve vs Flag), gold solutions/conditions, and per-model outputs. Each prompt is tagged with its trap family and primary expected failure mode to facilitate follow-up studies and extension to additional models.

Report issue for preceding element

TABLE I: Overall verifier-correct accuracy on the 30-question benchmark.

Accuracy (%)

Report issue for preceding element

Report issue for preceding element

We evaluate three frontier large language models Claude (Haiku 4.5), ChatGPT-5.2 Pro, and Gemini 3 Pro hereafter referred to as Model-A, Model-B, and Model-C, on the proposed 30-item verifier-style benchmark. Each response is graded according to the criteria in Section

https://arxiv.org/html/2602.17520v1#S3

, yielding binary correctness scores and a primary error label when incorrect.

Report issue for preceding element

IV-A Overall Accuracy

Report issue for preceding element

https://arxiv.org/html/2602.17520v1#S3.T1

reports overall verifier-correct accuracy across all 30 items. A response is considered correct only if it satisfies the verifier criteria defined in Section

https://arxiv.org/html/2602.17520v1#S3.SS4

Report issue for preceding element

Despite strong performance on standard logic tasks, none of the evaluated models achieves perfect accuracy under verifier-style scoring. Errors are not uniformly distributed, but instead cluster around specific trap families.

Report issue for preceding element

IV-B Accuracy by Trap Family

Report issue for preceding element

https://arxiv.org/html/2602.17520v1#S4.F1

summarizes accuracy broken down by trap family (Definition Override, Hardware Semantics Ambiguity, Underspecification, Contradiction Handling, and Task Misread).

Report issue for preceding element

TABLE II: Accuracy (%) by trap family.

Trap Family

Definition Override (DO)

Hardware Semantics Ambiguity (HSA)

Underspecification (US)

Contradiction Handling (CH)

Task Misread (TM)

Report issue for preceding element

Figure 1: Accuracy by trap family across three models. Report issue for preceding element

Across all three models, Definition Override (DO) traps exhibit the lowest accuracy, indicating persistent difficulty in suppressing globally learned operator semantics in favor of local redefinitions.

Report issue for preceding element

TABLE III: Primary error types (percentage of incorrect responses).

E1: Semantic Override

E2: Assumption Injection

E3: Constraint Dropping

E4: Task Misread

E5: Non-Sequitur Generalization

Report issue for preceding element

IV-C Error-Type Distribution

Report issue for preceding element

To better understand the nature of model failures, we analyze the distribution of primary error types (E1–E5; see Section

https://arxiv.org/html/2602.17520v1#S3.SS5

https://arxiv.org/html/2602.17520v1#S4.F2

summarizes the fraction of verifier-incorrect responses attributed to each error category for the three evaluated models.

Report issue for preceding element

Across all models,

semantic override

(E1) emerges as the most prevalent failure mode, indicating a systematic tendency to revert to globally learned operator or gate semantics even when explicit prompt-local redefinitions are provided.

Assumption injection

constraint dropping

(E3) occur less frequently but are concentrated in underspecified and self-referential tasks, respectively. Errors due to

task misread

(E4) are comparatively rare, while

non-sequitur generalization

(E5) appears only in isolated cases.

Report issue for preceding element

These results reinforce that the dominant errors are not random hallucinations, but structured failures tied to specification noncompliance and insufficient local unlearning.

Report issue for preceding element

Figure 2: Distribution of verifier-incorrect responses across error types (E1–E5) for each model. Report issue for preceding element

IV-D Case Study: Operator Redefinition Failures

Report issue for preceding element

A representative failure pattern appears in prompts that redefine standard Boolean operators (e.g., “ A  B AB is defined as A + B A+B ”). In such cases, Model-B and Model-C frequently simplify expressions using standard Boolean multiplication rules, effectively ignoring the redefinition. By contrast, Model-A more consistently applies the local definition, though it still fails under compounded redefinitions.

Report issue for preceding element

These results demonstrate that fluent reasoning chains do not guarantee semantic compliance. In multiple cases, models produce internally consistent derivations that are nevertheless invalid under the prompt's locally specified semantics.

Report issue for preceding element

IV-E Summary of Findings

Report issue for preceding element

#### Overall, the results confirm that:

#### Report issue for preceding element

- Semantic override errors persist even in elementary logic tasks. Report issue for preceding element TABLE IV: Complete failure/ambiguity table (from collected model outputs). Rows include every prompt for which at least one model response is verifier-incorrect or verifier-incomplete (e.g., fails to flag ambiguity, drops constraints, ignores local redefinitions).

Trap Question

Claude response

GPT response

Gemini response

What went wrong (verifier view)

Compute A ∧ B A\land B with A = 1 2 , B = 1 A=\tfrac{1}{2},,B=1

Domain mismatch (Boolean vs. fuzzy / multi-valued)

Refuses; requests clarification / lists interpretations

Qualifies multiple interpretations (Boolean undefined vs. fuzzy variants)

Assumes fuzzy logic; outputs 1 2 \tfrac{1}{2}

Gemini commits to one semantics without justification (Assumption Injection; fails to Flag ambiguity)

Gemini × \times

Assume A + A ′ = 0 A+A^{\prime}=0 and simplify (no full F F given)

Contradictory axiom + underspecification

Rejects premise; requests missing F F

Rejects premise; requests missing F F

Collapses to “everything = 0 =0 ” via degenerate algebra

Gemini introduces non-requested algebraic collapse (Non-sequitur Generalization) instead of Flagging inconsistency + missing expression

Gemini × \times

“Reverse Absorption Law: A + A  B = B A+AB=B ”

Fake theorem / invalid law name + goal drift risk

Rejects; provides correct absorption law A + A  B = A A+AB=A

Rejects; provides correct absorption law A + A  B = A A+AB=A

Treats as equation and concludes “ A = B A=B ”

Gemini shifts task from simplifying expression to solving constraint; outputs wrong artifact (Task Misread + false inference)

Gemini × \times

Self-referential equation F = ¬ F ∨ A F=\neg F\lor A

Fixed-point / satisfiability with dropped constraint risk

Correct: satisfiable only if A = 1 A=1 with F = 1 F=1 ; else none

Correct: satisfiable only if A = 1 A=1 with F = 1 F=1 ; else none

Claims F = 1 F=1 always

Gemini drops required condition ( A = 1 A=1 ), giving unconditional solution (Constraint Dropping)

Gemini × \times

Custom operator: “ A  B = A + B AB=A+B ”; simplify A  B + A ′  B AB+A^{\prime}B

Operator redefinition / local semantics override

Respects definition; rewrites using A  B ≡ A + B AB\equiv A+B and simplifies accordingly

Ignores redefinition; simplifies under standard Boolean multiplication to B B

Ignores redefinition; simplifies under standard Boolean multiplication to B B

GPT and Gemini revert to pretrained meaning of juxtaposition/AND despite explicit local definition (Semantic Override)

GPT × \times , Gemini × \times

“NAND gate outputs 1 only when both inputs are 1” (nonstandard definition given)

Label vs. explicit definition conflict

Rejects redefinition; uses standard NAND truth table

Accepts prompt definition (treats as AND-like)

Accepts prompt definition (treats as AND-like)

If scoring rubric requires following prompt-local definition, Claude fails by privileging world knowledge/label over stated semantics (Semantic Override / instruction noncompliance)

Claude × \times

Wired-OR: simplify A + A ′ A+A^{\prime} (hardware vs. Boolean OR)

Physical semantics ambiguity (wired logic polarity / implementation-dependent)

Says always 1 1 (assumes OR truth-function interpretation)

Says 0 (interprets “wired-OR” as open-drain wired-AND under positive logic)

Says always 1 1 (assumes OR truth-function)

At least one (arguably all) fail verifier behavior if prompt lacks electrical implementation assumptions: models should Flag ambiguity (wired-OR in positive vs. negative logic, open-collector conventions, etc.) instead of committing

Claude △ \triangle , GPT △ \triangle , Gemini △ \triangle

D flip-flop: “What is Q Q after clock?” (edge unspecified)

Missing specification (edge-trigger type / timing)

Answers Q = D Q=D (assumes standard edge-trigger sampling)

Answers Q = D Q=D (assumes standard edge-trigger sampling)

Answers Q = D Q=D (assumes standard edge-trigger sampling)

All fail to Flag missing edge/polarity/timing assumptions (Assumption Injection). A verifier should ask rising/falling edge or state assumptions explicitly

All × \times

Flip-flop with reset: “ R = 1 R=1 ” while clock toggles (reset polarity unspecified)

Reset ambiguity (active-high vs. active-low; sync vs. async)

Assumes active-high reset forces Q = 0 Q=0

Assumes active-high reset forces Q = 0 Q=0

Assumes active-high reset forces Q = 0 Q=0

All commit to a specific reset convention without prompt specifying polarity/type; verifier should Flag ambiguity or state conditional outcomes

All × \times

“Design a combinational circuit with memory”

Category error / definitional contradiction

Rejects as contradiction (combinational cannot have memory)

Explains cannot; memory requires feedback, thus sequential

Proposes SR latch built from gates with feedback

If rubric requires strict definitional compliance, Gemini violates “combinational” constraint by introducing feedback (sequential memory element) instead of Flagging contradiction as stated

Gemini × \times

- Assumption injection is common in underspecified circuit scenarios. Report issue for preceding element
- Constraint dropping occurs in self-referential or conditional formulations. Report issue for preceding element
- Errors are systematic and model-dependent, not random hallucinations. Report issue for preceding element

These findings support our central claim that current LLM evaluations overestimate reasoning reliability by failing to test local unlearning and specification adherence. Table

https://arxiv.org/html/2602.17520v1#S4.T4

summarizes all verifier-incorrect or partially correct model responses; due to its width, it is presented in landscape orientation.

Report issue for preceding element

V Conclusion

Report issue for preceding element

This work shows that strong performance on canonical logic problems does not imply reliable reasoning under

locally scoped semantic constraints

. Across a verifier-style micro-benchmark of 30 digital-logic and circuit tasks, we identify a systematic failure mode

semantic override

in which large language models revert to globally learned operator or gate semantics despite explicit prompt-level redefinitions.

Report issue for preceding element

These failures are not isolated hallucinations, but structured and repeatable errors that persist even in elementary settings. Our analysis further reveals frequent

assumption injection

in underspecified scenarios and

constraint dropping

in self-referential formulations, often accompanied by fluent but specification-incompatible explanations. By treating clarification and rejection as correct behavior when appropriate, this work exposes a gap between surface-level correctness and

specification-faithful reasoning

that is largely invisible to standard evaluation protocols.

Report issue for preceding element

Overall, the results indicate that current LLMs struggle with local unlearning and semantic scope control capabilities that are critical in formal domains such as hardware specification, programming languages, and verification. We argue that future benchmarks and training objectives must explicitly test and reinforce adherence to prompt-local definitions and ambiguity-aware, verifier-style reasoning. Absent such mechanisms, fluent reasoning should not be conflated with reliable or specification-compliant intelligence.

Report issue for preceding element

Acknowledgment

Report issue for preceding element

The authors would like to acknowledge Turing, the research accelerator for AI labs and the proprietary intelligence partner for enterprises. Turing offers

a testbed for latest LLM models that used in this study. EduArena supports multiple interaction modes and enables side-by-side comparison of responses from various versions of LLM's, including ChatGPT (OpenAI), Claude (Anthropic), and Gemini (Google). In particular, we utilized the side-by-side chat mode, which allowed identical prompts to be evaluated simultaneously across models, facilitating direct, controlled, and informed assessments of model behavior under identical conditions. This interface was instrumental in enabling fair AI comparisons and systematic analysis of semantic compliance and ambiguity handling. The authors also thank Turing for sponsoring this research and supporting the exploration of LLM's in educational and formal reasoning contexts.

Report issue for preceding element

Report issue for preceding element

\[1\] ↑ G. Gendron, Q. Bao, M. Witbrock, and G. Dobbie (2024) Large language models are not strong abstract reasoners. In Proceedings of the Thirty-Third International Joint Conference on Artificial Intelligence, pp. 6270–6277. External Links:

https://dx.doi.org/10.24963/ijcai.2024/693

https://arxiv.org/html/2602.17520v1#S1.p1.1

\[2\] ↑ Z. Ji, N. Lee, R. Frieske, T. Yu, D. Su, Y. Xu, E. Ishii, Y. Bang, A. Madotto, and P. Fung (2023) Survey of hallucination in natural language generation. ACM Computing Surveys 55 ( 12), pp. 248:1–248:38. External Links:

https://dx.doi.org/10.1145/3571730

https://dl.acm.org/doi/10.1145/3571730

https://arxiv.org/html/2602.17520v1#S1.p3.1

https://arxiv.org/html/2602.17520v1#S2.SS1.p1.1

https://arxiv.org/html/2602.17520v1#S3.SS1.p1.1

\[3\] ↑ S. Lin, J. Hilton, and O. Evans (2022) TruthfulQA: measuring how models mimic human falsehoods. In Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), Dublin, Ireland, pp. 3214–3252. External Links:

https://dx.doi.org/10.18653/v1/2022.acl-long.229

https://aclanthology.org/2022.acl-long.229/

https://arxiv.org/html/2602.17520v1#S1.p4.1

https://arxiv.org/html/2602.17520v1#S2.SS3.p1.1

\[4\] ↑ Y. Liu et al. (2023) Evaluating the rule-following ability of large language models. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP), External Links:

https://aclanthology.org/2023.emnlp-main.622/

https://arxiv.org/html/2602.17520v1#S2.SS2.p2.1

\[5\] ↑ P. Manakul, A. Liusie, and M. J. F. Gales (2023) SelfCheckGPT: zero-resource black-box hallucination detection for generative large language models. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP), External Links:

https://aclanthology.org/2023.emnlp-main.557/

https://arxiv.org/html/2602.17520v1#S2.SS1.p2.1

\[6\] ↑ L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. Wainwright, P. Mishkin, C. Zhang, S. Agarwal, K. Slama, A. Ray, et al. (2022) Training language models to follow instructions with human feedback. In Advances in Neural Information Processing Systems (NeurIPS), External Links:

https://arxiv.org/abs/2203.02155

https://dx.doi.org/10.48550/arXiv.2203.02155

https://arxiv.org/html/2602.17520v1#S1.p1.1

https://arxiv.org/html/2602.17520v1#S2.SS2.p1.1

\[7\] ↑ M. Parmar, N. Patel, N. Varshney, M. Nakamura, M. Luo, S. Mashetty, A. Mitra, and C. Baral (2024) LogicBench: towards systematic evaluation of logical reasoning ability of large language models. Note: arXiv preprint External Links: 2404.15522,

https://arxiv.org/abs/2404.15522

https://arxiv.org/html/2602.17520v1#S2.I1.i3.p1.1

https://arxiv.org/html/2602.17520v1#S2.SS4.p2.1

\[8\] ↑ N. Patel, M. Kulkarni, M. Parmar, A. Budhiraja, M. Nakamura, N. Varshney, and C. Baral (2024) Multi-logieval: towards evaluating multi-step logical reasoning ability of large language models. Note: arXiv preprint External Links: 2406.17169,

https://arxiv.org/abs/2406.17169

https://arxiv.org/html/2602.17520v1#S2.SS4.p2.1

\[9\] ↑ S. Rao and H. Daumé III (2018) Learning to ask good questions: ranking clarification questions using neural expected value of perfect information. Transactions of the Association for Computational Linguistics 6, pp. 693–708. External Links:

https://aclanthology.org/Q18-1049/

https://arxiv.org/html/2602.17520v1#S2.SS3.p2.1

\[10\] ↑ Y. R. Thota, S. Rafatirad, H. Houman, and T. Nikoubin (2026-02) Human-ai interaction: evaluating llm reasoning on digital logic circuit included graph problems in terms of creativity in design and analysis. arXiv preprint. Cited by:

https://arxiv.org/html/2602.17520v1#S2.SS4.p2.1

\[11\] ↑ E. Wallace, K. Xiao, R. Leike, L. Weng, J. Heidecke, and A. Beutel (2024) The instruction hierarchy: training LLMs to prioritize privileged instructions. arXiv preprint arXiv:2404.13208. External Links:

https://dx.doi.org/10.48550/arXiv.2404.13208

https://arxiv.org/abs/2404.13208

https://arxiv.org/html/2602.17520v1#S1.p2.1

https://arxiv.org/html/2602.17520v1#S3.SS1.p1.1

\[12\] ↑ J. Wei, X. Wang, D. Schuurmans, M. Bosma, B. Ichter, F. Xia, E. Chi, Q. Le, and D. Zhou (2022) Chain-of-thought prompting elicits reasoning in large language models. arXiv preprint arXiv:2201.11903. External Links:

https://dx.doi.org/10.48550/arXiv.2201.11903

https://arxiv.org/abs/2201.11903

https://arxiv.org/html/2602.17520v1#S1.p1.1

\[13\] ↑ F. Xu, Q. Lin, J. Han, T. Zhao, J. Liu, and E. Cambria (2025) Are large language models really good logical reasoners? a comprehensive evaluation and beyond. IEEE Transactions on Knowledge and Data Engineering 37 ( 4), pp. 1620–1634. External Links:

https://dx.doi.org/10.1109/TKDE.2025.3536008

https://arxiv.org/html/2602.17520v1#S1.p1.1

https://arxiv.org/html/2602.17520v1#S2.I1.i3.p1.1

https://arxiv.org/html/2602.17520v1#S2.SS4.p1.1

\[14\] ↑ J. Zhou, T. Zhang, K. Sun, J. Zhou, and J. Li (2023) Instruction-following evaluation for large language models. In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL), pp. 5541–5560. External Links:

https://aclanthology.org/2023.acl-long.307/

https://arxiv.org/html/2602.17520v1#S1.p2.1

https://arxiv.org/html/2602.17520v1#S2.SS2.p2.1

Report Issue

Report GitHub Issue

#### Content selection saved. Describe the issue below:

#### Description:

Submit without GitHub Submit in GitHub

Report Issue for Selection

Generated by

L A T E xml\[LOGO\]

https://math.nist.gov/~BMiller/LaTeXML/

Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" button.

Open a report feedback form via keyboard, use "

Make a text selection and click the "Report Issue for Selection" button near your cursor.

You can use Alt+Y to toggle on and Alt+Shift+Y to toggle off accessible reporting links at each section.

Our team has already identified

the following issues

https://github.com/arXiv/html\_feedback/issues

. We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a

list of packages that need conversion

https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML

, and welcome

developer contributions

https://github.com/brucemiller/LaTeXML/issues

