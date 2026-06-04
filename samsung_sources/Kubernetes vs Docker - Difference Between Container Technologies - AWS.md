---
sourceFile: "Kubernetes vs Docker - Difference Between Container Technologies - AWS"
exportedBy: "Kortex"
exportDate: "2026-05-20T06:50:17.447Z"
---

# Kubernetes vs Docker - Difference Between Container Technologies - AWS

15758a02-0d6b-4417-a16e-c07d825798db

Kubernetes vs Docker - Difference Between Container Technologies - AWS

003ab3ce-e303-4a3e-9bdd-c23c79e05b65

https://aws.amazon.com/compare/the-difference-between-kubernetes-and-docker/

Kubernetes vs Docker - Difference Between Container Technologies - AWS

Select your cookie preferences

We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can choose “Customize” or “Decline” to decline performance cookies.

If you agree, AWS and approved third parties will also use cookies to provide useful site features, remember your preferences, and display relevant content, including relevant advertising. To accept or decline all non-essential cookies, choose “Accept” or “Decline.” To make more detailed choices, choose “Customize.”

Accept Decline Customize

Customize cookie preferences

We use cookies and similar tools (collectively, "cookies") for the following purposes.

Essential cookies are necessary to provide our site and services and cannot be deactivated. They are usually set in response to your actions on the site, such as setting your privacy preferences, signing in, or filling in forms.

Performance

Performance cookies provide anonymous statistics about how customers navigate our site so we can improve site experience and performance. Approved third parties may perform analytics on our behalf, but they cannot use the data for their own purposes.

Functional cookies help us provide useful site features, remember your preferences, and display relevant content. Approved third parties may set these cookies to provide certain site features. If you do not allow these cookies, then some or all of these services may not function properly.

Advertising

Advertising cookies may be set through our site by us or our advertising partners and help us deliver relevant marketing content. If you do not allow these cookies, you will experience less relevant advertising.

Blocking some types of cookies may impact your experience of our sites. You may review and change your choices at any time by selecting Cookie preferences in the footer of this site. We and selected third-parties use cookies or similar technologies as specified in the

AWS Cookie Notice

https://aws.amazon.com/legal/cookies/

Cancel Save preferences

Your privacy choices

We and our advertising partners (“we”) may use information we collect from or about you to show you ads on other websites and online services. Under certain laws, this activity is referred to as “cross-context behavioral advertising” or “targeted advertising.”

To opt out of our use of cookies or similar technologies to engage in these activities, select “Opt out of cross-context behavioral ads” and “Save preferences” below. If you clear your browser cookies or visit this site from a different device or browser, you will need to make your selection again. For more information about cookies and how we use them, read our

Cookie Notice

https://aws.amazon.com/legal/cookies/

\[x\] allowed

Allow cross-context behavioral ads

\[-\] not allowed

Opt out of cross-context behavioral ads

To opt out of the use of other identifiers, such as contact information, for these activities, fill out the form

https://pulse.aws/application/ZRPLWLL6?p=0

For more information about how AWS handles your information, read the

AWS Privacy Notice

https://aws.amazon.com/privacy/

Cancel Save preferences

Unable to save cookie preferences

We will only store essential cookies at this time, because we were unable to save your cookie preferences.

If you want to change your cookie preferences, try again later using the link in the AWS console footer, or contact support if the problem persists.

Skip to main content

https://aws.amazon.com/compare/the-difference-between-kubernetes-and-docker/#aws-page-content-main

https://aws.amazon.com/?nc2=h\_home

Filter: All

https://aws.amazon.com/contact-us/?nc2=h\_ut\_cu

AWS Marketplace

https://aws.amazon.com/marketplace?nc2=h\_utmp

Search Filter: All

Sign in to console

https://console.aws.amazon.com/console/home/?nc2=h\_si&src=header-signin

Create account

https://signin.aws.amazon.com/signup?request\_type=register

What is Cloud Computing?

https://aws.amazon.com/what-is-cloud-computing/

Cloud Computing Concepts Hub

https://aws.amazon.com/what-is/

AWS for Every Application

https://aws.amazon.com/aws-for-every-application/

Developer Tools

What's the Difference Between Kubernetes and Docker?

Create an AWS Account

https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?pg=compare\_header

What's the difference between Kubernetes and Docker?

https://aws.amazon.com/compare/the-difference-between-kubernetes-and-docker/#ams#what-isc1#pattern-data

Where are Kubernetes and Docker used?

https://aws.amazon.com/compare/the-difference-between-kubernetes-and-docker/#ams#what-isc2#pattern-data

Key differences: Kubernetes vs. Docker

https://aws.amazon.com/compare/the-difference-between-kubernetes-and-docker/#ams#what-isc3#pattern-data

When to use Kubernetes or Docker

https://aws.amazon.com/compare/the-difference-between-kubernetes-and-docker/#ams#what-isc4#pattern-data

Summary of differences: Kubernetes vs. Docker Desktop

https://aws.amazon.com/compare/the-difference-between-kubernetes-and-docker/#ams#what-isc5#pattern-data

How can AWS support your container management requirements?

https://aws.amazon.com/compare/the-difference-between-kubernetes-and-docker/#ams#what-isc6#pattern-data

What's the difference between Kubernetes and Docker?

Docker is a container runtime technology that allows you to build, test, and deploy applications faster than traditional methods. It packages software into standardized units called

with everything the software needs to run—including libraries, system tools, and code. Kubernetes is a container orchestration tool that allows you to scale your container systems so you can manage, coordinate and schedule containers at a vast scale.

Where are Kubernetes and Docker used?

Kubernetes and Docker are both container technologies. Modern applications are made of microservices—independent components that run each application process as a service. Each service performs a single function and communicates with other services via a well-defined interface called

. Containerization provides the software tool to pack microservices as deployable programs on different platforms.

Read about microservices »

https://aws.amazon.com/microservices/

Read about containerization »

https://aws.amazon.com/what-is/containerization/

Create containers

Docker is an open-source container runtime that has gained popularity in recent years. It provides a toolkit for creating containers easily and efficiently. Developers run commands to build a container image file encompassing system libraries, tools, code, and other software configurations that each microservice requires. Every microservice has its own Docker image. You can use the Docker image to run the microservice in any environment.

Manage containers

Most applications are made of several microservices. Some of them can scale to thousands of microservices running across different servers. Multi-container applications introduce new management challenges:

How should you coordinate multiple containers?

How should you schedule containers?

How should you group and catalog containers?

Developers solve these challenges using a container orchestration platform like Kubernetes. Kubernetes is an open-source technology that lets you manage containers at scale. It handles operating complexities so you can scale your workloads and manage container deployment across multiple servers.

Key differences: Kubernetes vs. Docker

Both Kubernetes and Docker are open-source container technologies. However, they are fundamentally different in how they work and what role they play in distributing containerized applications. Developers use Docker to create and manipulate container images. They use Kubernetes to manage multiple microservices at scale. Each microservice is individually made up of multiple containers itself.

actually refers to a set of tools developers use to build, share, and run containerized applications. Here are some Docker commands you can use:

Use Docker Build to create container images

Use Docker Compose to define and run multi-container applications

Use Docker Hub to find and share container images, similar to GitHub for code sharing

On the other hand, Kubernetes works by managing a cluster of compute instances. It schedules containers to run on the cluster based on the available compute resources and the resource requirements of each container. Containers are run in logical groupings called

, and you can run and scale one or many containers together as a pod. You can automatically start additional pods on your Kubernetes cluster based on their resource requirements.

Core technology

Docker Engine is the component developers use for building and containerizing your applications. It offers APIs which specify interfaces that programs can use to talk to and instruct it.Similarly, Kubernetes control-plane software decides when and where to run container pods, manages traffic routing, and scales your pods based on utilization or other metrics you define.

Biggest benefit

Docker streamlines the development lifecycle by allowing developers to work in standardized environments using local containers which provide your applications and services. It's container-based platform allows for highly portable workloads. On the other hand, Kubernetes lets you define complex containerized applications and run them at scale across a cluster of servers.

When to use Kubernetes or Docker

Docker and Kubernetes are two different technologies with different use cases. You use Docker Desktop to run, edit and manager container development. You use Kubernetes to run production grade applications at scale.

Summary of differences: Kubernetes vs. Docker Desktop

Characteristics

What is it?

Container orchestration tool.

Stack of container technologies to create and run containers.

Coordinate multiple containers across multiple servers.

Package applications with libraries and runtime into container images.

Main benefit

Define and run complex containerized applications at scale.

Standardize application operations and ship code faster.

How can AWS support your container management requirements?

AWS has several container services

https://aws.amazon.com/containers/

that make managing your underlying container infrastructure easier, whether on premises or in the cloud. You can do everything from container orchestration to running containers without managing servers. We give some examples below.

Amazon Elastic Container Service

Amazon Elastic Container Service (Amazon ECS

https://aws.amazon.com/ecs/

) is a fully managed container orchestration service that makes it easy for you to deploy, manage, and scale containerized applications. You can replace Kubernetes with Amazon ECS to run Docker containers in the AWS Cloud.

Kubernetes vs. Amazon ECS

Amazon ECS provides two solutions in one service—a container orchestration tool and a fully managed service that automatically provisions underlying infrastructure resources. In contrast, Kubernetes requires you to provision resources in the cloud or on premises.

Amazon Elastic Kubernetes Service

Amazon Elastic Kubernetes Service (Amazon EKS

https://aws.amazon.com/eks/

) is a managed Kubernetes service to run Kubernetes in the AWS Cloud and on-premises data centers. In the cloud, Amazon EKS automatically manages the availability and scalability of the Kubernetes control plane nodes responsible for scheduling containers, managing application availability, storing cluster data, and other key tasks.

Next Steps with AWS

Start building with Kubernetes

Learn how to get started with Kubernetes on AWS Learn more\](https://aws.amazon.com/aws-for-every-application/)

Start building with Docker

Learn how to get started with Docker on AWS Learn more\](https://aws.amazon.com/aws-for-every-application/)

Browse all cloud computing concepts

#### Browse all cloud computing concepts content here:

Displaying 1-8 (293)

Displaying 1-8 (293)

\[2022-08-08

What is IaaS (Infrastructure as a Service)?

Infrastructure as a Service (IaaS) is a business model that delivers IT infrastructure like compute, storage, and network resources on a pay-as-you-go basis over the internet. You can use IaaS to request and configure the resources you require to run your applications and IT systems. You are responsible for deploying, maintaining, and supporting your applications, and the IaaS provider is responsible for maintaining the physical infrastructure. Infrastructure as a Service gives you flexibility and control over your IT resources in a cost-effective manner. Learn more\](https://aws.amazon.com/what-is/iaas/?trk=faq\_card)

\[2022-05-25

What is Machine Translation?

Machine translation is the process of using artificial intelligence to automatically translate text from one language to another without human involvement. Modern machine translation goes beyond simple word-to-word translation to communicate the full meaning of the original language text in the target language. It analyzes all text elements and recognizes how the words influence one another. Learn more\](https://aws.amazon.com/what-is/machine-translation/?trk=faq\_card)

\[2022-08-12

What is Block Storage?

Block storage is technology that controls data storage and storage devices. It takes any data, like a file or database entry, and divides it into blocks of equal sizes. The block storage system then stores the data block on underlying physical storage in a manner that is optimized for fast access and retrieval. Developers prefer block storage for applications that require efficient, fast, and reliable data access. Think of block storage as a more direct pipeline to the data as opposed to file storage which has an extra layer consisting of a file system (NFS, SMB) to process before accessing the data. Learn more\](https://aws.amazon.com/what-is/block-storage/?trk=faq\_card)

\[2021-09-29

What is a Relational Database?

A relational database is a collection of data items with pre-defined relationships between them. These items are organized as a set of tables with columns and rows. Tables are used to hold information about the objects to be represented in the database. Each column in a table holds a certain kind of data and a field stores the actual value of an attribute. The rows in the table represent a collection of related values of one object or entity. Each row in a table could be marked with a unique identifier called a primary key, and rows among multiple tables can be made related using foreign keys. This data can be accessed in many different ways without reorganizing the database tables themselves. Learn more\](https://aws.amazon.com/relational-database/?trk=faq\_card)

\[2023-10-02

What is Advanced Analytics?

Advanced analytics is the process of using complex machine learning (ML) and visualization techniques to derive data insights beyond traditional business intelligence. Modern organizations collect vast volumes of data and analyze it to discover hidden patterns and trends. They use the information to improve business process efficiency and customer satisfaction. With advanced analytics, you can take this one step further and use data for future and real-time decision-making. Advanced analytics techniques also derive meaning from unstructured data like social media comments or images. They can help your organization solve complex problems more efficiently. Advancements in cloud computing and data storage have made advanced analytics more affordable and accessible to all organizations. Learn more\](https://aws.amazon.com/what-is/advanced-analytics/?trk=faq\_card)

\[2023-10-04

What is a GPU?

A graphics processing unit (GPU) is an electronic circuit that can perform mathematical calculations at high speed. Computing tasks like graphics rendering, machine learning (ML), and video editing require the application of similar mathematical operations on a large dataset. A GPU's design allows it to perform the same operation on multiple data values in parallel. This increases its processing efficiency for many compute-intensive tasks. Learn more\](https://aws.amazon.com/what-is/gpu/?trk=faq\_card)

\[2024-08-01

What Is Enterprise AI?

Enterprise artificial intelligence (AI) is the adoption of advanced AI technologies within large organizations. Taking AI systems from prototype to production introduces several challenges around scale, performance, data governance, ethics, and regulatory compliance. Enterprise AI includes policies, strategies, infrastructure, and technologies for widespread AI use within a large organization. Even though it requires significant investment and effort, enterprise AI is important for large organizations as AI systems become more mainstream. Learn more\](https://aws.amazon.com/what-is/enterprise-ai/?trk=faq\_card)

\[2022-05-25

What is Web Hosting?

Web hosting is a service that stores your website or web application and makes it easily accessible across different devices such as desktop, mobile, and tablets. Any web application or website is typically made of many files, such as images, videos, text, and code, that you need to store on special computers called servers. The web hosting service provider maintains, configures, and runs physical servers that you can rent for your files. Website and web application hosting services also provide additional support, such as security, website backup, and website performance, which free up your time so that you can focus on the core functions of your website. Learn more\](https://aws.amazon.com/what-is/web-hosting/?trk=faq\_card)

Show 8 more

Did you find what you were looking for today?

Let us know so we can improve the quality of the content on our pages

Create an AWS account

https://signin.aws.amazon.com/signup?request\_type=register

What Is AWS?

https://aws.amazon.com/what-is-aws/?nc1=f\_cc

What Is Cloud Computing?

https://aws.amazon.com/what-is-cloud-computing/?nc1=f\_cc

What Is Agentic AI?

https://aws.amazon.com/what-is/agentic-ai/?nc1=f\_cc

Cloud Computing Concepts Hub

https://aws.amazon.com/what-is/?nc1=f\_cc

AWS Cloud Security

https://aws.amazon.com/security/?nc1=f\_cc

https://aws.amazon.com/new/?nc1=f\_cc

https://aws.amazon.com/blogs/?nc1=f\_cc

Press Releases

https://press.aboutamazon.com/press-releases/aws

Getting Started

https://aws.amazon.com/getting-started/?nc1=f\_cc

https://aws.amazon.com/training/?nc1=f\_cc

AWS Trust Center

https://aws.amazon.com/trust-center/?nc1=f\_cc

AWS Solutions Library

https://aws.amazon.com/solutions/?nc1=f\_cc

Architecture Center

https://aws.amazon.com/architecture/?nc1=f\_cc

Product and Technical FAQs

https://aws.amazon.com/faqs/?nc1=f\_dr

Analyst Reports

https://aws.amazon.com/resources/analyst-reports/?nc1=f\_cc

AWS Partners

https://aws.amazon.com/partners/work-with-partners/?nc1=f\_dr

Builder Center

https://aws.amazon.com/developer/?nc1=f\_dr

SDKs & Tools

https://aws.amazon.com/developer/tools/?nc1=f\_dr

.NET on AWS

https://aws.amazon.com/developer/language/net/?nc1=f\_dr

Python on AWS

https://aws.amazon.com/developer/language/python/?nc1=f\_dr

Java on AWS

https://aws.amazon.com/developer/language/java/?nc1=f\_dr

https://aws.amazon.com/developer/language/php/?nc1=f\_cc

JavaScript on AWS

https://aws.amazon.com/developer/language/javascript/?nc1=f\_dr

https://aws.amazon.com/contact-us/?nc1=f\_m

File a Support Ticket

https://console.aws.amazon.com/support/home/?nc1=f\_dr

AWS re:Post

https://repost.aws/?nc1=f\_dr

Knowledge Center

https://repost.aws/knowledge-center/?nc1=f\_dr

AWS Support Overview

https://aws.amazon.com/premiumsupport/?nc1=f\_dr

Get Expert Help

https://iq.aws.amazon.com/?utm=mkt.foot/?nc1=f\_m

AWS Accessibility

https://aws.amazon.com/accessibility/?nc1=f\_cc

https://aws.amazon.com/legal/?nc1=f\_cc

Back to top

Amazon is an equal opportunity employer and does not discriminate on the basis of protected veteran status, disability or other legally protected status.

https://twitter.com/awscloud

https://www.facebook.com/amazonwebservices

https://www.linkedin.com/company/amazon-web-services/

https://www.instagram.com/amazonwebservices/

https://www.twitch.tv/aws

https://www.youtube.com/user/AmazonWebServices/Cloud/

https://aws.amazon.com/podcasts/?nc1=f\_cc

https://pages.awscloud.com/communication-preferences?trk=homepage

https://aws.amazon.com/privacy/?nc1=f\_pr

https://aws.amazon.com/terms/?nc1=f\_pr

Your Privacy Choices

https://aws.amazon.com/compare/the-difference-between-kubernetes-and-docker/

Cookie Preferences

https://aws.amazon.com/compare/the-difference-between-kubernetes-and-docker/

© 2026, Amazon Web Services, Inc. or its affiliates. All rights reserved.

