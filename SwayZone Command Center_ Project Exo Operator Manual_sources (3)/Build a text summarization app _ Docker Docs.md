---
sourceFile: "Build a text summarization app | Docker Docs"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.160Z"
---

# Build a text summarization app | Docker Docs

d674c6c9-bc9d-4eea-9735-2238d105045f

Build a text summarization app | Docker Docs

ced7c7ab-128d-4619-8703-c091df9b592c

https://docs.docker.com/guides/text-summarization/

Build a text summarization app | Docker Docs

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

Build a text summarization app

https://docs.docker.com/guides/text-summarization/

This guide shows how to containerize text summarization models with Docker.

« Back to all guides

https://docs.docker.com/guides/

https://docs.docker.com/

https://docs.docker.com/guides/

/ Text summarization

Build a text summarization app

Ask Gordon Copy Markdown View Markdown

Table of contents

https://docs.docker.com/guides/text-summarization/#overview

Prerequisites

https://docs.docker.com/guides/text-summarization/#prerequisites

Get the sample application

https://docs.docker.com/guides/text-summarization/#get-the-sample-application

Explore the application code

https://docs.docker.com/guides/text-summarization/#explore-the-application-code

Explore the application environment

https://docs.docker.com/guides/text-summarization/#explore-the-application-environment

Run the application

https://docs.docker.com/guides/text-summarization/#run-the-application

https://docs.docker.com/guides/text-summarization/#summary

https://docs.docker.com/guides/text-summarization/#next-steps

https://docs.docker.com/guides/text-summarization/#overview

In this guide, you'll learn how to build and run a text summarization application. You'll build the application using Python with the Bert Extractive Summarizer, and then set up the environment and run the application using Docker.

The sample text summarization application uses the Bert Extractive Summarizer. This tool utilizes the HuggingFace Pytorch transformers library to run extractive summarizations. This works by first embedding the sentences, then running a clustering algorithm, finding the sentences that are closest to the cluster's centroids.

Prerequisites

https://docs.docker.com/guides/text-summarization/#prerequisites

You have installed the latest version of

Docker Desktop

https://docs.docker.com/get-started/get-docker/

. Docker adds new features regularly and some parts of this guide may work only with the latest version of Docker Desktop.

https://git-scm.com/downloads

. The examples in this section use a command-line based Git client, but you can use any client.

Get the sample application

https://docs.docker.com/guides/text-summarization/#get-the-sample-application

Open a terminal, and clone the sample application's repository using the following command.

$ git clone https://github.com/harsh4870/Docker-NLP.git

Verify that you cloned the repository. You should see the following files in your

01\_sentiment\_analysis.py
02\_name\_entity\_recognition.py
03\_text\_classification.py
04\_text\_summarization.py
05\_language\_translation.py
entrypoint.sh
requirements.txt
Dockerfile
README.md

Explore the application code

https://docs.docker.com/guides/text-summarization/#explore-the-application-code

The source code for the text summarization application is in the

Docker-NLP/04\_text\_summarization.py

04\_text\_summarization.py

in a text or code editor to explore its contents in the following steps.

Import the required libraries.

from summarizer import Summarizer

This line of code imports the

class from the

package, essential for your text summarization application. The summarizer module implements the Bert Extractive Summarizer, leveraging the HuggingFace Pytorch transformers library, renowned in the NLP (Natural Language Processing) domain. This library offers access to pre-trained models like BERT, which revolutionized language understanding tasks, including text summarization. The BERT model, or Bidirectional Encoder Representations from Transformers, excels in understanding context in language, using a mechanism known as "attention" to determine the significance of words in a sentence. For summarization, the model embeds sentences and then uses a clustering algorithm to identify key sentences, those closest to the centroids of these clusters, effectively capturing the main ideas of the text.

2. Specify the main execution block.

if \_\_name\_\_ == "\_\_main\_\_":

This Python idiom ensures that the following code block runs only if this script is the main program. It provides flexibility, allowing the script to function both as a standalone program and as an imported module.

3. Create an infinite loop for continuous input.

while True:
      input\_text = input("Enter the text for summarization (type 'exit' to end): ")

      if input\_text.lower() == 'exit':
         print("Exiting...")
         break

An infinite loop continuously prompts you for text input, ensuring interactivity. The loop breaks when you type

, allowing you to control the application flow effectively.

4. Create an instance of Summarizer.

bert\_model = Summarizer()

Here, you create an instance of the Summarizer class named

. This instance is now ready to perform the summarization task using the BERT model, simplifying the complex processes of embedding sentences and clustering into an accessible interface.

5. Generate and print a summary.

summary = bert\_model(input\_text)
print(summary)

Your input text is processed by the bert\_model instance, which then returns a summarized version. This demonstrates the power of Python's high-level libraries in enabling complex operations with minimal code.

requirements.txt

. The sample application already contains the

requirements.txt

file to specify the necessary modules that the application imports. Open

requirements.txt

in a code or text editor to explore its contents.

...

# 04 text\_summarization
bert-extractive-summarizer==0.10.1

...

torch==2.1.2

bert-extractive-summarizer

modules are required for the text summarization application. The summarizer module generates a summary of the input text. This requires PyTorch because the underlying BERT model, which is used for generating the summary, is implemented in PyTorch.

Explore the application environment

https://docs.docker.com/guides/text-summarization/#explore-the-application-environment

You'll use Docker to run the application in a container. Docker lets you containerize the application, providing a consistent and isolated environment for running it. This means the application will operate as intended within its Docker container, regardless of the underlying system differences.

To run the application in a container, a Dockerfile is required. A Dockerfile is a text document that contains all the commands you would call on the command line to assemble an image. An image is a read-only template with instructions for creating a Docker container.

The sample application already contains a

in a code or text editor to explore its contents.

The following steps explain each part of the

. For more details, see the

Dockerfile reference

https://docs.docker.com/reference/dockerfile/

Specify the base image.

FROM python:3.8-slim

This command sets the foundation for the build.

python:3.8-slim

is a lightweight version of the Python 3.8 image, optimized for size and speed. Using this slim image reduces the overall size of your Docker image, leading to quicker downloads and less surface area for security vulnerabilities. This is particularly useful for a Python-based application where you might not need the full standard Python image.

2. Set the working directory.

WORKDIR /app

sets the current working directory within the Docker image. By setting it to

, you ensure that all subsequent commands in the Dockerfile (like

) are executed in this directory. This also helps in organizing your Docker image, as all application-related files are contained in a specific directory.

3. Copy the requirements file into the image.

COPY requirements.txt /app

command transfers the

requirements.txt

file from your local machine into the Docker image. This file lists all Python dependencies required by the application. Copying it into the container lets the next command (

RUN pip install

) to install these dependencies inside the image environment.

4. Install the Python dependencies in the image.

RUN pip install --no-cache-dir -r requirements.txt

This line uses

, Python's package installer, to install the packages listed in

requirements.txt

--no-cache-dir

option disables the cache, which reduces the size of the Docker image by not storing the unnecessary cache data.

5. Run additional commands.

RUN python -m spacy download en\_core\_web\_sm

This step is specific to NLP applications that require the spaCy library. It downloads the

en\_core\_web\_sm

model, which is a small English language model for spaCy. While not needed for this app, it's included for compatibility with other NLP applications that might use this Dockerfile.

6. Copy the application code into the image.

COPY \*.py /app
COPY entrypoint.sh /app

These commands copy your Python scripts and the

entrypoint.sh

script into the image's

directory. This is crucial because the container needs these scripts to run the application. The

entrypoint.sh

script is particularly important as it dictates how the application starts inside the container.

7. Set permissions for the

entrypoint.sh

RUN chmod +x /app/entrypoint.sh

This command modifies the file permissions of

entrypoint.sh

, making it executable. This step is necessary to ensure that the Docker container can run this script to start the application.

8. Set the entry point.

ENTRYPOINT \["/app/entrypoint.sh"\]

instruction configures the container to run

entrypoint.sh

as its default executable. This means that when the container starts, it automatically executes the script. You can explore the

entrypoint.sh

script by opening it in a code or text editor. As the sample contains several applications, the script lets you specify which application to run when the container starts.

Run the application

https://docs.docker.com/guides/text-summarization/#run-the-application

#### To run the application using Docker:

Build the image. In a terminal, run the following command inside the directory of where the

is located.

$ docker build -t basic-nlp .

#### The following is a break down of the command:

docker build

: This is the primary command used to build a Docker image from a Dockerfile and a context. The context is typically a set of files at a specified location, often the directory containing the Dockerfile.

-t basic-nlp

: This is an option for tagging the image. The

flag stands for tag. It assigns a name to the image, which in this case is

. Tags are a convenient way to reference images later, especially when pushing them to a registry or running containers.

: This is the last part of the command and specifies the build context. The period (

) denotes the current directory. Docker will look for a Dockerfile in this directory. The build context (the current directory, in this case) is sent to the Docker daemon to enable the build. It includes all the files and subdirectories in the specified directory. For more details, see the

docker build CLI reference

https://docs.docker.com/reference/cli/docker/buildx/build/

. Docker outputs several logs to your console as it builds the image. You'll see it download and install the dependencies. Depending on your network connection, this may take several minutes. Docker does have a caching feature, so subsequent builds can be faster. The console will return to the prompt when it's complete.

Run the image as a container. In a terminal, run the following command.

$ docker run -it basic-nlp 04\_text\_summarization.py

#### The following is a break down of the command:

: This is the primary command used to run a new container from a Docker image.

: This is a combination of two options:

--interactive

: This keeps the standard input (STDIN) open even if not attached. It lets the container remain running in the foreground and be interactive.

: This allocates a pseudo-TTY, essentially simulating a terminal, like a command prompt or a shell. It's what lets you interact with the application inside the container.

: This specifies the name of the Docker image to use for creating the container. In this case, it's the image named

that you created with the

docker build

04\_text\_summarization.py

: This is the script you want to run inside the Docker container. It gets passed to the

entrypoint.sh

script, which runs it when the container starts. For more details, see the

docker run CLI reference

https://docs.docker.com/reference/cli/docker/container/run/

. Note For Windows users, you may get an error when running the container. Verify that the line endings in the

entrypoint.sh

), then rebuild the image. For more details, see \[Avoid unexpected syntax errors, use Unix style line endings for files in containers\](/desktop/troubleshoot-and-support/troubleshoot/topics/#Unexpected-syntax-errors-use-Unix-style-line endings-for-files-in-containers). You will see the following in your console after the container starts.

#### Enter the text for summarization (type 'exit' to end):

Test the application. Enter some text to get the text summarization.

Enter the text for summarization (type 'exit' to end): Artificial intelligence (AI) is a branch of computer science that aims to create machines capable of intelligent behavior. These machines are designed to mimic human cognitive functions such as learning, problem-solving, and decision-making. AI technologies can be classified into two main types: narrow or weak AI, which is designed for a particular task, and general or strong AI, which possesses the ability to understand, learn, and apply knowledge across various domains. One of the most popular approaches in AI is machine learning, where algorithms are trained on large datasets to recognize patterns and make predictions.

Artificial intelligence (AI) is a branch of computer science that aims to create machines capable of intelligent behavior. These machines are designed to mimic human cognitive functions such as learning, problem-solving, and decision-making.

https://docs.docker.com/guides/text-summarization/#summary

In this guide, you learned how to build and run a text summarization application. You learned how to build the application using Python with Bert Extractive Summarizer, and then set up the environment and run the application using Docker.

#### Related information:

Docker CLI reference

https://docs.docker.com/reference/cli/docker/

Dockerfile reference

https://docs.docker.com/reference/dockerfile/

Bert Extractive Summarizer

https://github.com/dmmiller612/bert-extractive-summarizer

https://pytorch.org/

Python documentation

https://docs.python.org/3/

https://docs.docker.com/guides/text-summarization/#next-steps

Explore more

natural language processing guides

https://docs.docker.com/guides/

Edit this page

https://github.com/docker/docs/edit/main/content/guides/text-summarization.md

Request changes

https://github.com/docker/docs/issues/new?template=doc\_issue.yml&location=https%3a%2f%2fdocs.docker.com%2fguides%2ftext-summarization%2f&labels=status%2Ftriage

Table of contents

https://docs.docker.com/guides/text-summarization/#overview

Prerequisites

https://docs.docker.com/guides/text-summarization/#prerequisites

Get the sample application

https://docs.docker.com/guides/text-summarization/#get-the-sample-application

Explore the application code

https://docs.docker.com/guides/text-summarization/#explore-the-application-code

Explore the application environment

https://docs.docker.com/guides/text-summarization/#explore-the-application-environment

Run the application

https://docs.docker.com/guides/text-summarization/#run-the-application

https://docs.docker.com/guides/text-summarization/#summary

https://docs.docker.com/guides/text-summarization/#next-steps

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

