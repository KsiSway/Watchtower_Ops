---
sourceFile: "ai/gemma3 - Docker Image"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.900Z"
---

# ai/gemma3 - Docker Image

4bb927bd-b318-47e3-96b6-8ec5ad464063

ai/gemma3 - Docker Image

7e2380de-bdbe-48f8-baa7-8085b97e360a

https://hub.docker.com/r/ai/gemma3

Verified Publisher

https://hub.docker.com/u/ai

- Updated   8 months ago

Google’s latest Gemma, small yet strong for chat and generation

ai / gemma3  repository overview

GGUF version by Unsloth

Gemma is a versatile AI model family designed for tasks like question answering, summarization, and reasoning. With open weights and responsible commercial use, it supports image-text input, a 128K token context, and over 140 languages.

Intended uses

#### Gemma 3 4B model can be used for:

#### Text generation:

Create poems, scripts, code, marketing copy, and email drafts.

#### Chatbots and conversational AI:

Enable virtual assistants and customer service bots.

#### Text summarization:

Produce concise summaries of reports and research papers.

#### Image data extraction:

Interpret and summarize visual data for text-based communication.

#### Language learning tools:

Aid in grammar correction and interactive writing practice.

#### Knowledge exploration:

Assist researchers by generating summaries and answering questions.

Characteristics

Attribute Details

Google DeepMind

Architecture

Cutoff date

140 languages

Tool calling

Input modalities

Text, Image

Output modalities

Gemma Terms ⁠

Available model variants

Model variant Parameters Quantization Context window VRAM¹ Size ai/gemma3:4B 
 ai/gemma3:4B-Q4\_K\_M 
 ai/gemma3:latest 4B MOSTLY\_Q4\_K\_M 131K tokens 3.83 GiB 2.31 GB ai/gemma3:270M-F16 270M MOSTLY\_F16 33K tokens 1.59 GiB 511.46 MB ai/gemma3:270M-UD-IQ2\_XXS 270M MOSTLY\_IQ2\_XXS 33K tokens 1.26 GiB 165.54 MB ai/gemma3:270M-UD-Q4\_K\_XL 270M MOSTLY\_Q4\_K\_M 33K tokens 1.33 GiB 235.95 MB ai/gemma3:4B-F16 4B MOSTLY\_BF16 131K tokens 8.75 GiB 7.23 GB

¹: VRAM estimated based on model characteristics.

latest  →  4B

Use this AI model with Docker Model Runner

#### First, pull the model:

docker model pull ai/gemma3

#### Then run the model:

docker model run ai/gemma3

For more information on Docker Model Runner,

explore the documentation ⁠

https://docs.docker.com/desktop/features/model-runner/

https://docs.docker.com/desktop/features/model-runner/

Benchmark performance

Category Benchmark Value General MMLU 59.6 GSM8K 38.4 ARC-Challenge 56.2 BIG-Bench Hard 50.9 DROP 60.1 STEM & Code MATH 24.2 MBPP 46.0 HumanEval 36.0 Multilingual MGSM 34.7 Global-MMLU-Lite 57.0 XQuAD (all) 68.0 Multimodal VQAv2 63.9 TextVQA 58.9 DocVQA 72.8

https://docs.docker.com/desktop/features/model-runner/

Gemma 3 Model Overview ⁠

https://docs.docker.com/desktop/features/model-runner/

Gemma 3 Technical Report ⁠

https://docs.docker.com/desktop/features/model-runner/

Unsloth Dynamic 2.0 GGUF ⁠

https://docs.docker.com/desktop/features/model-runner/

Tag summary

latest Recent tags

Content type

sha256:a353a8898 …

Last updated

8 months ago

docker model pull ai/gemma3

This week's pulls

Learn more ⁠

https://docs.docker.com/desktop/features/model-runner/

