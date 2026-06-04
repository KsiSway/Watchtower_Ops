---
sourceFile: "All you need to know about moving to containerd on Amazon EKS | Containers"
exportedBy: "Kortex"
exportDate: "2026-05-20T06:50:17.254Z"
---

# All you need to know about moving to containerd on Amazon EKS | Containers

d1b5ae12-11f3-43ca-9f07-6c370bd57a00

All you need to know about moving to containerd on Amazon EKS | Containers

eb80a4dc-37eb-4b63-b3d6-d0d12d0c9eba

https://aws.amazon.com/blogs/containers/all-you-need-to-know-about-moving-to-containerd-on-amazon-eks/

All you need to know about moving to containerd on Amazon EKS | Containers

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

Skip to Main Content

https://aws.amazon.com/blogs/containers/all-you-need-to-know-about-moving-to-containerd-on-amazon-eks/#aws-page-content-main

https://aws.amazon.com/?nc2=h\_home

Filter: All

https://aws.amazon.com/contact-us/?nc2=h\_ut\_cu

AWS Marketplace

https://aws.amazon.com/marketplace/?nc2=h\_utmp

Search Filter: All

Sign in to console

https://console.aws.amazon.com/console/home/?nc2=h\_si&src=header-signin

Create account

https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h\_su&src=header\_signup

https://aws.amazon.com/blogs/containers/

All you need to know about moving to containerd on Amazon EKS

by Arun Nalpet Ramakrishna, Chance Lee, and Gowtham S on 01 JUN 2023 in

Amazon Elastic Kubernetes Service

https://aws.amazon.com/blogs/containers/category/compute/amazon-kubernetes-service/

https://aws.amazon.com/blogs/containers/category/containers/

https://aws.amazon.com/blogs/containers/all-you-need-to-know-about-moving-to-containerd-on-amazon-eks/

https://aws.amazon.com/blogs/containers/all-you-need-to-know-about-moving-to-containerd-on-amazon-eks/

mailto:?subject=All%20you%20need%20to%20know%20about%20moving%20to%20containerd%20on%20Amazon%20EKS&body=All%20you%20need%20to%20know%20about%20moving%20to%20containerd%20on%20Amazon%20EKS%0A%0Ahttps://aws.amazon.com/blogs/containers/all-you-need-to-know-about-moving-to-containerd-on-amazon-eks/

https://aws.amazon.com/blogs/containers/all-you-need-to-know-about-moving-to-containerd-on-amazon-eks/

Introduction

The dockershim, an application programming interface (API) shim between the kubelet and the Docker Engine, deprecated from Kubernetes 1.24 in favor of supporting

Container Runtime Interface (CRI)

https://kubernetes.io/blog/2016/12/container-runtime-interface-cri-in-kubernetes/

compatible runtimes. Amazon Elastic Kubernetes Service (

https://aws.amazon.com/eks/

) also ended support of the dockershim starting with the Kubernetes version 1.24 release. The official

EKS Amazon Machine I

https://github.com/awslabs/amazon-eks-ami

mages(AMI) for version 1.24 and later include containerd as the only runtime, while versions earlier than 1.24 included both the Docker Engine and containerd with Docker Engine as the default runtime.

In this post, we'll walk you through the context around Dockershim removal and the implications when moving from Docker Engine to containerd runtime to help you prepare run your Kubernetes workloads on it. We'll also discuss dependency scenarios, along with various AWS native and open-source tools for considerations.

About Dockershim removal

A container runtime is a software component that run containers and manages container images on a node. Docker Engine was the first container runtime leveraged by Kubernetes. Hence, as part of the development, Docker Engine support was inadvertently hardcoded into Kubernetes. With increased Kubernetes adoption, users wanted a choice of container runtimes to cater to different use cases. With multiple container runtimes around, there was a need to provide flexibility that allows smooth interoperability of different container runtimes. Thus, Kubernetes community released

Container Runtime Interface (CRI)

https://github.com/kubernetes/cri-api

, a plug-in interface to support communication between the kubelet and container runtimes without the need to hard code runtime's APIs into the Kubernetes code base.

Docker Engine is not Container Runtime Interface(CRI) compatible because it existed before the CRI was created. To solve this, Dockershim was introduced as part of kubelet component to fill in the gap between Docker Engine and CRI (Figure 1).

The fact that kubelet has a tight dependency on specific container runtime led to maintenance burden. To remove this dependency and move toward a collaborative community in support of open standards, the Kubernetes community announced the decision to

deprecate Dockershim

https://kubernetes.io/blog/2022/02/17/dockershim-faq/

. Under the hood, Docker Engine was using containerd. Dockershim removal eliminated one extra hop in the stack (Figure 1).

In general, the Kubernetes developer community is in favor of having to develop and maintain only the “Kubernetes core” and abstract out all other supporting components like container runtime, storage, networking, etc., through a mechanism of having standard interface and implementation specific plugins. This de-coupling allows the supporting components having release cycles independent of core Kubernetes releases.

#### Figure 1: Removal of Dockershim and moving to containerd \[Src:

https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you/#role-of-dockershim

https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you/#role-of-dockershim

Why Containerd

Containerd was

one component of a decomposition of the original Docker engine

https://www.docker.com/blog/introducing-containerd/

into discrete components, including the runc executor and containerd as a lifecycle manager for runc. It was subsequently donated to the Cloud Native Computing Foundation (CNCF) after increasing scope to add image management and registry interactions to stand alone as a core container runtime with an emphasis on simplicity, robustness, and portability, provided as a daemon that can manage the complete container lifecycle. Containerd has a much smaller scope than Docker that results in a smaller codebase that's easier to maintain and support over time. The Container Runtime Interface (CRI) plugin is built into containerd since version 1.1, which is enabled by default and interacts with containerd through direct function calls. This eliminates another grpc hop in the stack (Figure 2).

#### Figure 2: CRI plugin built into containerd \[Src:

https://kubernetes.io/blog/2018/05/24/kubernetes-containerd-integration-goes-ga/

https://kubernetes.io/blog/2018/05/24/kubernetes-containerd-integration-goes-ga/

As described in the introduction, Amazon EKS official AMIs have containerd as the only runtime starting with Kubernetes version 1.24. Amazon EKS

https://docs.aws.amazon.com/ecs/?icmpid=docs\_homepage\_serverless

and Bottlerocket already use containerd only.

Can I still use my existing images?

With containerd, you can still use container images built from “docker build” as they are Open Container Initiative (

https://opencontainers.org/

)-compatible. Any OCI-compliant image, regardless of the tool you use to build it, will look the same to Kubernetes.

Important note on the timelines

#### Kubernetes:

Dockershim was marked

deprecated in Kubernetes version 1.20

https://kubernetes.io/blog/2022/02/17/dockershim-faq/

Dockershim is removed from Kubernetes version 1.24 onward.

#### Amazon EKS:

Amazon EKS has Docker Engine as a default runtime until Kubernetes version 1.23.

Amazon EKS supports enabling containerd for Kubernetes version 1.23 (and prior versions) (

https://docs.aws.amazon.com/eks/latest/userguide/eks-optimized-ami.html#containerd-bootstrap

https://docs.aws.amazon.com/eks/latest/userguide/eks-optimized-ami.html#containerd-bootstrap

containerd is the default runtime on Amazon EKS Kubernetes version 1.24 onward.

#### Containerd:

containerd version 1.6.4+, 1.7.0+ support Kubernetes version 1.24.

https://containerd.io/releases/#kubernetes-support

https://containerd.io/releases/#kubernetes-support

Solution overview

Impact on your application: Scenarios where there is a dependency with Docker Engine runtime

Scenario 1: Metrics and security agents

Some container applications like metrics collector or security agents have the Docker daemon's socket (/var/run/docker.sock) mounted as a volume. These container images invoke Docker APIs to interact with underlying Docker runtime through Docker socket for collecting metrics or monitoring events, etc. In the absence of Docker runtime, these APIs fail to gather information.

This is because the containerd's runtime interaction protocol is completely different from Docker Engine's. The communication with Docker Engine happens over a RESTful HTTP based API, while the communication with containerd happens over CRI protocol which is implemented using

https://grpc.io/

, which is an open-source remote procedure call (RPC) framework.

In this scenario, you must migrate the applications using runtime APIs, from the Docker Engine API to containerd's gRPC API.

Apart from this, you also need to mount appropriate container runtime socket for communication. For containerd, it is /run/containerd/containerd.sock.

Most of the widely used third-party independent software vendors who package their solutions in containers, employ a mechanism to detect the underlying container runtime and invoke corresponding client-libraries. Another option is to abstract away from the runtime, and rely only on CRI APIs, so that the applications is portable across all CRI compliant runtimes.

Scenario 2: Log format

The containerd runtime generates logs as a non-JSON string while Docker Engine uses JSON format to write logs by default. Fluentd's default configuration is designed to only expect JSON strings so when the runtime changes to containerd, it fails to parse any non-JSON log message from containerd and produce a large amount of parse error messages in its container logs. Here is an

https://github.com/fluent/fluentd-kubernetes-daemonset/issues/412

in Fluentd GitHub repository to check more details.

AWS has launched Fluent Bit as the default log solution for

Container insights

https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights.html

with significant performance gains and flexible parsers. When you're upgrading to Amazon EKS version 1.24 with Fluentd pre-configured, we encourage you to consider migrating to Fluent Bit. You must delete Fluentd before installing Fluent Bit to prevent Fluent Bit from processing Fluentd's parse error log messages and to ensure continuity in logging. Here's a

quick start guide

https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-setup-EKS-quickstart.html

Scenario 3: Container build process

Customers also host their Continuous Integration (CI) pipelines on Kubernetes, for triggering container builds. As part of this process, the CI tool executes a task that's essentially a Kubernetes Job. This Kubernetes Job typically is part of the CI pipeline, which takes up the responsibility of building the application, creating a container image and pushing it to the configured image repository. This job will essentially have docker.sock mounted as a volume and issues docker build instructions from within the container (Job).

Now that Docker runtime is not available, and we won't be able to use containerd to build images, the above CI pipeline breaks with the following error.

Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?

Moreover, building images this way also needs elevated privileges with additional security context to be set or privileged mode to be turned on.

The containerd by design is kept minimal to reduce the footprint and inter-dependencies, and hence doesn't include the tools to build container images. There are few workarounds to mitigate this issue:

Building images outside of Kubernetes Cluster

AWS CodeBuild

https://docs.aws.amazon.com/codebuild/?icmpid=docs\_homepage\_devtools

AWS CodePipeline

https://docs.aws.amazon.com/codepipeline/?icmpid=docs\_homepage\_devtools

Leverage AWS CodeBuild to build and push it either Amazon ECR, Docker Hub, or any private registry.

This approach will need re-architecting of your existing build process to adopt AWS CodeBuild. AWS CodeBuild provides fully managed CI service that compiles source code, run tests ,and build images at scale.

#### References:

Push image to Docker Hub using CodeBuild

https://docs.aws.amazon.com/codebuild/latest/userguide/sample-docker.html#sample-docker-docker-hub

Creating multi-architecture images using AWS CodeBuild and AWS CodePipeline

https://aws.amazon.com/blogs/devops/creating-multi-architecture-docker-images-to-support-graviton2-using-aws-codebuild-and-aws-codepipeline/

Use Amazon Elastic Compute Cloud (

https://docs.aws.amazon.com/ec2/?icmpid=docs\_homepage\_compute

) instance as build agent.

Setup a standalone Amazon EC2 instance as container image build agents, and redirect all build jobs to this particular node. This is suitable if there are a fewer number of builds.

Use GitHub actions to build and push to Amazon Elastic Container Registry (

https://docs.aws.amazon.com/ecr/?icmpid=docs\_homepage\_containers

) or docker repo.

There are several open-source GitHub actions published on GitHub marketplace.

Building images inside within a Kubernetes Cluster

Most of the following tools don't have a dependency on docker daemon, and hence, don't require elevated privileges. Some of these tools provide an option to execute the container builds as native Kubernetes Jobs (i.e., elevated securityContext not needed). They also provide simple Command Line Interface (CLI) as well, which use the build process that can be executed from within a container or on a specific build machine.

https://github.com/containers/buildah

Buildah has specific focus, which is to build container images without full blown runtime.

It is easy to incorporate this into scripts and build pipelines.

https://github.com/moby/buildkit

BuildKit is a toolkit for converting source code to build artifacts in an efficient, expressive, and repeatable manner.

BuildKit can be run in both privileged and unprivileged mode. Buildkit can be configured to run as an application on Kubernetes, and can be deployed as

Pod/Deployment/Statefulset/Job

https://github.com/moby/buildkit/tree/master/examples/kubernetes

K8s job definition of buildkit to build and push image

https://github.com/moby/buildkit/blob/master/examples/kubernetes/job.rootless.yaml

https://github.com/GoogleContainerTools/kaniko

This tool can be leveraged within a container or Kubernetes cluster.

Build and push images in kubernetes cluster.

Kaniko can be run as pod/deployment in Kubernetes. Just share the Dockerfile and build artifacts as arguments. The pod builds and pushes the image to specified container registry.

docker:dind (Docker-in-Docker) container build images

This is a container image(docker:dind), which has sock pre-packaged within the image and the docker daemon runs within the container.

This can be used purely for the purpose of building container images using Docker CLI.

But this approach requires you to configure this pod with elevated privileges. Hence, its recommended to adapt to one of the approaches mentioned above.

Detecting Docker Engine dependency

For identifying which of the pods have Docker Engine dependency, we need to figure out which of the pods are having Docker socket volume mounts. Or we can leverage dds, a kubectl krew plugin to scan through all the workload and detect which of the pods have this dependency (

https://github.com/aws-containers/kubectl-detector-for-docker-socket

https://github.com/aws-containers/kubectl-detector-for-docker-socket

#### Sample YAML with docker.sock mounted:

apiVersion: v1
kind: Pod
metadata:
  name: pod-with-hostpath-mounting
spec:
  containers:
  - name: test-webserver
    image: k8s.gcr.io/test-webserver:latest
    volumeMounts:
    - mountPath: /var/local/aaa
      name: mydir
    - mountPath: /var/local/aaa/1.txt
      name: myfile
  volumes:
  - name: mydir
    hostPath:
      # Ensure the file directory is created.
      path: /var/run/docker
      type: DirectoryOrCreate
  - name: myfile
    hostPath:
      path: /var/run/docker.sock
      type: FileOrCreate

Apache Configuration

#### Run kubectl dds command to identify pods with docker.sock mounted:

arun:~ $ kubectl dds
NAMESPACE       TYPE            NAME                            STATUS
default         pod             pod-with-hostpath-mounting      mounted
kube-system     daemonset       aws-node                        mounted

Apache Configuration

Should containers stop mounting docker sock?

Ideally, you should be mounting containerd socket. But many of the existing pod deployment artifacts have Dockershim mount. For the purpose of backward compatibility, the Dockershim volume mounts won't error out because with Amazon EKS optimized AMIs, there is a soft-link pointing to the current runtime (i.e., containerd). This soft-link is added to enable a smooth migration. If you are building your own custom AMIs, you need to ensure you either create this soft-link or update the mount host path to /run/containerd/containerd.sock.

With this pod, artifacts continue to have a Dockershim socket as part of the volume.

dockershim:
    Type:          HostPath (bare host directory volume)
    Path:          /var/run/dockershim.sock
    HostPathType:

Apache Configuration

under the hoods, we have:

/var/run/dockershim.sock -> /run/containerd/containerd.sock

Apache Configuration

Current mount points of Dockershim can continue to operate, but underneath containerd socket is being mounted. It is the client program within the container, that will need to identify the runtime configured on the node and use corresponding APIs for interaction.

Working with containerd

At times you might want to login to worker nodes, to inspect containers and troubleshoot. Docker CLI debugging capabilities like docker ps/inspect/exec will no longer be an option. Hence, let's look at a brief summary on containerd based interaction.

#### You can interact with containerd using various CLIs:

ctr: pre-packaged along with containerd, available out of the box. Mostly used to debug low-level CRI integration, not human-friendly, docker-incompatible

nerdctl: General purpose CLI tool that provides human-friendly experience very similar to docker

crictl: CLI for CRI-compatible container runtimes primarily to inspect and debug container runtimes and images

Out of these only ctr is pre-packaged. Other tools will need to be installed manually on need basis.

An important note while working with ctr or in general containerd runtimes. Containerd supports namespaces at the container runtime level. These namespaces are entirely different from the Kubernetes namespaces. Containerd namespaces are used to provide isolation to different applications that might be using containerd like docker, kubelet, etc. One such namespace configured by default for use by kubelet is k8s.io. Specify this namespace, with any of the CLI tools you choose to use.

The primary use-case of ctr is for containerd developers testing daemon or debugging low-level OCI container runtimes since it is close to the actual containerd API. As ctr is hard to use and not user-friendly, nerdctl or crictl are more preferred for general purpose.

If you are used to Docker commands in the past, you can install another tool nerdctl. This is Docker compatible CLI for containerd that provides similar experience as Docker CLI. This isn't installed on the Amazon EKS nodes out-of-the box, but the binary can be downloaded and run on nodes with containerd runtime. The binary of nerdctl can be downloaded from the

releases page

https://github.com/containerd/nerdctl/releases

. The only point to keep in mind is to specify the namespace of k8s.io while running the commands.

nerdctl --namespace k8s.io ps -a
CONTAINER ID    IMAGE                                                                                          COMMAND                   CREATED        STATUS     PORTS    NAMES
0a4be1e431de    602401143452.dkr.ecr-fips.us-east-1.amazonaws.com/eks/pause:3.5                                "/pause"                  4 hours ago    Up                  k8s://kube-system/aws-node-bcpqn
1154f11c1952    602401143452.dkr.ecr-fips.us-east-1.amazonaws.com/amazon-k8s-cni:v1.11.4                       "/app/entrypoint.sh"      4 hours ago    Up                  k8s://kube-system/aws-node-bcpqn/aws-node
183c759ff8de    602401143452.dkr.ecr-fips.us-east-1.amazonaws.com/eks/kube-proxy:v1.24.7-minimal-eksbuild.2    "kube-proxy --v=2 --…"    4 hours ago    Up                  k8s://kube-system/kube-proxy-xflnr/kube-proxy

Apache Configuration

For more details and samples, check out the GitHub repository at

https://github.com/containerd/nerdctl

https://github.com/containerd/nerdctl

crictl is a CLI for CRI-compatible container runtimes primarily to inspect and debug container runtimes and images on a Kubernetes node. If you use crictl to create pods on a running Kubernetes cluster, then the kubelet eventually deletes them because it's not a general purpose tool but for debugging. crictl and its source are hosted in the

https://github.com/kubernetes-sigs/cri-tools

repository. Most of commands are similar to Docker (

ex-crictl exec

crictl image

crictl logs

) with some unsupported features and only supported features in crictl. You can check mapping from Docker CLI to crictl here (

https://kubernetes.io/docs/reference/tools/map-crictl-dockercli/

https://kubernetes.io/docs/reference/tools/map-crictl-dockercli/

In this post, we showed you the context of Dockershim removal, and discussed various considerations and tools validate your Kubernetes workloads when moving from Docker Engine to containerd. We discussed scenarios where you might have a dependency on Docker runtime, and AWS native or open-source alternatives to consider when there is a dependency. Since the Docker CLI will no longer be available, we saw how we can use other tools like ctr, nerdctl, and crictl to interact with the container runtime to troubleshoot containers at node level.

Further reading

Kubernetes is Moving on From Dockershim: Commitments and Next Steps

https://kubernetes.io/blog/2022/01/07/kubernetes-is-moving-on-from-dockershim/

Amazon EKS ended support for Dockershim

https://docs.aws.amazon.com/eks/latest/userguide/dockershim-deprecation.html

Enable the containerd runtime bootstrap flag

https://docs.aws.amazon.com/eks/latest/userguide/eks-optimized-ami.html#containerd-bootstrap

Amazon EKS now supports Kubernetes version 1.24

https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-kubernetes-version-1-24/

https://aws.amazon.com/blogs/containers/tag/amazon-eks/

https://aws.amazon.com/blogs/containers/tag/containerd/

https://aws.amazon.com/blogs/containers/tag/docker/

https://aws.amazon.com/blogs/containers/tag/metrics/

https://aws.amazon.com/blogs/containers/tag/migration/

AWS Guided Amazon EKS Workshop

https://aws-experience.com/emea/smb/events/series/get-hands-on-with-amazon-eks?trk=4b7ca6c3-5ec3-40a1-978b-a227224ab35d&sc\_channel=el

Amazon Container Services

https://aws.amazon.com/containers?sc\_ichannel=ha&sc\_icampaign=acq\_awsblogsb&sc\_icontent=containers-resources

AWS Fargate

https://aws.amazon.com/fargate/?sc\_ichannel=ha&sc\_icampaign=acq\_awsblogsb&sc\_icontent=containers-resources

Amazon Elastic Container Service (ECS)

https://aws.amazon.com/ecs/?sc\_ichannel=ha&sc\_icampaign=acq\_awsblogsb&sc\_icontent=containers-resources

Amazon Elastic Kubernetes Service (EKS)

https://aws.amazon.com/eks?sc\_ichannel=ha&sc\_icampaign=acq\_awsblogsb&sc\_icontent=containers-resources

Amazon Elastic Container Registry (ECR)

https://aws.amazon.com/ecr?sc\_ichannel=ha&sc\_icampaign=acq\_awsblogsb&sc\_icontent=containers-resources

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

https://aws.amazon.com/blogs/containers/all-you-need-to-know-about-moving-to-containerd-on-amazon-eks/

Cookie Preferences

https://aws.amazon.com/blogs/containers/all-you-need-to-know-about-moving-to-containerd-on-amazon-eks/

© 2026, Amazon Web Services, Inc. or its affiliates. All rights reserved.

