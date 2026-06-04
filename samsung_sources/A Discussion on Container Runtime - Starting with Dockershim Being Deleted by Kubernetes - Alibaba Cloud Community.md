---
sourceFile: "A Discussion on Container Runtime - Starting with Dockershim Being Deleted by Kubernetes - Alibaba Cloud Community"
exportedBy: "Kortex"
exportDate: "2026-05-20T06:50:17.249Z"
---

# A Discussion on Container Runtime - Starting with Dockershim Being Deleted by Kubernetes - Alibaba Cloud Community

e27f13d0-6450-4f89-8cdf-f113609dd9cb

A Discussion on Container Runtime - Starting with Dockershim Being Deleted by Kubernetes - Alibaba Cloud Community

2a8834c6-0e9b-48f8-9721-49ac3749934c

https://www.alibabacloud.com/blog/a-discussion-on-container-runtime---starting-with-dockershim-being-deleted-by-kubernetes\_600118

A Discussion on Container Runtime - Starting with Dockershim Being Deleted by Kubernetes - Alibaba Cloud Community

https://www.alibabacloud.com/

Intl - English

javascript:;

International English

https://www.alibabacloud.com/blog/a-discussion-on-container-runtime---starting-with-dockershim-being-deleted-by-kubernetes\_600118

https://www.alibabacloud.com/blog/a-discussion-on-container-runtime---starting-with-dockershim-being-deleted-by-kubernetes\_600118

https://cn.aliyun.com/

https://cart.alibabacloud.com/

https://home.console.alibabacloud.com/

Account Management

https://account-console.alibabacloud.com/#/secure

https://account.alibabacloud.com/logout/logout.htm

https://account-intl.aliyun.com/login/login.htm

Free Account

https://account.alibabacloud.com/register/intl\_register.htm

Free Account

https://account.alibabacloud.com/register/intl\_register.htm

https://home.console.alibabacloud.com/

International English

https://www.alibabacloud.com/blog/a-discussion-on-container-runtime---starting-with-dockershim-being-deleted-by-kubernetes\_600118

https://www.alibabacloud.com/blog/a-discussion-on-container-runtime---starting-with-dockershim-being-deleted-by-kubernetes\_600118

https://cn.aliyun.com/

https://www.alibabacloud.com/blog/

https://resource.alibabacloud.com/event/index

https://resource.alibabacloud.com/webinar/index.htm

https://community.alibabacloud.com/tags/type\_blog-tagid\_28404/

https://www.alibabacloud.com/forum

https://community.alibabacloud.com/

https://resource.alibabacloud.com/event/index

https://resource.alibabacloud.com/webinar/index.htm

https://www.alibabacloud.com/getting-started/projects

https://www.alibabacloud.com/forum

Create Account

https://account.alibabacloud.com/register/register.htm?from\_type=yqclub&oauth\_callback=https%3A%2F%2Fwww.alibabacloud.com%2Fblog%2Fa-discussion-on-container-runtime---starting-with-dockershim-being-deleted-by-kubernetes\_600118%3Fdo%3Dlogin

https://account.alibabacloud.com/login/login.htm?from\_type=yqclub&oauth\_callback=https%3A%2F%2Fwww.alibabacloud.com%2Fblog%2Fa-discussion-on-container-runtime---starting-with-dockershim-being-deleted-by-kubernetes\_600118%3Fdo%3Dlogin

https://community.alibabacloud.com/

https://www.alibabacloud.com/blog/

A Discussion on Container Runtime - Starting with Dockershim Being Deleted by Kubernetes

A Discussion on Container Runtime - Starting with Dockershim Being Deleted by Kubernetes

Alibaba Cloud Community

https://community.alibabacloud.com/users/5337701737861729

June 20, 2023

https://www.alibabacloud.com/blog/a-discussion-on-container-runtime---starting-with-dockershim-being-deleted-by-kubernetes\_600118#comment

This article explains the evolution of OCI and Docker, explores CRI and CRI-compliant containerd and CRI-O, and describes the principle of Kubernetes log collection.

By Yemo, from Alibaba Cloud Storage Team

Kubernetes 1.24 was released

https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#dockershim-removed-from-kubelet

in May 2022. The highlight was that the dockershim component was removed from kubelet in this release. Starting from this release, users must choose containerd or CRI-O as the container runtime when using Kubernetes. If you want to continue to rely on Docker Engine as a container runtime, the cri-dockerd component is required.

Why did Kubernetes remove Docker?

The main reason is that Docker does not support the CRI container runtime standard promoted by Kubernetes for a long time. Kubernetes needs to maintain the dockershim component for a long time to specifically adapt to Docker. Dockershim was a product of the early days of Kubernetes and the heyday of Docker. However, with the development of container runtime (such as containerd), Kubernetes has enough reasons to stop maintaining dockershim.

After removing dockershim, does Kubernetes not support Docker at all?

The answer is no. At present, in the community, there is a shim

cri-dockerd

https://github.com/Mirantis/cri-dockerd

(provided by Mirantis and acquired by Docker Enterprise in 2019) that is independent of Kubernetes and supports CRI. Users can use shim to implement Kubernetes support for Docker.

In addition, since Docker Image has become the standard image format used by various container runtime, it may become a common phenomenon to use Docker in the development phase and use containerd and other container runtimes in the production environment for a long time.

Here, we briefly introduce the whole event of removing dockershim from Kubernetes. At the same time, many concepts including CRI, dockershim, containerd are mentioned. This article will take a deeper look at the container runtime.

The Evolution of OCI and Docker

When it comes to container runtime, we have to mention Open Container Initiative (OCI).

Open Container Initiative

OCI, proposed in the context of preventing the container technology from fragmenting, is a formal specification for formulating container image format and container runtime, which mainly include

OCI Runtime Spec

https://github.com/opencontainers/runtime-spec

OCI Image Spec

https://github.com/opencontainers/image-spec

OCI Distribution Spec

https://github.com/opencontainers/distribution-spec

The well-known

https://github.com/opencontainers/runc

is a reference implementation of Runtime Spec. It was first migrated from the libcontainer of Docker and later donated to OCI by Docker. Docker containers are created based on runc.

#### The container runtime can be divided hierarchically:

#### Low-Level Runtime (OCI Runtime):

This refers to the container runtime that only focuses on running containers. It is responsible for calling the operating system and using namespaces and cgroups to isolate and restrict resources (such as runc and rkt).

#### High-Level Runtime:

Compared to low-level runtimes, it is located at the upper layer of the stack and is responsible for transporting and managing container images, unpacking images, and passing off to the low-level runtime to run the container (such as containerd and cri-o).

Starting from Docker 1.11 (2016), Docker Daemon was split into multiple modules to adapt to the OCI standard. Among them, containerd is a container runtime that manages the lifecycle of a container (such as creation, start, stop, abort, signal processing, and deletion). Other services (such as image building, volume management, and log) are provided by other modules of Docker Daemon.

The container operation process in the figure above can be simplified as Docker Daemon → containerd → containerd-shim → runc. Among them, the containerd-shim is the direct operator of containers.

containerd-shim is introduced here because runc will exit after the container is created and run. As such, containerd-shim is used as the parent process of the container instead of containerd. This avoids the problem that all containers on the entire host have to exit when containerd does not work.

Container Runtime Interface (CRI)

What Is CRI?

When it comes to Kubernetes removing dockershim events, we have to mention CRI. First of all, let's understand the background of CRI. In the early days of Kubernetes (before v1.5), Docker was the only container runtime supported by Kubernetes, and Kubelet directly called Docker API through hard coding. Later, a new container runtime rkt appeared and hoped to be integrated into the Kubelet code. Then, as a growing number of container runtimes emerged, it became clear that embedding was no longer suitable. In this context, the Container Runtime Interface (CRI) standard is proposed to decouple the Kubelet code from the implementation code of specific container runtime.

However, when Kubernetes launched CRI, it was not as dominant as it is now. Various container runtimes did not actively implement CRI, so it is necessary to adapt various container runtimes through CRI shim. For example, Docker had no intention to support CRI for the following reasons: Docker appeared earlier than Kubernetes, and Docker was in a stable and stronger position. Docker intended to promote Swarm, which was regarded as a competitor of Kubernetes. Finally, Kubelet chose the built-in dockershim to provide support for Docker.

Below is the architecture of Kubelet after the CRI interface is introduced.

The API defined by CRI

https://github.com/kubernetes/kubernetes/blob/release-1.5/pkg/kubelet/api/v1alpha1/runtime/api.proto

mainly consists of two gRPC services: ImageService and RuntimeService.

ImageService is responsible for pulling, viewing, and deleting images.

RuntimeService is responsible for managing the lifecycle of pods and containers and interaction calls among containers (such as exec, attach, and port-forward).

Thanks to CRI, kubelet can achieve unified management of container runtimes (such as Docker, containerd, and CRI-O).

#### The supporting forms of Docker:

Docker enjoyed a high status in the early days of CRI. Kubernetes built dockershim into kubelet to support Docker.

Kubelet (CRI Client) calls dockershim (CRI Server) through CRI. Dockershim requests the Docker Daemon to call containerd and then use containerd-shim and runc to create a container.

The call link of Docker is too long, and there are many redundant operations. As the CRI ecosystem became more perfect, the Kubernetes community removed dockershim in July 2020. Dockershim was officially deleted in version 1.24.

#### The supporting forms of containerd:

#### Containerd 1.0:

Adaptation to CRI is achieved through a separate CRI-Containerd process. The main reason why a separate CRI-Containerd is redundant is that CRI did not have absolute dominance in the early days and required kubelet to adapt to various container runtimes.

#### Containerd 1.1:

The CRI-Containerd is removed, and the adaptation logic is directly integrated into the main process of containerd as a plug-in.

In summary, kubelet can achieve unified management of Docker, containerd, and CRI-O with the help of CRI. After Kubernetes 1.24 removes the dockershim component from kubelet, we recommend using containerd or CRI-O. Next, we will focus on containerd and CRI-O.

Containerd is an industry-standard container runtime that emphasizes simplicity, robustness, and portability.

Manage the lifecycle of containers (from creation to destruction)

Pull / push container images

Storage management (managing the storage of images and container data)

Call runc to run the container (interact with runc and other container runtimes)

Manage container network interfaces and networks

Containerd was originally separated from Docker. As an independent open-source project, containerd aims to provide a more open and stable container operation infrastructure. (

Please see the architecture diagram in the Docker section for details.

The official architecture diagram provided by containerd shows that containerd also adopts the C/S architecture. containerd manages the complete container lifecycle of its host system: image transfer and storage, container execution and supervision, low-level storage and network attachments, etc. Runc is responsible for running containers. All containers that comply with OCI specifications can be supported.

In addition, containerd implements a richer container interface. In addition to using CRI, you can use the ctr tool to call these rich container runtime interfaces. For example:

A Docker-like command-line tool for operating CRI

Verify whether the CRI interface meets expectations

#### Performance Tool:

Test interface performance

The Kubernetes community has also developed a CRI runtime CRI-O specifically for Kubernetes, and the CRI-O is directly compatible with CRI and OCI specifications. It is a lightweight alternative to using Docker as the runtime for Kubernetes and supports any OCI-conformant runtimes. Kubelet talks directly to the CRI-O through CRI to extract an image and launch a lower-level runtime (such as runc).

An important difference between CRI-O and containerd is that CRI-O removed some unnecessary Linux features to reduce the possibility of external attacks.

CRI-O is a CRI service implemented by packaging the container interface directly on the OCI. Only specific CRI interfaces are provided to the public, and it does not have the ctr tool capability similar to containerd.

#### The overall architecture is shown below:

Multiple Container Runtimes

With the emergence of more container runtimes, different container runtimes have different requirement scenarios, so there is a need for multiple container runtimes, for which the Kubernetes community has introduced RuntimeClass.

Currently, sandboxed containers of Alibaba Cloud Container Service for Kubernetes (ACK) support multiple container runtimes. As shown in the following figure, the Pod of runc is on the left side, and the corresponding RuntimeClass is runc. The Pod of runv is on the right side, and the corresponding RuntimeClass is runv. You can configure multiple container runtimes in containerd.

kube-apiserver → kubelet → cri-plugin (cri-plugin queries the containerd configuration file for the Handler corresponding to runc) → Shim API runtime v1 → containerd-shim (it is a plug-in that implements CRI) → create a runc container

kube-apiserver → kubelet → cri-plugin (cri-plugin queries the containerd configuration file for the Handler corresponding to runv) → Shim API runtime v2 → containerd-shim-kata-v2 (it is a plug-in that implements CRI) → create a kata container

Kubernetes Log Collection Support

As an important part of observability construction, logs can record access requests and error information in detail, which is convenient for us to locate problems. Applications on Kubernetes, Kubernetes components, and hosts generate various types of log data. With the development of Kubernetes, it has gone through the phases of Docker to CRI, increasing the complexity of log collection.

iLogtail, an infrastructure for collecting observability data launched by

Alibaba Cloud Log Service (SLS)

https://www.alibabacloud.com/product/log-service

, has good support for Docker and containerd in Kubernetes scenarios. iLogtail generally uses two deployment modes: Sidecar and DaemonSet.

The prerequisite for Logtail to collect business Pods or containers is to have access to the container runtime on the host and have access to the business container's data.

#### Access the Container Runtime:

The Logtail container will mount the sock of container runtime (Docker Engine/ContainerD) on the host to the container directory and the Logtail container can access the Docker Engine/ContainerD of this node.

#### Access the Data of Business Containers:

The Logtail container mounts the root directory ('/' directory) of the host to the /logtail\_host of the container. You can access the data of other containers through the /logtail\_host directory (provided that the file system of the Docker Engine is stored on the host in the form of a common file system (such as overlays) or the log directory of the container is mounted to the host through the hostPath or emptyDir volume).

Please read the article entitled

Comprehensive Analysis of Kubernetes Log Collection Principles

https://www.alibabacloud.com/blog/comprehensive-analysis-of-kubernetes-log-collection-principles\_599411

for more information.

iLogtail is open-source

https://github.com/alibaba/ilogtail

. You are welcome to follow us.

This topic describes the evolution of OCI and Docker.

This topic describes CRI and CRI-compliant containerd and CRI-O.

This topic describes the principle of Kubernetes log collection.

For more information, please check

containerd github

https://github.com/containerd/containerd

https://community.alibabacloud.com/tags/type\_blog-tagid\_72/

https://community.alibabacloud.com/tags/type\_blog-tagid\_13302/

https://community.alibabacloud.com/tags/type\_blog-tagid\_16286/

https://community.alibabacloud.com/tags/type\_blog-tagid\_16433/

https://community.alibabacloud.com/tags/type\_blog-tagid\_27989/

cloud native

https://community.alibabacloud.com/tags/type\_blog-tagid\_28580/

https://community.alibabacloud.com/tags/type\_blog-tagid\_34202/

Container Runtime

https://community.alibabacloud.com/tags/type\_blog-tagid\_36253/

https://community.alibabacloud.com/tags/type\_blog-tagid\_36254/

https://www.alibabacloud.com/blog/a-discussion-on-container-runtime---starting-with-dockershim-being-deleted-by-kubernetes\_600118#comment

javascript:;

javascript:;

javascript:;

#### Read previous post:

Common Causes and Troubleshooting Methods for Connection Reset

https://www.alibabacloud.com/blog/common-causes-and-troubleshooting-methods-for-connection-reset\_600117

#### Read next post:

Alibaba Cloud's Energy Expert Helps Analyze Carbon Footprint for The First Olympic Esports Week

https://www.alibabacloud.com/blog/alibaba-clouds-energy-expert-helps-analyze-carbon-footprint-for-the-first-olympic-esports-week\_600126

Alibaba Cloud Community

https://community.alibabacloud.com/users/5337701737861729

1,403 posts | 493 followers

https://www.alibabacloud.com/blog/a-discussion-on-container-runtime---starting-with-dockershim-being-deleted-by-kubernetes\_600118

You may also like

Getting Started with Kubernetes | Kubernetes Container Runtime Interface

https://www.alibabacloud.com/blog/getting-started-with-kubernetes-%7C-kubernetes-container-runtime-interface\_596339

Alibaba Developer - June 23, 2020

CRI and ShimV2: A New Idea for Kubernetes Integrating Container Runtime

https://www.alibabacloud.com/blog/cri-and-shimv2-a-new-idea-for-kubernetes-integrating-container-runtime\_594783

Alibaba Developer - May 8, 2019

Container Technology: Container Image

https://www.alibabacloud.com/blog/container-technology-container-image\_597932

Alibaba Developer - July 20, 2021

DADI: Alibaba Cloud's Open-Source Accelerated Container Image Technology

https://www.alibabacloud.com/blog/dadi-alibaba-clouds-open-source-accelerated-container-image-technology\_597956

Alibaba Container Service - July 28, 2021

Thoughts on the Development of Secure Container Technology

https://www.alibabacloud.com/blog/thoughts-on-the-development-of-secure-container-technology\_595467

Alibaba Container Service - October 23, 2019

Kubernetes CronJobs - Part 1: Basics

https://www.alibabacloud.com/blog/kubernetes-cronjobs---part-1-basics\_595021

Alibaba Clouder - July 2, 2019

javascript:;

javascript:;

javascript:;

Alibaba Cloud Community

https://community.alibabacloud.com/users/5337701737861729

1,403 posts | 493 followers

https://www.alibabacloud.com/blog/a-discussion-on-container-runtime---starting-with-dockershim-being-deleted-by-kubernetes\_600118

Related Products

Container Service for Kubernetes

https://community.alibabacloud.com/go/1/214

Alibaba Cloud Container Service for Kubernetes is a fully managed cloud container management service that supports native Kubernetes and integrates with other Alibaba Cloud products.

https://community.alibabacloud.com/go/1/214

https://community.alibabacloud.com/go/1/441

Provides a control plane to allow users to manage Kubernetes clusters that run based on different infrastructure resources

https://community.alibabacloud.com/go/1/441

Container Compute Service (ACS)

https://community.alibabacloud.com/go/1/478

A cloud computing service that provides container compute resources that comply with the container specifications of Kubernetes

https://community.alibabacloud.com/go/1/478

Cloud-Native Applications Management Solution

https://community.alibabacloud.com/go/1/322

Accelerate and secure the development, deployment, and management of containerized applications cost-effectively.

https://community.alibabacloud.com/go/1/322

by Alibaba Cloud Community

https://community.alibabacloud.com/users/5337701737861729/article

Alibaba Introduces Fun-ASR1.5: Advancing Multi-language Speech Recognition

https://www.alibabacloud.com/blog/alibaba-introduces-fun-asr1-5-advancing-multi-language-speech-recognition\_603138

Alibaba Cloud Launches New AI Model Subscription Service for Enterprises and Developers

https://www.alibabacloud.com/blog/alibaba-cloud-launches-new-ai-model-subscription-service-for-enterprises-and-developers\_603136

AliViews: Eddie Wu on Alibaba's Q4 Earnings

https://www.alibabacloud.com/blog/aliviews-eddie-wu-on-alibabas-q4-earnings\_603122

Alibaba's Cloud Revenue Growth Accelerates to 40% as AI Strategy Delivers

https://www.alibabacloud.com/blog/alibaba%E2%80%99s-cloud-revenue-growth-accelerates-to-40%25-as-ai-strategy-delivers\_603121

Qwen Conference 2026: A First Look at the Exhibition Highlights!

https://www.alibabacloud.com/blog/qwen-conference-2026-a-first-look-at-the-exhibition-highlights\_603119

Alibaba Opens All of Taobao to Qwen AI, Ushering in a New Agentic Shopping Experience

https://www.alibabacloud.com/blog/alibaba-opens-all-of-taobao-to-qwen-ai-ushering-in-a-new-agentic-shopping-experience\_603104

Alibaba's Qwen Glasses Upgrades with Proactive AI Capabilities and Spatial 3D Display to Elevate Intuitive AI Experiences

https://www.alibabacloud.com/blog/alibaba%E2%80%99s-qwen-glasses-upgrades-with-proactive-ai-capabilities-and-spatial-3d-display-to-elevate-intuitive-ai-experiences\_603099

Alibaba Clinches Back-to-Back Spot on TIME100 Most Influential Companies List

https://www.alibabacloud.com/blog/alibaba-clinches-back-to-back-spot-on-time100-most-influential-companies-list\_603087

FlashQLA: CP-/Bwd-Friendly Fused Linear Attention Kernels for GDN

https://www.alibabacloud.com/blog/flashqla-cp-bwd-friendly-fused-linear-attention-kernels-for-gdn\_603084

Qwen-Scope: Decoding Intelligence, Unleashing Potential

https://www.alibabacloud.com/blog/qwen-scope-decoding-intelligence-unleashing-potential\_603083

A Free Trial That Lets You Build Big!

Start building with 80+ products and up to 12 months usage for Elastic Compute Service

Get Started for Free

https://www.alibabacloud.com/campaign/free-trial/enterprise

Get Started for Free

https://www.alibabacloud.com/blog/campaign/free-trial

Sales Support

Live-chat with our sales team or get in touch with a business development professional in your region.

Contact Sales

https://www.alibabacloud.com/contact-sales

Technical Support

Open a ticket and get quick help from our technical team.

Open a Ticket >

https://smartservice.console.alibabacloud.com/service/create-ticket-intl

Connect & Report Abuse

We look forward to your suggestion.

Post a Suggestion >

https://account.alibabacloud.com/login/login.htm?oauth\_callback=https://connect.console.aliyun.com

Report Abuse >

https://www.alibabacloud.com/report

Chat now with

Alibaba Cloud Customer Service

to assist you in finding the right products and services to meet your needs.

Hi, I'm Alibaba Cloud AI Assistant! I can help with questions and solutions.

https://www.alibabacloud.com/ai-assistant?displayMode=widget

{"moduleinfo":{"followUsLinks\_count":\[{"count\_phone":4,"count":4}\],"languages\_count":\[{"count\_phone":2,"count":2}\],"linkArray\_count":\[{"count\_phone":11,"count":11}\],"helperLinks\_count":\[{"count\_phone":17,"count":17}\],"links\_count":\[{"count\_phone":4,"count":4}\],"i18n":{"copyRight":"© 2009-2026 Copyright by Alibaba Cloud All rights reserved"},"showTruste":true},"links":\[{"rel":"follow","text":"About Us","url":"//intl.aliyun.com/about","target":"\_self"},{"rel":"nofollow","text":"Privacy Policy","url":"https://intl.aliyun.com/help/en/faq-detail/42425.htm","target":"\_self"},{"rel":"nofollow","text":"Legal","url":"//intl.aliyun.com/help/product/42384.htm","target":"\_self"},{"rel":"nofollow","text":"Notice List","url":"//intl.aliyun.com/notice","target":"\_self"}\],"helperLinks":\[{"text":"Alibaba Group","url":"http://www.alibabagroup.com/en/global/home","target":"\_blank"},{"text":"Taobao Marketplace","url":"//www.taobao.com/","target":"\_blank"},{"text":"Tmall","url":"//www.tmall.com/","target":"\_blank"},{"text":"Juhuasuan","url":"//ju.taobao.com/","target":"\_blank"},{"text":"AliExpress","url":"http://www.aliexpress.com/","target":"\_blank"},{"text":"Alibaba.com","url":"http://www.alibaba.com/","target":"\_blank"},{"text":"1688","url":"http://www.1688.com/","target":"\_blank"},{"text":"Alimama","url":"http://www.alimama.com/index.htm","target":"\_blank"},{"text":"Alitrip","url":"https://www.alitrip.com/","target":"\_blank"},{"text":"YunOS","url":"http://www.yunos.com/","target":"\_blank"},{"text":"AutoNavi","url":"http://www.autonavi.com/","target":"\_blank"},{"text":"UCWeb","url":"http://www.ucweb.com/","target":"\_blank"},{"text":"Umeng","url":"http://www.umeng.com/","target":"\_blank"},{"text":"Xiami","url":"http://www.xiami.com/","target":"\_blank"},{"text":"DingTalk","url":"http://www.dingtalk.com/?lwfrom=20150205111943449","target":"\_blank"},{"text":"Alipay","url":"https://www.alipay.com/","target":"\_blank"}\],"languages":\[{"text":"English","key":"en"},{"text":"简体中文","key":"zh"}\],"followUsLinks":\[{"icon":"fa fa-facebook","text":"Facebook","url":"https://www.facebook.com/alibabacloud/","target":"\_self"},{"icon":"fa fa-linkedin","text":"Linkedin","url":"//www.linkedin.com/company/alibaba-cloud-computing-company","target":"\_self"},{"icon":"fa fa-twitter","text":"Twitter","url":"//www.twitter.com/alibaba\_cloud","target":"\_self"},{"icon":"fa fa-google-plus","text":"Google+","url":"//plus.google.com/113352360570257060531/","target":"\_self"}\],"linkArray":\[{"url":"//intl.aliyun.com"},{"url":"//intl.aliyun.com/why-alibaba-cloud"},{"url":"//intl.aliyun.com/product"},{"url":"//intl.aliyun.com/solution"},{"url":"//intl.aliyun.com/chinaconnect"},{"url":"//intl.aliyun.com/icp"},{"url":"//intl.aliyun.com/pricing"},{"url":"//intl.aliyun.com/trust-center"},{"url":"//intl.aliyun.com/free-trial"},{"url":"//intl.aliyun.com/startup"},{"url":"//intl.aliyun.com/partner"}\]} pc

https://intl.aliyun.com/about

Privacy Policy

https://intl.aliyun.com/help/en/faq-detail/42425.htm

https://intl.aliyun.com/help/product/42384.htm

Notice List

https://intl.aliyun.com/notice

Alibaba Group

http://www.alibabagroup.com/en/global/home

Taobao Marketplace

https://www.taobao.com/

https://www.tmall.com/

https://ju.taobao.com/

http://www.aliexpress.com/

Alibaba.com

http://www.alibaba.com/

http://www.1688.com/

http://www.alimama.com/index.htm

https://www.alitrip.com/

http://www.yunos.com/

http://www.autonavi.com/

http://www.ucweb.com/

http://www.umeng.com/

http://www.xiami.com/

http://www.dingtalk.com/?lwfrom=20150205111943449

https://www.alipay.com/

© 2009-2026 Copyright by Alibaba Cloud All rights reserved

//intl.aliyun.com //intl.aliyun.com/why-alibaba-cloud //intl.aliyun.com/product //intl.aliyun.com/solution //intl.aliyun.com/chinaconnect //intl.aliyun.com/icp //intl.aliyun.com/pricing //intl.aliyun.com/trust-center //intl.aliyun.com/free-trial //intl.aliyun.com/startup //intl.aliyun.com/partner

