---
sourceFile: "What is Docker? | Docker Docs"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.886Z"
---

# What is Docker? | Docker Docs

8c68d459-c233-4c0d-8885-a97444049980

What is Docker? | Docker Docs

83f4adfe-6689-4b76-9440-cd49e6d50a8d

https://docs.docker.com/get-started/docker-overview/

What is Docker? | Docker Docs

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

Get started

https://docs.docker.com/get-started/

https://docs.docker.com/guides/

https://docs.docker.com/manuals/

https://docs.docker.com/reference/

https://docs.docker.com/get-started/get-docker/

What is Docker?

https://docs.docker.com/get-started/docker-overview/

Introduction

https://docs.docker.com/get-started/introduction/

Get Docker Desktop

https://docs.docker.com/get-started/introduction/get-docker-desktop/

Develop with containers

https://docs.docker.com/get-started/introduction/develop-with-containers/

Build and push your first image

https://docs.docker.com/get-started/introduction/build-and-push-first-image/

What's next

https://docs.docker.com/get-started/introduction/whats-next/

Docker concepts

What is a container?

https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/

What is an image?

https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-an-image/

What is a registry?

https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-registry/

What is Docker Compose?

https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-docker-compose/

Building images

https://docs.docker.com/get-started/docker-concepts/building-images/

Understanding the image layers

https://docs.docker.com/get-started/docker-concepts/building-images/understanding-image-layers/

Writing a Dockerfile

https://docs.docker.com/get-started/docker-concepts/building-images/writing-a-dockerfile/

Build, tag, and publish an image

https://docs.docker.com/get-started/docker-concepts/building-images/build-tag-and-publish-an-image/

Using the build cache

https://docs.docker.com/get-started/docker-concepts/building-images/using-the-build-cache/

Multi-stage builds

https://docs.docker.com/get-started/docker-concepts/building-images/multi-stage-builds/

Running containers

Publishing and exposing ports

https://docs.docker.com/get-started/docker-concepts/running-containers/publishing-ports/

Overriding container defaults

https://docs.docker.com/get-started/docker-concepts/running-containers/overriding-container-defaults/

Persisting container data

https://docs.docker.com/get-started/docker-concepts/running-containers/persisting-container-data/

Sharing local files with containers

https://docs.docker.com/get-started/docker-concepts/running-containers/sharing-local-files/

Multi-container applications

https://docs.docker.com/get-started/docker-concepts/running-containers/multi-container-applications/

Docker workshop

https://docs.docker.com/get-started/workshop/

Part 1: Containerize an application

https://docs.docker.com/get-started/workshop/02\_our\_app/

Part 2: Update the application

https://docs.docker.com/get-started/workshop/03\_updating\_app/

Part 3: Share the application

https://docs.docker.com/get-started/workshop/04\_sharing\_app/

Part 4: Persist the DB

https://docs.docker.com/get-started/workshop/05\_persisting\_data/

Part 5: Use bind mounts

https://docs.docker.com/get-started/workshop/06\_bind\_mounts/

Part 6: Multi-container apps

https://docs.docker.com/get-started/workshop/07\_multi\_container/

Part 7: Use Docker Compose

https://docs.docker.com/get-started/workshop/08\_using\_compose/

Part 8: Image-building best practices

https://docs.docker.com/get-started/workshop/09\_image\_best/

Part 9: What next

https://docs.docker.com/get-started/workshop/10\_what\_next/

Educational resources

https://docs.docker.com/get-started/resources/

https://docs.docker.com/

Get started

https://docs.docker.com/get-started/

/ What is Docker?

What is Docker?

Ask Gordon Copy Markdown View Markdown

Table of contents

The Docker platform

https://docs.docker.com/get-started/docker-overview/#the-docker-platform

What can I use Docker for?

https://docs.docker.com/get-started/docker-overview/#what-can-i-use-docker-for

Fast, consistent delivery of your applications

https://docs.docker.com/get-started/docker-overview/#fast-consistent-delivery-of-your-applications

Responsive deployment and scaling

https://docs.docker.com/get-started/docker-overview/#responsive-deployment-and-scaling

Running more workloads on the same hardware

https://docs.docker.com/get-started/docker-overview/#running-more-workloads-on-the-same-hardware

Docker architecture

https://docs.docker.com/get-started/docker-overview/#docker-architecture

The Docker daemon

https://docs.docker.com/get-started/docker-overview/#the-docker-daemon

The Docker client

https://docs.docker.com/get-started/docker-overview/#the-docker-client

Docker Desktop

https://docs.docker.com/get-started/docker-overview/#docker-desktop

Docker registries

https://docs.docker.com/get-started/docker-overview/#docker-registries

Docker objects

https://docs.docker.com/get-started/docker-overview/#docker-objects

The underlying technology

https://docs.docker.com/get-started/docker-overview/#the-underlying-technology

https://docs.docker.com/get-started/docker-overview/#next-steps

Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly. With Docker, you can manage your infrastructure in the same ways you manage your applications. By taking advantage of Docker's methodologies for shipping, testing, and deploying code, you can significantly reduce the delay between writing code and running it in production.

The Docker platform

https://docs.docker.com/get-started/docker-overview/#the-docker-platform

Docker provides the ability to package and run an application in a loosely isolated environment called a container. The isolation and security let you run many containers simultaneously on a given host. Containers are lightweight and contain everything needed to run the application, so you don't need to rely on what's installed on the host. You can share containers while you work, and be sure that everyone you share with gets the same container that works in the same way.

Docker provides tooling and a platform to manage the lifecycle of your containers:

Develop your application and its supporting components using containers.

The container becomes the unit for distributing and testing your application.

When you're ready, deploy your application into your production environment, as a container or an orchestrated service. This works the same whether your production environment is a local data center, a cloud provider, or a hybrid of the two.

What can I use Docker for?

https://docs.docker.com/get-started/docker-overview/#what-can-i-use-docker-for

Fast, consistent delivery of your applications

https://docs.docker.com/get-started/docker-overview/#fast-consistent-delivery-of-your-applications

Docker streamlines the development lifecycle by allowing developers to work in standardized environments using local containers which provide your applications and services. Containers are great for continuous integration and continuous delivery (CI/CD) workflows.

#### Consider the following example scenario:

Your developers write code locally and share their work with their colleagues using Docker containers.

They use Docker to push their applications into a test environment and run automated and manual tests.

When developers find bugs, they can fix them in the development environment and redeploy them to the test environment for testing and validation.

When testing is complete, getting the fix to the customer is as simple as pushing the updated image to the production environment.

Responsive deployment and scaling

https://docs.docker.com/get-started/docker-overview/#responsive-deployment-and-scaling

Docker's container-based platform allows for highly portable workloads. Docker containers can run on a developer's local laptop, on physical or virtual machines in a data center, on cloud providers, or in a mixture of environments.

Docker's portability and lightweight nature also make it easy to dynamically manage workloads, scaling up or tearing down applications and services as business needs dictate, in near real time.

Running more workloads on the same hardware

https://docs.docker.com/get-started/docker-overview/#running-more-workloads-on-the-same-hardware

Docker is lightweight and fast. It provides a viable, cost-effective alternative to hypervisor-based virtual machines, so you can use more of your server capacity to achieve your business goals. Docker is perfect for high density environments and for small and medium deployments where you need to do more with fewer resources.

Docker architecture

https://docs.docker.com/get-started/docker-overview/#docker-architecture

Docker uses a client-server architecture. The Docker client talks to the Docker daemon, which does the heavy lifting of building, running, and distributing your Docker containers. The Docker client and daemon can run on the same system, or you can connect a Docker client to a remote Docker daemon. The Docker client and daemon communicate using a REST API, over UNIX sockets or a network interface. Another Docker client is Docker Compose, that lets you work with applications consisting of a set of containers.

The Docker daemon

https://docs.docker.com/get-started/docker-overview/#the-docker-daemon

The Docker daemon (

) listens for Docker API requests and manages Docker objects such as images, containers, networks, and volumes. A daemon can also communicate with other daemons to manage Docker services.

The Docker client

https://docs.docker.com/get-started/docker-overview/#the-docker-client

The Docker client (

) is the primary way that many Docker users interact with Docker. When you use commands such as

, the client sends these commands to

, which carries them out. The

command uses the Docker API. The Docker client can communicate with more than one daemon.

Docker Desktop

https://docs.docker.com/get-started/docker-overview/#docker-desktop

Docker Desktop is an easy-to-install application for your Mac, Windows, or Linux environment that enables you to build and share containerized applications and microservices. Docker Desktop includes the Docker daemon (

), the Docker client (

), Docker Compose, Docker Content Trust, Kubernetes, and Credential Helper. For more information, see

Docker Desktop

https://docs.docker.com/desktop/

Docker registries

https://docs.docker.com/get-started/docker-overview/#docker-registries

A Docker registry stores Docker images. Docker Hub is a public registry that anyone can use, and Docker looks for images on Docker Hub by default. You can even run your own private registry.

When you use the

docker pull

commands, Docker pulls the required images from your configured registry. When you use the

docker push

command, Docker pushes your image to your configured registry.

Docker objects

https://docs.docker.com/get-started/docker-overview/#docker-objects

When you use Docker, you are creating and using images, containers, networks, volumes, plugins, and other objects. This section is a brief overview of some of those objects.

https://docs.docker.com/get-started/docker-overview/#images

An image is a read-only template with instructions for creating a Docker container. Often, an image is based on another image, with some additional customization. For example, you may build an image that is based on the Ubuntu image but includes the Apache web server and your application, as well as the configuration details needed to make your application run.

You might create your own images or you might only use those created by others and published in a registry. To build your own image, you create a Dockerfile with a simple syntax for defining the steps needed to create the image and run it. Each instruction in a Dockerfile creates a layer in the image. When you change the Dockerfile and rebuild the image, only those layers which have changed are rebuilt. This is part of what makes images so lightweight, small, and fast, when compared to other virtualization technologies.

https://docs.docker.com/get-started/docker-overview/#containers

A container is a runnable instance of an image. You can create, start, stop, move, or delete a container using the Docker API or CLI. You can connect a container to one or more networks, attach storage to it, or even create a new image based on its current state.

By default, a container is relatively well isolated from other containers and its host machine. You can control how isolated a container's network, storage, or other underlying subsystems are from other containers or from the host machine.

A container is defined by its image as well as any configuration options you provide to it when you create or start it. When a container is removed, any changes to its state that aren't stored in persistent storage disappear.

Example docker run command

https://docs.docker.com/get-started/docker-overview/#example-docker-run-command

The following command runs an

container, attaches interactively to your local command-line session, and runs

$ docker run -i -t ubuntu /bin/bash

When you run this command, the following happens (assuming you are using the default registry configuration):

If you don't have the

image locally, Docker pulls it from your configured registry, as though you had run

docker pull ubuntu

Docker creates a new container, as though you had run a

docker container create

command manually.

Docker allocates a read-write filesystem to the container, as its final layer. This allows a running container to create or modify files and directories in its local filesystem.

Docker creates a network interface to connect the container to the default network, since you didn't specify any networking options. This includes assigning an IP address to the container. By default, containers can connect to external networks using the host machine's network connection.

Docker starts the container and executes

. Because the container is running interactively and attached to your terminal (due to the

flags), you can provide input using your keyboard while Docker logs the output to your terminal.

When you run

to terminate the

command, the container stops but isn't removed. You can start it again or remove it.

The underlying technology

https://docs.docker.com/get-started/docker-overview/#the-underlying-technology

Docker is written in the

Go programming language

https://golang.org/

and takes advantage of several features of the Linux kernel to deliver its functionality. Docker uses a technology called

to provide the isolated workspace called the container. When you run a container, Docker creates a set of namespaces for that container.

These namespaces provide a layer of isolation. Each aspect of a container runs in a separate namespace and its access is limited to that namespace.

https://docs.docker.com/get-started/docker-overview/#next-steps

Install Docker

https://docs.docker.com/get-started/get-docker/

Get started with Docker

https://docs.docker.com/get-started/introduction/

Edit this page

https://github.com/docker/docs/edit/main/content/get-started/docker-overview.md

Request changes

https://github.com/docker/docs/issues/new?template=doc\_issue.yml&location=https%3a%2f%2fdocs.docker.com%2fget-started%2fdocker-overview%2f&labels=status%2Ftriage

Table of contents

The Docker platform

https://docs.docker.com/get-started/docker-overview/#the-docker-platform

What can I use Docker for?

https://docs.docker.com/get-started/docker-overview/#what-can-i-use-docker-for

Fast, consistent delivery of your applications

https://docs.docker.com/get-started/docker-overview/#fast-consistent-delivery-of-your-applications

Responsive deployment and scaling

https://docs.docker.com/get-started/docker-overview/#responsive-deployment-and-scaling

Running more workloads on the same hardware

https://docs.docker.com/get-started/docker-overview/#running-more-workloads-on-the-same-hardware

Docker architecture

https://docs.docker.com/get-started/docker-overview/#docker-architecture

The Docker daemon

https://docs.docker.com/get-started/docker-overview/#the-docker-daemon

The Docker client

https://docs.docker.com/get-started/docker-overview/#the-docker-client

Docker Desktop

https://docs.docker.com/get-started/docker-overview/#docker-desktop

Docker registries

https://docs.docker.com/get-started/docker-overview/#docker-registries

Docker objects

https://docs.docker.com/get-started/docker-overview/#docker-objects

The underlying technology

https://docs.docker.com/get-started/docker-overview/#the-underlying-technology

https://docs.docker.com/get-started/docker-overview/#next-steps

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

