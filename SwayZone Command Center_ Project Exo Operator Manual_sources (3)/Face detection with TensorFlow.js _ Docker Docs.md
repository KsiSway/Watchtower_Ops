---
sourceFile: "Face detection with TensorFlow.js | Docker Docs"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.408Z"
---

# Face detection with TensorFlow.js | Docker Docs

747870c9-6c21-4a56-b95c-30aac3a5b660

Face detection with TensorFlow.js | Docker Docs

be61951f-2a43-415e-96b6-016765bada9d

https://docs.docker.com/guides/tensorflowjs/

Face detection with TensorFlow.js | Docker Docs

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

Face detection with TensorFlow.js

https://docs.docker.com/guides/tensorflowjs/

This guide explains how to run TensorFlow.js in Docker containers.

JavaScript AI

« Back to all guides

https://docs.docker.com/guides/

https://docs.docker.com/

https://docs.docker.com/guides/

/ Face detection with TensorFlow.js

Face detection with TensorFlow.js

Ask Gordon Copy Markdown View Markdown

Table of contents

Prerequisites

https://docs.docker.com/guides/tensorflowjs/#prerequisites

What is TensorFlow.js?

https://docs.docker.com/guides/tensorflowjs/#what-is-tensorflowjs

Why Use TensorFlow.js and Docker together?

https://docs.docker.com/guides/tensorflowjs/#why-use-tensorflowjs-and-docker-together

Get and run the sample application

https://docs.docker.com/guides/tensorflowjs/#get-and-run-the-sample-application

About the application

https://docs.docker.com/guides/tensorflowjs/#about-the-application

https://docs.docker.com/guides/tensorflowjs/#wasm

https://docs.docker.com/guides/tensorflowjs/#webgl

https://docs.docker.com/guides/tensorflowjs/#cpu

Explore the application's code

https://docs.docker.com/guides/tensorflowjs/#explore-the-applications-code

The index.html file

https://docs.docker.com/guides/tensorflowjs/#the-indexhtml-file

The index.js file

https://docs.docker.com/guides/tensorflowjs/#the-indexjs-file

The tf-backend-wasm.js file

https://docs.docker.com/guides/tensorflowjs/#the-tf-backend-wasmjs-file

The tfjs-backend-wasm-simd.wasm file

https://docs.docker.com/guides/tensorflowjs/#the-tfjs-backend-wasm-simdwasm-file

Explore the Dockerfile

https://docs.docker.com/guides/tensorflowjs/#explore-the-dockerfile

Develop with Compose

https://docs.docker.com/guides/tensorflowjs/#develop-with-compose

Share your image

https://docs.docker.com/guides/tensorflowjs/#share-your-image

https://docs.docker.com/guides/tensorflowjs/#summary

This guide introduces the seamless integration of TensorFlow.js with Docker to perform face detection. In this guide, you'll explore how to:

Run a containerized TensorFlow.js application using Docker.

Implement face detection in a web application with TensorFlow.js.

Construct a Dockerfile for a TensorFlow.js web application.

Use Docker Compose for real-time application development and updates.

Share your Docker image on Docker Hub to facilitate deployment and extend reach.

Acknowledgment

Docker would like to thank

Harsh Manvar

https://github.com/harsh4870

for his contribution to this guide.

Prerequisites

https://docs.docker.com/guides/tensorflowjs/#prerequisites

You have installed the latest version of

Docker Desktop

https://docs.docker.com/get-started/get-docker/

https://git-scm.com/downloads

. The examples in this guide use a command-line based Git client, but you can use any client.

What is TensorFlow.js?

https://docs.docker.com/guides/tensorflowjs/#what-is-tensorflowjs

TensorFlow.js

https://www.tensorflow.org/js

is an open-source JavaScript library for machine learning that enables you to train and deploy ML models in the browser or on Node.js. It supports creating new models from scratch or using pre-trained models, facilitating a wide range of ML applications directly in web environments. TensorFlow.js offers efficient computation, making sophisticated ML tasks accessible to web developers without deep ML expertise.

Why Use TensorFlow.js and Docker together?

https://docs.docker.com/guides/tensorflowjs/#why-use-tensorflowjs-and-docker-together

Environment consistency and simplified deployment: Docker packages TensorFlow.js applications and their dependencies into containers, ensuring consistent runs across all environments and simplifying deployment.

Efficient development and easy scaling: Docker enhances development efficiency with features like hot reloading and facilitates easy scaling of - TensorFlow.js applications using orchestration tools like Kubernetes.

Isolation and enhanced security: Docker isolates TensorFlow.js applications in secure environments, minimizing conflicts and security vulnerabilities while running applications with limited permissions.

Get and run the sample application

https://docs.docker.com/guides/tensorflowjs/#get-and-run-the-sample-application

In a terminal, clone the sample application using the following command.

$ git clone https://github.com/harsh4870/TensorJS-Face-Detection

After cloning the application, you'll notice the application has a

. This Dockerfile lets you build and run the application locally with nothing more than Docker.

Before you run the application as a container, you must build it into an image. Run the following command inside the

TensorJS-Face-Detection

directory to build an image named

face-detection-tensorjs

$ docker build -t face-detection-tensorjs .

The command builds the application into an image. Depending on your network connection, it can take several minutes to download the necessary components the first time you run the command.

To run the image as a container, run the following command in a terminal.

$ docker run -p 80:80 face-detection-tensorjs

The command runs the container and maps port 80 in the container to port 80 on your system.

Once the application is running, open a web browser and access the application at

http://localhost:80

http://localhost:80

. You may need to grant access to your webcam for the application.

#### In the web application, you can change the backend to use one of the following:

To stop the application, press

in the terminal.

About the application

https://docs.docker.com/guides/tensorflowjs/#about-the-application

The sample application performs real-time face detection using

https://developers.google.com/mediapipe/

, a comprehensive framework for building multimodal machine learning pipelines. It's specifically using the BlazeFace model, a lightweight model for detecting faces in images.

In the context of TensorFlow.js or similar web-based machine learning frameworks, the WASM, WebGL, and CPU backends can be used to execute operations. Each of these backends utilizes different resources and technologies available in modern browsers and has its strengths and limitations. The following sections are a brief breakdown of the different backends.

https://docs.docker.com/guides/tensorflowjs/#wasm

WebAssembly (WASM) is a low-level, assembly-like language with a compact binary format that runs at near-native speed in web browsers. It allows code written in languages like C/C++ to be compiled into a binary that can be executed in the browser.

It's a good choice when high performance is required, and either the WebGL backend is not supported or you want consistent performance across all devices without relying on the GPU.

https://docs.docker.com/guides/tensorflowjs/#webgl

WebGL is a browser API that allows for GPU-accelerated usage of physics and image processing and effects as part of the web page canvas.

WebGL is well-suited for operations that are parallelizable and can significantly benefit from GPU acceleration, such as matrix multiplications and convolutions commonly found in deep learning models.

https://docs.docker.com/guides/tensorflowjs/#cpu

The CPU backend uses pure JavaScript execution, utilizing the device's central processing unit (CPU). This backend is the most universally compatible and serves as a fallback when neither WebGL nor WASM backends are available or suitable.

Explore the application's code

https://docs.docker.com/guides/tensorflowjs/#explore-the-applications-code

Explore the purpose of each file and their contents in the following sections.

The index.html file

https://docs.docker.com/guides/tensorflowjs/#the-indexhtml-file

file serves as the frontend for the web application that utilizes TensorFlow.js for real-time face detection from the webcam video feed. It incorporates several technologies and libraries to facilitate machine learning directly in the browser. It uses several TensorFlow.js libraries, including:

tfjs-core and tfjs-converter for core TensorFlow.js functionality and model conversion.

tfjs-backend-webgl, tfjs-backend-cpu, and the tf-backend-wasm script for different computational backend options that TensorFlow.js can use for processing. These backends allow the application to perform machine learning tasks efficiently by leveraging the user's hardware capabilities.

The BlazeFace library, a TensorFlow model for face detection.

#### It also uses the following additional libraries:

dat.GUI for creating a graphical interface to interact with the application's settings in real-time, such as switching between TensorFlow.js backends.

Stats.min.js for displaying performance metrics (like FPS) to monitor the application's efficiency during operation.

<style>
  body {
    margin: 25px;
  }

  .true {
    color: green;
  }

  .false {
    color: red;
  }

  #main {
    position: relative;
    margin: 50px 0;
  }

  canvas {
    position: absolute;
    top: 0;
    left: 0;
  }

  #description {
    margin-top: 20px;
    width: 600px;
  }

  #description-title {
    font-weight: bold;
    font-size: 18px;
  }
</style>

<body>
  <div id="main">
    <video
      id="video"
      playsinline
      style="
      -webkit-transform: scaleX(-1);
      transform: scaleX(-1);
      width: auto;
      height: auto;
      "
    ></video>
    <canvas id="output"></canvas>
    <video
      id="video"
      playsinline
      style="
      -webkit-transform: scaleX(-1);
      transform: scaleX(-1);
      visibility: hidden;
      width: auto;
      height: auto;
      "
    ></video>
  </div>
</body>
<script src="https://unpkg.com/@tensorflow/tfjs-core@2.1.0/dist/tf-core.js"></script>
<script src="https://unpkg.com/@tensorflow/tfjs-converter@2.1.0/dist/tf-converter.js"></script>

<script src="https://unpkg.com/@tensorflow/tfjs-backend-webgl@2.1.0/dist/tf-backend-webgl.js"></script>
<script src="https://unpkg.com/@tensorflow/tfjs-backend-cpu@2.1.0/dist/tf-backend-cpu.js"></script>
<script src="./tf-backend-wasm.js"></script>

<script src="https://unpkg.com/@tensorflow-models/blazeface@0.0.5/dist/blazeface.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/dat-gui/0.7.6/dat.gui.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/stats.js/r16/Stats.min.js"></script>
<script src="./index.js"></script>

The index.js file

https://docs.docker.com/guides/tensorflowjs/#the-indexjs-file

file conducts the facial detection logic. It demonstrates several advanced concepts in web development and machine learning integration. Here's a breakdown of some of its key components and functionalities:

Stats.js: The script starts by creating a Stats instance to monitor and display the frame rate (FPS) of the application in real time. This is helpful for performance analysis, especially when testing the impact of different TensorFlow.js backends on the application's speed.

TensorFlow.js: The application allows users to switch between different computation backends (wasm, webgl, and cpu) for TensorFlow.js through a graphical interface provided by dat.GUI. Changing the backend can affect performance and compatibility depending on the device and browser. The addFlagLabels function dynamically checks and displays whether SIMD (Single Instruction, Multiple Data) and multithreading are supported, which are relevant for performance optimization in the wasm backend.

setupCamera function: Initializes the user's webcam using the MediaDevices Web API. It configures the video stream to not include audio and to use the front-facing camera (facingMode: 'user'). Once the video metadata is loaded, it resolves a promise with the video element, which is then used for face detection.

BlazeFace: The core of this application is the renderPrediction function, which performs real-time face detection using the BlazeFace model, a lightweight model for detecting faces in images. The function calls model.estimateFaces on each animation frame to detect faces from the video feed. For each detected face, it draws a red rectangle around the face and blue dots for facial landmarks on a canvas overlaying the video.

const stats = new Stats();
stats.showPanel(0);
document.body.prepend(stats.domElement);

let model, ctx, videoWidth, videoHeight, video, canvas;

const state = {
  backend: "wasm",
};

const gui = new dat.GUI();
gui
  .add(state, "backend", \["wasm", "webgl", "cpu"\])
  .onChange(async (backend) => {
    await tf.setBackend(backend);
    addFlagLabels();
  });

async function addFlagLabels() {
  if (!document.querySelector("#simd\_supported")) {
    const simdSupportLabel = document.createElement("div");
    simdSupportLabel.id = "simd\_supported";
    simdSupportLabel.style = "font-weight: bold";
    const simdSupported = await tf.env().getAsync("WASM\_HAS\_SIMD\_SUPPORT");
    simdSupportLabel.innerHTML = \`SIMD supported: <span class=${simdSupported}>${simdSupported}<span>\`;
    document.querySelector("#description").appendChild(simdSupportLabel);
  }

  if (!document.querySelector("#threads\_supported")) {
    const threadSupportLabel = document.createElement("div");
    threadSupportLabel.id = "threads\_supported";
    threadSupportLabel.style = "font-weight: bold";
    const threadsSupported = await tf
      .env()
      .getAsync("WASM\_HAS\_MULTITHREAD\_SUPPORT");
    threadSupportLabel.innerHTML = \`Threads supported: <span class=${threadsSupported}>${threadsSupported}</span>\`;
    document.querySelector("#description").appendChild(threadSupportLabel);
  }
}

async function setupCamera() {
  video = document.getElementById("video");

  const stream = await navigator.mediaDevices.getUserMedia({
    audio: false,
    video: { facingMode: "user" },
  });
  video.srcObject = stream;

  return new Promise((resolve) => {
    video.onloadedmetadata = () => {
      resolve(video);
    };
  });
}

const renderPrediction = async () => {
  stats.begin();

  const returnTensors = false;
  const flipHorizontal = true;
  const annotateBoxes = true;
  const predictions = await model.estimateFaces(
    video,
    returnTensors,
    flipHorizontal,
    annotateBoxes,
  );

  if (predictions.length > 0) {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    for (let i = 0; i < predictions.length; i++) {
      if (returnTensors) {
        predictions\[i\].topLeft = predictions\[i\].topLeft.arraySync();
        predictions\[i\].bottomRight = predictions\[i\].bottomRight.arraySync();
        if (annotateBoxes) {
          predictions\[i\].landmarks = predictions\[i\].landmarks.arraySync();
        }
      }

      const start = predictions\[i\].topLeft;
      const end = predictions\[i\].bottomRight;
      const size = \[end\[0\] - start\[0\], end\[1\] - start\[1\]\];
      ctx.fillStyle = "rgba(255, 0, 0, 0.5)";
      ctx.fillRect(start\[0\], start\[1\], size\[0\], size\[1\]);

      if (annotateBoxes) {
        const landmarks = predictions\[i\].landmarks;

        ctx.fillStyle = "blue";
        for (let j = 0; j < landmarks.length; j++) {
          const x = landmarks\[j\]\[0\];
          const y = landmarks\[j\]\[1\];
          ctx.fillRect(x, y, 5, 5);
        }
      }
    }
  }

  stats.end();

  requestAnimationFrame(renderPrediction);
};

const setupPage = async () => {
  await tf.setBackend(state.backend);
  addFlagLabels();
  await setupCamera();
  video.play();

  videoWidth = video.videoWidth;
  videoHeight = video.videoHeight;
  video.width = videoWidth;
  video.height = videoHeight;

  canvas = document.getElementById("output");
  canvas.width = videoWidth;
  canvas.height = videoHeight;
  ctx = canvas.getContext("2d");
  ctx.fillStyle = "rgba(255, 0, 0, 0.5)";

  model = await blazeface.load();

  renderPrediction();
};

setupPage();

The tf-backend-wasm.js file

https://docs.docker.com/guides/tensorflowjs/#the-tf-backend-wasmjs-file

tf-backend-wasm.js

file is part of the

TensorFlow.js library

https://github.com/tensorflow/tfjs/tree/master/tfjs-backend-wasm

. It contains initialization logic for the TensorFlow.js WASM backend, some utilities for interacting with the WASM binaries, and functions to set custom paths for the WASM binaries.

The tfjs-backend-wasm-simd.wasm file

https://docs.docker.com/guides/tensorflowjs/#the-tfjs-backend-wasm-simdwasm-file

tfjs-backend-wasm-simd.wasm

file is part of the

TensorFlow.js library

https://github.com/tensorflow/tfjs/tree/master/tfjs-backend-wasm

. It's a WASM binary that's used for the WebAssembly backend, specifically optimized to utilize SIMD (Single Instruction, Multiple Data) instructions.

Explore the Dockerfile

https://docs.docker.com/guides/tensorflowjs/#explore-the-dockerfile

In a Docker-based project, the Dockerfile serves as the foundational asset for building your application's environment.

A Dockerfile is a text file that instructs Docker how to create an image of your application's environment. An image contains everything you want and need when running application, such as files, packages, and tools.

The following is the Dockerfile for this project.

FROM nginx:stable-alpine3.17-slim
WORKDIR /usr/share/nginx/html
COPY . .

This Dockerfile defines an image that serves static content using Nginx from an Alpine Linux base image.

Develop with Compose

https://docs.docker.com/guides/tensorflowjs/#develop-with-compose

Docker Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application's services, networks, and volumes. In this case, the application isn't a multi-container application, but Docker Compose has other useful features for development, like

Compose Watch

https://docs.docker.com/compose/how-tos/file-watch/

The sample application doesn't have a Compose file yet. To create a Compose file, in the

TensorJS-Face-Detection

directory, create a text file named

compose.yaml

and then add the following contents.

services:
  server:
    build:
      context: .
    ports:
      - 80:80
    develop:
      watch:
        - action: sync
          path: .
          target: /usr/share/nginx/html

This Compose file defines a service that is built using the Dockerfile in the same directory. It maps port 80 on the host to port 80 in the container. It also has a

subsection with the

attribute that defines a list of rules that control automatic service updates based on local file changes. For more details about the Compose instructions, see the

Compose file reference

https://docs.docker.com/reference/compose-file/

Save the changes to your

compose.yaml

file and then run the following command to run the application.

$ docker compose watch

Once the application is running, open a web browser and access the application at

http://localhost:80

http://localhost:80

. You may need to grant access to your webcam for the application.

Now you can make changes to the source code and see the changes automatically reflected in the container without having to rebuild and rerun the container.

file and update the landmark points to be green instead of blue on line 83.

-        ctx.fillStyle = "blue";
+        ctx.fillStyle = "green";

Save the changes to the

file and then refresh the browser page. The landmark points should now appear green.

To stop the application, press

in the terminal.

Share your image

https://docs.docker.com/guides/tensorflowjs/#share-your-image

Publishing your Docker image on Docker Hub streamlines deployment processes for others, enabling seamless integration into diverse projects. It also promotes the adoption of your containerized solutions, broadening their impact across the developer ecosystem. To share your image:

https://www.docker.com/pricing?ref=Docs&refAction=DocsGuidesTensorflowjs

or sign in to

https://hub.docker.com/

Rebuild your image to include the changes to your application. This time, prefix the image name with your Docker ID. Docker uses the name to determine which repository to push it to. Open a terminal and run the following command in the

TensorJS-Face-Detection

directory. Replace

YOUR-USER-NAME

with your Docker ID.

$ docker build -t YOUR-USER-NAME/face-detection-tensorjs .

Run the following

docker push

command to push the image to Docker Hub. Replace

YOUR-USER-NAME

with your Docker ID.

$ docker push YOUR-USER-NAME/face-detection-tensorjs

Verify that you pushed the image to Docker Hub.

https://hub.docker.com/

Repositories

Last pushed

time for your repository.

Other users can now download and run your image using the

command. They need to replace

YOUR-USER-NAME

with your Docker ID.

$ docker run -p 80:80 YOUR-USER-NAME/face-detection-tensorjs

https://docs.docker.com/guides/tensorflowjs/#summary

This guide demonstrated leveraging TensorFlow.js and Docker for face detection in web applications. It highlighted the ease of running containerized TensorFlow.js applications, and developing with Docker Compose for real-time code changes. Additionally, it covered how sharing your Docker image on Docker Hub can streamline deployment for others, enhancing the application's reach within the developer community.

#### Related information:

TensorFlow.js website

https://www.tensorflow.org/js

MediaPipe website

https://developers.google.com/mediapipe/

Dockerfile reference

https://docs.docker.com/reference/dockerfile/

Compose file reference

https://docs.docker.com/reference/compose-file/

Docker CLI reference

https://docs.docker.com/reference/cli/docker/

Docker Blog: Accelerating Machine Learning with TensorFlow.js

https://www.docker.com/blog/accelerating-machine-learning-with-tensorflow-js-using-pretrained-models-and-docker/

Edit this page

https://github.com/docker/docs/edit/main/content/guides/tensorflowjs.md

Request changes

https://github.com/docker/docs/issues/new?template=doc\_issue.yml&location=https%3a%2f%2fdocs.docker.com%2fguides%2ftensorflowjs%2f&labels=status%2Ftriage

Table of contents

Prerequisites

https://docs.docker.com/guides/tensorflowjs/#prerequisites

What is TensorFlow.js?

https://docs.docker.com/guides/tensorflowjs/#what-is-tensorflowjs

Why Use TensorFlow.js and Docker together?

https://docs.docker.com/guides/tensorflowjs/#why-use-tensorflowjs-and-docker-together

Get and run the sample application

https://docs.docker.com/guides/tensorflowjs/#get-and-run-the-sample-application

About the application

https://docs.docker.com/guides/tensorflowjs/#about-the-application

https://docs.docker.com/guides/tensorflowjs/#wasm

https://docs.docker.com/guides/tensorflowjs/#webgl

https://docs.docker.com/guides/tensorflowjs/#cpu

Explore the application's code

https://docs.docker.com/guides/tensorflowjs/#explore-the-applications-code

The index.html file

https://docs.docker.com/guides/tensorflowjs/#the-indexhtml-file

The index.js file

https://docs.docker.com/guides/tensorflowjs/#the-indexjs-file

The tf-backend-wasm.js file

https://docs.docker.com/guides/tensorflowjs/#the-tf-backend-wasmjs-file

The tfjs-backend-wasm-simd.wasm file

https://docs.docker.com/guides/tensorflowjs/#the-tfjs-backend-wasm-simdwasm-file

Explore the Dockerfile

https://docs.docker.com/guides/tensorflowjs/#explore-the-dockerfile

Develop with Compose

https://docs.docker.com/guides/tensorflowjs/#develop-with-compose

Share your image

https://docs.docker.com/guides/tensorflowjs/#share-your-image

https://docs.docker.com/guides/tensorflowjs/#summary

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

