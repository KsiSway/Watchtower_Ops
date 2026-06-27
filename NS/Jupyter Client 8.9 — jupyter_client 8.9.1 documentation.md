---
sourceFile: "Jupyter Client 8.9 — jupyter_client 8.9.1 documentation"
exportedBy: "Kortex"
exportDate: "2026-06-26T04:27:51.401Z"
---

# Jupyter Client 8.9 — jupyter_client 8.9.1 documentation

74aef1a0-e85e-487a-8f1d-a84aab843c55

Jupyter Client 8.9 — jupyter\_client 8.9.1 documentation

acdcc8ff-e7a4-4981-a5b6-fa8421f0c868

https://jupyter-client.readthedocs.io/en/latest/

Jupyter Client 8.9 — jupyter\_client 8.9.1 documentation

Skip to main content

https://jupyter-client.readthedocs.io/en/latest/#main-content

Back to top

jupyter\_client 8.9.1 documentation

https://jupyter-client.readthedocs.io/en/latest/

Messaging in Jupyter

https://jupyter-client.readthedocs.io/en/latest/messaging.html

Making kernels for Jupyter

https://jupyter-client.readthedocs.io/en/latest/kernels.html

Making simple Python wrapper kernels

https://jupyter-client.readthedocs.io/en/latest/wrapperkernels.html

Customizing the kernel's runtime environment

https://jupyter-client.readthedocs.io/en/latest/provisioning.html

Pending Kernels

https://jupyter-client.readthedocs.io/en/latest/pending-kernels.html

Transport security for kernels

https://jupyter-client.readthedocs.io/en/latest/security.html

https://jupyter-client.readthedocs.io/en/latest/api/modules.html

Changes in Jupyter Client

https://jupyter-client.readthedocs.io/en/latest/changelog.html

Migration Guide

https://jupyter-client.readthedocs.io/en/latest/migration.html

System Settings

Messaging in Jupyter

https://jupyter-client.readthedocs.io/en/latest/messaging.html

Making kernels for Jupyter

https://jupyter-client.readthedocs.io/en/latest/kernels.html

Making simple Python wrapper kernels

https://jupyter-client.readthedocs.io/en/latest/wrapperkernels.html

Customizing the kernel's runtime environment

https://jupyter-client.readthedocs.io/en/latest/provisioning.html

Pending Kernels

https://jupyter-client.readthedocs.io/en/latest/pending-kernels.html

Transport security for kernels

https://jupyter-client.readthedocs.io/en/latest/security.html

https://jupyter-client.readthedocs.io/en/latest/api/modules.html

Changes in Jupyter Client

https://jupyter-client.readthedocs.io/en/latest/changelog.html

Migration Guide

https://jupyter-client.readthedocs.io/en/latest/migration.html

System Settings

This isn't a stack. It's a pile. Errors, perf, logs, hosts. One tool, one bill, built 4 devs who ship

https://server.ethicalads.io/proxy/click/10510/019f0193-150b-7c81-bf1a-5d7920879e7a/

Ad by EthicalAds

https://www.ethicalads.io/advertisers/topics/data-science/?ref=rtd-sidebar-buy-ads

Jupyter Client 8.9

https://jupyter-client.readthedocs.io/en/latest/#jupyter-client-version

This package provides the Python API for starting, managing and communicating with Jupyter kernels.

This document contains the authoritative description of the Jupyter messaging protocol. All developers are strongly encouraged to keep it updated as the implementation evolves, so that we have a single common reference for all protocol details.

User Documentation

Messaging in Jupyter

https://jupyter-client.readthedocs.io/en/latest/messaging.html

https://jupyter-client.readthedocs.io/en/latest/messaging.html#versioning

Introduction

https://jupyter-client.readthedocs.io/en/latest/messaging.html#introduction

General Message Format

https://jupyter-client.readthedocs.io/en/latest/messaging.html#general-message-format

Compatibility

https://jupyter-client.readthedocs.io/en/latest/messaging.html#compatibility

The Wire Protocol

https://jupyter-client.readthedocs.io/en/latest/messaging.html#the-wire-protocol

Kernel startup handshake

https://jupyter-client.readthedocs.io/en/latest/messaging.html#kernel-startup-handshake

https://jupyter-client.readthedocs.io/en/latest/messaging.html#python-api

Messages on the shell (ROUTER/DEALER) channel

https://jupyter-client.readthedocs.io/en/latest/messaging.html#messages-on-the-shell-router-dealer-channel

Messages on the Control (ROUTER/DEALER) channel

https://jupyter-client.readthedocs.io/en/latest/messaging.html#messages-on-the-control-router-dealer-channel

Messages on the IOPub (XPUB/SUB) channel

https://jupyter-client.readthedocs.io/en/latest/messaging.html#messages-on-the-iopub-xpub-sub-channel

Messages on the stdin (ROUTER/DEALER) channel

https://jupyter-client.readthedocs.io/en/latest/messaging.html#messages-on-the-stdin-router-dealer-channel

Heartbeat for kernels

https://jupyter-client.readthedocs.io/en/latest/messaging.html#heartbeat-for-kernels

Custom Messages

https://jupyter-client.readthedocs.io/en/latest/messaging.html#custom-messages

https://jupyter-client.readthedocs.io/en/latest/messaging.html#changelog

https://jupyter-client.readthedocs.io/en/latest/messaging.html#notes

Developer documentation

Making kernels for Jupyter

https://jupyter-client.readthedocs.io/en/latest/kernels.html

Connection files

https://jupyter-client.readthedocs.io/en/latest/kernels.html#connection-files

Handling messages

https://jupyter-client.readthedocs.io/en/latest/kernels.html#handling-messages

Kernel specs

https://jupyter-client.readthedocs.io/en/latest/kernels.html#kernel-specs

https://jupyter-client.readthedocs.io/en/latest/kernels.html#packaging

Making simple Python wrapper kernels

https://jupyter-client.readthedocs.io/en/latest/wrapperkernels.html

Required steps

https://jupyter-client.readthedocs.io/en/latest/wrapperkernels.html#required-steps

https://jupyter-client.readthedocs.io/en/latest/wrapperkernels.html#example

Optional steps

https://jupyter-client.readthedocs.io/en/latest/wrapperkernels.html#optional-steps

Customizing the kernel's runtime environment

https://jupyter-client.readthedocs.io/en/latest/provisioning.html

Kernel Provisioning

https://jupyter-client.readthedocs.io/en/latest/provisioning.html#kernel-provisioning

The kernel manager and kernel provisioner relationship

https://jupyter-client.readthedocs.io/en/latest/provisioning.html#the-kernel-manager-and-kernel-provisioner-relationship

https://jupyter-client.readthedocs.io/en/latest/provisioning.html#discovery

Backwards Compatibility

https://jupyter-client.readthedocs.io/en/latest/provisioning.html#backwards-compatibility

Implementing a custom provisioner

https://jupyter-client.readthedocs.io/en/latest/provisioning.html#implementing-a-custom-provisioner

Pending Kernels

https://jupyter-client.readthedocs.io/en/latest/pending-kernels.html

How they work

https://jupyter-client.readthedocs.io/en/latest/pending-kernels.html#how-they-work

Using pending kernels

https://jupyter-client.readthedocs.io/en/latest/pending-kernels.html#using-pending-kernels

Transport security for kernels

https://jupyter-client.readthedocs.io/en/latest/security.html

The transport\_encryption setting

https://jupyter-client.readthedocs.io/en/latest/security.html#the-transport-encryption-setting

Kernelspec requirements

https://jupyter-client.readthedocs.io/en/latest/security.html#kernelspec-requirements

Connection file fields

https://jupyter-client.readthedocs.io/en/latest/security.html#connection-file-fields

Implementing curve support in a kernel

https://jupyter-client.readthedocs.io/en/latest/security.html#implementing-curve-support-in-a-kernel

https://jupyter-client.readthedocs.io/en/latest/api/modules.html

jupyter\_client package

https://jupyter-client.readthedocs.io/en/latest/api/jupyter\_client.html

Changes in Jupyter Client

https://jupyter-client.readthedocs.io/en/latest/changelog.html

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id1

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id2

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id4

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id9

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id15

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id20

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id24

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id28

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id32

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id36

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id39

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id44

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id48

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id52

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id57

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id61

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id65

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id68

https://jupyter-client.readthedocs.io/en/latest/changelog.html#rc0

https://jupyter-client.readthedocs.io/en/latest/changelog.html#b3

https://jupyter-client.readthedocs.io/en/latest/changelog.html#b2

https://jupyter-client.readthedocs.io/en/latest/changelog.html#b1

https://jupyter-client.readthedocs.io/en/latest/changelog.html#b0

https://jupyter-client.readthedocs.io/en/latest/changelog.html#a4

https://jupyter-client.readthedocs.io/en/latest/changelog.html#a3

https://jupyter-client.readthedocs.io/en/latest/changelog.html#a2

https://jupyter-client.readthedocs.io/en/latest/changelog.html#a1

https://jupyter-client.readthedocs.io/en/latest/changelog.html#a0

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id98

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id103

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id107

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id110

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id114

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id118

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id122

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id125

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id128

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id133

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id136

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id141

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id146

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id149

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id153

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id156

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id159

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id163

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id165

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id171

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id172

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id173

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id174

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id175

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id176

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id177

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id178

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id179

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id180

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id181

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id182

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id183

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id184

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id185

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id186

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id187

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id188

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id189

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id190

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id191

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id192

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id193

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id194

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id195

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id196

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id197

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id198

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id201

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id203

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id205

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id209

https://jupyter-client.readthedocs.io/en/latest/changelog.html#id211

Migration Guide

https://jupyter-client.readthedocs.io/en/latest/migration.html

Jupyter Client 6.0 to 7.0

https://jupyter-client.readthedocs.io/en/latest/migration.html#jupyter-client-6-0-to-7-0

Indices and tables

https://jupyter-client.readthedocs.io/en/latest/#indices-and-tables

https://jupyter-client.readthedocs.io/en/latest/genindex.html

Module Index

https://jupyter-client.readthedocs.io/en/latest/py-modindex.html

Search Page

https://jupyter-client.readthedocs.io/en/latest/search.html

next Messaging in Jupyter

https://jupyter-client.readthedocs.io/en/latest/messaging.html

On this page

Jupyter Client 8.9

https://jupyter-client.readthedocs.io/en/latest/

Indices and tables

https://jupyter-client.readthedocs.io/en/latest/#indices-and-tables

Show Source

https://jupyter-client.readthedocs.io/en/latest/\_sources/index.rst.txt

© Copyright 2015, Jupyter Development Team.

Created using

https://www.sphinx-doc.org/

Built with the

PyData Sphinx Theme

https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html

https://jupyter-client.readthedocs.io/en/stable/

https://jupyter-client.readthedocs.io/en/5.2.3/

https://jupyter-client.readthedocs.io/en/5.2.2/

https://jupyter-client.readthedocs.io/en/5.2.1/

https://jupyter-client.readthedocs.io/en/5.2.0/

https://jupyter-client.readthedocs.io/en/5.1.0/

On Read the Docs

Project Home

https://app.readthedocs.org/projects/jupyter-client/?utm\_source=jupyter-client&utm\_content=flyout

https://app.readthedocs.org/projects/jupyter-client/builds/?utm\_source=jupyter-client&utm\_content=flyout

Addons documentation

https://docs.readthedocs.io/page/addons.html?utm\_source=jupyter-client&utm\_content=flyout

― Hosted by

Read the Docs

https://about.readthedocs.com/?utm\_source=jupyter-client&utm\_content=flyout

No recent searches

to navigate

Search powered by

