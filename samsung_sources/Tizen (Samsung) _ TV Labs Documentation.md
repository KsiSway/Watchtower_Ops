---
sourceFile: "Tizen (Samsung) | TV Labs Documentation"
exportedBy: "Kortex"
exportDate: "2026-05-20T06:50:17.531Z"
---

# Tizen (Samsung) | TV Labs Documentation

7b814d40-9560-4668-b691-c55ef33e05db

Tizen (Samsung) | TV Labs Documentation

0e29501d-5c97-4363-95c8-a402955907ff

https://docs.tvlabs.ai/platform/platforms/tizen

Tizen (Samsung) | TV Labs Documentation

Skip to main content

https://docs.tvlabs.ai/platform/platforms/tizen#\_\_docusaurus\_skipToContent\_fallback

TV Labs Docs

https://docs.tvlabs.ai/

https://docs.tvlabs.ai/platform

https://docs.tvlabs.ai/automation/welcome

Lua Scripting

https://docs.tvlabs.ai/scripting/introduction/getting-started

https://docs.tvlabs.ai/api/overview

Go to Platform

https://tvlabs.ai/app

TV Labs Docs

https://docs.tvlabs.ai/

https://docs.tvlabs.ai/platform

https://docs.tvlabs.ai/automation/welcome

Lua Scripting

https://docs.tvlabs.ai/scripting/introduction/getting-started

https://docs.tvlabs.ai/api/overview

Go to Platform

https://tvlabs.ai/app

← Back to main menu

https://docs.tvlabs.ai/platform

https://docs.tvlabs.ai/platform/platforms/tizen

https://docs.tvlabs.ai/platform/guides/apps

Sideloading

https://docs.tvlabs.ai/platform/guides/sideloading

https://docs.tvlabs.ai/platform/platforms/tizen

https://docs.tvlabs.ai/platform/cli/setup

https://docs.tvlabs.ai/platform/platforms/tizen

tvlabs connect

https://docs.tvlabs.ai/platform/cli/commands/connect

tvlabs upload

https://docs.tvlabs.ai/platform/cli/commands/upload

tvlabs projects

https://docs.tvlabs.ai/platform/cli/commands/projects

https://docs.tvlabs.ai/platform/cli/commands/run

https://docs.tvlabs.ai/platform/cli/changelog

Supported Platforms

https://docs.tvlabs.ai/category/supported-platforms

https://docs.tvlabs.ai/platform/platforms/googletv

https://docs.tvlabs.ai/platform/platforms/firetv

https://docs.tvlabs.ai/platform/platforms/android

Apple (tvOS / iOS)

https://docs.tvlabs.ai/platform/platforms/apple

https://docs.tvlabs.ai/platform/platforms/roku

SmartCast (Vizio)

https://docs.tvlabs.ai/platform/platforms/smartcast

Tizen (Samsung)

https://docs.tvlabs.ai/platform/platforms/tizen

https://docs.tvlabs.ai/platform/platforms/webos

Network Capture

https://docs.tvlabs.ai/platform/network-capture

https://docs.tvlabs.ai/platform/teleport

Benchmarking

https://docs.tvlabs.ai/platform/benchmarking

Integrations

https://docs.tvlabs.ai/platform/platforms/tizen

https://docs.tvlabs.ai/platform/platforms/tizen

Getting Started

https://docs.tvlabs.ai/platform/integrations/appium/getting-started

Device Targeting

https://docs.tvlabs.ai/platform/integrations/appium/device-targeting

Capabilities

https://docs.tvlabs.ai/platform/integrations/appium/capabilities

Appium Inspector

https://docs.tvlabs.ai/platform/integrations/appium/inspector

Network Capture

https://docs.tvlabs.ai/platform/integrations/appium/network-capture

Execute Methods

https://docs.tvlabs.ai/platform/integrations/appium/execute-methods

SmartCast Driver

https://docs.tvlabs.ai/platform/integrations/appium/appium-smartcast-driver

https://docs.tvlabs.ai/platform/integrations/appium/examples

CI/CD Integration

https://docs.tvlabs.ai/platform/integrations/ci\_cd

https://docs.tvlabs.ai/platform/security

https://docs.tvlabs.ai/platform/licensing

Get in Touch

https://docs.tvlabs.ai/platform/get\_in\_touch

Supported Platforms

https://docs.tvlabs.ai/category/supported-platforms

Tizen (Samsung)

On this page

tvlabs connect

command uses the Tizen SDK to connect with Samsung devices on the TV Labs platform as if they were in front of you.

Prerequisites

https://docs.tvlabs.ai/platform/platforms/tizen#prerequisites

Ensure that Tizen Studio 6.0 is installed and

are in your PATH. You can download Tizen Studio from the

Tizen Developer website

https://developer.tizen.org/development/tizen-studio/download

. Additional installation instructions can be found in the

Tizen Studio documentation

https://docs.tizen.org/application/tizen-studio/setup/install-sdk/

Installing Tizen SDK

https://docs.tvlabs.ai/platform/platforms/tizen#installing-tizen-sdk

Once you have Tizen Studio downloaded, follow the subsequent instructions, which can be also found in the

Samsung documentation

https://developer.samsung.com/smarttv/develop/getting-started/using-sdk/command-line-interface.html

Depending on the specific version of Tizen Studio, installation instructions may differ slightly. Please follow the Tizen/Samsung documentation for the most up to date information. These instructions are provided solely as a convenience.

Start the Tizen Studio desktop Application

Open the Package Manager found under Tools -> Package Manager

Navigate to the "Main SDK" tab

Select "Tizen SDK Tools"

Click install

Update your PATH environment variable to the appropriate installation location

~/tizen-studio/tools/ide/bin

~/tizen-studio/tools/ide/bin

C:\tizen-studio\tools\ide\bin

https://docs.tvlabs.ai/platform/platforms/tizen#connecting

After the Tizen Studio and the SDK is installed,

start a Tizen session on TV Labs

https://tvlabs.ai/app/devices

tvlabs connect

tvlabs connect

has successfully created a vendor connection, run

sdb devices

to check that the device is connected properly. The Tizen device should appear in the list of devices as

<device-ip>:26101

Port Mapping

https://docs.tvlabs.ai/platform/platforms/tizen#port-mapping

The port mapping when

tvlabs connect

is running and connected to a Tizen session is as follows:

Local port 26099 to

sdb server port 26099

https://docs.tizen.org/application/tizen-studio/common-tools/smart-development-bridge/

(Samsung Debug Bridge interface)

Local port 9222 to dynamic inspector port when the

https://docs.tvlabs.ai/platform/platforms/tizen#debugging-your-application

Local port 8001 to

Tizen device port 8001

https://developer.samsung.com/smarttv/develop/getting-started/using-sdk/tv-device.html

(WebSocket remote)

Local port 8002 to

Tizen device port 8002

https://developer.samsung.com/smarttv/develop/getting-started/using-sdk/tv-device.html

(WebSocket + SSL remote)

You may run a local

server on the same machine where

tvlabs connect

is running, however only requests to

will be forwarded to the TV Labs device

Creating a Certificate

https://docs.tvlabs.ai/platform/platforms/tizen#creating-a-certificate

To run your application on the TV Labs device, please ensure that you have a certificate to sign your application with. If you already have a certificate, you can skip ahead to

https://docs.tvlabs.ai/platform/platforms/tizen#installing

Prerequisites

https://docs.tvlabs.ai/platform/platforms/tizen#prerequisites-1

Before creating a certificate, it is important to ensure that the following Tizen Studio packages are installed the package manager.

#### From Main SDK:

https://docs.tvlabs.ai/platform/platforms/tizen#from-main-sdk

#### From Extension SDK:

https://docs.tvlabs.ai/platform/platforms/tizen#from-extension-sdk

TV Extensions-8.0

Samsung Certificate Extension

Instructions

https://docs.tvlabs.ai/platform/platforms/tizen#instructions

If you have not created a certificate, follow the instructions in the Tizen Studio documentation for

creating a certificate

https://developer.samsung.com/smarttv/develop/getting-started/setting-up-sdk/creating-certificates.html

When creating a certificate, if you are connected to the device via

tvlabs connect

, the DUID (device ID) should be automatically retrieved. If it is not automatically retrieved, you can retrieve the DUID by running

sdb shell 0 getduidgadget

#### The certificate can now be used to sign your Tizen application when packaging:

tizen build -- /path/to/application
tizen package --type wgt --sign <Name of Certificate> -- /path/to/application/build\_output

https://docs.tvlabs.ai/platform/platforms/tizen#installing

Once your application has been built and packaged using your certificate, you will be able to install and run your Tizen app on the device by running

tizen install -n application.wgt

. The installation command will output your application ID. You can then use

tizen run -p <application id>

to start the application.

Debugging your application

https://docs.tvlabs.ai/platform/platforms/tizen#debugging-your-application

The Chrome web inspector is available to use on Tizen with web applications. Before beginning, ensure that Chrome is installed.

To start the inspector, the

tvlabs connect

command must know the ID of your application you are targeting. Provide it with

--application-id

tvlabs connect -a AvsPHsIO4r.HelloTVLabs

After the vendor connection is made and your application is installed, press "d" to launch the inspector.

Once the inspector is active, navigate to

chrome://inspect

within the Chrome browser. The device will appear on this page.

If nothing appears in the inspector list, please check the

tvlabs connect

UI for errors. If there are no errors, ensure that your development application is open and running.

The Tizen inspector runs on port 9222 by default, but can be configured by setting the

tvlabs connect -i 5678 -a AvsPHsIO4r.HelloTVLabs

Troubleshooting

https://docs.tvlabs.ai/platform/platforms/tizen#troubleshooting

If you cannot connect to the device because of the error

failed to setup port forwarding: failed to forward port 26099 to 26099: port is already in use

, please ensure that your local sdb server is not running. You can stop the sdb server by running

sdb kill-server

If application installation fails, please ensure that the device storage is not full.

If the device becomes disconnected during the session, check that the device is still powered on. Once the device is powered on, press the "r" key in the

tvlabs connect

UI to reconnect.

If the device becomes disconnected during the session while the device is powered on and pressing the "r" key in the

tvlabs connect

UI to reconnect does not work, try ending and restarting the session.

sdb devices

does not list any devices after a successful connection with

tvlabs connect

, and the above steps do not work, please ensure that

development mode is enabled

https://developer.samsung.com/smarttv/develop/getting-started/using-sdk/tv-device.html

. After ensuring that the device is powered on in development mode, try pressing the "r" key in the

tvlabs connect

UI to reconnect again.

tvlabs connect

still cannot make a connection after trying these steps, please contact TV Labs for support.

Previous SmartCast (Vizio)

https://docs.tvlabs.ai/platform/platforms/smartcast

Next webOS (LG)

https://docs.tvlabs.ai/platform/platforms/webos

https://docs.tvlabs.ai/platform

https://docs.tvlabs.ai/automation/welcome

https://docs.tvlabs.ai/scripting/introduction/getting-started

API Reference

https://docs.tvlabs.ai/scripting/lua

https://docs.tvlabs.ai/platform/security

https://tvlabs.ai/team

https://tvlabs.ai/privacy

https://tvlabs.ai/tos

Copyright © 2026 TV Labs Inc.

