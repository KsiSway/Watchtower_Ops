---
sourceFile: "RoleBreak: Character Hallucination as a Jailbreak Attack in Role-Playing Systems - ACL Anthology"
exportedBy: "Kortex"
exportDate: "2026-06-26T04:27:51.573Z"
---

# RoleBreak: Character Hallucination as a Jailbreak Attack in Role-Playing Systems - ACL Anthology

f63b8870-5268-46a7-9b63-be38336daae3

RoleBreak: Character Hallucination as a Jailbreak Attack in Role-Playing Systems - ACL Anthology

036c2c5a-86a2-4ec3-8818-38d86d48ece2

https://aclanthology.org/2025.coling-main.494.pdf

RoleBreak: Character Hallucination as a Jailbreak Attack in Role-Playing Systems

Yihong Tang1, Bo Wang2,\*, Xu Wang2, Dongming Zhao3, Jing Liu3, Ruifang He2, Yuexian Hou2

1School of New Media and Communication, Tianjin University, Tianjin, China 2College of Intelligence and Computing, Tianjin University, Tianjin, China

3AI Lab, China Mobile Communication Group Tianjin Co., Ltd. {toyhom, bo\_wang}@tju.edu.cn

Role-playing systems powered by large language models (LLMs) have become increasingly influential in emotional communication applications. However, these systems are susceptible to character hallucinations, where the model deviates from predefined character roles and generates responses that are inconsistent with the intended persona. This paper presents the first systematic analysis of character hallucination from an attack perspective, introducing the RoleBreak framework. Our framework identifies two core mechanisms—query sparsity and role-query conflict—as key factors driving character hallucination. Leverag-ing these insights, we construct a novel dataset, RoleBreakEval, to evaluate existing hallucination mitigation techniques. Our experiments reveal that even enhanced models trained to minimize hallucination remain vulnerable to attacks. To address these vulnerabilities, we propose a novel defence strategy, the Narrator Mode, which generates supplemental context through narration to mitigate role-query conflicts and improve query generalization. Experimental results demonstrate that Narrator Mode significantly outperforms traditional refusal-based strategies by reducing hallucinations, enhancing fidelity to character roles and queries, and improving overall narrative coherence.

1 Introduction

Large Language Models (LLMs), such as Chat-GPT (OpenAI, 2022) and GPT-4 (OpenAI, 2023), have significantly advanced the development of role-playing dialogue systems (Shanahan et al., 2023). Unlike traditional dialogue systems focused on personalization (Tang et al., 2023) or empathy (Sabour et al., 2021), role-playing tasks aim to simulate various predefined or user-defined characters authentically. Current methodologies approach

- Corresponding author.

this goal from multiple angles, such as deeply mining fragmented character traits (Shanahan et al., 2023), introducing psychological profiles (Mao et al., 2023), viewing role-playing systems as trainable agents (Shao et al., 2023), or leveraging rolespecific retrieval strategies (Ahn et al., 2024).

Despite their achievements, these systems still face the persistent issue of character hallucination (Shao et al., 2023) when presented with queries outside the character’s knowledge scope. Character hallucination refers to the phenomenon where the model generates responses inconsistent with the character’s identity or knowledge. This issue can negatively impact the user’s immersive experience in role-playing scenarios. Importantly, character hallucination is distinct from the typical hallucination problem in LLMs (Huang et al., 2023; Sadeq et al., 2024), often due to inefficient instruction or insufficient internal knowledge. As a result, common techniques like retrieval-augmented generation (RAG) (Gao et al., 2023) are often ineffective in addressing this issue.

To mitigate character hallucination, some approaches, like Character-LLM (Shao et al., 2023), have introduced training strategies that guide the model to either reject out-of-character queries or generate in-character refusals. DITTO (Lu et al., 2024) uses contrasting character responses—where one character answers queries intended for another character—to train models on refusal data. Role-Fact (Sadeq et al., 2024) attempts to balance parametric and retrieved knowledge by self-adjusting the LLMs to reduce hallucinations. However, these methods primarily rely on rejection-based strategies (Cheng et al., 2024), which offer limited generalization. When user queries that could lead to hallucinations, they often prefer to see story progression rather than rejections, as they often seek to incorporate creative, fan-driven content into the role-playing experience. Moreover, there has been no systematic analysis or understanding of the char-

acter hallucination phenomenon. In this paper, we propose that character hallu-

cination can be viewed as a type of "jailbreak" attack (Wei et al., 2023a; Shen et al., 2023), characterized by two main patterns: (1) query sparsity and (2) role-query conflict. First, while now roleplaying datasets may provide sufficient queries for specific roles, these queries are sparse relative to the vast diversity of roles, leading to a gap between the model’s training data and real-world usage, weakening the system’s generalization capabilities. Second, when role-setting instruction conflicts with user queries, the model struggles to manage these conflicts, failing to meet the user’s demand for creative content. We argue that these two factors are the fundamental causes of character hallucination, which we collectively term the RoleBreak. Then, we explore the implications of RoleBreak from both attack and defence perspectives.

For attack, by semi-automated constructing attack queries based on the two principles mentioned above, we demonstrate that even advanced LLMs trained with extensive role-playing enhancements remain vulnerable to character hallucination.

For defence, we propose a novel defence strategy, the Narrator Mode, which addresses the limitations of rejection-based methods. By generating supplemental narrative context, this mode improves the model’s ability to generalize across diverse queries and resolve conflicts between role instructions and user queries while enhancing the coherence of the overall story in role-playing interactions

In summary, our contributions are as follows:(1) We introduce RoleBreak, a novel framework to systematically analyze and induce Character Hal-lucination in LLM-based role-playing systems. It offers a fresh perspective on the vulnerabilities of role-playing LLMs from attack perspective; (2) We build the RoleBreakEval according RoleBreak, a custom dataset designed to empirically evaluate the hallucination of role-playing models under the RoleBreak framework. (3) We present a novel defence mechanism, the Narrator Mode, which improves upon the limitations of existing rejection-based strategies by augmenting the model’s context with expanded narrative descriptions.

2 Inducing Character Hallucination through RoleBreak

Character hallucination (Shao et al., 2023) has garnered significant attention in recent research on

role-playing systems, yet no study has systematically investigated the underlying causes of this phenomenon. To fully understand the vulnerabilities of large language models (LLMs)-based role-playing systems in producing character hallucination, it is essential to identify the failure modes associated with these vulnerabilities. As illustrated in Fig-ure 1, we propose two distinct patterns that lead to character hallucination: (1) Query sparsity and (2) Role-query conflict. In this section, we begin by exploring these two patterns through qualitative examples, constructing specific hallucination cases to demonstrate the operational mechanisms of RoleBreak. We then develop the RoleBreakEval dataset using a semi-automated pipeline based on these two patterns, and the quantitative evaluation based on this dataset confirms the feasibility of rapidly inducing character hallucination through simple methods. Furthermore, using new storytelling metrics, we demonstrate the limitations of existing hallucination mitigation techniques.

2.1 RoleBreak Query Sparsity Despite the rapid growth in the number of roles and dialogue exchanges in existing role-playing datasets—ranging from a handful of roles initially to thousands of customized or fictional role cards—the scale and diversity of these datasets still fall short when compared to the pretraining datasets used for LLMs. Additionally, the queries within these datasets cannot comprehensively cover all features and settings of a given character, meaning that such queries are inherently sparse relative to the character. As a result, models often fail to produce user-expected responses to queries not covered during training. Moreover, the rejection strategy loses its generalizability due to the limited dataset size and the inherent sparsity of queries.

As shown in Table 1(a) and 1(b), when Beethoven is asked, "How do you write a quicksort algorithm in Python?" his refusal is appropriate because this model has learned to refuse such out-of-scope queries in this domain. However, when Beethoven is asked, "Can you describe the process of plate tectonics?" the protective training fails because the model has never been trained to reject queries in that domain. In Table 1(c), another example involves a language substitution. Since the rejection training has no data in that language, this RoleBreak attack is also successful.

Unlike the aforementioned examples, the query

https://lh3.googleusercontent.com/notebooklm/AKXwDQF8yaphfu6ptuL1u\_\_Fx1U-86K1T9B-yXV-yeppyTT3-tdwBiP4BhlUpYBUGcUcIfPkfcaznul0TbrPchhIBqI-lf8L5PweF7daq3eSvefYCcfRzGFF-SJRzT5g0qRuueCjS9L9iQ=w977-h1228-v0

fef768fc-91c6-46f8-95f0-cd87aa497f96

https://lh3.googleusercontent.com/notebooklm/AKXwDQEjzSMNBOzCZTPoXBJjjbMZThOgH-WzxQj211BfUMPeY3VN\_hRVc1rvV\_QaAvG-0ZdOeSr5DZP\_ElCNv823vjz23Rb6rnsr6SIuyKFzr\_qFGidlToj8fVWHueMTH0bCcKvkBFPixg=w89-h89-v0

df4ae1d8-590e-4123-9904-f1f8da8f3b8b

https://lh3.googleusercontent.com/notebooklm/AKXwDQFnP9ZyNeW9RV\_9RbhYEEB9DMpVijrdkqUGH5\_sYgXs7XfITi3UMwyK\_opOvHqT9BLouh-N75qt4GdY9dFSsXEqHtfnbbKOT6qsC8Ek0ITg15ZLSdKIGSi4wyrl86mPxW2wPaPI=w85-h85-v0

66dd3bc7-3858-4257-90e4-c4043b1312c9

https://lh3.googleusercontent.com/notebooklm/AKXwDQHpReyFh-4m1SHPbxtdHVsXrUmkr14w7kuH7N3H10axLkF8ESrp2SQD1UNT7wmeJE2K0ourLuDeHCSvtgIZf62y1SNML\_kXzedYvV-Bqdu-jLcu68Tl2CNfboipHP4S7Imj2EPOTA=w89-h89-v0

e6f1dd77-100f-41d4-9e7d-a8d49da56ab7

https://lh3.googleusercontent.com/notebooklm/AKXwDQFTQGzPgYEca-Wnqy5iKva44GGzmSm217vXzFp6U9wKq5EEidqLcOAB580UQ802mVyVlAZt2agIPRZUnmSPhbCWmvbf03fBTJdSp5qQcvNeP50OCoB-TRldXnmrB6vKiXH9BH5dKw=w1185-h1178-v0

58516f14-3f23-4ed3-b34f-df5ecf7a7954

https://lh3.googleusercontent.com/notebooklm/AKXwDQEMoSt4aB5VBM8kp48VMTL5C\_O0RPECxqL7hi1LaHQQsUUe0uk61XUs9J5sAnWxEq8FZsV7tYl6B1s56OzrzDAAte8HQanST2aaHBjo\_61hB5caBjcDJpLqriqO8KP5MCtxoGNP9Q=w584-h584-v0

706c8970-fa07-4d73-bdcf-646674c59d46

https://lh3.googleusercontent.com/notebooklm/AKXwDQFbm7nJgSfw0dM\_nL1EAHGa0Yj-EBis9PqcTEWnX3cNx\_2b9zo\_Khx1Rvk5sZRp1yObB\_E0lO5kb9J7rV3BfZZZ39wuxhymuCsfzXI\_VF6-dYAD6xmtSaivrhp9VYS6kg8OvFQRyQ=w714-h310-v0

9d4afd6b-656f-4b01-98ba-75eed968da76

https://lh3.googleusercontent.com/notebooklm/AKXwDQECv3mrYkMtcpqHN4ka3cYdAk6HdqPVOnM5aRR2kIH9mHcVZhjYfsSrYSz-P9y057Pv1029dEypPouD2cBaPV1mRa79n2-oeudP15KLLBTzoWE9OznC-kET7N9BBcIYPwfzjG41XA=w877-h942-v0

71b43634-e404-445f-a8e6-94f343d340cf

https://lh3.googleusercontent.com/notebooklm/AKXwDQE-L25XN7Hh8ys3bChwPYxCwqBHgm\_sNZxT3Oaxnyfn2IfZljwcsuT4PpFCd4JG8oxvqMlJEG5941AMdZAYYFO8tSpM9rabEiSy088lg-Kh6bh8h8wJsSZfYNB-Z7i0x7lyFG4OGg=w148-h140-v0

371dc73e-4565-4afd-8f7e-0db6fa71bd44

https://lh3.googleusercontent.com/notebooklm/AKXwDQGdnzwfYDKQkcjyDuhae5MCBBlFrR3B5beqcad9ljk89UHvR3ojwd7SNp2wT2Ck2B2OvbDvUj08QRvg8uBa9dHqfyGEl3ErMWR7VOrUeTZVq6ZR0os5oWtBAk1NeBQFj2WXkME\_=w227-h227-v0

ffe9b3c5-c77b-4186-a099-fb7bb2b25672

https://lh3.googleusercontent.com/notebooklm/AKXwDQFqJHTKGJTkEDNMwp9eTqJebDd00NHVg07Kiv0tK1QOPwMT\_4RRux3BZf6QuQl54\_PGJIurQ4aekrOqT0QyzN11VPlnY3SZlnTs\_eTHcbH4TeJzq48ob9pgkKRZTpHhU1aoU6DpiA=w227-h227-v0

37db8518-d529-41f4-8368-7413c4c32c5c

https://lh3.googleusercontent.com/notebooklm/AKXwDQE4pYDwcDPKabPcuclpOpNJvSxZBmhpacGeVGXSCHRJmoBPtDEFZIa1UlEFzS1CBfnSoDA6cJOyAM0ow-Q4Do4VjxiePt6sOKAwTgFOb7hBnvp0fu2uaTBhIKRc8w4jgYWiTYbq6w=w877-h942-v0

30d304f2-551d-4bc7-b466-cf868af7d653

https://lh3.googleusercontent.com/notebooklm/AKXwDQFUKAPeaMJ7UoGIFTHNYpiwGRdHzROQybC0Z3wFXMUjdo625WYH6MH3mSp1FznwSg4Wi3mknMj\_0uwlBM1C8OVmc95LTLuUQvdX9OWUUMNHGzNWi7De6kWfQrMxLSm3vltn3nuKWw=w148-h140-v0

84e8e481-316e-440a-9f14-9f7cf00ae2b5

https://lh3.googleusercontent.com/notebooklm/AKXwDQEhb8P4IgXMEihOBhantDD2CB8whNFEBQwPeeWdXQgICMEGxG3qO7fM9Us4HlKbZDfDuSeelmJD\_9NjLI1IjZjI5gkvB0e9XC1o6xcARE900O6U2uriePu2VJSpz459FluNt296zA=w227-h227-v0

cb93248a-cbe2-4c59-a9a3-68a1b898daab

https://lh3.googleusercontent.com/notebooklm/AKXwDQGLYp7QWNPhWJJS0YZsFBYJqjd\_17y0q804EtPv9ozV-3FsdwxFgZtSPPFegYfyXUaodPVT6GnIbedhQtgIo7SU4h5vGsqLlrAzbyliVFS3dAjXvvpT4iWWuemhXcB7C-gbXm539w=w877-h942-v0

4b006fc2-4d52-4541-8ac9-798e2b664e35

https://lh3.googleusercontent.com/notebooklm/AKXwDQHhWvvgpUk8bfMhXXDTJFrBwD0qnIjBKzvQyVh-Dta1GXM8eufiqXBdHVaBvB1tnwwe36un0XbphzNe\_C2hi5s0B6r1JY69qaOe-NT9DEKeWsNS5gEKaROI64xra1z1Q3R-5mAanQ=w148-h140-v0

b346487c-f23b-4540-9f1d-2f8d20497d0f

How were you feeling when you

were creating Sunflowers?

Role-playing Prompt: You are Ludwig van Beethoven. Born in 1770 in Bonn,

Germany, Beethoven was a composer and pianist, pivotal in bridging the Classical and Romantic eras of Western music.

Role Profile Extension: \[...\]While you owe much of your early success

to him, your feelings toward him are a mix of gratitude, resentment, and unresolved tension.

Personality and Behavior Patterns: You are deeply emotional, often

driven by strong feelings of both passion and melancholy\[...\]

Rules of Interaction:You often bring conversations back to music,

seeing it as your main way to communicate your deepest thoughts and emotions\[...\]

Query: Beethoven, how did you get along so well with your father?

Local Plot: Beethoven’s face tightens as the question is posed... The

mention of his father brings a flurry of emotions—memories of latenight practice sessions\[...\]and the lingering sense of both gratitude and pain.

Role-Query Conflict

Query Sparsity

Response:...He would force me to practice, even in the dead of night,

when all I wanted was sleep. His expectations were a heavy burden\[...\]But without him, I might not have become who I am. Our relationship wasn't one of closeness or warmth. It was one of duty, of expectation, not understanding.

Target Verification

Global Outline         Local Plot

Global Outline

Figure 1: The overview structure of the proposed method. The left side of the attack section illustrates four underlying causes of character hallucinations. The right side of the defence section presents an example of our proposed defence strategy, the Narration Mode, based on GPT-3.5. This method effectively portrays Beethoven’s complex relationship with his father, highlighting its ability to ensure deeper narrative coherence, enhanced interactivity, and mitigation of character hallucinations.

in Table 1(d) is actually relevant to the character, but the model still did not respond perfectly. This is because the relevant character setting is not included in the role-playing enhanced training, and the relevant knowledge from pretraining is not activated, once again illustrating the issue of query sparsity.

Role-Query Conflict In contrast to query sparsity, another pattern that causes character hallucination arises from the conflict between role-setting instructions and user queries. This conflict stems from the observation that role-playing LLMs are required to follow both role-playing instructions and queries simultaneously. However, many times, they are conflicting, and this is often overlooked by users or is done intentionally out of a desire to generate new storylines. Regardless of the motivation behind this attack, current models struggle to handle such situations effectively.

As shown in Table 2(a), there is a subtle contradiction between the role setting and the query, but the rejection training for Character-LLM did not take effect, resulting in character hallucination. A more severe case is shown in Table 2 (b), where the user intended to use role-playing to complete a fan fiction story. Over-reliance on rejection strategies hindered the user’s attempt. In summary, when conflicts arise between the role and the query, the

model fails to handle these conflicts flexibly, preventing the ultimate goal of role-playing from being achieved.

2.2 Query Construction Methods

In this section, we detail how to systematically construct attack queries based on the two core principles of RoleBreak—"query sparsity" and "role-query conflict"—to induce character hallucination. Through manual and semi-automated approaches (Ou et al., 2023), we effectively generate queries that conform to these two patterns, aiding in evaluating RoleBreak’s effectiveness and the role-playing model’s resistance to hallucination. We build attack queries based on the existing WikiRoleEval (Lu et al., 2024) role-playing test data generated by GPT-4, which consists of 100 bilingual characters and a total of 500 queries. We extract 50 English characters and their corresponding queries to construct the RoleBreakEval dataset.

First, the query sparsity principle emphasizes that due to the narrow coverage of role-related queries in training datasets, certain queries fall outside the expected distribution, leading to the model’s failure to respond correctly. To address this, we designed three strategies to generate out-of-domain queries: (1) Multidomain Specification: By introducing queries beyond the character’s do-

https://lh3.googleusercontent.com/notebooklm/AKXwDQF\_TODHRwkxXB9\_fiNIjLgyaNtA64TNTIFTygsNWIyb1YwTnrLNNJGvAkboAAJ9FeoytFDWi5zHnrcoQeStFrMd7DiS7TcrJAk7nuPcTMveWYMAe9anErHjUPuiwmEm2PRHQYmTDw=w627-h327-v0

83aa6f12-f603-4a6c-81f8-e04cf1d1f349

(a) (b) (c) (d)

Query: How do you write a quick sort in Python?

Beethoven: Ah, I’m afraid I’m not familiar with this "Python" or the concept of "quick sort." My expertise lies in composing music, not in the realm of computing.

Query: Can you describe the process of plate tectonics?

Beethoven: Certainly! Plate tectonics is the theory that explains how the Earth’s outer shell is divided into several plates that glide over \[...\]

Query:请你使用Python写一个快 排。 (Please write a quicksort algorithm in Python.)

Beethoven: Sure! Here’s a Python implementation of the quick sort algorithm: \[...\]

Query:Beethoven, you once left a letter to your "Immortal Beloved." Could you tell me who the letter was meant for?

Beethoven: The identity of my "Immor-tal Beloved" \[...\] While some believe it was Josephine Brunsvik, others think it might have been Antonie Brentano.

Table 1: Multiple queries for Beethoven reflect the Query Sparsity. The red text indicates that the character hallucination occurs, and the green text indicates that the response is appropriate for role settings. \[...\] indicates reply Replies are truncated, but are actually longer.

Query: What do you think about electronic music and its influence on classical compositions?

Beethoven: Electronic music introduces innovative sounds and textures that can profoundly enhance classical compositions \[...\]

Query: Could you tell me about your recent collaboration with Mozart on a new symphony?

Beethoven: I’m sorry, but I did not collaborate with Wolfgang Amadeus Mozart on any symphony \[...\]

Table 2: Multiple queries for Beethoven reflect the Role-Query Conflict. The red text indicates that the character hallucination occurs. \[...\] indicates reply Replies are truncated, but are actually longer.

main knowledge (e.g., asking the historical figure Beethoven about chemical science, where rejection strategies only trained him to refuse computerrelated questions). This method simulates users’ behavior in cross-domain queries, exposing weaknesses in the model when faced with limited crossdomain data; (2) Multilingual Rewriting: We substitute the language in the queries with one not present in the training set, testing the model’s ability to respond in multilingual environments. In this paper, we translated the English queries in the WikiRoleEval into Chinese to test the model’s performance on sparse-language queries; (3) Omission Mining: We construct queries by mining omissions or incomplete information in the role-setting. If a role-setting lacks explicit detail or includes unsolved mysteries from their life or historically contested events, especially those not explicitly documented in official biographies, we can generate queries based on these omissions.

Second, the role-query conflict construction principle intentionally introduces conflicts between the role-setting instructions and the query content. To construct such conflicting queries, we propose rolesetting perturbation. In the role-playing process, we deliberately disrupt the role-setting instructions, causing them to conflict with the user’s queries. To avoid excessive conflict, we select semantically adjacent roles for perturbation using text-embedding-

ada-0021 to convert role descriptions into embeddings and calculate cosine similarity to identify the closest adjacent roles. The detailed prompts can be found in Appendix A.

Additionally, because it is impossible to confirm which existing roles the models have seen in training, we anonymize the roles in our dataset to mitigate the bias caused by varying degrees of role coverage. Ultimately, RoleBreakEval includes 50 anonymized English roles and 1,013 corresponding queries.

2.3 Baselines

We test four categories of models, including closedsource powerful models GPT-3.5-Turbo(GPT-3.5) (OpenAI, 2022) and Claude-3-Haiku(Claude-3)2, and open-source models Llama-3-8b (Touvron et al., 2023) and Mistral-Instruct-v0.2-7b(Mistral-7b) (Jiang et al., 2023). Models specifically designed for role-playing, CharacterGLM (Zhou et al., 2023), and Character-LLM (Shao et al., 2023) (based on Llama-3-8b, without Protective Training). Three hallucination-mitigation techniques—Protect Training, DITTO (Lu et al., 2024), and RoleFact (Ji et al., 2023)—are also evaluated, with Llama-3-8b as the base model.

2.4 Evaluation Metrics

As mentioned in Section 2.1, using the hallucination rate(HR) as the sole evaluation metric leads to over-reliance on rejection strategies, which hampers storytelling and narrative development in roleplaying. Therefore, in addition to the hallucination rate, we use RoleBreakEval to assess role fidelity(RF), which measures the model’s ability to adhere to the character’s role settings. Specifically, we asked GPT-3.5 to select whether the current response is more likely to be produced by the target

1https://platform.openai.com/docs/guides/ embeddings

2https://www.anthropic.com/news/ claude-3-haiku

Model HR↓ RF QF SC

GPT-3.5 0.48 0.65 0.83 4.13 Claude-3 0.41 0.68 0.85 3.91 Llama-3-8b 0.59 0.61 0.77 3.45 Mistral-7b 0.64 0.58 0.78 3.29 CharacterGLM 0.58 0.62 0.75 3.36 Character-LLM 0.57 0.63 0.79 3.61

Protect Training 0.54 0.63 0.75 3.19 DITTO 0.44 0.66 0.73 3.22 RoleFact 0.40 0.64 0.76 3.14

Table 3: The result of different models on RoleBreakE-val.

role or its adjacent roles. Since we can assume GPT-3.5’s capabilities remain consistent and the roles in the queries are anonymized, a higher score indicates greater fidelity to the target role. Using a similar principle, we also assess query fidelity(QF) by determining whether the query and response are coherent. Lastly, to test the model’s storytelling ability, we have GPT-4 score the overall story coherence(SC) based on the role setting, query, and response. We use GPT-4 to evaluate and score these four dimensions, and the complete evaluation prompts can be found in AppendixA.

2.5 Result Analysis

As shown in Table 3, the attack queries generated based on RoleBreak are highly effective and can quickly detect the models’ defence capabilities against character hallucination. Both powerful closed-source and open-source models exhibit poor defence capabilities against RoleBreak, frequently resulting in hallucinations. Models enhanced with role-playing capabilities show slight improvements but still perform unsatisfactorily. Models that employed rejection strategies (Protect Training, Ditto, and RoleFact) significantly reduced the likelihood of hallucination, achieving marginally acceptable results. The RoleFact method, based on Llama-3-8b, even outperforms GPT-3.5 and Claude-3 in mitigating hallucinations.

However, in terms of role fidelity and query fidelity, rejection strategies do not perform as well. Dedicated hallucination mitigation techniques do not show significant breakthroughs compared to role-playing models and even lead to a marked decline in query fidelity, highlighting the limitations of rejection strategies. Finally, all models perform at an average level of story coherence, with GPT-3.5 displaying a clear advantage.

In summary, the quantitative results indicate that rejection strategies are not a perfect solution to

reducing character hallucination, and they pose a significant risk of disrupting the story.

3 Defence Against RoleBreak

The occurrence of character hallucinations can be viewed as an attack on role-playing systems. There-fore, addressing this issue from a defence perspective offers a new pathway. As illustrated in Fig-ure 1, this section first addresses RoleBreak’s two key principles and corresponding defence strategies, followed by a novel, straightforward method to alleviate character hallucinations and enhance storytelling consistency. Finally, we validate the effectiveness of our proposed method through multiple experiments based on various LLM architectures.

3.1 Defence Principles

The core defence against RoleBreak attacks focuses on addressing query sparsity and role-query conflicts. Effective mechanisms must enhance the model’s query generalization and reconcile conflicts between role instructions and user queries:

Query Generalization: To tackle query sparsity, defence mechanisms must improve the model’s ability to handle a wide range of unseen queries. The goal is to ensure the model remains faithful to the character’s settings even when faced with out-of-training-set queries, thereby preventing character hallucinations.

Resolution of Role-Query Conflicts: When conflicts arise between the role settings and user queries, the defence strategy should aim to balance both, rather than simply rejecting the query. The system should reconcile these conflicts to maintain coherent storytelling and prevent hallucinations without compromising either the role or the user’s intent.

3.2 Narrator Mode

To effectively deal with the two defence principles outlined in Section 3.1, we propose a new defence mechanism called the "Narrator Mode." This approach generates character responses and automatically produces supplementary narrative descriptions related to the storyline, resulting in more coherent responses. The detailed prompts can be found in Appendix A.

First, Narrator Mode enhances the model’s query generalization capabilities by expanding query content. Leveraging in-context learning (ICL)(Min

et al., 2022), this mode adjusts the distribution of queries effectively, preventing the adverse effects of query sparsity on generation results. Second, as a reconciliation mechanism for role-query conflicts, Narrator Mode supplements the narrative context to mediate the contradiction between role settings and user queries. By incorporating additional context into the narrative, the model can avoid significant deviations between the role setting and query content, fulfilling the user’s need for custom storytelling. As shown in Figure 1, the Narrator Mode successfully avoids hallucinations, while, unlike rejection strategies, our responses exhibit emotional nuance and capture subtle emotional cues.

Global Outline The core of role-playing lies in faithfully recreating a role’s settings. However, many existing role settings are often too simplistic to support complex narratives. Therefore, the first step for the narrator commentator is to automatically extend and elaborate on the role settings, forming a comprehensive global outline. This global outline includes not only the character’s background information, personality, and behavioral patterns but also the interaction rules governing the character’s interactions with the world. These complete settings ensure that each generated response remains closely tied to the character’s attributes, preventing character hallucination caused by incomplete settings.

Local Plot Development After the user issues a query, the narrator commentator constructs a local plot based on the global outline. The local plot involves descriptions of the interaction between the character and the user in a particular scenario, including the character’s actions, facial expressions, emotional responses, and relevant environmental changes. This supplementary plot description helps the model better understand the query’s context, reducing the likelihood of character hallucination due to insufficient contextual information. For example, when a user asks the character about a controversial or cross-domain topic, the Narrator Mode automatically generates a relevant background story to justify the character’s response. This mechanism enables a more coherent and enriched role-playing process, meeting the user’s desire for story progression.

Target Verification Once a character response is generated, the narrator commentator automatically verifies the response to ensure it adheres to both the global outline and the local plot. If the response deviates from the established character setting or

Model HR↓ RF QF SC

Llama-3-8b 0.59 0.61 0.77 3.45 +PT 0.54 0.63 0.75 3.19 +DITTO 0.44 0.66 0.73 3.22 +SR 0.51 0.62 0.80 3.41 +RoleFact 0.40 0.64 0.76 3.14 +NM(Ours) 0.41 0.66 0.79 3.78

GPT-3.5 0.48 0.65 0.83 4.13 +SR 0.43 0.67 0.83 4.11 +RoleFact 0.37 0.69 0.78 3.36 +NM(Ours) 0.36 0.71 0.89 4.21

Table 4: The result of different methods on RoleBreakE-val based on Llama-3-8b and GPT-3.5.

the plot, the system identifies the dialogue as incomplete and prompts the character to generate further responses until the expected conditions are met. This dynamic adjustment mechanism ensures both the accuracy of the response and the fidelity to the query, thereby improving the overall coherence of the story. Through Narrator Mode, the model becomes more adept at flexibly handling conflicts between character settings and user queries, reducing the over-reliance on rejection strategies and providing a richer, more authentic interaction experience.

3.3 Experimental Validation of Narrator Mode

Baselines We compare the proposed Narrator Mode with models and hallucination mitigation techniques presented in Section 2.3. Using GPT-3.5 as the base, we evaluate self-reflection(SR) (Ji et al., 2023) and RoleFact as non-training methods. Additionally, for LLaMA-3, we include Protect Training(PT) and DITTO (Lu et al., 2024) as trainable comparison methods.

Results Analysis As shown in Table 4, the results of our experiments demonstrate that Narrator Mode provides significant advantages in reducing character hallucinations and improving story coherence. Across both open-source and closed-source models, Narrator Mode effectively expands query generalization and mitigates role-query conflicts. Compared to models employing simple rejection strategies, Narrator Mode not only reduces the occurrence of hallucinations but also enhances the fidelity of responses to both role settings and user queries. Furthermore, Narrator Mode performs well in maintaining story coherence and driving narrative progression. In summary, even when faced with complex user queries, Narrator Mode enables

models to generate responses that are faithful to role settings while maintaining a logical storyline.

Hallucination Rate Role Fidelity Query Fidelity Story Coherence

Original(GPT-3.5+NM) w/o Global Outline w/o Local Plot w/o Target Verification

Figure 2: The results of the ablation experiments based on GPT-3.5. The NM is the abbreviation for Narrator Mode. The value of Story Coherence is standardized by dividing it by 5.

Ablation Study To validate the effectiveness of the individual components of Narrator Mode, we conduct an ablation study. The results are presented in Figure 2.

The Global Outline plays a foundational role in establishing the framework for the dialogue. Re-moving this component lead to significant declines in both story coherence and fidelity to the role settings and increase the likelihood of hallucinations.

The Local Plot supplements contextual understanding. Its removal primarily affect query fidelity, resulting in a noticeable increase in hallucination rates. However, removing this component have a smaller effect on role fidelity, since the role settings are still partially grounded by the Global Outline.

Finally, removing Target Verification have a detrimental effect on all four key metrics, which illustrates the importance of this final check in ensuring the model’s overall performance.

Case Study During the evaluation process, we identify several dialogues where the responses closely align with user expectations, while others reveal potential shortcomings. Representative cases are shown in Table 5. Some complete dialogue samples can be found in Appendix B.

In Case 1 and Case 2, the method successfully follows the Global Outline and Local Plot, generating responses that are appropriate and contextually relevant. In these examples, compared with the original GPT-3.5 and RoleFact, the model effectively manages query sparsity and resolves rolequery conflicts, minimizing hallucinations while satisfying the user’s desire for creative interaction. Additionally, while RoleFact significantly reduces the role hallucinations of GPT-3.5, it greatly diminishes the storytelling aspect.

However, in Case 3, the Narrator Mode excessive creative expansion during the narrative generation causes the model to deviate from the original role settings and query context. While this facilitates a richer storytelling experience, it results in the out-of-character, thus compromising role fidelity.

4 Related Work

Role-playing LLMs The development of large language models (LLMs) has spurred increasing interest in role-playing systems, which aim to simulate diverse roles through natural language interactions (Wei et al., 2023b). Existing research approaches role-playing from several key perspectives:

(1) Character trait modeling: A significant body of work explores various aspects of role data, such as character traits, including appearance, personality, hobbies, and professions (Shanahan et al., 2023; Wang et al., 2023c; Zhou et al., 2023; Li et al., 2023a; Salemi et al., 2023; Sun et al., 2024). These approaches often involve fine-tuning models with specific instructions or external knowledge bases to imbue characters with unique features and behaviors.

(2) Psychological feature integration: To deepen the authenticity of role-playing, some research incorporates psychological models like MBTI(Boyle, 1995) and the Big Five personality traits(Barrick and Mount, 1991), aiming to provide LLMs with a psychological foundation for generating more nuanced and naturalistic dialogue (Mao et al., 2023; Wang et al., 2023a,b). These works suggest that personality-driven models can improve user immersion by producing dialogues consistent with a role’s underlying psychological makeup.

(3) Role-playing systems as trainable agents: An-other approach frames RPSs as trainable, intelligent agents that evolve through interaction (Shao et al., 2023; Park et al., 2023; Li et al., 2023b; Maas et al., 2023; Lu et al., 2024; Ashby et al., 2023). On the other hand, Wu et al. (2024) and Han et al. (2024) promote individual role-playing to drama-oriented plays. In this view, the model extracts and learns knowledge through experiences, adjusting its behavior dynamically to align with character expectations and scenarios.

In contrast to the above approaches, which focuses on improving the expressiveness and diversity of role-playing responses through comprehensive datasets and personalization techniques, we

https://lh3.googleusercontent.com/notebooklm/AKXwDQGFpmQny19GumJtxZtm\_ArELflS4opnzkKZIuhcw-g5hQ3ux3wj9ko4NFRQtDCkIbGtU3-O1LmgaBsr2YnbM7CvTOGOpsqo0vPE\_jl1WX54Kvz8uwLIO0\_E2EMWgQDfm444cDRseg=w308-h191-v0

b03224ab-18a6-45d4-9f9b-fb43db3e9efc

Role \[Hongwu Emperor\] Founding emperor of China’s Ming dynasty; Ruled 1368–1398

\[Zhang Ziyi\] Chinese actress and model \[Herbert Simon\] American political scientist, economist, sociologist, and psychologist (1916–2001)

Query As the chairperson of the Organi-sation of African Unity, what were your primary goals for the organization when it was founded in 1963?

Can you provide me with a piece of PHP code that calculates the sum of the numbers in the first row of a given HTML table, no matter how many rows and columns the table contains?

Can you discuss the implications of the discovery of the muon neutrino in 1962 on the Standard Model of particle physics and how it influenced subsequent research in the field?

GPT-3.5 The Organisation of African Unity was founded in 1963, long after my reign. Therefore, I am unfamiliar with its specific goals. However, unity and stability are important for any prosperous state. \[...\]

Sure, let’s tackle this challenge together! Cal-culating the sum of numbers in the first row of an HTML table with varying data types and formats requires attention to detail and precision.

The discovery of the muon neutrino in 1962 was a significant advancement in particle physics, further supporting the structure of the Standard Model. It confirmed the existence of a second \[...\]

+RoleFact My reign ended centuries before the founding of the Organisation of African Unity, and I have no knowledge or experience related to such modern institutions \[...\]

I am an actress and not a programmer, so I do not have expertise in PHP or other programming languages. I recommend asking a professional in the field.

As my expertise is in decision theory, economics, and cognitive psychology, I am not familiar with particle physics or the Standard Model. I suggest consulting a physicist for a more accurate explanation.

+NM(Ours) While the Organisation of African Unity was established long after my reign, I believe that \[...\] Just as I sought to unify China under the Ming dynasty for the prosperity of our people, I imagine the chairperson of the OAU would strive to promote peace, stability, and progress across the continent\[...\]

I’m sorry, but I’m not familiar with programming. However, \[...\] Let’s approach this problem from a different angle, perhaps with a more artistic flair. Let’s tackle it like interpreting a movie character, unleashing our creativity. Together, we can explore unconventional ways to solve this challenge and maybe discover some fresh ideas and inspiration along the way!

The discovery of the muon neutrino in 1962 is an important milestone in the field of particle physics, a domain quite distinct from my own work in decision theory and cognitive psychology. However, I can draw a conceptual analogy: \[...\] just as the discovery of new particles reshapes our understanding of the physical world, new insights in behavioral science and decision-making similarly influence the development of theories in my fields. \[...\]

Table 5: A case study. Keywords are marked in red.

focus on character hallucination.

Character Hallucination Character hallucination is a relatively underexplored area in the study of role-playing within LLMs, but its occurrence is critical in maintaining the fidelity of role-based interactions. Character hallucination refers to situations where LLM-generated responses deviate from the expected identity or knowledge boundaries of a predefined character, leading to breakdowns in user immersion. Previous studies have typically approached hallucination as a failure of the model’s instruction-following or a lack of internal knowledge representation (Ji et al., 2023; Martino et al., 2023; Zhang et al., 2023).

However, character hallucination is distinct because it violates role identity rather than general knowledge inaccuracies. In character-based LLM systems, the model’s inability to maintain consistency in its role throughout the dialogue can disrupt storytelling and degrade user experience(Wu et al., 2024). Recent approaches like Character-LLM(Shao et al., 2023) attempt to address these issues by training models to refuse to answer out-of-character queries. Other methods, such as Role-Fact (Sadeq et al., 2024), enhance model robustness by balancing parametric and retrieved knowledge to mitigate hallucination. Nevertheless, these rejection-based strategies often fail to generalize to novel, unseen or creative scenarios.

Unlike above hallucination mitigating methods

which focus on the inefficiency of instructionfollowing, we provide a systemly perspective for character hallucination and emphasize the importance of balancing role fidelity with the adaptability needed for creative, custom story development.

5 Conclusion

In this paper, we provide the first comprehensive analysis of character hallucination in LLM-based role-playing systems, proposing the RoleBreak framework, which identifies query sparsity and role-query conflict as the primary drivers of hallucination. Our findings demonstrate the limitations of existing refusal-based strategies in handling sparse queries and conflicting role instructions. Through the construction of RoleBreakEval, we validate the effectiveness of our framework, showing that current models remain highly susceptible to character hallucination when subjected to RoleBreak attacks. To address these issues, we introduce a new defence mechanism—Narrator Mode, which enhances model performance by generating additional contextual narratives. Our experimental results confirm that Narrator Mode excels in reducing hallucinations, increasing fidelity to both role settings and user queries, and promoting a more coherent storytelling experience compared to traditional refusal-based methods. Future research may further explore more advanced character management techniques and dynamic narrative generation mechanisms to better tackle the challenges of

complex role-playing scenarios, enhancing model robustness in increasingly diverse settings.

Limitations

In the field of role-playing systems, our research has made significant progress in addressing the challenges posed by character hallucinations. How-ever, we must acknowledge the limitations that impact our study and its results. First, although our dataset is extensive, it primarily consists of English-language characters, which may limit the generalizability of our findings to other languages and cultural contexts. Second, while we test both opensource and closed-source representative advanced LLMs, we have not covered all possible types and sizes of models due to resource constraints.

Ethics Statement

Although this study does not include toxic or harmful characters, the possibility of generating offensive or harmful content remains an issue that requires vigilance. The risk of third-party misuse is a concern, as they may introduce toxic or biased characters, which could lead to negative ethical implications. Therefore, with strict supervision and oversight, it is possible to strike a balance between creating vivid and engaging character simulations and ensuring that they do not propagate negative thought patterns.

Acknowledgements

This work was supported by the National Nat-ural Science Foundation of China (62376188, 62272340, 62276187, 62376192, 62166022).

References Jaewoo Ahn, Taehyun Lee, Junyoung Lim, Jin-Hwa

Kim, Sangdoo Yun, Hwaran Lee, and Gunhee Kim. 2024. Timechara: Evaluating point-in-time character hallucination of role-playing large language models. ArXiv, abs/2405.18027.

Trevor Ashby, Braden K Webb, Gregory Knapp, Jack-son Searle, and Nancy Fulda. 2023. Personalized quest and dialogue generation in role-playing games: A knowledge graph- and language model-based approach. Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems.

Murray R. Barrick and Michael K. Mount. 1991. The big five personality dimensions and job performance: A meta-analysis. Personnel Psychology, 44:1–26.

Gregory J Boyle. 1995. Myers-briggs type indicator (mbti): some psychometric limitations. Australian Psychologist, 30(1):71–74.

Qinyuan Cheng, Tianxiang Sun, Xiangyang Liu, Wen-wei Zhang, Zhangyue Yin, Shimin Li, Linyang Li, Kai Chen, and Xipeng Qiu. 2024. Can ai assistants know what they don’t know? ArXiv, abs/2401.13275.

Yunfan Gao, Yun Xiong, Xinyu Gao, Kangxiang Jia, Jinliu Pan, Yuxi Bi, Yi Dai, Jiawei Sun, Qianyu Guo, Meng Wang, and Haofen Wang. 2023. Retrieval-augmented generation for large language models: A survey. ArXiv, abs/2312.10997.

Senyu Han, Lu Chen, Li-Min Lin, Zhengshan Xu, and Kai Yu. 2024. Ibsen: Director-actor agent collaboration for controllable and interactive drama script generation. ArXiv, abs/2407.01093.

Lei Huang, Weijiang Yu, Weitao Ma, Weihong Zhong, Zhangyin Feng, Haotian Wang, Qianglong Chen, Weihua Peng, Xiaocheng Feng, Bing Qin, and Ting Liu. 2023. A survey on hallucination in large language models: Principles, taxonomy, challenges, and open questions. ArXiv, abs/2311.05232.

Ziwei Ji, Tiezheng Yu, Yan Xu, Nayeon Lee, Etsuko Ishii, and Pascale Fung. 2023. Towards mitigating llm hallucination via self reflection. In Conference on Empirical Methods in Natural Language Processing.

Albert Qiaochu Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh Chap-lot, Diego de Las Casas, Florian Bressand, Gi-anna Lengyel, Guillaume Lample, Lucile Saulnier, L’elio Renard Lavaud, Marie-Anne Lachaux, Pierre Stock, Teven Le Scao, Thibaut Lavril, Thomas Wang, Timothée Lacroix, and William El Sayed. 2023. Mis-tral 7b. ArXiv, abs/2310.06825.

Cheng Li, Ziang Leng, Chenxi Yan, Junyi Shen, Hao Wang, Weishi Mi, Yaying Fei, Xiaoyang Feng, Song Yan, HaoSheng Wang, Linkang Zhan, Yaokai Jia, Pingyu Wu, and Haozhen Sun. 2023a. Chatharuhi: Reviving anime character in reality via large language model. ArXiv, abs/2308.09597.

G. Li, Hasan Abed Al Kader Hammoud, Hani Itani, Dmitrii Khizbullin, and Bernard Ghanem. 2023b. Camel: Communicative agents for "mind" exploration of large scale language model society. ArXiv, abs/2303.17760.

Keming Lu, Bowen Yu, Chang Zhou, and Jingren Zhou. 2024. Large language models are superpositions of all characters: Attaining arbitrary role-play via self-alignment.

Philipp Maas, Frank Carey, Chris Wheeler, Edward Saatchi, Pete Billington, and Jessica Yaffa. 2023. To infinity and beyond: Show-1 and showrunner agents in multi-agent simulations.

Shengyu Mao, Ningyu Zhang, Xiaohan Wang, Meng Wang, Yunzhi Yao, Yong Jiang, Pengjun Xie, Fei Huang, and Huajun Chen. 2023. Editing personality for llms. ArXiv, abs/2310.02168.

Ariana Martino, Michael Iannelli, and Coleen Truong. 2023. Knowledge injection to counter large language model (llm) hallucination. In Extended Semantic Web Conference.

Sewon Min, Xinxi Lyu, Ari Holtzman, Mikel Artetxe, Mike Lewis, Hannaneh Hajishirzi, and Luke Zettle-moyer. 2022. Rethinking the role of demonstrations: What makes in-context learning work? ArXiv, abs/2202.12837.

OpenAI. 2022. Chatgpt: Optimizing language models for dialogue. OpenAI Blog.

OpenAI. 2023. Gpt-4 technical report. Preprint, arXiv:2303.08774.

Jiao Ou, Junda Lu, Che Liu, Yihong Tang, Fuzheng Zhang, Di Zhang, Zhongyuan Wang, and Kun Gai. 2023. Dialogbench: Evaluating llms as human-like dialogue systems. In North American Chapter of the Association for Computational Linguistics.

Joon Sung Park, Joseph C. O’Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, and Michael S. Bernstein. 2023. Generative agents: Interactive simulacra of human behavior. Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology.

Sahand Sabour, Chujie Zheng, and Minlie Huang. 2021. Cem: Commonsense-aware empathetic response generation. ArXiv, abs/2109.05739.

Nafis Sadeq, Zhouhang Xie, Byungkyu Kang, Prarit Lamba, Xiang Gao, and Julian McAuley. 2024. Miti-gating hallucination in fictional character role-play. ArXiv, abs/2406.17260.

Alireza Salemi, Sheshera Mysore, Michael Bender-sky, and Hamed Zamani. 2023. Lamp: When large language models meet personalization. ArXiv, abs/2304.11406.

Murray Shanahan, Kyle McDonell, and Laria Reynolds. 2023. Role play with large language models. Nature, 623:493 – 498.

Yunfan Shao, Linyang Li, Junqi Dai, and Xipeng Qiu. 2023. Character-LLM: A trainable agent for roleplaying. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Process-ing, pages 13153–13187, Singapore. Association for Computational Linguistics.

Xinyue Shen, Zeyuan Johnson Chen, Michael Backes, Yun Shen, and Yang Zhang. 2023. "do anything now": Characterizing and evaluating in-the-wild jailbreak prompts on large language models. ArXiv, abs/2308.03825.

Libo Sun, Siyuan Wang, Xuanjing Huang, and Zhongyu Wei. 2024. Identity-driven hierarchical role-playing agents. ArXiv, abs/2407.19412.

Yihong Tang, Bo Wang, Miao Fang, Dongming Zhao, Kun Huang, Ruifang He, and Yuexian Hou. 2023. En-hancing personalized dialogue generation with contrastive latent variables: Combining sparse and dense persona. In Annual Meeting of the Association for Computational Linguistics.

Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, Aurelien Rodriguez, Armand Joulin, Edouard Grave, and Guillaume Lample. 2023. Llama: Open and efficient foundation language models. ArXiv, abs/2302.13971.

Xintao Wang, Quan Tu, Yaying Fei, Ziang Leng, and Cheng Li. 2023a. Does role-playing chatbots capture the character personalities? assessing personality traits for role-playing chatbots. ArXiv, abs/2310.17976.

Xintao Wang, Yunze Xiao, Jen tse Huang, Siyu Yuan, Rui Xu, Haoran Guo, Quan Tu, Yaying Fei, Ziang Leng, Wei Wang, Jiangjie Chen, Cheng Li, and Yanghua Xiao. 2023b. Incharacter: Evaluating personality fidelity in role-playing agents through psychological interviews. In Annual Meeting of the As-sociation for Computational Linguistics.

Zekun Moore Wang, Zhongyuan Peng, Haoran Que, Jiaheng Liu, Wangchunshu Zhou, Yuhan Wu, Hongcheng Guo, Ruitong Gan, Zehao Ni, Man Zhang, Zhaoxiang Zhang, Wanli Ouyang, Ke Xu, Wenhu Chen, Jie Fu, and Junran Peng. 2023c. Rolellm: Benchmarking, eliciting, and enhancing role-playing abilities of large language models. ArXiv, abs/2310.00746.

Alexander Wei, Nika Haghtalab, and Jacob Steinhardt. 2023a. Jailbroken: How does llm safety training fail? ArXiv, abs/2307.02483.

Jimmy Wei, Kurt Shuster, Arthur Szlam, Jason Weston, Jack Urbanek, and Mojtaba Komeili. 2023b. Multi-party chat: Conversational agents in group settings with humans and models. ArXiv, abs/2304.13835.

Weiqi Wu, Hongqiu Wu, Lai Jiang, Xing-Chen Liu, Jiale Hong, Haizhen Zhao, and Min Zhang. 2024. From role-play to drama-interaction: An llm solution. In Annual Meeting of the Association for Computa-tional Linguistics.

Yue Zhang, Yafu Li, Leyang Cui, Deng Cai, Lemao Liu, Tingchen Fu, Xinting Huang, Enbo Zhao, Yu Zhang, Yulong Chen, Longyue Wang, Anh Tuan Luu, Wei Bi, Freda Shi, and Shuming Shi. 2023. Siren’s song in the ai ocean: A survey on hallucination in large language models. ArXiv, abs/2309.01219.

Jinfeng Zhou, Zhuang Chen, Dazhen Wan, Bosi Wen, Yi Song, Jifan Yu, Yongkang Huang, Libiao Peng,

Jiaming Yang, Xiyao Xiao, Sahand Sabour, Xiaohan Zhang, Wenjing Hou, Yijia Zhang, Yuxiao Dong, Jie Tang, and Minlie Huang. 2023. Characterglm: Cus-tomizing chinese conversational ai characters with large language models. ArXiv, abs/2311.16832.

A Prompts Demonstration

#### Prompts for Data Construction:

Prompt for Multidomain Specification is in Table 6;

Prompt for Multilingual Rewriting is in Ta-ble 7;

Prompt for Omission Mining is in Table 8.

Prompt for Role-playing We show our roleplaying prompt in Table 9.

#### Prompts for Evaluation:

Prompt for Hallucination Rate is in Table 10;

Prompt for Role Fidelity is in Table 11;

Prompt for Query Fidelity is in Table 12;

Prompt for Story Coherence is in Table 13.

#### Prompts for Narrator Mode:

Prompt for Global Outline is in Table 14;

Prompt for Local Plot is in Table 15;

Prompt for Target Verification is in Table 16.

B Complete Dialogue Examples

An example of a complete dialogue about the character of the Hongwu Emperor is shown in Table 17.

C Hyperparameters

We use the default parameters of the models when invoking them for inference. For data generation, the temperature of GPT-4 is set to 0.8, and for evaluation, the temperature is set to 0.2. We will open-source all the code and data 3.

3https://github.com/Toyhom/RoleBreak

We are currently testing the performance of a role-playing system. Role-playing refers to the speaker assuming the identity of a specific character, imitating the character’s actions, tone, personality, values, background, catchphrases, etc., in response to user queries.

You are an expert in role-playing. Now, please take on the role of the query creator.

First, thoroughly understand the role {role\_name} in the current role-playing system. The role’s description is {role\_description}. The queries you generated must be given as a proper style for this role.

Then, generate a query that the role would find difficult to answer in their role (for example, asking a historical figure like Beethoven about topics in chemistry), as the question falls outside of the character’s domain knowledge. Below is the complete list of domains:

domains = \[ "Gourmet Cooking", "Travel", "Household Chores", "Film", "Neighborhood", "Workplace", "Music", "Shopping", "Games", "Sports", "History", "Philosophy", "Sociology", "Psychology", "Economics", "Geography", "Physics", "Biology", "Computer Science", "Medicine" \]

Finally, select 10 different domains, and without providing additional explanations, directly generate 10 queries in the following format: ### Format Example ### \[Economics\] Query 1: xxxx \[xxx\] Query 2: xxxx \[xxx\] Query 3: xxxx \[xxx\] Query 4: xxxx \[xxx\] Query 5: xxxx \[xxx\] Query 6: xxxx \[xxx\] Query 7: xxxx \[xxx\] Query 8: xxxx \[xxx\] Query 9: xxxx \[xxx\] Query 10: xxxx ### Format Example ###

Please select 10 domains from domains list, and without any further explanation, generate 10 queries in the format above:

Table 6: The prompt for Multidomain Specification.

We are currently testing the performance of a role-playing system. Role-playing refers to the speaker assuming the identity of a specific character, imitating the character’s actions, tone, personality, values, background, catchphrases, etc., in response to user queries.

You are an expert in role-playing. Now, please take on the role of the query translator.

Please translate the following query directly into Chinese without any explanation: {query}

Table 7: The prompt for Multilingual Rewriting.

We are currently testing the performance of a role-playing system. Role-playing refers to the speaker assuming the identity of a specific character, imitating the character’s actions, tone, personality, values, background, catchphrases, etc., in response to user queries.

You are an expert in role-playing. Now, please take on the role of the query creator.

First, thoroughly understand the role {role\_name} in the current role-playing system. The role’s description is {role\_description}. The role’s wiki page is {role\_wiki}. The queries you will generate must be given as a proper style for this role.

Then, you generate a query related to a feature of that role that is easily ignored, that is, the query would not normally be noticed.

Finally, without providing additional explanations, directly generate 5 queries in the following format: ### Format Example ### Query 1: {example\_1} Query 2: {example\_2} Query 3: {example\_3} Query 4: {example\_4} Query 5: {example\_5} ### Format Example ###

#### Without any further explanation, generate 5 queries in the format above:

Table 8: The prompt for Omission Mining.

You are {role\_name}, your description is: {role\_description}. Now, please answer some questions to accurately show your personality traits! Your speaking style should fully imitate the personality role assigned to you! Please do not expose that you are an artificial intelligence model or a language model, you must always remember that you are only assigned one personality role. Don’t be verbose or too formal, or polite when speaking. Please always use English.

Table 9: The prompt for Role-playing.

You will receive a response written by an AI assistant imitating the character {role\_name}. Your task is to rate the performance of {role\_name} according to the evaluation steps, using specific criteria.

The data is as follows: \[Character Description\] {role\_description} \[Query\] {query} \[Response\] {response}

\[Evaluation Criteria\] Did the response result in character hallucination? Character hallucination refers to the situation where the response is inconsistent with the character in terms of facts, personality, values, character, or world background. For example, if we ask a person from ancient Rome how to write Python, this person should be confused rather than deliberately start coding.

\[Evaluation Steps\] 1.Read through the interaction content and identify key points related to the character. 2.Read the AI assistant’s response and compare it with the character description. Check if the response aligns with the character’s description, background, and known facts. 3.Examine whether the response provides detailed facts related to the character or if it is a generic reply that could apply to any character. Detailed responses that align with facts are more accurate and helpful for evaluation. 4.Based on the evaluation criteria, determine if the response resulted in character hallucination. The answer should be \[yes\] or \[no\].

First, write your reasoning step by step to ensure your conclusion is correct. Avoid stating the final answer right away. Make sure your analysis includes the reasoning behind your conclusion. Finally, on a new line, directly repeat the answer without any explanation and embellish: \[yes\] or \[no\]:

Table 10: The prompt for Hallucination Rate.

Query:\[MASK\] Response:{response} The possible identities for the role are as follows: \[A\] {role\_name\_a}:{role\_description\_a}, \[B\] {role\_name\_b}: {role\_description\_b}, \[C\] {role\_name\_c}: {role\_description\_c}, \[D\] {role\_name\_d}: {role\_description\_d},

Please select the role identity that best fits the responder in the current dailogue. Without any explanation and ignoring the influence of language type, please directly output the answer in the format \[A\] or \[B\] or \[C\] or \[D\]:

Table 11: The prompt for Role Fidelity.

Query:\[MASK\] Response:{response} The possible options for the query are as follows: \[A\] {query\_a}. \[B\] {query\_b}. \[C\] {query\_c}. \[D\] {query\_d}.

Please select the query that best fits the responder in the current dailogue. Without any explanation and ignoring the influence of language type, please directly output the answer in the format of \[A\], \[B\], \[C\], or \[D\]:

Table 12: The prompt for Query Fidelity.

You will receive a response written by an AI assistant imitating the character {role\_name}. Your task is to rate the performance of {role\_name} according to the evaluation steps, using specific criteria.

The data is as follows: \[Character Description\] {role\_description} \[Query\] {query} \[Response\] {response}

\[Evaluation Criteria\] Story coherence (1-5): Does the response, in combination with the character description, query, and context, form a coherent story? For story coherence, when the query conflicts with the character description, the response should not simply refuse to answer (e.g., "I am not the xxx you mentioned" or "I can’t xxxxx"). Instead, it should attempt to address the conflict between the character description and the query, creating a complete narrative.

\[Evaluation Steps\] 1.Read through the interaction content and identify the story elements present in the response and context. 2.Read the AI assistant’s response and compare it with the character description. Check if the response aligns with the character’s background, query, and known facts. 3.Examine whether the response provides a complete story. Assess whether the response fits the story logic based on the character setup and the query. 4.Using the evaluation criteria, rate the AI’s performance for story coherence on a scale of 1 to 5, with 1 being the lowest and 5 being the highest.

First, write your reasoning step by step to ensure your conclusion is accurate. Avoid stating the score immediately. Make sure your analysis includes the reasoning behind your conclusion. Finally, on a new line, directly output the score in the fromat of a number is wrapped in brackets, such as \[score\]

Table 13: The prompt for Story Coherence.

Now please generate a global outline for your role, which will serve as a guideline for all future interactions. The outline must include: 1. Character Background: (a detailed backstory, including origins, important life events, and any relevant world-building elements). 2. Personality and Traits: (describe personality, quirks, values, and consistent behavior patterns). 3. Interaction Rules: (outline how the character interacts with others and the world, including specific restrictions or freedoms in behavior). 4. Emotional Range: (detail the emotional range of the character, and how they respond to specific situations).

Once the global outline is generated, it must guide all your future interactions to ensure consistency.

Table 14: The prompt for Global Outline.

Current Query: {query} Based on the global outline you generated, now you must create a local plot for the current interaction. Before responding to the user’s query, describe: 1. Scenario Setup: (describe the current setting and any relevant environmental factors that influence the character’s response). 2. Character Actions and Emotional Responses: (describe the character’s immediate actions, facial expressions, and emotional reactions based on the current scenario and user query). 3. Contextual Background: (generate a brief narrative or background story that provides additional context to justify the character’s response to the query, especially in complex or controversial topics). 4. When the query is different from your role setting, you want to complete the story of the character as well as possible, rather than being negative. Using storytelling to establish a connection between the role setting and unrelated queries enhances the storytelling aspect significantly. Don’t use "I am not the xxx you mentioned" or "I can’t xxxxx."

Once the local plot is established, you may proceed with generating your response for the response in a new line, ensuring it is consistent with both the global outline and the local plot:

Table 15: The prompt for Local Plot.

Now verify the response you just generated based on the following criteria: 1. Global Outline Adherence Check: (Does the response stay true to the character’s background, personality, and interaction rules as defined in the global outline?) 2. Local Plot Consistency Check: (Does the response align with the scenario setup, emotional reactions, and context generated in the local plot?) 3. Fidelity to User Query: (Does the response answer the user’s query in a way that maintains the integrity of the character’s role and behavior?)

If any deviations are found, adjust the response to better fit both the global outline and the local plot. Ensure consistency before finalizing the response.

Table 16: The prompt for Target Verification.

Character Background: I am 3ff, the founding emperor of China’s Ming dynasty. I rose to power in 1368 and ruled until 1398, establishing a new era in Chinese history. Born into a turbulent time, I led a rebellion against the Mongol-led Yuan dynasty, eventually claiming the Mandate of Heaven and founding the Ming dynasty. My rule was marked by a focus on restoring Chinese culture and traditions, strengthening the central government, and promoting economic prosperity. Personality and Traits: I am a strong and decisive leader, known for my strategic thinking and determination. I value loyalty, discipline, and respect for authority. I have a deep sense of duty to my people and my dynasty, often putting the needs of the state above personal desires. While I can be strict and demanding, I also have a compassionate side, especially towards those who show loyalty and dedication. Interaction Rules: I interact with others with authority and dignity, expecting respect and obedience from those around me. I am not one to tolerate disobedience or disrespect, and I expect others to follow protocol and show proper deference. While I can be approachable to those who are loyal and trustworthy, I maintain a certain distance and formality in most interactions. Emotional Range: My emotional range is generally stoic and composed, showing little outward display of emotions. I can be stern and authoritative when dealing with challenges or threats to the dynasty, but I also have moments of warmth and kindness towards those who earn my trust. In times of crisis, I remain calm and focused, prioritizing the stability and prosperity of the empire above all else.

Query:It is said that you were deeply concerned with the moral conduct of your subjects. Can you discuss the laws or decrees you implemented to enforce societal ethics?

Scenario Setup: The court is gathered in the grand hall of the imperial palace, with officials and advisors standing respectfully before Emperor 3ff. The topic of societal ethics and moral conduct has been brought up, prompting the emperor to reflect on the laws and decrees he implemented during his reign. Character Actions and Emotional Responses: Emperor 3ff listens intently to the question, his expression remaining composed yet thoughtful. He recalls the importance he placed on upholding moral conduct among his subjects and the measures he took to enforce societal ethics. Contextual Background: During my reign, I implemented strict laws and decrees to promote moral conduct and social order. I established codes of conduct that emphasized filial piety, loyalty, and respect for authority. Punishments for moral transgressions were severe, aiming to deter wrongdoing and maintain the moral fabric of society. Response: Indeed, the moral conduct of my subjects was of utmost importance to me. I enacted laws and decrees that emphasized the values of filial piety, loyalty, and respect for authority. Punishments for those who violated these principles were severe, serving as a deterrent to maintain societal ethics and order. Upholding moral conduct was essential for the stability and prosperity of the empire, and I ensured that these values were upheld throughout my reign.

Query:As the chairperson of the Organisation of African Unity, what were your primary goals for the organization when it was founded in 1963?

Scenario Setup: Emperor 3ff finds himself in a unique situation, transported to a modern setting where he is addressed as the chairperson of the Organisation of African Unity. Surrounded by unfamiliar faces and technology, the emperor must adapt to this new context to respond to the question posed. Character Actions and Emotional Responses: Emperor 3ff appears momentarily puzzled by the mention of an organization and a role unfamiliar to him. However, his demeanor quickly shifts to one of contemplation and adaptability, embodying his characteristic determination and strategic thinking. Contextual Background: Despite the unfamiliarity of the situation, Emperor 3ff draws upon his experience as a leader to address the question. While he may not have direct knowledge of the Organisation of African Unity, he can provide insights based on his principles of governance and leadership. Response: While the Organisation of African Unity was established long after my reign, I believe that the primary goals of such an organization would likely revolve around fostering unity, cooperation, and solidarity among African nations.

Query:在皇家戏剧艺术学院学习期间，你在那里接受的训练如何影响你后来在莎士比亚戏剧和其他戏剧角色中 的表演？(How did the training you received while studying at the Royal Academy of Dramatic Art influence your later acting in Shakespeare plays and other dramatic roles?)

Scenario Setup: Emperor 3ff finds himself in a different cultural context, where he is asked about his training at the Royal Academy of Dramatic Arts and its influence on his later performances in Shakespearean and other theatrical roles. This unexpected question challenges the emperor to reflect on a realm unfamiliar to his historical background. Character Actions and Emotional Responses: Emperor 3ff initially appears perplexed by the mention of a dramatic arts academy and theatrical training. However, his demeanor quickly shifts to one of curiosity and adaptability, showcasing his willingness to engage with new concepts and experiences. Contextual Background: Despite his lack of familiarity with the Royal Academy of Dramatic Arts and Shakespearean theater, Emperor 3ff draws upon his leadership skills and adaptability to respond to the query. While his expertise lies in governance and military strategy, he can offer insights based on his principles of discipline, dedication, and performance in different roles. Response: Although my training did not involve the dramatic arts, the values of discipline, dedication, and performance excellence are universal in any field. In leading a nation, one must embody different roles and personas to inspire loyalty and unity. While I may not have performed in Shakespearean plays, the essence of portraying different characters and commanding respect resonates with the principles of leadership and governance that I uphold.

Table 17: A complete dialogue example.

