---
sourceFile: "Tizen Studio 6.0 – Tizen - Tizen Developer"
exportedBy: "Kortex"
exportDate: "2026-05-20T06:50:17.551Z"
---

# Tizen Studio 6.0 – Tizen - Tizen Developer

4dac9c2a-4027-43ca-82ea-85f86f1d20e0

Tizen Studio 6.0 – Tizen - Tizen Developer

b619798d-19b1-45f4-b9d1-af7645acc65f

https://samsungtizenos.com/release-notes/tizen-studio-6-0/

Tizen Studio 6.0 - Tizen Release Notes - Platform and SDK Updates

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

Tizen Studio 6.0

Release date

Nov 4, 2024

https://samsungtizenos.com/release-notes/tizen-studio-6-0/#content-ide-and-tools

IDE and Tools

https://samsungtizenos.com/release-notes/tizen-studio-6-0/#content-new-features

New features

#### Tizen Studio:

Added Tizen 9.0 profile and deprecated all Tizen profiles below 6.0.

Tizen Issue Reporter added in SDK and Baseline tools.

Tizen Studio and Tizen Tools are now supported on Windows 11 OS.

#### Visual Studio Code:

TV Web Development has been added along with TV Web Simulator and Web Inspector features.

SDK Installation wizard is provided to easily setup Tizen SDK and Extensions.

Added Unit Test, Code Coverage, ASAN and LSAN Tools support for Tizen Native Applications.

Added .NET Diagnostics Tools (GCDump, Dump, and Trace) for Tizen .NET Applications.

WASM (WebAssembly) feature has been added for Tizen Web Applications.

Tizen Activity bar, Device Monitoring and Welcome Page features have been added to enhance Tizen Developer experience.

Update .NET workload option is added.

#### Visual Studio (Windows):

Added Unit Test and Code Coverage support for Tizen Native Applications.

Added ASAN and LSAN tools support for Tizen Native Applications.

Added right click menu named

"Install Tizen Application"

to install application directly on a target device.

Added Issue Reporter menu to report issues related to VS plugin.

https://samsungtizenos.com/release-notes/tizen-studio-6-0/#content-fixed-bugs

Fixed the issue of Tizen Studio launcher splash image getting flipped in macOS Sonoma.

Fixed the issue of RPK not being installed in TV using SDB.

Fixed the issue of .NET workload getting installed on every launch in VS Code plugin.

Fixed the build issue of Tizen Native Shared Library projects in VS Code plugin.

Fixed the issue of newly added source and resource files not getting updated in Native project configuration in VS Code plugin.

Fixed the issue of

tizen-manifest.xml

not opening for Native, and

TizenNUIGadget\_inhouse

project in VS plugin.

Fixed the issue of all files getting deleted whenever creating a project inside an existing solution in VS plugin.

Fixed the issue of .NET trace getting stuck in VS plugin.

Fixed the issue of Certificate change not getting impacted by prompting the user to restart VS.

Fixed the issue of application being launched in unselected device in VS plugin.

Fixed the issue of .NET profiler session not closing upon the creation of another project in VS plugin.

https://samsungtizenos.com/release-notes/tizen-studio-6-0/#content-known-issues

Known issues

On macOS, if the UI perspectives are not displayed properly after updating Tizen Studio, it is recommended to restart the IDE. This issue is because of the uncleared cache from the previous installation.

In case you see any old perspective, it is recommended to create a new workspace and import the projects to the new workspace to resolve the issue.

On macOS, from Catalina and above versions, Native Templates 5.5 will not build with CLI when the compiler is set to

If you install Tizen Studio in a directory that requires administrator privileges for access, an alert will be shown. For example, for

C:\ProgramFiles

, location administrator privilege is needed to run Tizen SDK Tools. Tizen Installer and Baseline SDK Installer alerts you if you try to install it into such a directory.

On macOS, Tizen Studio will not work properly if it is installed on the desktop directory, that is

/HOME/Desktop

. However, it works properly if it is installed on any other directory.

#### Web and Native IDE:

You can create Unit Tests for Tizen 2.3.2 and higher version projects only. Unit Testing for older versions is not supported.

The preview tab in the Web Page Editor sometimes does not appear properly. In this case, you can use an alternative feature, named Web SDK HTML Editor, which has enhanced features compared to the Web Page Editor. Instead of the preview tab in the Web Page Editor, use the preview feature

of the Web SDK HTML Editor.

In Rapid Development Support (RDS) mode, the Web Unit Test result is not updated.

Remote Inspector does not allow audit in the updated version of Chrome.

#### Certificate Manager:

Overwriting a duplicate Certificate profile in the migration wizard does not work correctly on macOS.

In Tizen 5.5 version, the uninstallation of Emulator images application might take some time to complete if the application name contains more than 14 characters. A patch for this is expected to be released in the next update.

To use Tizen Emulator, use Intel VTx supported CPU and the latest version of the graphics card driver provided by the vendor. To verify the prerequisites for Tizen Emulator, check

Prerequisites for Tizen Studio

https://samsungtizenos.com/docs/sdk-tools/dotnet/vscode/vscode-ext/index

If the host machine is using NVIDIA® Optimus® technology on either Ubuntu or Windows, you must set Tizen Emulator to run with your NVIDIA® graphics card. For Ubuntu, verify the

Bumblebee Project

https://wiki.ubuntu.com/Bumblebee

. For Windows, select

High Speed NVIDIA® Processor

Preferred Graphics Processor

in the NVIDIA® Control Panel.

On Ubuntu, if the graphics driver is out-of-date while launching the Emulator Manager, your Ubuntu desktop session occasionally logs out, or the Emulator skin is not displayed properly. Verify the prerequisites and upgrade to the latest graphics driver.

On Windows, depending on your OS theme (such as, Non-Aero themes and Windows XP themes), a display surface can be erased for a while if the Emulator window is covered with another window. If you click on the Emulator window, the display surface runs correctly again.

On Windows, if an error with the message

"failed to allocate memory"

occurs while executing the Emulator, then try the following:

Close some of the other programs, and try to launch the Emulator again.

If the RAM size is set to 768 or 1024 MB for the VM in Emulator Manager, change it to 512 MB.

Increase the user area of the virtual memory in the system to 3 GB by entering the

bcdedit/setincreaseuserva 3072

command on the console with administrator rights (only on Windows 7), and then reboot.

If you use a MacBook Pro that has both Intel HD and NVIDIA® GPUs, the Emulator can terminate unexpectedly when you execute the Emulator with OpenGL ES version 1.1 or 2.0. Verify the Emulator configuration in the Emulator Manager, and on the

tab in the Emulator configuration window, set OpenGL ES version to version 2.0, or to version 3.0.

When you launch Emulator Manager in Tizen IDE, the shortcut image of Emulator Manager may not be displayed properly.

Basic Web Applications are not installed on SD cards.

To use Tizen Emulator in Tizen Platform 3.0 or lower, disable the CPU VT option in the

tab of the Emulator configuration.

#### CLI and SDB:

Tizen Studio does not support the

Smart Development Bridge

https://samsungtizenos.com/docs/sdk-tools/dotnet/vscode/tizen-studio/common-tools/smart-development-bridge

(SDB) bash auto-completion on Windows (it is available on Ubuntu and macOS).

SDB installation for RPK (Resource Package) is not supported in TV 8.0 Emulator and makes the SDB freeze, then press

to unfreeze (it will be supported in TV 9.0 Emulator).

#### Dynamic Analyzer:

When analyzing applications (newly released or after a firmware update) on commercial devices that run on Tizen 3.0, the following problems exist:

The core frequency information is not shown.

The screenshots on the scene transitions feature does not work.

When analyzing applications on Tizen 4.0 Emulator or on reference device, the startup profiling information is not shown.

The UI Hierarchy viewer feature and startup profiling are not performed simultaneously.

The Dynamic Analyzer cannot show lifecycle information for Web Applications.

Widget Applications cannot be profiled with the Dynamic Analyzer. They are hidden in the application list on the toolbar for all Tizen Platforms, except for Tizen 2.3.2.

The Dynamic Analyzer sometimes gets stuck, which is caused by an internal security checking program.

#### Visual Studio:

NUI XAML application build error can be resolved by doing a clean build.

On this page

IDE and Tools

https://samsungtizenos.com/release-notes/tizen-studio-6-0/#content-ide-and-tools

New features

https://samsungtizenos.com/release-notes/tizen-studio-6-0/#content-new-features

https://samsungtizenos.com/release-notes/tizen-studio-6-0/#content-fixed-bugs

Known issues

https://samsungtizenos.com/release-notes/tizen-studio-6-0/#content-known-issues

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

