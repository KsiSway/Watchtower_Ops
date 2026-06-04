---
sourceFile: "Tizen Studio 6.1 – Tizen - Tizen Developer"
exportedBy: "Kortex"
exportDate: "2026-05-20T06:50:17.552Z"
---

# Tizen Studio 6.1 – Tizen - Tizen Developer

c4c1fb94-62f3-4785-b148-3b884a067030

Tizen Studio 6.1 – Tizen - Tizen Developer

281bc6dc-b348-4085-bf4a-a47eb23affe5

https://samsungtizenos.com/release-notes/tizen-studio-6-1/

Tizen Studio 6.1 - Tizen Release Notes - Platform and SDK Updates

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

Tizen Studio 6.1

Release date

Apr 16, 2025

https://samsungtizenos.com/release-notes/tizen-studio-6-1/#content-ide-and-tools

IDE and tools

https://samsungtizenos.com/release-notes/tizen-studio-6-1/#content-new-features

New features

Tizen Studio

Registered Tizen Studio in Programs and Features of Windows.

Added support for default certificates on Public Target.

Tizen app samples and Web Add-on template are deprecated.

log4j library version up from log4j1(v.1.2.17) to log4j2(v.2.24.3).

Notification popup added for the deprecation of Tizen Studio and Dynamic Analyzer in the next version.

Enhanced Tizen development tools usage data collection.

Modified sdb device detection scheme to use --only-detect-tizen as default option.

Visual Studio Code

Added import-wgt command for importing web applications from .wgt files.

Visual Studio (Windows)

Added import-wgt feature for importing web applications from .wgt files.

https://samsungtizenos.com/release-notes/tizen-studio-6-1/#content-fixed-bugs

Fixed the issue of Download New Image failing while creating new emulator in Emulator Manager.

Fixed the issue of repository url not showing for local package in Package Manager.

Fixed the issue of remote device addition failed after deletion in Tizen Studio for macOS.

Fixed the issue of profiler failing to profile projects within folders in a solution in VS Extension.

Fixed the issue of extra attribute getting added in tizen-manifest.xml file when package is from tizen-core CLI.

https://samsungtizenos.com/release-notes/tizen-studio-6-1/#content-known-issues

Known issues

On macOS, if the UI perspectives are not displayed properly after updating Tizen Studio, it is recommended to restart the IDE. This issue is because of the uncleared cache from the previous installation.

In case you see any old perspective, it is recommended to create a new workspace and import the projects to the new workspace to resolve the issue.

On macOS, since Catalina and above versions, Native Templates-5.5 will not build with CLI when the compiler is set to

If you install Tizen Studio in a directory that requires administrator privileges for access, an alert will be given. For example, for

C:\ProgramFiles

, location administrator privilege is needed to run Tizen SDK tools. Tizen Installer and Baseline SDK Installer alerts you if you try to install it into such a directory.

On macOS, Tizen Studio will not work properly if it is installed on Desktop directory, that is

$HOME/Desktop

. However, it works properly if it is installed on any other directory.

Web and Native IDE

You can create unit tests for Tizen 2.3.2 and higher version projects only. Unit testing for older versions is not supported.

The preview tab in the Web Page Editor sometimes does not appear properly. In this case, you can use an alternative feature, named Web SDK HTML Editor, which has enhanced features compared to the Web Page Editor. Instead of the preview tab in the Web Page Editor, use the preview feature

of the Web SDK HTML Editor.

In Rapid Development Support (RDS) mode, the web unit test result is not updated.

Remote Inspector does not allow audit in the updated version of Chrome.

Certificate Manager

Overwriting a duplicate certificate profile in the migration wizard works incorrectly on macOS.

In Tizen 5.5 version, the emulator images app uninstallation might take some time to complete if the app name contains more than 14 characters. A patch for the same is expected to be released in the next update.

To use Tizen Emulator, use Intel VTx supported CPU and the latest version of the graphic card driver provided by the vendor. To verify the prerequisites for Tizen Emulator, see

Prerequisites for Tizen Studio

https://samsungtizenos.com/docs/sdk-tools/dotnet/vscode/vscode-ext/index

If the host machine is using NVIDIA® Optimus® technology on either Ubuntu or Windows, you must set Tizen Emulator to run with your NVIDIA® graphics card. For Ubuntu, verify the

Bumblebee Project

https://wiki.ubuntu.com/Bumblebee

. For Windows, select

High Speed NVIDIA® Processor

Preferred Graphics Processor

in the NVIDIA® Control Panel.

On Ubuntu, if the graphics driver is out-of-date while launching Emulator Manager, your Ubuntu desktop session occasionally logs out or the emulator skin is displayed improperly. Verify the prerequisites and upgrade to the latest graphics driver.

On Windows, depending on your OS theme (such as Non-Aero themes and Windows XP themes), a display surface can be erased for a while if the emulator window is covered with another window. If you click the emulator window, the display surface runs correctly again.

On Windows, if an error with the message "failed to allocate memory" occurs while executing the emulator, try the following:

Close some other programs and try to launch the emulator again.

If the RAM size is set to 768 or 1024 MB for the VM in Emulator Manager, change it to 512 MB.

Increase the user area of the virtual memory in the system to 3 GB by entering the

bcdedit /setincreaseuserva 3072

command on the console with administrator rights (only in Windows 7), and reboot.

If you use a MacBook Pro that has both Intel HD and NVIDIA® GPUs, the emulator can terminate unexpectedly when you execute the emulator with OpenGL ES version 1.1 or 2.0. Verify the emulator configuration in Emulator Manager and on the

tab in the emulator configuration window, set OpenGL ES version to version 2.0, or to version 3.0.

When you launch Emulator Manager in Tizen IDE, the shortcut image of Emulator Manager may not be displayed properly.

Basic web applications are not installed on SD cards.

To use Tizen Emulator in Tizen platform 3.0 or lower, disable the CPU VT option in the

tab of emulator configuration.

CLI and SDB

Tizen Studio does not support the

Smart Development Bridge

https://samsungtizenos.com/docs/sdk-tools/dotnet/vscode/tizen-studio/common-tools/smart-development-bridge

(SDB) bash auto-completion on Windows (it is available on Ubuntu and macOS).

sdb install for rpk is not supported in TV 8.0 emulator(it will be supported in TV 9.0 emulator) and makes sdb freeze, press Ctrl+C to unfreeze.

Dynamic Analyzer

When analyzing applications on commercial devices running Tizen 3.0, newly-released or after a firmware update, the following problems exist:

The core frequency information is not shown.

The screenshots on the scene transitions feature will not work.

When analyzing applications on Tizen 4.0 Emulator or reference device, the startup profiling information is not shown.

The UI Hierarchy viewer feature and startup profiling are not performed simultaneously.

The Dynamic Analyzer cannot show lifecycle information for web applications.

Widget applications cannot be profiled with the Dynamic Analyzer. They are hidden in the application list on the toolbar for all Tizen platforms, except Tizen 2.3.2.

The Dynamic Analyzer sometimes gets stuck, which is caused by an internal security checking program.

Visual Studio

NUI XAML application build error can be resolved by doing a clean build.

On this page

IDE and tools

https://samsungtizenos.com/release-notes/tizen-studio-6-1/#content-ide-and-tools

New features

https://samsungtizenos.com/release-notes/tizen-studio-6-1/#content-new-features

https://samsungtizenos.com/release-notes/tizen-studio-6-1/#content-fixed-bugs

Known issues

https://samsungtizenos.com/release-notes/tizen-studio-6-1/#content-known-issues

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

