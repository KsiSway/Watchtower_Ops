---
sourceFile: "Replacing OCSP with CRL as the method of certificate revocation checking"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.689Z"
---

# Replacing OCSP with CRL as the method of certificate revocation checking

b244068a-489a-4563-b0e1-0e83c09c84be

Replacing OCSP with CRL as the method of certificate revocation checking

62ce2471-bc81-4df3-a50d-7854e4e0a68b

https://community.snowflake.com/s/article/Replacing-OCSP-with-CRL-as-the-method-of-certificate-revocation-checking

Replacing OCSP with CRL as the method of certificate revocation checking

https://community.snowflake.com/s/article/Replacing-OCSP-with-CRL-as-the-method-of-certificate-revocation-checking

Sorry to interrupt

https://community.snowflake.com/s/article/Replacing-OCSP-with-CRL-as-the-method-of-certificate-revocation-checking?nocache=https%3A%2F%2Fcommunity.snowflake.com%2Fs%2Farticle%2FReplacing-OCSP-with-CRL-as-the-method-of-certificate-revocation-checking

Toggle Menu

CREATE ACCOUNT SIGN IN

KNOWLEDGE BASE ARTICLES

Can't find what you're looking for?

Ask The Community

Replacing OCSP with CRL as the method of certificate revocation checking

This article provides information about upcoming infrastructure changes related to OCSP-based certificate validation. These changes will initially affect accounts hosted on GCP and, later, AWS and Azure.

October 21, 2025

The Certificate Authority (CA) industry and Cloud Service Providers (CSPs) are continually refining their best practices for certificate technologies and revocation management.

A key mechanism in this area has been OCSP, which enables user-agents (like browsers and Snowflake drivers) to validate in real-time that a TLS certificate has not been revoked. However, many CAs and CSPs are now phasing out OCSP support. Notably,

Let's Encrypt

https://www.feistyduck.com/newsletter/issue\_121\_the\_slow\_death\_of\_ocsp

(the world's largest CA) and

Google Trust Services

https://pki.goog/updates/october2025-ocsp-update.html

leading this deprecation.

For more details, please see (non-Snowflake site)

\[Servercert-wg\] IPR Review period for SC63: Make OCSP optional, require CRLs, and incenctivize automation

https://lists.cabforum.org/pipermail/servercert-wg/2023-September/003998.html

This trend signals a broader shift in the security industry, moving away from OCSP and revocation checking in favour of short-lived certificates. Snowflake is aligning with this evolving best practice by preparing for OCSP's deprecation.

The article is targeted towards Google Cloud Platform (GCP) because GCP has indicated it will phase out OCSP; originally in November 2025, later pushed out to May 2026. However, as mentioned above, this reflects a broader industry trend, so please consider it relevant for the future in AWS and Azure too.

A note on certificate validation flows

The first layer of certificate validation always happens during the TLS handshake procedure upon connection establishment.

This is regardless of which cloud provider is used, and which Snowflake client driver is used.

The below change does not affect this first and primary level of certificate validation! This will always happen, as part of establishing the connection, it is not optional

, and our client drivers don't expose ways to turn this validation off.

OCSP is currently used as a secondary layer

of certificate validation (revocation checking), which only happens after the primary (TLS) validation is successful. OCSP checking is enabled by default but

entirely optional

, and all Snowflake client drivers expose an easily accessible way to disable such checks

How to turn off OCSP checking in Snowflake client drivers

https://community.snowflake.com/s/article/How-to-turn-off-OCSP-checking-in-Snowflake-client-drivers

Detailed Information

Starting from early May 2026 (originally was November 2025, see

https://pki.goog/updates/october2025-ocsp-update.html

article), Google Trust Services (GTS) will issue certificates which no longer embed OCSP information. This change will impact Snowflake customers on GCP who have OCSP checking enabled with mode

https://docs.snowflake.com/en/user-guide/ocsp#fail-close

We anticipate that other CAs and cloud service providers (CSPs) will adopt similar practices. While much of the mitigation outlined here is expected to apply to Azure and AWS environments, a separate notification will be issued once more information becomes available.

Additional Information

How to determine if you are impacted?

#### Possibly impacted:

If your CSP is GCP and have OCSP checking enabled in

https://docs.snowflake.com/en/user-guide/ocsp#fail-close

mode in ODBC, JDBC, Python, Go, node.js or PHP Drivers.

#### Not impacted:

If you did not configure the OCSP mode

in your client driver, and left it on the default

https://docs.snowflake.com/en/user-guide/ocsp#fail-open

If you use the Snowflake .NET Driver

regardless of the CSP (Snowflake .NET driver always used CRL as the method of secondary certificate revocation check)

If your Snowflake account is on GCP and

OCSP checking is already disabled

in your client driver

How to turn off OCSP checking in Snowflake client drivers

https://community.snowflake.com/s/article/How-to-turn-off-OCSP-checking-in-Snowflake-client-drivers

If your Snowflake account is on Azure or AWS

Note: statement is only relevant for the first wave of the change, which only happens in GCP. In the future, it could happen for other CSP too.

The guidelines above apply regardless of the method you use to connect to Snowflake. That is, clients using either Public and PrivateLink connectivity will see changes in certificates presented by GCP.

How can I determine which users, hosts use which driver versions, and what the OCSP related settings are?

Please feel free to use the existing article for

How to report on the Clients connecting to a snowflake account?

https://community.snowflake.com/s/article/how-to-report-on-the-clients-connecting-to-a-snowflake-account

, which you can modify to query ACCOUNT\_USAGE Session data to retrieve such information.

Example query to retrieve user name, source IP, driver type and version, OCSP mode:

s.user\_name,

lh.client\_ip,

s.client\_application\_id,

PARSE\_JSON(s.client\_environment):APPLICATION :: string AS app,

when PARSE\_JSON(s.client\_environment):OCSP\_MODE = 'INSECURE' then 'OCSP\_CHECKS\_DISABLED'

when PARSE\_JSON(s.client\_environment):OCSP\_MODE = 'FAIL\_CLOSED' then 'OCSP\_FAIL\_CLOSED'

when PARSE\_JSON(s.client\_environment):OCSP\_MODE = 'FAIL\_OPEN' then 'OCSP\_FAIL\_OPEN'

else PARSE\_JSON(s.client\_environment):OCSP\_MODE end ocsp\_mode,

COUNT(s.session\_id) AS num\_sessions

FROM snowflake.account\_usage.sessions s

LEFT JOIN snowflake.account\_usage.login\_history lh

ON lh.event\_id = s.login\_event\_id

-- last 3 months, please modify per your requirements

s.created\_on >= DATEADD(day, -90, current\_date())

app not ilike 'Snowflake Web App%' --Snowsight GUI

and client\_application\_id not ilike '%SNOWFLAKE UI%' --Classic GUI

and client\_application\_id not ilike '%SQLAPI%' --SQL REST API v2

GROUP BY ALL

ORDER BY num\_sessions DESC

#### Example output:

regardless of whether you're impacted or not, Snowflake always strongly recommends upgrading and using the latest client drivers

to make sure the resilience to the demands of an ever-changing cloud environment and other factors (bug fixes, new features, performance improvements) are available at your disposal.

#### Related documentation:

Recommended client versions

https://docs.snowflake.com/en/release-notes/requirements#recommended-client-versions

If you're using Snowflake client drivers with OCSP checks disabled.

Action needed

If you have been using Snowflake client drivers with OCSP checks enabled, in fail-open mode - this is the default mode, if you did not configure anything specifically.

Action needed

: from a secondary certificate validation standpoint, there is no practical difference between fail-open mode and OCSP checking disabled:

: OCSP validation is attempted, but if it fails for

kind of reason, the connection still proceeds, without OCSP. (Reference:

https://docs.snowflake.com/en/user-guide/ocsp#fail-open

https://docs.snowflake.com/en/user-guide/ocsp#fail-open

https://docs.snowflake.com/en/user-guide/ocsp#fail-open

) . Thus eventually, when it's not possible to perform OCSP checks (third party infrastructure problems for example), the

connection still proceeds without OCSP

, just prior to it, consumes resources and introduces extra processing time.

OCSP checking disabled

( disableOCSPChecks flag, earlier called insecureMode): the driver does not even attempt performing OCSP validation, just proceeds with connection. This is the most performant option.

If you have been using Snowflake client drivers, with OCSP enabled in fail-close mode.

Action needed

: Evaluate your threat model and decide if certificate revocation checking is important.

#### Some things to consider:

For a successful attack using Snowflake private key, the attacker must already control your DNS servers or be close to the source of the traffic.

If your jobs connect to Snowflake via PrivateLink, then the attackers must already have privileged access to your critical infrastructure and a stolen private key doesn't give them an edge.

If certificate revocation checking is critical

Snowflake is going to publish a new version of drivers planned in September 2025, with support for CRL checking instead of OCSP. Because the performance characteristics of CRL checking are environment and workload dependent, you must confirm via testing that this mode works correctly with your infrastructure and tools (please read the CRL enablement guideline).

Once your testing is satisfactory, upgrade your driver versions (see Client Versions table below).

The relevant Snowflake system functions (

SYSTEM$ALLOWLIST

https://docs.snowflake.com/en/sql-reference/functions/system\_allowlist

SYSTEM$ALLOWLIST\_PRIVATELINK

https://docs.snowflake.com/sql-reference/functions/system\_allowlist\_privatelink

will be of course enhanced to accommodate the relevant CRL endpoints, which -similarly how it worked with OCSP- should be allowed on the corporate network, policies, firewalls, proxies, etc. if one would need CRL checking to be enabled, in order for those endpoints to be actually reachable for the client driver to perform the certificate revocation check.

If certificate revocation checking is not critical

Upgrade your client driver (see Client Versions table below) and disable OCSP checks

How to turn off OCSP checking in Snowflake client drivers

https://community.snowflake.com/s/article/How-to-turn-off-OCSP-checking-in-Snowflake-client-drivers

But aren't you removing a crucial security feature by disabling OCSP checking and not using CRL?

From Snowflake's perspective, we take a principled stance toward Reliability/Availability and Security tradeoffs. With OCSP based revocation checks and fail-closed behaviour, we have seen customers experience a significant reduction in reliability. Snowflake has built our own mitigations for these issues, including providing a pre-populated OCSP cache for clients and enabling OCSP stapling where possible. However, with the transition to CRLs, which may be of arbitrary size (double or even triple digit

) and thus may require significant processing and memory capacity, we do not find the same analysis leads to the same conclusion; the reliability and availability tradeoffs lead us to recommend disabling these checks.

When CRL support is available (see Client Versions table below), we will support customers enabling it, with the understanding that it will introduce availability and resource consumption risks. Versus OCSP, CAs are still obligated to propagate CRLs on the same timeline.

Regardless, attackers would still need control over other parts of a customer's infrastructure to execute an attack intercepting Snowflake traffic. That is, they'd likely need to control DNS or parts of the network; obtaining a certificate's private key is insufficient.

Driver Versions

Minimum version for disable\_ocsp\_checks = true flag availability (see Note below)

Minimum version for CRL check capability

Libsnowflake

N/A since .NET only supports CRL\*

: disabling OCSP checks is still very well possible in older drivers too. Please see the article

How to turn off OCSP checking in Snowflake client drivers

https://community.snowflake.com/s/article/How-to-turn-off-OCSP-checking-in-Snowflake-client-drivers

We still recommend upgrading to the

\*Note: for Snowflake .NET driver, it always used CRL as certificate revocation check mechanism. However starting from v5.0.0, it uses an improved implementation which is also streamlined to be more in-sync with the implementation used in the other drivers as well.

CRL Enablement Guideline

: Snowflake is not responsible for CRL infrastructure, which is operated by its respective third parties and accessible worldwide. Snowflake cannot guarantee CRL infrastructure's availability and performance.

⚠ If you enabled CRL validation and it fails due to network connectivity issues, you possibly won't be able to connect to Snowflake. This will stop your workloads and may require extensive changes to disable CRL checking.

CRL-based revocation checking is disabled by default because it may significantly impact performance and memory utilisation and may not work in all environments.

#### Modes of operation:

(default) - driver performs a full TLS certificate validation as part of the connection process, and does not check CRL for revocation

- driver checks CRL for revocation, logs the findings, and proceeds with connecting even if the CRL check was unsuccessful for

reason (certificate is revoked, or revocation could not be checked due to third-party infrastructure problems). This is analogous to the previous OCSP FAIL\_OPEN mode.

WARNING - this might have a negative effect on your Snowflake workload!

The driver checks CRL for revocation, logs the findings, and if the CRL check was unsuccessful for

reason (certificate is found to be revoked, but also even if it's just the third party CRL endpoint was unreachable) then stops with connecting to Snowflake.

In this case, your workload will stop working.

We plan to publish further information and baseline alongside the general CRL check availability in drivers

Before enabling CRL-based revocation check, please ensure that your workloads can reach CRL lists published by the CAs. You may need to allowlist the domains in production proxies and firewalls.

We plan to prepare the existing SYSTEM$ALLOWLIST function to return the relevant CRL endpoints (currently it returns OCSP endpoints)

Before enabling CRL-based revocation checks in production, you should test your workloads and adjust allocated RAM, CPU, and disk resources to levels sufficient for correct operation.

Certificate Revocation Lists (CRLs) introduce an initial overhead for the first query, increasing connection time by ~2 seconds due to multiple CRL downloads and parsing, authentication, and query requests. Subsequent queries are not significantly impacted. While the caching of CRLs mitigates the time overhead, there's a substantial increase in memory usage when CRL checking is enabled.

Further baseline testing will be published in a later date

Was this article helpful?

HELPFUL LINKS

Support Portal Case Submission Updates

https://community.snowflake.com/s/article/How-To-Submit-a-Support-Case-in-Snowflake-Lodge

Snowflake Global Support Phone Numbers

https://community.snowflake.com/s/article/Snowflake-Support-Global-Phone-Numbers

Snowflake Status Page

https://status.snowflake.com/

Release Notes

https://docs.snowflake.com/en/release-notes/new-features.html

Behavior Changes

https://community.snowflake.com/s/article/Pending-Behavior-Change-Log

MOST VIEWED

Undropping and restoring an account in Snowflake

https://community.snowflake.com/s/article/Undropping-and-restoring-an-account-in-Snowflake

Dropping an account in Snowflake

https://community.snowflake.com/s/article/Dropping-an-account-in-Snowflake

Understanding Micro-partitions and Data Clustering

https://community.snowflake.com/s/article/understanding-micro-partitions-and-data-clustering

Enabling JDBC Driver Debugging in DBeaver

https://community.snowflake.com/s/article/Enabling-JDBC-Driver-Debugging-in-DBeaver

OAuth 2.0 Client Credentials Grant to Snowflake with Microsoft Entra ID

https://community.snowflake.com/s/article/Create-External-OAuth-Token-Using-Azure-AD-For-The-OAuth-Client-Itself

Nothing found

Documentation

https://docs.snowflake.net/

Education & Training

https://www.snowflake.com/en/resources/learn/training/

Snowflake University

https://learn.snowflake.com/

Get Started in the Snowflake Community

https://community.snowflake.com/s/community-help

Knowledge Base

https://community.snowflake.com/s/knowledgebase

https://www.snowflake.com/product/

Architecture

https://www.snowflake.com/product/architecture/

https://www.snowflake.com/product/security/

https://www.snowflake.com/product/pricing/

About Snowflake

https://www.snowflake.com/about/

https://www.snowflake.com/about/snowflake-team/

https://www.snowflake.com/about/board/

https://www.snowflake.com/about/careers/

Sign Up for snowflake

\*\* communications\*\*

United States

United Kingdom

Aland Islands

American Samoa

Antigua and Barbuda

Bosnia and Herzegovina

Bouvet Island

British Indian Ocean Territory

Brunei Darussalam

Burkina Faso

Cayman Islands

Central African Republic

Christmas Island

Cocos (Keeling) Islands

Congo The Democratic Republic of The

Cook Islands

Cote D'Ivoire (Ivory Coast)

Croatia (Hrvatska)

Czech Republic

Dominican Republic

El Salvador

Equatorial Guinea

Falkland Islands (Malvinas)

Faroe Islands

French Guiana

French Polynesia

French Southern Territories

Guinea-Bissau

Heard and McDonald Islands

Holy See (Vatican City State)

Isle of Man

Korea Republic of (South)

Lao People's Democratic Republic

Liechtenstein

Marshall Islands

Micronesia Federated States of

Moldova Republic of

Netherlands

Netherlands Antilles

New Caledonia

New Zealand

Norfolk Island

Northern Mariana Islands

Palestinian Territory Occupied

Papua New Guinea

Philippines

Puerto Rico

Russian Federation

Saint Helena

Saint Kitts and Nevis

Saint Lucia

Saint Pierre and Miquelon

Saint Vincent and the Grenadines

Sao Tome and Principe

Saudi Arabia

Sierra Leone

Solomon Islands

South Africa

South Georgia and The South Sandwich Island

Svalbard and Jan Mayen Islands

Switzerland

Tanzania United Republic of

Timor-Leste

Trinidad and Tobago

Turkmenistan

Turks and Caicos Islands

United Arab Emirates

United Kingdom

United States Minor Outlying Islands

Virgin Islands (British)

Virgin Islands (U.S.)

Wallis and Futuna Islands

Western Sahara

By submitting this form, I understand Snowflake will process my personal information in accordance with their

Privacy Notice

. Additionally, I consent to my information being shared with Event Partners in accordance with Snowflake's

Event Privacy Notice

. I understand I may withdraw my consent or update my preferences

at any time.

Subscribe Now

Privacy Notice

https://www.snowflake.com/privacy-policy/

https://www.snowflake.com/legal/snowflake-community-terms-of-service/

Cookies Settings

javascript:void(0);

Do not Share My personal Information

https://www.snowflake.com/privacy-policy/#12

© 2026 Snowflake Inc. All Rights Reserved | If you'd rather not receive future emails from Snowflake,

unsubscribe here

https://info.snowflake.com/2024-Preference-center.html

or customize your communication preferences

Replacing OCSP with CRL as the method of certificate revocation checking

Snowflake's Use of Cookies

We use cookies to enhance your experience and to analyze site traffic as described in our Cookie Statement. By accepting, you consent to our use of cookies.

Cookie Statement.

https://www.snowflake.com/privacy-policy/cookie-statement/

Cookies Settings Reject All Accept All Cookies

Privacy Preference Center

Opt-Out Request Honored

Privacy Preference Center

Your Privacy

Your Privacy

When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences, or your device, and is mostly used to make the site work as you expect. The information does not usually identify you directly, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to learn more and change our default settings. Blocking some types of cookies may impact your experience of the site and the services we are able to offer.

More information

https://cookiepedia.co.uk/giving-consent-to-cookies

Strictly Necessary Cookies

Strictly Necessary Cookies

Always Active These cookies are necessary for the website to function and cannot be switched off. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information. Cookies Details

Performance Cookies

Performance Cookies

\[-\]  Performance Cookies These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance. Cookies Details

Functional Cookies

Functional Cookies

\[-\]  Functional Cookies These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly. Cookies Details

Targeting Cookies

Targeting Cookies

\[-\]  Targeting Cookies These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly identifiable personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising. Cookies Details

Cookie List

Consent Leg.Interest

checkbox label label

checkbox label label

checkbox label label

checkbox label label

Apply Cancel

Confirm My Choices

