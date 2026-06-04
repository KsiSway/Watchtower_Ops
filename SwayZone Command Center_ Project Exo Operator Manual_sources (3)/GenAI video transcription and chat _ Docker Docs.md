---
sourceFile: "GenAI video transcription and chat | Docker Docs"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.425Z"
---

# GenAI video transcription and chat | Docker Docs

94a5c8a5-6d40-4ce7-b4ab-e93b987e4c3f

GenAI video transcription and chat | Docker Docs

9f7e7f35-2faa-4d1e-9efc-a6ddfb686089

https://docs.docker.com/guides/genai-video-bot/

GenAI video transcription and chat | Docker Docs

Insights on the state of AI agents from 800+ builders and leaders. Download your copy

https://www.docker.com/resources/the-state-of-agentic-ai-white-paper/

https://docs.docker.com/

Get started

https://docs.docker.com/get-started/

https://docs.docker.com/guides/

https://docs.docker.com/manuals/

https://docs.docker.com/reference/

Gordon, your AI assistant for Docker docs

Start a new chat

What can I help you with?

I'm Gordon, your AI assistant for Docker and documentation questions.

Get started with Docker

Docker Hardened Images

MCP Toolkit

Create an org

When enabled, Gordon considers the current page you're viewing to provide more relevant answers.

Share feedback

https://github.com/docker/docs/issues/23966

Answers are generated based on the documentation.

https://docs.docker.com/guides/

Get started

https://docs.docker.com/get-started/

https://docs.docker.com/manuals/

https://docs.docker.com/reference/

GenAI video transcription and chat

https://docs.docker.com/guides/genai-video-bot/

Learn how to build and deploy a generative AI video analysis and transcription bot using Docker.

« Back to all guides

https://docs.docker.com/guides/

https://docs.docker.com/

https://docs.docker.com/guides/

/ Video transcription and chat

GenAI video transcription and chat

Ask Gordon Copy Markdown View Markdown

Table of contents

https://docs.docker.com/guides/genai-video-bot/#overview

Prerequisites

https://docs.docker.com/guides/genai-video-bot/#prerequisites

About the application

https://docs.docker.com/guides/genai-video-bot/#about-the-application

Get and run the application

https://docs.docker.com/guides/genai-video-bot/#get-and-run-the-application

Using the yt-whisper service

https://docs.docker.com/guides/genai-video-bot/#using-the-yt-whisper-service

Using the dockerbot service

https://docs.docker.com/guides/genai-video-bot/#using-the-dockerbot-service

Explore the application architecture

https://docs.docker.com/guides/genai-video-bot/#explore-the-application-architecture

Explore the technologies used and their role

https://docs.docker.com/guides/genai-video-bot/#explore-the-technologies-used-and-their-role

Docker and Docker Compose

https://docs.docker.com/guides/genai-video-bot/#docker-and-docker-compose

https://docs.docker.com/guides/genai-video-bot/#openai-api

https://docs.docker.com/guides/genai-video-bot/#whisper

https://docs.docker.com/guides/genai-video-bot/#embeddings

Chat completions

https://docs.docker.com/guides/genai-video-bot/#chat-completions

https://docs.docker.com/guides/genai-video-bot/#pinecone

Retrieval-Augmented Generation

https://docs.docker.com/guides/genai-video-bot/#retrieval-augmented-generation

https://docs.docker.com/guides/genai-video-bot/#next-steps

https://docs.docker.com/guides/genai-video-bot/#overview

This guide presents a project on video transcription and analysis using a set of technologies related to the

GenAI Stack

https://www.docker.com/blog/introducing-a-new-genai-stack/

#### The project showcases the following technologies:

Docker and Docker Compose

https://docs.docker.com/guides/genai-video-bot/#docker-and-docker-compose

https://docs.docker.com/guides/genai-video-bot/#openai-api

https://docs.docker.com/guides/genai-video-bot/#whisper

https://docs.docker.com/guides/genai-video-bot/#embeddings

Chat completions

https://docs.docker.com/guides/genai-video-bot/#chat-completions

https://docs.docker.com/guides/genai-video-bot/#pinecone

Retrieval-Augmented Generation

https://docs.docker.com/guides/genai-video-bot/#retrieval-augmented-generation

Acknowledgment

This guide is a community contribution. Docker would like to thank

David Cardozo

https://www.davidcardozo.com/

for his contribution to this guide.

Prerequisites

https://docs.docker.com/guides/genai-video-bot/#prerequisites

You have an

OpenAI API Key

https://platform.openai.com/api-keys

. Note OpenAI is a third-party hosted service and

https://openai.com/pricing

Pinecone API Key

https://app.pinecone.io/

You have installed the latest version of

Docker Desktop

https://docs.docker.com/get-started/get-docker/

. Docker adds new features regularly and some parts of this guide may work only with the latest version of Docker Desktop.

https://git-scm.com/downloads

. The examples in this section use a command-line based Git client, but you can use any client.

About the application

https://docs.docker.com/guides/genai-video-bot/#about-the-application

The application is a chatbot that can answer questions from a video. In addition, it provides timestamps from the video that can help you find the sources used to answer your question.

Get and run the application

https://docs.docker.com/guides/genai-video-bot/#get-and-run-the-application

Clone the sample application's repository. In a terminal, run the following command.

$ git clone https://github.com/Davidnet/docker-genai.git

#### The project contains the following directories and files:

├── docker-genai/
│ ├── docker-bot/
│ ├── yt-whisper/
│ ├── .env.example
│ ├── .gitignore
│ ├── LICENSE
│ ├── README.md
│ └── docker-compose.yaml

Specify your API keys. In the

docker-genai

directory, create a text file called

and specify your API keys inside. The following is the contents of the

.env.example

file that you can refer to as an example.

#----------------------------------------------------------------------------
# OpenAI
#----------------------------------------------------------------------------
OPENAI\_TOKEN=your-api-key # Replace your-api-key with your personal API key

#----------------------------------------------------------------------------
# Pinecone
#----------------------------------------------------------------------------
PINECONE\_TOKEN=your-api-key # Replace your-api-key with your personal API key

Build and run the application. In a terminal, change directory to your

docker-genai

directory and run the following command.

$ docker compose up --build

Docker Compose builds and runs the application based on the services defined in the

docker-compose.yaml

file. When the application is running, you'll see the logs of 2 services in the terminal. In the logs, you'll see the services are exposed on ports

. The two services are complimentary to each other. The

service is running on port

. This service feeds the Pinecone database with videos that you want to archive in your knowledge database. The following section explores this service.

Using the yt-whisper service

https://docs.docker.com/guides/genai-video-bot/#using-the-yt-whisper-service

The yt-whisper service is a YouTube video processing service that uses the OpenAI Whisper model to generate transcriptions of videos and stores them in a Pinecone database. The following steps show how to use the service.

Open a browser and access the yt-whisper service at

http://localhost:8503

http://localhost:8503/

Once the application appears, in the

Youtube URL

field specify a Youtube video URL and select

. The following example uses

https://www.youtube.com/watch?v=yaQZFhrW0fU

https://www.youtube.com/watch?v=yaQZFhrW0fU

The yt-whisper service downloads the audio of the video, uses Whisper to transcribe it into a WebVTT (

) format (which you can download), then uses the text-embedding-3-small model to create embeddings, and finally uploads those embeddings in to the Pinecone database. After processing the video, a video list appears in the web app that informs you which videos have been indexed in Pinecone. It also provides a button to download the transcript.

You can now access the dockerbot service on port

and ask questions about the videos.

Using the dockerbot service

https://docs.docker.com/guides/genai-video-bot/#using-the-dockerbot-service

The dockerbot service is a question-answering service that leverages both the Pinecone database and an AI model to provide responses. The following steps show how to use the service.

You must process at least one video via the

yt-whisper service

https://docs.docker.com/guides/genai-video-bot/#using-the-yt-whisper-service

before using the dockerbot service.

Open a browser and access the service at

http://localhost:8504

http://localhost:8504/

What do you want to know about your videos?

text box, ask the Dockerbot a question about a video that was processed by the yt-whisper service. The following example asks the question, "What is a sugar cookie?". The answer to that question exists in the video processed in the previous example,

https://www.youtube.com/watch?v=yaQZFhrW0fU

https://www.youtube.com/watch?v=yaQZFhrW0fU

In this example, the Dockerbot answers the question and provides links to the video with timestamps, which may contain more information about the answer. The dockerbot service takes the question, turns it into an embedding using the text-embedding-3-small model, queries the Pinecone database to find similar embeddings, and then passes that context into the gpt-4-turbo-preview to generate an answer.

Select the first link to see what information it provides. Based on the previous example, select

https://www.youtube.com/watch?v=yaQZFhrW0fU&t=553s

https://www.youtube.com/watch?v=yaQZFhrW0fU&t=553s

. In the example link, you can see that the section of video perfectly answers the question, "What is a sugar cookie?".

Explore the application architecture

https://docs.docker.com/guides/genai-video-bot/#explore-the-application-architecture

The following image shows the application's high-level service architecture, which includes:

yt-whisper: A local service, ran by Docker Compose, that interacts with the remote OpenAI and Pinecone services.

dockerbot: A local service, ran by Docker Compose, that interacts with the remote OpenAI and Pinecone services.

OpenAI: A remote third-party service.

Pinecone: A remote third-party service.

Explore the technologies used and their role

https://docs.docker.com/guides/genai-video-bot/#explore-the-technologies-used-and-their-role

Docker and Docker Compose

https://docs.docker.com/guides/genai-video-bot/#docker-and-docker-compose

The application uses Docker to run the application in containers, providing a consistent and isolated environment for running it. This means the application will operate as intended within its Docker containers, regardless of the underlying system differences. To learn more about Docker, see the

Getting started overview

https://docs.docker.com/get-started/introduction/

Docker Compose is a tool for defining and running multi-container applications. Compose makes it easy to run this application with a single command,

docker compose up

. For more details, see the

Compose overview

https://docs.docker.com/compose/

https://docs.docker.com/guides/genai-video-bot/#openai-api

The OpenAI API provides an LLM service that's known for its cutting-edge AI and machine learning technologies. In this application, OpenAI's technology is used to generate transcriptions from audio (using the Whisper model) and to create embeddings for text data, as well as to generate responses to user queries (using GPT and chat completions). For more details, see

https://openai.com/product

https://docs.docker.com/guides/genai-video-bot/#whisper

Whisper is an automatic speech recognition system developed by OpenAI, designed to transcribe spoken language into text. In this application, Whisper is used to transcribe the audio from YouTube videos into text, enabling further processing and analysis of the video content. For more details, see

Introducing Whisper

https://openai.com/research/whisper

https://docs.docker.com/guides/genai-video-bot/#embeddings

Embeddings are numerical representations of text or other data types, which capture their meaning in a way that can be processed by machine learning algorithms. In this application, embeddings are used to convert video transcriptions into a vector format that can be queried and analyzed for relevance to user input, facilitating efficient search and response generation in the application. For more details, see OpenAI's

https://platform.openai.com/docs/guides/embeddings

documentation.

Chat completions

https://docs.docker.com/guides/genai-video-bot/#chat-completions

Chat completion, as utilized in this application through OpenAI's API, refers to the generation of conversational responses based on a given context or prompt. In the application, it is used to provide intelligent, context-aware answers to user queries by processing and integrating information from video transcriptions and other inputs, enhancing the chatbot's interactive capabilities. For more details, see OpenAI's

Chat Completions API

https://platform.openai.com/docs/guides/text-generation

documentation.

https://docs.docker.com/guides/genai-video-bot/#pinecone

Pinecone is a vector database service optimized for similarity search, used for building and deploying large-scale vector search applications. In this application, Pinecone is employed to store and retrieve the embeddings of video transcriptions, enabling efficient and relevant search functionality within the application based on user queries. For more details, see

https://www.pinecone.io/

Retrieval-Augmented Generation

https://docs.docker.com/guides/genai-video-bot/#retrieval-augmented-generation

Retrieval-Augmented Generation (RAG) is a technique that combines information retrieval with a language model to generate responses based on retrieved documents or data. In RAG, the system retrieves relevant information (in this case, via embeddings from video transcriptions) and then uses a language model to generate responses based on this retrieved data. For more details, see OpenAI's cookbook for

Retrieval Augmented Generative Question Answering with Pinecone

https://cookbook.openai.com/examples/vector\_databases/pinecone/gen\_qa

https://docs.docker.com/guides/genai-video-bot/#next-steps

Explore how to

create a PDF bot application

https://docs.docker.com/guides/genai-pdf-bot/

using generative AI, or view more GenAI samples in the

GenAI Stack

https://github.com/docker/genai-stack

repository.

Edit this page

https://github.com/docker/docs/edit/main/content/guides/genai-video-bot/index.md

Request changes

https://github.com/docker/docs/issues/new?template=doc\_issue.yml&location=https%3a%2f%2fdocs.docker.com%2fguides%2fgenai-video-bot%2f&labels=status%2Ftriage

Table of contents

https://docs.docker.com/guides/genai-video-bot/#overview

Prerequisites

https://docs.docker.com/guides/genai-video-bot/#prerequisites

About the application

https://docs.docker.com/guides/genai-video-bot/#about-the-application

Get and run the application

https://docs.docker.com/guides/genai-video-bot/#get-and-run-the-application

Using the yt-whisper service

https://docs.docker.com/guides/genai-video-bot/#using-the-yt-whisper-service

Using the dockerbot service

https://docs.docker.com/guides/genai-video-bot/#using-the-dockerbot-service

Explore the application architecture

https://docs.docker.com/guides/genai-video-bot/#explore-the-application-architecture

Explore the technologies used and their role

https://docs.docker.com/guides/genai-video-bot/#explore-the-technologies-used-and-their-role

Docker and Docker Compose

https://docs.docker.com/guides/genai-video-bot/#docker-and-docker-compose

https://docs.docker.com/guides/genai-video-bot/#openai-api

https://docs.docker.com/guides/genai-video-bot/#whisper

https://docs.docker.com/guides/genai-video-bot/#embeddings

Chat completions

https://docs.docker.com/guides/genai-video-bot/#chat-completions

https://docs.docker.com/guides/genai-video-bot/#pinecone

Retrieval-Augmented Generation

https://docs.docker.com/guides/genai-video-bot/#retrieval-augmented-generation

https://docs.docker.com/guides/genai-video-bot/#next-steps

https://www.linkedin.com/company/docker

https://x.com/docker/

https://www.facebook.com/docker.run

http://www.youtube.com/user/dockerrun

https://www.instagram.com/dockerinc/

Product offerings

https://www.docker.com/

https://www.docker.com/pricing?ref=Docs&refAction=DocsFooter

https://www.docker.com/company/

https://docs.docker.com/llms.txt

llms-full.txt

https://docs.docker.com/llms-full.txt

Cookies Settings |

Terms of Service

https://www.docker.com/legal/docker-terms-service

https://www.dockerstatus.com/

https://www.docker.com/legal

Copyright © 2013-2026 Docker Inc. All rights reserved.

Search this site Results will appear as you type Clear

Start typing to search the documentation

By clicking “Accept All Cookies”, you agree to the storing of cookies on your device to enhance site navigation, analyze site usage, and assist in our marketing efforts.

Cookies Settings Reject All Accept All Cookies

Privacy Preference Center

When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer.

More information

https://cookiepedia.co.uk/giving-consent-to-cookies

Manage Consent Preferences

Functional Cookies

Functional Cookies

These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.

Strictly Necessary Cookies

Always Active

These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.

Performance Cookies

Performance Cookies

These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance.

Targeting Cookies

Targeting Cookies

These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.

Cookie List

checkbox label label

Apply Cancel

Consent Leg.Interest

checkbox label label

checkbox label label

checkbox label label

Reject All Confirm My Choices

