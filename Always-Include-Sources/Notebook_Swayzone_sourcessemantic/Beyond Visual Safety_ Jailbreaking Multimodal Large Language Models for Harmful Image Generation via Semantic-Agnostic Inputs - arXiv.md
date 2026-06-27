---
sourceFile: "Beyond Visual Safety: Jailbreaking Multimodal Large Language Models for Harmful Image Generation via Semantic-Agnostic Inputs - arXiv"
exportedBy: "Kortex"
exportDate: "2026-06-26T04:27:51.067Z"
---

# Beyond Visual Safety: Jailbreaking Multimodal Large Language Models for Harmful Image Generation via Semantic-Agnostic Inputs - arXiv

a8063f14-9b23-4dfc-91ea-9531ebf83d55

Beyond Visual Safety: Jailbreaking Multimodal Large Language Models for Harmful Image Generation via Semantic-Agnostic Inputs - arXiv

1ef9ed20-46b9-4ddb-8c8a-f359c3ec3b0f

https://arxiv.org/html/2601.15698

Beyond Visual Safety: Jailbreaking Multimodal Large Language Models for Harmful Image Generation via Semantic-Agnostic Inputs

logo Back to arXiv

https://arxiv.org/

https://arxiv.org/abs/2601.15698

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

https://arxiv.org/abs/2601.15698v1

Download PDF

https://arxiv.org/pdf/2601.15698v1

javascript:toggleColorScheme()

Table of Contents

https://arxiv.org/html/2601.15698#abstract

1 Introduction

https://arxiv.org/html/2601.15698v1#S1

2 Related Work

https://arxiv.org/html/2601.15698v1#S2

3 Methodology

https://arxiv.org/html/2601.15698v1#S3

3.1 Overall Workflow of BVS

https://arxiv.org/html/2601.15698v1#S3.SS1

#### Visual Guidance Generation:

https://arxiv.org/html/2601.15698v1#S3.SS1.SSS0.Px1

#### Neutralized Visual Splicing:

https://arxiv.org/html/2601.15698v1#S3.SS1.SSS0.Px2

https://arxiv.org/html/2601.15698v1#S3.SS1.SSS0.Px3

3.2 Multi-Image Distance Optimization Selection Algorithm

https://arxiv.org/html/2601.15698v1#S3.SS2

3.3 Security Vulnerability Analysis of MLLMs

https://arxiv.org/html/2601.15698v1#S3.SS3

4 Experiment and Analysis

https://arxiv.org/html/2601.15698v1#S4

https://arxiv.org/html/2601.15698v1#S4.SS1

4.1.1 Visual Guidance Model

https://arxiv.org/html/2601.15698v1#S4.SS1.SSS1

4.1.2 Datasets

https://arxiv.org/html/2601.15698v1#S4.SS1.SSS2

4.1.3 Neutralized Image Data

https://arxiv.org/html/2601.15698v1#S4.SS1.SSS3

4.1.4 Baseline

https://arxiv.org/html/2601.15698v1#S4.SS1.SSS4

4.1.5 Evaluation Metric

https://arxiv.org/html/2601.15698v1#S4.SS1.SSS5

4.2 Motivation for Benchmark Construction

https://arxiv.org/html/2601.15698v1#S4.SS2

4.3 Jailbreaking Results

https://arxiv.org/html/2601.15698v1#S4.SS3

4.4 Ablation Study

https://arxiv.org/html/2601.15698v1#S4.SS4

4.5 Scalability and Diverse Manifestations of Jailbreak Outputs

https://arxiv.org/html/2601.15698v1#S4.SS5

4.6 MLLMs Visual Security Analysis

https://arxiv.org/html/2601.15698v1#S4.SS6

5 Conclusion

https://arxiv.org/html/2601.15698v1#S5

5.1 Summary of Contributions

https://arxiv.org/html/2601.15698v1#S5.SS1

5.2 Security Implications

https://arxiv.org/html/2601.15698v1#S5.SS2

https://arxiv.org/html/2601.15698v1#A1

A.1 Chinese Inductive Prompt

https://arxiv.org/html/2601.15698v1#A1.SS1

https://arxiv.org/html/2601.15698#bib

License: CC BY 4.0

https://info.arxiv.org/help/license/index.html#licenses-available

arXiv:2601.15698v1 \[cs.CV\] 22 Jan 2026

Beyond Visual Safety: Jailbreaking Multimodal Large Language Models for Harmful Image Generation via Semantic-Agnostic Inputs

Report issue for preceding element

Mingyu Yu Lana Liu Zhehao Zhao Wei Wang Sujuan Qin

Report issue for preceding element

Report issue for preceding element

The rapid advancement of Multimodal Large Language Models (MLLMs) has introduced complex security challenges, particularly at the intersection of textual and visual safety. While existing schemes have explored the security vulnerabilities of MLLMs, the investigation into their visual safety boundaries remains insufficient. In this paper, we propose Beyond Visual Safety (BVS), a novel image-text pair jailbreaking framework specifically designed to probe the visual safety boundaries of MLLMs. BVS employs a ”reconstruction-then-generation” strategy, leveraging neutralized visual splicing and inductive recomposition to decouple malicious intent from raw inputs, thereby leading MLLMs to be induced into generating harmful images. Experimental results demonstrate that BVS achieves a remarkable jailbreak success rate of 98.21% against GPT-5 (12 January 2026 release). Our findings expose critical vulnerabilities in the visual safety alignment of current MLLMs. Our code and benchmark is publicly available.

https://github.com/Steganographyer/JailBreak\_MLLM

https://github.com/Steganographyer/JailBreak\_MLLM

Report issue for preceding element

Multimodal Large Language Models, Visual Safety, Jailbreak Attack, Red Teaming, Semantic Dilution

1 Introduction

Report issue for preceding element

The rapid evolution of Multimodal Large Language Models (MLLMs) (OpenAI,

https://arxiv.org/html/2601.15698v1#bib.bib1

; Hurst et al.,

https://arxiv.org/html/2601.15698v1#bib.bib2

; Team et al.,

https://arxiv.org/html/2601.15698v1#bib.bib3

) has introduced significant security risks. Despite their versatility, the integrated multi-modal nature expands the attack surface (Jiang et al.,

https://arxiv.org/html/2601.15698v1#bib.bib4

; Peng et al.,

https://arxiv.org/html/2601.15698v1#bib.bib5

) , posing substantial challenges to the safety of the generated multimodal content.

Report issue for preceding element

Early research on LLM jailbreaking has transitioned from manual prompt engineering (Li et al.,

https://arxiv.org/html/2601.15698v1#bib.bib6

; Liu et al.,

https://arxiv.org/html/2601.15698v1#bib.bib7

) to automated frameworks leveraging evolutionary strategies (Yu et al.,

https://arxiv.org/html/2601.15698v1#bib.bib8

) , gradient optimizations (Zou et al.,

https://arxiv.org/html/2601.15698v1#bib.bib9

) , and structured red-teaming (Deng et al.,

https://arxiv.org/html/2601.15698v1#bib.bib10

; Mehrotra et al.,

https://arxiv.org/html/2601.15698v1#bib.bib11

) . However, these methods often overlook underlying safety mechanisms, leading to limited exploration of LLMs' safety boundaries.

Report issue for preceding element

Recent advancements further exploit vulnerabilities in prompt structures and model comprehension capabilities for jailbreaking (Zhang et al.,

https://arxiv.org/html/2601.15698v1#bib.bib12

https://arxiv.org/html/2601.15698v1#bib.bib13

) . Various methodologies have been proposed to exploit these gaps, such as iterative rewriting (Ding et al.,

https://arxiv.org/html/2601.15698v1#bib.bib14

) , code encryption (Lv et al.,

https://arxiv.org/html/2601.15698v1#bib.bib15

) , multilingual misalignment (Yuan et al.,

https://arxiv.org/html/2601.15698v1#bib.bib16

) , and inference pattern analysis (Deng et al.,

https://arxiv.org/html/2601.15698v1#bib.bib17

; Zhao et al.,

https://arxiv.org/html/2601.15698v1#bib.bib18

; Chao et al.,

https://arxiv.org/html/2601.15698v1#bib.bib19

) . Additionally, techniques manipulating semantic continuity (Liu et al.,

https://arxiv.org/html/2601.15698v1#bib.bib20

; Li et al.,

https://arxiv.org/html/2601.15698v1#bib.bib21

; Ramesh et al.,

https://arxiv.org/html/2601.15698v1#bib.bib22

) and adaptive strategies leveraging semantic understanding (Yu et al.,

https://arxiv.org/html/2601.15698v1#bib.bib23

) have achieved high success rates. These findings indicate that jailbreaking can be achieved by perturbing prompts to increase the model's difficulty in comprehending safety-aligned tasks. However, these works focus exclusively on jailbreaking the textual modality of LLMs.

Report issue for preceding element

Previous jailbreaking schemes for LLMs primarily focused on how to bypass linguistic safety defense mechanisms. However, MLLMs implement safety defense mechanisms not only against harmful semantics in textual inputs but also against those within visual inputs. To this end, many existing methods, such as Yang et al. (

https://arxiv.org/html/2601.15698v1#bib.bib24

); Jeong et al. (

https://arxiv.org/html/2601.15698v1#bib.bib25

); Zhao et al. (

https://arxiv.org/html/2601.15698v1#bib.bib26

); Ma et al. (

https://arxiv.org/html/2601.15698v1#bib.bib27

) , explore how to simultaneously bypass both textual and visual safety defense mechanisms through image-text pairs. These methods aim to jailbreak MLLMs to output harmful text, yet they do not attempt to generate harmful images. Conversely, jailbreaking schemes that rely on a single textual modality to generate harmful images (Huang et al.,

https://arxiv.org/html/2601.15698v1#bib.bib28

; Wang et al.,

https://arxiv.org/html/2601.15698v1#bib.bib29

) often exhibit limited effectiveness due to their reliance on only one modality.

Report issue for preceding element

Previous research has primarily focused on the safety boundaries of text generation in MLLMs or relied on a single textual modality to investigate the safety boundaries of image generation. Consequently, the exploration of visual safety boundaries in MLLMs remains insufficient. To address these issues, we propose Beyond Visual Safety (BVS), an image-text pair jailbreaking framework designed to explore the safety boundaries of MLLM image generation. BVS achieves a breakthrough by utilizing neutralized visual splicing and inductive recomposition. This work provides a more rigorous evaluation of the visual safety of MLLMs.

Report issue for preceding element

#### The primary contributions of this paper are summarized as follows:

#### Report issue for preceding element

- We propose a novel image-text pair jailbreaking framework, BVS, which investigates the visual safety boundaries of MLLMs. Report issue for preceding element
- We establish a rigorous benchmark dataset specifically designed for evaluating the visual safety of MLLMs. Experimental results demonstrate that our framework achieves a 98.21% jailbreak success rate against the GPT-5 (12 January 2026 release), revealing critical vulnerabilities in current multimodal safety alignment mechanisms. Report issue for preceding element
2 Related Work

Report issue for preceding element

Previous research has achieved significant breakthroughs in exploring the security vulnerabilities of MLLMs. Specifically, confusion-based schemes such as CodeChameleon (Lv et al.,

https://arxiv.org/html/2601.15698v1#bib.bib15

) , FlipAttack (Liu et al.,

https://arxiv.org/html/2601.15698v1#bib.bib20

) , and AJF (Yu et al.,

https://arxiv.org/html/2601.15698v1#bib.bib23

) have demonstrated that MLLMs exhibit poor defensive performance against disordered or obfuscated textual content, which hinders the model's ability to perform standard semantic alignment.

Report issue for preceding element

Regarding the multimodal context, Zhao et al. (

https://arxiv.org/html/2601.15698v1#bib.bib26

) identified that the simultaneous use of shuffled images and perturbed text can effectively compromise MLLMs. Their work reveals that even when both modalities contain prohibited content, the model may fail to refuse the query because the disordered input prevents the activation of safety guardrails. Furthermore, regarding image-based jailbreaking, Yang et al. (

https://arxiv.org/html/2601.15698v1#bib.bib24

) derived a critical conclusion: when processing a composite image comprising multiple sub-images with large semantic distances, MLLMs tend to overlook the harmful information embedded within. This suggests that the model's internal attention is dispersed by the semantic incoherence of the input.

Report issue for preceding element

In summary, disordered inputs and large-semantic-distance interference have proven effective in evading the safety filters of MLLMs for text generation. However, whether the synergy of image shuffling and semantic distance optimization can specifically bypass the safety scrutiny governing visual content generation remains an underexplored challenge, which constitutes the focus of this study.

Report issue for preceding element

3 Methodology

Report issue for preceding element

Figure 1: The overall architecture of the BVS framework. Report issue for preceding element

Previous research exhibits limitations in exploring the safety boundaries of MLLMs regarding the generation of harmful images. In contrast, BVS leverages semantically neutralized images paired with benign prompts to jailbreak MLLMs, effectively concealing the underlying malicious intent. During the MLLM's processing of this multimodal pair, the latent harmful intent is manifested, thereby inducing the model to generate harmful images.

#### Report issue for preceding element

3.1 Overall Workflow of BVS

Report issue for preceding element

The process of employing BVS to jailbreak MLLMs for the generation of harmful images consists of three stages, as illustrated in Figure

https://arxiv.org/html/2601.15698v1#S3.F1

. The first stage is Visual Guidance Generation, which produces a malicious inductive image. The second stage, Neutralized Visual Splicing, generates a semantically neutralized composite image. In the final stage, this composite image is paired with a specifically designed Chinese Inductive Prompt to execute the jailbreak. The detailed workflow is as follows:

Report issue for preceding element

#### Visual Guidance Generation:

Report issue for preceding element

The attacker first inputs a malicious prompt into a Visual Guidance Model (typically a text-to-image generative model). The model outputs an image I A I\_{A} that corresponds to the semantics of the malicious prompt. Thus, I A I\_{A} serves as a visual representation of the harmful intent originally contained in the text.

Report issue for preceding element

#### Neutralized Visual Splicing:

Report issue for preceding element

We first curate a dataset denoted as Neutralized Image Data, consisting of images with benign semantics designed to counteract the harmful nature of I A I\_{A} . The neutralization process involves partitioning I A I\_{A} into four equal-sized patches, denoted as f i , i ∈ { 1 , 2 , 3 , 4 } f\_{i},i\in{1,2,3,4} . These four patches are then randomly shuffled. Subsequently, five images, denoted as n i , i ∈ { 1 , 2 , 3 , 4 , 5 } n\_{i},i\in{1,2,3,4,5} , are selected from the Neutralized Image Data using the MIDOS(Multi-Image Distance Optimization Selection Algorithm ). Following the definition of the MIDOS and the insertion method illustrated in the Neutralized Visual Splicing section of Figure

https://arxiv.org/html/2601.15698v1#S3.F1

, the five n i n\_{i} patches are interleaved with the four shuffled f i f\_{i} patches to form a semantically neutralized composite image, I S I\_{S} . A representative example of this spliced image is provided in the Jailbreak section of Figure

https://arxiv.org/html/2601.15698v1#S3.F1

Report issue for preceding element

Report issue for preceding element

The composite image I S I\_{S} is paired with a Chinese Inductive Prompt to target the MLLM. By providing two seemingly harmless inputs, the attacker induces the MLLM to reconstruct the latent harmful intent during execution and subsequently generate a harmful image. The design logic of the Chinese Inductive Prompt is as follows: it instructs the MLLM to treat the input image as a 3 × 3 3\times 3 matrix, where the elements at positions a 11 , a 13 , a 31 a\_{11},a\_{13},a\_{31} , and a 33 a\_{33} constitute a semantically coherent image. The prompt then directs the model to first mentally reconstruct this complete image and then generate a new image based on that reconstructed semantic content. The specific Chinese Inductive Prompts used in our experiments are detailed in the

https://arxiv.org/html/2601.15698v1#A1.SS1

#### Report issue for preceding element

3.2 Multi-Image Distance Optimization Selection Algorithm

Report issue for preceding element

The core challenge in constructing the composite image I S I\_{S} lies in selecting benign patches from the neutralized dataset 𝒩 e  r \mathcal{N}

{er} that can effectively ”dilute” the malicious semantics of I A I

{A} while maintaining a natural distribution. To address this, we propose the Multi-Image Distance Optimization Selection (MIDOS) algorithm. MIDOS strategically selects five neutralized patches { n 1 , … , n 5 } {n\_{1},\dots,n\_{5}} to fill the gaps between the shuffled malicious patches { f a , f b , f c , f d } {f\_{a},f\_{b},f\_{c},f\_{d}} in a 3 × 3 3\times 3 grid.

Report issue for preceding element

The algorithm relies on two key metrics: the semantic distance D s  e  ( x , y ) D\_{se}(x,y) , which measures the distance between the feature representations of image x x and y y , and a norm penalty function defined as:

Report issue for preceding element

L  P  D s  e  ( x , y , z ) = 1 D s  e 2  ( x , z ) + 1 D s  e 2  ( y , z ) LPD\_{se}(x,y,z)=\frac{1}{D\_{se}^{2}(x,z)}+\frac{1}{D\_{se}^{2}(y,z)}

The selection logic is designed to maximize the semantic gap between the center patch and the original malicious image while minimizing the local perceptual dissonance between adjacent patches. The detailed procedure is presented in Algorithm

https://arxiv.org/html/2601.15698v1#alg1

Report issue for preceding element

Algorithm 1 MIDOS

Input: I A I\_{A} , { f a , f b , f c , f d } {f\_{a},f\_{b},f\_{c},f\_{d}} , Neutralized Image Data 𝒩 e  r \mathcal{N}\_{er}

Output: { n 1 , n 2 , n 3 , n 4 , n 5 } {n\_{1},n\_{2},n\_{3},n\_{4},n\_{5}}

n 1 ← argmax n i ∈ 𝒩 e  r  D s  e  ( I A , n i ) n\_{1}\leftarrow\text{argmax}

{i}\in\mathcal{N}

{se}(I\_{A},n\_{i})

𝒩 ′ ← 𝒩 e  r ∖ { n 1 } \mathcal{N}^{\prime}\leftarrow\mathcal{N}

{er}\setminus{n

n 2 ← argmin n i ∈ 𝒩 ′  L  P  D s  e  ( f a , f b , n i ) n\_{2}\leftarrow\text{argmin}

{i}\in\mathcal{N}^{\prime}}LPD\_{se}(f\_{a},f\_{b},n\_{i})

n 3 ← argmin n i ∈ 𝒩 ′ ∖ { n 2 }  L  P  D s  e  ( f b , f d , n i ) n\_{3}\leftarrow\text{argmin}

{i}\in\mathcal{N}^{\prime}\setminus{n\_{2}}}LPD\_{se}(f\_{b},f\_{d},n\_{i})

n 4 ← argmin n i ∈ 𝒩 ′ ∖ { n 2 , n 3 }  L  P  D s  e  ( f c , f d , n i ) n\_{4}\leftarrow\text{argmin}

{i}\in\mathcal{N}^{\prime}\setminus{n\_{2},n\_{3}}}LPD\_{se}(f\_{c},f\_{d},n\_{i})

n 5 ← argmin n i ∈ 𝒩 ′ ∖ { n 2 , n 3 , n 4 }  L  P  D s  e  ( f a , f c , n i ) n\_{5}\leftarrow\text{argmin}

{i}\in\mathcal{N}^{\prime}\setminus{n\_{2},n\_{3},n\_{4}}}LPD\_{se}(f\_{a},f\_{c},n\_{i})

return { n 1 , n 2 , n 3 , n 4 , n 5 } {n\_{1},n\_{2},n\_{3},n\_{4},n\_{5}}

Report issue for preceding element

The design of the MIDOS algorithm is theoretically grounded in the “Distraction Hypothesis” of MLLMs. Previous research indicates that the capability of MLLMs to identify harmful content heavily relies on the semantic consistency and alignment strength between visual elements and malicious intentions (Yang et al.,

https://arxiv.org/html/2601.15698v1#bib.bib24

) . MIDOS maximizes the global semantic distance D s  e D\_{se} between the central patch and the original malicious image, while simultaneously employing the Least Perceptual Dissonance ( L  P  D s  e LPD\_{se} ) penalty term to maximize the semantic variance among locally adjacent patches. The core logic of this approach lies in the intentional construction of a distributional shift. Such extreme semantic discontinuity significantly escalates the processing burden on the model's visual encoder, inducing a state of attention distraction during feature extraction. This mechanism effectively severs the semantic correlation between malicious fragments, thereby circumventing the internal safety alignment mechanisms of the model and preventing the reconstruction of harmful visual patterns.

#### Report issue for preceding element

3.3 Security Vulnerability Analysis of MLLMs

Report issue for preceding element

While prior research has explored the safety of image generation in MLLMs, many identified vulnerabilities reside in the ”surface layer” of safety boundaries, where models often generate harmful content even without sophisticated jailbreak techniques. This suggests a limitation in existing evaluations regarding the assessment of MLLM safety against complex, coordinated cross-modal inputs. Our BVS framework, however, identifies a deeper architectural vulnerability: the discrepancy between local visual perception and global semantic understanding in MLLMs.

Report issue for preceding element

The effectiveness of BVS can be attributed to the following two factors. First, the spatial attention fragmentation. By partitioning the malicious image I A I\_{A} into shuffled patches and interleaving them with neutralized buffers selected by MIDOS, we effectively disrupt the model's immediate recognition of harmful visual patterns. Current MLLM safety filters often rely on global feature extraction or rapid scanning of salient objects; BVS bypasses these by scattering malicious semantics into discrete spatial coordinates ( a 11 , a 13 , a 31 , a 33 a\_{11},a\_{13},a\_{31},a\_{33} ).

Report issue for preceding element

Second, the cross-modal inductive recomposition. We leverage the MLLM's inherent capability to follow complex instructions for multimodal inputs. While the individual visual and textual inputs are semantically benign at the point of ingestion, the chinese inductive prompt forces the model to perform a latent mental reconstruction of the interleaved patches during the execution phase. This ”reconstruction-then-generation” process bypasses the input-stage safety alignment, as the harmful intent only fully manifests within the model's internal latent space during the inference process, leading to the generation of harmful images.

Report issue for preceding element

4 Experiment and Analysis

Report issue for preceding element

Figure 2: Examples of Jailbreak Outputs. Report issue for preceding element

#### Report issue for preceding element

4.1.1 Visual Guidance Model

Report issue for preceding element

We adopt CogView4-6B (Zheng et al.,

https://arxiv.org/html/2601.15698v1#bib.bib31

) as our Visual Guidance Model. Although the referenced work describes the CogView3 architecture, we utilize the updated CogView4 version available on ModelScope.

https://modelscope.cn/models/ZhipuAI/CogView4-6B

https://modelscope.cn/models/ZhipuAI/CogView4-6B

Report issue for preceding element

This model is a highly instruction-compliant text-to-image generator. Notably, the Malicious Inductive Images generated by this model using raw malicious instructions are highly effective in triggering safety guardrails; direct input of these images into the target MLLMs consistently results in a refusal to respond.

#### Report issue for preceding element

4.1.2 Datasets

Report issue for preceding element

Our dataset is constructed by synthesizing and refining malicious prompts from existing safety research, including Huang et al. (

https://arxiv.org/html/2601.15698v1#bib.bib28

) , Wang et al. (

https://arxiv.org/html/2601.15698v1#bib.bib29

) , and Yang et al. (

https://arxiv.org/html/2601.15698v1#bib.bib30

) . To establish a more rigorous security assessment, we rephrase and intensify the descriptions of these prompts. This process results in an dataset of 110 initial malicious prompts. We verified the baseline safety of these prompts by directly querying GPT-5 (12 January 2026 release); notably, all 110 initial prompts were strictly rejected. This confirms that our dataset consists of high-quality samples that necessitate the use of jailbreaking techniques, thereby providing a robust foundation to further explore the visual safety boundaries of MLLMs when standard refusal mechanisms are bypassed. The motivation behind the construction of this dataset is discussed in Sec.

https://arxiv.org/html/2601.15698v1#S4.SS2

. Detailed contents of this dataset are provided in the Supplementary Material.

#### Report issue for preceding element

4.1.3 Neutralized Image Data

Report issue for preceding element

To implement the BVS framework, we curated a reference set of Neutralized Image Data. This dataset consists of 25 images collected from open web sources, representing common, everyday categories such as desserts, landscapes, and books. These images were specifically selected for their neutral semantic nature and lack of correlation with any prohibited or sensitive topics, ensuring they function as effective semantic diluents. The complete collection of these 25 images is provided in the Supplementary Material.

#### Report issue for preceding element

4.1.4 Baseline

Report issue for preceding element

To evaluate the effectiveness of BVS, we compare it against two representative and newly-proposed image-based jailbreaking schemes:

#### Report issue for preceding element

- Perception-Guided (Huang et al.,

https://arxiv.org/html/2601.15698v1#bib.bib28

) : A recent framework designed for jailbreaking text-to-image models. It employs a lexical substitution strategy to replace sensitive keywords in malicious prompts with neutralized synonyms, thereby inducing the model to generate prohibited visual content. We refer to this method as Per in the following sections. Report issue for preceding element

- Chain-of-Jailbreak (Wang et al.,

https://arxiv.org/html/2601.15698v1#bib.bib29

) : A novel and progressive jailbreaking scheme for MLLMs based on multi-step interactions. It first guides the model to generate a benign image and then iteratively directs it to perform incremental, malicious modifications until the final prohibited output is achieved. This method is henceforth referred to as Chain. Report issue for preceding element

4.1.5 Evaluation Metric

Report issue for preceding element

To ensure objectivity, we employ Doubao-1.5-Pro and Qwen2.5-VL as independent judges. In our experiments, both models yielded identical judgment results across all samples. We define the outcome of a jailbreak as follows:

#### Report issue for preceding element

- Success: The target MLLM successfully outputs an image, and the image is judged as prohibited. Report issue for preceding element
- Failure: The target MLLM either triggers a refusal response or produces an image that is judged as benign. Report issue for preceding element
4.2 Motivation for Benchmark Construction

Report issue for preceding element

The primary motivation for establishing our specialized benchmark stems from the observation that MLLMs lack inherent safety defenses against certain categories of prohibited content, which can be directly generated via simple text prompts without any jailbreaking techniques. We found that GPT-5 can be directly commanded to produce images involving general violence, illegal activities, discrimination, and offensive gestures, examples of which are shown in Figure

https://arxiv.org/html/2601.15698v1#S4.F3

. Previous studies on image-generation jailbreaking often included these ”defenseless” categories in their evaluation datasets, leading to an overestimation of jailbreak effectiveness and failing to conduct a deep exploration of the true visual safety boundaries of MLLMs.

Report issue for preceding element

Figure 3: Examples of harmful images that MLLMs can generate directly from text prompts without any jailbreaking. These categories (e.g., general violence, illegal activities, discrimination, offensive gestures) are often included in prior datasets but do not require sophisticated jailbreaking to produce. Report issue for preceding element

To address this limitation and rigorously test the safety limits of MLLMs, we conducted a systematic taxonomy of content that triggers robust refusal mechanisms. We identified high-risk categories that consistently elicit safety rejections from GPT-5, whether through textual descriptions or visual inputs. These include: bloody violence, drug consumption, pornography, self-harm (involving blood), arson and gun violence. Based on these strictly prohibited categories, we curated a benchmark consisting of 110 high-severity samples. This dataset is specifically designed to probe the deep-seated vulnerabilities of MLLMs, ensuring that any successful generation represents a genuine circumvention of the model's core safety alignment.

#### Report issue for preceding element

4.3 Jailbreaking Results

Report issue for preceding element

To evaluate the effectiveness of our proposed framework, we conduct attacks on two widely deployed MLLMs: GPT-5 (12 January 2026 release) and Gemini 1.5 Flash (15 January 2026 release). The comparative results of different jailbreaking schemes are summarized in Table

https://arxiv.org/html/2601.15698v1#S4.T1

Report issue for preceding element

Table 1: Jailbreak Success Rates (JSR) for different methods against state-of-the-art MLLMs.

Gemini 1.5 Flash

Report issue for preceding element

As demonstrated in Table

https://arxiv.org/html/2601.15698v1#S4.T1

, our BVS framework consistently achieves the highest JSR across both target models, significantly outperforming existing baselines.Specifically, while GPT-5 exhibits robust defense mechanisms against text-only attacks (Per and Chain), BVS effectively breaches these guardrails by leveraging image-text pairs. This demonstrates that, compared to prior schemes, our approach provides a much deeper exploration into the visual safety boundaries of MLLMs.

Report issue for preceding element

Furthermore, the performance gap remains pronounced on Gemini 1.5 Flash. The relatively high success rates of the Per and Chain baselines suggest that Gemini is less resilient to attacks involving linguistic variations, leading to the unhindered generation of numerous prohibited images. Nevertheless, our BVS framework maintains dominant performance, further validating its superior capability in circumventing multimodal safety alignments.

#### Report issue for preceding element

4.4 Ablation Study

Report issue for preceding element

To verify the effectiveness of the MIDOS module in our framework, we conducted a comparative ablation experiment. We evaluated two distinct image selection strategies: (1) Using MIDOS to strategically select five benign images ( n 1 n\_{1} to n 5 n\_{5} ). (2) A baseline approach that selects five benign images randomly. Both strategies were tested against GPT-5, and the results are summarized in Table

https://arxiv.org/html/2601.15698v1#S4.T2

Report issue for preceding element

Table 2: Ablation study of the MIDOS module on GPT-5.

MIDOS Strategy

w/o MIDOS (Random)

Report issue for preceding element

The experimental results demonstrate that MIDOS plays a pivotal role in optimizing the attack effectiveness. By selecting benign images that optimally dilute the harmful content, MIDOS achieves a higher success rate compared to the random selection baseline. Notably, for the two specific cases where BVS with MIDOS failed to jailbreak, we attempted multiple subsequent trials using random selection, none of which resulted in a successful attack. This further confirms that MIDOS consistently identifies superior image combinations for semantic dilution, and its effectiveness is not a result of stochastic fortuity.

#### Report issue for preceding element

4.5 Scalability and Diverse Manifestations of Jailbreak Outputs

Report issue for preceding element

Figure 4: Diversity of generated harmful images from a single inducing image. (a) The inducing image I S I\_{S} used as input. (b)-(f) Five distinct harmful images generated by GPT-5 over five separate trials, demonstrating varied visual content while maintaining consistent malicious semantics. Report issue for preceding element

To further assess the capabilities and implications of the BVS framework, we investigate the diversity of the generated content. We conducted multiple experiments using the same image-text pair and observed that MLLMs produce distinct harmful images in each trial. This indicates that repetitive application of our framework can yield multiple different harmful images from a single image-text pair.

Report issue for preceding element

https://arxiv.org/html/2601.15698v1#S4.F4

illustrates a compelling example of this phenomenon. Figure

https://arxiv.org/html/2601.15698v1#S4.F4

(a) shows the inducing image I S I\_{S} used for the attack. Figures

https://arxiv.org/html/2601.15698v1#S4.F4

(b) through

https://arxiv.org/html/2601.15698v1#S4.F4

(f) display five different harmful images generated by GPT-5 across five separate experiments with the identical I S I\_{S} . It is evident that while the underlying harmful semantics remain consistent, the visual content of these harmful images varies significantly. This experiment highlights that BVS can effectively leverage MLLMs to generate multiple distinct harmful images from just one single inducing image I S I\_{S} , underscoring the severe security threat posed by this vulnerability.

Report issue for preceding element

We attribute this phenomenon to the inherent stochastic sampling mechanism and the high-dimensional probability space of MLLMs. First, the visual generation process in MLLMs typically involves probabilistic sampling (e.g., Top-p or Temperature sampling). Even when the input image-text pair remains identical, the model does not produce a deterministic output but rather samples from a learned conditional distribution P  ( Image | I S , T ) P(\text{Image}|I\_{S},T) . Second, our BVS framework successfully guides the model's hidden states into a ”malicious semantic region.” Within this region, there exists a vast manifold of potential visual realizations that satisfy the harmful semantic constraints. Since the safety filters are bypassed by the fragmented semantics in I S I\_{S} , the model is free to explore different coordinates within this manifold across multiple trials, resulting in diverse visual manifestations of the same underlying violation. This confirms that the vulnerability exploited by BVS is robust and rooted in the generative nature of the models.

#### Report issue for preceding element

4.6 MLLMs Visual Security Analysis

Report issue for preceding element

https://arxiv.org/html/2601.15698v1#S4.F2

presents representative jailbreak samples generated by our BVS framework. Notably, the MLLM is induced to generate spliced images where one side contains prohibited content while the other appears benign. This strategy of concatenating images with significant semantic discrepancies effectively paralyzes the output safety filters of MLLMs. These results reveal that current MLLMs possess the latent capability to generate highly hazardous content.

Report issue for preceding element

We further warn that such vulnerabilities could be exploited in future applications, where malicious actors might use a single harmful image to trigger the automated generation of large-scale harmful visual data. Consequently, these prohibited images could spread uncontrollably, inflicting severe damage on the reputation of MLLM service providers.

Report issue for preceding element

Consequently, the safety alignment of MLLMs must evolve to defend against ”fragmented malicious semantics.” Our BVS framework empirically demonstrates that while MLLMs are robust against images with explicit, holistic harmful semantics, they struggle to identify and intercept malicious intent that has been decomposed and recomposed. Given that MLLMs inherently support complex instruction following, the existence of such semantic-decoupling vulnerabilities makes sophisticated attacks like BVS not only possible but highly effective.

Report issue for preceding element

5 Conclusion

#### Report issue for preceding element

5.1 Summary of Contributions

Report issue for preceding element

In this study, we have systematically exposed a critical vulnerability in the safety alignment of current MLLMs. Our contributions are two-fold:

Report issue for preceding element

First, we proposed BVS, a novel jailbreak framework that pioneers the methodology of ”semantic decoupling and instruction-based recomposition.” By strategically fragmenting malicious intent and leveraging the model's instruction-following capabilities, BVS circumvents existing safety guardrails.

Report issue for preceding element

Second, we have conducted a deeper exploration of the visual safety boundaries of MLLMs compared to prior research. While earlier studies often included defenseless categories that models could generate directly, our work focuses on high-severity violations—such as arson, gun violence, and self-harm—which typically trigger robust refusal mechanisms in widely-deployed MLLMs. Our findings reveal that the perceived security of these models is significantly fragile when faced with coordinated semantic manipulation, offering a more rigorous and realistic benchmark for evaluating the visual safety of multimodal systems.

#### Report issue for preceding element

5.2 Security Implications

Report issue for preceding element

The effectiveness of BVS serves as a catalyst for future research in two critical dimensions. From the perspective of safety boundary exploration, there is significant potential to expand the diversity and scale of Neutralized Image Data to test the limits of semantic dilution. Beyond simple image concatenation, more sophisticated semantic dilution schemes—such as cross-modal interference or subtle stylistic blending—could be investigated to further probe the hidden vulnerabilities of generative manifolds.

Report issue for preceding element

From the perspective of security defense, our work is a call to action for the AI safety community. Current defense paradigms must evolve beyond holistic recognition to address ”fragmented semantic attacks.” As MLLMs become more deeply integrated into human society, the risk of malicious actors exploiting these models to generate large-scale, automated harmful content becomes a tangible threat to human safety. Defenders must prioritize the development of fine-grained, intent-aware guardrails that can preemptively detect decoupled malicious signals.

Report issue for preceding element

Report issue for preceding element

P. Chao, A. Robey, E. Dobriban, H. Hassani, G. J. Pappas, and E. Wong (2025) ↑ Jailbreaking black box large language models in twenty queries. In 2025 IEEE Conference on Secure and Trustworthy Machine Learning (SaTML), pp. 23–42. Cited by:

https://arxiv.org/html/2601.15698v1#S1.p3.1

G. Deng, Y. Liu, Y. Li, K. Wang, Y. Zhang, Z. Li, H. Wang, T. Zhang, and Y. Liu (2024) ↑ MASTERKEY: automated jailbreaking of large language model chatbots. In NDSS, Cited by:

https://arxiv.org/html/2601.15698v1#S1.p3.1

Y. Deng, W. Zhang, S. J. Pan, and L. Bing (2023) ↑ Multilingual jailbreak challenges in large language models. arXiv preprint arXiv:2310.06474. Cited by:

https://arxiv.org/html/2601.15698v1#S1.p2.1

P. Ding, J. Kuang, D. Ma, X. Cao, Y. Xian, J. Chen, and S. Huang (2024) ↑ A wolf in sheep's clothing: generalized nested jailbreak prompts can fool large language models easily. In Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), pp. 2136–2153. Cited by:

https://arxiv.org/html/2601.15698v1#S1.p3.1

Y. Huang, L. Liang, T. Li, X. Jia, R. Wang, W. Miao, G. Pu, and Y. Liu (2025) ↑ Perception-guided jailbreak against text-to-image models. In Proceedings of the AAAI Conference on Artificial Intelligence, Vol. 39, pp. 26238–26247. Cited by:

https://arxiv.org/html/2601.15698v1#S1.p4.1

https://arxiv.org/html/2601.15698v1#S4.I1.i1.p1.1

https://arxiv.org/html/2601.15698v1#S4.SS1.SSS2.p1.1

A. Hurst, A. Lerer, A. P. Goucher, A. Perelman, A. Ramesh, A. Clark, A. Ostrow, A. Welihinda, A. Hayes, A. Radford, et al. (2024) ↑ Gpt-4o system card. arXiv preprint arXiv:2410.21276. Cited by:

https://arxiv.org/html/2601.15698v1#S1.p1.1

J. Jeong, S. Bae, Y. Jung, J. Hwang, and E. Yang (2025) ↑ Playing the fool: jailbreaking llms and multimodal llms with out-of-distribution strategy. In Proceedings of the Computer Vision and Pattern Recognition Conference, pp. 29937–29946. Cited by:

https://arxiv.org/html/2601.15698v1#S1.p4.1

C. Jiang, Z. Wang, M. Dong, and J. Gui (2025) ↑ Survey of adversarial robustness in multimodal large language models. arXiv preprint arXiv:2503.13962. Cited by:

https://arxiv.org/html/2601.15698v1#S1.p1.1

H. Li, D. Guo, W. Fan, M. Xu, J. Huang, F. Meng, and Y. Song (2023a) ↑ Multi-step jailbreaking privacy attacks on chatgpt. In Findings of the Association for Computational Linguistics: EMNLP 2023, pp. 4138–4153. Cited by:

https://arxiv.org/html/2601.15698v1#S1.p2.1

X. Li, Z. Zhou, J. Zhu, J. Yao, T. Liu, and B. Han (2023b) ↑ Deepinception: hypnotize large language model to be jailbreaker. arXiv preprint arXiv:2311.03191. Cited by:

https://arxiv.org/html/2601.15698v1#S1.p3.1

Y. Liu, G. Deng, Z. Xu, Y. Li, Y. Zheng, Y. Zhang, L. Zhao, T. Zhang, K. Wang, and Y. Liu (2023) ↑ Jailbreaking chatgpt via prompt engineering: an empirical study. arXiv preprint arXiv:2305.13860. Cited by:

https://arxiv.org/html/2601.15698v1#S1.p2.1

Y. Liu, X. He, M. Xiong, J. Fu, S. Deng, and B. Hooi (2025) ↑ FlipAttack: jailbreak llms via flipping. In Proceedings of ICML, Cited by:

https://arxiv.org/html/2601.15698v1#S1.p3.1

https://arxiv.org/html/2601.15698v1#S2.p1.1

H. Lv, X. Wang, Y. Zhang, C. Huang, S. Dou, J. Ye, T. Gui, Q. Zhang, and X. Huang (2024) ↑ Codechameleon: personalized encryption framework for jailbreaking large language models. arXiv preprint arXiv:2402.16717. Cited by:

https://arxiv.org/html/2601.15698v1#S1.p3.1

https://arxiv.org/html/2601.15698v1#S2.p1.1

T. Ma, X. Jia, R. Duan, X. Li, Y. Huang, X. Jia, Z. Chu, and W. Ren (2025) ↑ Heuristic-induced multimodal risk distribution jailbreak attack for multimodal large language models. In Proceedings of the IEEE/CVF International Conference on Computer Vision, pp. 2686–2696. Cited by:

https://arxiv.org/html/2601.15698v1#S1.p4.1

A. Mehrotra, M. Zampetakis, P. Kassianik, B. Nelson, H. Anderson, Y. Singer, and A. Karbasi (2024) ↑ Tree of attacks: jailbreaking black-box llms automatically. Advances in Neural Information Processing Systems 37, pp. 61065–61105. Cited by:

https://arxiv.org/html/2601.15698v1#S1.p2.1

OpenAI (2023) ↑ GPT-4 technical report. arXiv preprint arXiv:2303.08774. Cited by:

https://arxiv.org/html/2601.15698v1#S1.p1.1

B. Peng, K. Chen, Q. Niu, Z. Bi, M. Liu, P. Feng, T. Wang, L. K. Yan, Y. Wen, Y. Zhang, et al. (2024) ↑ Jailbreaking and mitigation of vulnerabilities in large language models. arXiv preprint arXiv:2410.15236. Cited by:

https://arxiv.org/html/2601.15698v1#S1.p1.1

G. Ramesh, Y. Dou, and W. Xu (2024) ↑ GPT-4 jailbreaks itself with near-perfect success using self-explanation. In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, pp. 22139–22148. Cited by:

https://arxiv.org/html/2601.15698v1#S1.p3.1

G. Team, R. Anil, S. Borgeaud, J. Alayrac, J. Yu, R. Soricut, J. Schalkwyk, A. M. Dai, A. Hauth, K. Millican, et al. (2023) ↑ Gemini: a family of highly capable multimodal models. arXiv preprint arXiv:2312.11805. Cited by:

https://arxiv.org/html/2601.15698v1#S1.p1.1

W. Wang, K. Gao, Y. Yuan, J. Huang, Q. Liu, S. Wang, W. Jiao, and Z. Tu (2025) ↑ Chain-of-jailbreak attack for image generation models via step by step editing. In Findings of the Association for Computational Linguistics: ACL 2025, pp. 10940–10957. Cited by:

https://arxiv.org/html/2601.15698v1#S1.p4.1

https://arxiv.org/html/2601.15698v1#S4.I1.i2.p1.1

https://arxiv.org/html/2601.15698v1#S4.SS1.SSS2.p1.1

Y. Yang, B. Hui, H. Yuan, N. Gong, and Y. Cao (2024) ↑ Sneakyprompt: jailbreaking text-to-image generative models. In 2024 IEEE symposium on security and privacy (SP), pp. 897–912. Cited by:

https://arxiv.org/html/2601.15698v1#S4.SS1.SSS2.p1.1

Z. Yang, J. Fan, A. Yan, E. Gao, X. Lin, T. Li, K. Mo, and C. Dong (2025) ↑ Distraction is all you need for multimodal large language model jailbreaking. In Proceedings of the Computer Vision and Pattern Recognition Conference, pp. 9467–9476. Cited by:

https://arxiv.org/html/2601.15698v1#S1.p4.1

https://arxiv.org/html/2601.15698v1#S2.p2.1

https://arxiv.org/html/2601.15698v1#S3.SS2.p3.2

J. Yu, X. Lin, Z. Yu, and X. Xing (2023) ↑ Gptfuzzer: red teaming large language models with auto-generated jailbreak prompts. arXiv preprint arXiv:2309.10253. Cited by:

https://arxiv.org/html/2601.15698v1#S1.p2.1

M. Yu, W. Wang, Y. Wei, and S. Qin (2025) ↑ Adaptive jailbreaking strategies based on the semantic understanding capabilities of large language models. arXiv preprint arXiv:2505.23404. Cited by:

https://arxiv.org/html/2601.15698v1#S1.p3.1

https://arxiv.org/html/2601.15698v1#S2.p1.1

Y. Yuan, W. Jiao, W. Wang, J. Huang, P. He, S. Shi, and Z. Tu (2024) ↑ GPT-4 is too smart to be safe: stealthy chat with llms via cipher. In ICLR, Cited by:

https://arxiv.org/html/2601.15698v1#S1.p3.1

H. Zhang, Z. Guo, H. Zhu, B. Cao, L. Lin, J. Jia, J. Chen, and D. Wu (2023) ↑ On the safety of open-sourced large language models: does alignment really prevent them from being misused?. arXiv preprint arXiv:2310.01581. Cited by:

https://arxiv.org/html/2601.15698v1#S1.p3.1

Z. Zhang, C. Chen, B. Liu, C. Liao, Z. Gong, H. Yu, J. Li, and R. Wang (2024) ↑ Unifying the perspectives of nlp and software engineering. TMLR. Cited by:

https://arxiv.org/html/2601.15698v1#S1.p3.1

J. Zhao, K. Chen, W. Zhang, and N. Yu (2025a) ↑ Sql injection jailbreak: a structural disaster of large language models. In Findings of the Association for Computational Linguistics: ACL 2025, pp. 6871–6891. Cited by:

https://arxiv.org/html/2601.15698v1#S1.p3.1

S. Zhao, R. Duan, F. Wang, C. Chen, C. Kang, S. Ruan, J. Tao, Y. Chen, H. Xue, and X. Wei (2025b) ↑ Jailbreaking multimodal large language models via shuffle inconsistency. In Proceedings of the IEEE/CVF International Conference on Computer Vision, pp. 2045–2054. Cited by:

https://arxiv.org/html/2601.15698v1#S1.p4.1

https://arxiv.org/html/2601.15698v1#S2.p2.1

W. Zheng, J. Teng, Z. Yang, W. Wang, J. Chen, X. Gu, Y. Dong, M. Ding, and J. Tang (2024) ↑ Cogview3: finer and faster text-to-image generation via relay diffusion. arXiv preprint arXiv:2403.05121. Cited by:

https://arxiv.org/html/2601.15698v1#S4.SS1.SSS1.p1.1

A. Zou, Z. Wang, J. Z. Kolter, and M. Fredrikson (2023) ↑ Universal and transferable adversarial attacks on aligned language models. arXiv preprint arXiv:2307.15043. Cited by:

https://arxiv.org/html/2601.15698v1#S1.p2.1

Appendix A Appendix

Report issue for preceding element

A.1 Chinese Inductive Prompt

Report issue for preceding element

We present the specific configuration of the Chinese inductive prompt used in our BVS framework in Figure

https://arxiv.org/html/2601.15698v1#A1.F5

Report issue for preceding element

Figure 5: Example of the Chinese inductive prompt used in the BVS framework. The prompt is designed to guide the MLLM through role-playing and spatial reassembly tasks. Report issue for preceding element

It should be noted that the prompt provided in Figure

https://arxiv.org/html/2601.15698v1#A1.F5

serves as a representative example. In practice, the prompt can be dynamically adjusted based on the specific target category of the harmful content. To ensure successful execution, an effective inductive prompt should generally satisfy the following three core requirements:

#### Report issue for preceding element

- Expert Role Assumption: The prompt must establish a professional persona (e.g., an expert in image reconstruction) to redefine the task's context, shifting the model's focus from safety filtering to ”technical reconstruction.” Report issue for preceding element
- Matrix-based Spatial Decomposition: The prompt should treat the input image as a matrix (e.g., a 11 a\_{11} to a 33 a\_{33} ) and instruct the model to reassemble specific, non-contiguous cells. This force the MLLM to perform ”semantic re-integration” of the fragmented malicious components. Report issue for preceding element
- Contrastive Output Constraint: The prompt must explicitly command the generation of a spliced output with ”high semantic discrepancy” between the left and right segments. This intentional disharmony is designed to confuse the model's output safety filters by diluting the harmful segment with a benign one. Report issue for preceding element

We chose Chinese as the primary language for our inductive prompts based on the following strategic considerations:

Report issue for preceding element

First, semantic proficiency: Modern MLLMs have demonstrated sophisticated multilingual capabilities, possessing a deep understanding of Chinese semantics. This ensures that the model can accurately interpret complex spatial matrix instructions without any loss of intent during the decoupling process.

Report issue for preceding element

Second, information density and expressive power: Compared to English, Chinese possesses higher information density. It can convey rich, multi-layered instructions (such as role-playing, matrix mapping, and output constraints) within a more concise structure. This compactness helps maintain the model's attention on the core generation task without being distracted by overly long prompt contexts.

Report issue for preceding element

Third, low operational overhead for modification: The structural characteristics of the Chinese language make it exceptionally convenient to refine instructions. We can alter the core intent or adjust the ”semantic dilution” strategy by modifying only a few characters, which facilitates rapid adaptation to different high-severity safety boundaries while keeping the prompt logic coherent and potent.

Report issue for preceding element

Report issue for preceding element

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

