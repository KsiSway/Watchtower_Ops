---
sourceFile: "CAMERA: Adapting to Semantic Camouflage in Unsupervised Text-Attributed Graph Fraud Detection - arXiv"
exportedBy: "Kortex"
exportDate: "2026-06-26T04:27:51.078Z"
---

# CAMERA: Adapting to Semantic Camouflage in Unsupervised Text-Attributed Graph Fraud Detection - arXiv

1630d3d1-f289-4166-9a5e-05c1e0a9c1fa

CAMERA: Adapting to Semantic Camouflage in Unsupervised Text-Attributed Graph Fraud Detection - arXiv

c3179a65-7d1b-45c6-9f3a-69770b2b5e5d

https://arxiv.org/html/2605.20032v1

CAMERA: Adapting to Semantic Camouflage in Unsupervised Text-Attributed Graph Fraud Detection

Report GitHub Issue

#### Content selection saved. Describe the issue below:

#### Description:

Submit without GitHub Submit in GitHub

arXiv logo Back to arXiv

https://arxiv.org/

https://info.arxiv.org/about/accessible\_HTML.html

Report Issue

https://arxiv.org/html/2605.20032v1

Back to Abstract

https://arxiv.org/abs/2605.20032v1

Download PDF

https://arxiv.org/pdf/2605.20032v1

javascript:toggleNavTOC();

javascript:toggleReadingMode();

https://arxiv.org/html/2605.20032v1#abstract1

1 Introduction

https://arxiv.org/html/2605.20032v1#S1

2 Related Work

https://arxiv.org/html/2605.20032v1#S2

3 Preliminary

https://arxiv.org/html/2605.20032v1#S3

4 Methodology

https://arxiv.org/html/2605.20032v1#S4

4.1 Textual Feature Encoder

https://arxiv.org/html/2605.20032v1#S4.SS1

4.2 Ego-decoupled MoE Architecture

https://arxiv.org/html/2605.20032v1#S4.SS2

4.2.1 Ego-Decoupled MoE Layer

https://arxiv.org/html/2605.20032v1#S4.SS2.SSS1

4.2.2 Expert Specialization

https://arxiv.org/html/2605.20032v1#S4.SS2.SSS2

4.2.3 Context-informed Gating Model

https://arxiv.org/html/2605.20032v1#S4.SS2.SSS3

4.3 Rarity-driven Unsupervised Fraud Detection

https://arxiv.org/html/2605.20032v1#S4.SS3

4.3.1 Parameter-free One-class Fraud Detector

https://arxiv.org/html/2605.20032v1#S4.SS3.SSS1

4.3.2 Expert Loss

https://arxiv.org/html/2605.20032v1#S4.SS3.SSS2

5 Experiments

https://arxiv.org/html/2605.20032v1#S5

5.1 Experimental Setup

https://arxiv.org/html/2605.20032v1#S5.SS1

5.2 Experimental Results

https://arxiv.org/html/2605.20032v1#S5.SS2

5.2.1 Performance Comparison

https://arxiv.org/html/2605.20032v1#S5.SS2.SSS1

5.2.2 Ablation Study

https://arxiv.org/html/2605.20032v1#S5.SS2.SSS2

5.2.3 Visualization of Expert Allocation

https://arxiv.org/html/2605.20032v1#S5.SS2.SSS3

6 Conclusion

https://arxiv.org/html/2605.20032v1#S6

https://arxiv.org/html/2605.20032v1#bib

A Related work in details

https://arxiv.org/html/2605.20032v1#A1

A.1 Fraud Detection on Attributed Graph

https://arxiv.org/html/2605.20032v1#A1.SS1

A.2 Fraud Detection on Text-Attributed Graph

https://arxiv.org/html/2605.20032v1#A1.SS2

B Analyzing Collapse Risk of Training Objectives

https://arxiv.org/html/2605.20032v1#A2

C Algorithm Description

https://arxiv.org/html/2605.20032v1#A3

D Complexity Analysis

https://arxiv.org/html/2605.20032v1#A4

E Dataset and Implementation Details

https://arxiv.org/html/2605.20032v1#A5

F Addition Experiments Results

https://arxiv.org/html/2605.20032v1#A6

F.1 Sensitivity

https://arxiv.org/html/2605.20032v1#A6.SS1

License: arXiv.org perpetual non-exclusive license

https://info.arxiv.org/help/license/index.html#licenses-available

arXiv:2605.20032v1 \[cs.LG\] 19 May 2026

CAMERA: Adapting to Semantic Camouflage in Unsupervised Text-Attributed Graph Fraud Detection

Lianhua Chi

Alan Wee-Chung Liew

School of Information and Communication Technology, Griffith University, Australia

Department of Computer Science and Information Technology, La Trobe University, Australia

junjun.pan@griffithuni.edu.au, {yixin.liu, yu.zheng, a.liew, s.pan}@griffith.edu.au, l.chi@latrobe.edu.au

Text-attributed graph fraud detection (TAGFD) plays a critical role in preventing fraudulent activities on online social and e-commerce platforms. However, to evade detection, fraudsters continuously evolve their camouflaging strategies by deliberately mimicking textual responses of benign users, thereby concealing their malicious purposes. This phenomenon, referred to as semantic camouflage, fundamentally undermines commonly relied assumptions on how structural and attribute cues can be exploited to identify fraudsters, and makes it difficult to spot fraudsters with unsupervised TAGFD. To bridge the gaps, we propose a C ase- A daptive M ulti-cue E xpert f RA mework (CAMERA) for unsupervised TAGFD. CAMERA employs an ego-decoupled mixture-of-experts architecture, where each expert specializes in modeling a distinct type of fraud-indicative cue. A context-informed gating model is introduced to jointly consider the ego node representation and its local neighborhood context for adaptive integration of cues learned by different experts. Furthermore, CAMERA leverages the inherent rarity of fraudsters to support unsupervised one-class learning with expert-level objectives that encourage modeling dominant benign patterns, thereby enabling reliable unsupervised detection of camouflaged fraudsters. Experiments on 4 challenging datasets show that CAMERA consistently outperforms competitors, showing its effectiveness against semantically camouflaged fraudsters. Code available at https://github.com/CampanulaBells/CAMERA

footnotetext: Corresponding authors.

1 Introduction

With the continued advancement of information technology, graph-structured data has become ubiquitous in online services such as e-commerce Yu et al. (

https://arxiv.org/html/2605.20032v1#bib.bib18

) and social media Hu et al. (

https://arxiv.org/html/2605.20032v1#bib.bib19

) . This ubiquity has been accompanied by increasing malicious activities, including fake reviews and spam messages, which underscores the importance of graph fraud detection (GFD) Pan et al. (

https://arxiv.org/html/2605.20032v1#bib.bib20

); Cai et al. (

https://arxiv.org/html/2605.20032v1#bib.bib43

) . Since many real-world platforms are inherently associated with textual content, text-attributed graph fraud detection (TAGFD) has emerged as an essential research direction for identifying suspicious behaviors embedded in text-attributed graphs Yang et al. (

https://arxiv.org/html/2605.20032v1#bib.bib22

); Qian et al. (

https://arxiv.org/html/2605.20032v1#bib.bib44

) . By jointly capturing network structures and attribute information, TAGFD plays a vital role in safeguarding the online platforms Pan et al. (

https://arxiv.org/html/2605.20032v1#bib.bib49

(a) Early fraudsters hide in benign communities.

(b) Evolved fraudsters employ semantic camouflage.

Figure 1: Illustration of fraudster evolution in text-attributed graphs, where the edge weights indicate the affinities between two nodes.

Despite the remarkable progress of detection techniques in recent years, fraudsters also continuously adapt their camouflage strategies to evade detection Yang et al. (

https://arxiv.org/html/2605.20032v1#bib.bib21

) . As illustrated in Figure

https://arxiv.org/html/2605.20032v1#S1.F1

, earlier fraudsters primarily operated at the structure level, where fraudulent nodes attempted to blend into the benign community by connecting themselves to benign users Dou et al. (

https://arxiv.org/html/2605.20032v1#bib.bib1

) . While existing fraud detection methods could still handle these topology-level camouflages by pruning heterophily edges Qiao and Pang (

https://arxiv.org/html/2605.20032v1#bib.bib13

) , evolved fraudsters also deliberately hide their malicious intent by mimicking normal characteristics, which significantly increases the difficulty of detection. Going beyond structure-level blending, these evolved fraudsters further engage in semantic camouflage, i.e., they reshape their language to mimic benign expressions like criticism, while quietly advancing malicious goals like review manipulation or the spread of misleading information.

To counter this semantic camouflage, recent TAGFD studies have explored supervised approaches to learn semantic-level anomalies-indicative cues. For instance, FLAG Yang et al. (

https://arxiv.org/html/2605.20032v1#bib.bib22

) leverages a large language model (LLM) to extract both shared and discriminative contextual signals from collections of fraudulent and normal texts, while DGP Li et al. (

https://arxiv.org/html/2605.20032v1#bib.bib51

) integrates graph structure into LLM fine-tuning. However, these methods typically rely on labels to find the cue from semantics. In real-world applications, however, obtaining reliable annotations for GFD is often costly and impractical. This limitation motivates us to explore a more practical research problem, i.e., unsupervised TAGFD, where fraudsters are identified without access to ground-truth labels.

Figure 2: Left: Local affinity of different datasets with and without semantic camouflage (SC). Right: ROAUC on Instagram dataset.

To handle this new research problem, a naive solution is to extend existing unsupervised GFD methods Qiao and Pang (

https://arxiv.org/html/2605.20032v1#bib.bib13

); He et al. (

https://arxiv.org/html/2605.20032v1#bib.bib16

); Pan et al. (

https://arxiv.org/html/2605.20032v1#bib.bib3

) by incorporating a text encoder to extract textual representation as graph features. These methods assume that fraudsters disrupt local affinity Huang et al. (

https://arxiv.org/html/2605.20032v1#bib.bib40

) , and hence the structure and attribute information are combined to compute affinity as fraud-indicative cues, either directly detecting fraudsters Pan et al. (

https://arxiv.org/html/2605.20032v1#bib.bib3

) or revealing camouflage through edge pruning Qiao and Pang (

https://arxiv.org/html/2605.20032v1#bib.bib13

); He et al. (

https://arxiv.org/html/2605.20032v1#bib.bib16

) . However, as shown in Figure

https://arxiv.org/html/2605.20032v1#S1.F2

, fraudsters with semantic camouflage induce only minor changes in local affinity. As a result, simply extending unsupervised GFD methods to TAGFD scenarios with semantic camouflage can lead to degraded performance. In light of this, a core question arises:

How can we perform unsupervised TAGFD under semantic camouflage without access to ground-truth labels?

In answering this question, we identify two critical challenges: Challenge 1 - Adaptive integration of fraud-indicative cues. Effective fraud detection relies on capturing diverse fraud-indicative cues from both graph structure and node attributes. However, evolving camouflaging strategies and increasingly complex real-world GFD scenarios continually invalidate the predetermined assumptions regarding the integration of these cues. This motivates the need for approaches that adaptively integrate multiple fraud-indicative cues to detect fraudsters with diverse camouflaging strategies. Challenge 2 - Capturing fraud-indicative cues under unsupervised settings. Evolved fraudsters not only hide in benign communities but also actively camouflage in the semantic domain, making their malicious evidence hard to recognize. Such semantic camouflage undermines many commonly adopted heuristic designs, making it particularly challenging to highlight minor deviations from normal patterns without human-annotated labels. As a result, how to leverage the minority nature of fraudsters becomes critical for building an effective TAGFD model.

To fill the gap, we propose a C ase- A daptive M ulti-cue E xpert f RA mework (CAMERA) for unsupervised TAGFD against evolved fraudsters. To tackle Challenge 1, CAMERA introduces an ego-decoupled Mixture-of-Experts (MoE) architecture that allows adaptive integration of multiple fraud-indicative cues, where each expert specializes in a distinct type of anomaly signal. By explicitly decoupling the specialization of each expert, the experts can extract complementary fraud-indicative cues that highlight diverse fraud patterns. Moreover, we further enhance the gating model with local context to guide the adaptive integration in a finer manner. To address Challenge 2, CAMERA leverages the inherent rarity of fraudsters to support unsupervised training. Through one-class learning combined with expert-specific loss, each expert is encouraged to model dominant benign patterns, making malicious deviations introduced by fraudsters more pronounced. Based on these deviation-aware representations, a lightweight parameter-free fraud detector identifies nodes that deviate from normal patterns, enabling unsupervised detector training. Together, CAMERA avoids reliance on rigid assumptions about fraud behaviors while integrating multiple fraud-indicative cues, providing a solid solution for unsupervised TAGFD in the presence of semantically camouflaged fraudsters. In summary, our contributions are threefold:

Problem. To the best of our knowledge, we are the first to formally address the challenge of unsupervised TAGFD under the semantic camouflage scenarios, where fraudsters can mimic benign behaviors to hide their malicious intent.

Method. We propose CAMERA, a novel unsupervised TAGFD framework that employs a MoE architecture to adaptively integrate multiple fraud-indicative cues to reveal semantically camouflaged fraudsters without supervision.

Experiments. We conduct extensive experiments to demonstrate the superior performance of CAMERA over the state-of-the-art methods on four real-world TAGFD datasets under unsupervised learning scenarios.

2 Related Work

In this section, we provide a summary of two related areas. Detailed reviews are provided in Appendix A.

Fraud Detection on Attributed Graph. Early studies formulate graph fraud detection (GFD) as a supervised class-imbalanced classification problem, relying on labeled fraud instances and sampling-based techniques Liu et al. (

https://arxiv.org/html/2605.20032v1#bib.bib31

) . However, real-world fraudsters often camouflage themselves by blending into benign communities via heterophilic edges Gao et al. (

https://arxiv.org/html/2605.20032v1#bib.bib34

) , which substantially degrades supervised models. To address this, later works explicitly incorporate this finding into model design Zhao et al. (

https://arxiv.org/html/2605.20032v1#bib.bib50

) , for example, by pruning heterophilic edges Gao et al. (

https://arxiv.org/html/2605.20032v1#bib.bib34

) or mitigating representation shift caused by fraudsters Tang et al. (

https://arxiv.org/html/2605.20032v1#bib.bib35

) . However, the cost of obtaining annotations can limit their application in diverse real-world scenarios. To address this, follow-up unsupervised GFD studies incorporate heuristic assumptions to obtain heterophilic edges. For example, TAM Qiao and Pang (

https://arxiv.org/html/2605.20032v1#bib.bib13

) and ADA-GAD He et al. (

https://arxiv.org/html/2605.20032v1#bib.bib16

) iteratively compute pseudo-labels to prune heterophilic edges, while HUGE Pan et al. (

https://arxiv.org/html/2605.20032v1#bib.bib3

) establishes a label-free heterophily measure as guidance, thereby training the fraud detector through alignment loss. While recent works further enhance the generalizability by transfer to unseen domains Pan et al. (

https://arxiv.org/html/2605.20032v1#bib.bib41

); Zhao et al. (

https://arxiv.org/html/2605.20032v1#bib.bib52

) or building one-for-all GAD models Liu et al. (

https://arxiv.org/html/2605.20032v1#bib.bib42

) , they ignore the rich semantics contained in text attributes, thereby limiting their application.

Fraud Detection on Text-Attributed Graph Many real-world graphs contain rich textual context, making text-attributed GFD (TAGFD) an important research direction, where evolved fraudsters employ semantic camouflage to escape detection. As a representative method, CoLL Xu et al. (

https://arxiv.org/html/2605.20032v1#bib.bib29

) incorporates LLMs to generate anomaly evidence, but as evolved fraudsters deliberately mimic benign user behaviors, yet when fraudsters deliberately mimic benign behaviors, LLMs are easily misled, resulting in incorrect or misleading evidence. Another line of work integrates structural and textual information into unified graph contrastive learning frameworks Liu et al. (

https://arxiv.org/html/2605.20032v1#bib.bib28

); Xu et al. (

https://arxiv.org/html/2605.20032v1#bib.bib15

) . Nevertheless, semantic camouflage typically induces only subtle ego-neighbor divergence compared to injected structural or feature anomalies Ding et al. (

https://arxiv.org/html/2605.20032v1#bib.bib26

) , weakening the effectiveness of contrastive objectives. These limitations motivate us to address semantic camouflage in unsupervised TAGFD.

3 Preliminary

Notations. Let 𝒢 = ( 𝒱 , ℰ , 𝒯 ) \mathcal{G}=(\mathcal{V},\mathcal{E},\mathcal{T}) represents a text-attributed graph, where 𝒱 \mathcal{V} is the set of nodes and ℰ \mathcal{E} is the set of edges. We denote the number of nodes and edges as n n and m m , respectively. 𝒯 = { t i ∣ v i ∈ 𝒱 } \mathcal{T}={t\_{i}\mid v\_{i}\in\mathcal{V}} denotes the set of textual attributes, where t i ∈ 𝒟 L i t\_{i}\in\mathcal{D}^{L\_{i}} is the text sequence associated with node v i v\_{i} , 𝒟 \mathcal{D} represents the dictionary of words, and L i L\_{i} is the length of the text sequence. The graph structure can also be represented as adjacent matrix 𝐀 ∈ { 0 , 1 } n × n \mathbf{A}\in{0,1}^{n\times n} , with 𝐀 i , j = 1 \mathbf{A}

{i,j}=1 if there exists an edge between nodes v i v

{i} and v j v\_{j} , and 𝐀 i , j = 0 \mathbf{A}

{i,j}=0 otherwise. We denote the set of neighbors of the i i th node as 𝒩  ( v i ) = { v j ∣ 𝐀 i , j = 1 } \mathcal{N}(v

{i})={v\_{j}\mid\mathbf{A}\_{i,j}=1} .

Problem Definition. In the context of TAGFD, each node v i ∈ 𝒱 v\_{i}\in\mathcal{V} has a label y i ∈ { 0 , 1 } y\_{i}\in{0,1} , where y i = 0 y\_{i}=0 indicates a benign node and y i = 1 y\_{i}=1 represents a fraudulent node. A commonly accepted assumption is that the number of benign nodes is significantly greater than the number of fraudulent nodes. In unsupervised scenarios, labels are unavailable during the training stage. Given a text-attributed graph 𝒢 \mathcal{G} , the goal of unsupervised TAGFD is to learn an scoring function f : 𝒱 → ℛ f:\mathcal{V}\xrightarrow{}\mathcal{R} to identify whether a node v i v\_{i} is suspicious by predicting a fraud score s i fraud = f  ( v i , 𝒢 ) s\_{i}^{\text{fraud}}=f(v\_{i},\mathcal{G}) , where a higher score indicates a greater likelihood that the node is fraudulent.

4 Methodology

Figure 3: Overall framework of CAMERA.

In this section, we provide an overview of CAMERA. As shown in Figure

https://arxiv.org/html/2605.20032v1#S4.F3

, we first encode textual node attributes using an LLM to extract high-quality node embeddings. Building on these embeddings, the ego-decoupled Mixture-of-Experts (MoE) layers extract complementary deviation signals, with each expert specializing in a distinct type of fraud-indicative cue. As what constitutes anomalous behavior differs across communities, the contributions of the MoE experts are weighted by a context-informed gating model that leverages both ego and neighborhood embeddings as priors. By learning dominant normal patterns in an unsupervised manner to expose subtle deviations, CAMERA enables adaptive integration of fraud-indicative cues for detecting camouflaged fraudsters without access to ground-truth labels.

4.1 Textual Feature Encoder

Conventional GFD methods often rely on pre-extracted shallow features (e.g., TF-IDF), which are insufficient for capturing the nuanced evidence for malicious purposes required to detect fraud under semantic camouflage. To address these limitations, we employ a pre-trained LLM to encode the textual attributes, providing richer semantic representations for the identification of camouflaged fraudsters. Specifically, given the textual attributes t i t\_{i} of node v i v\_{i} , we adopt an LLM-based feature encoder to transform the input text into a dense semantic representation 𝐱 i \mathbf{x}

{i} as the node attribute: 𝐱 i = LLM  ( t i ) \mathbf{x}

{i}=\text{LLM}(t\_{i}) . The representations are subsequently used as the input to the downstream MoE modules, i.e., 𝐇 \[ 0 \] = \[ 𝐱 1 , … , 𝐱 n \] ∈ ℝ n × d \mathbf{H}^{\[0\]}=\left\[\mathbf{x}

{1},\dots,\mathbf{x}

{n}\right\]\in\mathbb{R}^{n\times d} , where d d is the dimension of LLM-generated representations and each row 𝐡 i \[ 0 \] \mathbf{h}^{\[0\]}

{i} is the representation vector of node v i v

{i} . Compared with small-size text encoders such as SentenceBERT Reimers and Gurevych (

https://arxiv.org/html/2605.20032v1#bib.bib2

) , which were utilized by previous studies of text-attributed graphs, the LLM-based encoder exhibits a stronger semantic compression capability. This is particularly critical under unsupervised TAGFD settings, where subtle cues must be preserved without supervision signals.

4.2 Ego-decoupled MoE Architecture

While the pre-trained LLM-based encoder captures deep semantic information, spotting evolving camouflaged fraudsters requires the effective and adaptive integration of other fraud-indicative cues, ranging from local structural patterns Pan et al. (

https://arxiv.org/html/2605.20032v1#bib.bib3

) to global semantic distributions Jin et al. (

https://arxiv.org/html/2605.20032v1#bib.bib4

) . To address this challenge, we adopt a MoE architecture Li et al. (

https://arxiv.org/html/2605.20032v1#bib.bib48

) , where each expert is highly specialized and capable of capturing one type of discriminative fraud-indicative cues, providing strong and complementary representations for effective detection against camouflaged fraud Tan et al. (

https://arxiv.org/html/2605.20032v1#bib.bib47

) . To model the interactions among heterogeneous cues, we further employ a multi-layer MoE design, where each MoE layer adaptively routes node representations to different experts and refines the fused representation, which hierarchically integrates the fraud-indicative cues. Moreover, a gating network complements the experts by dynamically learning to weight their contributions for each node. This adaptive mechanism allows the model to flexibly integrate fraud-indicative cues without relying on dataset-specific heuristics or domain knowledge, ensuring the most informative cues are prioritized.

4.2.1 Ego-Decoupled MoE Layer

As the essential building block of CAMERA, we first introduce the proposed MoE layer, which adaptively routes and integrates heterogeneous fraud-indicative cues. Specifically, taking the l l -th layer as an example, a standard MoE layer can be written as:

𝐇 \[ l \] = ∑ k diag  ( g k \[ l \]  ( 𝐇 \[ l − 1 \] , 𝐀 ) )  e k \[ l \]  ( 𝐇 \[ l − 1 \] , 𝐀 ) . \mathbf{H}^{\[l\]}=\sum\_{k}\mathrm{diag}!\big(g\_{k}^{\[l\]}(\mathbf{H}^{\[l-1\]},\mathbf{A})\big),e\_{k}^{\[l\]}(\mathbf{H}^{\[l-1\]},\mathbf{A}).

where 𝐇 \[ l \] ∈ ℝ n × d \mathbf{H}^{\[l\]}\in\mathbb{R}^{n\times d} denotes the output embedding matrix, e k \[ l \]  ( 𝐇 \[ l − 1 \] , 𝐀 ) ∈ ℝ n × d e\_{k}^{\[l\]}(\mathbf{H}^{\[l-1\]},\mathbf{A})\in\mathbb{R}^{n\times d} is the embedding matrix produced by the expert k k , and g k \[ l \]  ( 𝐇 \[ l − 1 \] , 𝐀 ) ∈ ℝ n g\_{k}^{\[l\]}(\mathbf{H}^{\[l-1\]},\mathbf{A})\in\mathbb{R}^{n} denotes the corresponding gating weight vector.

Despite its effectiveness in modeling heterogeneous fraud-indicative cues, this generic formulation does not explicitly enforce functional decoupling among experts. Similar to the over-smoothing effect in graph neural networks Rusch et al. (

https://arxiv.org/html/2605.20032v1#bib.bib6

) , redundant expert functions can produce overly homogeneous representations Liu et al. (

https://arxiv.org/html/2605.20032v1#bib.bib7

) , which may obscure critical malicious cues. To address this issue, we propose an ego-decoupled MoE layer that separates expert-specific deviation signals from shared ego features:

𝐇 \[ l \] = 𝐇 \[ l − 1 \] + ∑ k diag  ( g k \[ l \]  ( 𝐇 \[ l − 1 \] , 𝐀 ) )  e k \[ l \]  ( 𝐇 \[ l − 1 \] , 𝐀 ) . \mathbf{H}^{\[l\]}=\mathbf{H}^{\[l-1\]}+\sum\_{k}\mathrm{diag}!\big(g\_{k}^{\[l\]}(\mathbf{H}^{\[l-1\]},\mathbf{A})\big)e\_{k}^{\[l\]}(\mathbf{H}^{\[l-1\]},\mathbf{A}).

By isolating shared ego embeddings, each expert focuses on complementary fraud signals rather than redundant information. Additionally, the skip connection integrates multi-hop graph features across layers, further enhancing the inter-layer information communication within the MoE model for fraud detection Dong et al. (

https://arxiv.org/html/2605.20032v1#bib.bib5

4.2.2 Expert Specialization

MoE architectures typically achieve expert functional divergence through large-scale unsupervised pretraining Fedus et al. (

https://arxiv.org/html/2605.20032v1#bib.bib37

) or domain partitioning Gururangan et al. (

https://arxiv.org/html/2605.20032v1#bib.bib9

) with supervision. However, in unsupervised TAGFD, neither human annotations nor sufficiently large curated datasets are available, which hinders the operationally identical experts from learning diverse and discriminative fraud-indicative cues. Therefore, to ensure functionality divergence, we explicitly design the operation of each expert e k \[ l \] e\_{k}^{\[l\]} to specialize in a distinct fraud-indicative cue, ensuring functional differentiation and capturing complementary cues critical for detecting camouflaged fraudsters. Concretely, three specialized experts, i.e., the graph expert e graph \[ l \] e\_{\text{graph}}^{\[l\]} , the semantic expert, and the global expert, are instantiated in CAMERA, which are defined as follows.

Graph Expert. The graph expert focuses on capturing structural deviation signals, thereby spotting any unusual structural patterns that cannot be encoded with text attributes alone. We first encode local structural patterns using a GCN layer and compute the residual between ego representations and aggregated neighborhood features to expose anomalous structural discrepancies. Specifically, for each node v i v\_{i} with representation 𝐡 i \[ l − 1 \] \mathbf{h}^{\[l-1\]}\_{i} , the operation of the graph expert can be written as:

e graph \[ l \]  ( 𝐡 i \[ l − 1 \] , 𝐀 ) = 𝐡 i \[ l − 1 \] − GCN  ( 𝐡 i \[ l − 1 \] , { 𝐡 j \[ l − 1 \] } v j ∈ 𝒩  ( v i ) ) . e\_{\text{graph}}^{\[l\]}(\mathbf{h}^{\[l-1\]}

{i},\mathbf{A})=\mathbf{h}

{i}^{\[l-1\]}-\operatorname{GCN}!\left(\mathbf{h}

{i}^{\[l-1\]},{\mathbf{h}

{j}^{\[l-1\]}}

{j}\in\mathcal{N}(v\_{i})}\right).

Semantic Expert. To precisely spot any malicious semantic cues, the semantic expert employs an MLP-based autoencoder to learn a compact representation of benign semantics, and uses the difference between that and the input embedding to reveal semantic deviations:

e semantic l  ( 𝐡 i \[ l − 1 \] ) = 𝐡 i \[ l − 1 \] − Decoder  ( Encoder  ( 𝐡 i \[ l − 1 \] ) ) . e\_{\text{semantic}}^{l}(\mathbf{h}

{i}^{\[l-1\]})=\mathbf{h}

{i}^{\[l-1\]}-\text{Decoder}(\text{Encoder}(\mathbf{h}\_{i}^{\[l-1\]})).

Hence, the semantic deviation encodes fine-grained malicious cues of the text, which is critical for detecting semantically camouflaged fraudsters that mimic normal behaviors.

Global Expert. While the graph and semantic experts focus on local deviations, fraudsters are inherently rare instances that deviate from the overall data distribution, which can be exposed from a global perspective. In light of this, we utilized the global expert to measure each node's discrepancy from the dominant benign prototype:

e global \[ l \]  ( 𝐡 i \[ l − 1 \] ) = 𝐡 i \[ l − 1 \] − MLP  ( 𝐡 global \[ l − 1 \] ) , e\_{\text{global}}^{\[l\]}(\mathbf{h}

{i}^{\[l-1\]})=\mathbf{h}

{i}^{\[l-1\]}-\text{MLP}(\mathbf{h}\_{\text{global}}^{\[l-1\]}),

where 𝐡 global \[ l − 1 \] = 1 n  ∑ v j ∈ 𝒱 𝐡 j \[ l − 1 \] \mathbf{h}

{\text{global}}^{\[l-1\]}=\frac{1}{n}\sum

{v\_{j}\in\mathcal{V}}\mathbf{h}\_{j}^{\[l-1\]} . The estimated global deviation characterizes how much a node diverges from the majority, complementing the local structural and semantic deviations captured by other experts.

Collectively, the graph, semantic, and global experts maintain functional differentiation while capturing complementary fraud residuals across structural, textual, and distributional fraud-indicative cues, which ensures that the MoE layer learns diverse and complementary fraud-indicative cues, thereby laying a solid foundation for the gating network to perform adaptive, instance-specific embedding integration.

4.2.3 Context-informed Gating Model

After embedding extraction by specialized experts, a gating model is responsible for dynamically weighting their contributions for every node, enabling adaptive integration of fraud-indicative cues without relying on prior assumptions or domain-specific knowledge. In standard MoE architectures, gating is typically implemented using input-dependent mechanisms such as self-attention Lewis et al. (

https://arxiv.org/html/2605.20032v1#bib.bib11

) . However, in TAGFD, the importance of different fraud-indicative cues is not solely determined by a node's attributes, but is highly dependent on its local context. For example, in topic-focused communities, abnormal connection patterns often provide stronger evidence of fraud, whereas in more diverse communities, semantic irregularities such as misleading or toxic content become more informative. Relying only on ego features may therefore lead to suboptimal expert selection. Motivated by this observation, we propose a context-informed gating model that jointly considers the ego node representation and its local neighborhood context when determining expert contributions to allow for more fine-grained adaptation.

Specifically, to obtain the local neighborhood context 𝐜 i \[ l − 1 \] \mathbf{c}

{i}^{\[l-1\]} of node v i v

{i} , we aggregate the embeddings of its neighbors as:

𝐜 i \[ l − 1 \] = 1 deg  ( v i )  ∑ v j ∈ 𝒩  ( v i ) 𝐡 j \[ l − 1 \] , \mathbf{c}

{i}^{\[l-1\]}=\frac{1}{\text{deg}(v

{i})}\sum\_{v\_{j}\in\mathcal{N}(v\_{i})}\mathbf{h}\_{j}^{\[l-1\]},

where 𝐡 j \[ l − 1 \] \mathbf{h}

{j}^{\[l-1\]} denotes the input embedding of node v j v

{j} at the l − 1 l-1 -th layer, 𝒩  ( v i ) \mathcal{N}(v\_{i}) is the neighbor set of v i v\_{i} , and deg  ( v i ) \text{deg}(v\_{i}) is its degree. The gating network then leverages both the ego representation and the local context to compute expert weights:

𝐠 i \[ l \] \displaystyle\mathbf{g}\_{i}^{\[l\]}

= Softmax ( Linear ( \[ 𝐡 i \[ l − 1 \] | | 𝐜 i \[ l − 1 \] \] ) ) ∈ ℝ 3 , \displaystyle=\text{Softmax}\big(\text{Linear}(\[\mathbf{h}

{i}^{\[l-1\]},||,\mathbf{c}

{i}^{\[l-1\]}\])\big)\in\mathbb{R}^{3},

g k \[ l \]  ( 𝐇 \[ l − 1 \] , 𝐀 ) = { 𝐠 i , k \[ l \] ∣ v i ∈ 𝒱 } , \displaystyle g\_{k}^{\[l\]}(\mathbf{H}^{\[l-1\]},\mathbf{A})={\mathbf{g}

{i,k}^{\[l\]}\mid v

{i}\in\mathcal{V}},

where 𝐠 i , k \[ l \] \mathbf{g}

{i,k}^{\[l\]} represents the k k -th entry of 𝐠 i \[ l \] \mathbf{g}

{i}^{\[l\]} with k = { 1 , 2 , 3 } k={1,2,3} corresponds to graph, semantic, and global experts, respectively, | | || denotes concatenation and Linear  ( ⋅ ) \text{Linear}(\cdot) is a learnable linear transformation. By incorporating both ego features and neighborhood context, the proposed gating model enables more informed selection and aggregation of the malicious cues captured by different experts. Together with the unsupervised training objectives, our context-aware weighting allows the MoE layer to adaptively integrate fraud-indicative cues, thereby providing the flexibility needed to effectively detect camouflaged fraudsters under the diverse and evolving conditions of TAGFD.

To encourage context-dependent expert usage and sparse gating weights, we apply an entropy-based regularization loss on the gating weights 𝐠 i \mathbf{g}\_{i} to train the gating layer:

ℒ gating = ∑ l ∑ k ∈ { graph, semantic, global } − 1 N  ∑ i = 1 N g i , k \[ l \]  log  ( g i , k \[ l \] + ϵ ) , \mathcal{L}

{\text{gating}}=\sum

{l}\sum\_{k\in{\text{graph, semantic, global}}}-\frac{1}{N}\sum\_{i=1}^{N}g\_{i,k}^{\[l\]}\log(g\_{i,k}^{\[l\]}+\epsilon),

where ϵ \epsilon is a small constant for numerical stability. Notably, during training, we block the gradient from propagating to earlier layers to ensure that the gating loss only updates the gating network, preventing it from directly updating weights of experts to ensure their specialization. By minimizing ℒ gating \mathcal{L}\_{\text{gating}} , we encourage the gating distribution to have a sharper distribution, thereby encouraging each node to strategically utilize the relevant experts given its local context.

4.3 Rarity-driven Unsupervised Fraud Detection

While the proposed MoE layers are designed to adaptively integrate fraud-indicative cues, training them for TAGFD in a fully unsupervised setting remains challenging. As evolved fraudsters deliberately camouflage their malicious purpose by mimicking benign semantics, the assumptions underlying traditional detection methods (e.g., affinity assumption Qiao and Pang (

https://arxiv.org/html/2605.20032v1#bib.bib13

) ) no longer hold, thereby rendering them ineffective in handling evolved fraudsters.

To seek alternative supervision signals, the intrinsic rarity of fraudsters in real-world datasets is a stable and persistent property that can serve as a reliable training prior. Concretely, the “rarity assumption” is that fraudulent behaviors can be characterized as deviations from dominant benign patterns, and hence fraudsters can be identified as low-density outliers in the learned normality space. Motivated by this insight, we draw inspiration from one-class (OC) classification to model the dominant patterns of benign nodes with a parameter-free OC fraud detector, thereby exposing the deviations introduced by minority fraudulent nodes. Meanwhile, we design an expert loss that encourages each expert to capture normal patterns, thereby highlighting any cues of fraudsters in the residual deviations.

4.3.1 Parameter-free One-class Fraud Detector

Building on the discriminative embeddings produced by the MoE experts, we employ a parameter-free OC classifier that models normal patterns and identifies deviations. Specifically, the ℓ 2 \ell\_{2} norm of each embedding serves as a normality measure, which is converted into a bounded fraud score via a sigmoid function σ  ( ⋅ ) \sigma(\cdot) , i.e.,

s i = σ  ( ‖ 𝐡 i final ‖ 2 ) , s\_{i}=\sigma(|\mathbf{h}^{\text{final}}

where 𝐡 i final \mathbf{h}^{\text{final}}

{i} is the representation of v i v

{i} at the final MoE layer. This design provides a lightweight yet effective mechanism to fully leverage the fraud-indicative cues captured by the MoE layers, while also enabling unsupervised detection of subtle fraudulent behaviors with an OC detector.

Under the assumption that fraudsters are a minority, we encourage most fraud scores to approach zero by minimizing

ℒ OC = 1 N  ∑ i = 1 N BCE  ( s i , 0 ) , \mathcal{L}

{\text{OC}}=\frac{1}{N}\sum

{i=1}^{N}\text{BCE}(s\_{i},0),

where BCE  ( ⋅ , ⋅ ) \text{BCE}(\cdot,\cdot) denotes binary cross-entropy. Optimizing ℒ OC \mathcal{L}\_{\text{OC}} pushes the embeddings of normal nodes into a compact hypersphere around the origin while naturally allowing minority fraudsters to stand out due to their larger norms Wang et al. (

https://arxiv.org/html/2605.20032v1#bib.bib12

) . Leveraging the rarity assumption, the OC loss suppresses fraud scores for the majority of nodes while keeping the detector lightweight and easy to optimize. More discussion on the property of OC loss is given in Appendix B.

| Type | Method | AUROC (%) |||| AUPRC (%) ||||

| ^^ | ^^ | Reddit | Instagram | AmazonVideo | YelpChi | Reddit | Instagram | AmazonVideo | YelpChi |

| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| GAD | DOMINANT (SDM'19) | 62.89±0.09 | 45.35±0.08 | OOM | OOM | 20.60±0.04 | 8.92±0.01 | OOM | OOM |

| ^^ | CoLA (TNNLS'21) | 58.63±1.81 | 45.05±0.20 | 51.06±1.95 | 48.62±0.16 | 13.44±0.60 | 8.95±0.06 | 12.83±0.56 | 14.08±0.08 |

| ^^ | PREM (ICDM'23) | 54.85±4.99 | 54.38±3.59 | 58.08±1.91 | OOM | 12.16±2.31 | 11.51±1.16 | 15.06±0.68 | OOM |

| GFD | TAM (NeurIPS'23) | 63.07±0.10 | 47.51±0.06 | OOM | OOM | 14.76±0.11 | 10.40±0.07 | OOM | OOM |

| ^^ | ADA-GAD (AAAI'24) | 64.09±0.02 | 44.98±0.01 | OOM | OOM | 21.78±0.02 | 8.87±0.01 | OOM | OOM |

| ^^ | HUGE (AAAI'25) | 60.64±0.78 | 44.07±0.17 | 51.77±0.55 | OOM | 12.80±0.57 | 9.00±0.15 | 12.49±0.17 | OOM |

| TAGAD | TAGAD (arXiv'25) | 56.65±0.12 | 44.83±0.06 | 51.55±0.12 | 42.21±0.11 | 11.64±0.04 | 9.04±0.02 | 12.14±0.04 | 10.78±0.02 |

| ^^ | CMUCL (ECAI'25) | 60.72±0.15 | 44.41±0.30 | 53.99±0.22 | OOM | 13.52±0.14 | 8.81±0.11 | 13.80±0.19 | OOM |

| ^^ | CoLL (MM'25) | 59.26±0.06 | 44.02±0.72 | 50.27±1.26 | 47.25±0.32 | 13.22±0.18 | 8.88±0.20 | 11.99±0.41 | 12.50±0.09 |

| TAGFD | CAMERA (Ours) | 65.09±0.04 | 58.21±0.29 | 63.05±0.60 | 61.74±0.04 | 18.99±0.04 | 14.23±0.54 | 17.37±0.83 | 18.47±0.02 |

Table 1: Performance comparison in terms of AUROC and AUPRC, with best results in bold. OOM means out-of-memory on a 24GB GPU.

4.3.2 Expert Loss

Although the OC loss can supervise the whole network at a global level, the functionality of each expert could be unconstrained, which leads to expert redundancy and weak specialization. To further regularize the specialization of experts, we introduce an expert loss to enforce functional usefulness at a fine-grained expert level. As we explicitly design each expert to specialize in a distinct type of fraud-indicative cue, minimizing their corresponding deviation signals can naturally serve as the optimization objective. Since the majority of nodes are normal, this encourages each expert to model the patterns of benign nodes, causing the residual deviations of minority fraudulent nodes to become more pronounced. To maintain expert disentanglement, each loss is applied only to the parameters of the corresponding expert, and gradients are blocked from propagating to earlier layers or the gating network. Formally, the expert loss is computed as the average squared deviation across nodes, experts, and layers:

ℒ expert = ∑ l ∑ k ∈ { graph, semantic, global } 1 N  ∑ i = 1 N ‖ e k \[ l \]  ( 𝐡 i \[ l − 1 \] , 𝐀 ) ‖ 2 2 , \mathcal{L}

{\text{expert}}=\sum

{l}\sum\_{k\in{\text{graph, semantic, global}}}\frac{1}{N}\sum\_{i=1}^{N}|e\_{k}^{\[l\]}(\mathbf{h}

{i}^{\[l-1\]},\mathbf{A})|

where N N is the number of nodes, and e k \[ l \]  ( ⋅ ) e\_{k}^{\[l\]}(\cdot) denotes the residual deviation captured by the k k -th expert at layer l l . By modeling benign patterns, the experts naturally amplify the subtle malicious signals caused by camouflaged fraudsters, thereby producing discriminative embeddings 𝐡 i final \mathbf{h}^{\text{final}}\_{i} for the subsequent detector.

The overall training objective is defined by combining ℒ OC \mathcal{L}

{\text{OC}} with ℒ expert \mathcal{L}

{\text{expert}} and ℒ gating \mathcal{L}\_{\text{gating}} , which is written as:

ℒ = ℒ expert + α  ℒ gating + β  ℒ OC , \mathcal{L}=\mathcal{L}

{\text{expert}}+\alpha\mathcal{L}

{\text{gating}}+\beta\mathcal{L}\_{\text{OC}},

where α \alpha and β \beta are trade-off hyperparameters. The overall algorithm and complexity analysis of CAMERA is given in Appendices C and D, respectively.

5 Experiments

5.1 Experimental Setup

Datasets. We conduct experiments on four public GAD datasets spanning diverse application domains, including Reddit Li et al. (

https://arxiv.org/html/2605.20032v1#bib.bib25

) , Instagram Li et al. (

https://arxiv.org/html/2605.20032v1#bib.bib25

) , AmazonVideo McAuley and Leskovec (

https://arxiv.org/html/2605.20032v1#bib.bib24

) , and YelpChi Rayana and Akoglu (

https://arxiv.org/html/2605.20032v1#bib.bib23

) . Following the previous work Li et al. (

https://arxiv.org/html/2605.20032v1#bib.bib51

); Yang et al. (

https://arxiv.org/html/2605.20032v1#bib.bib22

) , we construct the text-attributed graph for fraud detection purposes, and convert all graphs to homogeneous undirected graphs for our experiments. Detailed dataset statistics are summarized in Appendix E.

Baseline and Evaluation Metrics. We compare our approach against 9 state-of-the-art methods. CoLA Liu et al. (

https://arxiv.org/html/2605.20032v1#bib.bib14

) , DOMINANT Ding et al. (

https://arxiv.org/html/2605.20032v1#bib.bib26

) , and PERM Pan et al. (

https://arxiv.org/html/2605.20032v1#bib.bib27

) represent contrastive learning, reconstruction-based, and affinity-based paradigms for unsupervised graph anomaly detection (GAD). TAM Qiao and Pang (

https://arxiv.org/html/2605.20032v1#bib.bib13

) , ADA-GAD He et al. (

https://arxiv.org/html/2605.20032v1#bib.bib16

) , and HUGE Pan et al. (

https://arxiv.org/html/2605.20032v1#bib.bib3

) focus on unsupervised GFD by pruning heterophily edges to mitigate the impact of camouflaged fraudsters. We also include recent studies that incorporate text attributes (TAGAD), namely TAGAD Liu et al. (

https://arxiv.org/html/2605.20032v1#bib.bib28

) , CMUCL Xu et al. (

https://arxiv.org/html/2605.20032v1#bib.bib15

) , and CoLL Xu et al. (

https://arxiv.org/html/2605.20032v1#bib.bib29

) . To ensure a fair comparison, we use OpenAI's text-embedding-3-small model to encode textual attributes for CAMERA and baselines. We use gpt-4o-mini for TAGAD methods that incorporate LLM. The area under the receiver operating characteristic curve (AUROC) and the area under the precision-recall curve (AUPRC) are used as the evaluation metrics. Average results with standard deviations are reported over five runs with different random seeds. The implementation details and more experiments are presented in Appendices E and F, respectively.

AmazonVideo

OpenAI (Ours)

SentenceBERT

Table 2: Ablation study on text encoder. Result in AUROC (%).

5.2 Experimental Results

5.2.1 Performance Comparison

The comparison results of CAMERA is illustrated in Table

https://arxiv.org/html/2605.20032v1#S4.T1

. From the table, we make the following key observations: ❶ CAMERA outperforms SOTA methods in most datasets, with the only exception being AUPRC on Reddit. These results demonstrate the effectiveness of CAMERA in diverse real-world scenarios. ❷ Among the baselines, methods that address structure camouflage by pruning heterophilic edges (TAM, ADA-GAD, HUGE) achieve strong performance on Reddit but perform poorly on other datasets such as Instagram, revealing the limitation of static assumptions that fail to capture evolving fraudster characteristics. In contrast, the adaptive fraud-indicative cues integration strategy of CAMERA allows it to automatically learn and exploit the most informative malicious signal, thereby effectively addressing evolving camouflaging strategies. ❸ The scalability of existing unsupervised GFD methods is limited by out-of-memory (OOM) issues when applied to large-scale real-world datasets such as AmazonVideo and YelpChi. In contrast, CAMERA demonstrates better scalability, underscoring its effectiveness in safeguarding large-scale real-world graph applications like e-commerce and social networks. ❹ Although existing TAGAD incorporate large language models to enhance feature alignment Xu et al. (

https://arxiv.org/html/2605.20032v1#bib.bib15

) or to generate auxiliary evidence Xu et al. (

https://arxiv.org/html/2605.20032v1#bib.bib29

) , they achieve limited performance on the TAGFD task. This is because malicious intent is often concealed by semantic camouflage employed by fraudsters, making it substantially harder to identify than anomalies in constructed benchmark datasets Ma et al. (

https://arxiv.org/html/2605.20032v1#bib.bib30

5.2.2 Ablation Study

To examine the contribution of key design in CAMERA, we conduct ablation studies on critical model components.

Textual Feature Encoder. We replace the LLM-based feature encoder with bag-of-words (BoW) and SentenceBERT representations Reimers and Gurevych (

https://arxiv.org/html/2605.20032v1#bib.bib2

) to assess the impact of semantic representation quality. As shown in Table

https://arxiv.org/html/2605.20032v1#S5.T2

, the LLM-based encoder consistently achieves the highest detection performance. In contrast, although bag-of-words representations are the most commonly-adopted choice in GAD Pan et al. (

https://arxiv.org/html/2605.20032v1#bib.bib27

) , they fail to capture the critical semantic information required for TAGFD. These findings confirm that rich semantic embeddings are critical for detecting camouflaged fraudsters, aligning with our method's emphasis on preserving subtle textual cues in an unsupervised setting.

#### AmazonVideo

65.09 ± \pm 0.04

58.21 ± \pm 0.29

63.05 ± \pm 0.60

61.74 ± \pm 0.04

55.74 ± \pm 0.51

56.55 ± \pm 1.55

58.97 ± \pm 3.37

60.32 ± \pm 0.17

59.96 ± \pm 1.50

56.52 ± \pm 0.57

57.69 ± \pm 5.59

60.24 ± \pm 0.18

60.46 ± \pm 1.71

57.65 ± \pm 0.34

61.35 ± \pm 1.38

59.90 ± \pm 0.07

61.40 ± \pm 0.34

57.95 ± \pm 0.47

61.35 ± \pm 1.56

60.29 ± \pm 0.06

54.00 ± \pm 0.33

57.06 ± \pm 0.35

60.00 ± \pm 0.53

58.14 ± \pm 0.35

54.41 ± \pm 0.29

53.55 ± \pm 1.98

54.64 ± \pm 7.80

59.74 ± \pm 0.22

Table 3: Ablation study on expert participation.

Specialized Experts. To quantify the contribution of each expert, we compare the full model with variants using only one or two experts. Table

https://arxiv.org/html/2605.20032v1#S5.T3

shows that the full MoE achieves the best overall performance, and Figure

https://arxiv.org/html/2605.20032v1#S5.F4

(left) demonstrates that adding more experts consistently improves the results. Together, these results demonstrate that successful TAGFD demands diverse fraud-indicative cues. Among the experts, the graph expert contributes most significantly, highlighting the importance of local structural deviations.

Context-informed Gating. We evaluate the gating model by replacing it with two alternatives: uniform weighting and ego-only gating. As shown in Figure

https://arxiv.org/html/2605.20032v1#S5.F4

(right), incorporating local neighborhood context consistently improves performance across all datasets, highlighting the importance of incorporating community-specific information for weighting experts. In contrast, uniform weighting leads to overall inferior results. Together, the experiment findings confirm that adaptively integrating fraud-indicative cues is critical for identifying evolved, camouflaged fraudsters.

Figure 4: Ablation on (L): #experts and (R): gating mechanism.

Figure 5: Visualization of expert weight.

Figure 6: Case study on YelpChi.

5.2.3 Visualization of Expert Allocation

To investigate how CAMERA adaptively integrates fraud-indicative cues across different scenarios, we visualize the gating weights at the dataset and case levels.

Dataset-level visualization is shown in Figure

https://arxiv.org/html/2605.20032v1#S5.F5

. On Instagram and AmazonVideo, the three experts receive relatively balanced weights. However, as illustrated in Figure

https://arxiv.org/html/2605.20032v1#S5.F4

, replacing them with uniform weights results in a significant performance drop, which shows that the gating model also provides sample-specific fraud-indicative cues integration. On YelpChi and Reddit, the model demonstrates sparse activation. Specifically, YelpChi primarily relies on graph and semantic cues, while Reddit emphasizes the graph expert at layer 1 and the global expert at layer 2. This visualization result also shows that CAMERA performs hierarchical cue integration through expert specialization at different layers.

Case Study on YelpChi. To further investigate the gating model, we analyze the activation weights on YelpChi in detail. As illustrated in Figure

https://arxiv.org/html/2605.20032v1#S5.F6

, on the first MoE layer, different types of food venues exhibit distinct expert weight patterns. For luxury restaurants, the gating model assigns a higher weight to the graph expert compared to the weight reported in Figure

https://arxiv.org/html/2605.20032v1#S5.F5

, emphasizing the importance of reputation. In contrast, beer gardens rely more on subjective reviews, resulting in relatively higher weights for the semantic expert. These observations confirm that CAMERA can achieve adaptive integration of fraud-indicative cues.

To sum up, these observations confirm that CAMERA can achieve adaptive integration of fraud-indicative cues. This flexibility not only enhances detection of evolved fraudsters in diverse real-world scenarios but also enables data-specific integration within the same datasets, leading to superior unsupervised TAGFD performance.

6 Conclusion

In this paper, we propose a novel unsupervised TAGFD framework, CAMERA, that enables detection against evolved fraudsters that engage in semantic camouflage to mimic benign behaviors and evade detection. By utilizing ego-decoupled MoE architecture together with a one-class unsupervised training objective, CAMERA can adaptively integrate different fraud-indicative cues to address evolving camouflaging strategies. Comprehensive empirical results show the effectiveness and robustness of CAMERA in unsupervised TAGFD, validating CAMERA as a practical solution for detecting evolved fraudsters in real-world scenarios.

Acknowledgements

The work of S. Pan was partially supported by the Australian Research Council (ARC) under Grant Nos. DP240101547 and FT210100097. The work of Y. Liu was partially supported by the ARC under Grant No. DE260101172.

T. Cai, Y. Jiang, Y. Liu, M. Li, C. Huang, and S. Pan (2025) Out-of-distribution detection on graphs: a survey. arXiv preprint arXiv:2502.08105. Cited by:

https://arxiv.org/html/2605.20032v1#S1.p1.1

G. Cybenko (1989) Approximation by superpositions of a sigmoidal function. Mathematics of control, signals and systems 2 ( 4), pp. 303–314. Cited by:

https://arxiv.org/html/2605.20032v1#A2.p12.1

K. Ding, J. Li, R. Bhanushali, and H. Liu (2019) Deep anomaly detection on attributed networks. In Proceedings of the 2019 SIAM international conference on data mining, pp. 594–602. Cited by:

https://arxiv.org/html/2605.20032v1#A1.SS1.p2.1

https://arxiv.org/html/2605.20032v1#A1.SS2.p2.1

https://arxiv.org/html/2605.20032v1#A2.p11.1

https://arxiv.org/html/2605.20032v1#S2.p3.1

https://arxiv.org/html/2605.20032v1#S5.SS1.p2.1

X. Dong, X. Zhang, L. Chen, M. Yuan, and S. Wang (2025) SpaceGNN: multi-space graph neural network for node anomaly detection with extremely limited labels. In The Thirteenth International Conference on Learning Representations, External Links:

https://openreview.net/forum?id=Syt4fWwVm1

https://arxiv.org/html/2605.20032v1#S4.SS2.SSS1.p4.2

Y. Dou, Z. Liu, L. Sun, Y. Deng, H. Peng, and P. S. Yu (2020) Enhancing graph neural network-based fraud detectors against camouflaged fraudsters. In Proceedings of the 29th ACM international conference on information & knowledge management, pp. 315–324. Cited by:

https://arxiv.org/html/2605.20032v1#S1.p2.1

W. Fedus, B. Zoph, and N. Shazeer (2022) Switch transformers: scaling to trillion parameter models with simple and efficient sparsity. Journal of Machine Learning Research 23 ( 120), pp. 1–39. Cited by:

https://arxiv.org/html/2605.20032v1#S4.SS2.SSS2.p1.2

Y. Gao, X. Wang, X. He, Z. Liu, H. Feng, and Y. Zhang (2023) Addressing heterophily in graph anomaly detection: a perspective of graph spectrum. In Proceedings of the ACM web conference 2023, pp. 1528–1538. Cited by:

https://arxiv.org/html/2605.20032v1#A1.SS1.p1.1

https://arxiv.org/html/2605.20032v1#S2.p2.1

S. Gururangan, M. Lewis, A. Holtzman, N. A. Smith, and L. Zettlemoyer (2022) Demix layers: disentangling domains for modular language modeling. In Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, pp. 5557–5576. Cited by:

https://arxiv.org/html/2605.20032v1#S4.SS2.SSS2.p1.2

J. He, Q. Xu, Y. Jiang, Z. Wang, and Q. Huang (2024) Ada-gad: anomaly-denoised autoencoders for graph anomaly detection. In Proceedings of the AAAI Conference on Artificial Intelligence, Vol. 38, pp. 8481–8489. Cited by:

https://arxiv.org/html/2605.20032v1#A1.SS1.p2.1

https://arxiv.org/html/2605.20032v1#A2.p11.1

https://arxiv.org/html/2605.20032v1#A2.p12.1

https://arxiv.org/html/2605.20032v1#S1.p4.1

https://arxiv.org/html/2605.20032v1#S2.p2.1

https://arxiv.org/html/2605.20032v1#S5.SS1.p2.1

X. Hu, H. Chen, H. Chen, S. Liu, X. Li, S. Zhang, Y. Wang, and X. Xue (2023) Cost-sensitive gnn-based imbalanced learning for mobile social network fraud detection. IEEE Transactions on Computational Social Systems 11 ( 2), pp. 2675–2690. Cited by:

https://arxiv.org/html/2605.20032v1#A1.SS1.p1.1

https://arxiv.org/html/2605.20032v1#S1.p1.1

Y. Huang, L. Wang, F. Zhang, and X. Lin (2023) Unsupervised graph outlier detection: problem revisit, new insight, and superior method. In 2023 IEEE 39th International Conference on Data Engineering (ICDE), pp. 2565–2578. Cited by:

https://arxiv.org/html/2605.20032v1#S1.p4.1

M. Jin, Y. Liu, Y. Zheng, L. Chi, Y. Li, and S. Pan (2021) Anemone: graph anomaly detection with multi-scale contrastive learning. In Proceedings of the 30th ACM international conference on information & knowledge management, pp. 3122–3126. Cited by:

https://arxiv.org/html/2605.20032v1#S4.SS2.p1.1

D. P. Kingma and M. Welling (2013) Auto-encoding variational bayes. arXiv preprint arXiv:1312.6114. Cited by:

https://arxiv.org/html/2605.20032v1#A2.I1.i3.p1.1

M. Lewis, S. Bhosale, T. Dettmers, N. Goyal, and L. Zettlemoyer (2021) Base layers: simplifying training of large, sparse models. In International Conference on Machine Learning, pp. 6265–6274. Cited by:

https://arxiv.org/html/2605.20032v1#S4.SS2.SSS3.p1.1

R. Li, Z. Liu, Y. Ma, D. Yang, and S. Sun (2022) Internet financial fraud detection based on graph learning. IEEE Transactions on Computational Social Systems 10 ( 3), pp. 1394–1401. Cited by:

https://arxiv.org/html/2605.20032v1#A1.SS1.p1.1

S. Li, Y. Liu, Y. Zheng, X. Cao, S. Pan, and H. T. Shen (2026) Towards one-for-all anomaly detection for tabular data. In International Conference on Machine Learning (ICML), Cited by:

https://arxiv.org/html/2605.20032v1#S4.SS2.p1.1

Y. Li, J. Hu, B. Hooi, B. He, and C. Chen (2025) DGP: a dual-granularity prompting framework for fraud detection with graph-enhanced llms. arXiv preprint arXiv:2507.21653. Cited by:

https://arxiv.org/html/2605.20032v1#A1.SS2.p1.1

https://arxiv.org/html/2605.20032v1#S1.p3.1

https://arxiv.org/html/2605.20032v1#S5.SS1.p1.1

Y. Li, P. Wang, X. Zhu, A. Chen, H. Jiang, D. Cai, V. W. Chan, and J. Li (2024) Glbench: a comprehensive benchmark for graph with large language models. Advances in Neural Information Processing Systems 37, pp. 42349–42368. Cited by:

https://arxiv.org/html/2605.20032v1#S5.SS1.p1.1

B. Liu, L. Ding, L. Shen, K. Peng, Y. Cao, D. Cheng, and D. Tao (2023) Diversifying the mixture-of-experts representation for language models with orthogonal optimizer. In Proceedings of the European Conference on Artificial Intelligence (ECAI), Cited by:

https://arxiv.org/html/2605.20032v1#S4.SS2.SSS1.p4.1

X. Liu, Y. Ren, H. Zhang, R. Wang, S. Zheng, and Z. Zou (2025) Towards anomaly detection on text-attributed graphs. Note: OpenReview preprint

https://openreview.net/forum?id=LMKYd9JHgU

https://openreview.net/forum?id=LMKYd9JHgU

https://arxiv.org/html/2605.20032v1#A1.SS2.p2.1

https://arxiv.org/html/2605.20032v1#S2.p3.1

https://arxiv.org/html/2605.20032v1#S5.SS1.p2.1

Y. Liu, X. Ao, Z. Qin, J. Chi, J. Feng, H. Yang, and Q. He (2021a) Pick and choose: a gnn-based imbalanced learning approach for fraud detection. In Proceedings of the web conference 2021, pp. 3168–3177. Cited by:

https://arxiv.org/html/2605.20032v1#A1.SS1.p1.1

https://arxiv.org/html/2605.20032v1#S2.p2.1

Y. Liu, S. Li, Y. Zheng, Q. Chen, C. Zhang, P. S. Yu, and S. Pan (2026) From few-shot to zero-shot: towards generalist graph anomaly detection. arXiv preprint arXiv:2602.18793. Cited by:

https://arxiv.org/html/2605.20032v1#S2.p2.1

Y. Liu, Z. Li, S. Pan, C. Gong, C. Zhou, and G. Karypis (2021b) Anomaly detection on attributed networks via contrastive self-supervised learning. IEEE transactions on neural networks and learning systems 33 ( 6), pp. 2378–2392. Cited by:

https://arxiv.org/html/2605.20032v1#A1.SS1.p2.1

https://arxiv.org/html/2605.20032v1#S5.SS1.p2.1

X. Ma, J. Wu, S. Xue, J. Yang, C. Zhou, Q. Z. Sheng, H. Xiong, and L. Akoglu (2021) A comprehensive survey on graph anomaly detection with deep learning. IEEE transactions on knowledge and data engineering 35 ( 12), pp. 12012–12038. Cited by:

https://arxiv.org/html/2605.20032v1#S5.SS2.SSS1.p1.1

X. Ma, Y. Zhang, K. Ding, J. Yang, J. Wu, and H. Fan (2024) On fake news detection with llm enhanced semantics mining. In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, pp. 508–521. Cited by:

https://arxiv.org/html/2605.20032v1#A1.SS2.p1.1

J. J. McAuley and J. Leskovec (2013) From amateurs to connoisseurs: modeling the evolution of user expertise through online reviews. In Proceedings of the 22nd international conference on World Wide Web, pp. 897–908. Cited by:

https://arxiv.org/html/2605.20032v1#S5.SS1.p1.1

J. Pan, Y. Zheng, Y. Tan, and Y. Liu (2025a) A survey of generalization of graph anomaly detection: from transfer learning to foundation models. In 2025 IEEE International Conference on Knowledge Graph (ICKG), pp. 316–323. External Links:

https://dx.doi.org/10.1109/ICKG66886.2025.00048

https://arxiv.org/html/2605.20032v1#S1.p1.1

J. Pan, Y. Liu, R. Miao, K. Ding, Y. Zheng, Q. V. H. Nguyen, A. W. Liew, and S. Pan (2026a) Explainable and fine-grained safeguarding of llm multi-agent systems via bi-level graph anomaly detection. In Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics, Cited by:

https://arxiv.org/html/2605.20032v1#S1.p1.1

J. Pan, Y. Liu, X. Zheng, Y. Zheng, A. W. Liew, F. Li, and S. Pan (2025b) A label-free heterophily-guided approach for unsupervised graph fraud detection. In Proceedings of the AAAI Conference on Artificial Intelligence, Vol. 39, pp. 12443–12451. Cited by:

https://arxiv.org/html/2605.20032v1#A1.SS1.p2.1

https://arxiv.org/html/2605.20032v1#S1.p4.1

https://arxiv.org/html/2605.20032v1#S2.p2.1

https://arxiv.org/html/2605.20032v1#S4.SS2.p1.1

https://arxiv.org/html/2605.20032v1#S5.SS1.p2.1

J. Pan, Y. Liu, Y. Zheng, and S. Pan (2023) Prem: a simple yet effective approach for node-level graph anomaly detection. In 2023 IEEE International Conference on Data Mining (ICDM), pp. 1253–1258. Cited by:

https://arxiv.org/html/2605.20032v1#A1.SS1.p2.1

https://arxiv.org/html/2605.20032v1#S5.SS1.p2.1

https://arxiv.org/html/2605.20032v1#S5.SS2.SSS2.p2.1

J. Pan, Y. Liu, C. Zhou, F. Xiong, A. W. Liew, and S. Pan (2026b) Correcting false alarms from unseen: adapting graph anomaly detectors at test time. In Proceedings of the AAAI Conference on Artificial Intelligence, Cited by:

https://arxiv.org/html/2605.20032v1#S2.p2.1

Y. Pang, B. Chen, F. Zhang, Y. Rao, E. Kharlamov, and J. Tang (2025) Guard: effective anomaly detection through a text-rich and graph-informed language model. In Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V. 2, pp. 2222–2233. Cited by:

https://arxiv.org/html/2605.20032v1#A1.SS2.p1.1

Y. Qian, Y. Tan, Y. Liu, W. Yu, and S. Pan (2026) DynHD: hallucination detection for diffusion large language models via denoising dynamics deviation learning. arXiv preprint arXiv:2603.16459. Cited by:

https://arxiv.org/html/2605.20032v1#S1.p1.1

H. Qiao and G. Pang (2023) Truncated affinity maximization: one-class homophily modeling for graph anomaly detection. Advances in Neural Information Processing Systems 36, pp. 49490–49512. Cited by:

https://arxiv.org/html/2605.20032v1#A1.SS1.p2.1

https://arxiv.org/html/2605.20032v1#S1.p2.1

https://arxiv.org/html/2605.20032v1#S1.p4.1

https://arxiv.org/html/2605.20032v1#S2.p2.1

https://arxiv.org/html/2605.20032v1#S4.SS3.p1.1

https://arxiv.org/html/2605.20032v1#S5.SS1.p2.1

S. Rayana and L. Akoglu (2015) Collective opinion spam detection: bridging review networks and metadata. In Proceedings of the 21th acm sigkdd international conference on knowledge discovery and data mining, pp. 985–994. Cited by:

https://arxiv.org/html/2605.20032v1#S5.SS1.p1.1

N. Reimers and I. Gurevych (2019) Sentence-bert: sentence embeddings using siamese bert-networks. arXiv preprint arXiv:1908.10084. Cited by:

https://arxiv.org/html/2605.20032v1#S4.SS1.p1.8

https://arxiv.org/html/2605.20032v1#S5.SS2.SSS2.p2.1

A. Roy, J. Shu, J. Li, C. Yang, O. Elshocht, J. Smeets, and P. Li (2024) Gad-nr: graph anomaly detection via neighborhood reconstruction. In Proceedings of the 17th ACM international conference on web search and data mining, pp. 576–585. Cited by:

https://arxiv.org/html/2605.20032v1#A2.I1.i1.p1.1

T. K. Rusch, M. M. Bronstein, and S. Mishra (2023) A survey on oversmoothing in graph neural networks. arXiv preprint arXiv:2303.10993. Cited by:

https://arxiv.org/html/2605.20032v1#S4.SS2.SSS1.p4.1

Y. Tan, X. Hu, H. Xue, C. De Melo, and F. Salim (2025) Bisecle: binding and separation in continual learning for video language understanding. Advances in Neural Information Processing Systems 38, pp. 33752–33782. Cited by:

https://arxiv.org/html/2605.20032v1#S4.SS2.p1.1

J. Tang, J. Li, Z. Gao, and J. Li (2022) Rethinking graph neural networks for anomaly detection. In International conference on machine learning, pp. 21076–21089. Cited by:

https://arxiv.org/html/2605.20032v1#A1.SS1.p1.1

https://arxiv.org/html/2605.20032v1#S2.p2.1

X. Wang, B. Jin, Y. Du, P. Cui, Y. Tan, and Y. Yang (2021) One-class graph neural networks for anomaly detection in attributed networks. Neural computing and applications 33 ( 18), pp. 12073–12085. Cited by:

https://arxiv.org/html/2605.20032v1#S4.SS3.SSS1.p3.2

Y. Xu, J. Chen, Z. Peng, Z. Chen, Q. Lin, L. Ma, B. Shi, and B. Dong (2025a) Court of llms: evidence-augmented generation via multi-llm collaboration for text-attributed graph anomaly detection. In Proceedings of the 33rd ACM International Conference on Multimedia, pp. 2437–2446. Cited by:

https://arxiv.org/html/2605.20032v1#A1.SS2.p2.1

https://arxiv.org/html/2605.20032v1#S2.p3.1

https://arxiv.org/html/2605.20032v1#S5.SS1.p2.1

https://arxiv.org/html/2605.20032v1#S5.SS2.SSS1.p1.1

Y. Xu, X. Hua, Z. Peng, B. Shi, J. Chen, X. Fu, S. Wang, and B. Dong (2025b) Text-attributed graph anomaly detection via multi-scale cross-and uni-modal contrastive learning. arXiv preprint arXiv:2508.00513. Cited by:

https://arxiv.org/html/2605.20032v1#A1.SS2.p2.1

https://arxiv.org/html/2605.20032v1#S2.p3.1

https://arxiv.org/html/2605.20032v1#S5.SS1.p2.1

https://arxiv.org/html/2605.20032v1#S5.SS2.SSS1.p1.1

C. Yang, H. Liu, D. Wang, Z. Zhang, C. Yang, and C. Shi (2025a) Flag: fraud detection with llm-enhanced graph neural network. In Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V. 2, pp. 5150–5160. Cited by:

https://arxiv.org/html/2605.20032v1#A1.SS2.p1.1

https://arxiv.org/html/2605.20032v1#S1.p1.1

https://arxiv.org/html/2605.20032v1#S1.p3.1

https://arxiv.org/html/2605.20032v1#S5.SS1.p1.1

J. Yang, R. Zhang, Z. Cheng, D. Cheng, G. Yang, and B. Wang (2025b) Grad: guided relation diffusion generation for graph augmentation in graph fraud detection. In Proceedings of the ACM on Web Conference 2025, pp. 5308–5319. Cited by:

https://arxiv.org/html/2605.20032v1#S1.p2.1

J. Yu, H. Wang, X. Wang, Z. Li, L. Qin, W. Zhang, J. Liao, and Y. Zhang (2023) Group-based fraud detection network on e-commerce platforms. In Proceedings of the 29th ACM SIGKDD conference on knowledge discovery and data mining, pp. 5463–5475. Cited by:

https://arxiv.org/html/2605.20032v1#A1.SS1.p1.1

https://arxiv.org/html/2605.20032v1#S1.p1.1

Y. Zhao, Y. Liu, Q. Chen, S. Li, Y. Tan, and S. Pan (2026) FedCIGAR: a personalized reconstruction approach for federated graph-level anomaly detection. In International Joint Conference on Artificial Intelligence, Cited by:

https://arxiv.org/html/2605.20032v1#S2.p2.1

Y. Zhao, Y. Liu, S. Li, Q. Chen, Y. Zheng, and S. Pan (2025) Freegad: a training-free yet effective approach for graph anomaly detection. In Proceedings of the 34th ACM International Conference on Information and Knowledge Management, pp. 4379–4389. Cited by:

https://arxiv.org/html/2605.20032v1#S2.p2.1

Appendix A Related work in details

A.1 Fraud Detection on Attributed Graph

Graph fraud detection (GFD) aims to identify fraudulent activities in real-world graph applications, such as financial fraud Li et al. \[

https://arxiv.org/html/2605.20032v1#bib.bib32

\] , fake reviews Yu et al. \[

https://arxiv.org/html/2605.20032v1#bib.bib18

\] , and spamming Hu et al. \[

https://arxiv.org/html/2605.20032v1#bib.bib19

\] . Earlier works treat GFD as a class-imbalance classification problem and incorporate techniques such as sampling Liu et al. \[

https://arxiv.org/html/2605.20032v1#bib.bib31

\] . However, camouflaged fraudsters bring unique challenges, as fraudsters can blend into benign communities in graph structure through heterophily edges Gao et al. \[

https://arxiv.org/html/2605.20032v1#bib.bib34

\] . As a result, later studies explicitly incorporate this knowledge into model design. For example, GHRN Gao et al. \[

https://arxiv.org/html/2605.20032v1#bib.bib34

\] directly prunes heterophily edges, while BWGNN Tang et al. \[

https://arxiv.org/html/2605.20032v1#bib.bib35

\] employs spectral GNNs to reduce the 'right-shift' phenomenon caused by fraudsters.

Despite their promising results, the reliance on labels restricts their applicability in unsupervised scenarios, which motivates early attempts to leverage graph anomaly detection (GAD) by treating fraudsters as outliers in graphs. To address this problem, early attempts have tried to utilize graph anomaly detection (GAD) methods to treat fraudsters as outliers in the graph. These methods can be broadly categorized into three paradigms: contrastive learning Liu et al. \[

https://arxiv.org/html/2605.20032v1#bib.bib14

\] , reconstruction Ding et al. \[

https://arxiv.org/html/2605.20032v1#bib.bib26

\] , and affinity-guided methods Pan et al. \[

https://arxiv.org/html/2605.20032v1#bib.bib27

\] . However, the camouflaged fraudsters can disrupt unsupervised learning objectives, resulting in issues such as anomaly overfitting and homophily traps He et al. \[

https://arxiv.org/html/2605.20032v1#bib.bib16

\] . Therefore, follow-up unsupervised GFD studies utilize heuristic assumptions to address camouflaged fraudsters. For example, TAM Qiao and Pang \[

https://arxiv.org/html/2605.20032v1#bib.bib13

\] and ADA-GAD He et al. \[

https://arxiv.org/html/2605.20032v1#bib.bib16

\] prune heterophily edges by iteratively computing pseudo-labels, while HUGE Pan et al. \[

https://arxiv.org/html/2605.20032v1#bib.bib3

\] establishes a label-free heterophily measure to guide the fraud detection.

A.2 Fraud Detection on Text-Attributed Graph

As many real-world graph applications are inherently associated with rich textual context, text-attributed GFD (TAGFD) has emerged as an important research direction. However, beyond structure-level blending, evolved fraudsters introduce new challenges through semantic camouflage, deliberately concealing malicious intent by imitating text generated by benign users. To address this, it is necessary to effectively utilize textual information. For example, LESS4FD Ma et al. \[

https://arxiv.org/html/2605.20032v1#bib.bib33

\] constructs heterogeneous graphs with rich semantic information to provide strong support for fake news detection. With the advancement of pretrained foundation models, DGB Li et al. \[

https://arxiv.org/html/2605.20032v1#bib.bib51

\] and GuARD Pang et al. \[

https://arxiv.org/html/2605.20032v1#bib.bib36

\] finetune a large language model(LLMs) to enable joint understanding of fraud patterns and graph structures. To improve efficiency, FLAG alternatively uses LLM as teachers to guide smaller detection models in learning discriminative patterns Yang et al. \[

https://arxiv.org/html/2605.20032v1#bib.bib22

However, in real-world applications, annotating semantically camouflaged fraudsters requires substantial manual effort, making unsupervised TAGFD methods increasingly important given rapidly expanding use cases. Despite their practical relevance, most existing attempts focus on artificial settings, namely text-attributed GAD benchmarks, and remain highly challenged by semantic camouflage. One line of work leverages the zero-shot capabilities of LLM. For instance, CoLL Xu et al. \[

https://arxiv.org/html/2605.20032v1#bib.bib29

\] incorporates LLMs to generate anomaly evidence from both textual content and graph structure to assist downstream anomaly detection. However, as evolved fraudsters deliberately mimic benign user behaviors, LLMs are often misled, resulting in incorrect or misleading evidence. Another line of methods integrates structural and textual information into unified graph contrastive learning frameworks Liu et al. \[

https://arxiv.org/html/2605.20032v1#bib.bib28

\]; Xu et al. \[

https://arxiv.org/html/2605.20032v1#bib.bib15

\] . Nevertheless, semantic camouflage typically introduces only small ego-neighbor divergence compared to the injected structure and feature anomalies Ding et al. \[

https://arxiv.org/html/2605.20032v1#bib.bib26

\] , which undermines the reliability of contrastive training objectives. These limitations motivate our work to address semantic camouflage in unsupervised TAGFD, thereby safeguarding graph applications against evolving fraudsters.

| 𝒱 | |\mathcal{V}|

| ℰ | |\mathcal{E}|

Table 4: Dataset statistics.

Appendix B Analyzing Collapse Risk of Training Objectives

While the rarity-driven training pipeline enables unsupervised learning in CAMERA, a careful reader may note that the one-class (OC) loss could potentially encourage trivial solutions, i.e., assigning uniformly zero fraud scores to all instances. In the following, we show that, provided the model is not overly over-parameterized, such collapse does not occur.

Assume the model has L L MoE layers. The final embedding of node v i v\_{i} can be expressed as

𝐡 i final = 𝐡 i \[ L − 1 \] + ∑ k g i , k \[ L \]  e k \[ L \]  ( 𝐡 i \[ L − 1 \] , 𝐀 ) , \mathbf{h}

{i}^{\mathrm{final}}=\mathbf{h}

{i}^{\[L-1\]}+\sum\_{k}g\_{i,k}^{\[L\]},e\_{k}^{\[L\]}(\mathbf{h}\_{i}^{\[L-1\]},\mathbf{A}),

and the OC loss is defined as

ℒ OC = \displaystyle\mathcal{L}\_{\mathrm{OC}}=

1 N  ∑ i = 1 N BCE  ( σ  ( ‖ 𝐡 i final ‖ 2 ) , 0 ) \displaystyle\frac{1}{N}\sum\_{i=1}^{N}\mathrm{BCE}\big(\sigma(|\mathbf{h}

{i}^{\mathrm{final}}|

{2}),0\big)

= \displaystyle=

− 1 N  ∑ i = 1 N log  ( 1 − σ  ( ‖ 𝐡 i final ‖ 2 ) ) \displaystyle-\frac{1}{N}\sum\_{i=1}^{N}\log\Big(1-\sigma(|\mathbf{h}

{i}^{\mathrm{final}}|

= \displaystyle=

− 1 N ∑ i = 1 N log ( 1 − \displaystyle-\frac{1}{N}\sum\_{i=1}^{N}\log\Big(1-

σ ( ∥ 𝐡 i \[ L − 1 \] + ∑ k g i , k \[ L \] e k \[ L \] ( 𝐡 i \[ L − 1 \] , 𝐀 ) ∥ 2 ) ) . \displaystyle\sigma(|\mathbf{h}

{i}^{\[L-1\]}+\sum

{k}g\_{i,k}^{\[L\]},e\_{k}^{\[L\]}(\mathbf{h}

{i}^{\[L-1\]},\mathbf{A})|

From this, it follows that minimizing ℒ OC \mathcal{L}

{\mathrm{OC}} is equivalent to minimizing the ℓ 2 \ell

{2} norm of the gating-weighted expert residuals:

min  ℒ OC ⟺ min  ∑ i ‖ ∑ k g i , k \[ L \]  e k \[ L \]  ( 𝐡 i \[ L − 1 \] , 𝐀 ) ‖ 2 . \min\mathcal{L}

{\mathrm{OC}};\Longleftrightarrow;\min\sum

{i}\Big|\sum\_{k}g\_{i,k}^{\[L\]}e\_{k}^{\[L\]}(\mathbf{h}

{i}^{\[L-1\]},\mathbf{A})\Big|

Therefore, to analyze potential collapse, we need to examine both the gating model and the experts to see if they could potentially collapse.

Statement 1: The gating model does not collapse. Although the interaction between the gating model and OC loss is complex, the gating mechanism employs a softmax function that ensures the expert weights sum to one. As a result, the gating model cannot trivially collapse to zero weight for all experts.

Statement 2: Experts do not trivially collapse. As both the expert loss and the OC loss encourage minimizing the output signal of experts, we analyze each expert using the expert loss to show why collapse is unlikely. Similar procedure can be applied to the OC loss.

- Graph expert: As expert loss minimizes the Euclidean distance between ego features and aggregated neighbor features, it can be seen as reconstructing the neighborhood features using ego information Roy et al. \[

https://arxiv.org/html/2605.20032v1#bib.bib38

- Global expert: The global expert is identical to the graph expert operating on a clique graph structure. Therefore, similar reconstruction statement holds.
- Semantic expert: The semantic expert directly employs an autoencoder to model benign patterns. By approximating the manifold of input data with limited parameters, the encoder acts as a denoiser Kingma and Welling \[

https://arxiv.org/html/2605.20032v1#bib.bib39

\] to capture the distribution of normal semantic.

In this sense, each expert is trained with an autoencoder-like loss that minimize the discrepancy to learn benign manifold, and return the discrepancy between ego and reconstructed features to highlight fraud-indicative cues. Therefore, despite the OC training objective, on an expert-level, it is as collapse-tolerant as an autoencoder-based anomaly detectors, which is widely utilized in anomaly and fraud detection tasks Ding et al. \[

https://arxiv.org/html/2605.20032v1#bib.bib26

\]; He et al. \[

https://arxiv.org/html/2605.20032v1#bib.bib16

Figure 7: Over-parameterization study on YelpChi and Amazon datasets.

Despite this intuition, the risk of overfitting to residuals remains, as sufficiently wide neural networks can approximate arbitrary functions Cybenko \[

https://arxiv.org/html/2605.20032v1#bib.bib17

\] . This can give rise to issues such as anomaly overfitting and homophily traps He et al. \[

https://arxiv.org/html/2605.20032v1#bib.bib16

\] in GFD, thereby reducing performance.. To study the effect of over-parameterization, we employ a two-layer MLP as the encoder for each expert and investigate how varying the hidden dimension affects results. As shown in Figure

https://arxiv.org/html/2605.20032v1#A2.F7

, CAMERA exhibits solid performance even when over-parameterized, demonstrating its robustness.

Appendix C Algorithm Description

The procedure of training and inference CAMERA is summarized in Algorithm

https://arxiv.org/html/2605.20032v1#alg1

Algorithm 1 CAMERA

Input: Text-Attributed graph G = ( 𝒱 , ℰ , 𝒯 ) G=(\mathcal{V},\mathcal{E},\mathcal{T}) , LLM: pretrained and frozen text encoder, E E : Training epochs, lr: Learning rate, α \alpha : weight for ℒ gating \mathcal{L}

{\text{gating}} , β \beta : weight for ℒ OC \mathcal{L}

{\text{OC}}

Output: Anomaly scores 𝐬 = { s 1 , … , s n } \mathbf{s}={s\_{1},...,s\_{n}}

1: Randomly initialize parameters of the ego-decoupled MoE layers f = f \[ 1 \] ∘ f \[ 2 \] ∘ … ∘ f \[ L \] f=f^{\[1\]}\circ f^{\[2\]}\circ...\circ f^{\[L\]} , where f \[ l \] f^{\[l\]} includes experts e k \[ l \] e\_{k}^{\[l\]} and the gating model g k \[ l \] g^{\[l\]}\_{k} , where k ∈ { graph , semantic , global } k\in{\text{graph},\text{semantic},\text{global}} .

2: 𝐇 \[ 0 \] ← LLM  ( 𝒯 ) \mathbf{H}^{\[0\]}\leftarrow\text{LLM}(\mathcal{T})

3: // Training phase

4: for e  p  o  c  h = 1 , … , E epoch=1,...,E do

5: ℒ expert ← 0 \mathcal{L}\_{\text{expert}}\leftarrow 0

6: ℒ gating ← 0 \mathcal{L}\_{\text{gating}}\leftarrow 0

7: for l = 1 , … , L l=1,...,L do

8: 𝐇 \[ l \] ← f \[ l \]  ( 𝐇 \[ l − 1 \] , A ) \mathbf{H}^{\[l\]}\leftarrow f^{\[l\]}(\mathbf{H}^{\[l-1\]},\textbf{A})

9: ℒ expert ← ℒ expert + ∑ k 1 N  ∑ i = 1 N ‖ e k \[ l \]  ( 𝐡 i \[ l − 1 \] , 𝐀 ) ‖ 2 2 \mathcal{L}

{\text{expert}}\leftarrow\mathcal{L}

{\text{expert}}+\sum\_{k}\frac{1}{N}\sum\_{i=1}^{N}|e\_{k}^{\[l\]}(\mathbf{h}

{i}^{\[l-1\]},\mathbf{A})|

10: ℒ gating ← ℒ gating + ∑ k − 1 N  ∑ i = 1 N g i , k \[ l \]  log  ( g i , k \[ l \] + ϵ ) \mathcal{L}

{\text{gating}}\leftarrow\mathcal{L}

{\text{gating}}+\sum\_{k}-\frac{1}{N}\sum\_{i=1}^{N}g\_{i,k}^{\[l\]}\log(g\_{i,k}^{\[l\]}+\epsilon)

11: end for

12: Compute 𝐬 \mathbf{s} , where s i = σ  ( ‖ 𝐡 i L ‖ 2 ) s\_{i}=\sigma(|\mathbf{h}^{\text{L}}

13: ℒ OC = 1 N  ∑ i = 1 N BCE  ( s i , 0 ) \mathcal{L}

{\text{OC}}=\frac{1}{N}\sum

{i=1}^{N}\text{BCE}(s\_{i},0)

14: ℒ = ℒ expert + α  ℒ gating + β  ℒ OC \mathcal{L}=\mathcal{L}

{\text{expert}}+\alpha\mathcal{L}

{\text{gating}}+\beta\mathcal{L}\_{\text{OC}}

15: Update model f f by back-propagating ℒ \mathcal{L} with learning rate lr.

16: end for

17: // Inference phase

18: 𝐇 \[ L \] ← f  ( 𝐇 \[ 0 \] , A ) \mathbf{H}^{\[L\]}\leftarrow f(\mathbf{H}^{\[0\]},\textbf{A})

19: Compute 𝐬 \mathbf{s} , where s i = σ  ( ‖ 𝐡 i L ‖ 2 ) s\_{i}=\sigma(|\mathbf{h}^{\text{L}}

20: return 𝐬 \mathbf{s}

Appendix D Complexity Analysis

We discuss the time complexity of each component in CAMERA. Let n n and m m denote the number of nodes and edges in the input graph, respectively. The textual encoder maps raw text attributes to node embeddings with a cost of 𝒪  ( n ) \mathcal{O}(n) . In each training epoch, the GNN in the graph expert costs 𝒪  ( m ) \mathcal{O}(m) to perform message passing, while the semantic expert and global expert have a complexity of 𝒪  ( n ) \mathcal{O}(n) . The context-informed gating model computes expert weights based on ego and neighborhood embeddings, which requires an additional 𝒪  ( m + n ) \mathcal{O}(m+n) cost for neighborhood aggregation and linear projection. As the computation of anomaly score and loss operates in 𝒪  ( n ) \mathcal{O}(n) complexity, the overall per-epoch training complexity is 𝒪  ( L  ( m + n ) ) \mathcal{O}(L(m+n)) , where L L denotes the number of MoE layers. Overall, CAMERA scales linearly with the number of nodes and edges, making it suitable for real-world large-scale TAGFD scenarios.

Appendix E Dataset and Implementation Details

AmazonVideo

learning rate

Table 5: Hyperparameter settings.

Detailed statistics of the datasets are summarized in Table

https://arxiv.org/html/2605.20032v1#A1.T4

. All experiments are conducted on a Windows desktop equipped with 32 GB RAM and an RTX 4090 GPU with 24 GB VRAM. For implementation details of CAMERA, we stack two MoE layers, where each expert is implemented with a single corresponding encoder layer. The hyperparameter settings are reported in Table

https://arxiv.org/html/2605.20032v1#A5.T5

Figure 8: Grid search results for α \alpha vs. β \beta (surface height indicates AUROC).

Appendix F Addition Experiments Results

F.1 Sensitivity

To investigate the effect of the hyperparameters α \alpha and β \beta , we perform a grid search for them. As illustrated in Figure

https://arxiv.org/html/2605.20032v1#A5.F8

, different datasets require different hyperparameters. The grid search results are shown in Figure

https://arxiv.org/html/2605.20032v1#A5.F8

. Overall, the performance varies smoothly across the search space, indicating that the proposed method is not overly sensitive to these hyperparameters. This robustness is particularly desirable in unsupervised TAGFD, where labeled data for validation purposes are unavailable. Hence, the observed stability further supports the practicality of CAMERA in real-world scenarios with diverse and evolving fraud patterns.

Experimental support, please

view the build logs

https://arxiv.org/html/2605.20032v1/\_\_stdout.txt

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

