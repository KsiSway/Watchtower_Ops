---
sourceFile: "Tizen 6.0 Public M2"
exportedBy: "Kortex"
exportDate: "2026-05-20T06:50:17.534Z"
---

# Tizen 6.0 Public M2

0c435f9c-a7df-4b84-b6ad-41f402dd3380

Tizen 6.0 Public M2

6cf23898-6f4d-45a7-bca5-7ce53b116876

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/

Tizen 6.0 Public M2 - Tizen Release Notes - Platform and SDK Updates

Tizen Developer

https://samsungtizenos.com/

https://samsungtizenos.com/login

https://samsungtizenos.com/about/overview/

https://samsungtizenos.com/products

https://samsungtizenos.com/tools-download/

https://samsungtizenos.com/docs

https://samsungtizenos.com/docs/platform/hal/overview

VS Code Extension

https://samsungtizenos.com/docs/sdk-tools/dotnet/vscode/tizen-studio/common-tools/overview

Visual Studio

https://samsungtizenos.com/docs/sdk-tools/dotnet/visual-studio/tizen-studio/common-tools/overview

Application

https://samsungtizenos.com/docs/application/dotnet/overview

https://samsungtizenos.com/docs/application/native/overview

https://samsungtizenos.com/docs/application/web/overview

https://samsungtizenos.com/docs/application/flutter/overview

https://samsungtizenos.com/docs/extensions/tizenx/overview

https://samsungtizenos.com/docs/misc/feature

https://samsungtizenos.com/docs/misc/privilege

https://samsungtizenos.com/docs/misc/runtime

https://samsungtizenos.com/docs/misc/setting

https://samsungtizenos.com/docs/misc/system

https://samsungtizenos.com/blog/

Knowledge Hub

https://samsungtizenos.com/knowledge-hub

Release Notes

https://samsungtizenos.com/release-notes

Tizen 6.0 Public M2

Release date

Oct 27, 2020

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-release-details

Release details

Getting source code

http://review.tizen.org/git/

(Tizen 6.0 M2 source codes are under

Getting binaries and images

http://download.tizen.org/releases/milestone/tizen/base/tizen-base\_20201008.1/

http://download.tizen.org/releases/milestone/tizen/base/tizen-base\_20201008.1/

#### Profile(Unified):

http://download.tizen.org/releases/milestone/tizen/unified/tizen-unified\_20201020.1/

http://download.tizen.org/releases/milestone/tizen/unified/tizen-unified\_20201020.1/

How to flash to a device

https://samsungtizenos.com/release-notes/developing/flashing.md

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-release-notes

Release notes

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-system-kernel-and-system-framework

System (kernel and system framework)

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-new-and-changed-features

New and changed features

Kernel upgrade

Kernel for Raspberry Pi 4 has been upgraded to version 5.4.50.

64Bit Kernel and Boot Support

64Bit Kernel and Boot for Raspberry Pi 4 has been supported.

Lightweight KSM

Reference lightweight version of Kernel Samepage Merging (LKSM) in Raspberry PI 4 Kernel and resourced extension with LKSM has been implemented.

System management

Runtime storage verification with dm-verity has been developed.

Systemd has been optimized for better boot performance.

Algorithms for D-Bus policy check have been improved for reducing the D-Bus call latency.

D-Bus implementation on public API set has been optimized.

QoS feature has been developed for limiting and fully utilizing log usage.

A deduplication feature has been developed for preventing repeated logs.

CPU usage on dlog\_logger has been optimized with added configurations.

Device and resource management

Doze mode has been developed for power saving during the LCD off period.

The Always-on-display feature has been improved for better user experience.

Configurable CPU pinning for heterogeneous cores has been developed.

Monitoring for CPU lock timeout has been improved to prevent battery drain.

C API set for obtaining battery information has been added.

C# API set for power management QoS has been added.

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-fixes

System and device management

The emergency mode has been fixed to remove wrong service dependencies.

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-system-system-reliability-and-os-upgrade

System (system reliability and OS upgrade)

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-new-and-changed-features-1

New and changed features

Update package signing/verification has been enhanced.

A recovery package signer/verifier has been added.

Removable storage-based update/recovery has been supported.

Update result API has been enhanced.

Diagnostics API, which can be used to retrieve diagnostic information from the system like system crash, has been added.

The ability to resolve Callstack from updatable applications has been added.

Core dumps with reduced size for C# programs have been added.

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-system-base

System (base)

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-new-and-changed-features-2

New and changed features

The capi-base-utils API set has been expanded.

ures: Resource management module.

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-fixes-1

The capi-system-system-settings API has been refactored.

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-application-framework

Application framework

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-new-and-changed-features-3

New and changed features

TIDL Extension

The API set for synchronous connection has been added.

New keywords for sharing files have been added.

Tools for analyzing latency and throughput have been provided.

The enhanced TIDL compiler using receive threads to improve concurrency has been provided.

Multi-package installer

The API set has been provided to install multiple packages at once.

Tools have been provided to install multiple packages at once.

Tizen Theme Manager

Getting resources

The API set for obtaining related resource path using a specific resource key has been provided.

Theme changed event

The API set for receiving the changed event from the app when changing the settings has been provided.

Theme overlay

Overlay function between the default theme and the selected theme has been provided.

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-window-and-interaction

Window and interaction

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-new-and-changed-features-4

New and changed features

Interaction

Gesture FW and engine

The API set to receive the event for hand gesture has been supported.

Gesture Framework for managing multi gesture clients and engines has been supported.

The service app for the default gesture engine has been supported.

Support for on-demand daemon launch has been added.

Enlightenment Wayland display server

Display Compatibility for the Legacy Widget application has been added. Without any modification, Legacy Widget applications can be viewed on different screen sizes than that it was originally designed for.

Ecore buffer

The ecore-buffer and ecore-buffer-queue API set has been deprecated.

Tizen-ws-shell

A new enumeration has been added to support a new type of Quickpanel service.

Quickpanel C# Support

C# API set for Quickpanel client and service has been added (Tizen.NUI.WindowSystem.Shell).

The libds API set used to create and configure Wayland-based display server has been newly added.

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-graphics-engine

Graphics engine

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-new-and-changed-features-5

New and changed features

DALi (3D UI Toolkit)

API set of DALi has been deprecated. DALi API set has been replaced with NUI (DALi C# layer).

Throwing an exception has been added when some methods are used in worker threads.

Support for ComponentApplications has been added.

Support for WebP image has been added.

Support for asynchronous loading of gif images has been added.

The keyboard repeat setting changed event has been added.

Some Capture API set has been added.

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-fixes-2

The View size-related bug has been fixed when setting and animating the size are used at the same time.

A PropertyNotification bug has been fixed.

Some bugs of GaussianBlurVies have been fixed.

Some bugs of TextLabels have been fixed.

Some memory leak bugs have been fixed.

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-ui-framework

UI framework

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-new-and-changed-features-6

New and changed features

Version 1.24 has been upgraded to version 1.25.

Support for gengrid has been added for the wearable profile.

Support for evas vector graphics has been added.

Support for relative container has been added.

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-multimedia-framework

Multimedia framework

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-new-and-changed-features-7

New and changed features

Support for platform privilege has been added.

MediaStreamer

Native WebRTC API set has been added.

MEDIA\_STREAMER\_PARAM\_WEBRTC\_PEER\_TYPE

MEDIA\_STREAMER\_PARAM\_WEBRTC\_STUN\_SERVER

MEDIA\_STREAMER\_PARAM\_WEBRTC\_REMOTE\_SESSION\_DESCRIPTION

MEDIA\_STREAMER\_PARAM\_WEBRTC\_ADD\_ICE\_CANDIDATE

MEDIA\_STREAMER\_PARAM\_WEBRTC\_RTP\_TRANSCEIVER\_DIRECTION\_FOR\_AUDIO

MEDIA\_STREAMER\_PARAM\_WEBRTC\_RTP\_TRANSCEIVER\_DIRECTION\_FOR\_VIDEO

MEDIA\_STREAMER\_PARAM\_MAX\_LATENESS

MEDIA\_STREAMER\_PARAM\_RTP\_LATENCY

media\_streamer\_node\_decoded\_ready\_cb

media\_streamer\_node\_set\_decoded\_ready\_cb

media\_streamer\_node\_unset\_decoded\_ready\_cb

media\_streamer\_webrtc\_node\_set\_message\_cb

media\_streamer\_webrtc\_node\_unset\_message\_cb

Support for WebP has been added.

Support for encoding GIF and WebP animation has been added.

Support for ARGB and GBRA for PNG encoding has been added.

Metadata editor

Support for WAV, FLAC, and OGG has been added.

Media controller

Result codes for command have been added.

Three Playback states connection, buffering, and error have been added.

Media vision

New enumerations for human pose landmark and body part have been added.

API set to detect pose landmarks, such as the human body pose has been added.

API set to decide video frame encoding has been added.

Support for video scaling has been added.

Video scaling is only for a single video stream supported device.

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-network-and-connectivity

Network and connectivity

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-new-and-changed-features-8

New and changed features

Connection API

Following API set has been changed to require new partner level privilege.

#### New privilege:

http://tizen.org/privilege/network.route

Privilege level: partner

Affected API set

connection\_add\_route

connection\_remove\_route

connection\_add\_route\_ipv6

connection\_remove\_route\_ipv6

connection\_add\_route\_entry

connection\_remove\_route\_entry

Bluetooth mesh network

Bluetooth framework has been extended to support the Bluetooth mesh network standards.

Platform API for Bluetooth mesh network features has been added.

Open source bluez module has been upgraded to support Bluetooth mesh network.

Tizen Bluetooth framework has been extended to control bluez's mesh daemon.

Bluetooth mesh network provisioning and controlling devices like smart bulbs, which support Bluetooth mesh network standards has been added.

Wi-Fi multiple interface support

Network modules have been extended to support devices with multiple Wi-Fi network interfaces.

connman and net-config have been extended to identify a specific Wi-Fi network interface for operations like scan and connect.

Platform API for specifying the Wi-Fi network interface for each operation has been added for connection and Wi-Fi Manager API.

Public connection and Wi-Fi Manager API is backward compatible by introducing a concept of default Wi-Fi network interface.

Ultra-wideband (UWB) ranging

Platform API for UWB has been added.

UWB manager daemon has been added.

UWB manager daemon has been tested with Decawave's dwm1001 module on RPI 4.

Devices with UWB modules have been enabled to measure the distance between them.

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-security

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-new-and-changed-features-9

New and changed features

Security monitor

Query-based security API has been added.

Type-safe query builder has been added.

Support for Device Policy Management has been added.

New privilege has been added.

network.route

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-service-framework

Service framework

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-new-and-changed-features-10

New and changed features

Location framework

Support for getting velocity accuracy has been added.

Support for getting location bounds to check on edge with tolerance has been added.

Support for checking on edge with tolerance for polygon has been added.

Support for checking on edge with tolerance for circle has been added.

Support for checking on edge with tolerance for rectangle has been added.

Battery-monitor framework

Support for resetting battery dump data has been added.

Support for dumping application ID with the event of battery dump has been added.

Context framework

Motion API has been deprecated.

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-fixes-3

Context framework

A potential security vulnerability has been fixed.

Location framework

The precision in getting distance between two locations has been improved.

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-web-framework

Web framework

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-new-and-changed-features-11

New and changed features

Feature support

Support for OffscreenCanvas has been added: OffscreenCanvas enables canvas rendering apart from the main thread.

Strict MIME type for module scripts

Loading module script from the local file feature has been removed.

Web runtime

Device API for wrt-service has been added.

Web server has been added as a wrt-service built-in module.

WRT.js API management policy has been added.

API has been changed from generic js to TypeScript.

API compatibility checker has been added.

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-fixes-4

Compatibility enhancement

The problem of autofill operation in major web site has been improved.

Stability enhancement

Unexpected random crash while clean up sequence has been fixed.

App control URL bug

appcontrol:// scheme is now able to launch application from encoded URL.

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-lightweight-web-solution

Lightweight web solution

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-new-and-changed-features-12

New and changed features

Rendering engine

Data Element's DOM API has been added.

Performance Web API set has been added.

Range Web API set has been added.

ES10 features have been added.

Array.prototype.flat

Array.prototype.flatMap

Object.fromEntries

String.prototype.trimStart

String.prototype.trimEnd

The syntax of the following features has been updated.

Optional catch binding parameters

Allowing U+2028 (Line Separator) and U+2029 (Paragraph Separator) in string literals

Array.prototype.sort has been updated due to the specification change.

Function.prototype.toString has been updated due to the specification change.

Performance and memory Optimization

Debugger core features have been updated.

Lazy AtomicString initialization for memory and performance has been optimized.

Vector extension logic has been improved.

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-fixes-5

Layout bugs have been fixed.

Scroll bugs have been fixed.

Font Rendering bugs have been fixed.

Memory overflow bugs have been fixed.

Crash issues have been fixed.

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-tizen-net

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-new-and-changed-features-13

New and changed features

NET runtime and tools

.NETCore has been upgraded from 3.1.0 to 3.1.3.

VertexBuffer class has been added.

Pagination class has been added.

Screen connection methods have been added to CustomView class.

SlidingStarted event has been added to Slider class.

ThumbColor property has been added to Slider class.

FlexLayout and GridLayout have been added.

ScrollPosition and ScrollCurrentPosition have been added to ScrollableBase class.

Notification class has been added.

FlexContainer class has been deprecated.

IndicatorColor and SelectedIndicatorColor have been added to Pagination class.

Quickpanel has been added to WindowSystem.

Tizen.Network.Connection

Required privilege level has been changed.

Tizen.MachineLearning

Custom filter class has been added.

Tizen.Multimedia

Setter and Getter for volume recording has been added to AudioIO.

Result code and playback state have been added to MediaController.

New RequestCommand for async has been added to MediaController.

New barcode types have been added to Vision.

Tizen.Applications

Synchronous connection request and private file sharing have been added to RPCPort.

Tizen.Network

New Avrcp Control has been added to Bluetooth.

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-toolchain

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-new-and-changed-features-14

New and changed features

Toolchain configure dumper support has been developed.

"{package}-configure-dump.rpm" in binutils, glibc, and gcc have been provided with “dump\_configure“ macro.

Build with armv8-a machine option has been added.

ASan has been enabled.

Automated build, test with JIRA reporting process has been established.

Libasansi feature for .NET ASan has been back-ported from Tizen 5.5.

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-fixes-6

Patches for CVE-2020-10029 have been back-ported in glibc from upstream.

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-machine-learning

Machine learning

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-new-and-changed-features-15

New and changed features

Machine Learning Training API (new)

The ability to update and train deep Neural Networks on Tizen devices has been added.

The Machine Learning Training API allows application developers to describe their own Neural Network models and train the models or to re-train pre-trained models in runtime.

Machine Learning Inference API update

The ability to use various hardware accelerators with Single API has been added.

The ability to fine-tune each element of a pipeline in runtime has been added.

The latency overheads of Single API have been reduced.

NNStreamer update

NNStreamer has been upgraded from 1.5.2 to 1.6.0.

AI acceleration hardware support has been added.

Machine Learning API can utilize Verisicon-Vivante and Qualcomm-SNPE in addition to previously supported hardware.

You may need to download and install additional adaptors from tizen.org to support additional hardware.

The ability to import stream data from or export stream data to Flatbuffers and Protobuffers has been added for distributed or remote pipelines.

The ability to implement and insert tensor-converters for custom data types in runtime has been added.

NNTrainer (new)

NNTrainer has been added to allow on-device Neural Network training, mainly targeting transfer learning mechanisms with a few simple layers.

NNTrainer provides various weight initializers, optimizers, activation functions, and loss functions.

Neural Network models can be constructed by applications in runtime or loaded from a model file and pre-trained weight values. Trained weight values can be saved and loaded later.

Data set for training can be generated by the application in runtime or can be fetched from a filesystem.

NNFW Runtime (ONE Runtime) update

NNFW Runtime has been upgraded from 1.4.0 to 1.9.0.

The ability to install extensions to provide customized performance optimization has been added.

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-fixes-7

Machine Learning Inference API

Incorrect error codes have been fixed.

The edge-TPU and Movidius-X runtime issues have been fixed.

On this page

Release details

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-release-details

Release notes

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-release-notes

System (kernel and system framework)

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-system-kernel-and-system-framework

New and changed features

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-new-and-changed-features

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-fixes

System (system reliability and OS upgrade)

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-system-system-reliability-and-os-upgrade

New and changed features

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-new-and-changed-features-1

System (base)

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-system-base

New and changed features

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-new-and-changed-features-2

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-fixes-1

Application framework

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-application-framework

New and changed features

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-new-and-changed-features-3

Window and interaction

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-window-and-interaction

New and changed features

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-new-and-changed-features-4

Graphics engine

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-graphics-engine

New and changed features

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-new-and-changed-features-5

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-fixes-2

UI framework

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-ui-framework

New and changed features

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-new-and-changed-features-6

Multimedia framework

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-multimedia-framework

New and changed features

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-new-and-changed-features-7

Network and connectivity

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-network-and-connectivity

New and changed features

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-new-and-changed-features-8

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-security

New and changed features

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-new-and-changed-features-9

Service framework

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-service-framework

New and changed features

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-new-and-changed-features-10

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-fixes-3

Web framework

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-web-framework

New and changed features

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-new-and-changed-features-11

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-fixes-4

Lightweight web solution

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-lightweight-web-solution

New and changed features

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-new-and-changed-features-12

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-fixes-5

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-tizen-net

New and changed features

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-new-and-changed-features-13

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-toolchain

New and changed features

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-new-and-changed-features-14

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-fixes-6

Machine learning

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-machine-learning

New and changed features

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-new-and-changed-features-15

https://samsungtizenos.com/release-notes/tizen-6-0-public-m2/#content-fixes-7

Tizen Developer

About Tizen

https://samsungtizenos.com/about/overview/

https://samsungtizenos.com/about/brand-guide/

https://samsungtizenos.com/blog/

Learn Tizen

https://samsungtizenos.com/docs/sdk-tools/dotnet/vscode/tizen-studio/common-tools/overview

https://samsungtizenos.com/docs

https://samsungtizenos.com/tools-download/

Release Notes

https://samsungtizenos.com/release-notes/

Family site

Samsung developer

https://developer.samsung.com/

Tizen partners

https://www.tizenpartner.com/

https://www.tizen.org/

Terms of use

https://samsungtizenos.com/terms-of-use/

Privacy Policy

https://samsungtizenos.com/privacy-policy/

Cookie settings

Copyright © 2026 SAMSUNG. All rights reserved.

https://www.youtube.com/@SamsungDevelopers

https://www.facebook.com/TizenProject/

https://x.com/Tizen

For the best experience,

Please visit us from a computer

Copyright © 2026 SAMSUNG. All rights reserved.

https://www.youtube.com/@SamsungDevelopers

https://www.facebook.com/TizenProject/

https://x.com/Tizen

We use cookies to ensure the proper functioning of our site, to remember your preferences (such as global messages and release notes), and to analyze traffic. You can change your preferences at any time.

Read our cookie & privacy policy

https://samsungtizenos.com/privacy-policy

Accept all Reject non-essential

Preferences

Customize your cookie preferences

You can enable or disable non-essential cookies. Essential cookies are always on to ensure the site works properly and to keep you signed in.

These cookies are necessary for the website to function properly and cannot be switched off. They help with things like logging in and setting your privacy preferences.

These cookies help us improve the site by tracking which pages are most popular and how visitors move around the site.

Enable analytics cookies

Accept all Reject non-essential

Report any errors or questions you found

https://github.com/Samsung/Tizen.Issues/issues

