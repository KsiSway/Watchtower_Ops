---
sourceFile: "Containerize a Django application | Docker Docs"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.193Z"
---

# Containerize a Django application | Docker Docs

d4119221-5042-4890-b828-90faefaf2d50

Containerize a Django application | Docker Docs

2807af18-6f9e-44c3-9670-b6e94528e3ff

https://docs.docker.com/guides/django/

Containerize a Django application | Docker Docs

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

Containerize a Django application

https://docs.docker.com/guides/django/

This guide shows how to containerize a Django application using Docker. You'll scaffold the project with uv, create a production-ready Dockerfile using a Docker Hardened Image, then add a development stage and Compose Watch for fast iteration.

Python Docker Hardened Images

« Back to all guides

https://docs.docker.com/guides/

https://docs.docker.com/

https://docs.docker.com/guides/

Containerize a Django application

Ask Gordon Copy Markdown View Markdown

Table of contents

Prerequisites

https://docs.docker.com/guides/django/#prerequisites

https://docs.docker.com/guides/django/#overview

Create the Django project

https://docs.docker.com/guides/django/#create-the-django-project

Create a production Dockerfile

https://docs.docker.com/guides/django/#create-a-production-dockerfile

Run the application

https://docs.docker.com/guides/django/#run-the-application

Set up a development environment

https://docs.docker.com/guides/django/#set-up-a-development-environment

Update the Dockerfile

https://docs.docker.com/guides/django/#update-the-dockerfile

Update the Compose file

https://docs.docker.com/guides/django/#update-the-compose-file

Add the PostgreSQL driver

https://docs.docker.com/guides/django/#add-the-postgresql-driver

Run with Compose Watch

https://docs.docker.com/guides/django/#run-with-compose-watch

https://docs.docker.com/guides/django/#summary

Prerequisites

https://docs.docker.com/guides/django/#prerequisites

You have installed the latest version of

Docker Desktop

https://docs.docker.com/get-started/get-docker/

https://docs.astral.sh/uv/

installed, or you can use Docker to scaffold the project without a local Python or uv installation.

If you're new to Docker, start with the

Docker basics

https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/

guide to get familiar with key concepts like images, containers, and Dockerfiles.

https://docs.docker.com/guides/django/#overview

This guide walks you through containerizing a Django application with Docker. By the end, you will:

Initialize a Django project using uv, either locally or inside a Docker Hardened Image container.

Create a production-ready Dockerfile using

Docker Hardened Images (DHI)

https://docs.docker.com/dhi/

development

stage to your Dockerfile and configure Compose Watch for automatic code syncing.

Create the Django project

https://docs.docker.com/guides/django/#create-the-django-project

You can bootstrap the project with a local uv installation, or entirely inside a container using the same DHI image the Dockerfile uses, with no local Python required.

Local (uv) Container (DHI)

#### Initialize the project pinned to Python 3.14, then navigate into it:

$ uv init --python 3.14 django-docker
$ cd django-docker

#### Add Django and Gunicorn, then scaffold the Django project:

$ uv add django gunicorn
$ uv run django-admin startproject myapp .

The DHI dev image already has Python 3.14, so the bootstrapped project will match the Dockerfile exactly.

#### Create the project directory and navigate into it:

$ mkdir django-docker && cd django-docker

Initialize the project, add dependencies, and scaffold. All in one container run:

$ docker run --rm -v $PWD:$PWD -w $PWD \
  -e UV\_LINK\_MODE=copy \
  dhi.io/python:3.14-alpine3.23-dev \
  sh -c "pip install --quiet --root-user-action=ignore uv && uv init --name django-docker --python 3.14 . && uv add django gunicorn && uv run django-admin startproject myapp ."

Note The previous command uses Mac/Linux shell syntax. On Windows, adjust the path: PowerShell uses

, Command Prompt uses

, Git Bash requires

MSYS\_NO\_PATHCONV=1

#### Your directory should now contain the following files:

├── .python-version
├── main.py
├── manage.py
├── myapp/
│ ├── \_\_init\_\_.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── pyproject.toml
├── uv.lock
└── README.md

Create a production Dockerfile

https://docs.docker.com/guides/django/#create-a-production-dockerfile

Docker Hardened Images are production-ready base images maintained by Docker that minimize attack surface. For more details, see

Docker Hardened Images

https://docs.docker.com/dhi/

#### Sign in to the DHI registry:

$ docker login dhi.io

.dockerignore

file to exclude local artifacts from the build context: .dockerignore

.venv/
\_\_pycache\_\_/
\*.pyc
.git/

with the following contents: Dockerfile

# syntax=docker/dockerfile:1

# Build stage: the -dev image includes tools needed to install packages.
FROM dhi.io/python:3.14-alpine3.23-dev AS builder

# Prevent Python from writing .pyc files to disk.
ENV PYTHONDONTWRITEBYTECODE=1
# Prevent Python from buffering stdout/stderr so logs appear immediately.
ENV PYTHONUNBUFFERED=1

RUN pip install --quiet --root-user-action=ignore uv
# Use copy mode since the cache and build filesystem are on different volumes.
ENV UV\_LINK\_MODE=copy

WORKDIR /app

# Install dependencies into a virtual environment using cache and bind mounts
# so neither uv nor the lock files need to be copied into the image.
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project

# Runtime stage: minimal DHI image with no shell or package manager,
# already runs as the nonroot user.
FROM dhi.io/python:3.14-alpine3.23

# Prevent Python from buffering stdout/stderr so logs appear immediately.
ENV PYTHONUNBUFFERED=1
# Activate the virtual environment copied from the build stage.
ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /app

# Copy the pre-built virtual environment and application source code.
COPY --from=builder /app/.venv /app/.venv
COPY . .

EXPOSE 8000

# Run Gunicorn as the production WSGI server.
CMD \["gunicorn", "myapp.wsgi:application", "--bind", "0.0.0.0:8000"\]

compose.yaml

file: compose.yaml

services:
  web:
    build: .
    ports:
      - "8000:8000"

Run the application

https://docs.docker.com/guides/django/#run-the-application

django-docker

directory, run:

$ docker compose up --build

Open a browser and navigate to

http://localhost:8000

http://localhost:8000/

. You should see the Django welcome page.

to stop the application.

Set up a development environment

https://docs.docker.com/guides/django/#set-up-a-development-environment

The production setup uses Gunicorn and requires a full image rebuild to pick up code changes. For development, you can add a

development

stage to your Dockerfile that uses Django's built-in server, and configure Compose Watch to automatically sync code changes into the running container without a rebuild.

Update the Dockerfile

https://docs.docker.com/guides/django/#update-the-dockerfile

Replace your

with a multi-stage version that adds a

development

stage alongside

# syntax=docker/dockerfile:1

# Build stage: the -dev image includes tools needed to install packages.
FROM dhi.io/python:3.14-alpine3.23-dev AS builder

# Prevent Python from writing .pyc files to disk.
ENV PYTHONDONTWRITEBYTECODE=1
# Prevent Python from buffering stdout/stderr so logs appear immediately.
ENV PYTHONUNBUFFERED=1

RUN pip install --quiet --root-user-action=ignore uv
# Use copy mode since the cache and build filesystem are on different volumes.
ENV UV\_LINK\_MODE=copy

WORKDIR /app

# Install dependencies into a virtual environment using cache and bind mounts
# so neither uv nor the lock files need to be copied into the image.
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project

# The development stage inherits the -dev image and virtual environment from
# the builder. Django's built-in server reloads when Compose Watch syncs files.
FROM builder AS development

ENV PATH="/app/.venv/bin:$PATH"

COPY . .
EXPOSE 8000
CMD \["python", "manage.py", "runserver", "0.0.0.0:8000"\]

# The production stage uses the minimal runtime image, which has no shell,
# no package manager, and already runs as the nonroot user.
FROM dhi.io/python:3.14-alpine3.23 AS production

# Prevent Python from buffering stdout/stderr so logs appear immediately.
ENV PYTHONUNBUFFERED=1
# Activate the virtual environment copied from the build stage.
ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /app

# Copy only the pre-built virtual environment and application source code.
COPY --from=builder /app/.venv /app/.venv
COPY . .

EXPOSE 8000

# Run Gunicorn as the production WSGI server.
CMD \["gunicorn", "myapp.wsgi:application", "--bind", "0.0.0.0:8000"\]

Update the Compose file

https://docs.docker.com/guides/django/#update-the-compose-file

Replace your

compose.yaml

with the following. It targets the

development

stage, adds a PostgreSQL database, and configures Compose Watch:

compose.yaml

services:
  web:
    build:
      context: .
      # Build the development stage from the multi-stage Dockerfile.
      target: development
    ports:
      - "8000:8000"
    environment:
      # Enable Django's verbose debug error pages (the dev server always auto-reloads).
      - DEBUG=1
      # Database connection settings passed to Django via environment variables.
      - POSTGRES\_DB=myapp
      - POSTGRES\_USER=postgres
      - POSTGRES\_PASSWORD=password
      - POSTGRES\_HOST=db
      - POSTGRES\_PORT=5432
    # Wait for the database to pass its healthcheck before starting the web service.
    depends\_on:
      db:
        condition: service\_healthy
    develop:
      watch:
        # Sync source file changes directly into the container so Django's
        # dev server can reload them without a full image rebuild.
        - action: sync
          path: .
          target: /app
          ignore:
            - \_\_pycache\_\_/
            - "\*.pyc"
            - .git/
            - .venv/
        # Rebuild the image when dependencies change.
        - action: rebuild
          path: pyproject.toml
        - action: rebuild
          path: uv.lock
  db:
    image: dhi.io/postgres:18
    restart: always
    volumes:
      # Persist database data across container restarts.
      - db-data:/var/lib/postgresql
    environment:
      - POSTGRES\_DB=myapp
      - POSTGRES\_USER=postgres
      - POSTGRES\_PASSWORD=password
    # Expose the port only to other services on the Compose network,
    # not to the host machine.
    expose:
      - 5432
    # Only report healthy once PostgreSQL is ready to accept connections,
    # so the web service doesn't start before the database is available.
    healthcheck:
      test: \["CMD", "pg\_isready"\]
      interval: 10s
      timeout: 5s
      retries: 5
volumes:
  db-data:

action pushes file changes directly into the running container so Django's dev server reloads them automatically. A change to

pyproject.toml

triggers a full image rebuild instead.

To learn more about Compose Watch, see

Use Compose Watch

https://docs.docker.com/compose/how-tos/file-watch/

Add the PostgreSQL driver

https://docs.docker.com/guides/django/#add-the-postgresql-driver

adapter to your project:

Local (uv) Container (DHI)

$ uv add 'psycopg\[binary\]'

$ docker run --rm -v $PWD:$PWD -w $PWD \
  -e UV\_LINK\_MODE=copy \
  dhi.io/python:3.14-alpine3.23-dev \
  sh -c "pip install --quiet --root-user-action=ignore uv && uv add 'psycopg\[binary\]'"

Then update

myapp/settings.py

from environment variables:

myapp/settings.py

import os

DEBUG = os.environ.get('DEBUG', '0') == '1'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES\_DB", "myapp"),
        "USER": os.environ.get("POSTGRES\_USER", "postgres"),
        "PASSWORD": os.environ.get("POSTGRES\_PASSWORD", "password"),
        "HOST": os.environ.get("POSTGRES\_HOST", "localhost"),
        "PORT": os.environ.get("POSTGRES\_PORT", "5432"),
    }
}

Run with Compose Watch

https://docs.docker.com/guides/django/#run-with-compose-watch

#### Start the development stack:

$ docker compose watch

Open a browser and navigate to

http://localhost:8000

http://localhost:8000/

Try editing a file, for example add a view to

myapp/views.py

. Compose Watch syncs the change into the container and Django's dev server reloads automatically. If you update

pyproject.toml

, Compose Watch triggers a full image rebuild.

https://docs.docker.com/guides/django/#summary

#### In this guide, you:

Bootstrapped a Django project using uv, with options for both local and containerized setup.

Created a production-ready Dockerfile using Docker Hardened Images and uv for dependency management.

development

stage to the

and configured Compose Watch for fast iterative development with a PostgreSQL database.

#### Related information:

Dockerfile reference

https://docs.docker.com/reference/dockerfile/

Compose file reference

https://docs.docker.com/reference/compose-file/

Use Compose Watch

https://docs.docker.com/compose/how-tos/file-watch/

Docker Hardened Images

https://docs.docker.com/dhi/

Multi-stage builds

https://docs.docker.com/build/building/multi-stage/

uv documentation

https://docs.astral.sh/uv/

Edit this page

https://github.com/docker/docs/edit/main/content/guides/django.md

Request changes

https://github.com/docker/docs/issues/new?template=doc\_issue.yml&location=https%3a%2f%2fdocs.docker.com%2fguides%2fdjango%2f&labels=status%2Ftriage

Table of contents

Prerequisites

https://docs.docker.com/guides/django/#prerequisites

https://docs.docker.com/guides/django/#overview

Create the Django project

https://docs.docker.com/guides/django/#create-the-django-project

Create a production Dockerfile

https://docs.docker.com/guides/django/#create-a-production-dockerfile

Run the application

https://docs.docker.com/guides/django/#run-the-application

Set up a development environment

https://docs.docker.com/guides/django/#set-up-a-development-environment

Update the Dockerfile

https://docs.docker.com/guides/django/#update-the-dockerfile

Update the Compose file

https://docs.docker.com/guides/django/#update-the-compose-file

Add the PostgreSQL driver

https://docs.docker.com/guides/django/#add-the-postgresql-driver

Run with Compose Watch

https://docs.docker.com/guides/django/#run-with-compose-watch

https://docs.docker.com/guides/django/#summary

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

