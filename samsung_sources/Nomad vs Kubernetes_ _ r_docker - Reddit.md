---
sourceFile: "Nomad vs Kubernetes? : r/docker - Reddit"
exportedBy: "Kortex"
exportDate: "2026-05-20T06:50:17.463Z"
---

# Nomad vs Kubernetes? : r/docker - Reddit

f4c6f738-5642-42a6-b34e-72464df994ef

Nomad vs Kubernetes? : r/docker - Reddit

aca41c0f-f2c1-4556-a837-67cd71aec779

https://www.reddit.com/r/docker/comments/1rx0zw8/nomad\_vs\_kubernetes/

Nomad vs Kubernetes? : r/docker

Skip to main content

https://www.reddit.com/r/docker/comments/1rx0zw8/nomad\_vs\_kubernetes/#main-content

Nomad vs Kubernetes? : r/docker

Open navigation

https://www.reddit.com/

Go to Reddit Home

https://www.reddit.com/register/

Sign up for Reddit

https://www.reddit.com/login/

Log in to Reddit

Expand user menu

Open settings menu

Skip to Navigation

https://www.reddit.com/r/docker/comments/1rx0zw8/nomad\_vs\_kubernetes/#left-sidebar-container

Skip to Right Sidebar

https://www.reddit.com/r/docker/comments/1rx0zw8/nomad\_vs\_kubernetes/#right-sidebar-container

Go to docker

https://www.reddit.com/r/docker/

https://www.reddit.com/r/docker/

Inevitable\_Put\_4032

https://www.reddit.com/user/Inevitable\_Put\_4032/

Locked post

Stickied post

Archived post

Nomad vs Kubernetes?

Anybody out there who can share experiences about Nomad vs Kubernetes?

I was looking at Nomad for its simplicity but its licensing model does not make me 100% confident about its future. Besides, it does not seem to gain traction these days.

On the other hand, being a small team K8s looks too heavy for most of our use cases. So far we have mostly relied on AWS services (ALB + ECS) but we need on-premises alternatives that would not severely impact our operational costs.

Ideally I want to be able to package a local development environment (now managed via docker compose) and extend it to a multi-server deployment when needed. Nomad at first seemed to be the lighter possibility.

Upvote 19 Downvote 22 Go to comments Share

Sort by: Best

Open comment sort options

Controversial

Search Comments Expand comment search

Comments Section

https://www.reddit.com/user/mister2d/

https://www.reddit.com/r/docker/comments/1rx0zw8/comment/ob3y2rh/

- Edited 2mo ago

The experience I can share is that it pairs great with Vault for secrets management and Consul for service discovery. It's a first class citizen with those infrastructure pillars. There's no etcd to worry about for secrets exfil if you go with Nomad + Vault. Nomad job specs are easier for cognitive load. Nomad, Vault, Consul, Terraform all share the same configuration language which was built to be human readable.

Those are the pros I can think of.

I've designed greenfields with k8s and nomad. Nomad still powers my production home lab with Ceph csi for many years now. No pain points to report.

If you decide to deploy k8s, then I suggest looking into declarative k8s tooling like Talos Linux or Typhoon (based on flatcar Linux).

Upvote 13 Downvote Reply Award Share

Golden\_Age\_Fallacy

https://www.reddit.com/user/Golden\_Age\_Fallacy/

https://www.reddit.com/r/docker/comments/1rx0zw8/comment/ob8a3ls/

Built Nomad with all the Hashicorp enterprise integration, fully agree.

I run Talos in my homelab, love it.

Upvote 4 Downvote Reply Award Share

https://www.reddit.com/user/jfrazierjr/

https://www.reddit.com/r/docker/comments/1rx0zw8/comment/ob436de/

Depending on your use cases it sounds like docker swarm might be your solution.

Upvote 4 Downvote Reply Award Share

Alvarito1983\_

https://www.reddit.com/user/Alvarito1983\_/

https://www.reddit.com/r/docker/comments/1rx0zw8/comment/ob3m4zx/

Honestly for a small team coming from docker compose,

Docker Swarm

is worth considering before jumping to either. It's basically compose syntax but multi-host, zero new concepts to learn, and it's built into Docker. Not as powerful as K8s or Nomad but for "I want my compose setup to run across a few servers" it's often the right level of complexity.

#### That said, if you want something more capable but still sane:

Nomad's licensing concern is valid

since HashiCorp moved to BSL, but for most small teams the practical impact is minimal — it only matters if you're building a competing product. The real issue is the trajectory, and K3s/K8s has clearly won the mindshare war.

If I were in your position: start with Swarm, see if it covers your needs. If you outgrow it, K3s (lightweight Kubernetes) is a much gentler on-ramp to the K8s ecosystem than full K8s, and you keep your AWS knowledge transferable.

Upvote 3 Downvote Reply Award Share

https://www.reddit.com/user/Dangle76/

https://www.reddit.com/r/docker/comments/1rx0zw8/comment/ob3us32/

Tbh building a vm cluster is just as costly and the question is do you have enough running where you actually need the operational overhead of kubernetes. Most places don't.

Upvote 3 Downvote Reply Award Share

https://www.reddit.com/user/IulianHI/

https://www.reddit.com/r/docker/comments/1rx0zw8/comment/ob5rr3x/

Surprised Docker Swarm isn't getting more love here. If you're already working with compose files (which it sounds like you are), the jump to Swarm is almost zero — your compose files become stack deploy files with minimal changes. You get multi-node scheduling, rolling updates, overlay networks, and built-in load balancing without the cognitive overhead of K8s manifests.

I ran a 5-node Swarm cluster for about two years managing ~40 services before migrating to K3s. Swarm handled everything we threw at it and the only reason we moved was that we needed CRDs and the K8s ecosystem for some specific tooling. For a small team that just wants reliable multi-host deployments, Swarm is honestly the path of least resistance.

That said, I'd echo the K3s recommendation if you think you'll eventually need K8s features. The learning curve isn't as bad as full K8s and you get future-proofing. But if you want something working this afternoon, Swarm's your quickest win.

Upvote 2 Downvote Reply Award Share

https://www.reddit.com/user/NiftyLogic/

https://www.reddit.com/r/docker/comments/1rx0zw8/comment/obp1877/

Nomad brings CSI and CNI to the table, which makes networking and storage just so much simpler and more robust.

Tried Swarm once, but it felt too much was lacking for a proper orchestration platform. In the end I settled on Nomad. Simple enough to understand for a hobbyist, while still offering some advanced features from k8s.

Upvote 1 Downvote Reply Award Share

Sh3llSh0cker

https://www.reddit.com/user/Sh3llSh0cker/

https://www.reddit.com/r/docker/comments/1rx0zw8/comment/ob93gzk/

K3s cluster is the move, I'll be adding to my infrastructure/homelab soon a 4 node K3s cluster. I don't do cloud service AWS, Azure, this, that all trash to me and cash grabs.

Upvote 2 Downvote Reply Award Share

https://www.reddit.com/user/l13t/

https://www.reddit.com/r/docker/comments/1rx0zw8/comment/obji4rv/

Running my homelab with Nomad for the last 9 years. I'm happy with it. Especially after they added service discovery and some sort of “secrets” like k8s “secrets”. That helped me to simplify setup and get rid of Consul and Vault. I considered using Nomad for one project at work - unfortunately the general lack of knowledge of cloud in my team (we did migration from on-prem) and lack of resources about Nomad stopped me.

If I'll start some project from scratch, I'll definitely go with Nomad for the start to keep infra simple enough.

P.S. At work for the last 9-10 years I'm using k8s.

Upvote 2 Downvote Reply Award Share

https://www.reddit.com/user/NiftyLogic/

https://www.reddit.com/r/docker/comments/1rx0zw8/comment/obp0phg/

Pretty much the same here. Running Nomad for three years in my homelab now, and I'm pretty happy with it.

Tried k8s before, but it was just too complex for my taste. I would like to understand what's going on in my system, and k8s has just too many moving parts for that if you're just doing it as a hobby.

Really love the orchestration features. Plus Nomad can use CNI and CSI pluging, which makes advanced networking and storage management so much simpler.

Upvote 2 Downvote Reply Award Share

More replies

https://www.reddit.com/r/docker/comments/1rx0zw8/comment/obp0phg/?force-legacy-sct=1

DisastrousPipe8924

https://www.reddit.com/user/DisastrousPipe8924/

https://www.reddit.com/r/docker/comments/1rx0zw8/comment/ob3s4f3/

- Edited 2mo ago

Edit: Before you read the below our team is small, and we manage 12 deployment environments some on AWS, GCP, Azure and even on bare servers. If we didn't pick k8s this would not be possible. We only touch k8s stuff when doing initial onboarding of a new client on-prem, or when architecture changes are needed. K8s is not as hard if you stick to provider defaults instead of trying to cook it from scratch each time.

I honestly dont understand the whole “k8s is hard” argument anymore. We are a team of 11 developers with 2 of us dedicated to ops. Most of the time ops spends is on gitlab ci related issues. K8s has been solid. We only touch it when we want architectural changes.

K8s can be as much of a rabbit hole as you want it to be. Which is probably why people claim “it's hard”. These days most components will be handled by your

but you have the option to swap them out if you want (which I won't recommend unless you've exhausted their provided solutions, and need something more customizable).

#### I recommend two simultaneous approaches:

Setup a cluster to tinker with in your cloud provider

Play around with k3s (it's a local batteries-included implementation of k8s)

Upvote 3 Downvote Reply Award Share

https://www.reddit.com/user/Dangle76/

https://www.reddit.com/r/docker/comments/1rx0zw8/comment/ob3uy93/

They need on prem which with kubernetes can be a heavy thing to manage. They can rely on cloud provider abstractions when they need on prem.

Upvote 2 Downvote Reply Award Share

More replies

https://www.reddit.com/r/docker/comments/1rx0zw8/comment/ob3uy93/?force-legacy-sct=1

Finance\_Potential

https://www.reddit.com/user/Finance\_Potential/

https://www.reddit.com/r/docker/comments/1rx0zw8/comment/ob4f7xr/

K3s solves most of what you're describing. Full K8s API, runs on a single node, and writing manifests by hand isn't as bad a jump from compose as people make it sound. Nomad's BSL license would worry me though, OpenTofu happened for a reason. Pair K3s with Flux and you get GitOps without the overhead of full-fat K8s.

Upvote 2 Downvote Reply Award Share

Minute-Shape-5468

https://www.reddit.com/user/Minute-Shape-5468/

https://www.reddit.com/r/docker/comments/1rx0zw8/comment/ob3mnh6/

We were in a similar spot a while back — small team, loved Compose for local dev, dreaded the K8s overhead. One thing that worked well for us was just sticking with Docker Swarm as an intermediate step. It's built right into Docker, uses almost the same Compose file format (just

docker stack deploy

), and the jump from single-host to multi-host is genuinely pretty painless.

Nomad is solid but the BSL licensing change did make us nervous too. Swarm isn't as feature-rich, but for a handful of services it has almost zero ops overhead and the learning curve is basically flat if you already know Compose. Worth evaluating before committing to either Nomad or K8s — for a lot of small-team use cases it's honestly enough.

Upvote 1 Downvote Reply Award Share

https://www.reddit.com/user/scidu/

https://www.reddit.com/r/docker/comments/1rx0zw8/comment/ob4g1zo/

We are on the

https://www.reddit.com/r/docker/

, i don't know why no one until now recommended just using docker and docker compose for the deploy too. I'm currently managing a few k8s clusters and some others stacks where k8s is not needed, 99% of the use cases a docker compose stack solves the issue. You can use n tools to automate the deploy, or just use the ci/cd pipeline.

Upvote 1 Downvote Reply Award Share

https://www.reddit.com/user/trudesea/

https://www.reddit.com/r/docker/comments/1rx0zw8/comment/ob646k9/

Had the same concerns (and more) about Nomad when architecting a custom IDP for my former employer 5 years ago. Wound up going with GKE. It's definitely a niche tool but in some aspects it's more capable than K8s. It's single binary is nice for maintenance for sure. Now that I am looking for a new job, I've only seen (and interviewed) for one company that uses Nomad for production workloads. All the rest have been K8s.

Honestly, if I were you I would take a couple days and eval it, especially if you use other Hashicorp stuff as it integrates very well.

Upvote 1 Downvote Reply Award Share

https://www.reddit.com/user/Gerbils21/

https://www.reddit.com/r/docker/comments/1rx0zw8/comment/obctxut/

There is very little documentation on nomad. It's always a pain to debug failures.

Upvote 1 Downvote Reply Award Share

wasted\_in\_ynui

https://www.reddit.com/user/wasted\_in\_ynui/

https://www.reddit.com/r/docker/comments/1rx0zw8/comment/obf6fw3/

For the last three years I have been the only ops developer supporting 24+ nomad clusters across many clients most with at least 2 environments. Many of these in single server/client mode, we mostly run Django/nextjs and a few php setups. It's very reliable and easy to upgrade, essentially single binary with some config. We generally run it on ec2 instances with trafeik as load balancer using docker labels for routing config. Having the nomad ui is so handy for giving devs access to exec into containers to debug and run one off tasks or investigate logs We have the ability to add new nodes to a cluster manually or dynamically with autoscaling with preconfigured amis. I love the canary deployments. Make sure you setup a grafana cluster with loki/mimir to capture all your logs and metrics. Good luck

Upvote 1 Downvote Reply Award Share

New to Reddit?

Create your account and connect with a world of communities.

Continue with Email

https://www.reddit.com/register/

Continue with Phone Number

https://www.reddit.com/login/

By continuing, you agree to our

User Agreement

https://www.redditinc.com/policies/user-agreement

and acknowledge that you understand the

Privacy Policy

https://www.redditinc.com/policies/privacy-policy

Related Answers Section

Related Answers

Comparison of Nomad and Kubernetes

https://www.reddit.com/answers/5ddc1b98-14a7-4580-bd6c-2a6519489755/?q=Comparison+of+Nomad+and+Kubernetes&source=PDP

Packer versus Nomad comparison

https://www.reddit.com/answers/cc2daee4-a7ec-4951-91db-ad7bb5ddd948/?q=Packer+versus+Nomad+comparison&source=PDP

Consul versus Nomad comparison

https://www.reddit.com/answers/ae680634-2283-45a5-94b8-00b2502bd76e/?q=Consul+versus+Nomad+comparison&source=PDP

Terraform versus Nomad comparison

https://www.reddit.com/answers/2d0f691e-aab7-4a7d-91e9-739d3daab276/?q=Terraform+versus+Nomad+comparison&source=PDP

Nomad experiences and reviews

https://www.reddit.com/answers/c9c77694-3422-4f28-a338-c16b3e44e53a/?q=Nomad+experiences+and+reviews&source=PDP

Migrate from Kubernetes to Nomad

https://www.reddit.com/r/kubernetes/comments/1qmgmjs/migrate\_from\_kubernetes\_to\_nomad/

r/kubernetes

https://www.reddit.com/r/kubernetes/

- 4mo ago \[

Migrate from Kubernetes to Nomad

\](https://www.reddit.com/r/kubernetes/comments/1qmgmjs/migrate\_from\_kubernetes\_to\_nomad/) 43 upvotes · 70 comments

Daedream vs Hoocrates?

https://www.reddit.com/r/Palworld/comments/1qyszvl/daedream\_vs\_hoocrates/

https://www.reddit.com/r/Palworld/

- 3mo ago \[

Daedream vs Hoocrates?

\](https://www.reddit.com/r/Palworld/comments/1qyszvl/daedream\_vs\_hoocrates/) 4 upvotes · 2 comments

Is there an app that will give me a clickable overview of all my containers and their ports?

https://www.reddit.com/r/docker/comments/1t9m71g/is\_there\_an\_app\_that\_will\_give\_me\_a\_clickable/

https://www.reddit.com/r/docker/

Is there an app that will give me a clickable overview of all my containers and their ports?

\](https://www.reddit.com/r/docker/comments/1t9m71g/is\_there\_an\_app\_that\_will\_give\_me\_a\_clickable/) 23 upvotes · 29 comments

Docker Desktop is a nightmare — never using it again!

https://www.reddit.com/r/docker/comments/1o5wnp2/docker\_desktop\_is\_a\_nightmare\_never\_using\_it\_again/

https://www.reddit.com/r/docker/

- 7mo ago \[

Docker Desktop is a nightmare — never using it again!

\](https://www.reddit.com/r/docker/comments/1o5wnp2/docker\_desktop\_is\_a\_nightmare\_never\_using\_it\_again/) 9 comments

Help. I am addicted to Docker.

https://www.reddit.com/r/docker/comments/1n4hkfe/help\_i\_am\_addicted\_to\_docker/

https://www.reddit.com/r/docker/

- 9mo ago \[

Help. I am addicted to Docker.

\](https://www.reddit.com/r/docker/comments/1n4hkfe/help\_i\_am\_addicted\_to\_docker/) 189 upvotes · 106 comments

Which platform are you using to deploy your dockerized apps ?

https://www.reddit.com/r/docker/comments/1n9u5xf/which\_platform\_are\_you\_using\_to\_deploy\_your/

https://www.reddit.com/r/docker/

- 8mo ago \[

Which platform are you using to deploy your dockerized apps ?

\](https://www.reddit.com/r/docker/comments/1n9u5xf/which\_platform\_are\_you\_using\_to\_deploy\_your/) 19 upvotes · 74 comments

Rootless docker has become easy

https://www.reddit.com/r/docker/comments/1o0sv41/rootless\_docker\_has\_become\_easy/

https://www.reddit.com/r/docker/

- 7mo ago \[

Rootless docker has become easy

\](https://www.reddit.com/r/docker/comments/1o0sv41/rootless\_docker\_has\_become\_easy/) 125 upvotes · 55 comments

I made an Android app to manage my Docker containers on the go

https://www.reddit.com/r/docker/comments/1omovfs/i\_made\_an\_android\_app\_to\_manage\_my\_docker/

https://www.reddit.com/r/docker/

- 7mo ago \[

I made an Android app to manage my Docker containers on the go

\](https://www.reddit.com/r/docker/comments/1omovfs/i\_made\_an\_android\_app\_to\_manage\_my\_docker/) 39 upvotes · 66 comments

Why Is Nobody Talking About Docker Swarm?

https://www.reddit.com/r/docker/comments/1m3swyh/why\_is\_nobody\_talking\_about\_docker\_swarm/

https://www.reddit.com/r/docker/

- 10mo ago \[

Why Is Nobody Talking About Docker Swarm?

\](https://www.reddit.com/r/docker/comments/1m3swyh/why\_is\_nobody\_talking\_about\_docker\_swarm/) 228 upvotes · 169 comments

Trying to simplify container setups

https://www.reddit.com/r/docker/comments/1p68ar1/trying\_to\_simplify\_container\_setups/

https://www.reddit.com/r/docker/

- 6mo ago \[

Trying to simplify container setups

\](https://www.reddit.com/r/docker/comments/1p68ar1/trying\_to\_simplify\_container\_setups/) 96 upvotes · 20 comments

Black Swan or Hysilens for a DoT team ?

https://www.reddit.com/r/JiaoqiuMainsHSR/comments/1qxhkkz/black\_swan\_or\_hysilens\_for\_a\_dot\_team/

r/JiaoqiuMainsHSR

https://www.reddit.com/r/JiaoqiuMainsHSR/

- 3mo ago \[

Black Swan or Hysilens for a DoT team ?

\](https://www.reddit.com/r/JiaoqiuMainsHSR/comments/1qxhkkz/black\_swan\_or\_hysilens\_for\_a\_dot\_team/) 4 upvotes · 11 comments

Small static webhosting image?

https://www.reddit.com/r/docker/comments/1mt2wwz/small\_static\_webhosting\_image/

https://www.reddit.com/r/docker/

- 9mo ago \[

Small static webhosting image?

\](https://www.reddit.com/r/docker/comments/1mt2wwz/small\_static\_webhosting\_image/) 8 upvotes · 20 comments

Bring Animus - Harbinger back?

https://www.reddit.com/r/MobileGaming/comments/1qtrfbz/bring\_animus\_harbinger\_back/

r/MobileGaming

https://www.reddit.com/r/MobileGaming/

- 4mo ago \[

Bring Animus - Harbinger back?

\](https://www.reddit.com/r/MobileGaming/comments/1qtrfbz/bring\_animus\_harbinger\_back/) 1 upvote

What is the biggest docker swarm that you have seen?

https://www.reddit.com/r/docker/comments/1o7bt0h/what\_is\_the\_biggest\_docker\_swarm\_that\_you\_have/

https://www.reddit.com/r/docker/

- 7mo ago \[

What is the biggest docker swarm that you have seen?

\](https://www.reddit.com/r/docker/comments/1o7bt0h/what\_is\_the\_biggest\_docker\_swarm\_that\_you\_have/) 81 upvotes · 45 comments

Docker on Windows

https://www.reddit.com/r/docker/comments/1t483jl/docker\_on\_windows/

https://www.reddit.com/r/docker/

- 14d ago \[

Docker on Windows

\](https://www.reddit.com/r/docker/comments/1t483jl/docker\_on\_windows/) 33 upvotes · 50 comments

Mahoraga Vs. Doomsday (both start at base. ie; not adapted to anything yet)

https://www.reddit.com/r/JujutsuPowerScaling/comments/1q2b0t8/mahoraga\_vs\_doomsday\_both\_start\_at\_base\_ie\_not/

r/JujutsuPowerScaling

https://www.reddit.com/r/JujutsuPowerScaling/

- 5mo ago \[

Mahoraga Vs. Doomsday (both start at base. ie; not adapted to anything yet)

\](https://www.reddit.com/r/JujutsuPowerScaling/comments/1q2b0t8/mahoraga\_vs\_doomsday\_both\_start\_at\_base\_ie\_not/)

2 2 upvotes · 39 comments

Yet another Lens / Kubernetes Dashboard alternative

https://www.reddit.com/r/devops/comments/1qqk10r/yet\_another\_lens\_kubernetes\_dashboard\_alternative/

https://www.reddit.com/r/devops/

- 4mo ago \[

Yet another Lens / Kubernetes Dashboard alternative

\](https://www.reddit.com/r/devops/comments/1qqk10r/yet\_another\_lens\_kubernetes\_dashboard\_alternative/) 21 upvotes · 20 comments

Migrate from Portainer to Dockhand

https://www.reddit.com/r/docker/comments/1qib1uo/migrate\_from\_portainer\_to\_dockhand/

https://www.reddit.com/r/docker/

- 4mo ago \[

Migrate from Portainer to Dockhand

\](https://www.reddit.com/r/docker/comments/1qib1uo/migrate\_from\_portainer\_to\_dockhand/) 7 upvotes · 16 comments

Malekith viability?

https://www.reddit.com/r/MarvelCrisisProtocol/comments/1q6xif4/malekith\_viability/

r/MarvelCrisisProtocol

https://www.reddit.com/r/MarvelCrisisProtocol/

- 4mo ago \[

Malekith viability?

\](https://www.reddit.com/r/MarvelCrisisProtocol/comments/1q6xif4/malekith\_viability/) 8 upvotes · 11 comments

One terminal view for all my containers across all my servers (OT)

https://www.reddit.com/r/docker/comments/1tb3fh3/one\_terminal\_view\_for\_all\_my\_containers\_across/

https://www.reddit.com/r/docker/

One terminal view for all my containers across all my servers (OT)

\](https://www.reddit.com/r/docker/comments/1tb3fh3/one\_terminal\_view\_for\_all\_my\_containers\_across/) 26 upvotes · 14 comments

Zerg build order to counter Hellion/Cyclone?

https://www.reddit.com/r/starcraft/comments/1qibrjq/zerg\_build\_order\_to\_counter\_hellioncyclone/

r/starcraft

https://www.reddit.com/r/starcraft/

- 4mo ago \[

Zerg build order to counter Hellion/Cyclone?

\](https://www.reddit.com/r/starcraft/comments/1qibrjq/zerg\_build\_order\_to\_counter\_hellioncyclone/) 6 upvotes · 14 comments

Dworgyns vs Novus in wallaru

https://www.reddit.com/r/Wizard101/comments/1q4v3xk/dworgyns\_vs\_novus\_in\_wallaru/

r/Wizard101

https://www.reddit.com/r/Wizard101/

- 4mo ago \[

Dworgyns vs Novus in wallaru

\](https://www.reddit.com/r/Wizard101/comments/1q4v3xk/dworgyns\_vs\_novus\_in\_wallaru/) 5 upvotes · 3 comments

Oura vs RingConn?

https://www.reddit.com/r/FitnessTrackers/comments/1rqvlgh/oura\_vs\_ringconn/

r/FitnessTrackers

https://www.reddit.com/r/FitnessTrackers/

- 2mo ago \[

Oura vs RingConn?

\](https://www.reddit.com/r/FitnessTrackers/comments/1rqvlgh/oura\_vs\_ringconn/) 1 upvote · 6 comments

Amanamu Void Shadow Nerfed?

https://www.reddit.com/r/PathOfExile2/comments/1qdw2ne/amanamu\_void\_shadow\_nerfed/

r/PathOfExile2

https://www.reddit.com/r/PathOfExile2/

- 4mo ago \[

Amanamu Void Shadow Nerfed?

\](https://www.reddit.com/r/PathOfExile2/comments/1qdw2ne/amanamu\_void\_shadow\_nerfed/) 11 comments

Is this Hynix A die?

https://www.reddit.com/r/overclocking/comments/1rupnrd/is\_this\_hynix\_a\_die/

r/overclocking

https://www.reddit.com/r/overclocking/

- 2mo ago \[

Is this Hynix A die?

\](https://www.reddit.com/r/overclocking/comments/1rupnrd/is\_this\_hynix\_a\_die/)

View Post in

https://www.reddit.com/r/docker/comments/1rx0zw8/nomad\_vs\_kubernetes/?tl=ja

https://www.reddit.com/r/docker/comments/1rx0zw8/nomad\_vs\_kubernetes/?tl=zh-hans

https://www.reddit.com/r/docker/comments/1rx0zw8/nomad\_vs\_kubernetes/?tl=fr

Português (Brasil)

https://www.reddit.com/r/docker/comments/1rx0zw8/nomad\_vs\_kubernetes/?tl=pt-br

https://www.reddit.com/r/docker/comments/1rx0zw8/nomad\_vs\_kubernetes/?tl=hi

See more See fewer

https://www.reddit.com/r/docker/comments/1rx0zw8/nomad\_vs\_kubernetes/?tl=de

https://www.reddit.com/r/docker/comments/1rx0zw8/nomad\_vs\_kubernetes/?tl=it

https://www.reddit.com/r/docker/comments/1rx0zw8/nomad\_vs\_kubernetes/?tl=ar

https://www.reddit.com/r/docker/comments/1rx0zw8/nomad\_vs\_kubernetes/?tl=th

https://www.reddit.com/r/docker/comments/1rx0zw8/nomad\_vs\_kubernetes/?tl=fil

https://www.reddit.com/r/docker/comments/1rx0zw8/nomad\_vs\_kubernetes/?tl=sv

Español (Latinoamérica)

https://www.reddit.com/r/docker/comments/1rx0zw8/nomad\_vs\_kubernetes/?tl=es-419

Community Info Section

https://www.reddit.com/r/docker/

Docker: An open source project to pack, ship and run any application as a lightweight containers

Docker is an open-source project to easily create lightweight, portable, self-sufficient containers from any application. The same container that a developer builds and tests on a laptop can run at scale, in production, on VMs, bare metal, OpenStack clusters, public clouds and more.

Anyone can view, post, and comment to this community

Reddit Rules

https://www.redditinc.com/policies/content-policy

Privacy Policy

https://www.reddit.com/policies/privacy-policy

User Agreement

https://www.redditinc.com/policies/user-agreement

Your Privacy Choices

https://support.reddithelp.com/hc/articles/43980704794004

Accessibility

https://support.reddithelp.com/hc/sections/38303584022676-Accessibility

Reddit, Inc. © 2026. All rights reserved.

https://redditinc.com/

Expand Navigation

Expand Navigation

Collapse Navigation

Collapse Navigation

0cAFcWeA6ZP5J\_zbgHF-O1TOqGur3RVhzBebY\_ZDnDQDD0ryv\_A6Bm-ZV23V3gecAWzQFq3omF2wmbGa3fKf9XqmLzmcD\_BWcRm63RxTNDVmro\_JUULJK27ELh085pYD90rhC5SISo5UsXeBbnOEwkxP8jBV3wfM-L7e0uYWzgNB5mf2\_mojZc7w44HkC2J6eZIbj-9cH6L-iWRU8trZJIAp6rNWaYKFiPYpPj4-kZrxb1SNdya6QZst9eC6c1aWHNw6LauCMHf3aZoB\_2JzFCl2o3GzHsjjlthJulWcX8GOHmCAGTvtZossGmHSVPZg\_8yW8nYyTWOYQxHdZ0GfRi5IEmsPH5SN4iQ98nB-u4Hc0o4txhhwm\_wB3HqwtoLh4PxZIPrQyIY5PSPlLni4J2eBBaf\_RH6MCvsfV4SQLfKv-aLrPlXTBsPE8Oe9IvOSxjlaT6qfZiqRo5goj78QHE0bomSuP\_NAwYvbC8T0pdGe59ywhijtnljbCzFa7WX6P5rc6CgZLIFRcpqMngzx6rI6LnFazkT2Sws3DntP9V81Qqr5FvXw1Z3E6E1v5c8opPzVaNF6LCuUjK7CjyhjX9D0zmENio\_qderm5o2OEwuCGLShvNWWpcjL05t9sQRMe2O6E5SI5OQ6gpxdTB3XkT7oVEmQlGvcvTkv-H3d-N4NG1xmpaup0GduGwS86ISFR1rWIRlGojUK1zEV829lVZhsF-kYf-UixLIrmMWQuZ3vefXU\_XsD5rvH\_e6bFhwnwEMOCmf39jqg4Drg7rm4Je6PJQJKS4nVN2FXziwwmktYfza5-9ulzHtxnNrM2vA0FJoLyKzzLokEo2ADeVFL5EFWfco0pUUZ52b2yHkH9MjDT\_0qcFCTAdk3DgEyjPTpdkG5XRXr5xADMkexrSTz0RlK8MTOKp\_TUF6aiqjVVnC03SSZvj3t-05E8HP2EgSZDCiWkBt2CttsPnVHxEDTRlc\_DXMWp6qTMHJpRl0rUiOmJTaiUsrG6Vaxxy2zikelSg6cD9zZjjvWuhp2JKWsIKFKGd3N\_D4QsAZKy0AcXp2N-U\_KVurVqtAOgrqagFA8ibEZjadlt7HiXj\_zkN3j624ra-Hx-2KzwIbLNgPZVLlCOp4v1xOEKg214qTBHLQr1ST3TFzYlWhOOlYg9Jy9yEQSu2k\_orwW-Sc-TLMNF6Nhf-8cHj8qQteJP345JOy7V1MlfX-4f80nsEzVXay5n3\_NoueVGgbJnKxkcTNc2Dfps2-o9FeoCp5Txk1GWDO9fpqHqfh2ZSFIlTfkpp-WybgR4eR0Sq4aZE7PL\_w4mR587Givu5enbm7DtNhu2r1dozK7kyXkXlkkP7LGbRVPlwoFCNRwsl9V39FLCl5accz9sOfrluu\_Oc-OvWU8THzZmN1iAQoj0VM9Rt0JKxnrll2W6EG92lzy4f1YtpDFRXtfPmGf3GeMRmXoEcwj7ApNRczIBlSrisgG5oLZTZUCqu5RIwTS01GkOAZxLyBCfGxI7\_ptw6CCCOINGKGVQJiCOAz-v1GandVGtqZ3hUKIzbx1Cp2VDpEdERd4F2YxrF0NK55gu45i9Ys7nIM\_ZEbw5hIMFznwxxAoz6S8gIHXOHXuUy8mIrDCtRotsVCnV-fm45TpD1Ygc5nVsAJ8Yi-a\_giq11PRXeeV2f7f1ZFZp2S8ryYwFP2Sj9QKSFhY0Rd3sAcmv4KZXRXz91ltiY7iGaLZSi0ypcllhE6f2aRcvP5RrhIZ1ycPsj199L9jXZrJIMRYkffjJzHCCnaJ7mYoyc1roFrYtjktg\_yY15boVmIj9xXLSEuetlEm-z9FZio9uUeg2W2iZjow48mcOHZH9g\_qEHlZ0sxrkgVa6eZUN7QLHpAR4IPj5YGDG0BgKFdiDTdoBX9eu\_r8bl92-6PJQVN84uf88HqsONmOXWt593dj5k3d8BPFhs9aKrscbD5Sp4s653V3pkJCEz3PcJos9dJZPmfTU5iFBsdSoPSXi9c999VziXHYdB9Qoyl1w-jQSCfFgm\_Uq8W-kk\_-6Adw1bOqWXWSoOfTDyvNuxe0vzlx7K96AWnVXWpjeD7ON-9fgQVMpvq6cHlcLPM967Wf3AtS5tA\_AraznP\_1kA\_02zU61tK839131mgtdUUoTgNCR9DmM379wV6\_7a-42EVBmKh8ZNqErAl39orS1xm38EDalDTrhSVfxtmUdJTWTU1aV51X\_t2WPr3mA

