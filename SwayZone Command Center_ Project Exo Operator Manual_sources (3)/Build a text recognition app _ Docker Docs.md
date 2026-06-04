---
sourceFile: "Build a text recognition app | Docker Docs"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.158Z"
---

# Build a text recognition app | Docker Docs

4830c68a-3911-4933-a4be-674f5cd8e9cd

Build a text recognition app | Docker Docs

da095a3b-3581-4466-ad0d-3c89b265123f

https://docs.docker.com/guides/text-classification/

Build a text recognition app | Docker Docs

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

Build a text recognition app

https://docs.docker.com/guides/text-classification/

This guide details how to containerize text classification models using Docker.

« Back to all guides

https://docs.docker.com/guides/

https://docs.docker.com/

https://docs.docker.com/guides/

/ Text classification

Build a text recognition app

Ask Gordon Copy Markdown View Markdown

Table of contents

https://docs.docker.com/guides/text-classification/#overview

Prerequisites

https://docs.docker.com/guides/text-classification/#prerequisites

Get the sample application

https://docs.docker.com/guides/text-classification/#get-the-sample-application

Explore the application code

https://docs.docker.com/guides/text-classification/#explore-the-application-code

Explore the application environment

https://docs.docker.com/guides/text-classification/#explore-the-application-environment

Run the application

https://docs.docker.com/guides/text-classification/#run-the-application

https://docs.docker.com/guides/text-classification/#summary

https://docs.docker.com/guides/text-classification/#next-steps

https://docs.docker.com/guides/text-classification/#overview

In this guide, you'll learn how to create and run a text recognition application. You'll build the application using Python with scikit-learn and the Natural Language Toolkit (NLTK). Then you'll set up the environment and run the application using Docker.

The application analyzes the sentiment of a user's input text using NLTK's SentimentIntensityAnalyzer. It lets the user input text, which is then processed to determine its sentiment, classifying it as either positive or negative. Also, it displays the accuracy and a detailed classification report of its sentiment analysis model based on a predefined dataset.

Prerequisites

https://docs.docker.com/guides/text-classification/#prerequisites

You have installed the latest version of

Docker Desktop

https://docs.docker.com/get-started/get-docker/

. Docker adds new features regularly and some parts of this guide may work only with the latest version of Docker Desktop.

https://git-scm.com/downloads

. The examples in this section use a command-line based Git client, but you can use any client.

Get the sample application

https://docs.docker.com/guides/text-classification/#get-the-sample-application

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

https://docs.docker.com/guides/text-classification/#explore-the-application-code

The source code for the text classification application is in the

Docker-NLP/03\_text\_classification.py

03\_text\_classification.py

in a text or code editor to explore its contents in the following steps.

Import the required libraries.

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.metrics import accuracy\_score, classification\_report
from sklearn.model\_selection import train\_test\_split
import ssl

: A popular Python library for natural language processing (NLP).

SentimentIntensityAnalyzer

: A component of

for sentiment analysis.

accuracy\_score

classification\_report

: Functions from scikit-learn for evaluating the model.

train\_test\_split

: Function from scikit-learn to split datasets into training and testing sets.

: Used for handling SSL certificate issues which might occur while downloading data for

Handle SSL certificate verification.

try:
    \_create\_unverified\_https\_context = ssl.\_create\_unverified\_context
except AttributeError:
    pass
else:
    ssl.\_create\_default\_https\_context = \_create\_unverified\_https\_context

This block is a workaround for certain environments where downloading data through NLTK might fail due to SSL certificate verification issues. It's telling Python to ignore SSL certificate verification for HTTPS requests.

3. Download NLTK resources.

nltk.download('vader\_lexicon')

vader\_lexicon

is a lexicon used by the

SentimentIntensityAnalyzer

for sentiment analysis.

4. Define text for testing and corresponding labels.

texts = \[...\]
labels = \[0, 1, 2, 0, 1, 2\]

This section defines a small dataset of texts and their corresponding labels (0 for positive, 1 for negative, and 2 for spam).

5. Split the test data.

X\_train, X\_test, y\_train, y\_test = train\_test\_split(texts, labels, test\_size=0.2, random\_state=42)

This part splits the dataset into training and testing sets, with 20% of data as the test set. As this application uses a pre-trained model, it doesn't train the model.

6. Set up sentiment analysis.

sia = SentimentIntensityAnalyzer()

This code initializes the

SentimentIntensityAnalyzer

to analyze the sentiment of text.

7. Generate predictions and classifications for the test data.

vader\_predictions = \[sia.polarity\_scores(text)\["compound"\] for text in X\_test\]
threshold = 0.2
vader\_classifications = \[0 if score > threshold else 1 for score in vader\_predictions\]

This part generates sentiment scores for each text in the test set and classifies them as positive or negative based on a threshold.

8. Evaluate the model.

accuracy = accuracy\_score(y\_test, vader\_classifications)
report\_vader = classification\_report(y\_test, vader\_classifications, zero\_division='warn')

This part calculates the accuracy and classification report for the predictions.

9. Specify the main execution block.

if \_\_name\_\_ == "\_\_main\_\_":

This Python idiom ensures that the following code block runs only if this script is the main program. It provides flexibility, allowing the script to function both as a standalone program and as an imported module.

10. Create an infinite loop for continuous input.

while True:
    input\_text = input("Enter the text for classification (type 'exit' to end): ")

      if input\_text.lower() == 'exit':
         print("Exiting...")
         break

This while loop runs indefinitely until it's explicitly broken. It lets the user continuously enter text for entity recognition until they decide to exit.

11. Analyze the text.

input\_text\_score = sia.polarity\_scores(input\_text)\["compound"\]
        input\_text\_classification = 0 if input\_text\_score > threshold else 1

Print the VADER Classification Report and the sentiment analysis.

print(f"Accuracy: {accuracy:.2f}")
        print("\nVADER Classification Report:")
        print(report\_vader)

        print(f"\nTest Text (Positive): '{input\_text}'")
        print(f"Predicted Sentiment: {'Positive' if input\_text\_classification == 0 else 'Negative'}")

requirements.txt

. The sample application already contains the

requirements.txt

file to specify the necessary packages that the application imports. Open

requirements.txt

in a code or text editor to explore its contents.

# 01 sentiment\_analysis
nltk==3.6.5

...

# 03 text\_classification
scikit-learn==1.3.2

...

scikit-learn

modules are required for the text classification application.

Explore the application environment

https://docs.docker.com/guides/text-classification/#explore-the-application-environment

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

) install these dependencies inside the image environment.

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

https://docs.docker.com/guides/text-classification/#run-the-application

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

$ docker run -it basic-nlp 03\_text\_classification.py

#### The following is a break down of the command:

: This is the primary command used to run a new container from a Docker image.

: This is a combination of two options:

--interactive

: This keeps the standard input (STDIN) open even if not attached. It lets the container remain running in the foreground and be interactive.

: This allocates a pseudo-TTY, essentially simulating a terminal, like a command prompt or a shell. It's what lets you interact with the application inside the container.

: This specifies the name of the Docker image to use for creating the container. In this case, it's the image named

that you created with the

docker build

03\_text\_classification.py

: This is the script you want to run inside the Docker container. It gets passed to the

entrypoint.sh

script, which runs it when the container starts. For more details, see the

docker run CLI reference

https://docs.docker.com/reference/cli/docker/container/run/

. Note For Windows users, you may get an error when running the container. Verify that the line endings in the

entrypoint.sh

), then rebuild the image. For more details, see \[Avoid unexpected syntax errors, use Unix style line endings for files in containers\](/desktop/troubleshoot-and-support/troubleshoot/topics/#Unexpected-syntax-errors-use-Unix-style-line endings-for-files-in-containers). You will see the following in your console after the container starts.

#### Enter the text for classification (type 'exit' to end):

Test the application. Enter some text to get the text classification.

Enter the text for classification (type 'exit' to end): I love containers!
Accuracy: 1.00

VADER Classification Report:
              precision    recall  f1-score   support

           0       1.00      1.00      1.00         1
           1       1.00      1.00      1.00         1

    accuracy                           1.00         2
   macro avg       1.00      1.00      1.00         2
weighted avg       1.00      1.00      1.00         2

Test Text (Positive): 'I love containers!'
Predicted Sentiment: Positive

https://docs.docker.com/guides/text-classification/#summary

In this guide, you learned how to build and run a text classification application. You learned how to build the application using Python with scikit-learn and NLTK. Then you learned how to set up the environment and run the application using Docker.

#### Related information:

Docker CLI reference

https://docs.docker.com/reference/cli/docker/

Dockerfile reference

https://docs.docker.com/reference/dockerfile/

Natural Language Toolkit

https://www.nltk.org/

Python documentation

https://docs.python.org/3/

scikit-learn

https://scikit-learn.org/

https://docs.docker.com/guides/text-classification/#next-steps

Explore more

natural language processing guides

https://docs.docker.com/guides/

Edit this page

https://github.com/docker/docs/edit/main/content/guides/text-classification.md

Request changes

https://github.com/docker/docs/issues/new?template=doc\_issue.yml&location=https%3a%2f%2fdocs.docker.com%2fguides%2ftext-classification%2f&labels=status%2Ftriage

Table of contents

https://docs.docker.com/guides/text-classification/#overview

Prerequisites

https://docs.docker.com/guides/text-classification/#prerequisites

Get the sample application

https://docs.docker.com/guides/text-classification/#get-the-sample-application

Explore the application code

https://docs.docker.com/guides/text-classification/#explore-the-application-code

Explore the application environment

https://docs.docker.com/guides/text-classification/#explore-the-application-environment

Run the application

https://docs.docker.com/guides/text-classification/#run-the-application

https://docs.docker.com/guides/text-classification/#summary

https://docs.docker.com/guides/text-classification/#next-steps

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

