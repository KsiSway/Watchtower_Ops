---
sourceFile: "Kubernetes Architecture in 7 minutes | K8s explained"
exportedBy: "Kortex"
exportDate: "2026-05-20T06:50:17.418Z"
---

# Kubernetes Architecture in 7 minutes | K8s explained

45ef7f25-4d0c-461d-b9a6-6451d7060fe7

Kubernetes Architecture in 7 minutes | K8s explained

33a9d0d5-18b7-407c-8ba1-a87752cb2a38

https://www.youtube.com/watch?v=vmCuNJiNzfg

vmCuNJiNzfg

Cloud Champ

in this video I will explain you kubernetes architecture in simplest manner possible we go deep down in the kubernetes cluster understanding different components and how they actually work so make sure you watch this video till the end let's start so we start with creating a cluster you can create a kubernetes cluster locally either using tools like mini Cube or cube ADM optionally you can also use probably cloud provider services like eks and AWS AKs in aure gka in Google Cloud to create kubernetes clusters inside this kubernetes

this cluster we have two different types of machines or as we call them nodes so we have a master node which is responsible to handled everything inside the cluster along with Master node we also have another kind of node known as worker node this worker node is actually responsible to run your application containers inside kubernetes cluster so you have Master node that is when to handle everything inside the cluster and you have worker notes which are responsible to run your application containers

inside the kubernetes cluster let's start with worker nodes and look at different components inside it as we all know worker nodes are responsible to run application containers and they run this application containers inside something known as pods pods are smallest Deployable units in the kubernetes tester and the Pod can hold one or more containers a single worker node can have more than one pods or it can have a single pod as well so these containers are actually running inside object kuet is object known as

pods to deploy and manage pods inside this worker node we have an agent named as cuet this cuet agent is running on all worker nodes and it gets information from the master node to decide where should be the P running and how to manage it along with this for a worker machine to create and manage containers we need to have a container runtime interface or a software like Docker so worker machine will also contain CRI or container Endtime interface such as Docker here other options are container d

locket Etc which is supported by cetes as well also to enable communication between these two ports or to make these pods or application accessible to the Ed users we have another networking component in the worker node which is known as cube proxy qoxy is used for Port toport communication also for load balancing service proxy and to make your application accessible to the end users so these are different components inside the worker nodes you have q proxy for port-to-port communication and

expose your application you have container runtime interface to create and delete containers you have cuet an agent that is running on every worker node which get information from the master node and handle the workloads inside the worker nodes along with this you can have more add-ons or plugins that you install on your worker notes but these are all the important components inside your worker notes now that we have understood the different components inside worker nodes and how they actually work let's look at the different components inside Master node so

so Master node or control plane has four very important components that are responsible to manage everything inside the cluster the first component is the cube API server this Cube API server is like an entry point for everything you do inside the cluster so let's say you are a devops engineer and you want to create a new pod or maybe delete a pod or just get the status if you want to do anything inside cluster you will have to talk to the cube API server so you can talk to cube API server either by running commands using Cube CTL command line tool either using

Cube uh Cube it is dashboard or maybe using sdks or anything so you will talk to the cube API server Cube API server will validate if the request is okay if the user is authenticated or not and if it works then it will get the information from the other components and provide it to the end user or to the dev optionor so API server is like an entry point which validates the request and also authenticates the user next Master node component is the scheduler scheduler is used to assign pods

to the worker nodes let's say you made a request to the API server to create a new pod scheder is going to check which nodes have enough capacity to launch this new pod once the nodes on which the pods are going to be run is decided by the scheduler scheduler provides this information to the cube API server Cube API server gives this information to the cubet running on that particular node and thus it creates the new pod on the worker note so scheder is used to assign pods on the notes based on

resource capacity all the Manifest files that you have defined for your cluster now what if there's an issue inside the cluster or one of these ports shows an error or gets deleted that's when the next kubernetes Master node components comes into play so next kubernetes component is the controller manager controller manager is used to monitor the entire cluster and it makes sures that everything is as you have defined inside your manifested files so let's say you have said you want to have four pods running it will make sure that the four pods are running all the times if

that's not the case it'll tell API server which will recreate the P following the same procedure with the scheduler first decides what nodes to create the pods on then gives the information to API server and then cuade creates it so controller manager is used to Monitor and make sure everything is working as you have defined and it does that by comparing the desired state with the actual state of the cluster but where is this cluster information or cluster data stored it is stored inside the new it is stored inside the next Master node component which is hcd

hcd is a key value store that stores all the information about the cluster what application is running what pods are running on which nodes and everything else one thing to note is hcd can only talk to the cube API server so if you want to get any information from the hcd it has to be through the cube API server so you can see Cube API server is like a center of communication for every component inside the master node as well as to the CET which is running on the worker node so this is the kubernetes architecture we have

Master node and the worker node Master node is responsible for handling workloads inside the cluster worker nodes are actually running the application workloads here inside worker node we have the parts which is the smallest unit responsible to run the application container we have cuate and agent which is going to run on all the worker nodes and also responsible to create pods next we have con the runtime interface and we also have q proxy for networking and for exposing our application inside Master node we have QBE API server which is the entry point and the authentic

ation system for every request that you make it also exposes a kubernetes API for the end user to start using it next component is a scheder which is used to assign ports to the notes then we have controller manager that makes sure everything is working as you want or as you have desired and all the cluster information is stored inside hcd so so this is a simplified explanation on ku's architecture I hope this video was informative if you have any questions any doubt do let me know in the comment section and for more information I would recommend checking out my another video

which explains what is kubernetes and how it actually works do check it out thank you and have a good day

