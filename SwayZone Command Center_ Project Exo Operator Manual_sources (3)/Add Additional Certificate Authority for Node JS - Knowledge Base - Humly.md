---
sourceFile: "Add Additional Certificate Authority for Node JS - Knowledge Base - Humly"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.128Z"
---

# Add Additional Certificate Authority for Node JS - Knowledge Base - Humly

158884a5-bb05-4ba5-8c4e-4afe6f145f84

Add Additional Certificate Authority for Node JS - Knowledge Base - Humly

9c308bd6-9d6b-441f-a2be-b48a2f1cf3cf

https://support.humly.com/add-additional-certificate-authority-for-node-js

Add Additional Certificate Authority for Node JS

This website stores cookies on your computer. These cookies are used to collect information about how you interact with our website and allow us to remember you. We use this information in order to improve and customize your browsing experience and for analytics and metrics about our visitors both on this website and other media. To find out more about the cookies we use, see our

Privacy Policy

http://humly.com/privacy-policy

If you decline, your information won't be tracked when you visit this website. A single cookie will be used in your browser to remember your preference not to be tracked.

javascript:void(0);

javascript:void(0);

Skip to content

https://support.humly.com/add-additional-certificate-authority-for-node-js#main-content

Customer portal

https://support.humly.com/tickets-view

https://support.humly.com/add-additional-certificate-authority-for-node-js

Show submenu for Resources

https://www.humly.com/partners

Blog and insights

https://blog.humly.com/

About Humly

https://www.humly.com/about

Book a Demo

https://www.humly.com/demo

https://www.humly.com/how-to-buy

Humly Academy

https://academy.humly.com/

Open main navigation Close main navigation

https://support.humly.com/add-additional-certificate-authority-for-node-js

Show submenu for Resources

https://www.humly.com/partners

Blog and insights

https://blog.humly.com/

About Humly

https://www.humly.com/about

Book a Demo

https://www.humly.com/demo

https://www.humly.com/how-to-buy

Humly Academy

https://academy.humly.com/

Customer portal

https://support.humly.com/tickets-view

Create a ticket

https://share.hsforms.com/1Bc4vZxO8TfmqIJ8UJcrtcA3uyw3

Create a ticket

https://share.hsforms.com/1Bc4vZxO8TfmqIJ8UJcrtcA3uyw3

Hello. How can we help you?

There are no suggestions because the search field is empty.

Knowledge Base

https://support.humly.com/

Administration

https://support.humly.com/administration

Administration

https://support.humly.com/administration#administration

Add Additional Certificate Authority for Node JS

I have received this error when trying to connect Humly Control Panel to Exchange Server or when trying to connect Humly Controle Panel to the booking system through a proxy server. What shall I do?

"UNABLE\_TO\_VERIFY\_LEAF\_SIGNATURE" or "UNABLE\_TO\_VERIFY\_FIRST\_CERTIFICATE"

In some installations, the exchange server/proxy uses a certificate issued by the local CA, to allow Node to trust this certificate authority, the CA has to be added to the (Trusted Root Certification Authorities) container.

Solution On Windows

The solution is to add "NODE\_EXTRA\_CA\_CERTS" Windows system variable with the path to Root CA certificate (or a chain with Intermediate CA) in PEM (Base64 / CRT ) format.

#### Option one:

Prepare/Export the CA certificate of the exchange server or the proxy server as Base64/CRT format and place a copy on Humly Control Panel server.

Open CMD as an administrator

Use this command to add the certificate, change the path to the place where you have placed the certificate file

setx NODE\_EXTRA\_CA\_CERTS "C:\Path\To\CA\_Root\_Cert.crt" -m

Reboot the server and start Humly Control Panel Wizard again.

#### Option two:

Open Windows Environment Variables

Add new variable

Add the following variable name "

NODE\_EXTRA\_CA\_CERTS

", click on browse file and select the CA CRT file

Reboot the server and start Humly Control Panel Wizard again.

#### Solution On Ubuntu:

Please follow the steps mentioned in the Ubuntu documentation link here

Installing a root CA certificate in the trust store

https://ubuntu.com/server/docs/security-trust-store

To export the Root Certificate Authority (CA) from a working certificate in a browser, you can follow these general steps depending on your browser:

#### For Google Chrome:

#### Open the Certificate Viewer:

Navigate to the site that uses the certificate in question.

Click the padlock icon in the address bar.

Click on "Connection is secure" (or a similar option depending on the Chrome version).

Click on "Certificate is valid."

#### View the Certificate Chain:

In the Certificate window, go to the "Certification Path" tab.

Here, you'll see a hierarchy of certificates. The top one is usually the Root CA, in this case, you are looking for the "Basel" root CA.

#### Export the Root CA:

Select the top-level certificate (Root CA).

Click "View Certificate."

In the new window, go to the "Details" tab.

Click "Copy to File…" to start the Certificate Export Wizard.

Choose the format (usually DER or Base-64 encoded X.509).

Save the file to your desired location.

#### For Microsoft Edge:

#### Open the Certificate Viewer:

Similar to Chrome, click on the padlock icon in the address bar.

Click on "Connection is secure" or "Certificate (valid)."

#### View the Certificate Chain:

In the Certificate window, go to the "Certification Path" tab.

Select the Root CA (look for "Basel").

#### Export the Root CA:

Click "View Certificate."

Go to the "Details" tab.

Click "Copy to File…" and save the certificate.

Was this article helpful?

Getting started!

https://support.humly.com/getting-started#main-content

Introduction

https://support.humly.com//getting-started#introduction

Step 1: Booking System Preparation

https://support.humly.com//getting-started#step-1-booking-system-preparation

Step 2: Humly Control Panel Installation

https://support.humly.com//getting-started#step-2-humly-control-panel-installation

Step 3: Connect HCP to Booking System

https://support.humly.com//getting-started#step-3-connect-hcp-to-booking-system

Step 4: HCP Basic Setup - Global Settings

https://support.humly.com//getting-started#step-4-hcp-basic-setup-global-settings

Step 5: HCP Basic Setup - Add Buildings and Structure

https://support.humly.com//getting-started#step-5-hcp-basic-setup-add-buildings-and-structure

Step 6: Add licenses

https://support.humly.com//getting-started#step-6-add-licenses

Step 7: Humly Room Display installation

https://support.humly.com//getting-started#step-7-humly-room-display-installation

Step 8: Humly Booking Device Installation

https://support.humly.com//getting-started#step-8-humly-booking-device-installation

Humly Room Display

https://support.humly.com/humly-room-display#main-content

Humly Room display

https://support.humly.com//humly-room-display#humly-room-display

Humly Booking Device

https://support.humly.com/humly-booking-device#main-content

Desk Control

https://support.humly.com//humly-booking-device#desk-control

Release Notes

https://support.humly.com//release-notes

Administration

https://support.humly.com/administration#main-content

Administration

https://support.humly.com//administration#administration

Humly Control Panel

https://support.humly.com/humly-control-panel#main-content

https://support.humly.com//humly-control-panel#users

Room Settings

https://support.humly.com//humly-control-panel#room-settings

https://support.humly.com//humly-control-panel#statistics

Guest Account

https://support.humly.com//humly-control-panel#guest-account

https://support.humly.com//humly-control-panel#general

Humly Reservations

https://support.humly.com/humly-reservations#main-content

Humly Reservations

https://support.humly.com//humly-reservations#humly-reservations

Humly Visitor

https://support.humly.com/humly-visitor#main-content

Outlook Add-in

https://support.humly.com//humly-visitor#outlook-add-in

Humly Wayfinding

https://support.humly.com//humly-wayfinding

Humly Floor Plan

https://support.humly.com/humly-floor-plan#main-content

Humly Floor Plan - Admin Guide

https://support.humly.com//humly-floor-plan#humly-floor-plan-admin-guide

User and Interactive Booking Guide

https://support.humly.com//humly-floor-plan#user-and-interactive-booking-guide

Humly Sense

https://support.humly.com/humly-sense#main-content

Humly Sense overview

https://support.humly.com//humly-sense#humly-sense-overview

Humly Sense integrations

https://support.humly.com//humly-sense#humly-sense-integrations

Humly Sense configuration

https://support.humly.com//humly-sense#humly-sense-configuration

Latest News

https://support.humly.com/latest-news#main-content

Technical News

https://support.humly.com//latest-news#technical-news

https://support.humly.com/faq#main-content

General FAQ

https://support.humly.com//faq#general-faq

Global Settings

https://support.humly.com//faq#global-settings

Humly Solutions AB | Sveavägen 124, 113 50 Stockholm

https://www.humly.com/

https://www.linkedin.com/company/humly

mailto:support@humly.com

Copyright © 2026, Humly Solutions AB

Ask me anything…

