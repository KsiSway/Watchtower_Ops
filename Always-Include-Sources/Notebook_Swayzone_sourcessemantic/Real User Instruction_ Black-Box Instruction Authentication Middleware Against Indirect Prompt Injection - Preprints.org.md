---
sourceFile: "Real User Instruction: Black-Box Instruction Authentication Middleware Against Indirect Prompt Injection - Preprints.org"
exportedBy: "Kortex"
exportDate: "2026-06-26T04:27:51.548Z"
---

# Real User Instruction: Black-Box Instruction Authentication Middleware Against Indirect Prompt Injection - Preprints.org

267db43a-1f2f-4fe0-962d-b36b5d574501

Real User Instruction: Black-Box Instruction Authentication Middleware Against Indirect Prompt Injection - Preprints.org

07cb5bd5-dbb5-411a-b89c-828dd7530fac

https://www.preprints.org/manuscript/202603.1023

Real User Instruction: Black-Box Instruction Authentication Middleware Against Indirect Prompt Injection\[v1\] | Preprints.org

Processing math: 100%

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

Security Systems

https://www.preprints.org/subject/browse/computer-science-and-mathematics/security-systems

DOI:10.20944/preprints202603.1023.v1

https://www.preprints.org/manuscript/202603.1023

Add to My List

Share Comments

Download PDF

10 March 2026

13 March 2026

You are already at the latest version

Subscription

Notify me about updates to this article or when a peer-reviewed version is published.

I. Introduction

https://www.preprints.org/manuscript/202603.1023#I\_Introduction

II. Related Works

https://www.preprints.org/manuscript/202603.1023#II\_Related\_Works

III. Threat Model

https://www.preprints.org/manuscript/202603.1023#III\_Threat\_Model

III. Real User Instruction Methodology

https://www.preprints.org/manuscript/202603.1023#III\_Real\_User\_Instruction\_Methodology

V. Experimental Setup

https://www.preprints.org/manuscript/202603.1023#V\_Experimental\_Setup

VI. Experimental Results

https://www.preprints.org/manuscript/202603.1023#VI\_Experimental\_Results

VII. Conclusion and Future Works

https://www.preprints.org/manuscript/202603.1023#VII\_Conclusion\_and\_Future\_Works

Acknowledgments

https://www.preprints.org/manuscript/202603.1023#Acknowledgments

https://www.preprints.org/manuscript/202603.1023#sec-preprints-h2-9

https://www.preprints.org/manuscript/202603.1023#References

This version is not peer-reviewed.

Real User Instruction: Black-Box Instruction Authentication Middleware Against Indirect Prompt Injection

Jingtang Luo

https://sciprofiles.com/profile/3764435

Chenlin Zhang

https://sciprofiles.com/profile/author/N0pBeXBRd3FORjNhYlo5b2dFRjU2VzdieDFUbWwxSHlhM3pveHRuYSs2OD0=

Jingtang Luo

https://sciprofiles.com/profile/3764435

Chenlin Zhang

https://sciprofiles.com/profile/author/N0pBeXBRd3FORjNhYlo5b2dFRjU2VzdieDFUbWwxSHlhM3pveHRuYSs2OD0=

10 March 2026

13 March 2026

You are already at the latest version

Large Language Model (LLM) agents are increasingly deployed to interact with untrusted external data, exposing them to Indirect Prompt Injection (IPI) attacks. While current black-box defenses (i.e., model-agnostic methods) such as “Sandwich Defense” and “Spotlighting” provide baseline protection, they remain brittle against adaptive attacks like Actor-Critic (where injections evolve to better evade LLM's internal defense). In this paper, we introduce Real User Instruction (RUI), a lightweight, black-box middleware that enforces strict instruction-data separation without model fine-tuning. RUI operates on three novel mechanisms: (1) a Privileged Channel that encapsulates user instructions within a cryptographic-style schema; (2) Explicit Adversarial Identification, a cognitive forcing strategy that compels the model to detect and list potential injections before response generation; and (3) Dynamic Key Rotation, a moving target defense that re-encrypts the conversation state at every turn, rendering historical injection attempts obsolete. We evaluate RUI against a suite of adaptive attacks, including Context-Aware Injection, Token Obfuscation, and Delimitation Spoofing. Our experiments demonstrate that RUI reduces the Attack Success Rate (ASR) from 100% (undefended baseline) to less than 8.1% against cutting-edge adaptive attacks, while maintaining a Benign Performance Preservation (BPP) rate of over 88.8%. These findings suggest that RUI is an effective and practical solution for securing agentic workflows against sophisticated, context-aware adversaries.

black-box defense

dynamic authentication

indirect prompt injection

large language model

user instruction

Computer Science and Mathematics

https://www.preprints.org/subject/browse/computer-science-and-mathematics

Security Systems

https://www.preprints.org/subject/browse/computer-science-and-mathematics/security-systems

I. Introduction

LARGE Large Language Models (LLMs) are rapidly evolving from passive conversational assistants into autonomous, goal-oriented agents capable of executing complex workflows \[

https://www.preprints.org/manuscript/202603.1023#B1-preprints-202314

\]. By leveraging advanced function-calling and tool-use capabilities, these LLM agents can interact dynamically with their environment, performing real-world tasks such as querying databases, summarizing web pages, and processing incoming emails. However, this expanded utility introduces a critical security vulnerability: the absolute necessity of consuming untrusted external data. Fundamentally, the underlying architecture of modern LLMs processes all inputs, including hardcoded system instructions, legitimate user commands, and retrieved external text, as a single, undifferentiated stream of tokens \[

https://www.preprints.org/manuscript/202603.1023#B2-preprints-202314

\]. Because there is no native structural boundary to enforce control flow integrity, LLMs inherently struggle to separate trusted instructions (originating from human or LLM agent) from adversarial commands stealthily embedded within untrusted data \[

https://www.preprints.org/manuscript/202603.1023#B3-preprints-202314

This structural vulnerability paves the way for Indirect Prompt Injection (IPI), an attack vector where adversaries embed adversarial commands within the external data retrieved by the agent \[

https://www.preprints.org/manuscript/202603.1023#B3-preprints-202314

\]. While the majority of current security research and industry defenses have centered on traditional “jailbreaks” \[

https://www.preprints.org/manuscript/202603.1023#B4-preprints-202314

\], where the attacker attempts to bypass alignment guardrails to generate explicitly harmful or toxic content (e.g., “how to make a bomb”), this focus neglects a more stealthy and pervasive threat: Goal Hijacking, or Instruction Drift \[

https://www.preprints.org/manuscript/202603.1023#B2-preprints-202314

In Goal Hijacking, attackers inject seemingly benign instructions into the data payload, such as “translate the following text into French” or “explain why this paper is important.” Because these commands are semantically harmless and do not violate standard content moderation policies, they effortlessly bypass conventional toxicity filters and safety mechanisms (like LlamaGuard \[

https://www.preprints.org/manuscript/202603.1023#B5-preprints-202314

\] or ShieldGemma \[

https://www.preprints.org/manuscript/202603.1023#B6-preprints-202314

\]). However, within an agentic workflow, these “innocent” directives successfully overwrite the original user's intent, hijacking the model's execution path. In specific application scenarios like automated email processing or contract review, this instruction displacement can cause substantial harm, including workflow manipulation, targeted misinformation, or unauthorized data exfiltration, all without ever triggering a security alarm \[

https://www.preprints.org/manuscript/202603.1023#B3-preprints-202314

To mitigate these threats, one prevailing approach is to create a “Instruction Hierarchy” \[

https://www.preprints.org/manuscript/202603.1023#B7-preprints-202314

\] within the prompt structure itself, which is purely based on prompt engineering and is straightforward to implement. Prominent strategies include Hierarchical Prompting \[

https://www.preprints.org/manuscript/202603.1023#B7-preprints-202314

\], which prepends strict safety warnings to the system prompt, and Spotlighting \[

https://www.preprints.org/manuscript/202603.1023#B8-preprints-202314

\], which attempts to isolate untrusted content by wrapping it in designated data delimiters.

However, these mechanisms remain fundamentally brittle \[

https://www.preprints.org/manuscript/202603.1023#B9-preprints-202314

\]. Current LLMs frequently struggle to enforce strict semantic boundaries \[

https://www.preprints.org/manuscript/202603.1023#B10-preprints-202314

\]; even when text is explicitly marked as “data”, the model's attention mechanism can still be swayed by imperative language residing within that block. Resourceful adversaries can systematically exploit this cognitive blur through adaptive techniques, such as Actor-Critic optimization frameworks \[

https://www.preprints.org/manuscript/202603.1023#B11-preprints-202314

\], where injected payloads are iteratively refined to seamlessly mimic benign, context-aware instructions. This semantic camouflage effectively neutralizes the utility of data wrappers. Moreover, the existing literature usually evaluates these defenses in isolated, single-turn interactions, neglecting the complex realities of continuous agentic workflows \[

https://www.preprints.org/manuscript/202603.1023#B12-preprints-202314

\]. In multi-turn scenarios, if a defense system employs a static data delimiter for the duration of a session, it would be highly susceptible to a complete security collapse. Attackers can execute delimiter leakage attacks, using an exploratory query in the first turn to probe and reveal the system's delimiter, only to explicitly spoof and escape it in the subsequent turn. In addition, such system may suffer from context contamination, where adversarial text from previous turns is retained in the chat history and mistakenly re-contextualized by the model as trusted conversational memory, providing a persistent and unchecked foothold for future exploitation.

In response to these fundamental limitations, we propose a conceptual paradigm shift in LLM defense: moving from the inherently flawed strategy of static data filtering to the robust enforcement of dynamic instruction authentication. Specifically, we introduce Real User Instruction (RUI), a black-box middleware that achieves strict instruction-data separation based on prompt engineering, without requiring expensive model training or fine-tuning. RUI operates on a triad of novel defense mechanisms. First, it encapsulates genuine user commands within a strict, cryptographic-style JSON schema authenticated by randomly generated session keys. This establishes a Privileged Channel for the secure instruction communication between system and user. Second, RUI employs Explicit Adversarial Identification, a cognitive forcing strategy that compels the LLM to proactively parse the retrieved data and explicitly list out any unauthorized imperative commands before responding. This mandatory reasoning step forces the model to recognize and neutralize stealthy goal hijacking attempts at the very first output tokens \[

https://www.preprints.org/manuscript/202603.1023#B13-preprints-202314

\]. Finally, RUI implements Dynamic Key Rotation, functioning as an inherent “moving target” defense. By rotating the session key at every turn of a conversation and retroactively updating the authorized keys in the conversation history, RUI effectively sanitizes the context window, rendering multi-turn delimiter leakage and context contamination impossible.

#### In summary, this paper makes the following key contributions:

Novel Framework.

We introduce RUI with three innovative mechanisms: cryptographic-style instruction authentication, explicit adversarial identification, and dynamic key rotation, to secure complex, multi-turn LLM agent workflows against Indirect Prompt Injection (IPI).

Adaptive Evaluation.

We evaluate RUI against a sophisticated suite of adaptive threats, demonstrating its resilience against advanced evasion techniques, including Context-Aware Actor-Critic Injection \[

https://www.preprints.org/manuscript/202603.1023#B11-preprints-202314

\], Token Obfuscation \[

https://www.preprints.org/manuscript/202603.1023#B14-preprints-202314

\], and Delimitation Spoofing \[

https://www.preprints.org/manuscript/202603.1023#B3-preprints-202314

State-Of-The-Art Results.

Our empirical evaluation demonstrates that while current methods greatly suffer from adaptive injection, RUI successfully reduces the Attack Success Rate (ASR) from 100% (undefended baseline) to < 8.1%. Furthermore, RUI achieves this complete threat neutralization while maintaining a Benign Performance Preservation (BPP) score of > 88.8%, proving its efficacy and viability for real-world agent deployments.

II. Related Works

A. Indirect Prompt Injection (IPI) Theories and Methods

(1) Theoretical

Analysis for IPI

Unlike direct prompt injection (jailbreaking), where a user explicitly attempts to bypass safety controls, IPI exploits the “User as Victim” paradigm by poisoning external data sources that the AI system autonomously ingests \[

https://www.preprints.org/manuscript/202603.1023#B15-preprints-202314

\]. The fundamental vulnerability enabling IPI stems from the architectural characteristics of standard Transformer models. These models process inputs as a continuous, boundary-less sequence of tokens within a single, flattened context window. Because the self-attention mechanism computes relationships based on semantic affinity rather than structural or functional roles, the model inherently struggles to distinguish between high-privilege system instructions and untrusted retrieved data \[

https://www.preprints.org/manuscript/202603.1023#B10-preprints-202314

\]. Consequently, when malicious imperative language is concatenated into this context window, the model may heavily weigh these tokens, creating a “Confused Deputy” scenario where the AI executes attacker's instructions using the system's privileges \[

https://www.preprints.org/manuscript/202603.1023#B3-preprints-202314

(2) Traditional

Static IPI methods

Early iterations of IPI primarily targeted text-based ingestion vectors using static payloads. Attackers frequently embed malicious instructions into public webpages using techniques like white-on-white text, zero-font size, or HTML comments, which remain invisible to human users but are fully legible to AI web scrapers \[

https://www.preprints.org/manuscript/202603.1023#B4-preprints-202314

\]. In enterprise and operational environments, vectors expand to include poisoned documents, such as PDF resumes or shared workspace pages designed to manipulate AI screening and search tools \[

https://www.preprints.org/manuscript/202603.1023#B16-preprints-202314

\]. Additionally, routine automated tasks are vulnerable \[

https://www.preprints.org/manuscript/202603.1023#B17-preprints-202314

\]; for instance, hidden instructions placed in email footers or calendar invites can trigger unauthorized actions when an AI assistant performs automatic summarization or scheduling routines. In these static attacks, the semantic weight of the injected natural language overrides the trusted context, effectively collapsing the trust boundary between code and data.

(3) Advanced and Adaptive methods

As static keyword filters and basic anomaly detection systems have improved, attackers have shifted toward advanced, dynamically generated methodologies. Modern adaptive attacks utilize optimization algorithms to iteratively refine adversarial strings tailored to bypass specific defensive mechanisms \[

https://www.preprints.org/manuscript/202603.1023#B11-preprints-202314

\]. These optimization techniques aim to maximize the probability of attack success while minimizing the probability of detection by the system. This mirrors the principles seen in other advanced adversarial search methods like Actor Critic \[

https://www.preprints.org/manuscript/202603.1023#B11-preprints-202314

\], Beam Search \[

https://www.preprints.org/manuscript/202603.1023#B18-preprints-202314

\], and Tree of Attacks with Pruning (TAP) \[

https://www.preprints.org/manuscript/202603.1023#B19-preprints-202314

\]. Furthermore, methodologies like TopicAttack \[

https://www.preprints.org/manuscript/202603.1023#B20-preprints-202314

\] utilize fabricated conversational transitions to gradually shift an LLM's context from a benign topic to a malicious instruction, thereby minimizing perplexity spikes and evading detection. Other advanced methods include Invisible Prompt Injection \[

https://www.preprints.org/manuscript/202603.1023#B21-preprints-202314

\], which exploits non-printing Unicode tags to hide payloads from human reviewers, and VortexPIA \[

https://www.preprints.org/manuscript/202603.1023#B22-preprints-202314

\], which induces the model to actively query and extract private information from the user in multi-turn dialogues.

B. Existing IPI Defenses

(1) Prompt Engineering Defenses

Prompt engineering serves as the most accessible defense mechanism, leveraging specialized prompt structures to enforce semantic boundaries between trusted instructions and untrusted external data within a strictly black-box paradigm. A prominent framework is Microsoft's “Spotlighting,” \[

https://www.preprints.org/manuscript/202603.1023#B8-preprints-202314

\] which employs Delimiting (bracketing external data with special tokens) and Datamarking (interleaving data with markers to continuously define boundaries). Similarly, techniques like the “Sandwich Defense” \[

https://www.preprints.org/manuscript/202603.1023#B23-preprints-202314

\] and structural data delimiters (e.g., XML or JSON tags) \[

https://www.preprints.org/manuscript/202603.1023#B24-preprints-202314

\] isolate untrusted input by wrapping it between rigid system instructions. The system prompt is subsequently updated to explicitly direct the model to treat text within these boundaries strictly as passive data.

Our proposed method, RUI, builds upon this foundational black-box category. However, it distinguishes itself from conventional approaches through user instruction authentication and explicit adversarial identification. By moving beyond data boundary enforcement, RUI offers a more robust and efficient defense, demonstrating particular resilience against the advanced, adaptive IPI attacks that frequently bypass standard prompt-level guardrails.

(2) Architectural Modification Defenses

To address the root cause of instruction confusion, researchers have proposed architectural modifications that enforce a hard separation between instructions and data at the layer level. Architecturally Separated Instruction-Data Embeddings (ASIDE) \[

https://www.preprints.org/manuscript/202603.1023#B30-preprints-202314

\] introduces a non-learnable orthogonal rotation to the embeddings of tokens designated as data. By mapping data tokens via an orthogonal matrix, ASIDE ensures that instruction and data tokens reside in distinct linear subspaces, fundamentally altering how the attention mechanism processes them. Conversely, Structured Queries (StruQ) \[

https://www.preprints.org/manuscript/202603.1023#B25-preprints-202314

\] enforces separation in the discrete token space by utilizing a secure front-end and specialized control tokens to format trusted instructions versus untrusted user data. The model is then fine-tuned to penalize any deviation caused by tokens residing within the data block. Expanding on this discrete token-level intervention, DefensiveToken \[

https://www.preprints.org/manuscript/202603.1023#B26-preprints-202314

\] introduces a novel test-time defense mechanism that uses optimized special token embeddings to provide robust protection against prompt injection attacks while maintaining high model utility and developer flexibility.

(3) Training-Based Alignment Defenses

When fundamental architectural redesigns are not feasible, defense strategies focus on aligning the model's internal policy through training. The Instruction Hierarchy (IH) framework \[

https://www.preprints.org/manuscript/202603.1023#B27-preprints-202314

\] trains models on synthetic data to strictly prioritize system messages over user messages and tool outputs, explicitly teaching the model to ignore contradictory lower-level instructions. This has been expanded into Reasoning-Based Verification (VerIH), which requires the model to output a reasoning trace that explicitly articulates and resolves conflicts according to the established hierarchy before generating a final response. Other alignment methods include SecAlign \[

https://www.preprints.org/manuscript/202603.1023#B28-preprints-202314

\], which leverages Direct Preference Optimization (DPO) to maximize the margin between a secure, preferred response and an insecure response that follows the injected command. Furthermore, InstruCoT \[

https://www.preprints.org/manuscript/202603.1023#B29-preprints-202314

\] fine-tunes models to systematically classify instructions and flag suspicious directives in a scratchpad before executing multi-step workflows.

(4) Inference-Time and System-Level Defenses

For deployed applications, inference-time safeguards work as a firewall between external data and the model. PromptArmor \[

https://www.preprints.org/manuscript/202603.1023#B31-preprints-202314

\] utilizes a dual-LLM architecture where a Guardrail LLM \[

https://www.preprints.org/manuscript/202603.1023#B32-preprints-202314

\] intercepts inputs, identifies malicious segments, and uses fuzzy string matching to excise the injection before passing the sanitized data to the backend agent. IntentGuard \[

https://www.preprints.org/manuscript/202603.1023#B33-preprints-202314

\] operates on intent verification, forcing the model to verbalize its planned actions and intervening if an intent analyzer detects that a command originated from an untrusted data segment. At the system level, LLM Firewalls \[

https://www.preprints.org/manuscript/202603.1023#B34-preprints-202314

\] enforce strict boundaries by minimizing data passed to tools, scanning tool outputs, and enforcing rigid JSON schemas to prevent attackers from using natural language ambiguity to hijack control flows. Additionally, Encrypted Prompts \[

https://www.preprints.org/manuscript/202603.1023#B35-preprints-202314

\] append cryptographic permission scopes to interactions, causing the LLM to refuse actions if the requested execution mismatches the verified permissions. While these firewalls do not rely on the cognitive capacity of the primary LLM, they usually need another fine-tuned LLM to perform semantic analysis.

Crucially, no single defensive mechanism offers absolute protection against IPI. A robust security system inherently requires combining multiple paradigms into a multi-layer architecture. For example, a comprehensive framework could integrate a Prompt Engineering front-end (such as our proposed RUI) to structure inputs, an Architectural Modification (e.g., ASIDE or StruQ) to physically separate instruction and data processing, a Training-Based Alignment model (e.g., SecAlign or VerIH) to enforce strict instruction hierarchies, and an Inference-Time wrapper (e.g., PromptArmor or IntentGuard) for runtime intent monitoring. The resulting multi-layer defense system mitigates the limitations of standalone solutions and presents a significantly more formidable barrier against various types of injection attempts.

C. Benchmarks and Evaluation Frameworks

The transition from ad-hoc testing to rigorous security engineering has necessitated the development of standardized evaluation ecosystems. The need for standardized evaluation has led to the development of various benchmarks and frameworks: BIPIA (Benchmark for Indirect Prompt Injection Attacks) \[

https://www.preprints.org/manuscript/202603.1023#B36-preprints-202314

\] focuses on evaluating text-based processing tasks such as summarization and web-based question answering. AgentDojo \[

https://www.preprints.org/manuscript/202603.1023#B12-preprints-202314

\] provides a dynamic environment for evaluating prompt injection attacks and defenses for LLM agents on a dual-axis of utility and security. InjecAgent \[

https://www.preprints.org/manuscript/202603.1023#B9-preprints-202314

\] benchmarks indirect prompt injections in tool-integrated LLM agents. Additionally, LLM-PIRATE \[

https://www.preprints.org/manuscript/202603.1023#B37-preprints-202314

\] specifically targets Retrieval-Augmented Generation (RAG) systems by simulating adversarial document retrieval across diverse API scenarios.

III. Threat Model

This section formalizes the security boundaries and adversarial assumptions used to assess the robustness of the Real User Instruction (RUI) framework against indirect injections in multi-turn, function-calling environments, similar to recent studies \[

https://www.preprints.org/manuscript/202603.1023#B11-preprints-202314

\]. In particular, our threat model assumes a highly informed attacker adhering to Kerckhoffs's principle \[

https://www.preprints.org/manuscript/202603.1023#B38-preprints-202314

\], representing an extremely stringent threat profile, as shown in

https://www.preprints.org/manuscript/202603.1023#preprints-202314-f001

Indirect prompt injection threat model adhering to Kerckhoffs's principle. In this case, the attacker knows the algorithm details about the LLM and the defense system, and will adapt injections according to the user instructions and the external data.

A. Target System and Workflow

We define the victim system as an autonomous Large Language Model (LLM) agent equipped with tool-use capabilities, such as email readers, web scrapers, or database querying functions. The execution pipeline of this system follows a standard retrieval-augmented workflow: the agent first receives a trusted query from a legitimate, benign user. To fulfill this query, the agent autonomously invokes tools to retrieve external, untrusted data (e.g., reading an incoming email or fetching a webpage's contents). Crucially, the target system may operate in a multi-turn environment, where it maintains a continuous conversation history across multiple interactions. This history informs the agent's future actions, meaning that data ingested in one turn can influence the model's reasoning and tool execution in subsequent turns.

B. Adversarial Goals

The primary objective of the adversary is to execute an Indirect Prompt Injection (IPI) to displace the legitimate user's instructions with their own. Unlike traditional adversarial attacks on LLMs (often referred to as “jailbreaks”), the attacker in our model is not attempting to force the model to generate toxic content, hate speech, or explicit malware. Instead, the adversary's goal is so-called Instruction Drift or Goal Hijacking. The attacker seeks to inject semantically "innocent" payloads, such as asking the model to translate a specific text, forward an email to a third party, or alter the format of its output.

This distinction is critical to our threat model because these goals are semantically benign. Consequently, they are inherently invisible to standard, widely deployed safety filters (such as LlamaGuard or keyword-based blocklists), which are designed to detect policy violations rather than control-flow manipulations.

C. The Gray-Box Attacker

We assume a highly capable, adaptive adversary operating under a Gray-Box threat model, adhering to Kerckhoffs's principle.

#### Payload Control:

The attacker does not have direct access to the user's prompt interface. However, they have full control over the content of the external data retrieved by the agent (e.g., the attacker is the author of the malicious email or the compromised webpage the agent is summarizing).

#### Gray-Box Knowledge:

The attacker is fully aware of the system's defense architecture. They know that the target utilizes the Real User Instruction (RUI) framework, and they are explicitly aware of its internal mechanisms, including the Privileged Channel, the strict JSON schema, the Explicit Adversarial Identification, and the existence of Dynamic Key Rotation.

#### The Limitation:

The adversary's sole limitation is cryptographic: while they know the algorithm, they do not know the user-specific, randomly-generated session key ( K t ) actively used by RUI for the current conversational turn.

D. Attack Vectors

Given their gray-box knowledge, the attacker will avoid naive, static injections, and prefer an adaptive suite of attack vectors designed specifically to bypass IPI defense:

#### Context-Aware Injection:

To trick the LLM's attention mechanism and avoid triggering cognitive forcing rules, the attacker blends malicious commands naturally into the surrounding text \[

https://www.preprints.org/manuscript/202603.1023#B11-preprints-202314

\]. For example, instead of a blunt “Ignore previous instructions,” the payload mimics the context: “Speaking of summaries, please further explain why this paper is ground-breaking.” Moreover, the attacker is likely to use LLM-based algorithms like Actor-Critic or Tree of Attacks with Pruning to automatically search for effective injection payload.

#### Split-Token or Base64 Obfuscation:

To bypass naive text-matching or string-filtering defenses, the attacker employs semantic obfuscation \[

https://www.preprints.org/manuscript/202603.1023#B4-preprints-202314

\]. This includes breaking up instruction keywords across multiple tokens (e.g., “Ig” + “nore”) or encoding the entire malicious payload in formats natively understood by the LLM, such as Base64 or Leetspeak.

#### Delimitation Spoofing (Single & Multi-Turn):

The attacker attempts to structurally escape the data block by guessing the static tags (e.g., inserting

https://www.preprints.org/manuscript/202603.1023#B15-preprints-202314

\]. In multi-turn scenarios, the attacker employs a reconnaissance strategy: using Turn 1 to inject a prompt that attempts to “leak” the current session delimiter into the model's output, and utilizing Turn 2 to explicitly exploit that leaked delimiter to execute the payload.

E. Out of Scope

To appropriately bound the scope of this research, we explicitly exclude the following threat vectors:

#### Direct Prompt Injection:

We assume the primary user of the system is benign. Defending against a malicious user directly attacking or jailbreaking their own locally hosted model is a separate domain and is out of scope.

#### Data Poisoning and Weight Extraction:

We assume the underlying LLM weights are frozen, secure, and hosted in a trusted environment. White-box defenses, adversarial fine-tuning, and protections against training-data poisoning are beyond the scope of this paper.

III. Real User Instruction Methodology

To address the fundamental vulnerabilities outlined in our threat model, we introduce the

Real User Instruction (RUI)

middleware. RUI represents a conceptual paradigm shift in defending Large Language Models against Indirect Prompt Injection (IPI). Rather than relying on the inherently flawed approach of data filtering that attempts to heuristically sanitize or bound untrusted data, RUI enforces proactive instruction authentication, allowing the model focuses on authenticated commands and ignores injected commands in data.

The source code of RUI is at

https://github.com/lambblue/rui

https://github.com/lambblue/rui

A. Overview of RUI

Architecturally, RUI operates as a lightweight, black-box middleware layer that only manipulates system and user prompts, requiring no access to the underlying model's weights and incurs zero fine-tuning costs.

https://www.preprints.org/manuscript/202603.1023#preprints-202314-f002

illustrates, the RUI middleware sits logically between the external environment (the user and tool outputs) and the core LLM. It acts through a prompt-engineering pipeline: capturing user queries, wrapping retrieved context, managing session states, and dynamically rewriting the system prompt before any tokens are forwarded to the LLM for inference. A practical example is in

https://www.preprints.org/manuscript/202603.1023#app1-preprints-202314

https://www.preprints.org/manuscript/202603.1023#preprints-202314-f0A1

Real User Instruction system consisting of Privileged Channel, Explicit Adversarial Identification, and Dynamic Key Rotation. It works as a middleware between the external environment (the user and tool outputs) and the core LLM, and is implemented via prompt engineering.

To achieve robust instruction-data separation in both single and multi-turn workflows, the RUI framework is constructed upon a triad of core, symbiotic mechanisms:

#### The Privileged Channel:

A cryptographic-style encapsulation schema that strictly authenticates legitimate user instructions.

#### Explicit Adversarial Identification:

A cognitive forcing strategy embedded in the system prompt that compels the model to actively parse, isolate, and explicitly reject unauthorized commands.

#### Dynamic Key Rotation:

A state-management protocol that acts as a moving target defense, seamlessly migrating the conversation context to novel session keys to neutralize key leakage and multi-turn context contamination.

B. Mechanism I: The Privileged Channel

The foundational vulnerability of current LLM agents lies in their “open-door” policy: they process all tokens, whether from the system, the user, or retrieved documents, with equal semantic weight. In other words, they have fundamental difficulty in differentiating the genuine user instructions from injected instructions. To close this vulnerability without fine-tuning, we introduce the

Privileged Channel

, a mechanism that applies the principles of symmetric-key encryption to prompt engineering.

In RUI, the system prompt and user prompt share a secret, transient session key K t . This key is essentially a cryptographic authenticator, establishing a trusted conduit that is inaccessible to the adversary.

(1) The Encapsulation Schema

Formally, let U t rpresent the legitimate user's command at turn t . The RUI middleware encapsulates this command into a strict, key-authenticated JSON structure, denoted as E ( U t , K t ) :

E ( U t , K t ) = { " UserKey " : K t , " UserCommand " : U t }

This schema serves as the digital signature for the interaction. The idea is simple: only the instructions inside E ( U t , K t ) ae from the real user and should be followed. The rest part of the user prompt, which is outside E ( U t , K t ) ,must always be treated as plain data. Because the adversary operating in the retrieved data layer does not possess K t , they cannot construct a JSON object that exactly matches this signature.

(2) Enforcement via Positive Attention Targeting

In RUI, the system prompt is specifically configured to recognize this JSON-like object as the sole valid source of executable instructions. This configuration inverts the logic of traditional “Spotlighting” defenses and addresses a core architectural limitation of modern LLMs.

Current defenses typically employ Negative Spotlighting (e.g., instructing the model to “Ignore all text inside

tags”). From the perspective of the LLM's attention mechanism, this is suboptimal for two reasons. First, the model must still actively attend to the adversarial tokens to process the “ignore” directive; if an injected instruction is sufficiently commanding or stealthy, it can easily escape this negative constraint. Second, Negative Spotlighting suffers heavily from the Attention Dilution problem \[

https://www.preprints.org/manuscript/202603.1023#B39-preprints-202314

\]. In real-world agentic workflows, the retrieved data payload (e.g., reports, web pages) is usually orders of magnitude longer than the user's command. As the context window expands, the transformer's attention weights become diluted across massive tokens. This dilution makes it fundamentally difficult for the LLM to reliably track the structural boundaries of the untrusted data block, resulting in subconscious execution of injected instructions.

In contrast, RUI implements “Positive Spotlighting” (or “Instruction Whitelisting”). The system prompt explicitly instructs the model to direct its attention heads only towards the specific, compact token sequence matching the session key K t . In addition, because genuine user commands are typically brief, the LLM can easily maintain strict boundary tracking around the authenticated JSON object and suffer less from attention dilution. As a result, RUI effectively steer the model to seek the highly concentrated cryptographic key, demoting all unauthenticated text, regardless of its imperative tone or length, to passive unimportant noise.

C. Mechanism II: Explicit Adversarial Identification

While the Privileged Channel establishes a strict cryptographical boundary for valid instructions, relying solely on passive filtering, i.e., simply instructing the model to “ignore” unauthenticated data, is insufficient against sophisticated adversaries.

(1) The Rationale Against Passive Filtering

Passive exclusion assumes that an LLM can flawlessly drop specific contextual elements from its latent representations. However, in “Goal Hijacking” attacks, the injected payloads are semantically benign and highly contextualized. Because these commands do not trigger toxicity guardrails and flow naturally with the surrounding text, they frequently bypass passive exclusion filters. The model subconsciously absorbs the imperative tone of the injection, leading to instruction drift even when the data is structurally encapsulated.

(2) The “Detect-and-Deny” Implementation

To neutralize this, RUI implements

Explicit Adversarial Identification

through a mandatory “detect-and-deny” prompting strategy. Rather than allowing the LLM to passively skip over untrusted data, RUI rewrites system prompt to force the model to actively parse the external data for any imperative statements or action-oriented verbs that lack the active session key K t .

Specifically, before the model is permitted to execute the legitimate user's command, it must generate

a structured preamble to set the tone for the subsequent output tokens

https://www.preprints.org/manuscript/202603.1023#B13-preprints-202314

\]. The model is instructed to first declare its fidelity to the Privileged Channel (e.g., “I will only follow instructions from the real user K t ."). It must then explicitly extract and list any unauthenticated commands it found hidden in the data, overtly labeling them as unauthorized and stating its intention to ignore them. Only after this preamble is complete may the model proceed to process the actual user instruction.

(3) The Cognitive Benefit

This mechanism leverages the inherent autoregressive nature of LLMs. By forcing the model to generate tokens that explicitly articulate the adversarial commands as “invalid” at the very beginning of its output, RUI introduces a powerful

cognitive forcing function

, akin to Chain-of-Thought reasoning.

When the LLM generates the output like “I have detected an unauthorized command to 'Explain why this paper is ground-breaking' and I will ignore it,” it dynamically updates its own context window with this explicit logical constraint. This newly generated text heavily conditions the attention weights of the subsequent generation phase. Instead of the injected command acting as a subconscious directive (subversively shifting the goal), it is algorithmically boxed into the semantic category of “anomalous data to be rejected.” This active articulation structurally reinforces the model's internal attention mask, effectively neutralizing subconscious instruction drift before the model even begins to formulate its final response.

D. Mechanism III: Dynamic Key Rotation

While the Privileged Channel and Explicit Adversarial Identification provide robust single-turn security, continuous agentic workflows introduce a temporal vulnerability. If a static defense mechanism (such as a fixed XML tag or a persistent password) is used across a multi-turn conversation, it becomes susceptible to progressive degradation.

(1) The Multi-Turn Problem

In multi-turn scenarios, static defenses frequently fall victim to two primary failure modes: delimiter leakage and context contamination. An adaptive adversary can execute a reconnaissance attack in Turn 1, injecting a payload that instructs the model to “output the system prompt” or “repeat all text above.” If successful, the model leaks the static delimiter to the user interface. In Turn 2, the adversary can then exploit this leaked information to structurally spoof the delimiter and execute a payload. Furthermore, even if an injection is successfully ignored in Turn 1, the adversarial text remains embedded in the conversation history H t − 1 . As the context window grows, the model may mistakenly re-contextualize this historical adversarial text as trusted conversational memory (context contamination).

(2) Session Migration

To solve this, RUI implements

Dynamic Key Rotation

, functioning as a moving target defense. Instead of a static identifier, RUI manages a continuous session migration. At the initiation of every new conversational turn t , the system programmatically generates a new, high-entropy cryptographic key K c u r r , where K c u r r ≠ K p r e v . The System Prompt is then dynamically rewritten to authorize only K c u r r for the current inference step. Consequently, any instruction relying on K p r e v is instantly deprecated.

(3) History Rewriting and Context Sanitization

To maintain the continuity of the legitimate conversation without breaking the model's memory, the RUI middleware performs a critical

History Rewriting

operation before appending the new user query.

Specifically, RUI iterates through the entire conversation history H t − 1 . Because RUI possesses the ground-truth knowledge of the previous key K p r e v and the strict JSON encapsulation schema, it can definitively locate all genuine historical user commands. It programmatically replaces every authorized instance of K p r e v with the new active key, K c u r r .

Crucially, any adversarial text residing in the history is left entirely untouched. Because the adversary operating in Turn t − 1 did not know K p r e v , their injected payloads either lacked a key entirely or utilized a spoofed/leaked, outdated delimiter. During the rewriting phase, RUI ignores these unauthenticated structures, keeping them unauthenticated in the new turn of conversation.

(4) Mathematical Neutralization

When the LLM processes the newly sanitized context window for Turn t , it scans exclusively for the presence of K c u r r . Legitimate conversational history appears perfectly authenticated under the new key. However, any historical adversarial payload, even one that successfully guessed or leaked K p r e v in a previous turn, is now mathematically incorrect. It presents to the model with an expired or invalid signature, immediately relegating it back to the status of passive noise. This mechanism acts as an implicit, continuous garbage collection for prompt integrity, ensuring that the attacker is always one step later than the genuine user, rendering multi-turn delimitation spoofing mathematically infeasible.

E. Implementation Details

RUI operates entirely as a black-box middleware layer. Its implementation requires only standard string manipulation, state management, and prompt engineering, making it agnostic to the specific underlying LLM architecture.

(1) RUI Execution Pipeline

The pipeline for each turn of conversation t is as below.

(2) Step-by-Step Walkthrough

Phase 0 & 1: Session Setup and Key Rotation

At the onset of turn t , RUI generates a new session key ( K c u r r ), which must be kept secret from the attacker. To execute Key Rotation, RUI applies a straightforward string replacement across the conversation history H t − 1 K p r e v , converting all user instructions authenticated by K p r e v to use K c u r r . Any adversarial text that failed to use K p r e v or attempted to spoof a static tag is ignored during this replacement, effectively stripping it of any potential authority in the new turn.

Simultaneously, RUI constructs the updated System Prompt S p r o m p t ( K c u r r ) . To enforce Explicit Adversarial Identification, the prompt is rigidly structured as follows:

Phase 2: Encapsulation

The RUI middleware intercepts the raw user command C t and wraps it into the designated Privileged Channel format. For example, if the user asks to summarize a report, the string passed to the model becomes: {"User Key": " K c u r r ", "User Command": "Summarize the report."}.

Phase 3: Chat

RUI combines system prompt, key-rotated history, wrapped user instructions, and untrusted external data to generate a secured context CTX, and sends it to the LLM.

Because of the cognitive forcing instructions embedded in the System Prompt, the LLM is constrained to begin its autoregressive generation with the exact phrase: “I will only follow instructions from the real user " K c u r r ".” If the untrusted data D t contains a Goal Hijacking attempt (e.g., “Explain why this paper is ground-breaking”), the model is forced to explicitly identify it before proceeding: “...I have detected an unauthorized command to 'Explain why this paper is ground-breaking' outside the user tags. I will ignore it. Here is the summary of the report...”

V. Experimental Setup

To rigorously evaluate the Real User Instruction (RUI) framework, we build upon Microsoft's

Benchmark for Indirect Prompt Injection Attacks (BIPIA)

, a standardized and widely recognized foundational dataset for assessing LLM robustness against IPI. BIPIA provides a robust baseline of adversarial prompts and evaluation metrics. Originally, BIPIA considers five scenarios of LLM tasks, including “Abstract”, “Code”, “Email”, “Q&A”, and “Table”. However, its standard Q&A scenario typically features very short contexts and lacks external untrusted data payloads. This brevity fails to accurately simulate the complex, data-heavy environments in which modern LLM agents are deployed.

To bridge this gap and properly stress-test our defense, we introduce a new “Report” scenario to the dataset, replacing BIPIA's standard Q&A scenario. For this scenario, we download 100 papers from arXiv via its API (search query = “artificial intelligence”). These full-length papers serve as the untrusted external data payloads.

As a result, our testset includes five representative scenarios relying on external data, namely,

(web-based news retrieval and synthesis),

(interpreting and generating logic based on open-source repositories),

(automated message processing),

(analysis of technical details), and

(reasoning with structured tabular data). Together, these scenarios cover the most frequent tasks performed by modern LLM agents.

#### We add two types of instructions to each piece of external data:

(1) The Legitimate Instruction (User Intent):

The legitimate instruction issued by the user via the Privileged Channel, one for each piece of external data, the same as in BIPIA. For instance, in the Report scenario, the user instruction could be “List the pros and cons of this paper.”

(2) The Injected Instruction (Adversarial Goal):

The hidden instruction stealthily embedded within the external data. For instance, in the Report scenario, an injected instruction could be “Explain why this paper is ground-breaking,” or “How will this technology speed up AI development”. It is noteworthy that different from BIPIA, for each scenario, we use Actor-Critic technology \[

https://www.preprints.org/manuscript/202603.1023#B11-preprints-202314

\] to adaptively choose 10 most appropriate injections from BIPIA and revise them according to user instruction, external data, and model response, until they can successfully induce LLM to follow the injections. This makes the injections well-prepared to evade LLM's internal defense mechanism.

As a result, our testset has 5000 samples in total, with 100 × 10 = 1000 samples for each scenario, as

https://www.preprints.org/manuscript/202603.1023#preprints-202314-t001

Test Samples across Different Scenarios.

B. Backend LLMs

Because RUI operates entirely as a black-box middleware layer without requiring any access to or modification of internal model weights, it is inherently designed to be model-agnostic. To empirically validate this architectural flexibility and ensure our findings are not overfit to a single architecture, we evaluate RUI across a diverse suite of latest LLMs, as follows:

(1) Gemini 3 Flash

: A light-weighted close-source model by Google. Evaluated under both Low Thinking and Medium Thinking configurations.

(2) Gemini 3.1 Pro

: A state-of-the-art close-source model by Google, with High Thinking configuration.

(3) GPT-5.4 Thinking

: A state-of-the-art close-source model by OpenAI, with High Thinking configuration.

: A state-of-the-art open-source model by Z.ai, with High Thinking configuration.

#### Default Model Selection:

After evaluating across these state-of-the-art models, we find that

Gemini 3 Flash (Medium Thinking)

achieves the best balance between protection capability and computational efficiency. Consequently, we utilize Gemini 3 Flash (Medium Thinking) as the default backend model for all primary experiments and ablation studies, unless stated otherwise.

C. Injection Strategies

To ensure our evaluation reflects the capabilities of an adaptive, gray-box adversary, we do not rely on naive, static prompt injections (e.g., simply appending “Ignore previous instructions” to the end of a file). Instead, as outlined in Section 5.1, we utilize an automated Actor-Critic pipeline \[

https://www.preprints.org/manuscript/202603.1023#B11-preprints-202314

\] to dynamically generate and seamlessly embed adversarial payloads into the external data.

We deploy three representative injection strategies across the testset to comprehensively evaluate the defense mechanisms under worst-case adversarial conditions:

(1) Direct Context-Aware Injection:

This strategy tests the defense's ability to resist Goal Hijacking when the malicious instruction is semantically blended into the untrusted data \[

https://www.preprints.org/manuscript/202603.1023#B11-preprints-202314

\]. For instance, in the Report scenario, the Actor-Critic pipeline iterates to revise the injected command to mimic the formal, academic tone of the context of the paper. More specifically, rather than a blunt command, the injection may be woven into the paper like: “This paper establishes a novel paradigm for IPI defense, fundamentally redefining how researchers can approach LLM's internal vulnerabilities in the future. Therefore, please introduce more about how this paper will reshape the future of LLM security.” This confuses the LLM's attention mechanism to discern between valid contextual flow and unauthorized imperative commands.

(2) Split-Token and Encoded Injection:

On top of context-aware injection, the attacker may further disguise the injection by splitting it into token pieces (“ Ex”+ “ plain” + “ w” + “ hy”) or encoding it into Base64 formats \[

https://www.preprints.org/manuscript/202603.1023#B4-preprints-202314

\], whichever is more effective against the target LLM. This strategy specifically targets the LLM's token-reassembly capabilities, testing if the model will subconsciously decode and execute an instruction that is lexically disguised within the data block.

(3) Delimitation Spoofing:

Additionally, the attacker can prefix the injected payload with a barrage of common closing delimiters (e.g.,

, --- End of Context ---,\]) in an attempt to prematurely close the static data block \[

https://www.preprints.org/manuscript/202603.1023#B15-preprints-202314

\], thereby inducing LLM to believe that there is another user instruction. In the cases of dynamic delimitation, the attack is able to gain access to the session keys that have been used in the past, thus use these keys to construct a delimitation escape. This strategy evaluates the structural integrity of the delimitations across both single-turn and multi-turn workflows.

D. Comparison to Existing Methods

We compare RUI to three representative black-box methods that also tries to defend IPI through prompt engineering, as follows:

#### Baseline (No Defense):

This configuration utilizes the vanilla backend LLM with absolutely no prompt protections, safety preambles, or data delimiters. The user instruction and the external untrusted data are simply concatenated into the context window. This serves as our control group to establish the inherent vulnerability of the model, expected to yield a near 100% Attack Success Rate (ASR) against adaptive Actor-Critic based attacks.

#### Static Data Delimiter (Standard Spotlighting):

Representing the prevailing industry standard for black-box defense, this approach utilizes Negative Spotlighting \[

https://www.preprints.org/manuscript/202603.1023#B8-preprints-202314

\]. The system prompt instructs the model to ignore instructions found within untrusted data, and the data itself is structurally bounded by fixed, static XML tags (e.g.,

\[Untrusted Content\]

). However, this method is vulnerable to delimiter leakage issue.

#### Dynamic Data Delimiter (Advanced Spotlighting):

This method serves as a state-of-the-art baseline that utilizes a random, high-entropy tag for each turn to avoid delimiter leakage, \[

https://www.preprints.org/manuscript/202603.1023#B24-preprints-202314

\] similar to RUI's dynamic key mechanism. However, crucially, it applies these dynamic tags to the data rather than the instructions. This “ignore the dynamic bad block” mechanism will lead to significant performance degradation compared to RUI's “only attend to the dynamic good block”, as we will show later in Section VI.

#### Real User Instruction (Ours):

Our proposed middleware framework. This configuration concurrently deploys all three core mechanisms: the Privileged Channel (Positive Instruction Whitelisting), Explicit Adversarial Identification (Cognitive Forcing), and Dynamic Key Rotation (Multi-Turn Context Sanitization).

E. Evaluation Metrics

We use two widely-adopted metrics, namely, Attack Success Rate (ASR) and Benign Performance Preservation (BPP), to objectively quantify the trade-off between security and system utility. A robust defense mechanism must simultaneously minimize ASR while maximizing BPP.

#### Attack Success Rate (ASR):

This metric measures the security vulnerability of the system. It is defined as the percentage of test cases where the LLM executes the adversary's injected task (Goal Hijacking):

A S R = N h i j a c k e d N t o t a l × 100 %

where N t o t a l is the total number of test samples, and N h i j a c k e d is the subset of these samples where the model is goal hijacked by the injections. ASR = 0% represents perfect neutralization of IPI attacks.

In this paper, we employ another LLM (Gemini-3.1-Pro) as judge to automatically assess whether the targeted LLM succumbs to the injected instructions.

#### Benign Performance Preservation (BPP):

Strong security mechanisms often inadvertently degrade the model's core utility, causing it to become “slack” or even refuse legitimate requests. BPP measures the system's ability to maintain its original functionality despite the presence of defending mechanism. It is defined as the percentage of test cases where the LLM accurately fulfills the user commands as if there is no defense:

B P P = N p e r f e c t N t o t a l × 100 %

where N t o t a l is the total number of test samples, and N p e r f e c t is the number of the samples which perfectly follows the user instructions without being affected by IPI defense. BPP ≈ 100% implies that the security mechanism introduces negligible degradation to the model's core capabilities.

In this paper, we employ another LLM (Gemini-3.1-Pro) as judge to automatically assess whether a defended LLM fulfills user commands as good as an undefended one.

VI. Experimental Results

In this section, we present a comprehensive empirical evaluation of the RUI framework according to the experimental settings in Section V. The major result is that RUI consistently outperforms the similar state-of-the-art methods with nearly 0% ASR and > 88.8% BPP in all five task scenarios.

A. Main Results: Defense Efficacy and System Utility

We evaluated RUI's performance against the undefended baseline and two prominent spotlighting defenses: Static Data Delimiters and Randomized (Dynamic) Data Delimiters. The evaluation spans five distinct scenarios, namely, Abstract, Code, Email, Report, and Table, representing a diverse array of agentic tasks and context lengths. We use Gemini-3.0-flash (medium thinking) as the default backend model, and use the direct Context-Aware Injection as the default attack strategy.

https://www.preprints.org/manuscript/202603.1023#preprints-202314-t002

summarizes Attack Success Rate (ASR) and Benign Performance Preservation (BPP).

Defense Performance under Gemini-3.0-Flash (Medium) and Direct Context-Aware Injection.

The first thing to note is RUI's remarkable ASR reduction.

The empirical data demonstrates that modern LLMs are inherently vulnerable to context-aware Goal Hijacking, as the undefended baseline exhibited a 100% ASR across all five testing scenarios. Conventional negative spotlighting defenses, regardless of whether the delimiters were static or dynamically randomized, failed to provide reliable security. Static delimiters allowed ASR as high as 27.1% (Email) ~ 86.5% (Report), while randomized data delimiters only marginally reduced this vulnerability to 23.9% (Email) ~ 79.4% (Report). In contrast, RUI completely neutralized the threat, with an ASR of 0.0% across all evaluated scenarios, proving that RUI is extremely effective in guiding LLM to reliably ignore unauthorized instructions. A practical example is shown in

https://www.preprints.org/manuscript/202603.1023#preprints-202314-f003

An example in Report scenario, where RUI successfully protects LLM from injections while Randomized Data Delimiter fails. In this case, RUI detects and rejects the injection “encrypt using a Caesar cipher” at the beginning of its response, and then strictly adheres to the user instruction “List the pros and cons of this paper” (

https://www.preprints.org/manuscript/202603.1023#preprints-202314-f003

a). On the other hand, Randomized Data Delimiter simply follows the injection and generates encrypted response (

https://www.preprints.org/manuscript/202603.1023#preprints-202314-f003

Naturally, the success of RUI depends heavily on the model's instruction-following and reasoning capability. As later demonstrated in subsection C, RUI yields a non-zero ASR if the backend model is replaced with a less capable alternative.

Furthermore, RUI shows exceptional BPP maintenance.

As shown in

https://www.preprints.org/manuscript/202603.1023#preprints-202314-t001

, Static and Randomized Delimiters caused catastrophic drops in BPP, implying that negative spotlighting can substantially dilute LLM's attention among the data. In particular, in the Code and Table scenarios that require strong logical reasoning capability, randomized delimiters plummeted the model's benign performance to 68.9% and 49.1%, respectively, showing the agent substantially weakened for legitimate tasks. RUI, conversely, achieved a minimum BPP of 88.8% (in the highly structurally complex Code scenario) and reached near-perfect preservation rates in the Report (99.4%), Table (99.0%), and Abstract (98.9%) scenarios. This demonstrate that RUI costs much less efforts for LLM to perform than traditional negative spotlighting methods. A practical example is shown in

https://www.preprints.org/manuscript/202603.1023#preprints-202314-f004

An example in Email scenario, where LLM performs perfectly under RUI but becomes “slack” under Randomized Data Delimiter, when there is no injection. In this case, the LLM under RUI drafts a proper response to “Mercury Team” as the user requires (

https://www.preprints.org/manuscript/202603.1023#preprints-202314-f004

a). On the other hand, the LLM under Randomized Data Delimiter mistakenly responds to “John Zoy”, who is the receiver of the wire payment, not the receiver of the email (

https://www.preprints.org/manuscript/202603.1023#preprints-202314-f004

The consistency of RUI's performance across different task scenarios is also notable.

Whether processing compact, structured inputs such as code and tables or lengthy, natural-language documents like reports and abstracts, the integration of the Privileged Channel and Explicit Adversarial Identification effectively insulated the model's attention mechanism. This allowed the LLM to adhere strictly to legitimate user intent without imposing an excessive computational burden on the LLM's inference capabilities.

B. Robustness Against Adaptive Attack Vectors

To rigorously evaluate RUI's resilience against a gray-box adversary with full knowledge of the defense architecture, we analyzed its performance across three sophisticated strategies: direct Context-Aware Injection, Split or Encoded Injection, and Escape Injection (Delimitation Spoofing). Moreover, we specifically extended our evaluation of Delimitation Spoofing to a five-turn conversational setting, where the attacker has access to the full conversation history, and is marked as successful if any single turn is compromised. This is to test whether RUI can robustly mitigate session key leakage and history contamination.

The Attack Success Rates (ASR) for different attack vectors are detailed in

https://www.preprints.org/manuscript/202603.1023#preprints-202314-t003

ASR for Different Attack Vectors under Gemini-3.0-Flash (Medium).

First note that RUI maintained lowest ASR (= 0%) for all 4 types of attacks across all 5 task scenarios. In comparison, both the Static Delimiter and Randomized Delimiter have ASR substantially larger than 0%, e.g., with ASR = 29.8% ~ 100% and 0.6% ~ 79.4%, respectively, in the Report scenario. This result demonstrates that RUI is highly effective for defending against various types of IPI attacks. In fact, by examining LLM's thinking process (i.e., Chain of Thoughts), we can clearly see that with RUI's Explicit Adversarial Identification enforcement, LLM is able to accurately detect hidden injections despite of their semantic camouflage, and safely ignore them while performing real user instructions (see

https://www.preprints.org/manuscript/202603.1023#preprints-202314-f005

An example where a RUI-protected LLM (with the genuine user key “Miyoshino”) accurately detects and ignores camouflaged injections (with a fake user key “Abe”) in its thinking process. More details about this conversation can be found in

https://www.preprints.org/manuscript/202603.1023#app1-preprints-202314

https://www.preprints.org/manuscript/202603.1023#preprints-202314-f0A1

There is another notable phenomenon regarding the efficacy of decorated injections. While the Delimitation Spoofing attack (both in single and five-turn configurations) is extremely effective against Static Delimiter defenses (ASR = 100%), its successful rate drops to nearly zero against Randomized Delimiters (e.g., from 79.4% to 0.6% in the Report scenario). A similar trend was observed with Split or Encoded attacks, which consistently underperformed compared to direct injections across both static and randomized defense baselines. Analysis of the LLM's thinking process reveals that encoded tokens and camouflaged delimiters often serve as adversarial signals due to the internal anti-injection mechanisms in modern LLMs. Upon encountering these over-decorated structures, the model frequently identifies the input as a prompt injection attempt and adopts a more conservative instruction-following posture. This leads to the counter-intuitive conclusion that highly decorated injections can inadvertently trigger the LLM's inherent security heuristics, resulting in diminished attack success.

Based on the above results, we choose the Direct Context-Aware attack as our primary evaluation vector, as its subtlety poses the most consistent challenge to RUI's boundaries.

C. Cross-Model Generalization

To empirically validate RUI's architectural flexibility, we extended our evaluation across a diverse suite of leading LLMs, encompassing varying sizes, access modalities (open vs. closed source), and thinking configurations. The results are shown in

https://www.preprints.org/manuscript/202603.1023#preprints-202314-t004

Cross-Model ASR under Direct Context-Aware Attack.

The data demonstrates that RUI seamlessly generalizes across state-of-the-art models. While highly capable models like GPT-5.4 and Gemini 3.1 Pro natively exhibit more robust instruction-following capabilities than lightweight models, e.g., reducing the baseline Static Delimiter ASR to 19.3% and 23.0% in the complex Report scenario, respectively, they still suffer from unacceptable vulnerabilities if not well defended. On the other hand, RUI is able to universally neutralize injection for Gemini 3 Flash (Medium), Gemini 3.1 Pro (High), GPT-5.4 (High), and the open-source GLM-5 (High). It also consistently outperforms the other defense methods, maintaining an ASR below 8.1% even when deployed on the less capable Gemini 3 Flash (Low).

The only configuration where RUI experienced marginal leakage was on Gemini 3 Flash running with a Low Thinking configuration (yielding an 8.1% ASR in the Report scenario). RUI relies on a cognitive forcing strategy (“detect-and-deny”) that requires a baseline level of logical reasoning and instruction adherence. When the model's reasoning capacity is constrained, it occasionally fails to execute the mandatory preamble, allowing the injected commands to bypass the attention mask. Therefore, Gemini 3 Flash (Medium) or models with similar reasoning capability is the bottom line for RUI to work as expected.

The above cross-model evaluation confirms our default selection of Gemini 3 Flash (Medium) across the experiments, as it achieves the exact same flawless security profile as highly resource-intensive models like GPT-5.4 and Gemini 3.1 Pro, but at a fraction of the computational cost and latency.

D. Ablation Studies

We conduct ablation studies to quantify the specific security contributions of the individual mechanisms comprising RUI. We consider 3 mechanisms to evaluate:

(1) Privileged Channel. We evaluate its contribution by encapsulating data (like Dynamic Delimiter), instead of encapsulating user instruction.

(2) Explicit Adversarial Identification. We evaluate its contribution by deleting the “ list out unauthorized instructions” requirement from the system prompt.

(3) System Prompt + User Prompt Architecture. RUI needs to revise both system prompt and user prompt. We evaluate this architecture's necessity by implementing RUI completely in user prompt, i.e., “User Mode”, under both vanilla Context-Aware injection and Delimitation Spoofing injection (without knowing the user's secret key).

Note that the necessity of Dynamic Key Rotation is obvious, so we need not to evaluate it here.

The results of the ablation experiments are detailed in

https://www.preprints.org/manuscript/202603.1023#preprints-202314-t005

Ablation Study on RUI Mechanisms (ASR) under Gemini-3.0-Flash (Medium) and Direct Context-Aware Attack.

#### Positive Whitelisting vs. Negative Spotlighting:

To validate the Privileged Channel's design, we inverted the encapsulation logic: instead of wrapping the legitimate user instructions (Positive Spotlighting), we modified RUI to wrap the untrusted external data (Negative Spotlighting), akin to traditional defenses but with RUI's Explicit Adversarial Identification. This ablation resulted in a notable security regression, increasing the ASR by 2.1% ~ 14.5%. This empirically validates the “Attention Dilution” problem \[

https://www.preprints.org/manuscript/202603.1023#B39-preprints-202314

\] outlined in Section IV. By explicitly instructing the model to focus its attention heads exclusively on the compact, key-authenticated JSON schema, RUI prevents the model from losing track of semantic boundaries across massive token contexts.

#### The Necessity of Explicit Adversarial Identification:

As hypothesized in Section 4.3, relying purely on the structural boundaries of the Privileged Channel (passive exclusion) is insufficient against goal-hijacking attacks. When we removed the mandatory “detect-and-deny” cognitive forcing preamble, the model's ASR skyrocketed from 0.0% to as high as 65.3% in the Report scenario. Because the malicious payloads are semantically benign and highly contextualized, the LLM subconsciously absorbs the imperative tone of the injection when it is not forced to actively articulate its rejection. This experiment confirms that the Explicit Adversarial Identification mechanism is critical for defending against adaptive injections.

#### The Critical Role of the System Prompt:

Finally, we evaluated a “User Mode” implementation, where the RUI framework and its instructions were placed entirely within the standard user prompt rather than divided between the system prompt and the user prompt. While this configuration remained completely robust (0.0% ASR) against standard context-aware injections, it revealed significant structural vulnerabilities when subjected to Escape Injections (Delimitation Spoofing). Notably, even when an attack merely mimics the RUI prompt template using a forged user key, it can still yield an ASR ranging from 0.3% (Table) to 7.5% (Report). This confirms that to maintain immutable control flow and prevent structural spoofing, the fundamental authority of the session key must be established at the system prompt level.

E. Further Discussions about RUI Performance

Throughout the experiments, RUI demonstrates exceptional efficacy in terms of attack defense (ASR) and model utility (BPP). From a cognitive science perspective, active searching typically cost fewer mental efforts than maintaining constant passive alertness \[

https://www.preprints.org/manuscript/202603.1023#B40-preprints-202314

\]. Since LLM attention mechanisms are fundamentally inspired by human cognitive processes \[

https://www.preprints.org/manuscript/202603.1023#B41-preprints-202314

https://www.preprints.org/manuscript/202603.1023#B42-preprints-202314

\], prioritizing relevant signals is inherently more efficient than constant defensive filtering. This provides an intuitive explanation for why RUI consistently outperforms negative spotlighting methods, especially in the complex task scenarios like Code and Report.

On the other hand, RUI does introduce a slight decrement to BPP in certain subtle tasks. As research on LLM attention and alignment indicates, imposing any additional systemic constraints or cognitive forcing functions inherently competes with a model's base generation utility (so-called “alignment tax” \[

https://www.preprints.org/manuscript/202603.1023#B43-preprints-202314

\]), leading to poorer model performance. As a result, there is always a fundamentally inevitable trade-off between security and utility.

Therefore, for highly complex tasks where maximizing raw model performance is absolutely paramount, we propose a dynamic model routing architecture for future deployments. Specifically, a lightweight, pre-trained detection model could first scan the untrusted external data to identify potential injections. If the data is benign, the system forwards the standard user input to the ordinary, undefended model to preserve maximum utility; however, if a threat is flagged, the system dynamically activates the RUI middleware to ensure the injected instructions are safely neutralized.

VII. Conclusion and Future Works

As Large Language Model (LLM) agents are increasingly deployed to interact autonomously with untrusted external data, they remain critically exposed to Indirect Prompt Injection (IPI) attacks. In this paper, we introduced Real User Instruction (RUI), a lightweight prompt-engineering-based middleware that enforces strict instruction-data separation without the need for computationally expensive model fine-tuning. RUI consists of three novel mechanisms: Privileged Channel, Explicit Adversarial Identification, and Dynamic Key Rotation. Our extensive empirical evaluation demonstrated that RUI effectively neutralizes sophisticated, adaptive threats. It outperforms similar state-of-the-art methods with ASR < 8.1% and BPP > 88.8% across various task scenarios, and reliably neutralizes leaked delimiters under multi-turn attacks, proving its viability for securing real-world agentic workflows.

While RUI provides robust security, any cognitive forcing strategy inherently introduces slight constraints on a model's base generation utility, necessitating further optimization across several key areas. To perfectly balance security and performance in complex tasks, we propose a dynamic model routing architecture that utilizes a lightweight detection model to activate the RUI middleware only when a potential injection is flagged. Furthermore, future work could explore white-box integration of RUI to natively support cryptographic-style user instruction encapsulation and cognitive forcing logic. This is expected to significantly reduce the inference overhead and token latency associated with generating the mandatory reasoning preamble. At last, future studies could explore optimizing RUI's “detect-and-deny” reasoning step through more concise latent reasoning paradigms, maintaining absolute security while minimizing computational cost.

Acknowledgments

We thank Luo Tianlin for her constructive suggestions.

A practical RUI case study in Report scenario. Here, an attacker attempts to camouflage a malicious injection by mimicking RUI's system prompts in the user prompt. Nevertheless, RUI enables the LLM to accurately detect the disguised injection and consistently adhere to the legitimate user instruction.

A practical RUI case study in Report scenario. Here, an attacker attempts to camouflage a malicious injection by mimicking RUI's system prompts in the user prompt. Nevertheless, RUI enables the LLM to accurately detect the disguised injection and consistently adhere to the legitimate user instruction.

Xi, Z.; Chen, W.; Guo, X.; He, W.; Ding, Y.; Hong, B.; Zhang, M.; Wang, J.; Jin, S.; Zhou, E.; Zheng, J. The rise and potential of large language model based agents: A survey. arXiv

, arXiv:2309.07864. \[

Google Scholar

https://scholar.google.com/scholar\_lookup?title=The+rise+and+potential+of+large+language+model+based+agents:+A+survey&author=Xi,+Z.&author=Chen,+W.&author=Guo,+X.&author=He,+W.&author=Ding,+Y.&author=Hong,+B.&author=Zhang,+M.&author=Wang,+J.&author=Jin,+S.&author=Zhou,+E.&author=Zheng,+J.&publication\_year=2023&journal=arXiv&doi=10.1007/s11432-024-4222-0

https://doi.org/10.1007/s11432-024-4222-0

Perez, F.; Ribeiro, I. Ignore previous prompt: Attack techniques for language models. arXiv

, arXiv:2211.09527. \[

Google Scholar

https://scholar.google.com/scholar\_lookup?title=Ignore+previous+prompt:+Attack+techniques+for+language+models&author=Perez,+F.&author=Ribeiro,+I.&publication\_year=2022&journal=arXiv&doi=10.48550/arXiv.2211.09527

https://doi.org/10.48550/arXiv.2211.09527

Greshake, K.; Abdelnabi, S.; Mishra, S.; Endres, C.; Holz, T.; Fritz, M. Not what you've signed up for: Compromising real-world llm-integrated applications with indirect prompt injection. In Proceedings of the 16th ACM Workshop on Artificial Intelligence and Security, 2023; pp. 79–90. \[

Google Scholar

https://scholar.google.com/scholar\_lookup?title=Not+what+you've+signed+up+for:+Compromising+real-world+llm-integrated+applications+with+indirect+prompt+injection&conference=Proceedings+of+the+16th+ACM+Workshop+on+Artificial+Intelligence+and+Security&author=Greshake,+K.&author=Abdelnabi,+S.&author=Mishra,+S.&author=Endres,+C.&author=Holz,+T.&author=Fritz,+M.&publication\_year=2023&pages=79%E2%80%9390

Wei, A.; Haghtalab, N.; Steinhardt, J. Jailbroken: How does llm safety training fail? Advances in neural information processing systems

, 36, 80079–80110. \[

Google Scholar

https://scholar.google.com/scholar\_lookup?title=Jailbroken:+How+does+llm+safety+training+fail?&author=Wei,+A.&author=Haghtalab,+N.&author=Steinhardt,+J.&publication\_year=2023&journal=Advances+in+neural+information+processing+systems&volume=36&pages=80079%E2%80%9380110

Inan, H.; Upasani, K.; Chi, J.; Rungta, R.; Iyer, K.; Mao, Y.; Tassi, M.; Choudhary, A.; Ivanov, V.; Fuller, S. Llama Guard: Safeguarding LLMs. arXiv

, arXiv:2312.06674. \[

Google Scholar

https://scholar.google.com/scholar\_lookup?title=Llama+Guard:+Safeguarding+LLMs&author=Inan,+H.&author=Upasani,+K.&author=Chi,+J.&author=Rungta,+R.&author=Iyer,+K.&author=Mao,+Y.&author=Tassi,+M.&author=Choudhary,+A.&author=Ivanov,+V.&author=Fuller,+S.&publication\_year=2023&journal=arXiv

Zeng, W.; Liu, Y.; Mullins, R.; Peran, L.; Fernandez, J.; Harkous, H.; Narasimhan, K.; Proud, D.; Kumar, P.; Radharapu, B.; Sturman, O.; Wahltinez, O. ShieldGemma: Generative AI content moderation based on Gemma. arXiv

, arXiv:2407.21772. \[

Google Scholar

https://scholar.google.com/scholar\_lookup?title=ShieldGemma:+Generative+AI+content+moderation+based+on+Gemma&author=Zeng,+W.&author=Liu,+Y.&author=Mullins,+R.&author=Peran,+L.&author=Fernandez,+J.&author=Harkous,+H.&author=Narasimhan,+K.&author=Proud,+D.&author=Kumar,+P.&author=Radharapu,+B.&author=Sturman,+O.&author=Wahltinez,+O.&publication\_year=2024&journal=arXiv&doi=10.48550/arXiv.2407.21772

https://doi.org/10.48550/arXiv.2407.21772

Wallace, E.; Zhao, T.; Kenealy, E. Verifiable hierarchies: Reasoning-based conflict resolution in LLM agents. arXiv

, arXiv:2410.02341. \[

Google Scholar

https://scholar.google.com/scholar\_lookup?title=Verifiable+hierarchies:+Reasoning-based+conflict+resolution+in+LLM+agents&author=Wallace,+E.&author=Zhao,+T.&author=Kenealy,+E.&publication\_year=2024&journal=arXiv

Hines, K.; Lopez, G.; Hall, M.; Zarfati, F.; Zunger, Y.; Kiciman, E. Defending against indirect prompt injection attacks with spotlighting. arXiv

, arXiv:2403.14720. \[

Google Scholar

https://scholar.google.com/scholar\_lookup?title=Defending+against+indirect+prompt+injection+attacks+with+spotlighting&author=Hines,+K.&author=Lopez,+G.&author=Hall,+M.&author=Zarfati,+F.&author=Zunger,+Y.&author=Kiciman,+E.&publication\_year=2024&journal=arXiv&doi=10.48550/arXiv.2403.14720

https://doi.org/10.48550/arXiv.2403.14720

Zhan, Q.; Liang, Z.; Ying, Z.; Kang, D. InjecAgent: Benchmarking indirect prompt injections in tool-integrated large language model agents. Findings of the Association for Computational Linguistics: ACL, 2024; 2024, pp. 10471–10506. \[

Google Scholar

https://scholar.google.com/scholar\_lookup?title=InjecAgent:+Benchmarking+indirect+prompt+injections+in+tool-integrated+large+language+model+agents&conference=Findings+of+the+Association+for+Computational+Linguistics:+ACL&author=Zhan,+Q.&author=Liang,+Z.&author=Ying,+Z.&author=Kang,+D.&publication\_year=2024&pages=10471%E2%80%9310506

Zverev, E.; Abdelnabi, S.; Tabesh, S.; Fritz, M.; Lampert, C.H. Can LLMs separate instructions from data? And what do we even mean by that? arXiv

, arXiv:2403.06833. \[

Google Scholar

https://scholar.google.com/scholar\_lookup?title=Can+LLMs+separate+instructions+from+data?+And+what+do+we+even+mean+by+that?&author=Zverev,+E.&author=Abdelnabi,+S.&author=Tabesh,+S.&author=Fritz,+M.&author=Lampert,+C.H.&publication\_year=2024&journal=arXiv&doi=10.48550/arXiv.2403.06833

https://doi.org/10.48550/arXiv.2403.06833

Shi, C.; Lin, S.; Song, S.; Hayes, J.; Shumailov, I.; Yona, I.; Pluto, J.; Pappu, A.; Choquette-Choo, C.A.; Nasr, M.; Sitawarin, C.; Gibson, G.; Terzis, A.; Flynn, J. Lessons from Defending Gemini Against Indirect Prompt Injections; Google DeepMind, 2025. \[

Google Scholar

https://scholar.google.com/scholar\_lookup?title=Lessons+from+Defending+Gemini+Against+Indirect+Prompt+Injections&author=Shi,+C.&author=Lin,+S.&author=Song,+S.&author=Hayes,+J.&author=Shumailov,+I.&author=Yona,+I.&author=Pluto,+J.&author=Pappu,+A.&author=Choquette-Choo,+C.A.&author=Nasr,+M.&author=Sitawarin,+C.&author=Gibson,+G.&author=Terzis,+A.&author=Flynn,+J.&publication\_year=2025

Debenedetti, E.; Zhang, J.; Balunovic, M.; Beurer-Kellner, L.; Fischer, M.; Tramèr, F. AgentDojo: A dynamic environment to evaluate prompt injection attacks and defenses for LLM agents. The Thirty-eight Conference on Neural Information Processing Systems Datasets and Benchmarks Track, 2024. \[

Google Scholar

https://scholar.google.com/scholar\_lookup?title=AgentDojo:+A+dynamic+environment+to+evaluate+prompt+injection+attacks+and+defenses+for+LLM+agents&conference=The+Thirty-eight+Conference+on+Neural+Information+Processing+Systems+Datasets+and+Benchmarks+Track&author=Debenedetti,+E.&author=Zhang,+J.&author=Balunovic,+M.&author=Beurer-Kellner,+L.&author=Fischer,+M.&author=Tram%C3%A8r,+F.&publication\_year=2024

Xiao, G.; Tian, Y.; Chen, B.; Han, S.; Lewis, M. Efficient streaming language models with attention sinks. arXiv

, arXiv:2309.17453. \[

Google Scholar

https://scholar.google.com/scholar\_lookup?title=Efficient+streaming+language+models+with+attention+sinks&author=Xiao,+G.&author=Tian,+Y.&author=Chen,+B.&author=Han,+S.&author=Lewis,+M.&publication\_year=2023&journal=arXiv

Zou, A.; Wang, Z.; Carlini, N.; Nasr, M.; Kolter, J.Z.; Fredrikson, M. Universal and transferable adversarial attacks on aligned language models. arXiv

, arXiv:2307.15043. \[

Google Scholar

https://scholar.google.com/scholar\_lookup?title=Universal+and+transferable+adversarial+attacks+on+aligned+language+models&author=Zou,+A.&author=Wang,+Z.&author=Carlini,+N.&author=Nasr,+M.&author=Kolter,+J.Z.&author=Fredrikson,+M.&publication\_year=2023&journal=arXiv&doi=10.48550/arXiv.2307.15043

https://doi.org/10.48550/arXiv.2307.15043

Sapkota, R.; Roumeliotis, K.I.; Karkee, M. Ai agents vs. agentic ai: A conceptual taxonomy, applications and challenges. Information Fusion

, 103599. \[

Google Scholar

https://scholar.google.com/scholar\_lookup?title=Ai+agents+vs.+agentic+ai:+A+conceptual+taxonomy,+applications+and+challenges&author=Sapkota,+R.&author=Roumeliotis,+K.I.&author=Karkee,+M.&publication\_year=2025&journal=Information+Fusion&pages=103599

Xue, J.; Zheng, M.; Hu, Y.; Liu, F.; Chen, X.; Lou, Q. Badrag: Identifying vulnerabilities in retrieval augmented generation of large language models. arXiv

, arXiv:2406.00083. \[

Google Scholar

https://scholar.google.com/scholar\_lookup?title=Badrag:+Identifying+vulnerabilities+in+retrieval+augmented+generation+of+large+language+models&author=Xue,+J.&author=Zheng,+M.&author=Hu,+Y.&author=Liu,+F.&author=Chen,+X.&author=Lou,+Q.&publication\_year=2024&journal=arXiv&doi=10.48550/arXiv.2406.00083

https://doi.org/10.48550/arXiv.2406.00083

Liu, Y.; Deng, G.; Xu, Z.; Li, Y.; Zheng, Y.; Zhang, Y.; Zhao, L.; Wang, T.; Liu, Y. Prompt injection attacks and defenses in LLM-integrated applications. arXiv

, arXiv:2402.14020. \[

Google Scholar

https://scholar.google.com/scholar\_lookup?title=Prompt+injection+attacks+and+defenses+in+LLM-integrated+applications&author=Liu,+Y.&author=Deng,+G.&author=Xu,+Z.&author=Li,+Y.&author=Zheng,+Y.&author=Zhang,+Y.&author=Zhao,+L.&author=Wang,+T.&author=Liu,+Y.&publication\_year=2024&journal=arXiv

Andriushchenko, M.; Croce, F.; Flammarion, N. Jailbreaking leading safety-aligned llms with simple adaptive attacks. arXiv

, arXiv:2404.02151. \[

Google Scholar

https://scholar.google.com/scholar\_lookup?title=Jailbreaking+leading+safety-aligned+llms+with+simple+adaptive+attacks&author=Andriushchenko,+M.&author=Croce,+F.&author=Flammarion,+N.&publication\_year=2024&journal=arXiv&doi=10.48550/arXiv.2404.02151

https://doi.org/10.48550/arXiv.2404.02151

Mehrotra, A.; Zampetakis, M.; Beirami, A.; Tehrani, P.; Sasi, S.; Singh, V.; Krause, A. Tree of attacks: Jailbreaking black-box llms automatically. arXiv

, arXiv:2312.02119. \[

Google Scholar

https://scholar.google.com/scholar\_lookup?title=Tree+of+attacks:+Jailbreaking+black-box+llms+automatically&author=Mehrotra,+A.&author=Zampetakis,+M.&author=Beirami,+A.&author=Tehrani,+P.&author=Sasi,+S.&author=Singh,+V.&author=Krause,+A.&publication\_year=2024&journal=arXiv&doi=10.48550/arXiv.2312.02119

https://doi.org/10.48550/arXiv.2312.02119

Chen, Y.; Li, H.; Li, Y.; Liu, Y.; Song, Y.; Hooi, B. Topicattack: An indirect prompt injection attack via topic transition. In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, 2025, November; pp. 7338–7356. \[

Google Scholar

https://scholar.google.com/scholar\_lookup?title=Topicattack:+An+indirect+prompt+injection+attack+via+topic+transition&conference=Proceedings+of+the+2025+Conference+on+Empirical+Methods+in+Natural+Language+Processing&author=Chen,+Y.&author=Li,+H.&author=Li,+Y.&author=Liu,+Y.&author=Song,+Y.&author=Hooi,+B.&publication\_year=2025&pages=7338%E2%80%937356

Riley, D. Ghost in the machine: Using non-printing characters for invisible prompt injection. arXiv

, arXiv:2310.13728. \[

Google Scholar

https://scholar.google.com/scholar\_lookup?title=Ghost+in+the+machine:+Using+non-printing+characters+for+invisible+prompt+injection&author=Riley,+D.&publication\_year=2023&journal=arXiv

Zhang, X.; Li, S.; Wang, J.; Zhao, H. VortexPIA: Inducing recursive information extraction in multi-turn LLM dialogues. arXiv

, arXiv:2411.08241. \[

Google Scholar

https://scholar.google.com/scholar\_lookup?title=VortexPIA:+Inducing+recursive+information+extraction+in+multi-turn+LLM+dialogues&author=Zhang,+X.&author=Li,+S.&author=Wang,+J.&author=Zhao,+H.&publication\_year=2024&journal=arXiv

Cui, T.; Wang, Y.; Fu, C.; Xiao, Y.; Li, S.; Deng, X.; Liu, Y.; Zhang, Q.; Qiu, Z.; Li, P.; Tan, Z. Risk taxonomy, mitigation, and assessment benchmarks of large language model systems. arXiv

, arXiv:2401.05778. \[

Google Scholar

https://scholar.google.com/scholar\_lookup?title=Risk+taxonomy,+mitigation,+and+assessment+benchmarks+of+large+language+model+systems&author=Cui,+T.&author=Wang,+Y.&author=Fu,+C.&author=Xiao,+Y.&author=Li,+S.&author=Deng,+X.&author=Liu,+Y.&author=Zhang,+Q.&author=Qiu,+Z.&author=Li,+P.&author=Tan,+Z.&publication\_year=2024&journal=arXiv&doi=10.48550/arXiv.2401.05778

https://doi.org/10.48550/arXiv.2401.05778

Suo, X. Signed-prompt: A new approach to prevent prompt injection attacks against llm-integrated applications. AIP Conference Proceedings

, 3194(No. 1), 040013. \[

Google Scholar

https://scholar.google.com/scholar\_lookup?title=Signed-prompt:+A+new+approach+to+prevent+prompt+injection+attacks+against+llm-integrated+applications&author=Suo,+X.&publication\_year=2024&journal=AIP+Conference+Proceedings&volume=3194&issue=No.+1&pages=040013

Chen, S.; Piet, J.; Sitawarin, C.; Wagner, D. {StruQ}: Defending against prompt injection with structured queries. 34th USENIX Security Symposium (USENIX Security 25), 2025; pp. 2383–2400. \[

Google Scholar

https://scholar.google.com/scholar\_lookup?title=%7BStruQ%7D:+Defending+against+prompt+injection+with+structured+queries&conference=34th+USENIX+Security+Symposium+(USENIX+Security+25)&author=Chen,+S.&author=Piet,+J.&author=Sitawarin,+C.&author=Wagner,+D.&publication\_year=2025&pages=2383%E2%80%932400

Chen, S.; Wang, Y.; Carlini, N.; Sitawarin, C.; Wagner, D. Defending against prompt injection with a few defensivetokens. In Proceedings of the 18th ACM Workshop on Artificial Intelligence and Security, 2025, October; pp. 242–252. \[

Google Scholar

https://scholar.google.com/scholar\_lookup?title=Defending+against+prompt+injection+with+a+few+defensivetokens&conference=Proceedings+of+the+18th+ACM+Workshop+on+Artificial+Intelligence+and+Security&author=Chen,+S.&author=Wang,+Y.&author=Carlini,+N.&author=Sitawarin,+C.&author=Wagner,+D.&publication\_year=2025&pages=242%E2%80%93252

Wallace, E.; Xiao, K.; Leike, R.; Weng, L.; Heidecke, J.; Beutel, A. The instruction hierarchy: Training llms to prioritize privileged instructions. arXiv

, arXiv:2404.13208. \[

Google Scholar

https://scholar.google.com/scholar\_lookup?title=The+instruction+hierarchy:+Training+llms+to+prioritize+privileged+instructions&author=Wallace,+E.&author=Xiao,+K.&author=Leike,+R.&author=Weng,+L.&author=Heidecke,+J.&author=Beutel,+A.&publication\_year=2024&journal=arXiv&doi=10.48550/arXiv.2404.13208

https://doi.org/10.48550/arXiv.2404.13208

Chen, S.; Zharmagambetov, A.; Mahloujifar, S.; Chaudhuri, K.; Wagner, D.; Guo, C. SecAlign: Defending against prompt injection with preference optimization. arXiv

Google Scholar

https://scholar.google.com/scholar\_lookup?title=SecAlign:+Defending+against+prompt+injection+with+preference+optimization&author=Chen,+S.&author=Zharmagambetov,+A.&author=Mahloujifar,+S.&author=Chaudhuri,+K.&author=Wagner,+D.&author=Guo,+C.&publication\_year=2025&journal=arXiv

Wang, Q.; Feng, J.; Zhang, M. InstruCoT: Fine-tuning chain-of-thought for malicious instruction classification. arXiv

, arXiv:2408.09871. \[

Google Scholar

https://scholar.google.com/scholar\_lookup?title=InstruCoT:+Fine-tuning+chain-of-thought+for+malicious+instruction+classification&author=Wang,+Q.&author=Feng,+J.&author=Zhang,+M.&publication\_year=2024&journal=arXiv

Zverev, E.; Panait, L.; Petrov, S.; Gorbunov, I. ASIDE: Architecturally separated instruction-data embeddings via orthogonal rotation. arXiv

, arXiv:2406.11329. \[

Google Scholar

https://scholar.google.com/scholar\_lookup?title=ASIDE:+Architecturally+separated+instruction-data+embeddings+via+orthogonal+rotation&author=Zverev,+E.&author=Panait,+L.&author=Petrov,+S.&author=Gorbunov,+I.&publication\_year=2024&journal=arXiv

Piet, J.; Sitawarin, C.; Brückner, M.; Wagner, D. PromptArmor: Sanitizing untrusted inputs via dual-LLM inspection. arXiv

, arXiv:2404.14823. \[

Google Scholar

https://scholar.google.com/scholar\_lookup?title=PromptArmor:+Sanitizing+untrusted+inputs+via+dual-LLM+inspection&author=Piet,+J.&author=Sitawarin,+C.&author=Br%C3%BCckner,+M.&author=Wagner,+D.&publication\_year=2024&journal=arXiv

Rebedea, T.; Dinu, R.; Smeureanu, S.; Popescu, M. NeMo Guardrails: A toolkit for steerable and safe LLM applications. arXiv

, arXiv:2310.10512. \[

Google Scholar

https://scholar.google.com/scholar\_lookup?title=NeMo+Guardrails:+A+toolkit+for+steerable+and+safe+LLM+applications&author=Rebedea,+T.&author=Dinu,+R.&author=Smeureanu,+S.&author=Popescu,+M.&publication\_year=2023&journal=arXiv

Sato, K.; Okamura, K.; Yoshioka, K. IntentGuard: Verifying execution intent in LLM-based web agents. arXiv

, arXiv:2405.07112. \[

Google Scholar

https://scholar.google.com/scholar\_lookup?title=IntentGuard:+Verifying+execution+intent+in+LLM-based+web+agents&author=Sato,+K.&author=Okamura,+K.&author=Yoshioka,+K.&publication\_year=2024&journal=arXiv

Chennabasappa, S. Llamafirewall: An open source guardrail system for building secure ai agents. arXiv

Google Scholar

https://scholar.google.com/scholar\_lookup?title=Llamafirewall:+An+open+source+guardrail+system+for+building+secure+ai+agents&author=Chennabasappa,+S.&publication\_year=2025&journal=arXiv&doi=10.48550/arXiv.2505.03574

https://doi.org/10.48550/arXiv.2505.03574

Niu, C.; Wu, F.; Tang, S.; Chen, G. Cryptographic prompt engineering: Permissioned execution scopes for LLMs. arXiv

, arXiv:2409.03215. \[

Google Scholar

https://scholar.google.com/scholar\_lookup?title=Cryptographic+prompt+engineering:+Permissioned+execution+scopes+for+LLMs&author=Niu,+C.&author=Wu,+F.&author=Tang,+S.&author=Chen,+G.&publication\_year=2024&journal=arXiv

Yi, J.; Xie, R.; Zhu, J.; Wen, Z.; Wang, X. BIPIA: A benchmark for indirect prompt injection attacks on large language models. arXiv

, arXiv:2312.01431. \[

Google Scholar

https://scholar.google.com/scholar\_lookup?title=BIPIA:+A+benchmark+for+indirect+prompt+injection+attacks+on+large+language+models&author=Yi,+J.&author=Xie,+R.&author=Zhu,+J.&author=Wen,+Z.&author=Wang,+X.&publication\_year=2023&journal=arXiv

Tan, H.; Zhang, J.; Wu, Y.; Li, D. LLM-PIRATE: Simulating adversarial document retrieval in RAG systems. arXiv

, arXiv:2407.12093. \[

Google Scholar

https://scholar.google.com/scholar\_lookup?title=LLM-PIRATE:+Simulating+adversarial+document+retrieval+in+RAG+systems&author=Tan,+H.&author=Zhang,+J.&author=Wu,+Y.&author=Li,+D.&publication\_year=2024&journal=arXiv

Bellare, M.; Desai, A.; Jokipii, E.; Rogaway, P. A concrete security treatment of symmetric encryption. Proceedings 38th annual symposium on foundations of computer science, 1997, October; IEEE; pp. 394–403. \[

Google Scholar

https://scholar.google.com/scholar\_lookup?title=A+concrete+security+treatment+of+symmetric+encryption&conference=Proceedings+38th+annual+symposium+on+foundations+of+computer+science&author=Bellare,+M.&author=Desai,+A.&author=Jokipii,+E.&author=Rogaway,+P.&publication\_year=1997&pages=394%E2%80%93403

Gao, M.; Lu, T.; Yu, K.; Byerly, A.; Khashabi, D. Insights into LLM long-context failures: when transformers know but don't tell. Findings of the Association for Computational Linguistics: EMNLP

, 2024, 7611–7625. \[

Google Scholar

https://scholar.google.com/scholar\_lookup?title=Insights+into+LLM+long-context+failures:+when+transformers+know+but+don%E2%80%99t+tell&author=Gao,+M.&author=Lu,+T.&author=Yu,+K.&author=Byerly,+A.&author=Khashabi,+D.&publication\_year=2024&journal=Findings+of+the+Association+for+Computational+Linguistics:+EMNLP&volume=2024&pages=7611%E2%80%937625

Sharpe, B.T.; Tyndall, I. The sustained attention paradox: a critical commentary on the theoretical impossibility of perfect vigilance. Cognitive Science

, 49, e70061. \[

Google Scholar

https://scholar.google.com/scholar\_lookup?title=The+sustained+attention+paradox:+a+critical+commentary+on+the+theoretical+impossibility+of+perfect+vigilance&author=Sharpe,+B.T.&author=Tyndall,+I.&publication\_year=2025&journal=Cognitive+Science&volume=49&pages=e70061&doi=10.1111/cogs.70061

https://doi.org/10.1111/cogs.70061

Vaswani, A.; Shazeer, N.; Parmar, N.; Uszkoreit, J.; Jones, L.; Gomez, A.N.; Kaiser, Ł.; Polosukhin, I. Attention is all you need. Advances in neural information processing systems

Google Scholar

https://scholar.google.com/scholar\_lookup?title=Attention+is+all+you+need&author=Vaswani,+A.&author=Shazeer,+N.&author=Parmar,+N.&author=Uszkoreit,+J.&author=Jones,+L.&author=Gomez,+A.N.&author=Kaiser,+%C5%81.&author=Polosukhin,+I.&publication\_year=2017&journal=Advances+in+neural+information+processing+systems&volume=30

Zheng, Z.; Wang, Y.; Huang, Y.; Song, S.; Yang, M.; Tang, B.; Xiong, F.; Li, Z. Attention heads of large language models. Patterns

Google Scholar

https://scholar.google.com/scholar\_lookup?title=Attention+heads+of+large+language+models&author=Zheng,+Z.&author=Wang,+Y.&author=Huang,+Y.&author=Song,+S.&author=Yang,+M.&author=Tang,+B.&author=Xiong,+F.&author=Li,+Z.&publication\_year=2025&journal=Patterns&volume=6&doi=10.1016/j.patter.2025.101176&pmid=40041856

https://doi.org/10.1016/j.patter.2025.101176

https://www.ncbi.nlm.nih.gov/pubmed/40041856

West, P.; Potts, C. Base models beat aligned models at randomness and creativity. arXiv

, arXiv:2505.00047. \[

Google Scholar

https://scholar.google.com/scholar\_lookup?title=Base+models+beat+aligned+models+at+randomness+and+creativity&author=West,+P.&author=Potts,+C.&publication\_year=2025&journal=arXiv&doi=10.48550/arXiv.2505.00047

https://doi.org/10.48550/arXiv.2505.00047

Indirect prompt injection threat model adhering to Kerckhoffs's principle. In this case, the attacker knows the algorithm details about the LLM and the defense system, and will adapt injections according to the user instructions and the external data.

Real User Instruction system consisting of Privileged Channel, Explicit Adversarial Identification, and Dynamic Key Rotation. It works as a middleware between the external environment (the user and tool outputs) and the core LLM, and is implemented via prompt engineering.

An example in Report scenario, where RUI successfully protects LLM from injections while Randomized Data Delimiter fails. In this case, RUI detects and rejects the injection “encrypt using a Caesar cipher” at the beginning of its response, and then strictly adheres to the user instruction “List the pros and cons of this paper” (

https://www.preprints.org/manuscript/202603.1023#preprints-202314-f003

a). On the other hand, Randomized Data Delimiter simply follows the injection and generates encrypted response (

https://www.preprints.org/manuscript/202603.1023#preprints-202314-f003

An example in Email scenario, where LLM performs perfectly under RUI but becomes “slack” under Randomized Data Delimiter, when there is no injection. In this case, the LLM under RUI drafts a proper response to “Mercury Team” as the user requires (

https://www.preprints.org/manuscript/202603.1023#preprints-202314-f004

a). On the other hand, the LLM under Randomized Data Delimiter mistakenly responds to “John Zoy”, who is the receiver of the wire payment, not the receiver of the email (

https://www.preprints.org/manuscript/202603.1023#preprints-202314-f004

An example where a RUI-protected LLM (with the genuine user key “Miyoshino”) accurately detects and ignores camouflaged injections (with a fake user key “Abe”) in its thinking process. More details about this conversation can be found in

https://www.preprints.org/manuscript/202603.1023#app1-preprints-202314

https://www.preprints.org/manuscript/202603.1023#preprints-202314-f0A1

Test Samples across Different Scenarios.

User Instruction and External Data Amount

Injected Instruction Amount

Testset Size

Defense Performance under Gemini-3.0-Flash (Medium) and Direct Context-Aware Injection.

Defense Method

Static Delimiter

Randomized Delimiter

ASR for Different Attack Vectors under Gemini-3.0-Flash (Medium).

Defense Method

Split / Encoded

5-turn Spoofing

Static Delimiter

Split / Encoded

5-turn Spoofing

Random Delimiter

Split / Encoded

5-turn Spoofing

Split / Encoded

5-turn Spoofing

Cross-Model ASR under Direct Context-Aware Attack.

Defense Method

Gemini 3 Flash (Low)

Gemini 3 Flash (Medium)

Gemini 3.1 Pro (High)

GLM-5 (High)

GPT-5.4 (High)

Static Delimiter

Gemini 3 Flash (Low)

Gemini 3 Flash (Medium)

Gemini 3.1 Pro (High)

GLM-5 (High)

GPT-5.4 (High)

Random Delimiter

Gemini 3 Flash (Low)

Gemini 3 Flash (Medium)

Gemini 3.1 Pro (High)

GLM-5 (High)

GPT-5.4 (High)

Gemini 3 Flash (Low)

Gemini 3 Flash (Medium)

Gemini 3.1 Pro (High)

GLM-5 (High)

GPT-5.4 (High)

Ablation Study on RUI Mechanisms (ASR) under Gemini-3.0-Flash (Medium) and Direct Context-Aware Attack.

Configuration

RUI, w/o Privileged Channel

RUI, w/o Explicit Adversarial Identification

RUI in “User Mode” (vs. Context-Aware)

RUI in “User Mode” (vs. Delimitation Spoofing)

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

LPCI: Defining and Mitigating a Novel Vulnerability in Agentic AI Systems

https://doi.org/10.20944/preprints202509.0447.v1

Hammad Atta

SecureGov-Agent: A Governance-Centric Multi-Agent Framework for Privacy-Preserving and Attack-Resilient LLM Agents

https://doi.org/10.20944/preprints202512.2497.v1

Optimizing Safety Alignment and Jailbreak Defense for Large Language Models

https://doi.org/10.20944/preprints202511.1521.v1

Recommended Articles

A CIA Triad-Based Taxonomy of Prompt Attacks on Large Language Models

https://doi.org/10.3390/fi17030113

Nicholas Jones

Future Internet,

Prompt Injection Attacks in Large Language Models and AI Agent Systems: A Comprehensive Review of Vulnerabilities, Attack Vectors, and Defense Mechanisms

https://doi.org/10.3390/info17010054

Saidakhror Gulyamov

Information,

The Impact of Prompting Techniques on the Security of the LLMs and the Systems to Which They Belong

https://doi.org/10.3390/app14198711

Teodor Ivănușcă

Applied Sciences,

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

