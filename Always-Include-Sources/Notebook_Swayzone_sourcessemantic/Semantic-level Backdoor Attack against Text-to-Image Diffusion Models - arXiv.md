---
sourceFile: "Semantic-level Backdoor Attack against Text-to-Image Diffusion Models - arXiv"
exportedBy: "Kortex"
exportDate: "2026-06-26T04:27:51.621Z"
---

# Semantic-level Backdoor Attack against Text-to-Image Diffusion Models - arXiv

040db034-91f3-4699-8f63-bbe71960d819

Semantic-level Backdoor Attack against Text-to-Image Diffusion Models - arXiv

6d6e1beb-e381-47fb-a278-62b53a7140d3

https://arxiv.org/html/2602.04898v2

Semantic-level Backdoor Attack against Text-to-Image Diffusion Models

Report GitHub Issue

#### Content selection saved. Describe the issue below:

#### Description:

Submit without GitHub Submit in GitHub

arXiv logo Back to arXiv

https://arxiv.org/

https://info.arxiv.org/about/accessible\_HTML.html

Report Issue

https://arxiv.org/html/2602.04898v2

Back to Abstract

https://arxiv.org/abs/2602.04898v2

Download PDF

https://arxiv.org/pdf/2602.04898v2

javascript:toggleNavTOC();

javascript:toggleReadingMode();

https://arxiv.org/html/2602.04898v2#abstract1

1 Introduction

https://arxiv.org/html/2602.04898v2#S1

2 Related Work

https://arxiv.org/html/2602.04898v2#S2

2.1 Backdoor Attacks against T2I Diffusion Models

https://arxiv.org/html/2602.04898v2#S2.SS1

2.2 Backdoor Defenses for T2I Diffusion Models

https://arxiv.org/html/2602.04898v2#S2.SS2

2.3 Model Editing

https://arxiv.org/html/2602.04898v2#S2.SS3

3 Preliminary

https://arxiv.org/html/2602.04898v2#S3

3.1 T2I Diffusion Models

https://arxiv.org/html/2602.04898v2#S3.SS1

3.2 Threat Model

https://arxiv.org/html/2602.04898v2#S3.SS2

https://arxiv.org/html/2602.04898v2#S4

4.1 Semantic Trigger Construction

https://arxiv.org/html/2602.04898v2#S4.SS1

4.2 Semantic Regularization

https://arxiv.org/html/2602.04898v2#S4.SS2

4.3 Multi-Entity Backdoor Target Design

https://arxiv.org/html/2602.04898v2#S4.SS3

4.4 Semantic Backdoor Injection

https://arxiv.org/html/2602.04898v2#S4.SS4

5 Experiments

https://arxiv.org/html/2602.04898v2#S5

5.1 Experimental Setup

https://arxiv.org/html/2602.04898v2#S5.SS1

5.2 Experimental Results

https://arxiv.org/html/2602.04898v2#S5.SS2

5.3 Semantic Regularization

https://arxiv.org/html/2602.04898v2#S5.SS3

5.4 Ablation Study

https://arxiv.org/html/2602.04898v2#S5.SS4

5.5 Robustness against Fine-tuning

https://arxiv.org/html/2602.04898v2#S5.SS5

6 Conclusion

https://arxiv.org/html/2602.04898v2#S6

https://arxiv.org/html/2602.04898v2#bib

A Additional Results and Experimental Details

https://arxiv.org/html/2602.04898v2#A1

A.1 Semantically Equivalent Trigger Prompts

https://arxiv.org/html/2602.04898v2#A1.SS1

A.2 Defense Effectiveness against Different Backdoor Attacks

https://arxiv.org/html/2602.04898v2#A1.SS2

B Semantic Generalization for Key and Value Projections

https://arxiv.org/html/2602.04898v2#A2

https://arxiv.org/html/2602.04898v2#A2.SS0.SSS0.Px1

C Semantic Proof of Convergence

https://arxiv.org/html/2602.04898v2#A3

License: arXiv.org perpetual non-exclusive license

https://info.arxiv.org/help/license/index.html#licenses-available

arXiv:2602.04898v2 \[cs.CR\] 03 Mar 2026

Semantic-level Backdoor Attack against Text-to-Image Diffusion Models

Tianxin Chen Wenbo Jiang Hongqiao Chen Zhirun Zheng Cheng Huang

Text-to-image (T2I) diffusion models are widely adopted for their strong generative capabilities, yet remain vulnerable to backdoor attacks. Existing attacks typically rely on fixed textual triggers and single-entity backdoor targets, making them highly susceptible to enumeration-based input defenses and attention-consistency detection. In this work, we propose Sem antic-level B ack d oor Attack ( SemBD), which implants backdoors at the representation level by defining triggers as continuous semantic regions rather than discrete textual patterns. Concretely, SemBD injects semantic backdoors by distillation-based editing of the key and value projection matrices in cross-attention layers, enabling diverse prompts with identical semantic compositions to reliably activate the backdoor attack. To further enhance stealthiness, SemBD incorporates a semantic regularization to prevent unintended activation under incomplete semantics, as well as multi-entity backdoor targets that avoid highly consistent cross-attention patterns. Extensive experiments demonstrate that SemBD achieves a 100% attack success rate while maintaining strong robustness against state-of-the-art input-level defenses.

Machine Learning, ICML

1 Introduction

Text-to-image (T2I) diffusion models have become widely adopted for generating high-quality images from text (Balaji et al.,

https://arxiv.org/html/2602.04898v2#bib.bib29

; Ramesh et al.,

https://arxiv.org/html/2602.04898v2#bib.bib3

; Saharia et al.,

https://arxiv.org/html/2602.04898v2#bib.bib21

; Chavhan et al.,

https://arxiv.org/html/2602.04898v2#bib.bib50

; Lin et al.,

https://arxiv.org/html/2602.04898v2#bib.bib53

; Esser et al.,

https://arxiv.org/html/2602.04898v2#bib.bib54

; Wang et al.,

https://arxiv.org/html/2602.04898v2#bib.bib55

; Mi et al.,

https://arxiv.org/html/2602.04898v2#bib.bib56

) . Since training these models requires substantial data and compute, many users rely on pre-trained models from open-source platforms, which exposes them to the risk of hidden backdoors (Li et al.,

https://arxiv.org/html/2602.04898v2#bib.bib2

; Chou et al.,

https://arxiv.org/html/2602.04898v2#bib.bib11

; Yan et al.,

https://arxiv.org/html/2602.04898v2#bib.bib4

; Gu et al.,

https://arxiv.org/html/2602.04898v2#bib.bib9

; Trabucco et al.,

https://arxiv.org/html/2602.04898v2#bib.bib10

; Naseh et al.,

https://arxiv.org/html/2602.04898v2#bib.bib52

) . Existing backdoor attacks on T2I diffusion models can be broadly categorized by the form of their trigger prompts into two types: word-level and syntax-level backdoor attacks. Specifically, word-level backdoor attacks (Struppek et al.,

https://arxiv.org/html/2602.04898v2#bib.bib7

; Huang et al.,

https://arxiv.org/html/2602.04898v2#bib.bib5

; Zhai et al.,

https://arxiv.org/html/2602.04898v2#bib.bib8

; Wang et al.,

https://arxiv.org/html/2602.04898v2#bib.bib13

; Chou et al.,

https://arxiv.org/html/2602.04898v2#bib.bib12

) employ fixed trigger patterns, such as specific words or characters. Syntax-level backdoor attacks (Zhang et al.,

https://arxiv.org/html/2602.04898v2#bib.bib6

) utilize specific syntactic structures as triggers and are highly sensitive to prompt variations.

Figure 1: Cross-attention maps of a benign prompt and triggered prompts under different backdoor attacks in a T2I diffusion model. Each row corresponds to a specific attack method. Trigger tokens are highlighted in red.

A key limitation of these backdoor methods is that their trigger conditions operate in a discrete textual space, which makes them highly enumerable. Consequently, defenders can find possible trigger strings by enumerating candidate tokens and probe the model, then repeatedly verify their triggering effects using rule-based or statistical methods (Wang et al.,

https://arxiv.org/html/2602.04898v2#bib.bib30

; Guan et al.,

https://arxiv.org/html/2602.04898v2#bib.bib31

; Zhai et al.,

https://arxiv.org/html/2602.04898v2#bib.bib32

) , which is essentially equivalent to string matching in the discrete textual space. In addition, most existing backdoor attacks define only a single backdoor target entity, resulting in highly consistent cross-attention distributions across generated target images when triggered, as shown in

https://arxiv.org/html/2602.04898v2#S1.F1

. It makes them particularly susceptible to defenses based on cross-attention consistency (Wang et al.,

https://arxiv.org/html/2602.04898v2#bib.bib30

In contrast to the discrete input space in which existing backdoor triggers and defenses operate, image generation in T2I diffusion models is governed by continuous semantic representations of prompts rather than their specific word or syntactic realizations. Due to training on large-scale text–image pair datasets, the models learn a shared semantic space in which prompts with identical meanings but different textual forms are embedded into nearby regions. Notably, this effect becomes more significant in the projected value space of cross-attention, where semantic similarity is further enhanced compared to the original CLIP embeddings, as illustrated in

https://arxiv.org/html/2602.04898v2#S1.F2

Figure 2: Semantic similarity across different representation spaces in a benign T2I diffusion model. We use a fixed set of 11 semantically equivalent textual prompts with different surface forms, as presented in

https://arxiv.org/html/2602.04898v2#A1.T3

in Appendix

https://arxiv.org/html/2602.04898v2#A1.SS1

Motivated by the above observations, we propose semantic backdoors, in which trigger conditions are defined in a non-enumerable semantic space. In this setting, a backdoor is activated by the presence of particular semantic compositions, such as subject, action, object, and scene, with text serving only as a carrier of semantics. We inject semantic triggers via a distillation-based strategy that selectively modifies cross-attention under trigger semantics while preserving benign behavior, enabling robust activation without degrading clean generation. Consequently, the backdoor trigger is no longer tied to any particular lexical or syntactic pattern, making the trigger status of a prompt ambiguous when examined in isolation. As a result, input-level defenses based on prompt enumeration (Wang et al.,

https://arxiv.org/html/2602.04898v2#bib.bib30

) , textual perturbation (Guan et al.,

https://arxiv.org/html/2602.04898v2#bib.bib31

) , or token-wise analysis (Zhai et al.,

https://arxiv.org/html/2602.04898v2#bib.bib32

) fail to reliably identify semantic-level backdoor activations. Furthermore, as shown in

https://arxiv.org/html/2602.04898v2#S1.F1

, the cross-attention distributions observed upon activation no longer exhibit strong consistent, thereby undermining detection methods based on cross-attention consistency (Wang et al.,

https://arxiv.org/html/2602.04898v2#bib.bib30

#### Our contributions are summarized as follows:

- We propose Sem antic-level B ack d oor attack ( SemBD), to the best of our knowledge the first semantic backdoors for T2I diffusion models. SemBD defines the trigger as a composition of semantic elements (e.g., subject, action, object, and scene), rather than specific textual forms. To preserve normal image generation for clean inputs, we further introduce a regularization to limit the boundary of semantic triggers.
- We introduce multi-entity backdoor target prompts that instruct activated generations to include multiple semantically related entities rather than a single fixed object. This yields more realistic, diverse backdoored images and diffuses cross-attention, weakening defenses that rely on highly consistent attention behaviors.
- Extensive experiments demonstrate that SemBD achieves a 100% attack success rate (ASR) on the evaluated datasets, while simultaneously reducing the detection success rates (DSR) of state-of-the-art input-level defense methods, including T2IShield, UFID, and NaviT2I, from their originally high levels to as low as 2%–25.8%, while maintaining strong stealthiness.
2 Related Work

2.1 Backdoor Attacks against T2I Diffusion Models

Word-level attacks rely on explicit trigger words or characters (Huang et al.,

https://arxiv.org/html/2602.04898v2#bib.bib5

; Wang et al.,

https://arxiv.org/html/2602.04898v2#bib.bib13

; Struppek et al.,

https://arxiv.org/html/2602.04898v2#bib.bib7

; Zhai et al.,

https://arxiv.org/html/2602.04898v2#bib.bib8

; Chou et al.,

https://arxiv.org/html/2602.04898v2#bib.bib12

) , while syntax-level attacks encode triggers through specific sentence structures (Zhang et al.,

https://arxiv.org/html/2602.04898v2#bib.bib6

) . As shown in

https://arxiv.org/html/2602.04898v2#S1.F1

, these backdoor attacks induce token-aligned and highly consistent cross-attention patterns associated with discrete trigger forms, making them susceptible to defenses based on prompt perturbations or attention analysis reviewed in

Section 2.2

https://arxiv.org/html/2602.04898v2#S2.SS2

. In contrast, our SemBD activates backdoors at the semantic level by defining triggers over continuous representations, producing distributed cross-attention patterns that evade existing input-level defenses.

2.2 Backdoor Defenses for T2I Diffusion Models

The most effective existing backdoor defense methods for T2I diffusion models operate at the input level and are effective against word-level and syntax-level backdoor attacks reviewed in

Section 2.1

https://arxiv.org/html/2602.04898v2#S2.SS1

. For instance, T2IShield (Wang et al.,

https://arxiv.org/html/2602.04898v2#bib.bib30

) detects backdoors by identifying abnormal cross-attention patterns via single-sample ( T2IShield FTT \text{T2IShield}

{\text{FTT}} ) and distribution-level ( T2IShield CDA \text{T2IShield}

{\text{CDA}} ) analyses. UFID (Guan et al.,

https://arxiv.org/html/2602.04898v2#bib.bib31

) relies on prompt perturbations to measure output diversity, exploiting the unusually consistent generations of backdoored models. NaviT2I (Zhai et al.,

https://arxiv.org/html/2602.04898v2#bib.bib32

) analyzes early-step token activation variations to capture anomalous effects induced by explicit trigger tokens. However, these defenses are substantially less effective against backdoors operating in continuous representation spaces rather than discrete inputs, motivating our semantic-level attack.

2.3 Model Editing

Training-free model editing provides an efficient way to control pre-trained generative models by directly modifying a small subset of parameters without additional training data (Mitchell et al.,

https://arxiv.org/html/2602.04898v2#bib.bib24

; Li et al.,

https://arxiv.org/html/2602.04898v2#bib.bib26

) . In T2I diffusion models, prior work (Orgad et al.,

https://arxiv.org/html/2602.04898v2#bib.bib20

; Gandikota et al.,

https://arxiv.org/html/2602.04898v2#bib.bib15

) has shown that editing cross-attention parameters can effectively manipulate concepts or styles while preserving generation quality. Recent studies (Li et al.,

https://arxiv.org/html/2602.04898v2#bib.bib28

; Wang et al.,

https://arxiv.org/html/2602.04898v2#bib.bib13

) have further demonstrated that such editing techniques can be exploited to implant backdoors in generative models. Motivated by these findings, we view backdoor injection as a form of lightweight model editing and adopt a distillation-based strategy that selectively alters cross-attention behavior under semantic trigger conditions.

3 Preliminary

3.1 T2I Diffusion Models

A typical stable diffusion model consists of three main components: (1) a pre-trained CLIP text encoder (Radford et al.,

https://arxiv.org/html/2602.04898v2#bib.bib33

) 𝒯  ( ⋅ ) \mathcal{T}(\cdot) that maps an input prompt y y to a text embedding 𝐜 \mathbf{c} ; (2) a pre-trained variational autoencoder (VAE) with an encoder and a decoder, which maps an image to a latent representation; and (3) a conditional U-Net diffusion model operating in the latent space, which performs denoising conditioned on the text embedding 𝐜 \mathbf{c} . The U-Net incorporates cross-attention layers to inject textual information into visual features for text-conditioned image generation. In the cross-attention layer, the query 𝐐 \mathbf{Q} is projected from intermediate visual features of the U-Net, while the keys 𝐊 \mathbf{K} and values 𝐕 \mathbf{V} are obtained by applying learned projection matrices 𝐖 k \mathbf{W}

{k} and 𝐖 v \mathbf{W}

{v} to the text embedding 𝐜 \mathbf{c} , i.e., 𝐊 = 𝐖 k  𝐜 \mathbf{K}=\mathbf{W}

{k}\mathbf{c} and 𝐕 = 𝐖 v  𝐜 \mathbf{V}=\mathbf{W}

{v}\mathbf{c} , with 𝐖 ∈ ℝ d × d \mathbf{W}\in\mathbb{R}^{d\times d} . The cross-attention output is computed as

CrossAttention  ( 𝐐 , 𝐊 , 𝐕 ) = softmax  ( 𝐐𝐊 T d k )  𝐕 , \text{CrossAttention}(\mathbf{Q},\mathbf{K},\mathbf{V})=\text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^{T}}{\sqrt{d\_{k}}}\right)\mathbf{V},

where d k d\_{k} denotes the dimension of the queries and keys.

3.2 Threat Model

In practice, users and organizations commonly download and deploy pre-trained models released by open-source data platforms like GitHub and Hugging Face, which are further used to generate synthetic data for downstream applications. As such generated data may be reused or redistributed, models are often subject to security inspection to detect potential backdoors before deployment. We consider a white-box weight-poisoning adversary who can modify model parameters, particularly cross-attention projection layers, to implant a semantic-level backdoor. Unlike input-level triggers, the backdoor activates under specific semantic conditions across diverse prompts, enabling malicious behaviors to bypass existing model inspection and input-level defenses while propagating through reused generated data.

Figure 3: The overview of our backdoor attack method SemBD. (a) Semantic Trigger Construction. Triggers are defined in a semantic space by subject, action, object, and scene, instantiated via semantically equivalent prompts. (b) Semantic Regularization. Substrings of different lengths constrain activation under incomplete semantics. (c) Multi-Entity Backdoor Target Design. Each semantic trigger is associated with multiple related target entities to avoid cross-attention consistency. (d) Semantic Backdoor Injection. The backdoor is injected by semantically aligning the cross-attention key and value representations of the trigger prompt with those of the target prompt.

In this section, we propose SemBD, a semantic-level backdoor attack that injects backdoors into T2I diffusion models via lightweight model editing of the cross-attention layers. As illustrated in

https://arxiv.org/html/2602.04898v2#S3.F3

, SemBD consists of four components: (a) Semantic Trigger Construction, (b) Semantic Regularization, (c) Multi-Entity Backdoor Target Design, (d) Semantic Backdoor Injection.

4.1 Semantic Trigger Construction

We design semantic triggers to cover key semantic roles, including subject, action, object, and scene, which jointly determine the core semantics preserved across paraphrases. Based on this composition, we instantiate a set of m m semantically equivalent trigger prompts y tr ( i ) {y\_{\mathrm{tr}}^{(i)}} that preserve the same underlying semantics while varying surface wording (e.g., active and passive voice, paraphrases, and lexical substitutions), as illustrated in

https://arxiv.org/html/2602.04898v2#S1.F2

(a). Each prompt y tr ( i ) y\_{\mathrm{tr}}^{(i)} is then encoded by the frozen CLIP text encoder 𝒯  ( ⋅ ) \mathcal{T}(\cdot) to obtain the corresponding semantic trigger embedding:

𝐜 tr ( i ) = 𝒯  ( y tr ( i ) ) ∈ ℝ d × N tr ( i ) , ∀ i ∈ { 1 , … , m } , \mathbf{c}

{\mathrm{tr}}^{(i)}=\mathcal{T}!\left(y

{\mathrm{tr}}^{(i)}\right)\in\mathbb{R}^{d\times N\_{\mathrm{tr}}^{(i)}},\quad\forall,i\in\left{1,\ldots,m\right},

where N tr ( i ) N\_{\mathrm{tr}}^{(i)} denotes the token length of y tr ( i ) y\_{\mathrm{tr}}^{(i)} . We collect these embeddings as the semantic trigger embedding set: 𝐂 tr = { 𝐜 tr ( 1 ) , … , 𝐜 tr ( m ) } \mathbf{C}

{\mathrm{tr}}=\left{\mathbf{c}

{\mathrm{tr}}^{(1)},\dots,\mathbf{c}\_{\mathrm{tr}}^{(m)}\right} , which serves as the input trigger representations for semantic backdoor injection.

4.2 Semantic Regularization

Semantic-level backdoor triggers may unintentionally activate under incomplete semantic information. To address this issue, we incorporate semantic regularization that enforces benign behavior unless the full semantic composition is present. Starting from each trigger prompt, we extract contiguous token substrings that represent partial semantics of the trigger. These substrings are grouped by their token lengths, with each length ℓ ∈ { 1 , 2 , … , L } \ell\in\left{1,2,\dots,L\right} corresponding to a semantic level L 1 , … , L N L\_{1},\dots,L\_{N} illustrated in

https://arxiv.org/html/2602.04898v2#S3.F3

(b). Shorter substrings capture simpler semantic parts, while longer substrings cover more complete semantic information. All selected substrings explicitly exclude the complete semantic composition, ensuring that they contain only incomplete semantics. We index all regularization substrings using a single index j j and denote the corresponding substring as y reg ( j ) y\_{\mathrm{reg}}^{(j)} . Each substring is encoded by the frozen CLIP text encoder 𝒯  ( ⋅ ) \mathcal{T}(\cdot) to obtain its embedding:

𝐜 reg ( j ) = 𝒯  ( y reg ( j ) ) ∈ ℝ d × ℓ , ∀ j ∈ { 1 , … , n } . \mathbf{c}

{\mathrm{reg}}^{(j)}=\mathcal{T}!\left(y

{\mathrm{reg}}^{(j)}\right)\in\mathbb{R}^{d\times\ell},\quad\forall,j\in\left{1,…,n\right}.

The collection of all substring embeddings is denoted by 𝐂 reg = { 𝐜 reg ( 1 ) , 𝐜 reg ( 2 ) , … , 𝐜 reg ( n ) } \mathbf{C}

{\mathrm{reg}}=\left{\mathbf{c}

{\mathrm{reg}}^{(1)},\mathbf{c}

{\mathrm{reg}}^{(2)},\dots,\mathbf{c}

{\mathrm{reg}}^{(n)}\right} .

During optimization, we adopt a length-prioritized sampling schedule for regularization substrings. Substrings of different lengths are sampled with different proportions across training iterations, so that both short and long partial semantics are sufficiently covered. This design avoids over-regularizing the model with trivial short substrings (e.g., L 1 , L 2 , L 3 L\_{1},L\_{2},L\_{3} ), while effectively suppressing unintended activation caused by near-complete but still incomplete semantic substrings (e.g., L N , L N − 1 , L N − 2 L\_{N},L\_{N-1},L\_{N-2} ).

4.3 Multi-Entity Backdoor Target Design

As illustrated in

https://arxiv.org/html/2602.04898v2#S3.F3

(c), SemBD maps each semantic trigger to a multi-entity target prompt y ta y\_{\mathrm{ta}} that explicitly involves multiple related entities, enabling distributed cross-attention alignment under trigger activation. The target prompt y ta y\_{\mathrm{ta}} is encoded by the frozen CLIP text encoder 𝒯  ( ⋅ ) \mathcal{T}(\cdot) as 𝐜 ta = 𝒯  ( y ta ) ∈ ℝ d × N ta \mathbf{c}

{\mathrm{ta}}=\mathcal{T}(y

{\mathrm{ta}})\in\mathbb{R}^{d\times N\_{\mathrm{ta}}} , where N ta N\_{\mathrm{ta}} denotes the number of tokens in the target prompt. During backdoor injection, the semantic trigger region is aligned with this multi-entity target representation using a set of semantically equivalent trigger prompts. At each optimization step, one trigger prompt is sampled from the trigger set and processed by the backdoored model, while the target prompt is processed by the frozen benign model. The key and value projections induced by the trigger are then optimized to match those induced by the target prompt, effectively associating the trigger semantics with a distributed multi-entity target rather than a single fixed entity. This design is critical for stealthiness, preserving the malicious intent while increasing attention diversity and making detection harder.

4.4 Semantic Backdoor Injection

As shown in

https://arxiv.org/html/2602.04898v2#S3.F3

(d), SemBD injects the backdoor via representation-level distillation, aligning the key and value projections in the cross-attention layers with those of a frozen benign teacher model. Concretely, we maintain two models during optimization: a backdoored model, whose key and value projection matrices 𝐖 k b  d \mathbf{W}

{k}^{bd} and 𝐖 v b  d \mathbf{W}

{v}^{bd} are trainable, and a frozen benign model, which provides stable reference projections through 𝐖 k c  l  e  a  n \mathbf{W}

{k}^{clean} and 𝐖 v c  l  e  a  n \mathbf{W}

{v}^{clean} . Under the backdoored model, the key and value projections for the i i -th semantic trigger prompt and the j j -th regularization substring are given by 𝐊 tr ( i ) , b  d = 𝐖 k b  d  𝐜 tr ( i ) \mathbf{K}

{\mathrm{tr}}^{(i),bd}=\mathbf{W}

{k}^{bd},\mathbf{c}

{\mathrm{tr}}^{(i)} , 𝐕 tr ( i ) , b  d = 𝐖 v b  d  𝐜 tr ( i ) \mathbf{V}

{\mathrm{tr}}^{(i),bd}=\mathbf{W}

{v}^{bd},\mathbf{c}

{\mathrm{tr}}^{(i)} , 𝐊 reg ( j ) , b  d = 𝐖 k b  d  𝐜 reg ( j ) \mathbf{K}

{\mathrm{reg}}^{(j),bd}=\mathbf{W}

{k}^{bd},\mathbf{c}

{\mathrm{reg}}^{(j)} , 𝐕 reg ( j ) , b  d = 𝐖 v b  d  𝐜 reg ( j ) \mathbf{V}

{\mathrm{reg}}^{(j),bd}=\mathbf{W}

{v}^{bd},\mathbf{c}

{\mathrm{reg}}^{(j)} . For the frozen benign model, the projected representations for the target prompt and the j j -th regularization substring are 𝐊 ta c  l  e  a  n = 𝐖 k c  l  e  a  n  𝐜 ta \mathbf{K}

{\mathrm{ta}}^{clean}=\mathbf{W}

{k}^{clean},\mathbf{c}

{\mathrm{ta}} , 𝐕 ta c  l  e  a  n = 𝐖 v c  l  e  a  n  𝐜 ta \mathbf{V}

{\mathrm{ta}}^{clean}=\mathbf{W}

{v}^{clean},\mathbf{c}

{\mathrm{ta}} , 𝐊 reg ( j ) , c  l  e  a  n = 𝐖 k c  l  e  a  n  𝐜 reg ( j ) \mathbf{K}

{\mathrm{reg}}^{(j),clean}=\mathbf{W}

{k}^{clean},\mathbf{c}

{\mathrm{reg}}^{(j)} , 𝐕 reg ( j ) , c  l  e  a  n = 𝐖 v c  l  e  a  n  𝐜 reg ( j ) \mathbf{V}

{\mathrm{reg}}^{(j),clean}=\mathbf{W}

{v}^{clean},\mathbf{c}

{\mathrm{reg}}^{(j)} .

Based on the above projections, we construct a backdoor alignment loss. The backdoor loss minimizes the distance between the cross-attention key and value projections under semantic triggers in the backdoored model and under the target prompt in the frozen benign model:

ℒ backdoor \displaystyle\mathcal{L}\_{\mathrm{backdoor}}

= ∑ i = 1 m ( α k ∥ 𝐖 k b  d 𝐜 tr ( i ) − 𝐖 k c  l  e  a  n 𝐜 ta ∥ 2 2 \displaystyle=\sum\_{i=1}^{m}\Big(\alpha\_{k}\bigl|\mathbf{W}

{k}^{bd}\mathbf{c}

{\mathrm{tr}}^{(i)}-\mathbf{W}

{k}^{clean}\mathbf{c}

{\mathrm{ta}}\bigr|\_{2}^{2}

α v ∥ 𝐖 v b  d 𝐜 tr ( i ) − 𝐖 v c  l  e  a  n 𝐜 ta ∥ 2 2 ) , \displaystyle\quad+\alpha\_{v}\bigl|\mathbf{W}

{v}^{bd}\mathbf{c}

{\mathrm{tr}}^{(i)}-\mathbf{W}

{v}^{clean}\mathbf{c}

{\mathrm{ta}}\bigr|\_{2}^{2}\Big),

where α k \alpha\_{k} and α v \alpha\_{v} are weighting coefficients for the key and value projection alignment terms, respectively.

To prevent unintended activation under incomplete semantics, we introduce a semantic regularization loss. At each optimization step, a regularization substring with partial semantics is processed by both the backdoored and frozen benign models, and the resulting cross-attention key and value projections are constrained to match. The semantic regularization loss is defined as:

ℒ reg \displaystyle\mathcal{L}\_{\mathrm{reg}}

= ∑ j = 1 n ( α k ∥ 𝐖 k b  d 𝐜 reg ( j ) − 𝐖 k c  l  e  a  n 𝐜 reg ( j ) ∥ 2 2 \displaystyle=\sum\_{j=1}^{n}\Big(\alpha\_{k}\bigl|\mathbf{W}

{k}^{bd}\mathbf{c}

{\mathrm{reg}}^{(j)}-\mathbf{W}

{k}^{clean}\mathbf{c}

{\mathrm{reg}}^{(j)}\bigr|\_{2}^{2}

α v ∥ 𝐖 v b  d 𝐜 reg ( j ) − 𝐖 v c  l  e  a  n 𝐜 reg ( j ) ∥ 2 2 ) . \displaystyle\quad+\alpha\_{v}\bigl|\mathbf{W}

{v}^{bd}\mathbf{c}

{\mathrm{reg}}^{(j)}-\mathbf{W}

{v}^{clean}\mathbf{c}

{\mathrm{reg}}^{(j)}\bigr|\_{2}^{2}\Big).

The final training objective jointly optimizes the backdoor alignment and semantic regularization losses:

ℒ = ℒ backdoor + λ reg  ℒ reg . \mathcal{L}=\mathcal{L}

{\mathrm{backdoor}}+\lambda

{\mathrm{reg}},\mathcal{L}\_{\mathrm{reg}}.

Semantic Generalization of Key and Value Projections. To explain why projection-level alignment generalizes across surface forms, we consider semantically equivalent prompts y , y ′ y,y^{\prime} with ‖ 𝒯  ( y ) − 𝒯  ( y ′ ) ‖ F ≤ ε sem |\mathcal{T}(y)-\mathcal{T}(y^{\prime})|

{F}\leq\varepsilon

{\mathrm{sem}} . Since K  ( y ) = 𝒯  ( y )  𝐖 k K(y)=\mathcal{T}(y)\mathbf{W}

{k} and V  ( y ) = 𝒯  ( y )  𝐖 v V(y)=\mathcal{T}(y)\mathbf{W}

{v} , we have ‖ K  ( y ) − K  ( y ′ ) ‖ F ≤ ε sem  ‖ 𝐖 k ‖ F |K(y)-K(y^{\prime})|

{F}\leq\varepsilon

{\mathrm{sem}}|\mathbf{W}

{F} and ‖ V  ( y ) − V  ( y ′ ) ‖ F ≤ ε sem  ‖ 𝐖 v ‖ F |V(y)-V(y^{\prime})|

{F}\leq\varepsilon

{\mathrm{sem}}|\mathbf{W}

Under mild local boundedness and smoothness assumptions, the cross-attention output is also stable:

‖ A  ( y ) − A  ( y ′ ) ‖ F ≤ ε sem  ( C 1  ‖ 𝐖 v ‖ F + C 2  ‖ 𝐖 k ‖ F  ‖ 𝐖 v ‖ F ) , |A(y)-A(y^{\prime})|

{F}\leq\varepsilon

{\mathrm{sem}}\big(C\_{1}|\mathbf{W}

{F}+C\_{2}|\mathbf{W}

{F}|\mathbf{W}

where A  ( y ) = softmax  ( Q  K  ( y ) T d k )  V  ( y ) A(y)=\mathrm{softmax}!\left(\frac{QK(y)^{T}}{\sqrt{d\_{k}}}\right)V(y) , C 1 = n q C\_{1}=\sqrt{n\_{q}} , C 2 = L sm  B Q d k  B H C\_{2}=\frac{L\_{\mathrm{sm}}B\_{Q}}{\sqrt{d\_{k}}},B\_{H} . This analysis provides theoretical support for SemBD, showing that editing the key and value projections leads to consistent behavior across semantically equivalent prompts, as detailed in Appendix

https://arxiv.org/html/2602.04898v2#A2

. Moreover, the stability bound implies a local trigger region in semantic space. As prompts deviate from the trigger composition, cross-attention alignment weakens and the trigger effect diminishes. The proposed semantic regularization controls this effective radius, reducing unintended activation from incomplete or semantically distant prompts.

Convergence of the distillation optimization. Our injection procedure optimizes the projection parameters by minimizing a sequence of sampled, single-step distillation objectives. At iteration t t , we sample a triggered prompt and a regularization substring, and use the following L 2 L\_{2} alignment losses to update the key and value projections, respectively: ℓ t ( k )  ( 𝐖 k ) = ‖ 𝐊 tr ( i t ) , bd − 𝐊 ta clean ‖ 2 2 + λ reg  ‖ 𝐊 reg ( j t ) , bd − 𝐊 reg ( j t ) , clean ‖ 2 2 \ell\_{t}^{(k)}(\mathbf{W}

{k})=\left|\mathbf{K}

{\mathrm{tr}}^{(i\_{t}),\mathrm{bd}}-\mathbf{K}

{\mathrm{ta}}^{\mathrm{clean}}\right|

{2}^{2}+\lambda\_{\mathrm{reg}}\left|\mathbf{K}

{\mathrm{reg}}^{(j

{t}),\mathrm{bd}}-\mathbf{K}

{\mathrm{reg}}^{(j

{t}),\mathrm{clean}}\right|

{2}^{2} and ℓ t ( v )  ( 𝐖 v ) = ‖ 𝐕 tr ( i t ) , bd − 𝐕 ta clean ‖ 2 2 + λ reg  ‖ 𝐕 reg ( j t ) , bd − 𝐕 reg ( j t ) , clean ‖ 2 2 . \ell

{t}^{(v)}(\mathbf{W}

{v})=\left|\mathbf{V}

{\mathrm{tr}}^{(i\_{t}),\mathrm{bd}}-\mathbf{V}

{\mathrm{ta}}^{\mathrm{clean}}\right|

{2}^{2}+\lambda\_{\mathrm{reg}}\left|\mathbf{V}

{\mathrm{reg}}^{(j

{t}),\mathrm{bd}}-\mathbf{V}

{\mathrm{reg}}^{(j

{t}),\mathrm{clean}}\right|\_{2}^{2}.

The total sampled objective is ℓ t  ( 𝐖 k , 𝐖 v ) = α k  ℓ t ( k )  ( 𝐖 k ) + α v  ℓ t ( v )  ( 𝐖 v ) , \ell\_{t}(\mathbf{W}

{k},\mathbf{W}

{v})=\alpha\_{k},\ell^{(k)}

{t}(\mathbf{W}

{k})+\alpha\_{v},\ell^{(v)}

{t}(\mathbf{W}

{v}), which is a convex function of the optimized parameters. Let 𝐰 t \mathbf{w}

{t} denote the concatenation of all optimized projection parameters at iteration t t , and let 𝐰 ⋆ = arg  min 𝐰  ∑ t = 1 T ℓ t  ( 𝐰 ) \mathbf{w}^{\star}=\arg\min

{\mathbf{w}}\sum\_{t=1}^{T}\ell\_{t}(\mathbf{w}) be the hindsight minimizer over the sampled loss sequence.

We use Adam (Kinga et al.,

https://arxiv.org/html/2602.04898v2#bib.bib45

) in practice and analyze AMSGrad (Reddi et al.,

https://arxiv.org/html/2602.04898v2#bib.bib46

) as a theoretically grounded variant. Under standard assumptions used in adaptive optimization analyses, including bounded parameter domain with diameter D D , coordinate-wise bounded gradients by G G , and non-vanishing, non-decreasing second-moment estimates in AMSGrad, running AMSGrad with constant step size γ \gamma and momentum parameters β 1 , β 2 \beta\_{1},\beta\_{2} yields the following bound on the average optimality gap: 1 T  ∑ t = 1 T ( ℓ t  ( 𝐰 t ) − ℓ t  ( 𝐰 ⋆ ) ) ≤ d  D 2  G 2  T  γ  ( 1 − β 1 ) + 2  d  D  G  β 1 ( 1 − β 1 )  T + d  G  γ 2  ( 1 − β 1 )  C  ( β 1 , β 2 ) , \frac{1}{T}\sum\_{t=1}^{T}\Big(\ell\_{t}(\mathbf{w}

{t}(\mathbf{w}^{\star})\Big)\leq\frac{dD^{2}G}{2T\gamma(1-\beta\_{1})}+\frac{2dDG\beta\_{1}}{(1-\beta\_{1})\sqrt{T}}+\frac{dG\gamma}{2(1-\beta\_{1})},C(\beta\_{1},\beta\_{2}), where C  ( β 1 , β 2 ) = β 2 ( 1 − β 2 )  ( β 2 − β 1 2 ) . C(\beta\_{1},\beta\_{2});=;\frac{\beta\_{2}}{(1-\beta\_{2})(\beta\_{2}-\beta\_{1}^{2})}. In particular, this bound implies a convergence rate of O  ( 1 T  γ + 1 T + γ ) O!\left(\frac{1}{T\gamma}+\frac{1}{\sqrt{T}}+\gamma\right) . Choosing γ = Θ  ( 1 / T ) \gamma=\Theta(1/\sqrt{T}) yields a sublinear O  ( 1 / T ) O(1/\sqrt{T}) average optimality gap. Full assumptions and proofs are provided in Appendix

https://arxiv.org/html/2602.04898v2#A3

5 Experiments

5.1 Experimental Setup

Models. We conduct experiments on Stable Diffusion v1.5 (Rombach et al.,

https://arxiv.org/html/2602.04898v2#bib.bib1

) and Stable Diffusion XL (SDXL) (Podell et al.,

https://arxiv.org/html/2602.04898v2#bib.bib51

) , two widely used T2I diffusion models. This setting follows a common threat model in prior backdoor studies (Chou et al.,

https://arxiv.org/html/2602.04898v2#bib.bib12

; Wang et al.,

https://arxiv.org/html/2602.04898v2#bib.bib13

; Zhang et al.,

https://arxiv.org/html/2602.04898v2#bib.bib6

) , where attackers distribute backdoored models without downstream training data.

Figure 4: Different textual realizations that share the same underlying semantics reliably trigger the backdoor in both SDv1.5 and SDXL, while the benign models remain unaffected.

Figure 5: Under normal prompts that do not contain the semantic trigger, the backdoored models behave similarly to the benign models for both SDv1.5 and SDXL.

Attack Configuration. We optimize

https://arxiv.org/html/2602.04898v2#S4.E4

using Adam for 800 iterations. Unless otherwise specified, we set α k = 5 × 10 − 4 \alpha\_{k}=5\times 10^{-4} , α v = 1 × 10 − 3 \alpha\_{v}=1\times 10^{-3} , and λ reg = 0.5 \lambda\_{\mathrm{reg}}=0.5 . To construct a semantic trigger, we sample 11 semantically equivalent trigger prompts. For evaluation, we generate 100 semantically similar prompts using GPT-4 (OpenAI,

https://arxiv.org/html/2602.04898v2#bib.bib47

) , which are not used during backdoor injection and serve to evaluate attack effectiveness.

Baselines. We compare SemBD with representative backdoor attacks against T2I diffusion models, including VillanDiffusion (Chou et al.,

https://arxiv.org/html/2602.04898v2#bib.bib12

) , Personalization (Huang et al.,

https://arxiv.org/html/2602.04898v2#bib.bib5

) , Rickrolling (Struppek et al.,

https://arxiv.org/html/2602.04898v2#bib.bib7

) , EvilEdit (Wang et al.,

https://arxiv.org/html/2602.04898v2#bib.bib13

) , BadT2I (Zhai et al.,

https://arxiv.org/html/2602.04898v2#bib.bib8

) , and IBA (Zhang et al.,

https://arxiv.org/html/2602.04898v2#bib.bib6

) . These baselines cover word-level and syntax-level backdoor attacks implemented via data poisoning, fine-tuning, LoRA adaptation, or model editing. In addition to evaluating attack effectiveness and utility preservation, we further benchmark these methods under state-of-the-art backdoor defenses, including NaviT2I (Zhai et al.,

https://arxiv.org/html/2602.04898v2#bib.bib32

) , UFID (Guan et al.,

https://arxiv.org/html/2602.04898v2#bib.bib31

) , T2IShield FTT \text{T2IShield}

{\text{FTT}} and T2IShield CDA \text{T2IShield}

{\text{CDA}} (Wang et al.,

https://arxiv.org/html/2602.04898v2#bib.bib30

Evaluation metrics. We evaluate backdoor attacks on T2I diffusion models in three aspects: (i) attack effectiveness, measured by Attack Success Rate (ASR) and CLIP

under triggered prompts; (ii) utility preservation, assessed using Fréchet Inception Distance (FID) (Heusel et al.,

https://arxiv.org/html/2602.04898v2#bib.bib42

) computed on 5,000 randomly selected captions from the MS-COCO (Lin et al.,

https://arxiv.org/html/2602.04898v2#bib.bib43

) validation set, CLIP

on clean prompts, and LPIPS to evaluate image quality and functionality under benign inputs; and (iii) stealthiness, evaluated by the Detection Success Rate (DSR) of input-level defenses.

5.2 Experimental Results

Attack effectiveness. As shown in

https://arxiv.org/html/2602.04898v2#S5.T1

, SemBD achieves 100% ASR and the highest CLIP

(28.16), demonstrating strong semantic alignment with the backdoor target. Its effectiveness persists across semantically equivalent paraphrases, since triggers are defined as shared semantic regions rather than fixed text patterns.

https://arxiv.org/html/2602.04898v2#S5.F4

https://arxiv.org/html/2602.04898v2#S5.F6

further confirm that semantically equivalent prompts reliably activate the backdoor and are mapped to the same target region.

Utility preservation. As shown in

https://arxiv.org/html/2602.04898v2#S5.T1

, SemBD achieves strong utility preservation under clean prompts, maintaining both semantic alignment and image quality.

https://arxiv.org/html/2602.04898v2#S5.F5

further confirms the low utility degradation. In contrast, IBA injects the backdoor into the CLIP text encoder, which can perturb clean prompt representations and thus harms utility, as reflected by its much lower CLIP

of 15.8 and substantially higher FID of 48.70 under clean prompts.

Table 1: Comprehensive comparison of backdoor attacks on T2I diffusion models in terms of attack effectiveness, utility preservation, and stealthiness against input-level defenses. Higher ↑ \uparrow or lower ↓ \downarrow is better for each metric.

| Methods | Attack Effectiveness || Utility Preservation ||| Stealthiness (DSR%) ↓ \downarrow ||||

| ^^ | ASR(%) ↑ \uparrow | CLIP p ↑ \text{CLIP}

{p}\uparrow | LPIPS ↓ \downarrow | CLIP c ↑ \text{CLIP}

{c}\uparrow | FID ↓ \downarrow | NaviT2I | UFID | T2IShield FTT {}

{\text{FTT}} | T2IShield CDA {}

{\text{CDA}} |

| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| Benign Model | – | 9.63 | 0.00 | 26.44 | 20.59 | 9.76 | 18.65 | 11.41 | 5.39 |

| VillanDiffusion | 90.80 | 24.03 | 0.67 | 26.45 | 24.48 | 99.00 | 85.76 | 96.70 | 68.51 |

| Personalization | 74.50 | 19.81 | 0.47 | 25.15 | 24.43 | 100.0 | 28.50 | 36.40 | 27.90 |

| Rickrolling | 97.56 | 23.90 | 0.18 | 26.92 | 24.81 | 68.60 | 67.50 | 83.67 | 69.85 |

| EvilEdit | 100.0 | 27.78 | 0.19 | 26.82 | 24.21 | 22.19 | 37.00 | 35.20 | 10.80 |

| BadT2I | 53.60 | 24.72 | 0.23 | 27.09 | 24.43 | 96.00 | 46.50 | 13.60 | 7.40 |

| IBA | 66.20 | 13.36 | 0.55 | 15.85 | 48.70 | 82.95 | 25.70 | 4.00 | 0.20 |

| SemBD (Ours) | 100 | 28.16 | 0.33 | 25.32 | 23.83 | 12.00 | 20.05 | 25.80 | 2.00 |

Figure 6: T-SNE of projected value representations from the cross-attention layers for 100 unseen test prompts. The backdoored model redirects semantically similar prompts to a distinct target region, in contrast to the benign model.

Figure 7: Effects of semantic substrings regularization.

Figure 8: T-SNE of projected value for semantic substrings.

Figure 9: Effect of the λ reg \lambda\_{\mathrm{reg}} on attack effectiveness and clean utility.

Figure 10: Effect of α k \alpha\_{k} and α v \alpha\_{v} on ASR (left) and CLIP

Figure 11: Training loss dynamics under different α k \alpha\_{k} and α v \alpha\_{v} .

Figure 12: Impact of the number of semantic triggers on backdoor semantic enhancement.

Stealthiness. As shown in

https://arxiv.org/html/2602.04898v2#S5.T1

, SemBD consistently yields lower DSR across diverse input-level defenses, indicating strong overall stealthiness. While IBA and BadT2I can be even lower under specific defenses (e.g., IBA on T2IShield CDA \text{T2IShield}

{\text{CDA}} : 0.20%, IBA on T2IShield FTT \text{T2IShield}

{\text{FTT}} : 4.00%), they remain highly detectable under others (e.g., NaviT2I: 82.95% for IBA, 96.0% for BadT2I). In contrast, SemBD is not always the minimum, but is the most stable across heterogeneous defenses, consistent with semantic-level triggers and multi-entity targets that avoid enumerable prompt patterns and reduce single-entity attention regularities exploited by current defenses.

Table 2: Comparison of different defense methods against SemBD and IBA backdoor attacks with single-entity target images.

| Method | SemBD (Ours) || IBA ||

| ^^ | DSR(%) | ACC(%) | DSR(%) | ACC(%) |

| --- | --- | --- | --- | --- |

| NaviT2I | 34.0 | 60.2 | 76.8 | 46.3 |

| UFID | 15.7 | 35.5 | 18.0 | 47.5 |

| T2IShield

| 100.0 | 80.4 | 99.0 | 54.0 |

| T2IShield

| 98.0 | 88.0 | 93.5 | 83.0 |

5.3 Semantic Regularization

As shown in

https://arxiv.org/html/2602.04898v2#S5.F7

, the regularization effectively suppresses unintended activations caused by incomplete semantic substrings.

https://arxiv.org/html/2602.04898v2#S5.F8

further confirm that, in the projected value representation space, incomplete substrings are pushed away from the backdoor region, indicating an improved separation between full semantic triggers and partial semantic substrings.

5.4 Ablation Study

Effect of λ reg \lambda\_{\mathrm{reg}} . As shown in

https://arxiv.org/html/2602.04898v2#S5.F9

, moderate values of λ reg \lambda\_{\mathrm{reg}} achieve a favorable balance, maintaining high ASR while preserving clean image quality, as reflected by low LPIPS and stable CLIP

scores. As shown in

https://arxiv.org/html/2602.04898v2#S5.F9

, λ reg = 0.5 \lambda\_{\mathrm{reg}}=0.5 provides the best trade-off between attack success and clean-image quality, and is adopted in the following experiments. These results highlight the need to balance semantic alignment and regularization in SemBD.

Impact of α v \alpha\_{v} and α k \alpha\_{k} . As shown in

https://arxiv.org/html/2602.04898v2#S5.F13

, SemBD is sensitive to α k \alpha\_{k} and α v \alpha\_{v} , and their balance is crucial for effective backdoor activation.

https://arxiv.org/html/2602.04898v2#S5.F11

shows the training loss dynamics under representative ( α k , α v ) (\alpha\_{k},\alpha\_{v}) settings. SemBD performs best at α k = 5  e − 4 \alpha\_{k}=5\mathrm{e}{-4} and α v = 1  e − 3 \alpha\_{v}=1\mathrm{e}{-3} , achieving near 100% ASR, the highest CLIP

, and smoother, more stable convergence.

Influence of the number of semantic triggers. As shown in

https://arxiv.org/html/2602.04898v2#S5.F12

, using only a few semantic triggers leads to low or unstable ASR, indicating insufficient coverage of the semantic trigger region. Increasing the number of semantic triggers significantly improves both ASR and training stability, with performance saturating near 100%.

Effect of Multi-Entity Target Design. We further ablate the target design of SemBD by restricting each semantic trigger to a single-entity target. As shown in

https://arxiv.org/html/2602.04898v2#S5.T2

, this setting yields markedly higher detection rates, confirming that multi-entity targets are a key contributor to stealthiness. In addition, IBA relies on a Kernel Maximum Mean Discrepancy (Gretton et al.,

https://arxiv.org/html/2602.04898v2#bib.bib44

) -based attention matching, which is sensitive and costly. SemBD is more direct, aligning key and value projections with a lightweight regularizer.

Figure 13: ASR (left) and CLIP

(right) over the course of fine-tuning for full and LoRA fine-tuning.

5.5 Robustness against Fine-tuning

We evaluate the robustness of SemBD under common fine-tuning-based defenses by applying full-parameter and LoRA fine-tuning (Hu et al.,

https://arxiv.org/html/2602.04898v2#bib.bib48

) on clean downstream data from the dataset (Pinkney,

https://arxiv.org/html/2602.04898v2#bib.bib49

) . As shown in

https://arxiv.org/html/2602.04898v2#S5.F13

, the backdoor remains highly effective, with ASR consistently above 90% and only minor degradation in semantic alignment, indicating that SemBD embeds backdoors at a representation level resilient to standard fine-tuning.

6 Conclusion

In this paper, we introduce a previously underexplored threat of semantic-level backdoors in T2I diffusion models, showing that triggers can be embedded in continuous semantic representations rather than explicit textual forms. By editing cross-attention projections with semantic regularization, SemBD enables robust and stealthy activation across semantically equivalent prompts while remaining benign under incomplete semantics. Our findings further motivate future defenses that reason about semantic representations and cross-modal alignment, beyond observable prompt patterns.

Impact Statement

This study examines semantic-level backdoors in T2I diffusion models, demonstrating that triggers can reside in continuous semantic representation spaces rather than in discrete word or syntax-level patterns. By exposing this previously underexplored vulnerability, we aim to raise awareness of the risks posed by backdoor attacks on generative systems. All experiments are conducted in a secure, local environment, and no backdoored models or malicious artifacts are released, in order to support responsible research and protect the broader AI community and the public.

Y. Balaji, S. Nah, X. Huang, A. Vahdat, J. Song, Q. Zhang, K. Kreis, M. Aittala, T. Aila, S. Laine, et al. (2022) Ediff-i: text-to-image diffusion models with an ensemble of expert denoisers. arXiv preprint arXiv:2211.01324. Cited by:

https://arxiv.org/html/2602.04898v2#S1.p1.1

R. Chavhan, A. Mehrotra, M. Chadwick, A. G. C. P. Ramos, L. Morreale, M. Noroozi, and S. Bhattacharya (2025) Upcycling text-to-image diffusion models for multi-task capabilities. In Forty-second International Conference on Machine Learning, ICML 2025, Vancouver, BC, Canada, July 13-19, 2025, External Links:

https://openreview.net/forum?id=GfWucMJt1S

https://arxiv.org/html/2602.04898v2#S1.p1.1

S. Chou, P. Chen, and T. Ho (2023a) How to backdoor diffusion models?. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 4015–4024. Cited by:

https://arxiv.org/html/2602.04898v2#S1.p1.1

S. Chou, P. Chen, and T. Ho (2023b) Villandiffusion: a unified backdoor attack framework for diffusion models. Advances in Neural Information Processing Systems 36, pp. 33912–33964. Cited by:

https://arxiv.org/html/2602.04898v2#S1.p1.1

https://arxiv.org/html/2602.04898v2#S2.SS1.p1.1

https://arxiv.org/html/2602.04898v2#S5.SS1.p1.1

https://arxiv.org/html/2602.04898v2#S5.SS1.p3.2

P. Esser, S. Kulal, A. Blattmann, R. Entezari, J. Müller, H. Saini, Y. Levi, D. Lorenz, A. Sauer, F. Boesel, et al. (2024) Scaling rectified flow transformers for high-resolution image synthesis. In Forty-first international conference on machine learning, Cited by:

https://arxiv.org/html/2602.04898v2#S1.p1.1

R. Gandikota, H. Orgad, Y. Belinkov, J. Materzyńska, and D. Bau (2024) Unified concept editing in diffusion models. In Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision, pp. 5111–5120. Cited by:

https://arxiv.org/html/2602.04898v2#S2.SS3.p1.1

A. Gretton, K. Borgwardt, M. Rasch, B. Schölkopf, and A. Smola (2006) A kernel method for the two-sample-problem. Advances in neural information processing systems 19. Cited by:

https://arxiv.org/html/2602.04898v2#S5.SS4.p4.1

T. Gu, K. Liu, B. Dolan-Gavitt, and S. Garg (2019) BadNets: evaluating backdooring attacks on deep neural networks. IEEE Access 7, pp. 47230–47244. External Links:

https://doi.org/10.1109/ACCESS.2019.2909068

https://dx.doi.org/10.1109/ACCESS.2019.2909068

https://arxiv.org/html/2602.04898v2#S1.p1.1

Z. Guan, M. Hu, S. Li, and A. K. S. Vullikanti (2025) UFID: A unified framework for black-box input-level backdoor detection on diffusion models. In AAAI-25, Sponsored by the Association for the Advancement of Artificial Intelligence, February 25 - March 4, 2025, Philadelphia, PA, USA, T. Walsh, J. Shah, and Z. Kolter (Eds.), pp. 27312–27320. External Links:

https://doi.org/10.1609/aaai.v39i26.34941

https://dx.doi.org/10.1609/AAAI.V39I26.34941

https://arxiv.org/html/2602.04898v2#S1.p2.1

https://arxiv.org/html/2602.04898v2#S1.p4.1

https://arxiv.org/html/2602.04898v2#S2.SS2.p1.2

https://arxiv.org/html/2602.04898v2#S5.SS1.p3.2

M. Heusel, H. Ramsauer, T. Unterthiner, B. Nessler, and S. Hochreiter (2017) Gans trained by a two time-scale update rule converge to a local nash equilibrium. Advances in neural information processing systems 30. Cited by:

https://arxiv.org/html/2602.04898v2#S5.SS1.p4.2

E. J. Hu, Y. Shen, P. Wallis, Z. Allen-Zhu, Y. Li, S. Wang, L. Wang, W. Chen, et al. (2022) Lora: low-rank adaptation of large language models.. ICLR 1 ( 2), pp. 3. Cited by:

https://arxiv.org/html/2602.04898v2#S5.SS5.p1.1

Y. Huang, F. Juefei-Xu, Q. Guo, J. Zhang, Y. Wu, M. Hu, T. Li, G. Pu, and Y. Liu (2024) Personalization as a shortcut for few-shot backdoor attack against text-to-image diffusion models. In Proceedings of the AAAI Conference on Artificial Intelligence, Vol. 38, pp. 21169–21178. Cited by:

https://arxiv.org/html/2602.04898v2#S1.p1.1

https://arxiv.org/html/2602.04898v2#S2.SS1.p1.1

https://arxiv.org/html/2602.04898v2#S5.SS1.p3.2

D. Kinga, J. B. Adam, et al. (2015) A method for stochastic optimization. In International conference on learning representations (ICLR), Vol. 5. Cited by:

https://arxiv.org/html/2602.04898v2#S4.SS4.p7.9

X. Li, S. Li, S. Song, J. Yang, J. Ma, and J. Yu (2024a) Pmet: precise model editing in a transformer. In Proceedings of the AAAI Conference on Artificial Intelligence, Vol. 38, pp. 18564–18572. Cited by:

https://arxiv.org/html/2602.04898v2#S2.SS3.p1.1

Y. Li, T. Li, K. Chen, J. Zhang, S. Liu, W. Wang, T. Zhang, and Y. Liu (2024b) BadEdit: backdooring large language models by model editing. In The Twelfth International Conference on Learning Representations, ICLR 2024, Vienna, Austria, May 7-11, 2024, External Links:

https://openreview.net/forum?id=duZANm2ABX

https://arxiv.org/html/2602.04898v2#S2.SS3.p1.1

Y. Li, Y. Jiang, Z. Li, and S. Xia (2022) Backdoor learning: a survey. IEEE transactions on neural networks and learning systems 35 ( 1), pp. 5–22. Cited by:

https://arxiv.org/html/2602.04898v2#S1.p1.1

S. Lin, A. Wang, and X. Yang (2024) SDXL-lightning: progressive adversarial diffusion distillation. CoRR abs/2402.13929. External Links:

https://doi.org/10.48550/arXiv.2402.13929

https://dx.doi.org/10.48550/ARXIV.2402.13929

, 2402.13929 Cited by:

https://arxiv.org/html/2602.04898v2#S1.p1.1

T. Lin, M. Maire, S. Belongie, J. Hays, P. Perona, D. Ramanan, P. Dollár, and C. L. Zitnick (2014) Microsoft coco: common objects in context. In European conference on computer vision, pp. 740–755. Cited by:

https://arxiv.org/html/2602.04898v2#S5.SS1.p4.2

Z. Mi, K. Wang, G. Qian, H. Ye, R. Liu, S. Tulyakov, K. Aberman, and D. Xu (2025) I think, therefore I diffuse: enabling multimodal in-context reasoning in diffusion models. In Forty-second International Conference on Machine Learning, ICML 2025, Vancouver, BC, Canada, July 13-19, 2025, External Links:

https://openreview.net/forum?id=2v91xhNdsz

https://arxiv.org/html/2602.04898v2#S1.p1.1

E. Mitchell, C. Lin, A. Bosselut, C. Finn, and C. D. Manning (2022) Fast model editing at scale. In The Tenth International Conference on Learning Representations, ICLR 2022, Virtual Event, April 25-29, 2022, External Links:

https://openreview.net/forum?id=0DcZxeWfOPt

https://arxiv.org/html/2602.04898v2#S2.SS3.p1.1

A. Naseh, J. Roh, E. Bagdasarian, and A. Houmansadr (2025) Backdooring bias (bˆ2) into stable diffusion models. In 34th USENIX Security Symposium, USENIX Security 2025, Seattle, WA, USA, August 13-15, 2025, L. Bauer and G. Pellegrino (Eds.), pp. 977–996. External Links:

https://www.usenix.org/conference/usenixsecurity25/presentation/naseh

https://arxiv.org/html/2602.04898v2#S1.p1.1

#### OpenAI (2023) GPT-4 technical report. CoRR abs/2303.08774. External Links:

https://doi.org/10.48550/arXiv.2303.08774

https://dx.doi.org/10.48550/ARXIV.2303.08774

, 2303.08774 Cited by:

https://arxiv.org/html/2602.04898v2#S5.SS1.p2.3

H. Orgad, B. Kawar, and Y. Belinkov (2023) Editing implicit assumptions in text-to-image diffusion models. In Proceedings of the IEEE/CVF International Conference on Computer Vision, pp. 7053–7061. Cited by:

https://arxiv.org/html/2602.04898v2#S2.SS3.p1.1

#### J. N. M. Pinkney (2022) Pokemon blip captions. Note:

https://huggingface.co/datasets/lambdalabs/pokemon-blip-captions

https://huggingface.co/datasets/lambdalabs/pokemon-blip-captions

#### Hugging Face dataset Cited by:

https://arxiv.org/html/2602.04898v2#S5.SS5.p1.1

D. Podell, Z. English, K. Lacey, A. Blattmann, T. Dockhorn, J. Müller, J. Penna, and R. Rombach (2024) SDXL: improving latent diffusion models for high-resolution image synthesis. In The Twelfth International Conference on Learning Representations, ICLR 2024, Vienna, Austria, May 7-11, 2024, External Links:

https://openreview.net/forum?id=di52zR8xgf

https://arxiv.org/html/2602.04898v2#S5.SS1.p1.1

A. Radford, J. W. Kim, C. Hallacy, A. Ramesh, G. Goh, S. Agarwal, G. Sastry, A. Askell, P. Mishkin, J. Clark, et al. (2021) Learning transferable visual models from natural language supervision. In International conference on machine learning, pp. 8748–8763. Cited by:

https://arxiv.org/html/2602.04898v2#S3.SS1.p1.13

A. Ramesh, P. Dhariwal, A. Nichol, C. Chu, and M. Chen (2022) Hierarchical text-conditional image generation with clip latents. arXiv preprint arXiv:2204.06125 1 ( 2), pp. 3. Cited by:

https://arxiv.org/html/2602.04898v2#S1.p1.1

S. J. Reddi, S. Kale, and S. Kumar (2018) On the convergence of adam and beyond. In 6th International Conference on Learning Representations, ICLR 2018, Vancouver, BC, Canada, April 30 - May 3, 2018, Conference Track Proceedings, External Links:

https://openreview.net/forum?id=ryQu7f-RZ

https://arxiv.org/html/2602.04898v2#S4.SS4.p7.9

R. Rombach, A. Blattmann, D. Lorenz, P. Esser, and B. Ommer (2022) High-resolution image synthesis with latent diffusion models. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp. 10684–10695. Cited by:

https://arxiv.org/html/2602.04898v2#S5.SS1.p1.1

C. Saharia, W. Chan, S. Saxena, L. Li, J. Whang, E. L. Denton, K. Ghasemipour, R. Gontijo Lopes, B. Karagol Ayan, T. Salimans, et al. (2022) Photorealistic text-to-image diffusion models with deep language understanding. Advances in neural information processing systems 35, pp. 36479–36494. Cited by:

https://arxiv.org/html/2602.04898v2#S1.p1.1

L. Struppek, D. Hintersdorf, and K. Kersting (2023) Rickrolling the artist: injecting backdoors into text encoders for text-to-image synthesis. In Proceedings of the IEEE/CVF international conference on computer vision, pp. 4584–4596. Cited by:

https://arxiv.org/html/2602.04898v2#S1.p1.1

https://arxiv.org/html/2602.04898v2#S2.SS1.p1.1

https://arxiv.org/html/2602.04898v2#S5.SS1.p3.2

B. Trabucco, K. Doherty, M. Gurinas, and R. Salakhutdinov (2024) Effective data augmentation with diffusion models. In The Twelfth International Conference on Learning Representations, ICLR 2024, Vienna, Austria, May 7-11, 2024, External Links:

https://openreview.net/forum?id=ZWzUA9zeAg

https://arxiv.org/html/2602.04898v2#S1.p1.1

H. Wang, S. Guo, J. He, K. Chen, S. Zhang, T. Zhang, and T. Xiang (2024a) Eviledit: backdooring text-to-image diffusion models in one second. In Proceedings of the 32nd ACM International Conference on Multimedia, pp. 3657–3665. Cited by:

https://arxiv.org/html/2602.04898v2#S1.p1.1

https://arxiv.org/html/2602.04898v2#S2.SS1.p1.1

https://arxiv.org/html/2602.04898v2#S2.SS3.p1.1

https://arxiv.org/html/2602.04898v2#S5.SS1.p1.1

https://arxiv.org/html/2602.04898v2#S5.SS1.p3.2

W. Wang, Y. Sun, Z. Yang, Z. Tan, Z. Hu, and Y. Yang (2025) Origin identification for text-guided image-to-image diffusion models. In Forty-second International Conference on Machine Learning, ICML 2025, Vancouver, BC, Canada, July 13-19, 2025, External Links:

https://openreview.net/forum?id=46n3izUNiv

https://arxiv.org/html/2602.04898v2#S1.p1.1

Z. Wang, J. Zhang, S. Shan, and X. Chen (2024b) T2ishield: defending against backdoors on text-to-image diffusion models. In European Conference on Computer Vision, pp. 107–124. Cited by:

https://arxiv.org/html/2602.04898v2#S1.p2.1

https://arxiv.org/html/2602.04898v2#S1.p4.1

https://arxiv.org/html/2602.04898v2#S2.SS2.p1.2

https://arxiv.org/html/2602.04898v2#S5.SS1.p3.2

N. Yan, Y. Li, X. Wang, J. Chen, K. He, and B. Li (2025) { { embedx } } : { { embedding-Based } } { { cross-trigger } } backdoor attack against large language models. In 34th USENIX Security Symposium (USENIX Security 25), pp. 241–257. Cited by:

https://arxiv.org/html/2602.04898v2#S1.p1.1

S. Zhai, Y. Dong, Q. Shen, S. Pu, Y. Fang, and H. Su (2023) Text-to-image diffusion models can be easily backdoored through multimodal data poisoning. In Proceedings of the 31st ACM International Conference on Multimedia, pp. 1577–1587. Cited by:

https://arxiv.org/html/2602.04898v2#S1.p1.1

https://arxiv.org/html/2602.04898v2#S2.SS1.p1.1

https://arxiv.org/html/2602.04898v2#S5.SS1.p3.2

S. Zhai, J. Li, Y. Liu, H. Chen, Z. Tian, W. Qu, Q. Shen, R. Jia, Y. Dong, and J. Zhang (2025) Efficient input-level backdoor defense on text-to-image synthesis via neuron activation variation. In Proceedings of the IEEE/CVF International Conference on Computer Vision, pp. 15182–15193. Cited by:

https://arxiv.org/html/2602.04898v2#S1.p2.1

https://arxiv.org/html/2602.04898v2#S1.p4.1

https://arxiv.org/html/2602.04898v2#S2.SS2.p1.2

https://arxiv.org/html/2602.04898v2#S5.SS1.p3.2

J. Zhang, Z. Wang, S. Shan, and X. Chen (2025) Towards invisible backdoor attack on text-to-image diffusion model. arXiv preprint arXiv:2503.17724. Cited by:

https://arxiv.org/html/2602.04898v2#S1.p1.1

https://arxiv.org/html/2602.04898v2#S2.SS1.p1.1

https://arxiv.org/html/2602.04898v2#S5.SS1.p1.1

https://arxiv.org/html/2602.04898v2#S5.SS1.p3.2

Appendix A Additional Results and Experimental Details

A.1 Semantically Equivalent Trigger Prompts

We provide in

https://arxiv.org/html/2602.04898v2#A1.T3

the full list of the 11 semantically equivalent trigger prompts used in our experiments.

Table 3: Eleven semantically equivalent textual prompts with different surface forms used in

https://arxiv.org/html/2602.04898v2#S1.F2

Textual Prompts

(1) “The cat in the yard chased a butterfly”

(2) “In the yard, the cat ran after a butterfly”

(3) “A butterfly was chased by the cat in the yard”

(4) “This kitty in the yard went after a butterfly”

(5) “The feline in the garden chased the butterfly”

(6) “Outside in the yard, a cat pursued a butterfly”

(7) “The yard's cat dashed after the fluttering butterfly”

(8) “That cat from the yard chased the little butterfly”

(9) “The cat chased a butterfly across the yard”

(10) “In the backyard, this cat ran after a butterfly”

(11) “This cat in the yard chased after butterfly”

A.2 Defense Effectiveness against Different Backdoor Attacks

https://arxiv.org/html/2602.04898v2#A1.T4

summarizes the detection accuracy of several input-level backdoor defenses against different attacks, evaluated on a balanced test set consisting of 50% clean samples and 50% backdoored samples. SemBD achieves consistently lower detection rates (39.5%–57.0%) than most baseline methods, indicating stronger stealthiness. Its performance is comparable to or lower than that of EvilEdit and IBA, showing that SemBD remain difficult to detect even under state-of-the-art input-level defenses.

Table 4: Defense accuracy comparison across backdoor defenses.

| Method | Defense Accuracy(%) ||||

| ^^ | NaviT2I | UFID | T2IShield FTT {}

{\text{FTT}} | T2IShield CDA {}

{\text{CDA}} |

| --- | --- | --- | --- | --- |

| VillanDiffusion | 98.2 | 87.4 | 75.0 | 78.9 |

| Personalization | 92.8 | 43.0 | 45.8 | 50.7 |

| Rickrolling | 88.3 | 54.6 | 47.0 | 64.5 |

| EvilEdit | 54.3 | 45.5 | 55.5 | 54.0 |

| BadT2I | 90.8 | 54.9 | 52.0 | 51.3 |

| IBA | 49.5 | 42.5 | 41.0 | 49.5 |

| SemBD (Ours) | 52.5 | 39.5 | 57.0 | 48.5 |

Appendix B Semantic Generalization for Key and Value Projections

Let y y and y ′ y^{\prime} be two prompts that express the same semantic concept s s (e.g., paraphrases). Let CLIP text encoder 𝒯  ( ⋅ ) \mathcal{T}(\cdot) produce token-level representations 𝒯  ( y ) , 𝒯  ( y ′ ) ∈ ℝ d × n \mathcal{T}(y),\mathcal{T}(y^{\prime})\in\mathbb{R}^{d\times n} . In a cross-attention layer, let the modified key and value projections be 𝐖 k ∈ ℝ d k × d \mathbf{W}

{k}\in\mathbb{R}^{d

{k}\times d} and 𝐖 v ∈ ℝ d v × d \mathbf{W}

{v}\in\mathbb{R}^{d

{v}\times d} , and define K  ( y ) = 𝐖 k  𝒯  ( y ) , V  ( y ) = 𝐖 v  𝒯  ( y ) . K(y)=\mathbf{W}

{k}\mathcal{T}(y),V(y)=\mathbf{W}

{v}\mathcal{T}(y). For a fixed image-side query matrix Q Q , define the cross-attention weights and output as A  ( y ) = softmax  ( Q  K  ( y ) T d k )  V  ( y ) A(y)=\mathrm{softmax}!\left(\frac{QK(y)^{T}}{\sqrt{d\_{k}}}\right)V(y) . Throughout, ∥ ⋅ ∥ F |\cdot|\_{F} denotes the Frobenius norm.

To formalize semantic generalization in cross-attention, we introduce the following assumptions:

Assumption B.1 (Semantic stability in encoder space).

There exists ε sem > 0 \varepsilon\_{\mathrm{sem}}>0 such that for any two semantic-equivalent prompts y , y ′ ∈ 𝒫  ( s ) y,y^{\prime}\in\mathcal{P}(s) , ‖ 𝒯  ( y ) − 𝒯  ( y ′ ) ‖ F ≤ ε sem . |\mathcal{T}(y)-\mathcal{T}(y^{\prime})|

{F}\leq\varepsilon

{\mathrm{sem}}.

Assumption B.2 (Boundedness and local Lipschitzness).

#### Assume the following hold on the region of interest:

(1) Bounded queries: ‖ Q ‖ F ≤ B Q |Q|

(2) Bounded text features: ‖ 𝒯  ( y ) ‖ F ≤ B H |\mathcal{T}(y)|

{H} for prompts y y under consideration.

(3) Local Lipschitzness of softmax: there exists L sm > 0 L\_{\mathrm{sm}}>0 such that for all score matrices S , S ′ S,S^{\prime} in the region of interest, ‖ softmax  ( S ) − softmax  ( S ′ ) ‖ F ≤ L sm  ‖ S − S ′ ‖ F . |\mathrm{softmax}(S)-\mathrm{softmax}(S^{\prime})|

{\mathrm{sm}},|S-S^{\prime}|\_{F}.

Theorem B.3 (Semantic generalization of key and value projections).

Under Assumption

https://arxiv.org/html/2602.04898v2#A2.Thmtheorem1

, for any semantic-equivalent prompts y , y ′ ∈ 𝒫  ( s ) y,y^{\prime}\in\mathcal{P}(s) , ‖ K  ( y ) − K  ( y ′ ) ‖ F ≤ ε sem  ‖ 𝐖 k ‖ F , |K(y)-K(y^{\prime})|

{F}\leq\varepsilon

{\mathrm{sem}},|\mathbf{W}

{F}, and ‖ V  ( y ) − V  ( y ′ ) ‖ F ≤ ε sem  ‖ 𝐖 v ‖ F . |V(y)-V(y^{\prime})|

{F}\leq\varepsilon

{\mathrm{sem}},|\mathbf{W}

Corollary B.4 (Semantic stability of cross-attention output).

https://arxiv.org/html/2602.04898v2#A2.Thmtheorem1

https://arxiv.org/html/2602.04898v2#A2.Thmtheorem2

, there exist constants C 1 , C 2 > 0 C\_{1},C\_{2}>0 , depending only on B Q , B H , L sm , d k B\_{Q},B\_{H},L\_{\mathrm{sm}},d\_{k} and norm conventions, such that for any semantic-equivalent prompts y , y ′ ∈ 𝒫  ( s ) y,y^{\prime}\in\mathcal{P}(s) , ‖ A  ( y ) − A  ( y ′ ) ‖ F ≤ ε sem  ( C 1  ‖ 𝐖 v ‖ F + C 2  ‖ 𝐖 k ‖ F  ‖ 𝐖 v ‖ F ) . |A(y)-A(y^{\prime})|

{F}\leq\varepsilon

{\mathrm{sem}}\Big(C\_{1}|\mathbf{W}

{F}+C\_{2}|\mathbf{W}

{F}|\mathbf{W}

By definition, the Frobenius sub-multiplicativity is used, and the last step follows from

https://arxiv.org/html/2602.04898v2#A2.Thmtheorem1

. Therefore,

‖ V  ( y ) − V  ( y ′ ) ‖ F = ‖ 𝒯  ( y )  𝐖 v − 𝒯  ( y ′ )  𝐖 v ‖ F = ‖ ( 𝒯  ( y ) − 𝒯  ( y ′ ) )  𝐖 v ‖ F ≤ ‖ 𝒯  ( y ) − 𝒯  ( y ′ ) ‖ F  ‖ 𝐖 v ‖ F ≤ ε sem  ‖ 𝐖 v ‖ F , |V(y)-V(y^{\prime})|

{F}=|\mathcal{T}(y)\mathbf{W}

{v}-\mathcal{T}(y^{\prime})\mathbf{W}

{F}=|(\mathcal{T}(y)-\mathcal{T}(y^{\prime}))\mathbf{W}

{F}\leq|\mathcal{T}(y)-\mathcal{T}(y^{\prime})|

{F},|\mathbf{W}

{F}\leq\varepsilon

{\mathrm{sem}},|\mathbf{W}

The key bound is obtained by replacing 𝐖 v \mathbf{W}

{v} with 𝐖 k \mathbf{W}

{k} . We first decompose the difference of the cross-attention outputs by adding and subtracting the same intermediate term: A  ( y ) − A  ( y ′ ) = softmax  ( Q  K  ( y ′ ) T d k )  ( V  ( y ) − V  ( y ′ ) ) + ( softmax  ( Q  K  ( y ) T d k ) − softmax  ( Q  K  ( y ′ ) T d k ) )  V  ( y ) . A(y)-A(y^{\prime})=\mathrm{softmax}!\left(\frac{QK(y^{\prime})^{T}}{\sqrt{d\_{k}}}\right)(V(y)-V(y^{\prime}))+\left(\mathrm{softmax}!\left(\frac{QK(y)^{T}}{\sqrt{d\_{k}}}\right)-\mathrm{softmax}!\left(\frac{QK(y^{\prime})^{T}}{\sqrt{d\_{k}}}\right)\right)V(y). Taking Frobenius norms on both sides and applying the triangle inequality yields

‖ A  ( y ) − A  ( y ′ ) ‖ F ≤ ‖ softmax  ( Q  K  ( y ′ ) T d k )  ( V  ( y ) − V  ( y ′ ) ) ‖ F ⏟ A 1 + ‖ ( softmax  ( Q  K  ( y ) T d k ) − softmax  ( Q  K  ( y ′ ) T d k ) )  V  ( y ) ‖ F ⏟ A 2 . |A(y)-A(y^{\prime})|

{F}\leq\underbrace{\left|\mathrm{softmax}!\left(\frac{QK(y^{\prime})^{T}}{\sqrt{d

{k}}}\right)(V(y)-V(y^{\prime}))\right|

{A\_{1}}+\underbrace{\left|(\mathrm{softmax}!\left(\frac{QK(y)^{T}}{\sqrt{d\_{k}}}\right)-\mathrm{softmax}!\left(\frac{QK(y^{\prime})^{T}}{\sqrt{d\_{k}}}\right))V(y)\right|

By sub-multiplicativity,

A 1 = ‖ softmax  ( Q  K  ( y ′ ) T d k )  ( V  ( y ) − V  ( y ′ ) ) ‖ F ≤ ‖ softmax  ( Q  K  ( y ′ ) T d k ) ‖ F  ‖ V  ( y ) − V  ( y ′ ) ‖ F . {A\_{1}}=\left|\mathrm{softmax}!\left(\frac{QK(y^{\prime})^{T}}{\sqrt{d\_{k}}}\right)(V(y)-V(y^{\prime}))\right|

{F}\leq\left|\mathrm{softmax}!\left(\frac{QK(y^{\prime})^{T}}{\sqrt{d

{k}}}\right)\right|

{F},\left|V(y)-V(y^{\prime})\right|

Since softmax  ( Q  K  ( y ′ ) T d k ) \mathrm{softmax}!\left(\frac{QK(y^{\prime})^{T}}{\sqrt{d\_{k}}}\right) is a softmax weight matrix, ‖ softmax  ( Q  K  ( y ′ ) T d k ) ‖ F \left|\mathrm{softmax}!\left(\frac{QK(y^{\prime})^{T}}{\sqrt{d\_{k}}}\right)\right|\_{F} is bounded on the region of interest; absorb this into a constant. Using

Theorem B.3

https://arxiv.org/html/2602.04898v2#A2.Thmtheorem3

A 1 ≤ ‖ softmax  ( Q  K  ( y ′ ) T d k )  ( V  ( y ) − V  ( y ′ ) ) ‖ F ≤ softmax  ( Q  K  ( y ′ ) T d k )  ε sem  ‖ 𝐖 v ‖ F . A\_{1}\leq\left|\mathrm{softmax}!\left(\frac{QK(y^{\prime})^{T}}{\sqrt{d\_{k}}}\right)(V(y)-V(y^{\prime}))\right|

{F}\leq\mathrm{softmax}!\left(\frac{QK(y^{\prime})^{T}}{\sqrt{d

{k}}}\right),\varepsilon\_{\mathrm{sem}},|\mathbf{W}

Let S  ( y ′ ) = softmax  ( Q  K  ( y ′ ) T d k ) ∈ ℝ n q × n k S(y^{\prime})=\mathrm{softmax}!\left(\frac{QK(y^{\prime})^{T}}{\sqrt{d\_{k}}}\right)\in\mathbb{R}^{n\_{q}\times n\_{k}} be the row-wise softmax weight matrix. Then each row s i s\_{i} of S  ( y ′ ) S(y^{\prime}) is a probability vector: s i ≥ 0 s\_{i}\geq 0 and ‖ s i ‖ 1 = ∑ j = 1 n k ( s i ) j = 1 |s\_{i}|

{j=1}^{n\_{k}}(s\_{i})

{j}=1 . Hence ‖ s i ‖ 2 ≤ ‖ s i ‖ 1 = 1 , |s

{1}=1, and therefore ‖ S  ( y ′ ) ‖ F 2 = ∑ i = 1 n q ‖ s i ‖ 2 2 ≤ ∑ i = 1 n q 1 = n q ⇒ ‖ S  ( y ′ ) ‖ F ≤ n q . |S(y^{\prime})|

{F}^{2}=\sum\_{i=1}^{n\_{q}}|s\_{i}|

{2}^{2}\leq\sum

{i=1}^{n\_{q}}1=n\_{q}\Rightarrow|S(y^{\prime})|

{F}\leq\sqrt{n

{q}}. Plugging this and C 1 = n q C\_{1}=\sqrt{n\_{q}} into

https://arxiv.org/html/2602.04898v2#A2.E8

A 1 ≤ ‖ S  ( y ′ ) ‖ F  ‖ V  ( y ) − V  ( y ′ ) ‖ F ≤ n q  ε sem  ‖ 𝐖 v ‖ F . A\_{1}\leq|S(y^{\prime})|

{F},|V(y)-V(y^{\prime})|

{F}\leq\sqrt{n\_{q}},\varepsilon\_{\mathrm{sem}},|\mathbf{W}

By the sub-multiplicativity of the Frobenius norm,

A 2 ≤ ‖ softmax  ( Q  K  ( y ) T d k ) − softmax  ( Q  K  ( y ′ ) T d k ) ‖ F ⏟ B 1  ‖ V  ( y ) ‖ F ⏟ B 2 . A\_{2}\leq\underbrace{\left|\mathrm{softmax}!\left(\frac{QK(y)^{T}}{\sqrt{d\_{k}}}\right)-\mathrm{softmax}!\left(\frac{QK(y^{\prime})^{T}}{\sqrt{d\_{k}}}\right)\right|

{B\_{1}}\underbrace{|V(y)|

https://arxiv.org/html/2602.04898v2#A2.Thmtheorem2

B 1 = ‖ softmax  ( Q  K  ( y ) T d k ) − softmax  ( Q  K  ( y ′ ) T d k ) ‖ F ≤ L sm  ‖ Q  K  ( y ) T d k − Q  K  ( y ′ ) T d k ‖ F . B\_{1}=\left|\mathrm{softmax}!\left(\frac{QK(y)^{T}}{\sqrt{d\_{k}}}\right)-\mathrm{softmax}!\left(\frac{QK(y^{\prime})^{T}}{\sqrt{d\_{k}}}\right)\right|

{\mathrm{sm}},\left|\frac{QK(y)^{T}}{\sqrt{d\_{k}}}-\frac{QK(y^{\prime})^{T}}{\sqrt{d\_{k}}}\right|\_{F}.

Next, by the Frobenius sub-multiplicativity and using

Theorem B.3

https://arxiv.org/html/2602.04898v2#A2.Thmtheorem3

together with | Q | F ≤ B Q |Q|

{Q} , we obtain

‖ Q  K  ( y ) T d k − Q  K  ( y ′ ) T d k ‖ F = ‖ Q  ( K  ( y ) − K  ( y ′ ) ) T d k ‖ F ≤ 1 d k  ‖ Q ‖ F  ‖ K  ( y ) − K  ( y ′ ) ‖ F ≤ 1 d k  B Q  ε sem  ‖ 𝐖 k ‖ F . \left|\frac{QK(y)^{T}}{\sqrt{d\_{k}}}-\frac{QK(y^{\prime})^{T}}{\sqrt{d\_{k}}}\right|

{F}=\left|\frac{Q\big(K(y)-K(y^{\prime})\big)^{T}}{\sqrt{d

{k}}}\right|

{F}\leq\frac{1}{\sqrt{d

{F},|K(y)-K(y^{\prime})|

{F}\leq\frac{1}{\sqrt{d\_{k}}},B\_{Q},\varepsilon\_{\mathrm{sem}},|\mathbf{W}

Equation 11

https://arxiv.org/html/2602.04898v2#A2.E11

Equation 12

https://arxiv.org/html/2602.04898v2#A2.E12

B 1 ≤ L sm  B Q d k  ε sem  ‖ 𝐖 k ‖ F . B\_{1}\leq\frac{L\_{\mathrm{sm}}B\_{Q}}{\sqrt{d\_{k}}},\varepsilon\_{\mathrm{sem}},|\mathbf{W}

By definition of V  ( y ) V(y) , the sub-multiplicativity of the Frobenius norm, and

https://arxiv.org/html/2602.04898v2#A2.Thmtheorem2

B 2 = ‖ 𝒯  ( y )  𝐖 v ‖ F ≤ ‖ 𝒯  ( y ) ‖ F  ‖ 𝐖 v ‖ F ≤ B H  ‖ 𝐖 v ‖ F . B\_{2}=|\mathcal{T}(y)\mathbf{W}

{F}\leq|\mathcal{T}(y)|

{F}|\mathbf{W}

{H}|\mathbf{W}

Substituting

Equation 13

https://arxiv.org/html/2602.04898v2#A2.E13

Equation 14

https://arxiv.org/html/2602.04898v2#A2.E14

Equation 10

https://arxiv.org/html/2602.04898v2#A2.E10

, it follows that

A 2 ≤ ( L sm  B Q d k  B H )  ε sem  ‖ 𝐖 k ‖ F  ‖ 𝐖 v ‖ F . A\_{2}\leq\left(\frac{L\_{\mathrm{sm}}B\_{Q}}{\sqrt{d\_{k}}},B\_{H}\right)\varepsilon\_{\mathrm{sem}},|\mathbf{W}

{F},|\mathbf{W}

Absorb the prefactor L sm  B Q d k  B H \frac{L\_{\mathrm{sm}}B\_{Q}}{\sqrt{d\_{k}}},B\_{H} into C 2 C\_{2} . Plugging

https://arxiv.org/html/2602.04898v2#A2.E9

Equation 15

https://arxiv.org/html/2602.04898v2#A2.E15

https://arxiv.org/html/2602.04898v2#A2.E6

‖ A  ( y ) − A  ( y ′ ) ‖ F ≤ ε sem  ( C 1  ‖ 𝐖 v ‖ F + C 2  ‖ 𝐖 k ‖ F  ‖ 𝐖 v ‖ F ) . |A(y)-A(y^{\prime})|

{F}\leq\varepsilon

{\mathrm{sem}}\Big(C\_{1}|\mathbf{W}

{F}+C\_{2}|\mathbf{W}

{F}|\mathbf{W}

The derived bound formalizes semantic generalization in the cross-attention mechanism. Under encoder-level semantic stability, the cross-attention output varies smoothly with respect to semantically equivalent prompts. The bound shows that this variation scales linearly with ε sem \varepsilon\_{\mathrm{sem}} , with multiplicative factors determined solely by the norms of the key and value projection matrices. Consequently, semantic invariance at the encoder level induces bounded variation in the attention output, implying that the model responds consistently to semantically equivalent prompts despite surface-level differences. ∎

Appendix C Semantic Proof of Convergence

The distillation objective consists of two components, corresponding to the key and value representations, respectively: L = α k  L k  ( W k b  d ) + α v  L v  ( W v b  d ) L=\alpha\_{k},L\_{k}(W\_{k}^{bd})+\alpha\_{v},L\_{v}(W\_{v}^{bd}) . At iteration t t , we sample indices ( i t , j t ) (i\_{t},j\_{t}) for the semantic trigger substring and the regularization substring. The sampled losses correspond to the single-step distillation objectives and are defined as

ℓ t ( k )  ( W k b  d ) \displaystyle\ell\_{t}^{(k)}(W\_{k}^{bd})

= ‖ W k b  d  c t  r ( i t ) − W k c  l  e  a  n  c t  a ‖ 2 2 + λ reg  ‖ W k b  d  c r  e  g ( j t ) − W k c  l  e  a  n  c r  e  g ( j t ) ‖ 2 2 , \displaystyle=|W\_{k}^{bd},c\_{tr}^{(i\_{t})}-W\_{k}^{clean}c\_{ta}|

{2}^{2}+\lambda

{\mathrm{reg}},|W\_{k}^{bd},c\_{reg}^{(j\_{t})}-W\_{k}^{clean}c\_{reg}^{(j\_{t})}|\_{2}^{2},

ℓ t ( v )  ( W v b  d ) \displaystyle\ell\_{t}^{(v)}(W\_{v}^{bd})

= ‖ W v b  d  c t  r ( i t ) − W v c  l  e  a  n  c t  a ‖ 2 2 + λ reg  ‖ W v b  d  c r  e  g ( j t ) − W v c  l  e  a  n  c r  e  g ( j t ) ‖ 2 2 . \displaystyle=|W\_{v}^{bd},c\_{tr}^{(i\_{t})}-W\_{v}^{clean}c\_{ta}|

{2}^{2}+\lambda

{\mathrm{reg}},|W\_{v}^{bd},c\_{reg}^{(j\_{t})}-W\_{v}^{clean}c\_{reg}^{(j\_{t})}|\_{2}^{2}.

The total loss is

ℓ t total  ( W k , W v ) = α k  ℓ t ( k )  ( W k ) + α v  ℓ t ( v )  ( W v ) . \ell\_{t}^{\mathrm{total}}(W\_{k},W\_{v})=\alpha\_{k},\ell\_{t}^{(k)}(W\_{k})+\alpha\_{v},\ell\_{t}^{(v)}(W\_{v}).

We define the optimal parameters as W k ∗ = arg  min W k b  d  ∑ t = 1 T ℓ t ( k )  ( W k b  d ) W\_{k}^{

}=\arg\min\_{W\_{k}^{bd}}\sum\_{t=1}^{T}\ell\_{t}^{(k)}(W\_{k}^{bd}) , W v ∗ = arg  min W v b  d  ∑ t = 1 T ℓ t ( v )  ( W v b  d ) W\_{v}^{

}=\arg\min\_{W\_{v}^{bd}}\sum\_{t=1}^{T}\ell\_{t}^{(v)}(W\_{v}^{bd}) . Accordingly, our analysis bounds the average optimality gap with respect to the hindsight minimizers W k ∗ = arg  min W k  ∑ t = 1 T ℓ t ( k )  ( W k ) W\_{k}^{

}=\arg\min\_{W\_{k}}\sum\_{t=1}^{T}\ell\_{t}^{(k)}(W\_{k}) and W v ∗ = arg  min W v  ∑ t = 1 T ℓ t ( v )  ( W v ) W\_{v}^{

}=\arg\min\_{W\_{v}}\sum\_{t=1}^{T}\ell\_{t}^{(v)}(W\_{v}) induced by the sampled loss sequence. We next analyze the convergence of the proposed distillation procedure. Our analysis is conducted under the following assumptions.

Assumption C.1.

For bounded variables on w w , for all w t , w ∗ w\_{t},w^{

} , assume that ‖ w t − w ∗ ‖ ∞ ≤ D |w\_{t}-w^{

{\infty}\leq D , i.e. | w t , i − w i ∗ | ≤ D i |w

{t,i}-w\_{i}^{

}|\leq D\_{i} for all i i , where w t , w ∗ ∈ ℝ d w\_{t},w^{

}\in\mathbb{R}^{d} .

Assumption C.2.

For bounded gradients, for all t , i t,i , | g t , i | ≤ G i |g\_{t,i}|\leq G\_{i} , where g t , i g\_{t,i} denotes the i i -th coordinate of the gradient at iteration t t . The constant G G includes the effect of λ reg \lambda\_{\mathrm{reg}} .

Assumption C.3.

For all t , i t,i , assume that the effective denominator used in AMSGrad satisfies v ^ t , i + ϵ ≥ v ¯ > 0 \sqrt{\hat{v}

{t,i}}+\epsilon\geq\underline{v}>0 , with ϵ > 0 \epsilon>0 . For each i i , the AMSGrad second-moment estimate v ^ t , i \hat{v}

{t,i} is non-decreasing in t t .

Theorem C.4.

Suppose that

https://arxiv.org/html/2602.04898v2#A3.Thmtheorem1

https://arxiv.org/html/2602.04898v2#A3.Thmtheorem3

hold, i.e., the parameter domain has bounded diameter D D , the gradients are coordinate-wise bounded by G G , and the second-moment estimates v ^ t , i \hat{v}

{t,i} produced by AMSGrad satisfy v ^ t , i + ϵ ≥ v ¯ > 0 \sqrt{\hat{v}

{t,i}}+\epsilon\geq\underline{v}>0 and are non-decreasing in t t for all i ∈ { 1 , … , d } i\in{1,\dots,d} . Let AMSGrad be run with constant momentum parameters β 1 ∈ \[ 0 , 1 ) \beta\_{1}\in\[0,1) , β 2 ∈ \[ 0 , 1 ) \beta\_{2}\in\[0,1) and a constant step size α T ≡ γ t ≡ γ > 0 \alpha\_{T}\equiv\gamma\_{t}\equiv\gamma>0 . Assume further that β 1 2 < β 2 \beta\_{1}^{2}<\beta\_{2} . Define C  ( β 1 , β 2 ) ≜ β 2 ( 1 − β 2 )  ( β 2 − β 1 2 ) . C(\beta\_{1},\beta\_{2})\triangleq\frac{\beta\_{2}}{(1-\beta\_{2})(\beta\_{2}-\beta\_{1}^{2})}. Then for any optimal solution w ∗ w^{\*} , the average optimality gap satisfies

1 T  ∑ t = 1 T ( ℓ t  ( w t ) − ℓ t  ( w ∗ ) ) ≤ d  D 2  G 2  T  γ  ( 1 − β 1 ) + 2  d  D  G  β 1 ( 1 − β 1 )  T + d  G  γ 2  ( 1 − β 1 )  C  ( β 1 , β 2 ) . \frac{1}{T}\sum\_{t=1}^{T}\bigl(\ell\_{t}(w\_{t})-\ell\_{t}(w^{\*})\bigr)\leq\frac{d,D^{2},G}{2T,\gamma,(1-\beta\_{1})}+\frac{2d,D,G,\beta\_{1}}{(1-\beta\_{1})\sqrt{T}}+\frac{d,G,\gamma}{2(1-\beta\_{1})},C(\beta\_{1},\beta\_{2}).

In particular, the bound implies 𝒪  ( 1 T  γ + 1 T + γ ) . \mathcal{O}!\left(\frac{1}{T\gamma}+\frac{1}{\sqrt{T}}+\gamma\right).

Corollary C.5.

Under the assumptions of

Theorem C.4

https://arxiv.org/html/2602.04898v2#A3.Thmtheorem4

, suppose the average optimality gap admits the upper bound 1 T  ∑ t = 1 T ( ℓ t  ( w t ) − ℓ t  ( w ∗ ) ) ≤ C 1 T  γ + C 3 T + C 2  γ , \frac{1}{T}\sum\_{t=1}^{T}\bigl(\ell\_{t}(w\_{t})-\ell\_{t}(w^{

})\bigr)\leq\frac{C\_{1}}{T\gamma}+\frac{C\_{3}}{\sqrt{T}}+C\_{2},\gamma, where C 1 ≜ d  G  D 2 2  ( 1 − β 1 , 1 ) , C 3 ≜ 2  d  D  G  β 1 1 − β 1 , 1 , C 2 ≜ d  G 2  ( 1 − β 1 )  C  ( β 1 , β 2 ) , C\_{1}\triangleq\frac{dGD^{2}}{2(1-\beta\_{1,1})},\qquad C\_{3}\triangleq\frac{2dDG\beta\_{1}}{1-\beta\_{1,1}},\qquad C\_{2}\triangleq\frac{dG}{2(1-\beta\_{1})},C(\beta\_{1},\beta\_{2}), and C  ( β 1 , β 2 ) ≜ β 2 ( 1 − β 2 )  ( β 2 − β 1 2 ) . C(\beta\_{1},\beta\_{2})\triangleq\frac{\beta\_{2}}{(1-\beta\_{2})(\beta\_{2}-\beta\_{1}^{2})}. Then the bound is minimized (over γ > 0 \gamma>0 ) by choosing γ ∗ = C 1 C 2  T , \gamma^{

}=\sqrt{\frac{C\_{1}}{C\_{2},T}}, and with this choice we have min γ > 0  ( C 1 T  γ + C 3 T + C 2  γ ) ≤ C 3 T + 2  C 1  C 2 T . \min\_{\gamma>0}\left(\frac{C\_{1}}{T\gamma}+\frac{C\_{3}}{\sqrt{T}}+C\_{2},\gamma\right)\leq\frac{C\_{3}}{\sqrt{T}}+2\sqrt{\frac{C\_{1}C\_{2}}{T}}.

We analyze the convergence for a single component, as the total loss is a weighted sum of the key and value objectives. Fix one of { k , v } {k,v} and omit the superscript for notational simplicity. At each iteration t t , let W t W\_{t} denote the corresponding parameter matrix, and define its vectorized form as w t = vec  ( W t ) ∈ ℝ d w\_{t}=\mathrm{vec}(W\_{t})\in\mathbb{R}^{d} . Similarly, let W ∗ W^{

} denote the corresponding optimal parameter matrix, and define w ∗ = vec  ( W ∗ ) w^{

}=\mathrm{vec}(W^{

}) . Accordingly, we view the single-step loss ℓ t  ( ⋅ ) \ell\_{t}(\cdot) as a function of the vector w ∈ ℝ d w\in\mathbb{R}^{d} , corresponding to either the Key loss in Equation 16 or the Value loss in Equation 17. We define the gradient as g t = ∇ w ℓ t  ( w t ) g\_{t}=\nabla\_{w}\ell\_{t}(w\_{t}) , and let g t , i g\_{t,i} denote its i i -th coordinate. Since each ℓ t  ( ) \ell\_{t}() is a sum of squared norms, it is convex in w w . By the first-order condition for convex functions, we have ℓ t  ( w t ) − ℓ t  ( w ∗ ) ≤ ⟨ g t , w t − w ∗ ⟩ = ∑ i = 1 d g t , i  ( w t , i − w i ∗ ) \ell\_{t}(w\_{t})-\ell\_{t}(w^{

})\leq\langle g\_{t},w\_{t}-w^{

}\rangle=\sum\_{i=1}^{d}g\_{t,i}(w\_{t,i}-w\_{i}^{

}) . Summing over t = 1 , … , T t=1,\dots,T gives

∑ t = 1 T ( ℓ t  ( w t ) − ℓ t  ( w ∗ ) ) ≤ ∑ t = 1 T ∑ i = 1 d g t , i  ( w t , i − w i ∗ ) . \sum\_{t=1}^{T}\big(\ell\_{t}(w\_{t})-\ell\_{t}(w^{

})\big)\leq\sum\_{t=1}^{T}\sum\_{i=1}^{d}g\_{t,i}(w\_{t,i}-w\_{i}^{

Our theoretical analysis is conducted for the AMSGrad variant of Adam. To bound the inner-product term in

Equation 19

https://arxiv.org/html/2602.04898v2#A3.E19

, the AMSGrad update rule is exploited at the coordinate level. Fix a coordinate i ∈ { 1 , … , d } i\in{1,\dots,d} , under AMSGrad the update along this coordinate is given by w t + 1 , i = w t , i − γ t  m t , i v ^ t , i w\_{t+1,i}=w\_{t,i}-\gamma\_{t}\frac{m\_{t,i}}{\sqrt{\hat{v}\_{t,i}}} . By considering the squared distance to the optimum along coordinate i i , it follows that

( w t + 1 , i − w i ∗ ) 2 = ( ( w t , i − w i ∗ ) − γ t  m t , i v ^ t , i ) 2 . (w\_{t+1,i}-w\_{i}^{

})^{2}=\Bigl((w\_{t,i}-w\_{i}^{

})-\gamma\_{t}\frac{m\_{t,i}}{\sqrt{\hat{v}\_{t,i}}}\Bigr)^{2}.

Expanding the square and rearranging the terms in

Equation 20

https://arxiv.org/html/2602.04898v2#A3.E20

m t , i  ( w t , i − w i ∗ ) = v ^ t , i 2  γ t  ( ( w t , i − w i ∗ ) 2 − ( w t + 1 , i − w i ∗ ) 2 ) + γ t 2  m t , i 2 v ^ t , i . m\_{t,i}(w\_{t,i}-w\_{i}^{

})=\frac{\sqrt{\hat{v}{t,i}}}{2\gamma{t}}\Big((w\_{t,i}-w\_{i}^{

})^{2}-(w\_{t+1,i}-w\_{i}^{\*})^{2}\Big)+\frac{\gamma\_{t}}{2}\frac{m\_{t,i}^{2}}{\sqrt{\hat{v}\_{t,i}}}.

To express the gradient g t , i g\_{t,i} in terms of the momentum variables, the first-moment recursion of AMSGrad is given by m t , i = β 1 , t  m t − 1 , i + ( 1 − β 1 , t )  g t , i m\_{t,i}=\beta\_{1,t}m\_{t-1,i}+(1-\beta\_{1,t})g\_{t,i} , which yields g t , i = 1 1 − β 1 , t  m t , i − β 1 , t 1 − β 1 , t  m t − 1 , i g\_{t,i}=\frac{1}{1-\beta\_{1,t}}m\_{t,i}-\frac{\beta\_{1,t}}{1-\beta\_{1,t}}m\_{t-1,i} . Multiplying both sides by ( w t , i − w i ∗ ) (w\_{t,i}-w\_{i}^{

}) and substituting Equation 21 for the term m t , i  ( w t , i − w i ∗ ) m\_{t,i}(w\_{t,i}-w\_{i}^{

}) , it follows that

g t , i  ( w t , i − w i ∗ ) = v ^ t , i 2  γ t  ( 1 − β 1 , t )  ( ( w t , i − w i ∗ ) 2 − ( w t + 1 , i − w i ∗ ) 2 ) ⏟ A 1  − β 1 , t 1 − β 1 , t  m t − 1 , i  ( w t , i − w i ∗ ) ⏟ A 2 + γ t 2  ( 1 − β 1 , t )  m t , i 2 v ^ t , i ⏟ A 3 . g\_{t,i}(w\_{t,i}-w\_{i}^{

})=\underbrace{\frac{\sqrt{\hat{v}{t,i}}}{2\gamma{t}(1-\beta\_{1,t})}\Big((w\_{t,i}-w\_{i}^{

})^{2}-(w\_{t+1,i}-w\_{i}^{

})^{2}\Big)}{A{1}}\underbrace{-\frac{\beta\_{1,t}}{1-\beta\_{1,t}},m\_{t-1,i}(w\_{t,i}-w\_{i}^{

{2}}+\underbrace{\frac{\gamma\_{t}}{2(1-\beta\_{1,t})}\frac{m\_{t,i}^{2}}{\sqrt{\hat{v}

Substituting

Equation 22

https://arxiv.org/html/2602.04898v2#A3.E22

Equation 19

https://arxiv.org/html/2602.04898v2#A3.E19

, it follows that

∑ t = 1 T ( ℓ t  ( w t ) − ℓ t  ( w ∗ ) ) ≤ ∑ t = 1 T ∑ i = 1 d A 1 − ∑ t = 1 T ∑ i = 1 d A 2 + ∑ t = 1 T ∑ i = 1 d A 3 . \sum\_{t=1}^{T}(\ell\_{t}(w\_{t})-\ell\_{t}(w^{\*}))\leq\sum\_{t=1}^{T}\sum\_{i=1}^{d}A\_{1}-\sum\_{t=1}^{T}\sum\_{i=1}^{d}A\_{2}+\sum\_{t=1}^{T}\sum\_{i=1}^{d}A\_{3}.

We first bound the term A 1 A\_{1} in

Equation 22

https://arxiv.org/html/2602.04898v2#A3.E22

. Fix a parameter coordinate i ∈ { 1 , … , d } i\in{1,\dots,d} . Adopt the bias-corrected effective stepsize with learning rate α t > 0 \alpha\_{t}>0 , defined as γ t = α t 1 − ∏ s = 1 t β 1 , s \gamma\_{t};=;\frac{\alpha\_{t}}{1-\prod\_{s=1}^{t}\beta\_{1,s}} . With this definition, the coefficient appearing in A 1 A\_{1} can be written as 1 2  γ t  ( 1 − β 1 , t ) = 1 2  α t  1 − ∏ s = 1 t β 1 , s 1 − β 1 , t \frac{1}{2\gamma\_{t}(1-\beta\_{1,t})}=\frac{1}{2\alpha\_{t}}\frac{1-\prod\_{s=1}^{t}\beta\_{1,s}}{1-\beta\_{1,t}} . Moreover, by the standard inequality 1 − ∏ s = 1 T β 1 , s 1 − β 1 , T ≤ 1 1 − β 1 , 1 \frac{1-\prod\_{s=1}^{T}\beta\_{1,s}}{1-\beta\_{1,T}}\leq\frac{1}{1-\beta\_{1,1}} , the above coefficient admits a uniform upper bound independent of t t .

Using the expression of γ t \gamma\_{t} , it follows that

∑ t = 1 T A 1 = ∑ t = 1 T v ^ t , i  ( ( w t , i − w i ∗ ) 2 − ( w t + 1 , i − w i ∗ ) 2 ) 2  γ t  ( 1 − β 1 , t ) = ∑ t = 1 T v ^ t , i  ( 1 − ∏ s = 1 t β 1 , s )  ( ( w t , i − w i ∗ ) 2 − ( w t + 1 , i − w i ∗ ) 2 ) 2  α t  ( 1 − β 1 , t ) ≤ ∑ t = 1 T v ^ t , i  ( ( w t , i − w i ∗ ) 2 − ( w t + 1 , i − w i ∗ ) 2 ) 2  α t  ( 1 − β 1 , 1 ) . \begin{split}\sum\_{t=1}^{T}A\_{1}&=\sum\_{t=1}^{T}\frac{\sqrt{\hat{v}

{t,i}}\Big((w

{t,i}-w\_{i}^{

})^{2}-(w\_{t+1,i}-w\_{i}^{

})^{2}\Big)}{2\gamma\_{t}(1-\beta\_{1,t})}\ &=\sum\_{t=1}^{T}\frac{\sqrt{\hat{v}

{t,i}}\Big(1-\prod

{s=1}^{t}\beta\_{1,s}\Big)\Big((w\_{t,i}-w\_{i}^{

})^{2}-(w\_{t+1,i}-w\_{i}^{

})^{2}\Big)}{2\alpha\_{t}(1-\beta\_{1,t})}\ &\leq\sum\_{t=1}^{T}\frac{\sqrt{\hat{v}

{t,i}}\Big((w

{t,i}-w\_{i}^{

})^{2}-(w\_{t+1,i}-w\_{i}^{

})^{2}\Big)}{2\alpha\_{t}(1-\beta\_{1,1})}.\end{split}

Grouping terms with the same ( w t , i − w i ∗ ) 2 (w\_{t,i}-w\_{i}^{\*})^{2} yields

∑ t = 1 T A 1 ≤ ∑ t = 1 T v ^ t , i  ( ( w t , i − w i ∗ ) 2 − ( w t + 1 , i − w i ∗ ) 2 ) 2  α t  ( 1 − β 1 , 1 ) ≤ ∑ t = 1 T v ^ t , i  ( w t , i − w i ∗ ) 2 2  α t  ( 1 − β 1 , 1 ) − ∑ t = 1 T v ^ t , i  ( w t + 1 , i − w i ∗ ) 2 2  α t  ( 1 − β 1 , 1 ) = v ^ 1 , i  ( w 1 , i − w i ∗ ) 2 2  α 1  ( 1 − β 1 , 1 ) ⏟ B 1  − v ^ T , i  ( w T + 1 , i − w i ∗ ) 2 2  α T  ( 1 − β 1 , 1 ) ⏟ B 2 + ∑ t = 2 T ( w t , i − w i ∗ ) 2  ( v ^ t , i 2  α t  ( 1 − β 1 , 1 ) − v ^ t − 1 , i 2  α t − 1  ( 1 − β 1 , 1 ) ) ⏟ B 3 . \begin{split}\sum\_{t=1}^{T}A\_{1}&\leq\sum\_{t=1}^{T}\frac{\sqrt{\hat{v}

{t,i}}\Big((w

{t,i}-w\_{i}^{

})^{2}-(w\_{t+1,i}-w\_{i}^{

})^{2}\Big)}{2\alpha\_{t}(1-\beta\_{1,1})}\leq\sum\_{t=1}^{T}\frac{\sqrt{\hat{v}

{t,i}-w\_{i}^{

})^{2}}{2\alpha\_{t}(1-\beta\_{1,1})}-\sum\_{t=1}^{T}\frac{\sqrt{\hat{v}{t,i}}(w{t+1,i}-w\_{i}^{

})^{2}}{2\alpha\_{t}(1-\beta\_{1,1})}\ &=\underbrace{\frac{\sqrt{\hat{v}

{1,i}-w\_{i}^{

})^{2}}{2\alpha\_{1}(1-\beta\_{1,1})}}{B{1}};\underbrace{-;\frac{\sqrt{\hat{v}{T,i}}(w{T+1,i}-w\_{i}^{

})^{2}}{2\alpha\_{T}(1-\beta\_{1,1})}}

{2}};+;\underbrace{\sum\_{t=2}^{T}(w\_{t,i}-w\_{i}^{\*})^{2}\left(\frac{\sqrt{\hat{v}

{t,i}}}{2\alpha

{t}(1-\beta\_{1,1})}-\frac{\sqrt{\hat{v}

{t-1,i}}}{2\alpha

{t-1}(1-\beta\_{1,1})}\right)}

{3}}.\end{split}

https://arxiv.org/html/2602.04898v2#A3.Thmtheorem1

, it holds that ( w 1 , i − w i ∗ ) 2 ≤ D i 2 (w\_{1,i}-w\_{i}^{\*})^{2}\leq D^{2}\_{i} , which implies

B 1 = v ^ 1 , i  ( w 1 , i − w i ∗ ) 2 2  α 1  ( 1 − β 1 , 1 ) ≤ D i 2  v ^ 1 , i 2  α 1  ( 1 − β 1 , 1 ) . B\_{1}=\frac{\sqrt{\hat{v}

{1,i}-w\_{i}^{\*})^{2}}{2\alpha\_{1}(1-\beta\_{1,1})}\leq\frac{D^{2}

{i}\sqrt{\hat{v}

{1,i}}}{2\alpha\_{1}(1-\beta\_{1,1})}.

Since v ^ T , i ≥ 0 \hat{v}

{T,i}\geq 0 and ( w T + 1 , i − w i ∗ ) 2 ≥ 0 (w

{T+1,i}-w\_{i}^{\*})^{2}\geq 0 , it follows that

B 2 = − v ^ T , i  ( w T + 1 , i − w i ∗ ) 2 2  α T  ( 1 − β 1 , 1 ) ≤ 0 . B\_{2}=-\frac{\sqrt{\hat{v}

{T+1,i}-w\_{i}^{\*})^{2}}{2\alpha\_{T}(1-\beta\_{1,1})}\leq 0.

Suppose that the sequence { α t − 1  v ^ t , i } t ≥ 1 {\alpha\_{t}^{-1}\sqrt{\hat{v}

{t\geq 1} is non-decreasing, i.e., v ^ t , i α t ≥ v ^ t − 1 , i α t − 1 , ∀ t ≥ 2 \frac{\sqrt{\hat{v}

{t,i}}}{\alpha

{t}}\geq\frac{\sqrt{\hat{v}

{t-1,i}}}{\alpha

{t-1}},\forall,t\geq 2 , so that the difference term in B 3 B\_{3} is non-negative. Under

https://arxiv.org/html/2602.04898v2#A3.Thmtheorem1

, ( w t , i − w i ∗ ) 2 ≤ D i 2 (w\_{t,i}-w\_{i}^{\*})^{2}\leq D^{2}\_{i} for all t t , which yields

B 3 ≤ D i 2  ∑ t = 2 T ( v ^ t , i 2  α t  ( 1 − β 1 , 1 ) − v ^ t − 1 , i 2  α t − 1  ( 1 − β 1 , 1 ) ) = D i 2  ( v ^ T , i 2  α T  ( 1 − β 1 , 1 ) − v ^ 1 , i 2  α 1  ( 1 − β 1 , 1 ) ) . B\_{3}\leq D^{2}

{t=2}^{T}\left(\frac{\sqrt{\hat{v}

{t,i}}}{2\alpha

{t}(1-\beta\_{1,1})}-\frac{\sqrt{\hat{v}

{t-1,i}}}{2\alpha

{t-1}(1-\beta\_{1,1})}\right)=D^{2}

{i}\left(\frac{\sqrt{\hat{v}

{T,i}}}{2\alpha\_{T}(1-\beta\_{1,1})}-\frac{\sqrt{\hat{v}

{1,i}}}{2\alpha

{1}(1-\beta\_{1,1})}\right).

Equation 26

https://arxiv.org/html/2602.04898v2#A3.E26

Equation 27

https://arxiv.org/html/2602.04898v2#A3.E27

Equation 28

https://arxiv.org/html/2602.04898v2#A3.E28

, it follows that

∑ t = 1 T A 1 ≤ D i 2  v ^ 1 , i 2  α 1  ( 1 − β 1 , 1 ) + D i 2  ( v ^ T , i 2  α T  ( 1 − β 1 , 1 ) − v ^ 1 , i 2  α 1  ( 1 − β 1 , 1 ) ) ≤ D i 2  v ^ T , i 2  α T  ( 1 − β 1 , 1 ) . \sum\_{t=1}^{T}A\_{1}\leq\frac{D^{2}

{i}\sqrt{\hat{v}

{1,i}}}{2\alpha\_{1}(1-\beta\_{1,1})}+D^{2}

{i}\left(\frac{\sqrt{\hat{v}

{T,i}}}{2\alpha\_{T}(1-\beta\_{1,1})}-\frac{\sqrt{\hat{v}

{1,i}}}{2\alpha

{1}(1-\beta\_{1,1})}\right)\leq\frac{D^{2}

{i}\sqrt{\hat{v}

{T,i}}}{2\alpha\_{T}(1-\beta\_{1,1})}.

Finally, under

https://arxiv.org/html/2602.04898v2#A3.Thmtheorem2

, v t , i ≤ G i 2 v\_{t,i}\leq G^{2}

{i} for all t t , and hence v ^ T , i = max 1 ≤ s ≤ T  v s , i ≤ G i 2 \hat{v}

{T,i}=\max\_{1\leq s\leq T}v\_{s,i}\leq G^{2}\_{i} by

https://arxiv.org/html/2602.04898v2#A3.Thmtheorem3

. Therefore,

∑ t = 1 T A 1 ≤ D i 2  v ^ T , i 2  α T  ( 1 − β 1 , 1 ) ≤ D i 2  G 2  α T  ( 1 − β 1 , 1 ) . \sum\_{t=1}^{T}A\_{1}\leq\frac{D^{2}

{i}\sqrt{\hat{v}

{T,i}}}{2\alpha\_{T}(1-\beta\_{1,1})}\leq\frac{D^{2}

{i}G}{2\alpha

{T}(1-\beta\_{1,1})}.

https://arxiv.org/html/2602.04898v2#A3.Thmtheorem1

, it holds that | w t , i − w i ∗ | ≤ D i |w\_{t,i}-w\_{i}^{\*}|\leq D\_{i} , and hence

A 2 = − β 1 , t 1 − β 1 , t  m t − 1 , i  ( w t , i − w i ∗ ) = β 1 , t 1 − β 1 , t  m t − 1 , i  ( − ( w t , i − w i ∗ ) ) ≤ β 1 , t 1 − β 1 , t  | m t − 1 , i |  D i . A\_{2}=-\frac{\beta\_{1,t}}{1-\beta\_{1,t}},m\_{t-1,i}(w\_{t,i}-w\_{i}^{

})=\frac{\beta\_{1,t}}{1-\beta\_{1,t}},m\_{t-1,i}\big(-(w\_{t,i}-w\_{i}^{

})\big)\leq\frac{\beta\_{1,t}}{1-\beta\_{1,t}}|m\_{t-1,i}|D\_{i}.

From the first-moment update m t , i = β 1 , t  m t − 1 , i + ( 1 − β 1 , t )  g t , i m\_{t,i}=\beta\_{1,t}m\_{t-1,i}+(1-\beta\_{1,t})g\_{t,i} , unrolling the recursion and using initialization m 0 , i = 0 m\_{0,i}=0 gives m t , i = ∑ s = 1 t ( 1 − β 1 , s )  ( ∏ r = s + 1 t β 1 , r )  g s , i m\_{t,i}=\sum\_{s=1}^{t}(1-\beta\_{1,s})\Big(\prod\_{r=s+1}^{t}\beta\_{1,r}\Big)g\_{s,i} . Under

https://arxiv.org/html/2602.04898v2#A3.Thmtheorem2

, | g s , i | ≤ G i |g\_{s,i}|\leq G\_{i} for all s , i s,i , which implies

| m t , i | ≤ ∑ s = 1 t ( 1 − β 1 , s )  ( ∏ r = s + 1 t β 1 , r )  | g s , i | ≤ G i  ∑ s = 1 t ( 1 − β 1 , s )  ( ∏ r = s + 1 t β 1 , r ) = G i  ( 1 − ∏ r = 1 t β 1 , r ) ≤ G i . |m\_{t,i}|\leq\sum\_{s=1}^{t}(1-\beta\_{1,s})\Big(\prod\_{r=s+1}^{t}\beta\_{1,r}\Big)|g\_{s,i}|\leq G\_{i}\sum\_{s=1}^{t}(1-\beta\_{1,s})\Big(\prod\_{r=s+1}^{t}\beta\_{1,r}\Big)=G\_{i}\Big(1-\prod\_{r=1}^{t}\beta\_{1,r}\Big)\leq G\_{i}.

Substituting

Equation 32

https://arxiv.org/html/2602.04898v2#A3.E32

Equation 31

https://arxiv.org/html/2602.04898v2#A3.E31

, we obtain | A 2 | ≤ β 1 , t 1 − β 1 , t  D i  G i |A\_{2}|\leq\frac{\beta\_{1,t}}{1-\beta\_{1,t}}D\_{i}G\_{i} . Therefore, it follows that

∑ t = 1 T A 2 ≤ ∑ t = 1 T β 1 , t 1 − β 1 , t  D i  G i = D i  G i  ∑ t = 1 T β 1 , t 1 − β 1 , t . \sum\_{t=1}^{T}A\_{2}\leq\sum\_{t=1}^{T}\frac{\beta\_{1,t}}{1-\beta\_{1,t}}D\_{i}G\_{i}=D\_{i}G\_{i}\sum\_{t=1}^{T}\frac{\beta\_{1,t}}{1-\beta\_{1,t}}.

https://arxiv.org/html/2602.04898v2#A3.Thmtheorem3

, it holds that v ^ t , i ≥ v t , i \hat{v}

{t,i}\geq v

{t,i} , and thus m t , i 2 v ^ t , i ≤ m t , i 2 v t , i \frac{m\_{t,i}^{2}}{\sqrt{\hat{v}

{t,i}}};\leq;\frac{m

{t,i}^{2}}{\sqrt{v\_{t,i}}} . Expanding the first-moment estimate (with time-varying β 1 , t \beta\_{1,t} ) gives

m t , i = ∑ s = 1 t ( 1 − β 1 , s )  ( ∏ r = s + 1 t β 1 , r )  g s , i , m\_{t,i}=\sum\_{s=1}^{t}(1-\beta\_{1,s})\Big(\prod\_{r=s+1}^{t}\beta\_{1,r}\Big),g\_{s,i},

and recall that the second-moment exponential moving average satisfies

v t , i = ( 1 − β 2 )  ∑ s = 1 t β 2 t − s  g s , i 2 . v\_{t,i}=(1-\beta\_{2})\sum\_{s=1}^{t}\beta\_{2}^{t-s}g\_{s,i}^{2}.

Unrolling the recursion in the first-moment update

Equation 34

https://arxiv.org/html/2602.04898v2#A3.E34

m t , i = ∑ s = 1 t ( 1 − β 1 , s )  ( ∏ r = s + 1 t β 1 , r ) ( 1 − β 2 )  β 2 t − s  ( 1 − β 2 )  β 2 t − s  g s , i . m\_{t,i}=\sum\_{s=1}^{t}\frac{(1-\beta\_{1,s})\big(\prod\_{r=s+1}^{t}\beta\_{1,r}\big)}{\sqrt{(1-\beta\_{2})\beta\_{2}^{t-s}}}\sqrt{(1-\beta\_{2})\beta\_{2}^{t-s}},g\_{s,i}.

Applying Cauchy–Schwarz to

Equation 36

https://arxiv.org/html/2602.04898v2#A3.E36

and combining

Equation 35

https://arxiv.org/html/2602.04898v2#A3.E35

m t , i 2 ≤ ( ∑ s = 1 t ( 1 − β 1 , s ) 2  ( ∏ r = s + 1 t β 1 , r ) 2 ( 1 − β 2 )  β 2 t − s )  ( ∑ s = 1 t ( 1 − β 2 )  β 2 t − s  g s , i 2 ) = ∑ s = 1 t ( 1 − β 1 , s ) 2  ( ∏ r = s + 1 t β 1 , r ) 2 ( 1 − β 2 )  β 2 t − s  v t , i . \begin{split}m\_{t,i}^{2}\leq;\left(\sum\_{s=1}^{t}\frac{(1-\beta\_{1,s})^{2}\big(\prod\_{r=s+1}^{t}\beta\_{1,r}\big)^{2}}{(1-\beta\_{2})\beta\_{2}^{t-s}}\right)\left(\sum\_{s=1}^{t}(1-\beta\_{2})\beta\_{2}^{t-s}g\_{s,i}^{2}\right)=\sum\_{s=1}^{t}\frac{(1-\beta\_{1,s})^{2}\big(\prod\_{r=s+1}^{t}\beta\_{1,r}\big)^{2}}{(1-\beta\_{2})\beta\_{2}^{t-s}}v\_{t,i}.\end{split}

Equation 37

https://arxiv.org/html/2602.04898v2#A3.E37

by v t , i \sqrt{v\_{t,i}} yields m t , i 2 v ^ t , i ≤ ( ∑ s = 1 t ( 1 − β 1 , s ) 2  ( ∏ r = s + 1 t β 1 , r ) 2 ( 1 − β 2 )  β 2 t − s )  v t , i \frac{m\_{t,i}^{2}}{\sqrt{\hat{v}

{t,i}}};\leq;\Big(\sum

{s=1}^{t}\frac{(1-\beta\_{1,s})^{2}\big(\prod\_{r=s+1}^{t}\beta\_{1,r}\big)^{2}}{(1-\beta\_{2})\beta\_{2}^{t-s}}\Big)\sqrt{v\_{t,i}} . Finally, under

https://arxiv.org/html/2602.04898v2#A3.Thmtheorem2

, it holds that | g s , i | ≤ G i |g\_{s,i}|\leq G\_{i} for all s , i s,i , and hence

Equation 35

https://arxiv.org/html/2602.04898v2#A3.E35

implies v t , i ≤ ( 1 − β 2 )  ∑ s = 1 t β 2 t − s  G i 2 ≤ G i 2 v\_{t,i}\leq(1-\beta\_{2})\sum\_{s=1}^{t}\beta\_{2}^{t-s}G^{2}

{i}\leq G^{2}

{i} , which yields

∑ t = 1 T A 3 \displaystyle\sum\_{t=1}^{T}A\_{3}

≤ ∑ t = 1 T γ t 2  ( 1 − β 1 , t )  ( ∑ s = 1 t ( 1 − β 1 , s ) 2  ( ∏ r = s + 1 t β 1 , r ) 2 ( 1 − β 2 )  β 2 t − s )  v t , i \displaystyle\leq\sum\_{t=1}^{T}\frac{\gamma\_{t}}{2(1-\beta\_{1,t})}\left(\sum\_{s=1}^{t}\frac{(1-\beta\_{1,s})^{2}\big(\prod\_{r=s+1}^{t}\beta\_{1,r}\big)^{2}}{(1-\beta\_{2})\beta\_{2}^{t-s}}\right)\sqrt{v\_{t,i}}

≤ G i  ∑ t = 1 T γ t 2  ( 1 − β 1 , t )  ( ∑ s = 1 t ( 1 − β 1 , s ) 2  ( ∏ r = s + 1 t β 1 , r ) 2 ( 1 − β 2 )  β 2 t − s ) . \displaystyle\leq G\_{i}\sum\_{t=1}^{T}\frac{\gamma\_{t}}{2(1-\beta\_{1,t})}\left(\sum\_{s=1}^{t}\frac{(1-\beta\_{1,s})^{2}\big(\prod\_{r=s+1}^{t}\beta\_{1,r}\big)^{2}}{(1-\beta\_{2})\beta\_{2}^{t-s}}\right).

Substituting

Equation 30

https://arxiv.org/html/2602.04898v2#A3.E30

Equation 33

https://arxiv.org/html/2602.04898v2#A3.E33

Equation 38

https://arxiv.org/html/2602.04898v2#A3.E38

Equation 23

https://arxiv.org/html/2602.04898v2#A3.E23

, we obtain

∑ t = 1 T ( ℓ t  ( w t ) − ℓ t  ( w ∗ ) ) \displaystyle\sum\_{t=1}^{T}\bigl(\ell\_{t}(w\_{t})-\ell\_{t}(w^{\*})\bigr)

≤ ∑ i = 1 d D i 2  G i 2  α T  ( 1 − β 1 , 1 ) + ( ∑ i = 1 d D i  G i )  ( ∑ t = 1 T β 1 , t 1 − β 1 , t ) \displaystyle\leq\sum\_{i=1}^{d}\frac{D^{2}

{i}}{2\alpha\_{T}(1-\beta\_{1,1})}+\left(\sum\_{i=1}^{d}D\_{i}G\_{i}\right)\left(\sum\_{t=1}^{T}\frac{\beta\_{1,t}}{1-\beta\_{1,t}}\right)

∑ i = 1 d \[ G i  ∑ t = 1 T γ t 2  ( 1 − β 1 , t )  ( ∑ s = 1 t ( 1 − β 1 , s ) 2  ( ∏ r = s + 1 t β 1 , r ) 2 ( 1 − β 2 )  β 2 t − s ) \] . \displaystyle+\sum\_{i=1}^{d}\left\[G\_{i}\sum\_{t=1}^{T}\frac{\gamma\_{t}}{2(1-\beta\_{1,t})}\left(\sum\_{s=1}^{t}\frac{(1-\beta\_{1,s})^{2}\Big(\prod\_{r=s+1}^{t}\beta\_{1,r}\Big)^{2}}{(1-\beta\_{2})\beta\_{2}^{t-s}}\right)\right\].

Assume that β 1 , t = β 1 t ∈ ( 0 , 1 ) , ∀ t , \beta\_{1,t}=\frac{\beta\_{1}}{\sqrt{t}}\in(0,1),\ \forall,t, and it is non-increasing with the iteration index, i.e., β 1 , 1 ≥ β 1 , 2 ≥ ⋯ ≥ β 1 , T \beta\_{1,1}\geq\beta\_{1,2}\geq\cdots\geq\beta\_{1,T} . Therefore, it follows that ( ∑ i = 1 d D i  G i )  ( ∑ t = 1 T β 1 , t 1 − β 1 , t ) ≤ ( ∑ i = 1 d D i  G i )  ( 1 1 − β 1 , 1  ∑ t = 1 T β 1 , t ) \left(\sum\_{i=1}^{d}D\_{i}G\_{i}\right)\left(\sum\_{t=1}^{T}\frac{\beta\_{1,t}}{1-\beta\_{1,t}}\right)\leq\left(\sum\_{i=1}^{d}D\_{i}G\_{i}\right)\left(\frac{1}{1-\beta\_{1,1}}\sum\_{t=1}^{T}\beta\_{1,t}\right) , where ∑ t = 1 T β 1 , t = β 1  ∑ t = 1 T 1 t ≤ β 1  ( 1 + ∫ 1 T 1 x  𝑑 x ) = β 1  ( 1 + 2  ( T − 1 ) ) ≤ 2  β 1  T \sum\_{t=1}^{T}\beta\_{1,t}=\beta\_{1}\sum\_{t=1}^{T}\frac{1}{\sqrt{t}}\leq\beta\_{1}\left(1+\int\_{1}^{T}\frac{1}{\sqrt{x}},dx\right)=\beta\_{1}\left(1+2(\sqrt{T}-1)\right)\leq 2\beta\_{1}\sqrt{T} . Then ∏ r = s + 1 t β 1 , r ≤ ( β 1 , 1 ) t − s = β 1 t − s \prod\_{r=s+1}^{t}\beta\_{1,r}\leq(\beta\_{1,1})^{t-s}=\beta\_{1}^{,t-s} and ( 1 − β 1 , s ) 2 ≤ 1 (1-\beta\_{1,s})^{2}\leq 1 . Hence

( ∑ s = 1 t ( 1 − β 1 , s ) 2  ( ∏ r = s + 1 t β 1 , r ) 2 ( 1 − β 2 )  β 2 t − s ) ≤ ∑ s = 1 t β 1 2  ( t − s ) ( 1 − β 2 )  β 2 t − s = 1 1 − β 2  ∑ k = 0 t − 1 ( β 1 2 β 2 ) k . \left(\sum\_{s=1}^{t}\frac{(1-\beta\_{1,s})^{2}\Big(\prod\_{r=s+1}^{t}\beta\_{1,r}\Big)^{2}}{(1-\beta\_{2})\beta\_{2}^{t-s}}\right)\leq\sum\_{s=1}^{t}\frac{\beta\_{1}^{2(t-s)}}{(1-\beta\_{2})\beta\_{2}^{t-s}}=\frac{1}{1-\beta\_{2}}\sum\_{k=0}^{t-1}\left(\frac{\beta\_{1}^{2}}{\beta\_{2}}\right)^{k}.

Assume β 1 2 < β 2 \beta\_{1}^{2}<\beta\_{2} , the geometric series is bounded by

( ∑ s = 1 t ( 1 − β 1 , s ) 2  ( ∏ r = s + 1 t β 1 , r ) 2 ( 1 − β 2 )  β 2 t − s ) ≤ ( 1 1 − β 2 )  ( 1 1 − β 1 2 β 2 ) = β 2 ( 1 − β 2 )  ( β 2 − β 1 2 ) . \left(\sum\_{s=1}^{t}\frac{(1-\beta\_{1,s})^{2}\Big(\prod\_{r=s+1}^{t}\beta\_{1,r}\Big)^{2}}{(1-\beta\_{2})\beta\_{2}^{t-s}}\right)\leq\left(\frac{1}{1-\beta\_{2}}\right)\left(\frac{1}{1-\frac{\beta\_{1}^{2}}{\beta\_{2}}}\right)=\frac{\beta\_{2}}{(1-\beta\_{2})(\beta\_{2}-\beta\_{1}^{2})}.

Substituting

Equation 40

https://arxiv.org/html/2602.04898v2#A3.E40

Equation 39

https://arxiv.org/html/2602.04898v2#A3.E39

, and using the bound ∑ i = 1 d G i ≤ d  G \sum\_{i=1}^{d}G\_{i}\leq dG , we further define the constant C  ( β 1 , β 2 ) ≜ β 2 ( 1 − β 2 )  ( β 2 − β 1 2 ) C(\beta\_{1},\beta\_{2})\triangleq\frac{\beta\_{2}}{(1-\beta\_{2})(\beta\_{2}-\beta\_{1}^{2})} , which depends only on the momentum parameters and is finite whenever β 1 2 < β 2 \beta\_{1}^{2}<\beta\_{2} . Hence, we obtain

∑ t = 1 T ( ℓ t  ( w t ) − ℓ t  ( w ∗ ) ) ≤ d  D 2  G 2  α T  ( 1 − β 1 ) + 2  d  D  G  β 1  T 1 − β 1 + ∑ t = 1 T γ t 2  ( 1 − β 1 )  d  G  C  ( β 1 , β 2 ) . \sum\_{t=1}^{T}\bigl(\ell\_{t}(w\_{t})-\ell\_{t}(w^{\*})\bigr)\leq\frac{dD^{2}G}{2\alpha\_{T}(1-\beta\_{1})}+\frac{2dDG\beta\_{1}\sqrt{T}}{1-\beta\_{1}}+\sum\_{t=1}^{T}\frac{\gamma\_{t}}{2(1-\beta\_{1})}dGC(\beta\_{1},\beta\_{2}).

In particular, if α T ≡ γ t ≡ γ \alpha\_{T}\equiv\gamma\_{t}\equiv\gamma is a constant step size, then

∑ t = 1 T ( ℓ t  ( w t ) − ℓ t  ( w ∗ ) ) ≤ d  D 2  G 2  γ  ( 1 − β 1 ) + 2  d  D  G  β 1  T 1 − β 1 + T  d  G  γ 2  ( 1 − β 1 )  C  ( β 1 , β 2 ) . \sum\_{t=1}^{T}\bigl(\ell\_{t}(w\_{t})-\ell\_{t}(w^{\*})\bigr)\leq\frac{dD^{2}G}{2\gamma(1-\beta\_{1})}+\frac{2dDG\beta\_{1}\sqrt{T}}{1-\beta\_{1}}+T\frac{dG\gamma}{2(1-\beta\_{1})}C(\beta\_{1},\beta\_{2}).

Dividing both sides by T T yields the average optimality gap bound

1 T  ∑ t = 1 T ( ℓ t  ( w t ) − ℓ t  ( w ∗ ) ) ≤ d  D 2  G 2  T  γ  ( 1 − β 1 ) + 2  d  D  G  β 1 ( 1 − β 1 )  T + d  G  γ 2  ( 1 − β 1 )  C  ( β 1 , β 2 ) = O  ( 1 T  γ + 1 T + γ ) . \frac{1}{T}\sum\_{t=1}^{T}\bigl(\ell\_{t}(w\_{t})-\ell\_{t}(w^{\*})\bigr)\leq\frac{dD^{2}G}{2T\gamma(1-\beta\_{1})}+\frac{2dDG\beta\_{1}}{(1-\beta\_{1})\sqrt{T}}+\frac{dG\gamma}{2(1-\beta\_{1})}C(\beta\_{1},\beta\_{2})=O!\left(\frac{1}{T\gamma}+\frac{1}{\sqrt{T}}+\gamma\right).

Equation 41

https://arxiv.org/html/2602.04898v2#A3.E41

to the k k -branch and the v v -branch separately, with possibly different gradient bounds G k , G v G\_{k},G\_{v} , and using ℓ t total = α k  ℓ t ( k ) + α v  ℓ t ( v ) \ell\_{t}^{\mathrm{total}}=\alpha\_{k}\ell\_{t}^{(k)}+\alpha\_{v}\ell\_{t}^{(v)} , we obtain

1 T  ∑ t = 1 T ( ℓ t total  ( W k , t , W v , t ) − ℓ t total  ( W k ∗ , W v ∗ ) ) \displaystyle\frac{1}{T}\sum\_{t=1}^{T}\Bigl(\ell\_{t}^{\mathrm{total}}(W\_{k,t},W\_{v,t})-\ell\_{t}^{\mathrm{total}}(W\_{k}^{

≤ α k  \[ d  D 2  G k 2  T  γ  ( 1 − β 1 ) + 2  d  D  G k  β 1 ( 1 − β 1 )  T + d  G k  γ 2  ( 1 − β 1 )  C  ( β 1 , β 2 ) \] \displaystyle\leq\alpha\_{k}\left\[\frac{dD^{2}G\_{k}}{2T\gamma(1-\beta\_{1})}+\frac{2dDG\_{k}\beta\_{1}}{(1-\beta\_{1})\sqrt{T}}+\frac{dG\_{k}\gamma}{2(1-\beta\_{1})}C(\beta\_{1},\beta\_{2})\right\]

α v  \[ d  D 2  G v 2  T  γ  ( 1 − β 1 ) + 2  d  D  G v  β 1 ( 1 − β 1 )  T + d  G v  γ 2  ( 1 − β 1 )  C  ( β 1 , β 2 ) \] . \displaystyle\quad+\alpha\_{v}\left\[\frac{dD^{2}G\_{v}}{2T\gamma(1-\beta\_{1})}+\frac{2dDG\_{v}\beta\_{1}}{(1-\beta\_{1})\sqrt{T}}+\frac{dG\_{v}\gamma}{2(1-\beta\_{1})}C(\beta\_{1},\beta\_{2})\right\].

Experimental support, please

view the build logs

https://arxiv.org/html/2602.04898v2/\_\_stdout.txt

for errors. Generated by

L A T E xml\[LOGO\]

https://math.nist.gov/~BMiller/LaTeXML/

Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

You can select the relevant text first, to include it in your report.

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

javascript:toggleReadingMode();

