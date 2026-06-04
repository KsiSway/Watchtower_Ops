---
sourceFile: "Accelerating QEMU on Windows with HAXM"
exportedBy: "Kortex"
exportDate: "2026-05-20T06:50:17.253Z"
---

# Accelerating QEMU on Windows with HAXM

8ea226cb-5ec6-4f03-b402-d382296c239f

Accelerating QEMU on Windows with HAXM

0bf34838-bd3e-47af-8089-c99757f3993f

https://www.qemu.org/2017/11/22/haxm-usage-windows/

Accelerating QEMU on Windows with HAXM - QEMU

https://www.qemu.org/

https://www.qemu.org/download

https://www.qemu.org/support

https://www.qemu.org/contribute

https://www.qemu.org/documentation

https://wiki.qemu.org/

https://www.qemu.org/blog

Accelerating QEMU on Windows with HAXM

22 Nov 2017 — by Yu Ning

In this post, I'm going to introduce a useful technique to people who are using, or are interested in using, QEMU on Windows. Basically, you can make the most of your hardware to accelerate QEMU virtual machines on Windows: starting with its 2.9.0 release, QEMU is able to take advantage of

https://github.com/intel/haxm

to run x86 and x86\_64 VMs with hardware acceleration.

If you have used QEMU on Linux, you have probably enjoyed the performance boost brought by

https://wiki.qemu.org/Features/KVM

: the same VM runs a lot faster when you launch QEMU with the

-enable-kvm

) option, thanks to hardware-assisted virtualization. On Windows, you can achieve a similar speed-up with

-enable-hax

), after completing a one-time setup process.

#### First, make sure your host system meets the requirements of HAXM:

An Intel CPU that supports

Intel VT-x with Extended Page Tables (EPT)

https://ark.intel.com/Search/FeatureFilter?productType=processors&ExtendedPageTables=true

Intel CPUs that do not support the said feature are almost extinct now. If you have a Core i3/i5/i7, you should be good to go.

Windows 7 or later.

HAXM works on both 32-bit and 64-bit versions of Windows. For the rest of this tutorial, I'll assume you are running 64-bit Windows, which is far more popular than 32-bit nowadays.

Next, check your BIOS (or UEFI boot firmware) settings, and make sure VT-x (or Virtualization Technology, depending on your BIOS) is enabled. If there is also a setting for Execute Disable Bit, make sure that one is enabled as well. In most cases, both settings are enabled by default.

If your system is protected against changes to BIOS, e.g. you have enabled BitLocker Drive Encryption or any other tamper protection mechanism, you may need to take preventive measures to avoid being locked out after changing the said BIOS settings.

After that, if you are on Windows 8 or later, make sure Hyper-V is disabled. This is especially important for Windows 10, which enables Hyper-V by default. The reason is that Hyper-V makes exclusive use of VT-x, preventing HAXM and other third-party hypervisors (such as VMware and VirtualBox) from seeing that hardware feature. There are a number of ways to disable Hyper-V; one of them is to bring up the

Windows Features

and Enter, uncheck

in the resulting dialog, and click on

to confirm.

Note that changing the Hyper-V setting could also trigger the alarm of the tamper protection mechanism (e.g. BitLocker) that may be enabled on your system. Again, make sure you won't be locked out after the reboot.

Now you're ready to install HAXM, which needs to run as a kernel-mode driver on Windows so as to execute the privileged VT-x instructions. Simply download the latest HAXM release for Windows

https://software.intel.com/en-us/articles/intel-hardware-accelerated-execution-manager-intel-haxm

, unzip, and run

intelhaxm-android.exe

to launch the installation wizard. (Despite the file name, Android is not the only guest OS that can be accelerated by HAXM.)

If you haven't installed QEMU, now is the time to do it. I recommend getting the latest stable release from

https://qemu.weilnetz.de/w64/

. At the time of this writing, the latest stable release is 2.10.1 (build 20171006), so I downloaded

qemu-w64-setup-20171006.exe

, which is an easy-to-use installer.

With all that, we're ready to launch a real VM in QEMU. You can use your favorite QEMU disk image, provided that the guest OS installed there is compatible with the x86 (i386) or x86\_64 (amd64) architecture. My choice for this tutorial is

debian\_wheezy\_amd64\_standard.qcow2

, which contains a fresh installation of the standard Debian Wheezy system for x86\_64, available

https://people.debian.org/~aurel32/qemu/amd64/

. To boot it, open a new command prompt window, switch to your QEMU installation directory (e.g.

cd "C:\Program Files\qemu"

), and run:

qemu-system-x86\_64.exe -hda X:\path\to\debian\_wheezy\_amd64\_standard.qcow2 -accel hax

You don't have to leave the screen as the VM boots up, because soon you'll be able to see the Debian shell and log in.

To feel the difference made by HAXM acceleration, shut down the VM, and relaunch it without

qemu-system-x86\_64.exe -hda X:\path\to\debian\_wheezy\_amd64\_standard.qcow2

If you're still not impressed, try a more sophisticated VM image such as

debian\_wheezy\_amd64\_desktop.qcow2

, which boots to a desktop environment. VMs like this are hardly usable without hardware acceleration.

That's it! I hope HAXM gives you a more enjoyable QEMU experience on Windows. You may run into issues at some point, because there are, inevitably, bugs in HAXM (e.g. booting an ISO image from CD-ROM doesn't work at the moment). But the good news is that HAXM is now open source on

https://github.com/intel/haxm

, so everyone can help improve it. Please create an issue on GitHub if you have a question, bug report or feature request.

https://www.qemu.org/blog/category/tutorials/index.html

https://www.qemu.org/blog/category/haxm/index.html

Recent Posts

QEMU version 11.0.0 released

https://www.qemu.org/2026/04/22/qemu-11-0-0/

22 Apr 2026

Announcing QEMU Google Summer of Code 2026 internships

https://www.qemu.org/2026/02/20/gsoc-2026/

20 Feb 2026

April 2026 (1)

https://www.qemu.org/blog/2026/04/

February 2026 (1)

https://www.qemu.org/blog/2026/02/

December 2025 (1)

https://www.qemu.org/blog/2025/12/

November 2025 (1)

https://www.qemu.org/blog/2025/11/

August 2025 (1)

https://www.qemu.org/blog/2025/08/

April 2025 (1)

https://www.qemu.org/blog/2025/04/

March 2025 (1)

https://www.qemu.org/blog/2025/03/

December 2024 (1)

https://www.qemu.org/blog/2024/12/

September 2024 (1)

https://www.qemu.org/blog/2024/09/

May 2024 (1)

https://www.qemu.org/blog/2024/05/

April 2024 (1)

https://www.qemu.org/blog/2024/04/

December 2023 (1)

https://www.qemu.org/blog/2023/12/

August 2023 (1)

https://www.qemu.org/blog/2023/08/

April 2023 (1)

https://www.qemu.org/blog/2023/04/

March 2023 (2)

https://www.qemu.org/blog/2023/03/

February 2023 (1)

https://www.qemu.org/blog/2023/02/

December 2022 (1)

https://www.qemu.org/blog/2022/12/

November 2022 (1)

https://www.qemu.org/blog/2022/11/

August 2022 (1)

https://www.qemu.org/blog/2022/08/

April 2022 (1)

https://www.qemu.org/blog/2022/04/

March 2022 (1)

https://www.qemu.org/blog/2022/03/

February 2022 (1)

https://www.qemu.org/blog/2022/02/

December 2021 (1)

https://www.qemu.org/blog/2021/12/

August 2021 (3)

https://www.qemu.org/blog/2021/08/

April 2021 (1)

https://www.qemu.org/blog/2021/04/

March 2021 (1)

https://www.qemu.org/blog/2021/03/

February 2021 (1)

https://www.qemu.org/blog/2021/02/

January 2021 (1)

https://www.qemu.org/blog/2021/01/

December 2020 (1)

https://www.qemu.org/blog/2020/12/

November 2020 (2)

https://www.qemu.org/blog/2020/11/

September 2020 (1)

https://www.qemu.org/blog/2020/09/

August 2020 (1)

https://www.qemu.org/blog/2020/08/

July 2020 (1)

https://www.qemu.org/blog/2020/07/

April 2020 (1)

https://www.qemu.org/blog/2020/04/

February 2020 (2)

https://www.qemu.org/blog/2020/02/

December 2019 (1)

https://www.qemu.org/blog/2019/12/

November 2019 (3)

https://www.qemu.org/blog/2019/11/

August 2019 (1)

https://www.qemu.org/blog/2019/08/

May 2019 (1)

https://www.qemu.org/blog/2019/05/

April 2019 (1)

https://www.qemu.org/blog/2019/04/

February 2019 (1)

https://www.qemu.org/blog/2019/02/

January 2019 (1)

https://www.qemu.org/blog/2019/01/

December 2018 (1)

https://www.qemu.org/blog/2018/12/

August 2018 (1)

https://www.qemu.org/blog/2018/08/

June 2018 (1)

https://www.qemu.org/blog/2018/06/

May 2018 (1)

https://www.qemu.org/blog/2018/05/

April 2018 (1)

https://www.qemu.org/blog/2018/04/

February 2018 (3)

https://www.qemu.org/blog/2018/02/

January 2018 (1)

https://www.qemu.org/blog/2018/01/

November 2017 (1)

https://www.qemu.org/blog/2017/11/

October 2017 (1)

https://www.qemu.org/blog/2017/10/

September 2017 (1)

https://www.qemu.org/blog/2017/09/

August 2017 (1)

https://www.qemu.org/blog/2017/08/

May 2017 (1)

https://www.qemu.org/blog/2017/05/

March 2017 (1)

https://www.qemu.org/blog/2017/03/

February 2017 (2)

https://www.qemu.org/blog/2017/02/

Advent calendar

http://qemu-advent-calendar.org/

Blog planet

https://planet.virt-tools.org/

https://www.linux-kvm.org/

http://libguestfs.org/

https://libvirt.org/

https://xenproject.org/

page source

https://gitlab.com/qemu-project/qemu-web/-/blob/master/\_posts/2017-11-22-haxm-usage-windows.md

QEMU is a member of

Software Freedom Conservancy

https://www.qemu.org/conservancy/

https://www.qemu.org/sponsors/

Website licenses

https://www.qemu.org/license.html

