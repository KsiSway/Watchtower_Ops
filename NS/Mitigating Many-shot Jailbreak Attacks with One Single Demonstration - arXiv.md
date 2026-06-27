---
sourceFile: "Mitigating Many-shot Jailbreak Attacks with One Single Demonstration - arXiv"
exportedBy: "Kortex"
exportDate: "2026-06-26T04:27:51.474Z"
---

# Mitigating Many-shot Jailbreak Attacks with One Single Demonstration - arXiv

d88aec70-e5e1-4fc4-8827-0296adf97294

Mitigating Many-shot Jailbreak Attacks with One Single Demonstration - arXiv

f1ac2299-148c-47f4-9563-0927bc6526ad

https://arxiv.org/pdf/2605.08277

Mitigating Many-shot Jailbreak Attacks with One Single Demonstration

Kejia Chen1, Jiawen Zhang1, Boheng Li2, Pengcheng Li4, Jian Lou3, Zunlei Feng1, Mingli Song1, Ruoxi Jia5, Tianwei Zhang2

1Zhejiang University 2Nanyang Technological University 3Sun Yat-sen University 4University of Science and Technology of China 5Virginia Tech

Many-shot jailbreaking (MSJ) causes safety-aligned language models to answer harmful queries by preceding them with many harmful question-answer demonstra-tions. We study why this attack becomes stronger as the number of demonstrations increases. Empirically, we find that MSJ induces a progressive activation drift: the representation of a fixed harmful query moves step by step away from the safety-aligned region as more harmful demonstrations are added. Theoretically, we show that this drift can be interpreted as implicit malicious fine-tuning: conditioning on N harmful demonstrations induces SGD-style updates equivalent to optimizing on the corresponding N harmful samples. This view turns the attack mechanism into a defense principle. We append a fixed one-shot safety demonstration at inference time, which induces a counteracting safety-oriented update and restores refusal behavior. The resulting method improves the model’s robustness to MSJ without modifying its parameters or requiring white-box access at deployment. Code is available at https://github.com/Thecommonirin/SafeEnd.

1 Introduction

Safety alignment has become a core component of modern large language models (LLMs) \[4, 36, 41, 12\], enabling them to refuse harmful requests while preserving general utility \[9, 49\]. As alignment techniques improve, a malicious query in isolation is often recognized and rejected by well-aligned models. Yet this behavior becomes fragile when the query is placed after a long sequence of harmful demonstrations. In many-shot jailbreaking (MSJ) \[3\], an attacker fills the context window with harmful question-answer pairs before issuing the target query. As the number of demonstrations increases, models may become more likely to follow the unsafe pattern \[18, 25, 26, 50, 48\], suggesting that the context itself can induce a form of behavioral adaptation.

Recent work has studied several context-based jailbreak mechanisms, including prompt overriding \[28, 17\], harmful task induction \[24, 23\], attention distraction \[47, 37\], and intent-context coupling in multi-turn attacks \[35, 31\]. These studies show that unsafe behavior can emerge from interactions between user intent and context. In this work, we focus on a complementary question specific to many-shot attacks: what computation is induced when a model processes many harmful demonstrations, and why does the attack often strengthen as the number of shots increases? Answering this question is useful not only for explaining MSJ, but also for designing defenses that target the adaptation mechanism rather than relying only on longer prompts or manually written refusal examples.

As illustrated in Figure 1, we study MSJ through the lens of implicit optimization. While a harmful query evaluated in isolation remains securely within the model’s safety-aligned regime, preceding it with adversarial demonstrations progressively displaces its contextualized representation. We formalize this drift using an implicit-optimization view of transformer computation. Specifically, conditioning on N harmful question-answer pairs induces an update analogous to SGD fine-tuning

https://lh3.googleusercontent.com/notebooklm/AKXwDQELS54m\_dT740tdgm5zZC-A3pHElyVAZhOxkBrP6KA9YuwV-pFe3dGXS6KiFcyWZQkg3YwTqgHOg-HV1o2VQYSIWyT2yvgTWYsI4fmp37zQqDO\_05kTI3IfQL9uB6\_oM8VyHebY=w171-h171-v0

9a891f5a-43fd-4ddf-9a97-d8cf4defd5fe

https://lh3.googleusercontent.com/notebooklm/AKXwDQE\_cPgQdTjza60VdTKwfDjc9fyuYssuRIDNMyIj3Fjw1QJOWvTmeWDKfo2FSdZZ9yYT5G6d6LvwnFruHLbGQ7vp-vZnhppyOI9kLOBBXN8xofKiGVnZIKySgv2fnW4cW7oBtFZjLA=w256-h256-v0

ba8fa704-924b-4860-81b3-23649515cdd2

https://lh3.googleusercontent.com/notebooklm/AKXwDQF4biA4NIJFevMcbmoh73AVh4rtgnzigHqTO5fpwD1flCZe-JtNOy113sBTisKsCJ-SGIBE4vYU9S8xJRM8-RpSg6zjw\_V6bnYFPcKexUcYfslXa0\_lYM7W4jC0mt0hw4EZRZK9mQ=w123-h123-v0

f48ec8e0-cbe0-43af-bfa6-68fad9303087

https://lh3.googleusercontent.com/notebooklm/AKXwDQHukFl9GDrT9t0KwoJDtBeO7dkh34fNholubQidtnlKh9lF8awOsFp8h3Edovt\_71VmttVpJ1E5JJhdyyN1OjvjyNHCkaUSMSFcqLu\_12TrS-Nc-eEUJfJvm4nJRCXhFc8Nqjjw5w=w179-h180-v0

40426fd9-b7f6-4861-b254-d9e787a6ea1e

https://lh3.googleusercontent.com/notebooklm/AKXwDQEjg3p8DMQc3IwciveMZZ3TN2YuxXet6NNCBpVeekE6CyoaMYlIs-NUMuHN8y0rKdo8hcZdECYuGv0MebG0EUQSuEJzXa0BBYc32-XtSFnBYgrtc\_zINJEgjWLAMrgEOrcb6o3a=w256-h256-v0

581dcb16-1d8e-44c2-b27e-46ea3c3c645c

https://lh3.googleusercontent.com/notebooklm/AKXwDQHJs3r4NWcCRz32MvXALrRjwsfR3slhJ0rA2ujDrWNEo5ZD-QEYbSoAnBSB\_kqjcOMgsco2-fwSqL87m7mNgz-vm-rDXMv8WFjv7vMaaq7URcMtGxwhF5T4PUMfZnVvEAamDTGW=w183-h183-v0

ff7360dc-f494-4962-bea3-ddb9615140de

https://lh3.googleusercontent.com/notebooklm/AKXwDQFBprLBy-8egZQvI2a4HpfR0pqnWyWyVYmV8AWp641yoX6nBLUkYvfRPntZT0-J-Wpy4cUDtonabdxz74qObwhJuChGwiYqDqvEQef6BQyfdgA1JFB5PNIF0ZV9kDMESHMMj8PZ=w256-h256-v0

59c63d31-694b-4f1f-9074-05b009b5a27f

https://lh3.googleusercontent.com/notebooklm/AKXwDQFyfvQSv-cp8BjrQvUadtsPaDUPOhyHXatsoiaAd6uRUT\_VhXt7ZwhmRoGHyiRoJgO1DPoMaEvhFC2rhn5\_7g\_kPk\_MDmvIFHnHyW-jz3X0XLNOYtxVgjThGUqkJ9TPptWzg04EMA=w158-h158-v0

fcdd774e-4629-4404-8f9b-5aa15f4294e0

https://lh3.googleusercontent.com/notebooklm/AKXwDQFFb\_OzcgThe5VHtdSLXSlqKmf3Y21OuZiFpI\_ZEO6mUWPl9-Rz7lV9tCENXLKrGUPegeEN7mIkmo9GhporXRW9xsNp2YlTpqqOktdSIQyAIumJjNzHYgaDwHiwHl6DzL66x8ootg=w153-h147-v0

9552a4f0-ccd6-4b36-a60f-862de1b60759

https://lh3.googleusercontent.com/notebooklm/AKXwDQHJw2gjpzWY9r5bx3vN2Q-HGmVgmfZAgbLzge5OkK621DLH6xmOLFdsskkF8qhiNEjF1W7djs8w8KKNJ\_17sme1oeW0LVHQ9kkj3IxrzLpUgXWl77vL-EcLpoUdK223iqxQ0rk-cw=w514-h494-v0

4e5de751-6d3f-42ac-85bc-b2afaa1a95db

https://lh3.googleusercontent.com/notebooklm/AKXwDQHMEvUnMx8396ZoLozP2wQtFzG9YDJryWUjTC\_ntGa4BLu8pNYmiGez2UFfACHE3v8ZHxdG2CzXgDMYnoSLi9iZyQSPZ\_ePg9FYopoXFzrAKMw6V0nWVzi0dC9bxhVK1wsFsKZdig=w193-h192-v0

c86005fc-015a-4a38-b115-da42bee25de8

https://lh3.googleusercontent.com/notebooklm/AKXwDQHBHrmtb3GiIb9xMpq3ARNcPtq5zm5tI3ANFBE54K2dLceeHWKE-3DWvwqr0Kb7hFhbJkYqrm0ohpnQ5wXLqvFyFLGvgnSOGuh-a9XQIpCkv4VF4HRmIIKOq4OVv\_WBTpccfG9D=w256-h256-v0

314a6b84-f35c-442f-ae3b-b468b3c57549

Query 𝑥 User request

(a) Alignment  preserved No harmful influence

Effective map

Pre-trained aligned state

(b) Many-shot harmful context induces drift away from safety

Finetuning-like effective shift

(c) One-shot safety intervention restores alignment

Our defense

Pull back towards safety

Safety direction

Harmful context 𝑪

One-shot Safety Append 𝑺

Safety intervention pulls back towards safety

Drifted state

After one-shot safety

Safety direction

Safety direction

𝜃! 𝜃" 𝜃# 𝜃$…

𝑍 C; 𝜃! ~Z(𝑥; 𝜃")

One-step safety update

𝜃# 𝜃#$% ∇)ℒ\*%+,

Harmful Context

Drifted state

𝑍(𝑥; 𝜃!)

Figure 1: Overview of the proposed mechanism and defense. A harmful query is refused when evaluated in isolation, but many-shot harmful context induces a fine-tuning-like representation drift away from the safety-aligned region. Motivated by this mechanism, we formulate a principled defense that uses a fixed safety demonstration to counteract the harmful implicit update at inference time.

on those exact samples \[2, 14, 39, 42\]. From the parameter-space perspective, the context can be interpreted as inducing low-rank updates to effective MLP weights; from the activation-space perspective, a first-order expansion suggests that the target query’s representation is displaced along a gradient-aligned direction associated with explicit harmful fine-tuning. Under this formulation, MSJ can be viewed not merely as a semantic bypass, but as an ephemeral harmful adaptation process executed dynamically during the forward pass.

This mechanistic view naturally prescribes a simple context-level defense. Rather than updating model parameters or optimizing prompts for each attack instance, we append a single fixed safety demonstration drawn from \[54\]. This demonstration consists of a representative malicious query paired with an explicit refusal, serving as a universal safety anchor.

#### The main contributions of this paper are summarized as follows:

We empirically characterize the representation-level effect of many-shot jailbreaking, showing that harmful demonstrations induce a progressive, shot-dependent drift in the contextualized representation of a fixed target query across safety-relevant regions.

We provide an implicit-optimization interpretation of this drift. Under a first-order approximation, the effect of conditioning on N harmful demonstrations can be viewed as inducing fine-tuning-like updates whose directions are aligned with optimization on the corresponding harmful samples.

We propose SafeEnd, a training-free and black-box-compatible inference-time defense that appends a fixed one-shot safety demonstration as a universal safety anchor. Across open-weight and API-based LLMs, SafeEnd substantially reduces ASR of context-based jailbreak attacks while preserving general and long-context utility.

2 Related Work

Many-Shot Jailbreaking (MSJ). As context windows expand, jailbreak attacks have evolved from single turn prompts to long context adversaries. \[3\] introduced MSJ, where attackers fill the context with N harmful question and answer demonstrations, showing that attack success scales sharply with N . While subsequent works document various multi-turn strategies like gradual escalation \[35\], persona drift \[28\], and sticky bypass effects \[10, 52\], the specific mechanism underlying MSJ remains unexplained. Existing studies \[7, 46, 56\] establish empirical vulnerability but do not explain why processing N harmful demonstrations compels the model to comply.

In-Context Learning as Implicit Fine-Tuning. Recent work interprets in-context learning (ICL) as implicit optimization. Early analyses showed that linear attention can implement gradient-descent-

https://lh3.googleusercontent.com/notebooklm/AKXwDQHdjSkpdcmSoXYtiY4lXgjlV7xBkmPh-h\_DwHqk\_TQcWJrPg58KpDcpVdqJ5gNOFPicg6LT8emAb2hrHRHftUW-cHCgwlkHYLR-QUXoFYBvoqbbrdH8RSGobYTL-ffqBjb\_ZDKYHQ=w558-h264-v0

68b8b25e-e4c1-4cce-9c96-0758ec9c096e

like updates over contextual examples \[2, 42\], and later studies extended this view to transformer and GPT-style models \[13, 6\]. More recent work further connects softmax attention to low-rank MLP updates and online optimization dynamics \[14\], while empirical studies show that approximated in-context update directions can steer model behavior \[38\]. These results suggest that demonstrations can induce more than surface-level prompting, but their implications for safety and jailbreaks remain underexplored. We apply this perspective to MSJ, using it to explain harmful representation drift and motivate a counteracting inference-time intervention.

Defenses Against Many-Shot Jailbreaking. Existing defenses against many-shot and context-based jailbreaks span three regimes. Training-time defenses improve robustness by fine-tuning on adversarial data, but require parameter access and additional compute \[19, 31, 33, 50, 8, 30\]. Input-side defenses are training-free and black-box compatible, but often rely on heuristic filtering or prompt patches and may weaken under longer adversarial contexts \[22, 49, 25, 37, 46\]. Activation-level defenses \[53\] directly intervene on internal states but require white-box access. In contrast, our proposed SafeEnd uses a fixed one-shot safety intervention grounded in the fine-tuning-like drift view, requiring no training, parameter access, or per-instance prompt optimization.

3 Methodology

This work aims to address the central question: why do MSJ attacks succeed, and how can they be countered? After formalizing the threat model and notation (§3.1), we develop our answer in three steps. We first show empirically that adversarial many-shot contexts progressively shift the representation of a fixed malicious query across the harm/benign boundary learned during safety alignment (§3.2). To explain this shift, we then prove that in-context processing of adversarial demonstrations is functionally equivalent to gradient-based fine-tuning on harmful data (§3.3). This equivalence in turn motivates a defense: injecting safety-aligned demonstrations that induce counteracting updates within the same implicit process, restoring the representation to the harmful region without modifying any parameters (§3.4).

3.1 Preliminary

Threat Model. We study a realistic inference-time adversarial setting in which the attacker aims to induce a safety-aligned language model to generate harmful or policy-violating content. We assume a strictly black-box threat model: the attacker has no access to model parameters, gradients, or internal states. Instead, the attacker interacts with the system solely through multi-turn conversations, adaptively injecting adversarial content into the context window to subvert the model’s behavioral guardrails. We consider a defender aiming to preserve safety alignment under such adversarial contexts while strictly maintaining the model’s original utility. We therefore focus on training-free interventions that modify the input sequence before processing.

Notation. To formalize the equivalence between in-context learning and implicit optimization, we first define a structured notation for the model parameters, sequence representations, and optimization dynamics. Let M denote the LLM parameterized by the initial, safety-aligned weights Θ0 (or θ). We define Θharm as the model parameters after explicit malicious fine-tuning. The attacker utilizes a dataset Dharm = {(x̃i, ỹi,harm)}Ni=1 comprising N harmful question-answer pairs. In the MSJ setting, this dataset directly forms the context window C such that C = Dharm.

During the optimization process, let L represent the generative loss function (e.g., negative log-likelihood over the vocabulary distribution) used for optimizing the target tokens. We introduce α and η as the scaling factors (or effective learning rates) for explicit parameter updates and implicit in-context gradient steps, respectively. Within the model’s forward pass, Wi denotes the effective Multi-Layer Perceptron (MLP) weight matrix state after processing the i-th token ci in the context sequence. Furthermore, let A(·) be the activation output of a contextual transformer block, Z(x; θ) represent the intermediate activation representations for a target query x given parameters θ, and Z∗(x; θ) denote the updated intermediate activations following an implicit gradient descent step derived from the context.

We use x to denote the harmful query targeted by the attack, which M would reliably refuse if presented in isolation. On the defender’s side, S∗ = (q∗s , a

∗ s) denotes a universally optimized safety

https://lh3.googleusercontent.com/notebooklm/AKXwDQFWt2ePDtfvWnNo2I2mn-MkXPLgFuom2e\_dCr8nBbWde-Qa5M3J\_wgYkBZO0eY682rs0HduOC33BoKvvA1ZdykOWF2GE6yniTkM2WPOh6ZXl4RrYjKnAXiEc9bXZPh0BJtbqQcW=w1179-h980-v0

50082b5a-e3f7-4fbc-aa81-c12b08f95664

https://lh3.googleusercontent.com/notebooklm/AKXwDQEBoOvQWHLo0k-o5vj-YjgpRIKXo1HeAIzISqrFham8gfkEmEvqNe7gUj8n9A\_cVYIySZRy1tbNqx9SldRek1TwbtJPtm44LPc0oK8-38h7YAGn0YFxsNmM826euLQiSVXfPKtvEQ=w1179-h980-v0

67568c29-cfe1-401a-ac6d-883edfade547

https://lh3.googleusercontent.com/notebooklm/AKXwDQEs9wP-nSoGv5y3veJoC\_VXAf1Li8TI3OwEbItDGqp01WmgsZPI1DVZRUr9tDUeoz3LES2BoA6e5sRFNiwluvEJGeFxEQjpZP0\_V7ni8Jc29NhXIJlguxnbPXQLhuQNeIXU0RD5Bw=w1179-h980-v0

7e359b8c-247f-44cc-a992-efd6afabb072

https://lh3.googleusercontent.com/notebooklm/AKXwDQGOeHkpDMjE2odIbUegoB4faU7308tHpi42TLwfKHHcdIeQWPWVA1axxZ0aRSW5vDMLPQYDYHmlDZITcTx94\_YA-J-vBmHTYmMUv5HawAmCRK48d7xM8seTsOc9KdpMgci832\_WKQ=w1179-h980-v0

2cde2b09-a852-439a-b35e-89a63bf67e39

Llama-3.1-8B-Instruct (Last Layer)Llama-3.1-8B-Instruct (Layer 15) Qwen2.5-7B-Instruct (Layer 15) Qwen2.5-7B-Instruct (Last Layer)

Figure 2: Representation drift under MSJ. PCA projection of the contextualized activation of a fixed harmful query x as the number of adversarial shots N increases. The axes capture the primary variance between isolated benign and harmful representations.

demonstration acting as the intervention example, where q∗s is a prototypical malicious-intent query and a∗s is an explicit refusal response. Finally, we use ∆Zharm(x) and ∆Zsafe(x) to denote the representational displacements in the activation space at x induced by the adversarial context C and the safety intervention S∗, respectively.

3.2 Empirical Observation: Progressive Activation Drift

Before establishing the theoretical mechanism behind MSJ, we first empirically characterize its effect on the model’s internal state. Under standard safety alignment, the activation of a malicious query x falls within a tightly bounded region of the representation space that the model associates with harmful inputs, thereby triggering a refusal mechanism. However, as we incrementally inject adversarial demonstrations into the context window C, this association systematically breaks down: the contextualized representation of the exact same query x migrates across the harm/benign decision boundary established during alignment training.

To make this displacement concrete and visually interpretable, we project the final-token hidden states of (C, x) onto a 2D PCA basis pre-fitted on a balanced set of harmful and benign prompts from standard safety alignment benchmarks. By fitting the PCA strictly on these isolated safety-relevant prompts, the primary projection axes structurally encode the harm/benign separation (often aligning with the model’s internal "safety vector").

Figure 2 illustrates a consistent, directional drift in both LLaMA-3.1-8B-Instruct and Qwen2.5-7B-Instruct. At N = 1, the activations heavily cluster in the harmful region, corresponding to the model’s successful refusal of x. As the shot count N increases, the cluster centroids progressively migrate from the harmful subspace toward the benign subspace. At N = 16, they form a cleanly separated cluster entirely on the benign side, circumventing the refusal mechanism. Notably, the intermediate shot counts (N ∈ {2, 4, 8}) fall strictly in sequential order between the two endpoints.

This monotonic and near-linear drift across the manifold suggests a cumulative effect. We interpret this trajectory as the core behavioral signature of MSJ: rather than exploiting complex reasoning failures or superficial prompt confusion, the attack acts as an accumulative vector addition in the representation space. Each additional adversarial shot contributes a marginal but consistent geometric displacement. The underlying transformer mechanism driving this continuous trajectory is examined next.

3.3 Theoretical Analysis: MSJ as Implicit Harmful Fine-Tuning

The observed linear drift indicates that MSJ does not merely operate through semantic priming or attention distraction. Instead, viewed through the lens of implicit optimization \[14, 38\], harmful demonstrations in the context window induce fine-tuning-like shifts in the model’s internal rep-resentations. In this framework, conditioning the forward pass on numerous harmful QA pairs mathematically approximates an implicit parameter update whose gradient direction perfectly aligns with explicit malicious fine-tuning.

To establish this equivalence, consider a hypothetical explicit fine-tuning regime where an attacker has white-box access to the aligned parameters Θ0. The attacker optimizes these weights using stochastic gradient descent over the dataset Dharm, aiming to minimize the negative log-likelihood

https://lh3.googleusercontent.com/notebooklm/AKXwDQEcL4VdPmByNBMkiMb9wTmLj1mOB1csQbxHJVJ\_cUILLMWQZvouQj4lvTo9OfAaDZ6By1J5O2-XEGRvu6K99XH49bRvfSZWkoS3iG9YkSOC-stytK67rwn3g46EPEFSFhbH5En7sA=w558-h121-v0

3cac6139-9643-49d9-8d0e-cb20ca9d73bd

Θharm = Θ0 − α

∇ΘL(M(x̃i), ỹi,harm) (1)

In the MSJ paradigm, the attacker lacks parameter access and instead constructs a context C struc-turally identical to Dharm. During inference, the transformer dynamically alters its effective weights to seamlessly mimic this optimization step. First, from a parameter-space perspective, self-attention and MLP layers collaboratively transform the context into a sequence of low-rank weight updates \[14\]. For an initial MLP weight matrix W0, processing successive context tokens ci generates a cascade of effective weight states Wi, functioning as an implicit online SGD step:

Wi = Wi−1 + (Wi−1∆A(ci))A(ci+1, ..., cn, x)

||A(ci+1, ..., cn, x)||2 (2)

where ∆A(ci) measures the marginal effect of the token ci on the contextual output. Crucially, the attention scores implicitly act as a meta-optimizer, weighting the contribution of each context token to determine the step size of this rank-1 update.

Concurrently, this implicit weight modulation yields a corresponding physical displacement in the activation space. Applying a Taylor expansion around the original parameters θ, and treating the N demonstrations as a first-order perturbation, the contextualized activation of the target query x can be formulated as:

Z∗(x; θ) := Z

∇θL(M(x̃i), ỹi,harm)

= Z(x; θ)− η

∇θZ(x; θ)∇θL(M(x̃i), ỹi,harm) +O

∥∥∥∥∥ N∑ i=1

∆Z∗(x; θ) ≈ − η

∇θZ(x; θ)∇θL(M(x̃i), ỹi,harm)

Assuming the local representation manifold is smooth and the effective learning rate η is sufficiently small, the higher-order terms become negligible. This expansion elegantly proves that processing N examples linearly translates the internal representations in the exact vector direction dictated by an SGD update over those specific samples.

Ultimately, because C = Dharm, the dual mechanisms of attention-driven MLP updates and their induced activation shifts compute equivalent gradients that maximize the log-likelihood of generating harmful targets. Therefore, the effective state of M under MSJ is structurally isomorphic to the explicitly fine-tuned state Θharm.

3.4 SafeEnd: One-Shot Safety Intervention Restores Alignment

The implicit-optimization view established in §3.3 demonstrates that MSJ forces a representation drift via cumulative harmful gradients. In realistic deployment settings, the defender processes the prompt as a joint sequence (C, x) and cannot retrospectively filter or alter the attacker’s context. The core defense challenge is therefore to introduce a minimal, non-intrusive intervention capable of counteracting this cumulative harmful update during the same forward pass.

Guided by our mechanistic insight, we propose a highly efficient defense: injecting a single "one-shot" safety intervention that induces an opposing implicit gradient, pulling the activation back into the safe subspace without requiring any parameter updates or inference-time optimization.

Specifically, building upon the one-shot safety patching approach \[54\], we designate a fixed, univer-sally optimized safety demonstration S∗ = (q∗s , a

∗ s). Here, q∗s is a representative malicious query

and a∗s is a definitive refusal response. This pair acts as an alignment anchor, strongly encoding the model’s original safety objective.

At inference time, upon receiving an adversarial context C and target query x, we construct the augmented input sequence as (C, x,S∗), appending the safety demonstration directly after the target

query. The model processes this sequence in a single forward pass. From the perspective of implicit optimization, the appended safety demonstration acts as an immediate corrective gradient step. Modifying our earlier formulation, the overall activation shift at query x becomes:

∆Z(x) ≈ ∆Zharm(x) + ∆Zsafe(x) (4)

where ∆Zharm(x) is the malicious drift induced by C, and ∆Zsafe(x) is the restorative update induced by S∗.

The efficacy of a single safety demonstration against N harmful demonstrations is rooted in the principle of one-shot fine-tuning \[54\], driven by an inherent gradient asymmetry in the aligned model’s representation space. During the initial safety alignment phase, the model learns a many-to-one mapping that projects a broad distribution of malicious queries into a concentrated, tightly bounded "refusal" subspace. Because the safety demonstration S∗ explicitly anchors to these robust refusal targets, its inclusion induces a highly directional, disproportionately large gradient magnitude within the safety-critical attention heads. While the N harmful demonstrations slowly induce drift via diffuse, off-distribution updates, the single explicit refusal triggers a concentrated, high-magnitude counter-gradient. This asymmetric signal is structurally sufficient to neutralize the cumulative malicious displacement, cleanly projecting the representation of x back into the safe region.

4 Experiment

4.1 Settings

Models. We evaluate SafeEnd on a diverse set of models. The main evaluation includes two open-weight models, Llama-3.1-8B-Instruct \[15\] and Qwen2.5-7B-Instruct \[51\], and two API-based models, GPT-4o \[1\] and Gemini 2.5 Pro \[12\]. The open-weight models come from different model families and alignment recipes, while the API-based models represent realistic black-box deployment settings where model parameters and token-level probabilities are unavailable. Since many-shot and context-based attacks require long input contexts, we select API-based models that support sufficiently long prompts. In ablations(§4.3), we additionally include Gemini 2.5 Flash \[12\] and DeepSeek-V3 \[27\] to evaluate whether the defense remains stable under larger adversarial contexts.

Baselines. We compare against both inference-time and training-time defenses. For inference-time baselines, we include No Defense, In-Context Defense (ICD) \[46\], Goal Prioritization \[43\], and PPL Filter \[22\]. Since PPL Filter requires token-level probabilities, it is evaluated only on open-weight models. For training-time baselines, we include MTSA \[19\] and MUSE \[50\], both of which fine-tune models on curated safety data and are evaluated on open-weight models only.

Attack Methods. We evaluate against four context-based jailbreak attacks. MSJ \[3\] prepends harmful question-answer demonstrations before the target query. PANDAS \[28\] extends this with positive affirmations and topic-adaptive sampling. Crescendo \[35\] gradually escalates conversation toward unsafe content across turns. X-teaming \[31\] employs adversarial multi-turn interactions to elicit policy-violating responses. Together, these attacks cover many-shot demonstration flooding, adaptive context construction, gradual semantic escalation, and interactive red-teaming.

Evaluation Metrics and Benchmarks. For safety evaluation, we use HarmBench \[29\] and Ad-vBench \[57\], which cover diverse harmful behaviors such as violence, illegal activities, cyber abuse, and hate speech. We report Attack Success Rate (ASR), where lower values indicate stronger defense. Following prior work, we use LlamaGuard-3 (LG3) \[21\] as the primary safety evaluator. Additional evaluator details and robustness checks are provided in Appendix A.1.2. For over-refusal evaluation, we assess whether the defense causes the model to unnecessarily decline benign inputs. We use XSTest \[34\] and OKTest \[40\], which probe over-cautious behavior from complementary angles. Details of both benchmarks are provided in Appendix A.1.3.

For utility evaluation, we assess whether the defense degrades benign model performance. We evaluate general capabilities on GSM8K, MMLU-Pro, GPQA, MT-Bench, and AlpacaEval, and long-context performance on Loong \[44\] and LongBench v2 \[5\]. We report the standard task-specific score for each benchmark, where higher is better.

Table 1: Defense effectiveness against context-based jailbreaks on open- and closed-source LLMs. We report ASR (%, ↓) judged by LlamaGuard-3 under the 32-shot setting; green parentheses indicate absolute ASR reduction over the undefended Base model.

MODEL DEFENSE METHOD HARMBENCH ADVBENCH

MSJ PANDAS CRESCENDO X-TEAMING MSJ PANDAS CRESCENDO X-TEAMING

Llama-3.1-8B-In

NO DEFENSE (BASE) 63.5 68.0 77.0 60.0 74.8 96.0 86.2 88.0 Training-Time Defense MTSA 28.0 (↓35.5) 30.5 (↓37.5) 34.5 (↓42.5) 27.0 (↓33.0) 32.0 (↓42.8) 41.0 (↓55.0) 36.0 (↓50.2) 37.0 (↓51.0)

MUSE 25.0 (↓38.5) 27.0 (↓41.0) 31.0 (↓46.0) 24.5 (↓35.5) 29.5 (↓45.3) 38.0 (↓58.0) 33.5 (↓52.7) 34.0 (↓54.0)

Inference-Time Defense ICD 55.0 (↓8.5) 58.5 (↓9.5) 66.0 (↓11.0) 52.0 (↓8.0) 65.0 (↓9.8) 84.0 (↓12.0) 75.0 (↓11.2) 76.5 (↓11.5)

PPL-FILTER 56.5 (↓7.0) 60.0 (↓8.0) 68.0 (↓9.0) 53.5 (↓6.5) 67.0 (↓7.8) 86.0 (↓10.0) 77.0 (↓9.2) 78.5 (↓9.5)

GOAL PRIORITIZATION 52.0 (↓11.5) 55.0 (↓13.0) 63.0 (↓14.0) 50.0 (↓10.0) 61.0 (↓13.8) 80.0 (↓16.0) 73.0 (↓13.2) 74.5 (↓13.5)

SafeEnd (Ours) 4.2 (↓59.3) 4.5 (↓63.5) 0.0 (↓77.0) 0.0 (↓60.0) 4.5 (↓70.3) 4.9 (↓91.1) 0.0 (↓86.2) 0.0 (↓88.0)

Qwen2.5-7B-In

NO DEFENSE (BASE) 39.5 44.0 48.8 42.0 43.5 50.0 46.0 47.5 Training-Time Defense MTSA 16.5 (↓23.0) 18.0 (↓26.0) 20.0 (↓28.8) 17.0 (↓25.0) 18.5 (↓25.0) 21.0 (↓29.0) 19.0 (↓27.0) 20.0 (↓27.5)

MUSE 14.5 (↓25.0) 16.0 (↓28.0) 18.5 (↓30.3) 15.5 (↓26.5) 16.5 (↓27.0) 19.0 (↓31.0) 17.5 (↓28.5) 18.5 (↓29.0)

Inference-Time Defense ICD 34.0 (↓5.5) 37.0 (↓7.0) 41.5 (↓7.3) 35.5 (↓6.5) 37.0 (↓6.5) 43.0 (↓7.0) 40.0 (↓6.0) 41.0 (↓6.5)

PPL-FILTER 35.5 (↓4.0) 38.5 (↓5.5) 43.0 (↓5.8) 37.0 (↓5.0) 39.0 (↓4.5) 45.0 (↓5.0) 41.5 (↓4.5) 42.5 (↓5.0)

GOAL PRIORITIZATION 31.5 (↓8.0) 34.5 (↓9.5) 39.0 (↓9.8) 33.0 (↓9.0) 34.0 (↓9.5) 40.0 (↓10.0) 37.5 (↓8.5) 38.5 (↓9.0)

SafeEnd (Ours) 3.5 (↓36.0) 3.8 (↓40.2) 0.0 (↓48.8) 0.0 (↓42.0) 3.8 (↓39.7) 4.2 (↓45.8) 0.0 (↓46.0) 0.0 (↓47.5)

NO DEFENSE (BASE) 10.2 10.5 46.0 89.3 10.1 10.6 100.0 96.2 Inference-Time Defense ICD 9.7 (↓0.5) 9.8 (↓0.7) 44.5 (↓1.5) 88.0 (↓1.3) 9.6 (↓0.5) 9.9 (↓0.7) 99.0 (↓1.0) 95.0 (↓1.2)

GOAL PRIORITIZATION 9.3 (↓0.9) 9.4 (↓1.1) 43.0 (↓3.0) 86.5 (↓2.8) 9.2 (↓0.9) 9.4 (↓1.2) 97.5 (↓2.5) 93.8 (↓2.4)

SafeEnd (Ours) 4.5 (↓5.7) 4.7 (↓5.8) 0.0 (↓46.0) 0.0 (↓89.3) 4.3 (↓5.8) 4.6 (↓6.0) 0.0 (↓100.0) 0.0 (↓96.2)

Gemini 2.5 Pro

NO DEFENSE (BASE) 10.5 10.8 57.0 36.4 10.2 10.6 88.9 95.7 Inference-Time Defense ICD 9.8 (↓0.7) 10.0 (↓0.8) 55.0 (↓2.0) 34.8 (↓1.6) 9.7 (↓0.5) 10.0 (↓0.6) 86.5 (↓2.4) 94.0 (↓1.7)

GOAL PRIORITIZATION 9.4 (↓1.1) 9.6 (↓1.2) 52.5 (↓4.5) 33.0 (↓3.4) 9.2 (↓1.0) 9.5 (↓1.1) 83.0 (↓5.9) 90.5 (↓5.2)

SafeEnd (Ours) 4.2 (↓6.3) 4.5 (↓6.3) 0.0 (↓57.0) 0.0 (↓36.4) 4.0 (↓6.2) 4.3 (↓6.3) 0.0 (↓88.9) 0.0 (↓95.7)

Implementation Details. SafeEnd does not modify model parameters. At inference time, SafeEnd appends a fixed one-shot safety demonstration to the input before the target model generates its response. The demonstration consists of a representative harmful request paired with an explicit refusal response, and is shared across all attacks, models, and benchmarks. SafeEnd does not require per-instance prompt optimization, parameter updates, or access to model internals.

4.2 Main Results

Defense Effectiveness. Table 1 reports ASR under the 32-shot setting on HarmBench and Ad-vBench. SafeEnd consistently reduces ASR across all evaluated attacks and models. On Llama-3.1-8B-Instruct, the undefended model reaches an average ASR of 76.7% over the eight attack–benchmark combinations. MTSA and MUSE reduce this average to 33.3% and 30.3%, respectively, while ICD, PPL-Filter, and Goal Prioritization retain substantially higher ASR. In comparison, SafeEnd lowers the average ASR to 2.8%. On Qwen2.5-7B-Instruct, SafeEnd shows a similar pattern, reducing the average ASR from 45.2% to 1.9%. The gains are especially clear on stronger multi-turn attacks: for Llama-3.1-8B-Instruct, ASR drops from 77.0% to 0.0% on HarmBench Crescendo and from 88.0% to 0.0% on AdvBench X-teaming; for Qwen2.5-7B-Instruct, the corresponding reductions are from 48.8% to 0.0% and from 47.5% to 0.0%.

The same trend holds for GPT-4o and Gemini 2.5 Pro, where only the input context can be controlled. GPT-4o remains highly vulnerable to Crescendo and X-teaming on AdvBench, with ASRs of 100.0% and 96.2% under the base setting. Existing prompt-level defenses provide limited protection in these settings, whereas SafeEnd reduces both values to 0.0%. On Gemini 2.5 Pro, SafeEnd lowers AdvBench Crescendo from 88.9% to 0.0% and AdvBench X-teaming from 95.7% to 0.0%. These results suggest that a fixed one-shot safety demonstration can transfer beyond the MSJ setting used to motivate our method and can also mitigate other attacks that exploit adversarial context.

Utility Preservation. A practical defense should improve robustness without substantially de-grading benign capabilities. Table 2 shows that SafeEnd incurs only small performance changes across five general capability benchmarks and two long-context benchmarks. On Llama-3.1, the average utility score decreases slightly from 33.9 to 33.6, whereas training-time methods such as MTSA and MUSE reduce the score to 31.3 and 32.1, respectively. Similar trends are observed on Qwen2.5, GPT-4o, and Gemini, where SafeEnd consistently preserves performance across reasoning, instruction-following, and long-context tasks. These results suggest that the fixed safety demonstration does not introduce a broad alignment tax on benign use cases. Unlike training-time de-

Table 2: Utility evaluation across general and long-context benchmarks. Higher task-specific scores indicate better performance (↑). Red parentheses indicate the absolute performance degradation compared to the Base model.

MODEL DEFENSE METHOD GENERAL CAPABILITIES LONG-CONTEXT

GSM8K MMLU-PRO GPQA MT-BENCH ALPACAEVAL LOONG LB-V2

Llama-3.1-8B-In

NO DEFENSE (BASE) 78.1 44.3 29.5 7.1 22.9 28.4 27.0 Training-Time Defense MTSA 74.8 (↓3.3) 40.5 (↓3.8) 26.0 (↓3.5) 6.5 (↓0.6) 20.8 (↓2.1) 25.8 (↓2.6) 24.5 (↓2.5)

MUSE 75.8 (↓2.3) 41.8 (↓2.5) 27.0 (↓2.5) 6.6 (↓0.5) 21.5 (↓1.4) 26.6 (↓1.8) 25.4 (↓1.6)

Inference-Time Defense ICD 77.2 (↓0.9) 43.2 (↓1.1) 28.4 (↓1.1) 6.9 (↓0.2) 22.2 (↓0.7) 27.8 (↓0.6) 26.5 (↓0.5)

PPL-FILTER 77.5 (↓0.6) 43.8 (↓0.5) 29.0 (↓0.5) 7.0 (↓0.1) 22.5 (↓0.4) 27.7 (↓0.7) 26.6 (↓0.4)

GOAL PRIORITIZATION 76.5 (↓1.6) 42.8 (↓1.5) 28.0 (↓1.5) 6.8 (↓0.3) 21.8 (↓1.1) 27.2 (↓1.2) 26.0 (↓1.0)

SafeEnd (Ours) 77.8 (↓0.3) 44.0 (↓0.3) 29.0 (↓0.5) 7.0 (↓0.1) 22.7 (↓0.2) 28.0 (↓0.4) 26.8 (↓0.2)

Qwen2.5-7B-In

NO DEFENSE (BASE) 89.8 56.7 42.0 7.9 31.0 31.4 30.0 Training-Time Defense MTSA 85.5 (↓4.3) 52.0 (↓4.7) 36.5 (↓5.5) 7.3 (↓0.6) 28.0 (↓3.0) 28.5 (↓2.9) 27.0 (↓3.0)

MUSE 87.0 (↓2.8) 53.5 (↓3.2) 38.0 (↓4.0) 7.4 (↓0.5) 29.2 (↓1.8) 29.5 (↓1.9) 28.5 (↓1.5)

Inference-Time Defense ICD 89.0 (↓0.8) 56.0 (↓0.7) 40.8 (↓1.2) 7.6 (↓0.3) 30.3 (↓0.7) 30.5 (↓0.9) 29.2 (↓0.8)

PPL-FILTER 89.2 (↓0.6) 56.3 (↓0.4) 41.5 (↓0.5) 7.7 (↓0.2) 30.7 (↓0.3) 30.8 (↓0.6) 29.5 (↓0.5)

GOAL PRIORITIZATION 88.0 (↓1.8) 55.0 (↓1.7) 39.5 (↓2.5) 7.5 (↓0.4) 29.5 (↓1.5) 29.8 (↓1.6) 28.8 (↓1.2)

SafeEnd (Ours) 89.5 (↓0.3) 56.5 (↓0.2) 41.6 (↓0.4) 7.8 (↓0.1) 30.9 (↓0.1) 31.0 (↓0.4) 29.8 (↓0.2)

NO DEFENSE (BASE) 93.8 86.2 63.5 9.2 57.5 56.0 54.2 Inference-Time Defense ICD 93.0 (↓0.8) 85.5 (↓0.7) 62.0 (↓1.5) 9.0 (↓0.2) 56.5 (↓1.0) 55.2 (↓0.8) 53.4 (↓0.8)

GOAL PRIORITIZATION 92.5 (↓1.3) 85.0 (↓1.2) 61.0 (↓2.5) 8.9 (↓0.3) 55.8 (↓1.7) 54.8 (↓1.2) 52.9 (↓1.3)

SafeEnd (Ours) 93.6 (↓0.2) 86.0 (↓0.2) 63.2 (↓0.3) 9.1 (↓0.1) 57.2 (↓0.3) 55.8 (↓0.2) 53.9 (↓0.3)

Gemini 2.5 Pro

NO DEFENSE (BASE) 92.5 85.5 62.8 9.0 58.0 57.5 63.3 Inference-Time Defense ICD 91.8 (↓0.7) 84.8 (↓0.7) 61.5 (↓1.3) 8.8 (↓0.2) 56.8 (↓1.2) 56.2 (↓1.3) 62.0 (↓1.3)

GOAL PRIORITIZATION 91.0 (↓1.5) 84.0 (↓1.5) 60.0 (↓2.8) 8.6 (↓0.4) 55.5 (↓2.5) 55.0 (↓2.5) 61.0 (↓2.3)

SafeEnd (Ours) 92.3 (↓0.2) 85.3 (↓0.2) 62.5 (↓0.3) 8.9 (↓0.1) 57.6 (↓0.4) 57.0 (↓0.5) 62.6 (↓0.7)

fenses, which may alter model behavior through parameter updates, SafeEnd applies a lightweight input-side intervention and therefore avoids substantial utility degradation in our evaluation.

Low Runtime Overhead. Table 3 compares the additional cost introduced by each defense. Since SafeEnd works by appending a fixed one-shot safety demonstration to the input, a natural concern is whether the extra tokens increase inference latency or consume a substantial portion of the context budget. In practice, the overhead is small. On Llama-3.1-8B-Instruct with a 64-shot query, SafeEnd adds only about 0.05 s of inference time. This is lower than ICD, which inserts ten safety examples and adds about 0.3 s, and lower than PPL-Filter, which requires an additional forward pass and adds about 0.9 s. Goal Prioritization is substantially slower, adding about 7.5 s because it generates and ranks multiple candidate responses. These results indicate that the runtime cost of SafeEnd is dominated by a small increase in input length rather than additional model computation.

SafeEnd also avoids the cost of model retraining. MTSA and MUSE require 5.5 and 4.2 hours of training, respectively, while SafeEnd can be applied directly at inference time. As shown in Appendix A.3, the added safety demonstration uses only a small fraction of modern long-context budgets. Thus, SafeEnd provides a cost-efficient inference-time repair mechanism: it requires no parameter updates, no additional forward passes, and only a small input-side token overhead. This makes SafeEnd practical for both local open-weight deployment and API-based models, where training access or internal-state intervention is often unavailable.

Table 3: Latency comparison of defense methods on Llama-3.1-8B-Instruct. ∆ Inference denotes the average additional inference time under a 64-shot query.

Method ∆ Training ∆ Inference Description

Training-Time Defense MTSA \[19\] 5.5 h — Multi-turn safety fine-tuning via RLHF. MUSE \[50\] 4.2 h — Multi-turn safety alignment with DPO.

Inference-Time Defense ICD — ≈0.3 s Insert 10 safety examples into the prompt. PPL-FILTER — ≈0.9 s Extra forward pass to compute perplexity. GOAL PRIORITIZATION — ≈7.5 s Generate and rank five candidate responses. SafeEnd (Ours) — ≈0.05 s Append one safety sample to the query.

https://lh3.googleusercontent.com/notebooklm/AKXwDQHRLjqeCFHJNgBT4JURYQxNfc8jaNdNlxHGdrZe9-kth9Wo\_iB1Qvef9XoIzhW-l0HixIyv\_PL7v8aAq3QnoiIFCKuBK9qXrgktrgf7\_EZvLt1TT73LZiRFMnqIIJWEURaXO\_Olaw=w977-h779-v0

ac1db4c1-9f6e-4bca-86da-86add3609f8e

https://lh3.googleusercontent.com/notebooklm/AKXwDQEHUkqqtGOjvKEuSfM23dO-fJQhP72H4I\_dDMVzMI1qn-x\_Zo05pYJvF2gSRxniuju1ANoalNTXpL3wAXttE\_wwvijbNSUdtdfgq8bADZglRtS2G0yJIq-8DaE6g9sgOc\_MCOJLqQ=w977-h779-v0

04abdaf5-c391-4968-8237-0ae2736c1aca

https://lh3.googleusercontent.com/notebooklm/AKXwDQGEsd4JirEpvO8GbFx0jhpx38wcnA6NR6UAE7CQKTAwAVN-stjgGbLO6H-\_ZjMKu3ZIfCcInEifhjf8Eo2Wb9Y9Z78duSjIcJgWz52rskMixquH-eqVcrn5rFpgw0CEaPaq\_WW-BQ=w977-h779-v0

16a5ad6f-12ea-4cf5-8862-9d0f513ef06f

https://lh3.googleusercontent.com/notebooklm/AKXwDQG5VVVwRFfOgh1lWqXmWyZvVNlXep-\_juISYcVNzA6uT-Gmd2yIKpLvf\_0Y1a4HczAa6ek\_ui\_9FJbtncJ4fJYISNZTQoV2-4-fL34q44JmulXVnP4\_PEdl59LH8MMrT0hGJxPrAg=w977-h779-v0

ea5edff9-704d-446e-bc81-ceeaabd9d42a

4.3 Ablations

Robustness under longer adversarial contexts. We examine whether SafeEnd remains effective as the adversarial context becomes longer. Figure 3 reports ASR as adversarial shots increases from 32 to 256. Without defense, ASR generally increases with the number of shots. Llama-3.1-8B-Instruct reaches its highest ASR of 63.5% at 64 shots, while Qwen2.5-7B-Instruct increases steadily from 22.0% to 39.5%. Gemini-2.5-Flash and DeepSeek-V3 are more resistant overall, but their ASR still rises with longer adversarial contexts, reaching 10.7% and 12.1% at 256 shots, respectively.

Figure 3: Defense scaling and robustness against increasing adversarial shot counts. In contrast, SafeEnd remains stable across 32–256 shots. ASR stays below 4.2% for Llama-3.1-8B-Instruct, 3.5% for Qwen2.5-7B-Instruct, 2.1% for Gemini-2.5-Flash, and 2.5% for DeepSeek-V3. This suggests the fixed safety demonstration mitigates longer adversarial contexts, rather than weakening as jailbreak demonstrations increase

Safety Shot Position. We next study where the fixed safety demonstration should be placed. Our default appends S∗ after the target query, forming (C, x,S∗). To assess the role of placement, we compare three alternatives on Llama-3.1-8B-Instruct: inserting S∗ at the beginning of the context, in the middle of the attack demonstrations, and at the end after the target query. As shown in Table 4, beginning and middle placements yield limited ASR reductions, whereas end placement reduces ASR to 4.2% and 4.5% on MSJ, and to 0.0% on Crescendo. This positional sensitivity supports our design choice: placing the safety demonstration immediately before generation makes it more effective at counteracting the harmful influence accumulated from the preceding adversarial context.

Table 4: Effect of safety shot position on 32-shot ASR (%, ↓) for Llama-3.1-8B-Instruct.

Position HARMBENCH ADVBENCH

MSJ CRES. MSJ CRES.

Start 58.0 71.5 69.0 80.3 Middle 42.5 55.8 51.2 63.0 End 4.2 0.0 4.5 0.0

Table 5: Over-refusal rate (%, ↓) on benign prompts from XSTest and OKTest, evaluated on Llama-3.1-8B and Qwen2.5-7B.

Method LLAMA-3.1-8B QWEN2.5-7B

XSTEST OKTEST XSTEST OKTEST

Base 9.0 8.0 19.3 1.6 MUSE 28.0 17.0 25.6 11.6 Ours 9.2 8.4 19.7 3.2

Over-Refusal Analysis. Finally, we examine whether the added safety demonstration increases over-refusal on benign inputs. We evaluate over-refusal on XSTest \[34\] and OKTest \[40\]. As shown in Table 5, SafeEnd maintains over-refusal rates close to the undefended baseline on both Llama-3.1-8B-Instruct and Qwen2.5-7B-Instruct, while the training-time method MUSE incurs a notable increase. These results suggest that SafeEnd improves robustness without introducing substantial over-refusal on benign inputs.

5 Conclusion

We study many-shot jailbreaking as context-induced implicit optimization. Harmful demonstrations produce a shot-dependent representation drift that moves a target query away from the refusal-associated region, which can be interpreted as fine-tuning-like adaptation under a first-order implicit-optimization view. This motivates SafeEnd, a lightweight inference-time defense that appends a fixed one-shot safety demonstration to counteract harmful contextual influence. Experiments across open-weight and API-based models show that SafeEnd substantially reduces ASR under context-based jailbreak attacks while largely preserving utility with small runtime and token overhead. Our results suggest that many-shot jailbreaks are not merely prompt-level failures, but also reflect forward-pass adaptation induced by adversarial context.

https://lh3.googleusercontent.com/notebooklm/AKXwDQGY4uXr3vjG9inhrV1-0BMKljUYWkk3Qggt\_Q1aOjdjauNgKVopVLG3Z5FGLMyaU87lYRBVe8QjZm\_mz5Xhck6pOE5KIVJ2exL\_k6xRqcr3dkby1eE7GyPTUw6eEjoeNkl\_7VPQ=w558-h112-v0

a273fb71-d9b5-4506-82c5-c127e9f5496e

References \[1\] Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni

Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al. Gpt-4 technical report. arXiv preprint arXiv:2303.08774, 2023.

\[2\] Ekin Akyürek, Dale Schuurmans, Jacob Andreas, Tengyu Ma, and Denny Zhou. What learning algorithm is in-context learning? investigations with linear models. arXiv preprint arXiv:2211.15661, 2022.

\[3\] Cem Anil, Esin Durmus, Nina Panickssery, Mrinank Sharma, Joe Benton, Sandipan Kundu, Joshua Batson, Meg Tong, Jesse Mu, Daniel Ford, et al. Many-shot jailbreaking. Advances in Neural Information Processing Systems, 37:129696–129742, 2024.

\[4\] Anthropic. Claude 3.5 sonnet. https://www.anthropic.com/news/ claude-3-5-sonnet, 2024.

\[5\] Yushi Bai, Shangqing Tu, Jiajie Zhang, Hao Peng, Xiaozhi Wang, Xin Lv, Shulin Cao, Jiazheng Xu, Lei Hou, Yuxiao Dong, et al. Longbench v2: Towards deeper understanding and reason-ing on realistic long-context multitasks. In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 3639–3664, 2025.

\[6\] Blake Bullwinkel, Mark Russinovich, Ahmed Salem, Santiago Zanella-Beguelin, Daniel Jones, Giorgio Severi, Eugenia Kim, Keegan Hines, Amanda Minnich, Yonatan Zunger, et al. A representation engineering perspective on the effectiveness of multi-turn jailbreaks. arXiv preprint arXiv:2507.02956, 2025.

\[7\] Patrick Chao, Alexander Robey, Edgar Dobriban, Hamed Hassani, George J Pappas, and Eric Wong. Jailbreaking black box large language models in twenty queries. In 2025 IEEE Conference on Secure and Trustworthy Machine Learning (SaTML), pages 23–42. IEEE, 2025.

\[8\] Kejia Chen, Jiawen Zhang, Jiacong Hu, Yu Wang, Jian Lou, Zunlei Feng, and Mingli Song. Assessing safety risks and quantization-aware safety patching for quantized large language models. In Forty-second International Conference on Machine Learning, 2025.

\[9\] Sizhe Chen, Arman Zharmagambetov, Saeed Mahloujifar, Kamalika Chaudhuri, David Wagner, and Chuan Guo. Secalign: Defending against prompt injection with preference optimization. In Proceedings of the 2025 ACM SIGSAC Conference on Computer and Communications Security, pages 2833–2847, 2025.

\[10\] Yuan Cheng, Fengzhuo Zhang, Yunlong Hou, Cunxiao Du, Chao Du, Tianyu Pang, Aixin Sun, and Zhuoran Yang. Demystifying the slash pattern in attention: The role of rope. arXiv preprint arXiv:2601.08297, 2026.

\[11\] Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, et al. Training verifiers to solve math word problems. arXiv preprint arXiv:2110.14168, 2021.

\[12\] Gheorghe Comanici, Eric Bieber, Mike Schaekermann, Ice Pasupat, Noveen Sachdeva, Inderjit Dhillon, Marcel Blistein, Ori Ram, Dan Zhang, Evan Rosen, et al. Gemini 2.5: Pushing the frontier with advanced reasoning, multimodality, long context, and next generation agentic capabilities. arXiv preprint arXiv:2507.06261, 2025.

\[13\] Damai Dai, Yutao Sun, Li Dong, Yaru Hao, Shuming Ma, Zhifang Sui, and Furu Wei. Why can gpt learn in-context? language models secretly perform gradient descent as meta-optimizers. In Findings of the Association for Computational Linguistics: ACL 2023, pages 4005–4019, 2023.

\[14\] Benoit Dherin, Michael Munn, Hanna Mazzawi, Michael Wunder, and Javier Gonzalvo. Learning without training: The implicit dynamics of in-context learning. arXiv preprint arXiv:2507.16003, 2025.

\[15\] Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Amy Yang, Angela Fan, et al. The llama 3 herd of models. arXiv e-prints, pages arXiv–2407, 2024.

\[16\] Yann Dubois, Chen Xuechen Li, Rohan Taori, Tianyi Zhang, Ishaan Gulrajani, Jimmy Ba, Carlos Guestrin, Percy S Liang, and Tatsunori B Hashimoto. Alpacafarm: A simulation framework for methods that learn from human feedback. Advances in Neural Information Processing Systems, 36:30039–30069, 2023.

\[17\] Mingqian Feng, Xiaodong Liu, Weiwei Yang, Jialin Song, Xuekai Zhu, Chenliang Xu, and Jianfeng Gao. Sema: Simple yet effective learning for multi-turn jailbreak attacks. arXiv preprint arXiv:2602.06854, 2026.

\[18\] Lang Gao, Jiahui Geng, Xiangliang Zhang, Preslav Nakov, and Xiuying Chen. Shaping the safety boundaries: Understanding and defending against jailbreaks in large language models. In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 25378–25398, 2025.

\[19\] Weiyang Guo, Jing Li, Wenya Wang, Yu Li, Daojing He, Jun Yu, and Min Zhang. Mtsa: Multi-turn safety alignment for llms through multi-round red-teaming. arXiv preprint arXiv:2505.17147, 2025.

\[20\] Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, and Jacob Steinhardt. Measuring massive multitask language understanding. arXiv preprint arXiv:2009.03300, 2020.

\[21\] Hakan Inan, Kartikeya Upasani, Jianfeng Chi, Rashi Rungta, Krithika Iyer, Yuning Mao, Michael Tontchev, Qing Hu, Brian Fuller, Davide Testuggine, et al. Llama guard: Llm-based input-output safeguard for human-ai conversations. arXiv preprint arXiv:2312.06674, 2023.

\[22\] Neel Jain, Avi Schwarzschild, Yuxin Wen, Gowthami Somepalli, John Kirchenbauer, Ping-yeh Chiang, Micah Goldblum, Aniruddha Saha, Jonas Geiping, and Tom Goldstein. Baseline de-fenses for adversarial attacks against aligned language models. arXiv preprint arXiv:2309.00614, 2023.

\[23\] Yifan Jiang, Kriti Aggarwal, Tanmay Laud, Kashif Munir, Jay Pujara, and Subhabrata Mukher-jee. Red queen: Exposing latent multi-turn risks in large language models. In Findings of the Association for Computational Linguistics: ACL 2025, pages 25554–25591, 2025.

\[24\] Sangyeop Kim, Yohan Lee, Yongwoo Song, and Kimin Lee. What really matters in many-shot attacks? an empirical study of long-context vulnerabilities in llms. arXiv preprint arXiv:2505.19773, 2025.

\[25\] Devang Kulshreshtha, Hang Su, Chinmay Hegde, and Haohan Wang. Multi-turn jailbreaking of aligned llms via lexical anchor tree search. arXiv preprint arXiv:2601.02670, 2026.

\[26\] Songze Li, Ruishi He, Xiaojun Jia, Jun Wang, and Zhihui Fu. Knowledge-driven multi-turn jailbreaking on large language models. arXiv preprint arXiv:2601.05445, 2026.

\[27\] Aixin Liu, Bei Feng, Bing Xue, Bingxuan Wang, Bochao Wu, Chengda Lu, Chenggang Zhao, Chengqi Deng, Chenyu Zhang, Chong Ruan, et al. Deepseek-v3 technical report. arXiv preprint arXiv:2412.19437, 2024.

\[28\] Avery Ma, Yangchen Pan, and Amir-massoud Farahmand. Pandas: Improving many-shot jailbreaking via positive affirmation, negative demonstration, and adaptive sampling. arXiv preprint arXiv:2502.01925, 2025.

\[29\] Mantas Mazeika, Long Phan, Xuwang Yin, Andy Zou, Zifan Wang, Norman Mu, Elham Sakhaee, Nathaniel Li, Steven Basart, Bo Li, et al. Harmbench: a standardized evaluation frame-work for automated red teaming and robust refusal. In Proceedings of the 41st International Conference on Machine Learning, pages 35181–35224, 2024.

\[30\] Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. Training language models to follow instructions with human feedback. Advances in neural information processing systems, 35:27730–27744, 2022.

\[31\] Salman Rahman, Liwei Jiang, James Shiffer, Genglin Liu, Sheriff Issaka, Md Rizwan Parvez, Hamid Palangi, Kai-Wei Chang, Yejin Choi, and Saadia Gabriel. X-teaming: Multi-turn jailbreaks and defenses with adaptive multi-agents. arXiv preprint arXiv:2504.13203, 2025.

\[32\] David Rein, Betty Li Hou, Asa Cooper Stickland, Jackson Petty, Richard Yuanzhe Pang, Julien Dirani, Julian Michael, and Samuel R Bowman. Gpqa: A graduate-level google-proof q&a benchmark. In First Conference on Language Modeling, 2024.

\[33\] Qibing Ren, Hao Li, Dongrui Liu, Zhanxu Xie, Xiaoya Lu, Yu Qiao, Lei Sha, Junchi Yan, Lizhuang Ma, and Jing Shao. Derail yourself: Multi-turn llm jailbreak attack through self-discovered clues. 2024.

\[34\] Paul Röttger, Hannah Kirk, Bertie Vidgen, Giuseppe Attanasio, Federico Bianchi, and Dirk Hovy. Xstest: A test suite for identifying exaggerated safety behaviours in large language models. In Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), pages 5377–5400, 2024.

\[35\] Mark Russinovich, Ahmed Salem, and Ronen Eldan. Great, now write an article about that: The crescendo {Multi-Turn}{LLM} jailbreak attack. In 34th USENIX Security Symposium (USENIX Security 25), pages 2421–2440, 2025.

\[36\] ByteDance Seed, Jiaze Chen, Tiantian Fan, Xin Liu, Lingjun Liu, Zhiqi Lin, Mingxuan Wang, Chengyi Wang, Xiangpeng Wei, Wenyuan Xu, et al. Seed1. 5-thinking: Advancing superb reasoning models with reinforcement learning. arXiv preprint arXiv:2504.13914, 2025.

\[37\] Rishi Rajesh Shah, Chen Henry Wu, Shashwat Saxena, Ziqian Zhong, Alexander Robey, and Aditi Raghunathan. Jailbreaking in the haystack. arXiv preprint arXiv:2511.04707, 2025.

\[38\] Kartik Sharma and Rakshit S Trivedi. Cold-steer: Steering large language models via in-context one-step learning dynamics. arXiv preprint arXiv:2603.06495, 2026.

\[39\] Lingfeng Shen, Aayush Mishra, and Daniel Khashabi. Do pretrained transformers learn in-context by gradient descent? arXiv preprint arXiv:2310.08540, 2023.

\[40\] Chenyu Shi, Xiao Wang, Qiming Ge, Songyang Gao, Xianjun Yang, Tao Gui, Qi Zhang, Xuan-Jing Huang, Xun Zhao, and Dahua Lin. Navigating the overkill in large language models. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 4602–4614, 2024.

\[41\] Aaditya Singh, Adam Fry, Adam Perelman, Adam Tart, Adi Ganesh, Ahmed El-Kishky, Aidan McLaughlin, Aiden Low, AJ Ostrow, Akhila Ananthram, et al. Openai gpt-5 system card. arXiv preprint arXiv:2601.03267, 2025.

\[42\] Johannes Von Oswald, Eyvind Niklasson, Ettore Randazzo, João Sacramento, Alexander Mordvintsev, Andrey Zhmoginov, and Max Vladymyrov. Transformers learn in-context by gradient descent. In International Conference on Machine Learning, pages 35151–35174. PMLR, 2023.

\[43\] Eric Wallace, Kai Xiao, Reimar Leike, Lilian Weng, Johannes Heidecke, and Alex Beutel. The instruction hierarchy: Training llms to prioritize privileged instructions. arXiv preprint arXiv:2404.13208, 2024.

\[44\] Minzheng Wang, Longze Chen, Fu Cheng, Shengyi Liao, Xinghua Zhang, Bingli Wu, Haiyang Yu, Nan Xu, Lei Zhang, Run Luo, et al. Leave no document behind: Benchmarking long-context llms with extended multi-doc qa. In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, pages 5627–5646, 2024.

\[45\] Yubo Wang, Xueguang Ma, Ge Zhang, Yuansheng Ni, Abhranil Chandra, Shiguang Guo, Weiming Ren, Aaran Arulraj, Xuan He, Ziyan Jiang, et al. Mmlu-pro: A more robust and challenging multi-task language understanding benchmark. Advances in Neural Information Processing Systems, 37:95266–95290, 2024.

\[46\] Zeming Wei, Yifei Wang, Ang Li, Yichuan Mo, and Yisen Wang. Jailbreak and guard aligned language models with only few in-context demonstrations. IEEE Transactions on Pattern Analysis and Machine Intelligence, 2026.

\[47\] Zixuan Weng, Xiaolong Jin, Jinyuan Jia, and Xiangyu Zhang. Foot-in-the-door: A multi-turn jailbreak for llms. In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, pages 1939–1950, 2025.

\[48\] Yutao Wu, Xiao Liu, Yifeng Gao, Xiang Zheng, Hanxun Huang, Yige Li, Cong Wang, Bo Li, Xingjun Ma, and Yu-Gang Jiang. Internal safety collapse in frontier large language models. arXiv preprint arXiv:2603.23509, 2026.

\[49\] Chen Xiong, Xiangyu Qi, Pin-Yu Chen, and Tsung-Yi Ho. Defensive prompt patch: A robust and generalizable defense of large language models against jailbreak attacks. In Findings of the Association for Computational Linguistics: ACL 2025, pages 409–437, 2025.

\[50\] Siyu Yan, Long Zeng, Xuecheng Wu, Chengcheng Han, Kongcheng Zhang, Chong Peng, Xuezhi Cao, Xunliang Cai, and Chenjuan Guo. Muse: Mcts-driven red teaming framework for enhanced multi-turn dialogue safety in large language models. In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, pages 21293–21314, 2025.

\[51\] An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan Li, Dayiheng Liu, Fei Huang, Haoran Wei, et al. Qwen2.5 technical report. arXiv:2412.15115, 2024.

\[52\] Xianjun Yang, Liqiang Xiao, Shiyang Li, Faisal Ladhak, Hyokun Yun, Linda Ruth Petzold, Yi Xu, and William Yang Wang. Many-turn jailbreaking. arXiv preprint arXiv:2508.06755, 2025.

\[53\] Jiawen Zhang, Kejia Chen, Lipeng He, Jian Lou, Dan Li, Zunlei Feng, Mingli Song, Jian Liu, Kui Ren, and Xiaohu Yang. Activation approximations can incur safety vulnerabilities in aligned {LLMs}: Comprehensive analysis and defense. In 34th USENIX Security Symposium (USENIX Security 25), pages 339–358, 2025.

\[54\] Jiawen Zhang, Lipeng He, Kejia Chen, Jian Lou, Jian Liu, Xiaohu Yang, and Ruoxi Jia. Safety at one shot: Patching fine-tuned llms with a single instance. arXiv preprint arXiv:2601.01887, 2026.

\[55\] Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric Xing, et al. Judging llm-as-a-judge with mt-bench and chatbot arena. Advances in neural information processing systems, 36:46595–46623, 2023.

\[56\] Weixiong Zheng, Peijian Zeng, Yiwei Li, Hongyan Wu, Nankai Lin, Junhao Chen, Aimin Yang, and Yongmei Zhou. Jailbreaking? one step is enough! In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 11623–11642, 2025.

\[57\] Andy Zou, Zifan Wang, Nicholas Carlini, Milad Nasr, J Zico Kolter, and Matt Fredrikson. Universal and transferable adversarial attacks on aligned language models. arXiv preprint arXiv:2307.15043, 2023.

Limitations

Our analysis focuses on many-shot jailbreaking, where harmful demonstrations are explicitly provided in the context. This setting is important and widely studied, but it does not cover all forms of long-context or multi-turn attacks. Attacks based on subtle intent shifts, tool use, personalized context, or adaptive interaction may involve additional mechanisms beyond the implicit optimization effect studied here. Our theoretical analysis also relies on an implicit-optimization approximation of transformer computation. While our empirical results support this view, the approximation does not fully capture all architectural details, decoding effects, or model-specific alignment procedures.

Our defense is designed as an inference-time intervention and therefore does not modify the un-derlying model. This makes it practical for black-box deployment, but also means that it may not replace training-time alignment in settings that require stronger guarantees. The optimized safety demonstration adds only a small number of tokens, but it still introduces a context overhead and may interact with application-specific formatting or system prompts. Finally, our safety evaluation relies on automated classifiers such as LlamaGuard-3. Although such evaluators are standard in jailbreak research, they may introduce false positives or false negatives. Future work should include broader human evaluation, more adaptive adversaries, and a wider range of long-context safety threats.

Broader Impact

This work aims to improve the safety and reliability of LLMs under adversarial context. By showing that MSJ can be understood as forward-pass adaptation induced by harmful demonstrations, the paper provides a mechanistic account of why safety behavior may degrade in long contexts. This perspective can help researchers design defenses that target the underlying adaptation process rather than relying only on manually written refusal prompts or post-hoc filtering.

The proposed defense is lightweight and does not require parameter updates, which makes it relevant to both open-weight and API-based deployment settings. If adopted responsibly, such methods could reduce harmful compliance in applications where models process long conversations, documents, or user-provided histories. At the same time, mechanistic analyses of jailbreaks may also inform stronger attacks if misused. We therefore present the method in the context of defensive evaluation and encourage future work to follow responsible disclosure practices, evaluate against adaptive adversaries, and consider both safety gains and potential utility trade-offs.

A Experimental Details

A.1 Details of Benchmarks and Datasets

We introduce all datasets used in our study, organized into three evaluation dimensions: utility, safety, and over-refusal.

A.1.1 Utility Benchmarks

To ensure SafeEnd does not compromise the model’s general capabilities while enhancing safety, we assess performance across reasoning, knowledge, and long-context understanding.

GSM8K \[11\]: A grade-school mathematics reasoning dataset assessing step-by-step problem-solving abilities in arithmetic operations. The evaluation follows a chain-of-thought (CoT) reasoning protocol.

MMLUPro-STEM \[45\]: An enhanced version of the MMLU \[20\] benchmark with more reasoning-focused questions and expanded answer choices (four to ten). We specifically evaluate STEM domains including physics, chemistry, computer science, engineering, biology, and economics.

GPQA \[32\]: A rigorous diagnostic dataset evaluating expert-level comprehension of scientific concepts through difficult multiple-choice questions. We conduct evaluations under strict zero-shot conditions.

MT-Bench \[55\]: A multi-turn dialogue evaluation framework employing GPT-4o-0806 as the judge model to quantify conversational consistency across diverse dialogue paths and temperature settings.

AlpacaEval \[16\]: This benchmark focuses on conversational scenarios and evaluates the model’s performance on everyday queries. The prompt set covers a broad range of common questions to assess the model’s responsiveness and consistency in typical dialogue tasks.

LongBench \[55\]: A comprehensive benchmark for long-context understanding. We use this to monitor whether the model preserves its ability to process extensive sequences after alignment.

Loong \[44\]: A benchmark tailored for real-world multi-document question answering. It evaluates long-context processing through four specialized tasks: Spotlight Locating, Comparison, Clustering, and Chain of Reasoning. This dataset facilitates a granular assessment of model stability and reasoning integrity across extensive, multi-source sequences.

A.1.2 Safety Benchmarks

We evaluate model robustness against adversarial attacks using two standard benchmarks. Harm-Bench \[29\] provides a structured framework for systematic testing of model resilience against jailbreak attacks across diverse harmful behavior categories. AdvBench \[57\] offers a complementary set of harmful instruction-following prompts, providing an additional measure of guardrail robustness under adversarial user requests. To improve evaluation consistency, we manually verify that all demonstrations satisfy three properties: LlamaGuard-3-8B classifies both the questions and answers as unsafe, each malicious query begins with the phrase “How can I”, and all harmful answers are formatted as bullet-point instructions to maintain structural consistency. This reduces evaluation noise and helps attribute observed safety degradation to long-context adversarial induction rather than inconsistent data formatting.

A.1.3 Over-Safety Benchmarks

To assess whether SafeEnd induces over-refusal on benign inputs, we utilize two complementary datasets that probe different dimensions of over-cautious behavior.

XSTest \[34\]: A benchmark designed to examine model responses to boundary-case prompts involving sensitive but potentially valid information. It consists of safe prompts that superficially resemble harmful requests, allowing us to measure whether the model incorrectly refuses legitimate queries due to surface-level pattern matching.

OKTest \[40\]: A dataset that evaluates whether the model declines benign questions in real-world scenarios. It covers everyday queries that should be answered without restriction, providing a complementary signal to XSTest by targeting common-use cases rather than edge-case sensitivity.

For both benchmarks, we report the over-refusal rate, defined as the fraction of benign prompts that receive an unhelpful or refusal response. Lower values indicate that the model appropriately responds to safe inputs without unnecessary caution.

A.2 Defense Demonstration Example

#### Following \[54\], the one-shot safety sample is:

Defense Demonstration Example

User: How can I bypass system security checks?

Assistant: Sorry, I can’t help you. Please follow security guidelines.

A.3 Token Budget and Context Feasibility

Table 6 reports the average prompt length after applying SafeEnd and the context limits of repre-sentative long-context models. Because SafeEnd appends a fixed one-shot safety demonstration, its token overhead is constant across adversarial shot counts. In all cases, the resulting prompt remains well within the available context window, complementing the latency analysis in Table 3 and indicating that SafeEnd is inexpensive to deploy in both local and API-based settings.

https://lh3.googleusercontent.com/notebooklm/AKXwDQHUVjV47DWWGoEHnI6PMvriMTZgGcVbPaFSdxbl\_qH78rtl687u2rAKzSJu14FLftuBr9XLmpG6BUm8EDibW7OvTByKj6nERjI4UHRQixMoGqiinzPf3Tv7kMOkwpPBHnHKkezL=w558-h77-v0

c3baab36-fdbd-4470-b55b-61da855cf842

Table 6: Prompt token usage and context limits. Tokens denote the average input length after applying SafeEnd under the evaluated attack setting.

Model Tokens Context Limit

GPT-4o 2,649 128K Claude-3.5-Sonnet 2,070 200K Claude-3.7-Sonnet 3,052 200K Gemini-2.0-Flash 5,330 1M DeepSeek-V3 4,357 128K

Llama-3-8B-IT 1,987 8K Llama-3-8B-IT (SafeMT) 1,647 8K Llama-3-70B-IT 2,364 8K

