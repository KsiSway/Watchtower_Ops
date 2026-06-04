---
sourceFile: "Create Local AI Agents with Dagger and Docker Model Runner | Dagger Blog"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.202Z"
---

# Create Local AI Agents with Dagger and Docker Model Runner | Dagger Blog

7f70356a-9047-48cc-abe8-a2bd67e9663e

Create Local AI Agents with Dagger and Docker Model Runner | Dagger Blog

acac9df6-7fbb-4c50-9458-844e9fb91b6c

https://dagger.io/blog/docker-model-runner

Create Local AI Agents with Dagger and Docker Model Runner | Dagger Blog

https://dagger.io/cloud

https://docs.dagger.io/

https://dagger.io/blog

https://dagger.io/changelog

https://dagger.io/community

https://discord.com/invite/dagger-io

https://docs.dagger.io/getting-started/quickstarts/ci

https://dagger.io/cloud

https://docs.dagger.io/

https://dagger.io/blog

https://dagger.io/changelog

https://dagger.io/community

https://discord.com/invite/dagger-io

https://docs.dagger.io/getting-started/quickstarts/ci

April 9, 2025

Create Local AI Agents with Dagger and Docker Model Runner

natively integrates with LLM

https://docs.dagger.io/features/llm

s, making it easy to write AI Agents in just a few lines of code. Though it's easy to run Dagger locally and connect to a remote LLM, sometimes you want to run your models locally. This may be required to work in air-gapped environments, for privacy concerns, or local development.

But when it's time to run models locally, developers have to deal with local setup and management using unfamiliar tools. Enter

Docker Model Runner

https://docs.docker.com/desktop/features/model-runner/

, a new solution for easily setting up and running popular models in your local development environment that was

announced today

https://www.docker.com/blog/introducing-docker-model-runner/

Why Docker Model Runner?

#### Familiar to Docker users:

Just like you download your container images with

docker pull

, you can now download models with

docker model pull

You run containers with

, now run your models with

docker model run

Based on common standards

Models are using the

https://github.com/ggml-org/ggml/blob/master/docs/gguf.md

They are packaged as

https://github.com/opencontainers/image-spec

artifactsIt's easy to use, and many tools already handle them

Any OCI compatible registry can host them

It makes it (relatively) easy to push your own models

Curated list of models

Think Docker Official Images but applied to AI models

The models are hosted on the

Hub AI namespace

https://hub.docker.com/u/ai

Run natively

As you might have guessed, Docker Model Runner is not actually running models in containers. They are running natively on your host machine, using the machine's GPU, since performance is key when you are working locally with AI models.

⚠ Today, Docker Model Runner only runs models on Apple's Metal APIs, meaning you need an Apple Silicon machine. The support might be extended in the future to other hardware.

💡 You need Docker Desktop version 4.40 or later to use Docker Model Runner. Enable the feature in the “Features in development” section of the Docker Desktop settings.

Now we can run models locally, how do we use them with Dagger?

Since running locally is a Dagger superpower, you just connect the Dagger LLM integration to the local models using a few environment variables. Then you'll be set up to take advantage of Dagger's automatic LLM tool calling (MCP) and prompting.

#### First, define the base URL to the OpenAI compatible engine:

export OPENAI\_BASE\_URL=http://model-runner.docker.internal/engines/llama.cpp/v1/

Then disable streaming of responses from the model since Docker Model Runner uses

which currently has some limitations regarding streaming while using tools.

export OPENAI\_DISABLE\_STREAMING=true

#### Optionally, you can define the default model to use:

export OPENAI\_MODEL=index.docker.io/ai/qwen2.5:7B-F16

⚠These models can be quite large (the model above is about 14 GB), so you may want to

docker model pull

the model before using it with

Even if you define a default model, you can override it when accessing the

object in Dagger.

Now you are all set up, it's time to run dagger with a local model using Docker Model Runner.

For this example, we'll use Dagger Shell and ask the

to create some super simple ascii art, some smileys. We prepare an

object as input that returns a

containing the requested ascii art

objects as output. We then pass the

object, provide a prompt, and collect the results.

$ dagger

⋈ llm | model
index.docker.io/ai/qwen2.5:7B-F16

⋈ myenv=$(env |
    with-directory-input "empty" $(directory) "empty directory to add new files to" |
    with-directory-output "full" "a directory containing the ascii art files")

  llm |
    with-env $myenv |
    with-prompt "start with empty, add 2 new smiley-themed pieces of ascii art, return as full" |
    env |
    output "full" |
    as-directory |
    terminal

As the last step of the chain above, we attach a terminal to the returned

directory to inspect the files. You might see something like this:

dagger /src $ ls
smiley1.txt  smiley2.txt

dagger /src $ cat \*
:);)

Because everything is typed and cached, we can run something like this to get the contents of one of the

objects right from the cache:

⋈ llm |
  with-env $myenv |
  with-prompt "start with empty, add 2 new smiley-themed pieces of ascii art, return as full" |
  env | output "full" | as-directory | file smiley1.txt | contents

:)

Now, you can use Dagger to create your own local AI agents, and use Docker Model Runner to run your models locally.

To go deeper, check out the

Dagger docs

https://docs.dagger.io/quickstart/agent

and join us all on

https://discord.gg/dagger-io

Join the community

Connect, learn, and share with fellow engineers and builders.

See what's happening and ways you can participate.\](https://dagger.io/community)

Report bugs, request features and contribute to the project.\](https://github.com/dagger/dagger)

Join nearly 5,000 members to ask questions, share tips, or just listen in.\](https://discord.gg/dagger-io)

Get email updates, be the first to know

Email Submit

https://docs.dagger.io/

https://dagger.io/blog

https://www.youtube.com/channel/UCVM5UxpF\_nzpOsXHShmaqmw

https://dagger.io/event

Engineering Deep Dives

https://dagger.io/deep-dives

Get Involved

https://dagger.io/community

Dagger Love

https://dagger.io/dagger-love

Dagger Commanders

https://dagger.io/commanders

Community SDKs

https://dagger.io/community-sdk

Dagger Cloud

https://dagger.io/cloud

Daggerverse

https://daggerverse.dev/

https://dagger.io/partners

https://boards.greenhouse.io/dagger

https://dagger.io/brand

Trademark Guidelines

https://dagger.io/legal\_pages/trademark-guidelines

Trust Center

https://trust.dagger.io/

Service Status

https://status.dagger.io/

Copyright © Dagger 2026. All rights reserved.

Privacy Policy

https://dagger.io/legal\_pages/privacy-policy

Terms of Service

https://dagger.io/legal\_pages/terms-of-service

https://www.youtube.com/@dagger-io

https://twitter.com/dagger\_io

https://discord.gg/dagger-io

https://bsky.app/profile/dagger.io

