---
sourceFile: "OCSP vs CRL Explained - Smallstep"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.677Z"
---

# OCSP vs CRL Explained - Smallstep

2c471f12-fb43-432a-addc-ab5e0975f541

OCSP vs CRL Explained - Smallstep

b9c6f549-8e68-4ee9-9669-a3df30e9bea9

https://smallstep.com/blog/ocsp-vs-crl-explained/

OCSP vs CRL Explained

Sign up for our Device Identity Webinar Series! Sign up for our Device Identity Webinar Series! Sign up for our Device Identity Webinar Series!

https://go.smallstep.com/webinars

https://smallstep.com/case-studies/

https://smallstep.com/pricing/

https://smallstep.com/app/

Book a demo

https://smallstep.com/webforms/book-a-demo/

OCSP vs CRL Explained

Updated on: January 8, 2025

Linda Ikechukwu

Follow Smallstep

https://twitter.com/smallsteplabs

Let's Encrypt, the non-profit Certificate Authority that offers free SSL/TLS certificates for secure HTTPS connections,

has announced plans to end OCSP support in favor of CRLs.

https://letsencrypt.org/2024/07/23/replacing-ocsp-with-crls.html

What are those, and why?

Read on to to find out

Online Certificate Status Protocol

) and CRL (

Certificate Revocation Lists

) are methods provided by Certificate Authorities (CA) for browsers to check if a web server's certificate has been revoked before establishing a connection.

Just like international passports or student IDs, digital certificates have expiry dates. The shorter the expiry date, the safer they are. After expiration, certificates become invalid.

However, what if a certificate is compromised before its expiry date? Maybe it was wrongfully issued, is now associated with a domain that has new owners, or the private keys have been stolen.

For example, when a student is expelled due to misconduct, their IDs become invalid even though it hasn't expired because their graduation date hasn't arrived.

Similarly, a certificate should be revoked and become invalid and untrustworthy when something serious happens. But, once the certificate holder and CA have revoked a certificate, how do browsers know to avoid establishing insecure connections?

This is where OCSP or CRL comes into play.

When a certificate is issued, Certificate Authorities provide a URL (or URI) from which the certificate's revocation status can be retrieved. This URL could be an OCSP server URL or a CRL URL status. It's like saying, “Please phone this number to check that this certificate has not been revoked.”

If a certificate has been revoked, the browser shows an error like below, advising that the certificate used by the website has been revoked and it's unsafe to continue:

OCSP (Online Certificate Status Protocol)

OCSP, described by

https://datatracker.ietf.org/doc/html/rfc6960

, defines an API for retrieving the real-time revocation status of a specific certificate from the issuing CA.

Web browsers and other relying parties can send a request to an OCSP server for information on the status of a certificate. The OCSP server (or responder) has access to the database that tracks the status of all certificates issued by a CA using their serial numbers. Individual CAs typically maintain their own database and OCSP responder.

#### Something like this:

If a certificate authority supports OCSP, the OCSP responder URL is included in the certificate info. For example, here is the OCSP URL for a revoked certificate. You can find the OCSP URL under the Authority Information Access field in a certificate's details, as shown bellow:

During a TLS handshake, when you enter a URL, like

https://letsencrypt.org/

into your browser, the browser contacts the web server to request its certificate and determine if it's safe to establish a connection. Then, your browser makes a GET request to the OCSP responder URL about the status of that specific certificate using its serial number. The responder checks the certificate's status in the CA's database and returns the result (good, revoked, or unknown) to the browser.

Let's see this in action. I'll query the status of Let's Encrypt's website certificate from it's listed OCSP server, using the step CLI tool.

The step CLI is an open-source easy-to-use CLI tool maintained by us at Smallstep for building, operating, and automating Public Key Infrastructure (PKI) systems and workflows. it is acts as the front-end interface to step-ca, an open-source X.509 and SSH Certificate Authority (CA). You can learn more about it and see the command reference

https://smallstep.com/docs/step-cli/

First, get the OCSP responder URL for the site's certificate by running the command below:

step certificate inspect https://letsencrypt.org/ --format json

The command above prints the details of the certificate in JSON format. You should see the OCSP URI under the

authority\_info\_access

field, like so:

"authority\_info\_access": {
    "ocsp\_urls": \[
        "http://e6.o.lencr.org"
    \],
    "issuer\_urls": \[
        "http://e6.i.lencr.org/"
    \]
},

Now that we have the OCSP responder URI, let's query it for the revocation status of the certificate. Run the command below:

step certificate verify https://letsencrypt.org  --verify-ocsp --ocsp-endpoint http://e6.o.lencr.org

The command above verifies the certificate against it's specified OCSP endpoint. If the certificate is valid this command will return '0'. If validation fails, or if an error occurs, this command will produce a non-zero return value. Here's an expected result:

$ step certificate verify https://letsencrypt.org  --verify-ocsp --ocsp-endpoint http://e6.o.lencr.org
$ echo $?
0
$ step certificate verify https://letsencrypt.org  --verify-ocsp --ocsp-endpoint http://not-an-ocsp-server
could not verify certificate against OCSP server(s)
exit status 1

CRL (Certificate Revocation Lists)

On the other hand, CRL is more of an offline way of verifying certificate revocation status.

A Certificate Revocation List (CRL) is a periodically updated list of the serial numbers of all certificates revoked by a Certificate Authority (CA), along with the timestamp of when each certificate was revoked, in one big downloadable data structure.

When a certificate is revoked, the CA updates its records to reflect the revocation. At defined intervals (could be every 24 hours, every 4 days, twice a month, e.t.c), the CA compiles a list of current, non-expired revoked certificates into a new CRL and publishes it to their public CRL URL.

The specific validity period for a CRL is defined in the CRL file itself under the “Next Update” field. This field indicates when the next CRL will be issued and when the current CRL will expire.

#### Something like this:

So, during a TLS handshake, if an OCSP URL is not provided, browsers first check if they have downloaded a valid CRL for the issuing certificate authority. If the downloaded CRL list has expired, the browser will download a new list from the CRL URL and check if the certificate's serial number is listed in the CRL.

It's important for browsers to frequently check for and download the latest CRL to maintain security.

#### The problem with the CRL revocation status check method is that:

CRL does not provide real time revocation status

Downloading a massive list of revoked certificates every time a connection is established would be slow and resource-intensive, so CRLs are usually cached. Caching creates a delay between when a certificate is revoked and when a relying party notices. This delay means there's a risk of a browser accepting a revoked certificate unknowingly, making CRLs less ideal for security-sensitive environments.

Despite this concerning problem and the fact that OCSP was introduced to address the shortcomings of the CRL, why is the CRL method now favored over OCSP?

Why the Industry Is Shifting Away from OCSP

In August of 2023 the

CA/Browser Forum

https://cabforum.org/

(the industry's standard body) passed a ballot to make CRLs a requirement and OCSP optional for publicly trusted CAs like Let's Encrypt.

#### It's because of three major reasons:

OCSP introduces privacy concerns

OCSP requests can expose user browsing behavior. Each request includes the certificate's serial number, which can be linked to the associated domain. The OCSP responder logs these requests, capturing the client's IP address. Over time, these logs can reveal which IP addresses access which websites. There is a risk that these logs could be shared with or accessed by third parties, potentially for surveillance purposes.

In contrast, CRLs preserve privacy because the querying web browser isn't required to send information about a specific website.

OCSP requests are vulnerable to interception

OCSP requests are sent over plain HTTP, not HTTPS. This lack of encryption allows anyone intercepting the traffic to view and modify the request and response. An attacker can alter the OCSP response to show a “good” status for a revoked certificate or block the response entirely, causing the client to proceed without proper revocation checking.

In contrast, CRLs are downloaded and stored locally, eliminating real-time network communication that could be intercepted. They are also signed by the issuing CA and are tamper-evident.

OCSP is resource intensive

Supporting OCSP introduces significant architectural and operational complexity. It requires high availability of both the CA and the OCSP servers, along with precise clock synchronization between them. They can't go down for over a minute or two; otherwise, things will break. Because of this, most browsers do not support OCSP implementation to avoid unnecessary glitches.

And that's why Let's Encrypt is opting to end OCSP support in favor of CRLs.

At Smallstep, especially for internal PKI implementations, we advocate for

passive revocation

https://smallstep.com/blog/passive-revocation/

instead of OCSP and CRL revocation checking because it is easier to implement and operate. If you'd like to learn more about certificates and Web PKI, see the links below:

Web PKI vs Internal PKI

https://www.youtube.com/watch?v=5weGQRwotas

Everything you should know about certificates and PKI but are too afraid to ask

https://smallstep.com/blog/everything-pki/

https://lindaikechukwu.com/

is a wannabe guitarist, who reads African literature or fiddles with a tennis racket to unwind while navigating the daily grind of helping growth-stage tech startups drive adoption and awareness of their products through tailored content strategies that translate concepts from arcane technical domains into plain and accessible language.

Introducing

Device Identity

Ensure that only company-owned devices can access your enterprise's most sensitive resources.

https://smallstep.com/signup/?utm\_campaign=workloads-banner&utm\_medium=blog&utm\_source=website

Subscribe to updates

Smallstep respects your privacy and will only use your information to administer your account and to provide a great product experience.

Occasionally, we would like to share other content and offers that may be of interest to you. Please choose how you would like to be contacted: If you consent to us contacting you for this purpose, below to say how you would like us to contact you:

Get updates from Smallstep. Unsubscribe anytime.

Unsubscribe anytime. View our

Privacy Policy

https://smallstep.com/privacy-policy/

By submitting this form, you allow Smallstep to store and process the information provided in accordance with our

Privacy Policy

https://smallstep.com/privacy-policy/

Further Reading

Device identity

After Mythos: Identity Has to Anchor in Hardware

Daniel Michan May 7, 2026\](https://smallstep.com/blog/after-mythos-hardware-bound-identity/)

Device identity

Shadow IT Exists Because You Don't Control Which Devices Get Identity

Daniel Michan March 27, 2026\](https://smallstep.com/blog/shadow-it-is-an-admission-failure/)

Device identity

Stryker Was Wiped Through Its Own Infrastructure

Daniel Michan March 23, 2026\](https://smallstep.com/blog/stryker-was-not-ransomwared-it-was-remotely-wiped/)

Device Identity for companies with sensitive resources. Secure corporate Wi-Fi, SaaS Apps, VPNs, and more.

https://smallstep.com/blog/

Documentation

https://smallstep.com/docs/platform/

Data sheets

https://smallstep.com/data-sheets/

Case studies

https://smallstep.com/case-studies/

Open source

https://smallstep.com/open-source/

https://support.smallstep.com/

Get started

Request demo

https://smallstep.com/webforms/contact-us/

Platform overview

https://smallstep.com/docs/platform/

Integrations

https://smallstep.com/integrations/

https://status.smallstep.com/

Privacy Preferences

Privacy Policy

https://smallstep.com/privacy-policy/

Terms of use

https://smallstep.com/terms-of-use/

https://smallstep.com/security/

https://smallstep.com/webforms/contact-us/

https://jobs.ashbyhq.com/smallstep

https://smallstep.com/case-studies/

https://smallstep.com/partner-with-smallstep/

https://smallstep.com/about/#investors

https://smallstep.com/tags/announcements/

https://smallstep.com/media/

https://twitter.com/smallsteplabs

https://www.linkedin.com/company/smallstep

https://github.com/smallstep

https://bit.ly/step-discord

Copyright © 2026 Smallstep Labs, Inc. All rights reserved.

Device Identity for companies with sensitive resources. Secure corporate Wi-Fi, SaaS Apps, VPNs, and more.

Get started

https://twitter.com/smallsteplabs

https://www.linkedin.com/company/smallstep

https://github.com/smallstep

https://bit.ly/step-discord

Copyright © 2026 Smallstep Labs, Inc. All rights reserved.

This site uses cookies. You may modify non-essential cookies at any time. Please view our relevant third party privacy policies for more information.

Reject all Save preferences

