---
sourceFile: "How to add custom certificate authority (CA) to nodejs - Stack Overflow"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.496Z"
---

# How to add custom certificate authority (CA) to nodejs - Stack Overflow

e2c887af-3fea-493e-8e75-81cb1acc17fe

How to add custom certificate authority (CA) to nodejs - Stack Overflow

e38f0fd5-f8c1-4211-8344-8674cd13d95a

https://stackoverflow.com/questions/29283040/how-to-add-custom-certificate-authority-ca-to-nodejs

node.js - How to add custom certificate authority (CA) to nodejs - Stack Overflow

By clicking “Sign up”, you agree to our

terms of service

https://stackoverflow.com/legal/terms-of-service/public

and acknowledge you have read our

privacy policy

https://stackoverflow.com/legal/privacy-policy

Sign up with Google

Sign up with GitHub

Already have an account?

https://stackoverflow.com/users/login

Skip to main content

https://stackoverflow.com/questions/29283040/how-to-add-custom-certificate-authority-ca-to-nodejs#content

1. \[Home\](https://stackoverflow.com/)
2. \[Questions\](https://stackoverflow.com/questions)
3. \[AI Assist\](https://stackoverflow.com/ai-assist)
4. \[Tags\](https://stackoverflow.com/tags)
5.
6. \[Challenges\](https://stackoverflow.com/beta/challenges)
7. \[Chat\](https://chat.stackoverflow.com/?tab=explore)
8. \[Articles\](https://stackoverflow.blog/contributed?utm\_medium=referral&utm\_source=stackoverflow-community&utm\_campaign=so-blog&utm\_content=experiment-articles)
9. \[Users\](https://stackoverflow.com/users)
10.
11. \[Companies\](https://stackoverflow.com/jobs/companies?so\_medium=stackoverflow&so\_source=SiteNav)
12. \[Collectives\](javascript:void(0))
13. Communities for your favorite technologies. \[Explore all Collectives\](https://stackoverflow.com/collectives-all)

Stack Internal Stack Overflow for Teams is now called

Stack Internal

. Bring the best of human thought and AI automation together at your work.

Try for free

https://stackoverflowteams.com/teams/create/free/?utm\_medium=referral&utm\_source=stackoverflow-community&utm\_campaign=side-bar&utm\_content=explore-teams

https://stackoverflow.co/internal/?utm\_medium=referral&utm\_source=stackoverflow-community&utm\_campaign=side-bar&utm\_content=explore-teams

Stack Internal

javascript:void(0)

Bring the best of human thought and AI automation together at your work.

https://stackoverflow.co/internal/?utm\_medium=referral&utm\_source=stackoverflow-community&utm\_campaign=side-bar&utm\_content=explore-teams-compact

Collectives™ on Stack Overflow

Find centralized, trusted content and collaborate around the technologies you use most.

Learn more about Collectives

https://stackoverflow.com/collectives

Stack Internal

Knowledge at work

Bring the best of human thought and AI automation together at your work.

Explore Stack Internal

https://stackoverflow.co/internal/?utm\_medium=referral&utm\_source=stackoverflow-community&utm\_campaign=side-bar&utm\_content=explore-teams-compact-popover

How are we doing? Take our short survey

https://stackoverflow.com/survey/site-satisfaction/redirect?source=sidebar

https://stackoverflow.com/

https://stackoverflow.co/

https://stackoverflow.co/internal/

Stack Internal Implement a knowledge platform layer to power your enterprise and AI tools.

https://stackoverflow.co/internal/?utm\_medium=referral&utm\_source=stackoverflow-community&utm\_campaign=top-nav&utm\_content=stack-overflow-for-teams

Stack Data Licensing Get access to top-class technical expertise with trusted & attributed content.

https://stackoverflow.co/data-licensing/?utm\_medium=referral&utm\_source=stackoverflow-community&utm\_campaign=top-nav&utm\_content=overflow-api

Stack Ads Connect your brand to the world's most trusted technologist communities.

https://stackoverflow.co/advertising/?utm\_medium=referral&utm\_source=stackoverflow-community&utm\_campaign=top-nav&utm\_content=stack-overflow-advertising

Releases Keep up-to-date on features we add to Stack Overflow and Stack Internal.

https://stackoverflow.blog/releases/?utm\_medium=referral&utm\_source=stackoverflow-community&utm\_campaign=top-nav&utm\_content=releases

About the company

https://stackoverflow.co/?utm\_medium=referral&utm\_source=stackoverflow-community&utm\_campaign=top-nav&utm\_content=about-the-company

Visit the blog

https://stackoverflow.blog/?utm\_medium=referral&utm\_source=stackoverflow-community&utm\_campaign=top-nav&utm\_content=blog

Tour Start here for a quick overview of the site

https://stackoverflow.com/tour

Help Center Detailed answers to any questions you might have

https://stackoverflow.com/help

Meta Discuss the workings and policies of this site

https://meta.stackoverflow.com/

About Us Learn more about Stack Overflow the company, and our products

https://stackoverflow.co/

current community

https://stackoverflow.com/

Stack Overflow

https://stackoverflow.com/

https://stackoverflow.com/help

https://chat.stackoverflow.com/?tab=explore

Meta Stack Overflow

https://meta.stackoverflow.com/

your communities

https://stackoverflow.com/users/signup?ssrc=site\_switcher&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f29283040%2fhow-to-add-custom-certificate-authority-ca-to-nodejs

https://stackoverflow.com/users/login?ssrc=site\_switcher&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f29283040%2fhow-to-add-custom-certificate-authority-ca-to-nodejs

to customize your list.

more stack exchange communities

https://stackexchange.com/sites

company blog

https://stackoverflow.blog/

https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f29283040%2fhow-to-add-custom-certificate-authority-ca-to-nodejs

https://stackoverflow.com/users/signup?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f29283040%2fhow-to-add-custom-certificate-authority-ca-to-nodejs

How are we doing? Please help us improve Stack Overflow.

Take our short survey

https://stackoverflow.com/survey/site-satisfaction/redirect

How to add custom certificate authority (CA) to nodejs

https://stackoverflow.com/questions/29283040/how-to-add-custom-certificate-authority-ca-to-nodejs

Ask Question

https://stackoverflow.com/questions/ask

Asked 11 years, 1 month ago

6 months ago

https://stackoverflow.com/questions/29283040/how-to-add-custom-certificate-authority-ca-to-nodejs?lastactivity

Viewed 321k times

This question shows research effort; it is useful and clear

This question does not show any research effort; it is unclear or not useful

Save this question.

https://stackoverflow.com/posts/29283040/timeline

Show activity on this post.

I'm using a CLI tool to build hybrid mobile apps which has a cool upload feature so I can test the app on a device without going through the app store (it's ionic-cli). However, in my company like so many other companies TLS requests are re-signed with the company's own custom CA certificate which I have on my machine in the keychain (OS X). However, nodejs does not use the keychain to get its list of CA's to trust. I don't control the ionic-cli app so I can't simply pass in a { ca: } property to the https module. I could also see this being a problem for any node app which I do not control. Is it possible to tell nodejs to trust a CA?

I wasn't sure if this belonged in Information Security or any of the other exchanges...

https://stackoverflow.com/questions/tagged/node.js

https://stackoverflow.com/questions/tagged/npm

https://stackoverflow.com/q/29283040

Share a link to this question

https://stackoverflow.com/q/29283040

CC BY-SA 3.0

https://creativecommons.org/licenses/by-sa/3.0/

Short permalink to this question

Improve this question

https://stackoverflow.com/posts/29283040/edit

Follow this question to receive notifications

asked Mar 26, 2015 at 15:51

https://stackoverflow.com/users/1454406/mike-haas

2,813 3 3 gold badges 29 29 silver badges 32 32 bronze badges

Looks like on the 10th anniversary of your question, Node has heard our collective pain. See reply from @MarcusOtter down below. Wellspring –

https://stackoverflow.com/users/8786602/wellspring

2025-04-28 19:52:04 +00:00

Commented Apr 28, 2025 at 19:52

https://stackoverflow.com/questions/29283040/how-to-add-custom-certificate-authority-ca-to-nodejs#comment140377879\_29283040

Add a comment

https://stackoverflow.com/questions/29283040/how-to-add-custom-certificate-authority-ca-to-nodejs

Report this ad

7 Answers 7

Reset to default

https://stackoverflow.com/questions/29283040/how-to-add-custom-certificate-authority-ca-to-nodejs?answertab=scoredesc#tab-top

Highest score (default)

Trending (recent votes count more)

Date modified (newest first)

Date created (oldest first)

This answer is useful

This answer is not useful

Save this answer.

Loading when this answer was accepted…

https://stackoverflow.com/posts/47160447/timeline

Show activity on this post.

Node.js 7.3.0 (and the LTS versions 6.10.0 and 4.8.0) added

NODE\_EXTRA\_CA\_CERTS

https://nodejs.org/api/cli.html#cli\_node\_extra\_ca\_certs\_file

environment variable for you to pass the CA certificates file. It will be safer than disabling certificate verification using

NODE\_TLS\_REJECT\_UNAUTHORIZED

$ export NODE\_EXTRA\_CA\_CERTS=\[your CA certificate file path\]

FYI: The file format is a PEM BUNDLE. That means it's just a bunch of PEM-encoded-certificates all in the same file. You can create it just like this:

cat \*.cer > node\_extra\_ca\_certs.pembundle

and the use

export NODE\_EXTRA\_CA\_CERTS=node\_extra\_ca\_certs.pembundle

https://stackoverflow.com/a/47160447

Share a link to this answer

https://stackoverflow.com/a/47160447

CC BY-SA 4.0

https://creativecommons.org/licenses/by-sa/4.0/

Short permalink to this answer

Improve this answer

https://stackoverflow.com/posts/47160447/edit

Follow this answer to receive notifications

edited May 12, 2025 at 11:35

https://stackoverflow.com/posts/47160447/revisions

StackzOfZtuff

https://stackoverflow.com/users/4247268/stackzofztuff

3,309 1 1 gold badge 32 32 silver badges 33 33 bronze badges

answered Nov 7, 2017 at 14:33

Cheng-Lin Tsao

https://stackoverflow.com/users/5253408/cheng-lin-tsao

2,734 1 1 gold badge 13 13 silver badges 6 6 bronze badges

Sign up to request clarification or add additional context in comments.

11 Comments

Add a comment

https://stackoverflow.com/users/185034/paul

Over a year ago

https://stackoverflow.com/questions/29283040/how-to-add-custom-certificate-authority-ca-to-nodejs#comment91616856\_47160447

cafile configuration property

https://docs.npmjs.com/misc/config#cafile

works similarly:

npm config set cafile \[your CA certificate file path\]

2018-09-14T15:18:59.033Z+00:00

https://stackoverflow.com/users/2183021/eric

Over a year ago

https://stackoverflow.com/questions/29283040/how-to-add-custom-certificate-authority-ca-to-nodejs#comment91831623\_47160447

The main difference between

NODE\_EXTRA\_CA\_CERTS

config property is that the former

a cert, whereas the

config property

the certs. For those that just want to add a corporate cert to the chain,

NODE\_EXTRA\_CA\_CERTS

is the easier option.

2018-09-21T13:08:12.983Z+00:00

Ganesh Karamala

Ganesh Karamala

https://stackoverflow.com/users/2881372/ganesh-karamala

Over a year ago

https://stackoverflow.com/questions/29283040/how-to-add-custom-certificate-authority-ca-to-nodejs#comment94160455\_47160447

does ca certificate means .pem/.cer file location ?

2018-12-06T12:14:32.073Z+00:00

Joel Pearson

Joel Pearson

https://stackoverflow.com/users/359999/joel-pearson

Over a year ago

https://stackoverflow.com/questions/29283040/how-to-add-custom-certificate-authority-ca-to-nodejs#comment99150919\_47160447

@ChrisDaMour it can work with sudo, you just need to edit the

and allow the

NODE\_EXTRA\_CA\_CERTS

environment variable to work across a sudo boundary.

2019-05-23T03:14:28.67Z+00:00

https://stackoverflow.com/users/1470040/ivandov

Over a year ago

https://stackoverflow.com/questions/29283040/how-to-add-custom-certificate-authority-ca-to-nodejs#comment100235968\_47160447

Can this be used to programmatically add certificates as the application is online? Or will this only work during initial startup with some pre-provided certs?

2019-07-01T20:26:25.137Z+00:00

Add a comment | Show 6 more comments

This answer is useful

This answer is not useful

Save this answer.

Loading when this answer was accepted…

https://stackoverflow.com/posts/67618741/timeline

Show activity on this post.

#### You can specify a command line option to tell node to use the system CA store:

Copynode --use-openssl-ca

Alternatively this can be specified as an environment variable, if you are not running the node CLI directly yourself:

CopyNODE\_OPTIONS=--use-openssl-ca

#### You can now use

--use-system-ca

on Windows and Mac, see

@MarcusOtter's answer

https://stackoverflow.com/a/79473632/1103530

https://stackoverflow.com/a/67618741

Share a link to this answer

https://stackoverflow.com/a/67618741

CC BY-SA 4.0

https://creativecommons.org/licenses/by-sa/4.0/

Short permalink to this answer

Improve this answer

https://stackoverflow.com/posts/67618741/edit

Follow this answer to receive notifications

edited May 27, 2025 at 13:03

https://stackoverflow.com/posts/67618741/revisions

answered May 20, 2021 at 10:39

https://stackoverflow.com/users/1103530/jimbali

2,715 1 1 gold badge 25 25 silver badges 30 30 bronze badges

Add a comment

https://stackoverflow.com/users/80002/mark

Over a year ago

https://stackoverflow.com/questions/29283040/how-to-add-custom-certificate-authority-ca-to-nodejs#comment130677320\_67618741

IMHO this is the best answer.

2022-10-10T04:27:57.097Z+00:00

akostadinov

akostadinov

https://stackoverflow.com/users/520567/akostadinov

Nov 3, 2025 at 11:58

https://stackoverflow.com/questions/29283040/how-to-add-custom-certificate-authority-ca-to-nodejs#comment140833481\_67618741

This answer is best for local usage. For modifying what containers use, Cheng-Lin's answer about

NODE\_EXTRA\_CA\_CERTS

is better. Depends on the use case.

2025-11-03T11:58:45.303Z+00:00

GoFindTruth

GoFindTruth

https://stackoverflow.com/users/5841242/gofindtruth

Over a year ago

https://stackoverflow.com/questions/29283040/how-to-add-custom-certificate-authority-ca-to-nodejs#comment133482454\_67618741

can you please tell how to use this flag with self-signed CA certificate?

2023-03-07T12:49:39.16Z+00:00

https://stackoverflow.com/users/1103530/jimbali

Over a year ago

https://stackoverflow.com/questions/29283040/how-to-add-custom-certificate-authority-ca-to-nodejs#comment133504275\_67618741

@GoFindTruth it depends what platform you're on, but if for example you are running your code in an Ubuntu Docker container then you would copy the CA file into the image under

/usr/local/share/ca-certificates/

update-ca-certificates

. Then it would be in the system CA store and the flag should work.

stackoverflow.com/a/42292623/1103530

https://stackoverflow.com/a/42292623/1103530

2023-03-08T15:27:42.267Z+00:00

Danila Kiver

Danila Kiver

https://stackoverflow.com/users/7191047/danila-kiver

Over a year ago

https://stackoverflow.com/questions/29283040/how-to-add-custom-certificate-authority-ca-to-nodejs#comment135862156\_67618741

Works like a charm. To make use of this option in

(e. g. to access private registry using machine-wide installed private CA certificate), one needs to export the

NODE\_OPTIONS

variable to make it visible for children processes of the shell invoking

internally runs

2023-09-08T14:34:14.91Z+00:00

Bruno Lamps

Bruno Lamps

https://stackoverflow.com/users/2600554/bruno-lamps

Over a year ago

https://stackoverflow.com/questions/29283040/how-to-add-custom-certificate-authority-ca-to-nodejs#comment140340529\_67618741

I was facing a situation when a

pm2 cluster application

didn't read

NODE\_EXTRA\_CA\_CERTS

, and this idea saved me. I added

node\_args: "--use-openssl-ca"

to my ecosystem file and it works great. I'm using node 22, pm2 6 and some ubuntu lts.

2025-04-16T11:36:05.023Z+00:00

Add a comment | Show 1 more comment

This answer is useful

This answer is not useful

Save this answer.

Loading when this answer was accepted…

https://stackoverflow.com/posts/39972054/timeline

Show activity on this post.

#### I'm aware of two npm modules that handle this problem when you control the app:

https://github.com/fujifish/syswide-cas

https://github.com/fujifish/syswide-cas

(I'm the author of this one)

https://github.com/coolaj86/node-ssl-root-cas

https://github.com/coolaj86/node-ssl-root-cas

node-ssl-root-cas

bundles it's own copies of nodes root CAs and also enables adding your own CAs to trust. It places the certs on the https global agent, so it will only be used for https module, not pure tls connections. Also, you will need extra steps if you use a custom Agent instead of the global agent.

syswide-cas

loads certificates from pre-defined directories (such as /etc/ssl/certs) and uses node internal API to add them to the trusted list of CAs in conjunction to the bundled root CAs. There is no need to use the

option since it makes the change globally which affects all later TLS calls automatically. It's also possible to add CAs from other directories/files if needed. It was verified to work with node 0.10, node 5 and node 6.

Since you do not control the app you can create a wrapper script to enable

syswide-cas

node-ssl-root-cas

) and then require the ionic-cli script:

Copyrequire('syswide-cas'); // this adds your custom CAs in addition to bundled CAs
require('./path/to/real/script'); // this runs the actual script

https://stackoverflow.com/a/39972054

Share a link to this answer

https://stackoverflow.com/a/39972054

CC BY-SA 4.0

https://creativecommons.org/licenses/by-sa/4.0/

Short permalink to this answer

Improve this answer

https://stackoverflow.com/posts/39972054/edit

Follow this answer to receive notifications

edited Mar 16, 2022 at 17:58

https://stackoverflow.com/posts/39972054/revisions

answered Oct 11, 2016 at 7:10

https://stackoverflow.com/users/5014029/fujifish

971 10 10 silver badges 10 10 bronze badges

Add a comment

ThorSummoner

ThorSummoner

https://stackoverflow.com/users/1695680/thorsummoner

Over a year ago

https://stackoverflow.com/questions/29283040/how-to-add-custom-certificate-authority-ca-to-nodejs#comment97862558\_39972054

can this method be used to monkey patch npm?

2019-04-08T21:44:28.467Z+00:00

https://stackoverflow.com/users/5014029/fujifish

Over a year ago

https://stackoverflow.com/questions/29283040/how-to-add-custom-certificate-authority-ca-to-nodejs#comment97910301\_39972054

If you're asking if you can run "npm" using syswide-cas module, then the answer is: not directly. You could however create an "npm-wrapper" file that performs require("syswide-cas") and then require("npm") to invoke npm programatically.

2019-04-10T08:18:23.743Z+00:00

ThorSummoner

ThorSummoner

https://stackoverflow.com/users/1695680/thorsummoner

Over a year ago

https://stackoverflow.com/questions/29283040/how-to-add-custom-certificate-authority-ca-to-nodejs#comment97933705\_39972054

I tried the wrapper thing and npm seemed to ignore the global http ca system certificates fix, and seemed to ignore the syswide-cas require too /shrug

2019-04-10T19:53:17.053Z+00:00

https://stackoverflow.com/users/3421536/cybered

Over a year ago

https://stackoverflow.com/questions/29283040/how-to-add-custom-certificate-authority-ca-to-nodejs#comment126307482\_39972054

Both Github links are broken.

2022-03-13T21:45:11.103Z+00:00

https://stackoverflow.com/users/5014029/fujifish

Over a year ago

https://stackoverflow.com/questions/29283040/how-to-add-custom-certificate-authority-ca-to-nodejs#comment126377656\_39972054

github.com/fujifish/syswide-cas

https://github.com/fujifish/syswide-cas

2022-03-16T17:59:29.17Z+00:00

Add a comment | Show 1 more comment

This answer is useful

This answer is not useful

Save this answer.

Loading when this answer was accepted…

https://stackoverflow.com/posts/53490133/timeline

Show activity on this post.

There is an undocumented, seemingly stable, API for

a certificate to the default list:

Copyconst tls = require('tls');

const secureContext = tls.createSecureContext();

// https://letsencrypt.org/certs/lets-encrypt-x3-cross-signed.pem.txt
secureContext.context.addCACert(\`-----BEGIN CERTIFICATE-----
MIIEkjCCA3qgAwIBAgIQCgFBQgAAAVOFc2oLheynCDANBgkqhkiG9w0BAQsFADA/
MSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT
DkRTVCBSb290IENBIFgzMB4XDTE2MDMxNzE2NDA0NloXDTIxMDMxNzE2NDA0Nlow
SjELMAkGA1UEBhMCVVMxFjAUBgNVBAoTDUxldCdzIEVuY3J5cHQxIzAhBgNVBAMT
GkxldCdzIEVuY3J5cHQgQXV0aG9yaXR5IFgzMIIBIjANBgkqhkiG9w0BAQEFAAOC
AQ8AMIIBCgKCAQEAnNMM8FrlLke3cl03g7NoYzDq1zUmGSXhvb418XCSL7e4S0EF
q6meNQhY7LEqxGiHC6PjdeTm86dicbp5gWAf15Gan/PQeGdxyGkOlZHP/uaZ6WA8
SMx+yk13EiSdRxta67nsHjcAHJyse6cF6s5K671B5TaYucv9bTyWaN8jKkKQDIZ0
Z8h/pZq4UmEUEz9l6YKHy9v6Dlb2honzhT+Xhq+w3Brvaw2VFn3EK6BlspkENnWA
a6xK8xuQSXgvopZPKiAlKQTGdMDQMc2PMTiVFrqoM7hD8bEfwzB/onkxEz0tNvjj
/PIzark5McWvxI0NHWQWM6r6hCm21AvA2H3DkwIDAQABo4IBfTCCAXkwEgYDVR0T
AQH/BAgwBgEB/wIBADAOBgNVHQ8BAf8EBAMCAYYwfwYIKwYBBQUHAQEEczBxMDIG
CCsGAQUFBzABhiZodHRwOi8vaXNyZy50cnVzdGlkLm9jc3AuaWRlbnRydXN0LmNv
bTA7BggrBgEFBQcwAoYvaHR0cDovL2FwcHMuaWRlbnRydXN0LmNvbS9yb290cy9k
c3Ryb290Y2F4My5wN2MwHwYDVR0jBBgwFoAUxKexpHsscfrb4UuQdf/EFWCFiRAw
VAYDVR0gBE0wSzAIBgZngQwBAgEwPwYLKwYBBAGC3xMBAQEwMDAuBggrBgEFBQcC
ARYiaHR0cDovL2Nwcy5yb290LXgxLmxldHNlbmNyeXB0Lm9yZzA8BgNVHR8ENTAz
MDGgL6AthitodHRwOi8vY3JsLmlkZW50cnVzdC5jb20vRFNUUk9PVENBWDNDUkwu
Y3JsMB0GA1UdDgQWBBSoSmpjBH3duubRObemRWXv86jsoTANBgkqhkiG9w0BAQsF
AAOCAQEA3TPXEfNjWDjdGBX7CVW+dla5cEilaUcne8IkCJLxWh9KEik3JHRRHGJo
uM2VcGfl96S8TihRzZvoroed6ti6WqEBmtzw3Wodatg+VyOeph4EYpr/1wXKtx8/
wApIvJSwtmVi4MFU5aMqrSDE6ea73Mj2tcMyo5jMd6jmeWUHK8so/joWUoHOUgwu
X4Po1QYz+3dszkDqMp4fklxBwXRsW10KXzPMTZ+sOPAveyxindmjkW8lGy+QsRlG
PfZ+G6Z6h7mjem0Y+iWlkYcV4PIWL1iwBi8saCbGS5jN2p8M+X+Q7UNKEkROb3N6
KOqkqm57TH2H3eDJAkSnh6/DNFu0Qg==
-----END CERTIFICATE-----\`);

const sock = tls.connect(443, 'host', { secureContext });

#### For more information, checkout the open issue on the subject:

https://github.com/nodejs/node/issues/27079

https://github.com/nodejs/node/issues/27079

https://stackoverflow.com/a/53490133

Share a link to this answer

https://stackoverflow.com/a/53490133

CC BY-SA 4.0

https://creativecommons.org/licenses/by-sa/4.0/

Short permalink to this answer

Improve this answer

https://stackoverflow.com/posts/53490133/edit

Follow this answer to receive notifications

edited Feb 11, 2020 at 4:53

https://stackoverflow.com/posts/53490133/revisions

answered Nov 26, 2018 at 22:33

Cameron Tacklind

https://stackoverflow.com/users/4612476/cameron-tacklind

7,590 2 2 gold badges 47 47 silver badges 52 52 bronze badges

Add a comment

https://stackoverflow.com/users/241955/se%C3%A1n-hayes

Over a year ago

https://stackoverflow.com/questions/29283040/how-to-add-custom-certificate-authority-ca-to-nodejs#comment95968158\_53490133

Is there a way to apply this globally?

2019-02-08T03:52:05.89Z+00:00

Cameron Tacklind

Cameron Tacklind

https://stackoverflow.com/users/4612476/cameron-tacklind

Over a year ago

https://stackoverflow.com/questions/29283040/how-to-add-custom-certificate-authority-ca-to-nodejs#comment96018246\_53490133

@SeánHayes I assume you've seen the other answers here that reference

NODE\_EXTRA\_CA\_CERTS

so I assume you mean can you do that in JavaScript? Researching this a little, it looks like the

NODE\_EXTRA\_CA\_CERTS

is entirely implemented in node's C++ source with methods that are not available to the JavaScript layer. Search for

UseExtraCaCerts

in node source to see for yourself. Not sure what mechanism the

method uses exactly so you might investigate that but I doubt it is serious different.

2019-02-09T23:51:52.317Z+00:00

This answer is useful

This answer is not useful

Save this answer.

Loading when this answer was accepted…

https://stackoverflow.com/posts/79473632/timeline

Show activity on this post.

2025 Update:

--use-system-ca

--use-system-ca

https://nodejs.org/docs/v23.8.0/api/cli.html#--use-system-ca

was added in Node.js v23.8.0 and also backported to v22.15.0:

Node.js uses the trusted CA certificates present in the system store along with the

--use-bundled-ca

--use-openssl-ca

This option is only supported on Windows and macOS

, and the certificate trust policy is planned to follow

Chromium's policy for locally trusted certificates

https://chromium.googlesource.com/chromium/src/+/main/net/data/ssl/chrome\_root\_store/faq.md#does-the-chrome-certificate-verifier-consider-local-trust-decisions

It seems like it is also supported on "non-Windows and non-macOS" in v23.9.0 (not backported to v22 as far as I can tell)

https://stackoverflow.com/a/79473632

Share a link to this answer

https://stackoverflow.com/a/79473632

CC BY-SA 4.0

https://creativecommons.org/licenses/by-sa/4.0/

Short permalink to this answer

Improve this answer

https://stackoverflow.com/posts/79473632/edit

Follow this answer to receive notifications

edited Nov 5, 2025 at 3:06

https://stackoverflow.com/posts/79473632/revisions

answered Feb 27, 2025 at 18:41

MarcusOtter

https://stackoverflow.com/users/10615308/marcusotter

1,402 15 15 silver badges 22 22 bronze badges

Add a comment

Dalibor Filus

Dalibor Filus

https://stackoverflow.com/users/737956/dalibor-filus

Nov 3, 2025 at 11:26

https://stackoverflow.com/questions/29283040/how-to-add-custom-certificate-authority-ca-to-nodejs#comment140833430\_79473632

I tested it in node 22.21.1 on macOS from homebrew and it works there too. Maybe it was backported?

2025-11-03T11:26:19.64Z+00:00

MarcusOtter

MarcusOtter

https://stackoverflow.com/users/10615308/marcusotter

Nov 5, 2025 at 3:01

https://stackoverflow.com/questions/29283040/how-to-add-custom-certificate-authority-ca-to-nodejs#comment140837011\_79473632

Good shout, looks like it was backported to 22.15.0!

2025-11-05T03:01:33.5Z+00:00

JIT Solution

JIT Solution

https://stackoverflow.com/users/8833472/jit-solution

Mar 25 at 13:46

https://stackoverflow.com/questions/29283040/how-to-add-custom-certificate-authority-ca-to-nodejs#comment141020612\_79473632

Hint: Some commands like npm need this node parameter as a system environment variable:

NODE\_OPTIONS=--use-system-ca

https://github.com/nodejs/node/issues/58346#issuecomment-2884992058

2026-03-25T13:46:39.61Z+00:00

This answer is useful

This answer is not useful

Save this answer.

Loading when this answer was accepted…

https://stackoverflow.com/posts/58702006/timeline

Show activity on this post.

This answer is more focused towards package maintainers/builders.

One can use this method if you do

want end users to rely on additional environment variables.

When nodejs is built from source, it (by default, can be overridden) embeds the Mozilla CA certificate database into the binary itself. One can add more certificates to this database using the following commands:

Copy# Convert your PEM certificate to DER
openssl x509 -in /path/to/your/CA.pem -outform der -out CA.der

# Add converted certificate to certdata
nss-addbuiltin -n "MyCompany-CA" -t "CT,C,C" < CA.der >> tools/certdata.txt

# Regenerate src/node\_root\_certs.h header file
perl tools/mk-ca-bundle.pl

# Finally, compile
make install

https://stackoverflow.com/a/58702006

Share a link to this answer

https://stackoverflow.com/a/58702006

CC BY-SA 4.0

https://creativecommons.org/licenses/by-sa/4.0/

Short permalink to this answer

Improve this answer

https://stackoverflow.com/posts/58702006/edit

Follow this answer to receive notifications

edited Dec 10, 2024 at 10:57

https://stackoverflow.com/posts/58702006/revisions

StackzOfZtuff

https://stackoverflow.com/users/4247268/stackzofztuff

3,309 1 1 gold badge 32 32 silver badges 33 33 bronze badges

answered Nov 4, 2019 at 22:29

Nehal J Wani

https://stackoverflow.com/users/1005215/nehal-j-wani

16.7k 3 3 gold badges 72 72 silver badges 93 93 bronze badges

Add a comment

This answer is useful

This answer is not useful

Save this answer.

Loading when this answer was accepted…

https://stackoverflow.com/posts/79639346/timeline

Show activity on this post.

(Adding to previous helpful answer)

#### To add a CA cert for all subsequent client connections, you can do this:

Copyconst origCsC = tls.createSecureContext;
tls.createSecureContext = options => {
  const secureContext = origCsC(options);
  secureContext.context.addCACert('-----BEGIN CERTIFICATE-----...');
  return secureContext;
};

If you're doing this in a unit test environment, you might consider using

mock.method

https://nodejs.org/api/test.html#mockmethodobject-methodname-implementation-options

Copyimport {test} from 'node:test';
import tls from 'node:tls';

test('foo', t => {
  t.mock.method(tls, 'createSecureContext', options => {
  const secureContext = origCsC(options);
  secureContext.context.addCACert('-----BEGIN CERTIFICATE-----...');
  return secureContext;
});
...
  t.mock.reset();

: This is a hack, replacing an existing built-in method with a wrapper, then calling an undocumented method. It works as of node v24.1.0, but may fail one day in the future.

https://stackoverflow.com/a/79639346

Share a link to this answer

https://stackoverflow.com/a/79639346

CC BY-SA 4.0

https://creativecommons.org/licenses/by-sa/4.0/

Short permalink to this answer

Improve this answer

https://stackoverflow.com/posts/79639346/edit

Follow this answer to receive notifications

answered May 26, 2025 at 17:13

Joe Hildebrand

https://stackoverflow.com/users/8388/joe-hildebrand

10.4k 2 2 gold badges 42 42 silver badges 52 52 bronze badges

Add a comment

Your Answer

Thanks for contributing an answer to Stack Overflow!

Please be sure to

answer the question

. Provide details and share your research!

Asking for help, clarification, or responding to other answers.

Making statements based on opinion; back them up with references or personal experience.

To learn more, see our

tips on writing great answers

https://stackoverflow.com/help/how-to-answer

Draft saved

Draft discarded

https://stackoverflow.com/users/login?ssrc=question\_page&returnurl=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F29283040%2Fhow-to-add-custom-certificate-authority-ca-to-nodejs%23new-answer

Sign up using Google

Sign up using Email and Password

Post as a guest

Required, but never shown

Post as a guest

Required, but never shown

Post Your Answer Discard

By clicking “Post Your Answer”, you agree to our

terms of service

https://stackoverflow.com/legal/terms-of-service/public

and acknowledge you have read our

privacy policy

https://stackoverflow.com/legal/privacy-policy

Start asking to get answers

Find the answer to your question by asking.

Ask question

https://stackoverflow.com/questions/ask

Explore related questions

https://stackoverflow.com/questions/tagged/node.js

https://stackoverflow.com/questions/tagged/npm

See similar questions with these tags.

The Overflow Blog

Connecting the dots for accurate AI

https://stackoverflow.blog/2026/05/12/connecting-the-dots-for-accurate-ai/?cb=1

Observability and human intuition in an AI world

https://stackoverflow.blog/2026/05/15/observability-and-human-intuition-in-an-ai-world/?cb=1

Featured on Meta

(Almost) One year of Challenges

https://meta.stackexchange.com/questions/418261/almost-one-year-of-challenges?cb=1

Policy: Generative AI (e.g., ChatGPT) is banned

https://meta.stackoverflow.com/questions/421831/policy-generative-ai-e-g-chatgpt-is-banned?cb=1

Report this ad

https://stackoverflow.com/questions/47580951/connect-to-a-remote-service-which-uses-a-self-signed-certificate?lq=1

Connect to a remote service which uses a self signed certificate

https://stackoverflow.com/questions/47580951/connect-to-a-remote-service-which-uses-a-self-signed-certificate?noredirect=1&lq=1

https://stackoverflow.com/questions/13913941/how-to-fix-ssl-certificate-error-when-running-npm-on-windows?lq=1

How to fix SSL certificate error when running Npm on Windows?

https://stackoverflow.com/questions/13913941/how-to-fix-ssl-certificate-error-when-running-npm-on-windows?noredirect=1&lq=1

https://stackoverflow.com/questions/42292444/how-do-i-add-a-ca-root-certificate-inside-a-docker-image?lq=1

How do I add a CA root certificate inside a docker image?

https://stackoverflow.com/questions/42292444/how-do-i-add-a-ca-root-certificate-inside-a-docker-image?noredirect=1&lq=1

https://stackoverflow.com/questions/23788564/npm-add-root-ca?lq=1

npm add root CA

https://stackoverflow.com/questions/23788564/npm-add-root-ca?noredirect=1&lq=1

https://stackoverflow.com/questions/62792477/cant-connect-to-elasticsearch-with-node-js-on-kubernetes-self-signed-certifica?lq=1

Can't connect to Elasticsearch with Node.Js on Kubernetes (self signed certificate in certificate chain)

https://stackoverflow.com/questions/62792477/cant-connect-to-elasticsearch-with-node-js-on-kubernetes-self-signed-certifica?noredirect=1&lq=1

https://stackoverflow.com/questions/60984525/knex-connect-with-heroku-postgres-getting-error?lq=1

Knex connect with Heroku Postgres getting error?

https://stackoverflow.com/questions/60984525/knex-connect-with-heroku-postgres-getting-error?noredirect=1&lq=1

https://stackoverflow.com/questions/66647092/does-java-runtimes-require-use-of-keystore-for-ssl-certificates-as-mandatory?lq=1

Does Java Runtimes require use of Keystore for SSL certificates as mandatory?

https://stackoverflow.com/questions/66647092/does-java-runtimes-require-use-of-keystore-for-ssl-certificates-as-mandatory?noredirect=1&lq=1

https://stackoverflow.com/questions/44428566/npm-error-unable-to-get-issuer-cert-locally-how-to-generate-a-pem-file-from-a?lq=1

npm error UNABLE\_TO\_GET\_ISSUER\_CERT\_LOCALLY, how to generate a .pem file from a bundle of certificates and that bundle as well?

https://stackoverflow.com/questions/44428566/npm-error-unable-to-get-issuer-cert-locally-how-to-generate-a-pem-file-from-a?noredirect=1&lq=1

https://stackoverflow.com/questions/17272628/nodejs-unable-to-verify-leaf-signature-with-self-signed-certificate?lq=1

nodejs - UNABLE\_TO\_VERIFY\_LEAF\_SIGNATURE with self-signed certificate

https://stackoverflow.com/questions/17272628/nodejs-unable-to-verify-leaf-signature-with-self-signed-certificate?noredirect=1&lq=1

https://stackoverflow.com/questions/75652653/nodejs-failing-to-establish-tls-connection-with-rds?lq=1

Nodejs failing to establish tls connection with RDS

https://stackoverflow.com/questions/75652653/nodejs-failing-to-establish-tls-connection-with-rds?noredirect=1&lq=1

See more linked questions

https://stackoverflow.com/questions/linked/29283040?lq=1

https://stackoverflow.com/questions/16430442/in-house-certificate-authority-ca-for-node-js-https-request-how-to-point-to?rq=3

In-House Certificate Authority (CA) for Node.js https.request: How to point to .PEM?

https://stackoverflow.com/questions/16430442/in-house-certificate-authority-ca-for-node-js-https-request-how-to-point-to?rq=3

https://stackoverflow.com/questions/19665863/how-do-i-use-a-self-signed-certificate-for-a-https-node-js-server?rq=3

How do I use a self signed certificate for a HTTPS Node.js server?

https://stackoverflow.com/questions/19665863/how-do-i-use-a-self-signed-certificate-for-a-https-node-js-server?rq=3

https://stackoverflow.com/questions/20658120/nodejs-unable-to-read-default-cas-in-ubuntu?rq=3

NodeJS unable to read default CAs in ubuntu

https://stackoverflow.com/questions/20658120/nodejs-unable-to-read-default-cas-in-ubuntu?rq=3

https://stackoverflow.com/questions/23746263/install-root-certificate-to-node-js-https-client?rq=3

Install root certificate to Node.js (HTTPS Client)

https://stackoverflow.com/questions/23746263/install-root-certificate-to-node-js-https-client?rq=3

https://stackoverflow.com/questions/32513739/using-an-ssl-certificate-pem-file-in-javascript?rq=3

Using an SSL certificate (pem file) in JavaScript

https://stackoverflow.com/questions/32513739/using-an-ssl-certificate-pem-file-in-javascript?rq=3

https://stackoverflow.com/questions/42771933/how-do-i-configure-npm-to-use-the-system-certificate-authorities-in-centos-rhel?rq=3

How do I configure NPM to use the system certificate authorities in CentOS/RHEL?

https://stackoverflow.com/questions/42771933/how-do-i-configure-npm-to-use-the-system-certificate-authorities-in-centos-rhel?rq=3

https://stackoverflow.com/questions/45088006/nodejs-error-self-signed-certificate-in-certificate-chain?rq=3

nodejs - error self signed certificate in certificate chain

https://stackoverflow.com/questions/45088006/nodejs-error-self-signed-certificate-in-certificate-chain?rq=3

https://stackoverflow.com/questions/48040682/installing-custom-ssl-certificate-in-node-unable-to-verify-leaf-signature?rq=3

Installing custom SSL certificate in Node (UNABLE\_TO\_VERIFY\_LEAF\_SIGNATURE)

https://stackoverflow.com/questions/48040682/installing-custom-ssl-certificate-in-node-unable-to-verify-leaf-signature?rq=3

https://stackoverflow.com/questions/56649374/how-to-create-a-certificate-authority-ca-using-pem-lib-nodejs?rq=3

How to create a Certificate Authority 'CA' using pem lib NodeJs?

https://stackoverflow.com/questions/56649374/how-to-create-a-certificate-authority-ca-using-pem-lib-nodejs?rq=3

https://stackoverflow.com/questions/70198705/how-can-i-set-node-extra-ca-certs-on-node?rq=3

How can I set NODE\_EXTRA\_CA\_CERTS on node

https://stackoverflow.com/questions/70198705/how-can-i-set-node-extra-ca-certs-on-node?rq=3

Hot Network Questions

https://stackexchange.com/questions?tab=hot

Does the sunk costs fallacy require an unprofitable outcome?

https://philosophy.stackexchange.com/questions/138385/does-the-sunk-costs-fallacy-require-an-unprofitable-outcome

How can a curved bow shock be considered a normal shock?

https://aviation.stackexchange.com/questions/115238/how-can-a-curved-bow-shock-be-considered-a-normal-shock

Where do the stats for animals come from in D&D?

https://rpg.stackexchange.com/questions/219327/where-do-the-stats-for-animals-come-from-in-dd

Increment strengths of cities in PSE Land

https://puzzling.stackexchange.com/questions/138051/increment-strengths-of-cities-in-pse-land

Why is my SIMD + PEXT implementation of octal string parsing unable to beat the compiler's?

https://stackoverflow.com/questions/79939722/why-is-my-simd-pext-implementation-of-octal-string-parsing-unable-to-beat-the

Two people playing the same PC?

https://rpg.stackexchange.com/questions/219319/two-people-playing-the-same-pc

How would Heidegger respond to a spontaneously created brain in a vat?

https://philosophy.stackexchange.com/questions/138372/how-would-heidegger-respond-to-a-spontaneously-created-brain-in-a-vat

What are the smaller nozzles for

https://3dprinting.stackexchange.com/questions/24447/what-are-the-smaller-nozzles-for

How would one distinguish time repeating from merely history repeating?

https://philosophy.stackexchange.com/questions/138406/how-would-one-distinguish-time-repeating-from-merely-history-repeating

How can I sell old shares?

https://money.stackexchange.com/questions/169587/how-can-i-sell-old-shares

SQL Login Audit stop applications from connecting to DB?

https://dba.stackexchange.com/questions/350262/sql-login-audit-stop-applications-from-connecting-to-db

renewcommand Gamma into itGamma in unicode-math

https://tex.stackexchange.com/questions/762771/renewcommand-gamma-into-itgamma-in-unicode-math

Was John the Baptist an Essene and was he a vegetarian?

https://christianity.stackexchange.com/questions/113829/was-john-the-baptist-an-essene-and-was-he-a-vegetarian

Finding the depth of sea very close to shore with a phone

https://physics.stackexchange.com/questions/872319/finding-the-depth-of-sea-very-close-to-shore-with-a-phone

Commutator of the BRST operator with the ghost number operator

https://physics.stackexchange.com/questions/872317/commutator-of-the-brst-operator-with-the-ghost-number-operator

Can't upgrade Kubutu 25.10 to 26.04 to new version because of broken build-essentials dependencies:

https://askubuntu.com/questions/1566786/cant-upgrade-kubutu-25-10-to-26-04-to-new-version-because-of-broken-build-essen

Which languages has Sir Terry Pratchett been translated into?

https://scifi.stackexchange.com/questions/304454/which-languages-has-sir-terry-pratchett-been-translated-into

How to figure the basis for this redemption?

https://money.stackexchange.com/questions/169576/how-to-figure-the-basis-for-this-redemption

Why isn't complete separation breaking my model?

https://stats.stackexchange.com/questions/675950/why-isnt-complete-separation-breaking-my-model

What purpose do the EXT pins on the SNES PPU2 serve?

https://retrocomputing.stackexchange.com/questions/32645/what-purpose-do-the-ext-pins-on-the-snes-ppu2-serve

How long is a month for vnstat?

https://unix.stackexchange.com/questions/805934/how-long-is-a-month-for-vnstat

Structural elucidation of olefin from hydrogenation and oxidative cleavage

https://chemistry.stackexchange.com/questions/195499/structural-elucidation-of-olefin-from-hydrogenation-and-oxidative-cleavage

Multiple entry Schengen Type C visa with two separate trips — confusion

https://travel.stackexchange.com/questions/203726/multiple-entry-schengen-type-c-visa-with-two-separate-trips-confusion

How can I present a highly interdisciplinary PhD talk in 15 minutes / 30 minutes?

https://academia.stackexchange.com/questions/226684/how-can-i-present-a-highly-interdisciplinary-phd-talk-in-15-minutes-30-minutes

Question feed

https://stackoverflow.com/feeds/question/29283040

Subscribe to RSS

Question feed

To subscribe to this RSS feed, copy and paste this URL into your RSS reader.

https://stackoverflow.com/feeds/question/29283040

Why are you flagging this comment?

Probable spam.

This comment promotes a product, service or website while

failing to disclose the author's affiliation

https://stackoverflow.com/help/promotion

Unfriendly or contains harassment/bigotry/abuse.

This comment is unkind, insulting or attacks another person or group. Learn more in our

Abusive behavior policy

https://stackoverflow.com/conduct/abusive-behavior

Not needed.

This comment is not relevant to the post.

Enter at least 6 characters

Something else.

A problem not listed above. Try to be as specific as possible.

Enter at least 6 characters

Flag comment Cancel

You have 0 flags left today

Hang on, you can't upvote just yet.

You'll need to complete a few actions and gain 15 reputation points before being able to upvote.

indicates when questions and answers are useful.

What's reputation and how do I get it?

https://stackoverflow.com/help/whats-reputation

Instead, you can save this post to reference later.

Save this post for later Not now

https://stackoverflow.com/

Stack Overflow

https://stackoverflow.com/

https://stackoverflow.com/questions

https://stackoverflow.com/help

https://chat.stackoverflow.com/?tab=explore

https://stackoverflow.co/

Stack Internal

https://stackoverflow.co/internal/?utm\_medium=referral&utm\_source=stackoverflow-community&utm\_campaign=footer&utm\_content=teams

Stack Data Licensing

https://stackoverflow.co/data-licensing/?utm\_medium=referral&utm\_source=stackoverflow-community&utm\_campaign=footer&utm\_content=data-licensing

https://stackoverflow.co/advertising/?utm\_medium=referral&utm\_source=stackoverflow-community&utm\_campaign=footer&utm\_content=advertising

https://stackoverflow.co/

https://stackoverflow.co/

https://stackoverflow.co/company/press/

https://stackoverflow.co/company/work-here/

https://stackoverflow.com/legal

Privacy Policy

https://stackoverflow.com/legal/privacy-policy

Terms of Service

https://stackoverflow.com/legal/terms-of-service/public

https://stackoverflow.com/contact

Your Privacy Choices

Cookie Policy

https://policies.stackoverflow.co/stack-overflow/cookie-policy

Stack Exchange Network

https://stackexchange.com/

https://stackexchange.com/sites#technology

Culture & recreation

https://stackexchange.com/sites#culturerecreation

Life & arts

https://stackexchange.com/sites#lifearts

https://stackexchange.com/sites#science

Professional

https://stackexchange.com/sites#professional

https://stackexchange.com/sites#business

https://api.stackexchange.com/

https://data.stackexchange.com/

https://stackoverflow.blog?blb=1

https://www.facebook.com/officialstackoverflow/

https://twitter.com/stackoverflow

https://linkedin.com/company/stack-overflow

https://www.instagram.com/thestackoverflow

Site design / logo © 2026 Stack Exchange Inc; user contributions licensed under

https://stackoverflow.com/help/licensing

. rev 2026.5.13.43074

By continuing to use this website, you agree Stack Exchange can store cookies on your device and disclose information in accordance with our

Cookie Policy

https://policies.stackoverflow.co/stack-overflow/cookie-policy/

. By exiting this window, default cookies will be accepted. To reject cookies, select an option from below.

Necessary cookies only

Customize settings

Report this ad

