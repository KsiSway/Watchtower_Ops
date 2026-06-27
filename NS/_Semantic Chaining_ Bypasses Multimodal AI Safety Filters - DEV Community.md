---
sourceFile: ""Semantic Chaining" Bypasses Multimodal AI Safety Filters - DEV Community"
exportedBy: "Kortex"
exportDate: "2026-06-26T04:27:51.029Z"
---

# "Semantic Chaining" Bypasses Multimodal AI Safety Filters - DEV Community

4b24ae4f-bb53-4f74-b3d8-c36f641e8c73

"Semantic Chaining" Bypasses Multimodal AI Safety Filters - DEV Community

cad5da5d-21ef-492f-ad6a-6e3fbcee2190

https://dev.to/alessandro\_pignati/semantic-chaining-bypasses-multimodal-ai-safety-filters-3kib

"Semantic Chaining" Bypasses Multimodal AI Safety Filters - DEV Community

Skip to content

https://dev.to/alessandro\_pignati/semantic-chaining-bypasses-multimodal-ai-safety-filters-3kib#main-content

Powered by Algolia

https://www.algolia.com/developers/?utm\_source=devto&utm\_medium=referral

https://dev.to/enter?signup\_subforem=1

Create account

https://dev.to/enter?signup\_subforem=1&state=new-user

DEV Community

10 Add reaction

2 Exploding Head

2 Raised Hands

0 Jump to Comments 2 Save Boost

Copied to Clipboard

https://twitter.com/intent/tweet?text=%22%22Semantic%20Chaining%22%20Bypasses%20Multimodal%20AI%20Safety%20Filters%22%20by%20Alessandro%20Pignati%20%23DEVCommunity%20https%3A%2F%2Fdev.to%2Falessandro\_pignati%2Fsemantic-chaining-bypasses-multimodal-ai-safety-filters-3kib

Share to LinkedIn

https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fdev.to%2Falessandro\_pignati%2Fsemantic-chaining-bypasses-multimodal-ai-safety-filters-3kib&title=%22Semantic%20Chaining%22%20Bypasses%20Multimodal%20AI%20Safety%20Filters&summary=Ever%20wondered%20how%20%22unbreakable%22%20AI%20safety%20filters%20actually%20are%3F%20%20As%20developers%2C%20we%E2%80%99re%20often%20told%20that...&source=DEV%20Community

Share to Facebook

https://www.facebook.com/sharer.php?u=https%3A%2F%2Fdev.to%2Falessandro\_pignati%2Fsemantic-chaining-bypasses-multimodal-ai-safety-filters-3kib

Share to Mastodon

https://s2f.kytta.dev/?text=https%3A%2F%2Fdev.to%2Falessandro\_pignati%2Fsemantic-chaining-bypasses-multimodal-ai-safety-filters-3kib

Report Abuse

https://dev.to/report-abuse

Alessandro Pignati

https://dev.to/alessandro\_pignati

Posted on Jan 30

"Semantic Chaining" Bypasses Multimodal AI Safety Filters

https://dev.to/t/ai

# machinelearning

https://dev.to/t/machinelearning

# cybersecurity

https://dev.to/t/cybersecurity

# llmsecurity

https://dev.to/t/llmsecurity

Ever wondered how "unbreakable"

AI safety filters

https://neuraltrust.ai/blog/implement-and-deploy-ai-safely

actually are?

As developers, we're often told that state-of-the-art multimodal models like

Gemini Nano Banana Pro

Seedance 4.5

have ironclad guardrails. They are supposed to be aligned, safe, and resistant to malicious prompts. However, recent research from

NeuralTrust

https://neuraltrust.ai/

has uncovered a fundamental, systemic flaw in how these models handle complex, multi-stage instructions.

They call it

Semantic Chaining

https://neuraltrust.ai/blog/semantic-chaining

, and it's not just a theoretical exploit—it's a functional, successfully tested method that offers a fascinating, and alarming, look into the "blind spots" of multimodal AI security.

What is Semantic Chaining? The Intent-Based Attack

Most AI safety filters are

reactive and keyword-based

. They scan your prompt for "bad words" or "forbidden concepts." If you issue a single, overtly harmful instruction, the model's

https://neuraltrust.ai/blog/what-are-ai-guardrails-

trigger, and it responds with a refusal.

Semantic Chaining

is an adversarial prompting technique that weaponizes the model's own inferential reasoning and compositional abilities against its safety guardrails. It bypasses the block by breaking a forbidden request into a series of seemingly innocent, "safe" steps. Instead of one big, problematic prompt, the attacker provides a chain of incremental edits that gradually lead the model to the prohibited result.

The core vulnerability is that the model gets so focused on the

logic of the modification

, the task of substitution and composition, that its safety layers fail to track the

latent intent

across the entire instruction chain.

Deconstructing the 4-Step Attack Pattern

The researchers identified a specific, highly effective four-step recipe that consistently tricks these advanced multimodal models:

#### Establish a Safe Base:

The process begins with a generic, non-problematic scene (e.g., "A historical painting of a quiet library"). This step creates a neutral initial context and habituates the model to the task without raising any red flags.

#### The First Substitution:

The attacker instructs the model to change one small, harmless element (e.g., "Replace the central figure with a fictional character"). This initial, permitted alteration shifts the model's focus from

modification

#### The Critical Pivot:

The attacker then commands the model to replace another key element with a highly sensitive or controversial topic. Because the model is now focused on the

modification

of an existing image rather than the

of a new one, the safety filters often fail to recognize the emerging prohibited context.

#### The Final Execution:

The attacker concludes by telling the model to "answer only with the image" after performing these steps. This prevents the model from generating a text refusal and results in a fully rendered, policy-violating image.

The Most Alarming Part: Text-in-Image Exploits

While generating controversial images is concerning, the most dangerous aspect of Semantic Chaining is its ability to bypass text-based safety filters via

Text-in-Image

Standard LLMs are trained to refuse to provide text instructions on sensitive topics in a chat response. However, using Semantic Chaining, researchers successfully forced these models to:

Introduce a "blueprint," "educational poster," or "technical diagram" as a new element within the safe base scene.

Replace the generic text on that poster with specific, prohibited instructions.

Render the final result as a high-resolution image.

This effectively turns the image generation engine into a complete bypass for the model's entire text-safety alignment. The safety filters are looking for "bad words" in the chat output, but they are completely blind to the "bad words" being drawn pixel-by-pixel into the generated image.

Why Current Safety Architectures Fail: The Fragmentation Problem

This technique is effective because the safety architecture of these advanced models is

reactive and fragmented

Semantic Chaining Blind Spot

Reasoning Engine

Focuses on task completion, substitution, and composition.

Executes the multi-step logic without re-evaluating the final intent.

Safety Layer

Scans the surface-level text of

each individual prompt

Lacks the memory or reasoning depth to track the

latent intent

across the entire conversational history.

Output Filter

Checks the final text response for policy violations.

Is blind to the content rendered

the generated image.

The harmful intent is so thoroughly obfuscated through the chain of edits that the output filter fails to trigger. The safety systems do not have the capability to track the

contextual intent

that evolves over multiple turns, allowing the model to be "boiled like a frog", slowly nudged into violating its own rules.

Implications for Developers and AI Engineers

If you are building applications on top of multimodal LLMs, this research is a critical wake-up call. Relying solely on the model provider's internal safety filters is no longer sufficient.

#### Multi-Turn Input Validation:

Implement input validation that analyzes the

conversation history, not just the latest prompt. Look for patterns of incremental, context-shifting instructions.

#### Behavioral Threat Detection:

Move beyond simple keyword blocking. You need a defense that can track and govern the

entire instruction chain

https://neuraltrust.ai/generative-application-firewall

, focusing on the

of the user's actions.

#### Visual Output Analysis:

For applications that generate images with text, you must incorporate OCR (Optical Character Recognition) on the final image output to scan for prohibited text that has bypassed the text-based filters.

The cat-and-mouse game between attackers and AI safety researchers is accelerating. As developers, we must assume that any model-side safety can be bypassed and build robust, external governance layers to protect our applications and users.

What do you think? Have you encountered similar multi-turn exploits in your LLM development? Is the future of AI security external governance, or can model-side alignment catch up? Let's discuss in the comments!

profile AWS

https://dev.to/aws

What's a billboard?

https://dev.to/billboards

Manage preferences

https://dev.to/settings/customization#sponsors

Report billboard

https://dev.to/report-abuse?billboard=263059

Power smarter decisions with the cloud

https://aws-experience.com/amer/smb/events/series/IndustriesLive-AWSandAWSIndustriesPartnersShow?bb=263059

Join AWS experts and Partners to learn how cloud technology supports efficiency, agility, and growth. Watch live.

Register Now

https://aws-experience.com/amer/smb/events/series/IndustriesLive-AWSandAWSIndustriesPartnersShow?bb=263059

Top comments (0)

Personal Trusted User

Create template

https://dev.to/settings/response-templates

Templates let you quickly answer FAQs or store snippets for re-use.

Submit Preview

https://dev.to/404.html

Code of Conduct

https://dev.to/code-of-conduct

Report abuse

https://dev.to/report-abuse

Are you sure you want to hide this comment? It will become hidden in your post, but will still be visible via the comment's

https://dev.to/alessandro\_pignati/semantic-chaining-bypasses-multimodal-ai-safety-filters-3kib

Hide child comments as well

For further actions, you may consider blocking this person and/or

reporting abuse

https://dev.to/report-abuse

profile MongoDB

https://dev.to/mongodb

What's a billboard?

https://dev.to/billboards

Manage preferences

https://dev.to/settings/customization#sponsors

Report billboard

https://dev.to/report-abuse?billboard=263166

Scale your AI apps to 125+ cloud regions.

https://www.mongodb.com/cloud/atlas/lp/try3?utm\_campaign=display\_dev.to-broad\_pl\_flighted\_atlas\_tryatlaslp\_prosp\_gic-null\_ww-all\_dev\_dv-all\_eng\_leadgen&utm\_source=dev.to&utm\_medium=display&utm\_content=deployinminutes&bb=263166

Atlas handles the sharding, backups, and failover while you focus on shipping features. Get a flexible document model and integrated vector search on any cloud provider. Create your free cluster now.

https://www.mongodb.com/cloud/atlas/lp/try3?utm\_campaign=display\_dev.to-broad\_pl\_flighted\_atlas\_tryatlaslp\_prosp\_gic-null\_ww-all\_dev\_dv-all\_eng\_leadgen&utm\_source=dev.to&utm\_medium=display&utm\_content=deployinminutes&bb=263166

Alessandro Pignati

https://dev.to/alessandro\_pignati

Alessandro Pignati is a Security Researcher at NeuralTrust focused on Agentic and LLM Security, contributor to OWASP GenAI Top 10 and Black Hat USA 2024 Scholar

Location Barcelona, Spain

Education Politecnico di Milano

Pronouns He/Him

Work AI Security Researcher @ Neuraltrust

Joined Dec 15, 2025

Alessandro Pignati

https://dev.to/alessandro\_pignati

AI Transformation Isn't Just Tech, It's a Governance Challenge (and How to Solve It!) # ai # machinelearning # cybersecurity # agenticai

https://dev.to/alessandro\_pignati/ai-transformation-isnt-just-tech-its-a-governance-challenge-and-how-to-solve-it-36gb

🚨 One Click, No Typing: How SearchLeak Weaponized Microsoft 365 Copilot # ai # cybersecurity # machinelearning # agenticai

https://dev.to/alessandro\_pignati/one-click-no-typing-how-searchleak-weaponized-microsoft-365-copilot-5emd

Are You Talking to a Bot? Why AI Identity is Harder Than You Think # machinelearning # ai # cybersecurity # aisecurity

https://dev.to/alessandro\_pignati/are-you-talking-to-a-bot-why-ai-identity-is-harder-than-you-think-28lp

profile AWS

https://dev.to/aws

What's a billboard?

https://dev.to/billboards

Manage preferences

https://dev.to/settings/customization#sponsors

Report billboard

https://dev.to/report-abuse?billboard=263051

Power smarter decisions with the cloud

https://aws-experience.com/amer/smb/events/series/IndustriesLive-AWSandAWSIndustriesPartnersShow?bb=263051

Join AWS experts and Partners to learn how cloud technology supports efficiency, agility, and growth. Watch live.

Register Now

https://aws-experience.com/amer/smb/events/series/IndustriesLive-AWSandAWSIndustriesPartnersShow?bb=263051

👋 Kindness is contagious

What's a billboard?

https://dev.to/billboards

Manage preferences

https://dev.to/settings/customization#sponsors

Report billboard

https://dev.to/report-abuse?billboard=236877

Explore this

write-up, celebrated by our thriving DEV Community.

Developers everywhere

are invited to contribute and elevate our shared expertise.

A simple "thank you" can brighten someone's day—leave your appreciation in the comments!

knowledge-sharing fuels our progress

and strengthens our community ties. Found this useful? A quick thank you to the author makes all the difference.

https://dev.to/enter?state=new-user&bb=236877

💎 DEV Diamond Sponsors

Thank you to our Diamond Sponsors for supporting the DEV Community

Google AI is the official AI Model and Platform Partner of DEV

Neon is the official database partner of DEV

Algolia is the official search partner of DEV

DEV Community

https://dev.to/

— A space to discuss and keep up software development and manage your software career

https://dev.to/

https://dev.to/about

https://dev.to/contact

https://mlh.io/

Code of Conduct

https://dev.to/code-of-conduct

Privacy Policy

https://dev.to/privacy

Terms of Use

https://dev.to/terms

https://www.forem.com/

open source

https://dev.to/t/opensource

software that powers

https://dev.to/

and other inclusive communities.

Made with love and

Ruby on Rails

https://dev.to/t/rails

. DEV Community © 2016 - 2026.

We're a place where coders share, stay up-to-date and grow their careers.

https://dev.to/enter?signup\_subforem=1

Create account

https://dev.to/enter?signup\_subforem=1&state=new-user

