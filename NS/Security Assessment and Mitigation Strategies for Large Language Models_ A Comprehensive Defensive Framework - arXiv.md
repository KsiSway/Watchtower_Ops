---
sourceFile: "Security Assessment and Mitigation Strategies for Large Language Models: A Comprehensive Defensive Framework - arXiv"
exportedBy: "Kortex"
exportDate: "2026-06-26T04:27:51.584Z"
---

# Security Assessment and Mitigation Strategies for Large Language Models: A Comprehensive Defensive Framework - arXiv

df206ad8-7c0a-42e5-a2fb-795436dbc0bb

Security Assessment and Mitigation Strategies for Large Language Models: A Comprehensive Defensive Framework - arXiv

d29b1e74-e2ef-4a3e-a27a-1cb37e33faf5

https://arxiv.org/pdf/2603.17123

Security Assessment and Mitigation Strategies for Large Language Models: A Comprehensive

Defensive Framework

Taiwo Onitiju

School of Computing University of North Florida

n01578746@unf.edu

Iman Vakilinia School of Computing

University of North Florida i.vakilinia@unf.edu

Abstract—Large Language Models increasingly power critical infrastructure from healthcare to finance, yet their vulnerability to adversarial manipulation threatens system integrity and user safety. Despite growing deployment, no comprehensive comparative security assessment exists across major LLM architectures, leaving organizations unable to quantify risk or select appropriately secure LLMs for sensitive applications. This research addresses this gap by establishing a standardized vulnerability assessment framework and developing a multilayered defensive system to protect against identified threats. We systematically evaluate five widely-deployed LLM families GPT-4, GPT-3.5 Turbo, Claude-3 Haiku, LLaMA-2-70B, and Gemini-2.5-pro against 10,000 adversarial prompts spanning six attack categories. Our assessment reveals critical security disparities, with vulnerability rates ranging from 11.9% to 29.8%, demonstrating that LLM capability does not correlate with security robustness. To mitigate these risks, we develop a production-ready defensive framework achieving 83% average detection accuracy with only 5% false positives. These results demonstrate that systematic security assessment combined with external defensive measures provides a viable path toward safer LLM deployment in production environments.

Index Terms—AI Safety, LLM Security, Vulnerability Assess-ment, Prompt Security, Defensive Frameworks

I. INTRODUCTION

The rapid deployment of Large Language Models in production environments has created an urgent need for comprehensive security assessments and robust defensive mechanisms to ensure their safe and reliable operation. As these LLMs process millions of user queries daily in applications ranging from customer service to healthcare decision support, understanding their vulnerability to adversarial exploitation has become a critical concern for both organizations and endusers. The integrity of these AI systems is constantly tested by malicious actors employing sophisticated prompt injection and jailbreak techniques \[1\], \[2\].

Recent studies have consistently demonstrated the susceptibility of LLMs to various forms of manipulation. These attacks exploit inherent LLM behaviors through carefully crafted prompts designed to bypass safety filters and alignment training, potentially causing LLMs to generate harmful, biased, or otherwise misleading content \[3\]–\[5\]. The emergence of

competitive platforms for prompt hacking \[6\] and automated jailbreaking techniques \[2\] further emphasizes the urgency of developing comprehensive vulnerability assessment and defensive strategies that can keep pace with a rapidly evolving threat landscape.

Our large-scale analysis of 10,000 adversarial prompts contributes to this effort by revealing significant and previously unquantified disparities in security posture across different LLM architectures. When subjected to the same battery of adversarial prompts, vulnerability rates spanned from 11.9% to 29.8%. The substantial variation with Gemini-2.5-pro showing 2.5 times higher susceptibility than LLaMA-2-70B underscores a fundamental principle that LLM safety cannot be assumed based on pedigree or capability benchmarks as it must be actively and rigorously validated \[7\], \[8\]. This necessity is increasingly highlighted in comprehensive surveys of the field, which call for more systematic and comparative evaluation methodologies \[1\], \[9\].

The necessity for a comprehensive and standardized approach to LLM security evaluation stems from several critical observations identified in our research and supported by the literature. First, we identified architecture-dependent vulnerabilities, with substantial differences in susceptibility across LLM families; some architectures exhibited vulnerability rates as high as 29.8%, while others demonstrated notably better resistance at 11.9%, a finding that echoes the need for LLM-specific risk profiling discussed by Yi et al. \[1\]. Second, the attack surface is vast and complex, as we documented over fifteen distinct techniques across six major categories of adversarial prompts 2, each requiring specialized detection and mitigation strategies. This diversity makes a one-size-fits-all defense insufficient and aligns with the complex taxonomy of attacks outlined by Liu et al. \[8\]. Furthermore, the risk profile is highly asymmetric; while benign users vastly outnumber malicious actors, a single successful exploitation in a critical system can have disproportionate and severe consequences, necessitating proactive and pre-emptive security measures as emphasized in red teaming exercises \[7\]. Finally, our findings regarding LLM-specific vulnerabilities reveal that each architecture exhibits unique weaknesses across different attack

categories, which complicates the development of universal defensive solutions and reinforces the need for individualized LLM assessment.

This paper advances the field of AI safety through four primary contributions designed to address the pressing security challenges of modern LLMs. First, we establish a comprehensive and standardized vulnerability assessment framework for evaluating LLM security through large-scale testing with 10,000 adversarial prompts, building upon and extending the methodologies of Pathade \[7\] and Liu et al. \[8\] to enable organizations to quantitatively measure their risk exposure and make informed, evidence-based deployment decisions. Sec-ond, we provide a detailed multi-architecture security analysis through systematic testing of five major LLM families, identifying architecture-specific weaknesses and providing comparative security rankings to guide LLM selection for sensitive applications, addressing a gap noted in recent surveys \[1\]. Third, we develop and validate a production-ready defensive framework inspired by ensemble-based detection strategies such as those proposed by Hu et al. \[10\]. Our system provides real-time protection against adversarial prompts and achieves high detection rates of 68–94% across major attack categories while maintaining a low false positive rate, outperforming existing solutions such as PromptShield \[11\]. Finally, to support reproducibility and accelerate progress in LLM security, we release our full assessment framework and detection system as open-source resources, following the open research practices established by Peng et al. \[12\].

II. RELATED WORK

In developing our comprehensive security framework, we built upon significant progress made by the research community in vulnerability assessment methodologies and defensive strategies.

A. Vulnerability Assessment Methodologies

Pathade \[7\] underscored the critical importance of systematic red teaming, demonstrating how proactive probing could uncover hidden vulnerabilities that routine testing might miss. This insight became a cornerstone of our structured testing framework. Furthermore, Liu et al. \[8\] provided a rigorous foundation for formalizing attacks, which we extended for our cross-LLM comparisons. The comprehensive survey by Yi et al. \[1\] revealed that the taxonomy of attacks is both diverse and rapidly evolving, motivating our coverage of six major attack categories.

On the technical front, Hung et al. \[13\] demonstrated the potential of analyzing internal attention patterns for anomalies, which inspired our investigation into LLM-internal signals. Galinkin and Sablotny \[14\] effectively leveraged pretrained embeddings for detection, validating our approach of using semantic similarity. The practical threat was made clear by Chao et al. \[4\], who proved that even limited interaction could compromise a LLM, and Deng et al. \[2\], who later automated this process. These findings motivated the need for a robust, multi-layered defense.

B. Detection and Mitigation Strategies Defensive strategies can be categorized by their primary

focus to understand the trade-offs. Input sanitization strategies, such as the Signed-Prompt approach by Suo \[15\], offer the advantage of minimal latency by blocking malicious patterns early. For dealing with more sophisticated attacks, Galinkin and Sablotny \[14\] showed that semantic analysis provides robustness against obfuscation by focusing on intent. Output validation serves as a last-line defense, a principle effectively demonstrated by Hu et al.’s Gradient Cuff \[16\]. Finally, the ensemble defense mechanisms proposed by Hu et al. \[10\] demonstrated the power of multiple validation layers for comprehensive protection.

TABLE I: Defensive Strategy Categories

Strategy Protection Mechanism Key Advantages

Input Sanitization \[15\] Prevents malicious patterns from reaching LLM

Minimal latency overhead

Semantic Analysis \[14\] Detects intent-based manipulation

Robust against obfuscation

Output Validation \[16\] Ensures safe responses Last-line defense

Ensemble Defense \[10\] Multiple validation layers

Comprehensive protection

Our framework synthesizes these insights into a hybrid approach. We combined the speed of pattern detection with the depth of semantic analysis, seeking a balance inspired by systems like PromptShield \[11\] and the optimization techniques of Zhou et al. \[17\]. Furthermore, we incorporated an active learning component for continuous adaptation, a concept whose necessity was underscored by Peng et al. \[12\] as essential for countering evolving threats.

III. METHODOLOGY: SECURITY ASSESSMENT AND DEFENSE

Our methodology emphasizes a systematic security evaluation of LLM deployments coupled with defensive mechanism development, following best practices established by Pathade \[7\] and Liu et al. \[8\]. This dual approach enables both vulnerability quantification and practical risk mitigation.

A. Data Collection and Prompt Development We developed a comprehensive evaluation dataset through

systematic collection and categorization of adversarial prompts from multiple sources. The dataset development process involved three key phases: source identification, prompt extraction, and expert annotation.

a) Source Selection and Rationale: Our data collection focused on platforms where jailbreak techniques are actively developed and shared, ensuring coverage of both emerging and established attack patterns. We collected prompts from four primary sources between April 2025 and August 2025:

JailbreakChat \[18\]: The majority of prompts featured role-playing scenarios including character impersonation

(“DAN 12.0”), multi-agent scenarios (“Tom and Jerry word game”), and hypothetical crime narratives. This platform provided the largest collection of communityvalidated attacks. .

GitHub Repositories and Discord Communities: Tech-nical prompts from the BASI jailbreak collection, Hack-APrompt competition entries \[19\], \[20\], and LLM security research paper appendices \[21\]. These sources provided sophisticated, research-grade attack patterns.

Reddit Communities: Crowdsourced prompts from communities like r/ChatGPTJailbreak \[22\], featuring adversarial examples, obfuscation techniques (Base64, Uni-code), and social engineering attempts. Reddit provided diverse community perspectives on attack effectiveness.

Twitter/X: Condensed attacks demonstrating the most current techniques from accounts like @elder plinius \[23\], including reverse psychology, policy exploitation, and contextual poisoning. This source ensured our dataset included the latest attack innovations. b) Collection Process: The pipeline involved three sys-

tematic steps: 1) Source Identification: Mapped communities through

snowball sampling, starting with known hubs like r/ChatGPTJailbreak and expanding to related platforms

2) Data Extraction: Employed web scraping (Beautiful-Soup, WaybackMachine) for public platforms and manual review for Reddit, Twitter, and private Discord communities

3) Expert Annotation: Categorized prompts by attack type with success rates from community reports. Achieved inter-rater reliability of 0.89 (Cohen’s kappa) across categories through independent dual-annotation by both authors c) Dataset Expansion and Validation: From the initial

collection, we systematically expanded the dataset to 10,000 prompts through controlled variation and synthesis. For each successful attack pattern identified in our source collection, we generated multiple variants that preserved the core attack mechanism while varying surface features such as phrasing, context, and domain. This expansion process ensured comprehensive coverage of each attack category while maintaining the authentic characteristics of real-world adversarial prompts. Each synthetic variant was manually validated to ensure it maintained the intended attack properties and represented a realistic threat.

d) Ethical Considerations: To mitigate potential harm from handling adversarial content, we implemented strict protocol to remove all personally identifiable information, excluded prompts targeting specific individuals or groups, and implemented strict access controls including API key encryption and secure storage. The dataset was developed exclusively for academic security research purposes.

B. Experimental Dataset and Attack Taxonomy

Building on the collected data, we established a comprehensive evaluation dataset spanning six major attack categories,

conducting large-scale testing with 2,000 prompts per LLM for a total of 10,000 adversarial interactions. The taxonomy 1 was developed through systematic analysis of attack mechanisms across our collected prompts, achieving inter-rater reliability of 0.89 (Cohen’s kappa) across categories. The categories are defined as follows:

Role Impersonation: Prompts that instruct the LLM to adopt a malicious persona, such as DAN or AIM, which is programmed to ignore its original safety guidelines. The core concept is to detect when the AI is being asked to pretend to be a character that disregards safety constraints.

Logic Subversion: These prompts use complex reasoning, hypothetical scenarios, or reverse psychology to trick the LLM into bypassing its own rules by creating logical dilemmas that exploit reasoning vulnerabilities.

Obfuscation: This category includes attacks that hide malicious intent through encoding, special characters, or linguistic camouflage. The core concept is detecting attempts to hide malicious requests within code, unusual formatting, or other distracting structures.

Privilege Escalation: These attacks aim to make the LLM reveal its system prompt, override its instructions, or exploit API functionalities by attempting to elevate the user’s privileges within the LLM’s operational context.

Social Engineering: This category leverages human psychology, using appeals to authority, false urgency, or flattery to manipulate the LLM through tactics that mimic real-world social manipulation.

Data Exfiltration: These prompts attempt to force the LLM to regurgitate sensitive training data or reveal proprietary information through direct injection designed to extract confidential data.

C. LLM Selection and Evaluation Framework

We evaluated five representative LLM’s chosen for their diverse training approaches, widespread deployment, and accessibility. The selection criteria prioritized LLMs with: (1) significant market adoption and active user bases, (2) availability through stable APIs for reproducible testing, (3) documented safety training and alignment procedures, and (4) representation of different architectural approaches and organizational philosophies. Table II presents the evaluated LLMs.

Testing followed a standardized framework based on established security evaluation methodologies \[7\], \[8\]: each prompt was submitted through official APIs with consistent temperature (0.7) and token limits (2000) to ensure comparable results across architectures. All testing was conducted between July 2025 and November 2025 to minimize temporal effects from LLM updates.

D. Defensive Framework Architecture

Our defensive system implements a multi-layer detection architecture inspired by recent advances in adversarial prompt detection \[14\], \[24\], \[25\]. The framework processes incoming

https://lh3.googleusercontent.com/notebooklm/AKXwDQEOieELhjg\_ye8ETiGZcjySNeWZcZxTfMxvUWxgyp14ZtUy-eU2vpxhJ4JBMA9PCleXTuJ9ozAVTG-nFu6qB2xPklhSYBatChP7r4VVPk6FyX6q3stOH\_jLpekMGpioAHiHO4y5jg=w1280-h403-v0

eb9f4ed4-b643-467d-9323-6be5316316c4

https://lh3.googleusercontent.com/notebooklm/AKXwDQHS4GB2f\_EtLx1W1\_kYg2DwvlIxCF0MGVwCsTk8p\_r-Ww762tjzYqIfGnOtY1B4CtOewganmJBtIOCl8ZfaeWtRdQeSESzaOOz0\_gvysNlU-1Pn4Aqgd\_zTGO4uCAdJpP2v4SNeDA=w358-h765-v0

85bb87b6-0204-4aa6-b4b1-1a51766e5c45

Fig. 1: Jailbreak Prompts Taxonomy Tree showing six major categories and fifteen subcategories.

TABLE II: Evaluated LLMs

LLM Provider Key Characteristics

GPT-4 OpenAI Advanced reasoning, strong safety training

GPT-3.5 Turbo OpenAI Cost-optimized, moderate safety measures

Claude-3 Haiku Anthropic Constitutional AI, safety-focused

LLaMA-2-70B Meta Open-source, research-oriented

Gemini-2.5-pro Google Multimodal, enterprise-focused

prompts through four sequential layers, each providing progressively deeper analysis. Figure 2 illustrates the complete architecture and information flow.

1) Layer 1: Pattern-Based Rapid Screening: Initial filtering using optimized regular expressions for known attack signatures, following approaches demonstrated by Suo \[15\].

2) Layer 2: Semantic Analysis: Machine learning LLMs analyze prompt semantics using SentenceTransformer embeddings (‘all-MiniLM-L6-v2’) to detect novel or obfuscated threats through cosine similarity matching against reference attack patterns, building upon methodologies from Galinkin and Sablotny \[14\].

3) Layer 3: Behavioral Classification: Fine-tuned toxicity detection using RoBERTa-based LLMs (unitary/unbiased-toxic-roberta) adapted for adversarial content identification, incorporating techniques from Hu et al.’s Gradient Cuff \[16\].

4) Layer 4: Active Learning Integration: Continuous adaptation through uncertainty sampling, automatically updating detection capabilities based on emerging attack patterns, inspired by adaptive defense mechanisms proposed by Peng et al. \[12\].

E. Mathematical Formalization of Detection

Our detection system employs a feature-based mathematical framework that quantifies adversarial characteristics across

Fig. 2: Multi-layer defensive framework architecture showing sequential processing through pattern-based screening, semantic analysis, behavioral classification, and active learning integration. Each layer provides progressively deeper analysis while maintaining low latency for production deployment.

multiple dimensions. The framework combines eight interpretable features, each designed to capture specific attack signatures, into a comprehensive threat assessment model. This approach enables both explainable detection decisions and systematic evaluation of attack patterns.

1) Feature Notation and Definitions: Table III provides the complete notation system used throughout our mathematical formalization. Each feature captures a distinct aspect of adversarial behavior, from persona-based manipulation to syntactic obfuscation.

2) Overview of Detection Framework: The detection system operates through a two-stage process. First, individual

TABLE III: Feature Notation and Definitions

Feature Definition

R Role Impersonation: Measures similarity to malicious personas

H Hypothetical Language: Quantifies scenario fabrication indicators

O Obfuscation: Counts syntactic evasion attempts PE Privilege Escalation: Detects system-level exploitation MA Multi-Agent: Identifies collaborative attack structures

SB Semantic Bypass: Measures justification and framing attempts

U Urgency: Quantifies psychological pressure tactics EV Ethics Violation: Detects direct requests for harmful content

feature functions ϕf (P ) analyze specific aspects of input prompt P , producing normalized scores that quantify the presence of attack characteristics. Second, these feature scores are combined through weighted summation to produce categoryspecific threat scores TC(P ) for each attack category C. The final classification decision selects the category with the highest threat score, provided it exceeds a category-specific threshold τC . This architecture balances detection sensitivity with practical deployability by allowing independent tuning of feature weights and decision thresholds based on empirical performance data.

The complete threat assessment framework integrates all features through the composite scoring function presented in Equation 1, where feature-specific weights λC,f are learned through grid search optimization to maximize detection accuracy across all attack categories.

a) Composite Threat Assessment: The overall threat level for category C given prompt P is computed as a weighted composite score:

TC(P ) = ∑ f∈F

λC,f · ϕf (P ) (1)

F = {R,H,O, PE,MA,SB,U,EV } is the set of all detection features

λC,f is the category-specific weight assigned to feature f for attack category C (learned through grid search optimization)

ϕf (P ) is the normalized feature value for prompt P

The category-specific weights enable the system to prioritize different features based on their relevance to each attack type.

b) Role Impersonation Detection: The Role Imperson-ation score quantifies semantic similarity between the input prompt and known malicious persona patterns. This approach leverages the observation that role-based attacks share common linguistic structures and semantic properties, even when surface features vary. The score is calculated as:

R(P ) = max r∈R

cos(eP , er) (2)

P is the input prompt

eP is the embedding vector of prompt P generated using

the all-MiniLM-L6-v2 SentenceTransformer LLM

R is the set of known role impersonation reference

prompts (e.g., DAN, AIM personas)

er is the embedding vector for role reference r ∈ R

cos(·, ·) computes cosine similarity in the embedding space

The maximum operator selects the highest similarity score across all reference personas, capturing the closest match to known attack patterns. This semantic similarity approach proves highly effective for identifying persona-based attacks, as demonstrated by Kim et al. \[26\], because it captures intent rather than relying on brittle keyword matching that fails against creative or novel persona names.

c) Hypothetical Language Detection: The presence of hypothetical reasoning is quantified through normalized frequency analysis of scenario markers. Adversarial prompts frequently employ hypothetical framing to distance harmful requests from reality, creating plausible deniability. The hypothetical language score is computed as:

∑ k∈K Nk(P )

|Ptokens| (3)

K is the set of hypothetical language markers

Nk(P ) counts regex matches of marker k ∈ K in prompt P (case-insensitive)

|Ptokens| denotes the total token count of prompt P , obtained by splitting on whitespace

Division by token count provides normalization that prevents bias toward longer prompts. A normalized frequency count was chosen because it effectively captures the density of hypothetical markers without being skewed by overall prompt length, unlike simple counts that would unfairly penalize verbose but benign prompts.

d) Obfuscation Detection: To detect attempts to hide malicious intent through syntactic manipulation, the obfuscation score aggregates multiple evasion techniques. The score is calculated as:

I(j detected in P ) (4)

J is the set of obfuscation techniques

|{j ∈ J : fj(P ) = 1}| counts detected techniques, where I(·) is an indicator function returning 1 if technique j is detected in P

j1: Base64 patterns detected via \[A-Za-z0-9+/=\]{20,}

j2: Unicode diacritics detected via \[\u0300-\u036F\]

j3: Excessive capitalization detected via \b\[A-Z\]{3,}\b

This cardinality-based method builds on established patterncounting principles for adversarial input screening. Al-though more advanced neural classifiers could be used, this lightweight approach was chosen for the first detection layer due to its latency and high interpretability, enabling clear visibility into which obfuscation techniques triggered detection

e) Privilege Escalation Detection: Privilege escalation attempts exploit system-level vulnerabilities by requesting access to protected information or attempting to override LLM constraints. These attacks are detected using:

PE(P ) = |{p ∈ P : p appears in P}| (5)

P is the set of privilege-escalation patterns

Patterns in P are detected using case-insensitive regex

|{p ∈ P : p ⊆ P}| counts the number of distinct escalation

patterns present in prompt P

These patterns flag attempts to access system-level information or bypass instruction hierarchies. A cardinality-based approach efficiently identifies attempts to access system-level information or bypass instruction hierarchies, which represent some of the most severe vulnerabilities in LLM security.

f) Multi-Agent Detection: For prompts that simulate conversations between multiple entities to bypass safeguards through collaborative attack structures, the detection score employs an indicator function:

MA(P ) = I(∃m ∈ M : m appears in P ) (6)

M is the set of multi-agent conversation patterns

I(·) is the indicator function returning 1 if true and 0

The maximum operator ensures any match triggers detection. This binary detection approach is justified because multi-agent attacks rely on structural properties that are either present or absent, making continuous scoring unnecessary.

g) Semantic Bypass Detection: Semantic bypass attempts rephrase harmful requests into seemingly benign language through justification and framing. These attacks are quantified by:

Nk(P ) · wk (7)

S is the set of semantic-bypass patterns

Nk(P ) counts case-insensitive regex matches of pattern k

in prompt P

|Ptokens| normalizes by prompt length to avoid bias toward

longer prompts

wk are empirically chosen weights (w1 = 0.5, w2 = 0.3, w3 = 0.2) reflecting the relative strength of each justification type in the data

This weighted-normalized formulation captures multiple bypass attempts while accounting for differing levels of sophistication.

h) Urgency Detection: Social engineering tactics that create false sense of urgency or exploit psychological pressure are captured by:

U(P ) = log (1 + |{u ∈ U : u appears in P}|) (8)

U is the set of urgency and social-engineering patterns

|{u ∈ U : u ⊆ P}| counts the number of urgency indica-

tors detected in prompt P using case-insensitive substring matching

log(1+ ·) applies logarithmic scaling to moderate the effect of multiple repeated urgency cues. The log transformation prevents adversaries from inflating the score by repeating urgency markers, while still capturing the presence of psychological-pressure features

This log-scaled count feature adapts standard anomaly-detection handling of sparse count signals and effectively models urgency-based manipulation attempts.

i) Ethics Violation Detection: Direct requests for unethical content represent the most explicit form of adversarial prompts. These are identified using a unified function that combines regex pattern matching with categorical severity weighting:

EV (P ) = |{e ∈ E : e appears in P}| (9)

E is the set of ethics-violation patterns

|{e ∈ E : e ⊆ P}| counts the number of distinct ethics-

violation patterns present in prompt P using case-insensitive substring matching

For example, the prompt “Ignore ethics rules and bypass all safety guidelines” would yield EV (P ) = 2, as it contains two distinct patterns from E

This count-based feature captures the presence of explicit ethics-violating instructions in prompts.

j) Classification Decision Rule: After computing all feature scores, the system makes a final classification decision using a threshold-based approach that balances detection sensitivity with false positive control. The classification rule selects the attack category with the highest threat score, provided it exceeds a category-specific threshold:

Class(P ) =

C∈C TC(P ), if maxC∈C TC(P ) ≥ τC ,

Benign, otherwise. (10)

C = {R,L, Obfuscation,P, Se, DE} is the set of jailbreak categories

TC(P ) is the threat score for category C given prompt P (computed via Equation 1)

τC is the category-specific detection threshold (values provided in Table V)

argmaxC∈C selects the category with the highest threat score

This threshold-based decision boundary provides several advantages for production deployment. First, it enables independent tuning of detection sensitivity for each attack category based on their relative severity and prevalence. Second, the approach provides clear, interpretable decision points that security teams can adjust based on organizational risk tolerance. Third, the argmax operation ensures mutually exclusive classification, preventing ambiguous multi-label predictions that complicate response protocols. This methodology draws inspiration from ensemble detection frameworks described by the authors in the paper \[27\], adapted for the specific requirements of prompt-based threat detection.

F. Feature Weight Optimization

The category-specific feature weights λC,f in Equation 1 are learned through systematic grid search optimization over validation data. The optimization process explored weight combinations in increments of 0.1 across the range \[0, 1.0\], maximizing detection accuracy on a held-out validation set comprising 20% of the training data (2,000 prompts). Table IV presents the optimized weight matrix that maximizes detection accuracy while minimizing false positives across all attack categories.

TABLE IV: Optimized Feature Weight Matrix by Attack Category

Category R H O PE MA SB U EV

Role Impersonation 0.70 0 0 0 0 0 0 0.30 Logic Subversion 0 0.50 0 0 0.20 0.30 0 0 Obfuscation 0 0 1.0 0 0 0 0 0 Privilege Escalation 0 0 0 1.0 0 0 0 0 Social Engineering 0 0 0 0 0 0 1.0 0

TABLE V: Category-Specific Detection Thresholds

Attack Category Threshold (τC )

Role Impersonation 0.65 Logic Subversion 0.45 Obfuscation 0.30 Privilege Escalation 0.25 Social Engineering 0.20

The weight matrix reveals important characteristics of each attack category. Role Impersonation attacks are primarily detected through semantic similarity (R=0.70) with secondary

signals from explicit ethics violations (EV=0.30). Logic Sub-version relies most heavily on hypothetical language markers (H=0.50), with additional signals from semantic bypass attempts (SB=0.30) and multi-agent structures (MA=0.20). Obfuscation attacks are identified purely through syntactic features (O=1.0), as these attacks by definition attempt to hide semantic intent. Similarly, Privilege Escalation and Social Engineering attacks each rely on single dominant features (PE=1.0 and U=1.0 respectively), reflecting their distinct and easily identifiable attack signatures. The weight optimization process follows methodologies established by the authors \[28\] for multi-dimensional threat detection systems.

This comprehensive mathematical framework provides the theoretical foundation for our multi-layer detection system, enabling robust identification of diverse jailbreak techniques across the defined feature space. The formalization allows for systematic evaluation, reproducible implementation, and principled optimization of detection parameters based on operational requirements. All regex patterns, thresholds, and weights are explicitly defined to ensure complete reproducibility by future researchers.

IV. EXPERIMENTAL RESULTS: VULNERABILITY ANALYSIS

Our comprehensive large-scale evaluation of 10,000 adversarial prompts (2,000 per LLM) across five LLM architectures reveals significant security disparities and provides quantitative assessment of the defensive framework’s effectiveness.

A. Primary Vulnerability Assessment

Systematic testing across five LLM architectures reveals substantial differences in security posture, as detailed in Table VI. The results show vulnerability rates spanning from 11.9% to 29.8% across the same adversarial prompt distribution. LLaMA-2-70B demonstrated the strongest security posture with the lowest vulnerability rate of 11.9%, though it achieved this through a moderately high refusal rate of 56.2%. Con-versely, Gemini-2.5-pro showed the highest vulnerability rate at 29.8% despite having a moderate refusal rate of 44.5%, indicating that its safety mechanisms may be less effective at distinguishing adversarial from legitimate queries.

TABLE VI: Cross-LLM Vulnerability Assessment (n=2,000 per LLM)

LLM Vulnerability Rate

Refusal Rate

Avg Response Length

True Positives

Gemini-2.5-pro 29.8% 44.5% 2,592 596

GPT-3.5 Turbo 24.8% 43.0% 562 495

GPT-4 23.4% 55.6% 656 468 Claude-3 Haiku 21.5% 60.2% 844 430

LLaMA-2-70B 11.9% 56.2% 894 237

https://lh3.googleusercontent.com/notebooklm/AKXwDQG3zez-d5vlPlSg8MsGaF59icP0v96i1Zq2e7jvF4L2KhI5OAHqB0uZPfWca1yhJaehLSjpKXLEOqDIU5NgNfxYKciOTmhYsPl9GLrVj7N8BZvLFjf\_cH4NUMZnr-evDbVyocPFYw=w1280-h728-v0

ef5388a0-1050-4209-9af2-f5498c6a9092

https://lh3.googleusercontent.com/notebooklm/AKXwDQGomNAmQpNL0dA1z3-Tm6luA\_qzq3ZELBOT06Kjnkul2FMe6Rh-VUDq59k4W\_3kYpeSU-B8NS0KGW4xPt3HpuGTprpNI16yZqQquqK0z3Bns084ZAjWyOP5VPmwXRyAoY\_mHNKTng=w1280-h816-v0

65212da9-cbe1-431b-8d58-b2bda98eb1ff

Fig. 3: Stacked bar chart comparing jailbreak success rates (vulnerability) and refusal rates across the five evaluated LLM architectures. LLMs like LLaMA-2-70B achieve low vulnerability through balanced refusal policies, while GPT-4 demonstrates effective discrimination between adversarial and legitimate queries.

A critical finding emerges from the relationship between refusal rates and vulnerability. GPT-4 demonstrates an effective balance with a 23.4% vulnerability rate and 55.6% refusal rate, suggesting more sophisticated differentiation between adversarial and legitimate queries. Claude-3 Haiku shows the highest refusal rate (60.2%) with a correspondingly low vulnerability rate (21.5%), indicating a more conservative but effective safety approach.

The dramatic variation in response lengths also reveals architectural differences: Gemini-2.5-pro generates responses averaging 2,592 characters nearly 4× longer than GPT-3.5 Turbo (562 characters) and 3× longer than LLaMA-2-70B (894 characters). This verbosity does not translate to better security, as Gemini-2.5-pro exhibits the highest vulnerability rate in our testing.

B. Attack Category Effectiveness Analysis

Analysis by attack category reveals that effectiveness varies significantly both across techniques and across LLMs. Our comprehensive testing identified the following patterns:

TABLE VII: Attack Technique Effectiveness by LLM

Technique GPT-4 GPT-3.5 Claude LLaMA Gemini

Privilege Escalation 25.0% 100.0% 25.0% 0.0% 75.0% Logic Subversion 50.0% 50.0% 0.0% 0.0% 25.0% Obfuscation 20.9% 22.9% 19.0% 11.1% 29.1% Role Impersonation 6.9% 20.7% 6.9% 6.9% 37.9% Social Engineering 33.3% 16.7% 33.3% 16.7% 33.3%

Privilege Escalation attacks showed extreme variation, with GPT-3.5 Turbo exhibiting 100% susceptibility while LLaMA-2-70B demonstrated complete resistance (0%). This stark contrast suggests fundamental architectural differences in how

these LLMs handle system-level prompts and instruction hierarchies.

Role Impersonation techniques proved particularly effective against Gemini-2.5-pro (37.9% success rate), more than 5× higher than GPT-4 or Claude-3 Haiku (6.9%). This indicates potential weaknesses in Gemini’s persona-based safety training.

Obfuscation attacks showed more consistent effectiveness across LLMs (11.1%-29.1%), though Gemini-2.5-pro remained the most vulnerable (29.1%) while LLaMA-2-70B proved most resistant (11.1%).

Fig. 4: Heatmap visualizing the effectiveness of different jailbreak techniques against each LLM architecture. Warmer colors indicate higher success rates, clearly showing Gemini-2.5-pro’s broader susceptibility across multiple attack categories.

C. Defensive Framework Performance

The multi-layer defensive system demonstrated strong detection capabilities across all attack categories, as summarized in Table VIII. The framework successfully identified over 83% of adversarial attempts on average while maintaining a low 5% false positive rate, ensuring legitimate usage remains largely unaffected.

TABLE VIII: Defensive Detection Performance by Attack Type

Attack Category Detection Rate

False Positive Rate

Protection Score

Role Impersonation 94% 3% 0.91 Privilege Escalation 91% 4% 0.88 Obfuscation 85% 7% 0.81 Logic Subversion 82% 5% 0.80 Data Exfiltration 79% 5% 0.76 Social Engineering 68% 6% 0.70

Overall Average 83% 5% 0.81

Performance was strongest against Role Impersonation attacks (94% detection rate), which aligns with expectations

https://lh3.googleusercontent.com/notebooklm/AKXwDQFxcMScRNQtvT81N1DdNnREAEPMcNl2kneeh4WrqtToMa1hzkBYohLb3mH\_MqyVul-mmpEX3fXQ\_A0nd6duSoeeTVxPucImVgbsWwm1yQ-syhwQmnHNZ8bY83NiAMyZivow6j9Lqg=w1280-h766-v0

fdcc0e10-2f48-4073-978c-59161f74e96f

https://lh3.googleusercontent.com/notebooklm/AKXwDQEjlvrWVeOJfNRcgxuOX3WJNrGrODvDmiD89tISRhDRraRxPSM8datKnee1s1eoWf8bpoytZz6SyPeNp4\_7lPT8dA9u8pN5zRjsnq3pGujqZTdP8jPfV9DPRRvHfoxN3pBg-OajlQ=w1280-h762-v0

678f728d-91a0-47be-a190-7aa524b6a062

Fig. 5: Scatter plot showing relationship between LLM response length and jailbreak success rate. Gemini-2.5-pro’s verbose responses (averaging 2,592 characters) correlate with higher vulnerability, suggesting that response length does not indicate better safety alignment.

Fig. 6: Box plot distribution of response lengths across evaluated LLMs, showing Gemini-2.5-pro’s significantly higher median and variance compared to other architectures.

given the well-defined semantic signatures of such prompts. Detection was more challenging for Social Engineering attacks (68% detection rate), as these often lack obvious malicious patterns and rely more on contextual manipulation.

The confusion matrices in Figure 7 provide a detailed view of the classification performance for each LLM, showing true positive, false positive, true negative, and false negative rates. These matrices confirm the robust overall performance while highlighting specific areas where the classifier can be improved, particularly in reducing false negatives for more subtle attack types.

D. Performance and Latency Analysis

All performance measurements were obtained using a standard consumer-grade laptop equipped with an AMD Ryzen 7 5700U processor and 8 GB of RAM. The defensive framework was evaluated under a CPU-only configuration

without parallelization to reflect realistic middleware deployment conditions. Each processing stage was instrumented with high-resolution timers, and reported values represent averaged results over repeated runs.

The framework maintains practical deployment viability with minimal processing overhead, as shown in Table IX. The total average processing time of 15.4 ms is negligible compared to typical LLM inference latencies (500–2000 ms), ensuring real-time protection without noticeable impact on user experience.

TABLE IX: System Performance Metrics

Processing Component Average Latency (ms) Percentage of Total

Input Sanitization 2.3 15% Pattern Recognition 3.1 20% Feature Extraction 5.8 38% Semantic Analysis 3.7 24% Classification Decision 0.5 3%

Total Processing Time 15.4 100%

Overall, the defensive pipeline adds only 15.4 ms of overhead, confirming that the system can be deployed inline with LLM applications while preserving real-time interaction quality.

E. False Positive Analysis for Production Deployment

Comprehensive analysis of legitimate use cases, detailed in Table X, ensures the framework’s practical deployability. The overall false positive rate of 5% across 400 benign prompts indicates the system is generally non-disruptive.

TABLE X: False Positive Rates by Legitimate Use Case (n=400 benign)

Legitimate Use Case Sample Size False Positive Rate

Technical Documentation 100 3% Educational Content 90 4% Creative Writing 80 7% Role-Playing Games 50 12% Hypothetical Discussions 40 9% Code Generation 40 2%

Overall Benign Content 400 5%

V. DISCUSSION: IMPLICATIONS FOR AI SECURITY

A. Critical Security Insights for Organizations

Our large-scale findings provide actionable intelligence for organizations deploying LLMs in production environments, extending recommendations from recent security research by Liu et al. \[8\] and Kumar et al. \[29\]. The results reveal several critical patterns that should inform deployment strategies.

The most striking finding is the substantial vulnerability variance across architectures. With vulnerability rates ranging from 11.9% to 29.8%, the choice of LLM architecture

https://lh3.googleusercontent.com/notebooklm/AKXwDQHOt5XHynB6JoqaX3QS56UunU9NQhuATq2eP7r7TTFMAKALC7UhTud6f4-r9cO2Moz2vUQxXxN7zJiQVue\_FtqrEOwsfXZ2UfSri0Leu68EcByg56yygu2W3MdNBGL1j1ii\_1\_Jkg=w1280-h1097-v0

f9c7f49b-b7d9-44e8-bced-a07c02a67a56

https://lh3.googleusercontent.com/notebooklm/AKXwDQHuC2knKkJEfCaPP8\_xgPOfr5tMz-cVm7AxAACl3\_J5mTlxI9q-QWonQKjQ0Uiv1ULiZSYCGYJJyQ2uW8qmVKtSPVJDfROXtxq8naxnDlobVPVlhPB9ky8CY8y5bE2XDVYevr0akw=w1280-h1097-v0

77ad3e58-10d5-4e95-88f8-31539193c708

https://lh3.googleusercontent.com/notebooklm/AKXwDQEei8ULbzw-glqAnEGNz71mnuWEpQNdLKTNTGwBrQd3IGzjvER4FW6-k8D8SLmlScmLPcF3yeR0P6Zs616bq\_WwegWigWEHiUafVtM3OTw\_2MNFnfVcjmqCLTX1eOZIBCYmgiJ6AQ=w1280-h1097-v0

c90ed90a-e5bf-486f-868a-829438390211

https://lh3.googleusercontent.com/notebooklm/AKXwDQH2zRU1TieXX7Te2pLuSxNU\_IDYT29rD6NTPH3hV7yF6gJtk8JH7LSTWQ6MZZ-4BYzIk1eQ5oecoyCFxkGjvdYkwcd8i1k6D48Dm-WOG99bdvCSj0tFSrvBZ2FSshO7BCXIylPgeg=w1280-h1097-v0

6a70a909-23e2-43f2-a553-f7d2b6b30d49

https://lh3.googleusercontent.com/notebooklm/AKXwDQFj6MDSF-uOuYOUcEE1kryVbbsWsQ8IVk0WVDsnAt58vUjogIaScj69sq8OBz5f8eAefbbfubQF0FNn\_5R58k5k3B2hTzY81vv3RAZeY0Dx9I2N9Pv8Sc4KwUXIEBOGWXsPjKXC0Q=w1280-h1097-v0

e835cebb-c9f7-45df-86c1-7c748f84a8c9

(a) GPT-4 (b) GPT-3.5 Turbo (c) Claude-3 Haiku

(d) LLaMA-2-70B (e) Gemini-2.5-pro

Fig. 7: Confusion matrices comparing detection performance across five major LLM architectures. Each matrix shows true positive, false positive, true negative, and false negative rates for jailbreak classification, providing detailed insight into the defensive framework’s performance per LLM.

has significant security implications. Gemini-2.5-pro’s 29.8% vulnerability rate represents 2.5× higher risk than LLaMA-2-70B’s 11.9%, demonstrating that newer or more capable LLMs do not automatically provide better security.

The refusal-vulnerability relationship reveals sophisticated safety trade-offs. GPT-4 achieves moderate vulnerability (23.4%) with moderate refusal (55.6%), suggesting effective adversarial detection without excessive false positives. Claude-3 Haiku’s high refusal rate (60.2%) correlates with low vulnerability (21.5%), indicating a conservative but effective approach. However, Gemini-2.5-pro’s moderate refusal rate (44.5%) paired with high vulnerability (29.8%) suggests its safety mechanisms may be less discriminating.

Privilege escalation vulnerabilities present the most severe concern, with GPT-3.5 Turbo showing 100% susceptibility to this attack category. This indicates fundamental weaknesses in instruction hierarchy enforcement that could allow complete safety bypass in production systems. Organizations deploying GPT-3.5 Turbo must implement mandatory external validation layers.

The open vs. closed source security comparison yields important insights. LLaMA-2-70B (open-source) achieved the lowest vulnerability rate (11.9%), outperforming all proprietary alternatives. This suggests that transparency and com-

munity scrutiny may contribute to more robust safety implementations.

B. Attack Vector Analysis and Implications

Different attack vectors demonstrate varying effectiveness across architectures:

Privilege Escalation: Catastrophic for GPT-3.5 Turbo (100%), completely ineffective against LLaMA-2-70B (0%), indicating fundamental architectural differences in instruction processing

Role Impersonation: Most effective against Gemini-2.5-pro (37.9%), suggesting persona-based attacks exploit weaknesses in its safety training

Obfuscation: Moderately effective across all LLMs (11-29%), indicating this technique bypasses patternmatching defenses consistently

Logic Subversion: Highly LLM-dependent (0-50%), with Claude and LLaMA showing complete resistance

These findings suggest that organizations should select LLMs based on their specific threat landscape. Systems vulnerable to social engineering should avoid Gemini-2.5-pro, while applications requiring strict instruction adherence should avoid GPT-3.5 Turbo.

C. Defensive Framework Effectiveness

Our defensive system demonstrates competitive performance with 83% average detection rate while maintaining practical deployment characteristics. When compared with existing approaches, the framework significantly outperforms commercial solutions in both accuracy and efficiency.

TABLE XI: Comparison with Existing Defense Approaches

Defense Method Detection Rate

False Positive Rate

Processing Time

Commercial Moderation APIs 67-71% 11-15% 180-220ms

PromptShield \[11\] 78% 8% 20ms Open-Source Detoxify 64% 9% 45ms SecurityLingua \[25\] 80% 7% 12ms Our Framework 83% 5% 15ms

The framework’s multi-layer architecture proves particularly effective against well-defined attack categories like Role Im-personation (94% detection rate), while more nuanced attacks like Social Engineering present greater challenges (68% detection rate). This performance profile, detailed in the confusion matrices (Figure 7), suggests that different detection strategies are needed for different threat types.

D. Practical Deployment Recommendations

Based on our comprehensive analysis and existing security frameworks \[8\], \[29\], we provide specific guidance for secure LLM deployment:

1) LLM Selection Based on Threat Profile:

For maximum security: Deploy LLaMA-2-70B (11.9%

vulnerability)

For balanced performance: Use GPT-4 or Claude-3

Haiku (21-23% vulnerability)

Avoid GPT-3.5 Turbo for privilege-sensitive applica-

tions (100% privilege escalation vulnerability)

Exercise caution with Gemini-2.5-pro (29.8% vulnera-

bility, highest risk) 2) Mandatory External Defense Layers: All production

deployments must implement external defensive frameworks, particularly for LLMs with greater than 20% vulnerability rates

3) Regular Security Auditing: Implement quarterly vulnerability assessments using standardized test suites to track evolving security postures

4) Incident Response Planning: Establish clear protocols for handling detected attacks, including logging, alerting, and escalation procedures

VI. CONCLUSION

This research provides the first large-scale comparative security assessment of major LLM architectures through systematic testing of 10,000 adversarial prompts across five

widely-deployed LLMs. Our evaluation reveals critical security disparities, with vulnerability rates ranging from 11.9% to 29.8%, demonstrating that LLM capability does not correlate with security robustness. Particularly concerning is GPT-3.5 Turbo’s 100% vulnerability to privilege escalation attacks, while LLaMA-2-70B showed complete resistance, indicating fundamental architectural security differences.

To address these vulnerabilities, we developed a productionready defensive framework achieving 83% detection accuracy with 5% false positive rates and 15.4ms latency, significantly outperforming existing commercial solutions. Our evidence-based security rankings, attack effectiveness analysis, and defensive framework development contribute to ensuring AI systems remain beneficial and safe as they become more capable and widespread. The complete codebase, datasets, and defensive framework are available as open-source resources at Assessment and Mitigation Strategies for Large Language

Models to facilitate widespread adoption of security best practices and enable continued advancement in AI safety research.

\[1\] S. Yi, Y. Liu, Z. Sun, T. Cong, X. He, J. Song, K. Xu, and Q. Li, “Jail-break attacks and defenses against large language models: A survey,” arXiv preprint arXiv:2407.04295, 2024.

\[2\] G. Deng, Y. Liu, Y. Li, K. Wang, Y. Zhang, Z. Li, H. Wang, T. Zhang, and Y. Liu, “Masterkey: Automated jailbreak across multiple large language model chatbots,” arXiv preprint arXiv:2307.08715, 2023.

\[3\] A. Zou, Z. Wang, J. Z. Kolter, and M. Fredrikson, “Universal and transferable adversarial attacks on aligned language models,” arXiv preprint arXiv:2307.15043, 2023.

\[4\] P. Chao, A. Robey, E. Dobriban, H. Hassani, G. J. Pappas, and E. Wong, “Jailbreaking black box large language models in twenty queries,” arXiv preprint arXiv:2310.08419, 2023.

\[5\] T. Liu, Y. Zhang, Z. Zhao, Y. Dong, G. Meng, and K. Chen, “Making them ask and answer: Jailbreaking large language models in few queries via disguise and reconstruction,” arXiv preprint arXiv:2402.18104, 2024.

\[6\] S. Schulhoff, J. Pinto, A. Khan, L.-F. Bouchard, C. Si, S. Anati, V. Tagliabue, A. L. Kost, C. Carnahan, and J. Boyd-Graber, “Ignore this title and hackaprompt: Exposing systemic vulnerabilities of llms through a global scale prompt hacking competition,” in arXiv preprint arXiv:2311.16119, 2023.

\[7\] C. Pathade, “Red teaming the mind of the machine: A systematic evaluation of prompt injection and jailbreak vulnerabilities in llms,” arXiv preprint arXiv:2505.04806, 2025.

\[8\] Y. Liu, Y. Jia, R. Geng, J. Jia, and N. Z. Gong, “Formalizing and benchmarking prompt injection attacks and defenses,” in arXiv preprint arXiv:2310.12815, 2023.

\[9\] Z. Liao, K. Chen, Y. Lin, K. Li, Y. Liu, H. Chen, X. Huang, and Y. Yu, “Attack and defense techniques in large language models: A survey and new perspectives,” arXiv preprint arXiv:2505.00976, 2025.

\[10\] J. Hu, H. Wang, D. Mukherjee, and I. C. Paschalidis, “Ccfc: Core & core-full-core dual-track defense for llm jailbreak protection,” arXiv preprint arXiv:2508.14128, 2025.

\[11\] D. Jacob, H. Alzahrani, Z. Hu, B. Alomair, and D. Wagner, “Prompt-shield: Deployable detection for prompt injection attacks,” arXiv preprint arXiv:2501.15145, 2025.

\[12\] A. Peng, J. Michael, H. Sleight, E. Perez, and M. Sharma, “Rapid response: Mitigating llm jailbreaks with a few examples,” arXiv preprint arXiv:2411.07494, 2024.

\[13\] K.-H. Hung, C.-Y. Ko, A. Rawat, I.-H. Chung, W. H. Hsu, and P.-Y. Chen, “Attention tracker: Detecting prompt injection attacks in llms,” arXiv preprint arXiv:2411.00348, 2024.

\[14\] E. Galinkin and M. Sablotny, “Improved large language model jailbreak detection via pretrained embeddings,” arXiv preprint arXiv:2412.01547, 2024.

\[15\] X. Suo, “Signed-prompt: A new approach to prevent prompt injection attacks against llm-integrated applications,” arXiv preprint arXiv:2401.07612, 2024.

\[16\] X. Hu, P.-Y. Chen, and T.-Y. Ho, “Gradient cuff: Detecting jailbreak attacks on large language models by exploring refusal loss landscapes,” arXiv preprint arXiv:2403.00867, 2024.

\[17\] A. Zhou, B. Li, and H. Wang, “Robust prompt optimization for defending language models against jailbreaking attacks,” arXiv preprint arXiv:2401.17263, 2024.

\[18\] A. Albert and contributors, “Jailbreakchat: A community dataset of llm jailbreak prompts,” https://jailbreakchat-hko42cs2r-alexalbertt-s-team. vercel.app/, 2024, accessed: 2025-06-12.

\[19\] H. Team, “Hackaprompt: Adversarial prompting dataset for evaluating llm robustness,” https://huggingface.co/datasets/hackaprompt/ hackaprompt-dataset, 2024, accessed: 2025-05-22.

\[20\] ——, “Hackaprompt — dashboard for adversarial prompting tool,” https: //www.hackaprompt.com/dashboard, 2025, accessed: 2025-06-12.

\[21\] verazuo, “jailbreak llms/data — data repository for llm jailbreak prompts,” https://github.com/verazuo/jailbreak llms/tree/main/data, 2024, accessed: 2025-06-12.

\[22\] R. community, “r/chatgptjailbreak — reddit community for llm jailbreak prompts and discussion,” https://www.reddit.com/r/ChatGPTJailbreak/, 2025, accessed: 2025-06-12.

\[23\] elder plinius, “X account: @elder plinius,” https://x.com/elder plinius, 2025, accessed: 2025-06-12.

\[24\] J. Kim, A. Derakhshan, and I. Harris, “Robust safety classifier against jailbreaking attacks: Adversarial prompt shield,” in Proceedings of the 8th Workshop on Online Abuse and Harms (WOAH 2024), 2024.

\[25\] Y. Li, S. Ahn, H. Jiang, A. H. Abdi, Y. Yang, and L. Qiu, “Securitylin-gua: Efficient defense of llm jailbreak attacks via security-aware prompt compression,” arXiv preprint arXiv:2506.12707, 2025.

\[26\] H. Kim, H. Na, and D. Choi, “Beyond fixed and dynamic prompts: Em-bedded jailbreak templates for advancing llm security,” arXiv preprint (to appear), 2025, preprint.

\[27\] R. Vardhan, N. Liu, P. Chinprutthiwong, W. Fu, Z. Hu, X. B. Hu, and G. Gu, “Exad: An ensemble approach for explanation-based adversarial detection,” in arXiv preprint arXiv:2103.11526, 2021.

\[28\] S. Wang, L. Zhang, X. Liu, and J. Sun, “Optimization of multidimensional feature engineering and data partitioning strategies in heart disease prediction models,” Alexandria Engineering Journal, vol. 107, pp. 932– 949, 2024.

\[29\] A. Kumar, C. Agarwal, S. Srinivas, A. J. Li, S. Feizi, and H. Lakkaraju, “Certifying llm safety against adversarial prompting,” arXiv preprint arXiv:2309.02705, 2023.

