---
sourceFile: "Spring AI"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.719Z"
---

# Spring AI

311be6d0-8f0d-42f8-b4bd-1a9e57fd4ad0

58a87308-aad8-474a-8214-d1914f876714

https://spring.io/projects/spring-ai

Skip to main content

https://spring.io/projects/spring-ai#main

https://spring.io/

https://spring.io/why-spring

Generative AI

https://spring.io/ai

https://spring.io/cloud

Architecture Patterns

Microservices

https://spring.io/microservices

https://spring.io/reactive

Event Driven

https://spring.io/event-driven

Application Types

Web Applications

https://spring.io/web-applications

https://spring.io/serverless

https://spring.io/batch

Getting Started

https://spring.io/quickstart

https://spring.io/guides

https://spring.academy/courses

Get Certified

https://spring.academy/learning-path

https://spring.io/projects

Spring Boot

https://spring.io/projects/spring-boot

Spring Framework

https://spring.io/projects/spring-framework

Spring Cloud

https://spring.io/projects/spring-cloud

https://spring.io/projects/spring-ai

Spring Data

https://spring.io/projects/spring-data

Spring Integration

https://spring.io/projects/spring-integration

Spring Batch

https://spring.io/projects/spring-batch

Spring Security

https://spring.io/projects/spring-security

Foundational Projects

https://micrometer.io/

https://projectreactor.io/

Development Tools

Spring Tools

https://spring.io/tools

Spring Initializr

https://start.spring.io/

https://spring.io/blog

Release Calendar

https://spring.io/projects#release-calendar

Version Mappings

https://spring.io/projects/generations

Release Highlights

https://spring.io/projects/release-highlights

Security Advisories

https://spring.io/security

GitHub Orgs

Spring Projects

https://github.com/spring-projects

Spring Cloud

https://github.com/spring-cloud

https://spring.io/community

https://spring.io/events

https://spring.io/authors

https://enterprise.spring.io/

Long-term Support

https://enterprise.spring.io/lts-releases

Automated Upgrades

https://enterprise.spring.io/spring-application-advisor

Governance and Compliance

https://enterprise.spring.io/enterprise-extensions

Modern App Development

https://enterprise.spring.io/enterprise-components

https://spring.io/

All projects

https://spring.io/projects

Spring Boot

https://spring.io/projects/spring-boot

Spring Framework

https://spring.io/projects/spring-framework

Spring Data

https://spring.io/projects/spring-data

Spring Cloud

https://spring.io/projects/spring-cloud

Spring Cloud Data Flow

https://spring.io/projects/spring-cloud-dataflow

Spring gRPC

https://spring.io/projects/spring-grpc

Spring Security

https://spring.io/projects/spring-security

Spring Authorization Server

https://spring.io/projects/spring-authorization-server

Spring for GraphQL

https://spring.io/projects/spring-graphql

Spring Session

https://spring.io/projects/spring-session

Spring Integration

https://spring.io/projects/spring-integration

Spring HATEOAS

https://spring.io/projects/spring-hateoas

Spring Modulith

https://spring.io/projects/spring-modulith

Spring REST Docs

https://spring.io/projects/spring-restdocs

https://spring.io/projects/spring-ai

Spring Batch

https://spring.io/projects/spring-batch

Spring AMQP

https://spring.io/projects/spring-amqp

Spring CredHub

https://spring.io/projects/spring-credhub

Spring for Apache Kafka

https://spring.io/projects/spring-kafka

Spring LDAP

https://spring.io/projects/spring-ldap

Spring for Apache Pulsar

https://spring.io/projects/spring-pulsar

Spring Shell

https://spring.io/projects/spring-shell

Spring Statemachine

https://spring.io/projects/spring-statemachine

Spring Vault

https://spring.io/projects/spring-vault

Spring Web Flow

https://spring.io/projects/spring-webflow

Spring Web Services

https://spring.io/projects/spring-ws

Spring AI 1.1.6

https://github.com/spring-projects/spring-ai

https://spring.io/projects/spring-ai#overview

https://spring.io/projects/spring-ai#learn

https://spring.io/projects/spring-ai#support

Spring AI is an application framework for AI engineering. Its goal is to apply to the AI domain Spring ecosystem design principles such as portability and modular design and promote using POJOs as the building blocks of an application to the AI domain.

At its core, Spring AI addresses the fundamental challenge of AI integration: Connecting your enterprise

#### Spring AI provides the following features:

Support for all major

AI Model providers

https://docs.spring.io/spring-ai/reference/api/index.html

such as Anthropic, OpenAI, Microsoft, Amazon, Google, and Ollama. Supported model types include:

Chat Completion

https://docs.spring.io/spring-ai/reference/api/chatmodel.html

https://docs.spring.io/spring-ai/reference/api/embeddings.html

Text to Image

https://docs.spring.io/spring-ai/reference/api/imageclient.html

Audio Transcription

https://docs.spring.io/spring-ai/reference/api/audio/transcriptions.html

Text to Speech

https://docs.spring.io/spring-ai/reference/api/audio/speech.html

https://docs.spring.io/spring-ai/reference/api/index.html#api/moderation

Portable API support across AI providers for both synchronous and streaming API options are supported. Access to

model-specific features

https://docs.spring.io/spring-ai/reference/api/chatmodel.html#\_chat\_options

is also available.

Structured Outputs

https://docs.spring.io/spring-ai/reference/api/structured-output-converter.html

- Mapping of AI Model output to POJOs.

Support for all major

Vector Database providers

https://docs.spring.io/spring-ai/reference/api/vectordbs.html

Apache Cassandra, Azure Vector Search, Chroma, Milvus, MongoDB Atlas, Neo4j, Oracle, PostgreSQL/PGVector, PineCone, Qdrant, Redis, and Weaviate

Portable API across Vector Store providers, including a novel SQL-like

metadata filter API

https://docs.spring.io/spring-ai/reference/api/vectordbs.html#metadata-filters

Tools/Function Calling

https://docs.spring.io/spring-ai/reference/api/functions.html

- permits the model to request the execution of client-side tools and functions, thereby accessing necessary real-time information as required.

Observability

https://docs.spring.io/spring-ai/reference/observability/index.html

- Provides insights into AI-related operations.

Document injection

ETL framework

https://docs.spring.io/spring-ai/reference/api/etl-pipeline.html

for Data Engineering.

AI Model Evaluation

https://docs.spring.io/spring-ai/reference/api/testing.html

- Utilities to help evaluate generated content and protect against hallucinated response.

ChatClient API

https://docs.spring.io/spring-ai/reference/api/chatclient.html

- Fluent API for communicating with AI Chat Models, idiomatically similar to the WebClient and RestClient APIs.

Advisors API

https://docs.spring.io/spring-ai/reference/api/advisors.html

- Encapsulates recurring Generative AI patterns, transforms data sent to and from Language Models (LLMs), and provides portability across various models and use cases.

Support for

Chat Conversation Memory

https://docs.spring.io/spring-ai/reference/api/chatclient.html#\_chat\_memory

Retrieval Augmented Generation (RAG)

https://docs.spring.io/spring-ai/reference/api/chatclient.html#\_retrieval\_augmented\_generation

Spring Boot Auto Configuration and Starters for all AI Models and Vector Stores - use the

start.spring.io

https://start.spring.io/

to select the Model or Vector-store of choice.

This feature set lets you implement common use cases such as "

Q&A over your documentation

Chat with your documentation.

Documentation

reference documentation

https://docs.spring.io/spring-ai/reference/index.html

, sample applications, and workshop/course material.

Getting Started

#### You can get started in a few simple steps:

Create a Spring Boot Web application with a Spring AI OpenAI boot starter dependency. This

Spring Initializr link

https://start.spring.io/#!type=maven-project&language=java&platformVersion=3.3.4&packaging=jar&jvmVersion=17&groupId=spring.ai.example&artifactId=spring-ai-demo&name=spring-ai-demo&description=Spring%20AI%20%2C%20getting%20started%20example%2C%20using%20Open%20AI&packageName=spring.ai.example.spring-ai-demo&dependencies=web,spring-ai-openai

can help you bootstrap the application. (

With start.spring.io you can select any AI Models or Vector Stores that you want to use in your new applications

Add your OpenAI key to the

application.properties

Copyspring.ai.openai.api-key=<YOUR OPENAI KEY>

Add the following snippet to your

SpringAiDemoApplication

Copy@Bean
public CommandLineRunner runner(ChatClient.Builder builder) {
    return args -> {
        ChatClient chatClient = builder.build();
        String response = chatClient.prompt("Tell me a joke").call().content();							
        System.out.println(response);
    };
}

#### Run the application:

Copy./mvnw spring-boot:run

Want to get started in another way? View the

Getting Started section

https://docs.spring.io/spring-ai/reference/getting-started.html

in the reference documentation.

Quickstart Your Project

Bootstrap your application with

Spring Initializr

https://start.spring.io/

VMware offers training and certification to turbo-charge your progress.

https://spring.academy/

Get support

Tanzu Spring offers support and binaries for OpenJDK™, Spring, and Apache Tomcat® in one simple subscription.

https://spring.io/support

Upcoming events

Check out all the upcoming events in the Spring community.

https://spring.io/events

https://spring.io/why-spring

Generative AI

https://spring.io/ai

Microservices

https://spring.io/microservices

https://spring.io/reactive

Event Driven

https://spring.io/event-driven

https://spring.io/cloud

Web Applications

https://spring.io/web-applications

https://spring.io/serverless

https://spring.io/batch

https://spring.io/learn

https://spring.io/quickstart

https://spring.io/guides

https://spring.academy/courses

Get Certified

https://spring.academy/learning-path

https://spring.io/projects

https://spring.io/blog

Release Calendar

https://spring.io/projects#release-calendar

Version Mappings

https://spring.io/projects/generations

Release Highlights

https://spring.io/projects/release-highlights

Security Advisories

https://spring.io/security

https://spring.io/community

https://spring.io/events

https://spring.io/authors

https://enterprise.spring.io/

Long-term Support

https://enterprise.spring.io/lts-releases

Automated Upgrades

https://enterprise.spring.io/spring-application-advisor

Governance and Compliance

https://enterprise.spring.io/enterprise-extensions

Modern App Development

https://enterprise.spring.io/enterprise-components

https://spring.io/thank-you

Get the Spring newsletter

Stay connected with the Spring newsletter

https://go-vmware.broadcom.com/tnz-spring-newsletter-subscribe

Copyright © 2005 - 2026 Broadcom. All Rights Reserved. The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

Terms of Use

https://www.broadcom.com/company/legal/terms-of-use

https://www.broadcom.com/company/legal/privacy

Trademark Guidelines

https://spring.io/trademarks

Apache®, Apache Tomcat®, Apache Kafka®, Apache Cassandra™, and Apache Geode™ are trademarks or registered trademarks of the Apache Software Foundation in the United States and/or other countries. Java™, Java™ SE, Java™ EE, and OpenJDK™ are trademarks of Oracle and/or its affiliates. Kubernetes® is a registered trademark of the Linux Foundation in the United States and other countries. Linux® is the registered trademark of Linus Torvalds in the United States and other countries. Windows® and Microsoft® Azure are registered trademarks of Microsoft Corporation. “AWS” and “Amazon Web Services” are trademarks or registered trademarks of Amazon.com Inc. or its affiliates. All other trademarks and copyrights are property of their respective owners and are only mentioned for informative purposes. Other names may be trademarks of their respective owners.

https://www.youtube.com/user/SpringSourceDev

https://github.com/spring-projects

https://x.com/springcentral

https://bsky.app/profile/spring.io

Broadcom and our partners use technology, including cookies to, among other things, operate the site, analyze site usage, view and retain your site interactions, improve your experience and help us advertise. Click “Cookie Settings” to manage your privacy choices. By continuing to use our site, you agree to these data practices as described in our

Cookie Notice

https://www.broadcom.com/company/legal/cookie-policy

Cookies Settings

Privacy Preference Center

Privacy Preference Center

Your Privacy

Your Privacy

When you interact with Broadcom as set forth in the Privacy Policy through visiting any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience.

Cookie Policy

https://www.broadcom.com/company/legal/privacy/cookie-policy

Privacy Policy

https://www.broadcom.com/company/legal/privacy/policy

Strictly Necessary Cookies

Strictly Necessary Cookies

Always Active These cookies are necessary for the website to function and cannot be switched off in Broadcom's systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.

Functional Cookies

Functional Cookies

\[x\]  Functional Cookies These cookies enable the website to provide enhanced functionality and personalization. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.

Performance Cookies

Performance Cookies

\[x\]  Performance Cookies These cookies allow Broadcom to count visits and traffic sources so Broadcom can measure and improve the performance of its site. They help Broadcom to know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies Broadcom will not know when you have visited our site and will not be able to monitor its performance.

Targeting Cookies

Targeting Cookies

\[x\]  Targeting Cookies These cookies may be set through Broadcom's site by its advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.

Cookie List

Consent Leg.Interest

checkbox label label

checkbox label label

checkbox label label

checkbox label label

Apply Cancel

Confirm My Choices

Required Only Allow All

