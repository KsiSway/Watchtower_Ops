---
sourceFile: "nodejs environment variable "NODE_EXTRA_CA_CERTS" - Stack Overflow"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.911Z"
---

# nodejs environment variable "NODE_EXTRA_CA_CERTS" - Stack Overflow

987573d7-f1e8-4136-919b-c5d55c3a387f

nodejs environment variable "NODE\_EXTRA\_CA\_CERTS" - Stack Overflow

d20c1eaf-94cc-4c11-9dfa-c32a00ba5999

https://stackoverflow.com/questions/44459971/nodejs-environment-variable-node-extra-ca-certs

node.js - nodejs environment variable "NODE\_EXTRA\_CA\_CERTS" - Stack Overflow

Skip to main content

https://stackoverflow.com/questions/44459971/nodejs-environment-variable-node-extra-ca-certs#content

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

https://stackoverflow.com/users/signup?ssrc=site\_switcher&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f44459971%2fnodejs-environment-variable-node-extra-ca-certs

https://stackoverflow.com/users/login?ssrc=site\_switcher&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f44459971%2fnodejs-environment-variable-node-extra-ca-certs

to customize your list.

more stack exchange communities

https://stackexchange.com/sites

company blog

https://stackoverflow.blog/

https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f44459971%2fnodejs-environment-variable-node-extra-ca-certs

https://stackoverflow.com/users/signup?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f44459971%2fnodejs-environment-variable-node-extra-ca-certs

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

nodejs environment variable "NODE\_EXTRA\_CA\_CERTS"

https://stackoverflow.com/questions/44459971/nodejs-environment-variable-node-extra-ca-certs

Ask Question

https://stackoverflow.com/questions/ask

Asked 8 years, 11 months ago

1 year, 7 months ago

https://stackoverflow.com/questions/44459971/nodejs-environment-variable-node-extra-ca-certs?lastactivity

Viewed 77k times

https://stackoverflow.com/posts/44459971/timeline

I am developing a mobile application based on Ionic + Angular + Cordova + Node js.

the application visits a https server via window.XMLHttpRequest:

module.exports = function request (method, url, body, headers) {
  return new Promise(function (resolve, reject) {
    var xhr = new window.XMLHttpRequest()

    xhr.open(method, url)

    xhr.onload = function () {
      return resolve({
        status: xhr.status,
        body: xhr.responseText
      })
    }

    xhr.onerror = xhr.onabort = function () {
      return reject(new Error(xhr.statusText || 'XHR aborted: ' + url))
    }

    Object.keys(headers).forEach(function (header) {
      xhr.setRequestHeader(header, headers\[header\])
    })

    xhr.send(body)
  })
}

for this function to be executed, an appropriate root CA need to be inserted into node environment. since I do not control the code that makes the https request, I would prefer a policy/config based approach that enables an extra root CA into node js.

I searched around, and found out that node had actually provided a environment variable '

NODE\_EXTRA\_CA\_CERTS

https://nodejs.org/api/cli.html#cli\_node\_extra\_ca\_certs\_file

' that seems to meet my purpose.

yet I can not find any examples on how to utilize this variable.

my implementation is to install the npm package

dotenv-webpack

https://www.npmjs.com/package/dotenv-webpack

added a .env file which contains configuration 'NODE\_EXTRA\_CA\_CERTS=./assets/cert/cacert.pem' (file path to the appropriate root CA).

I can verify that the variable NODE\_EXTRA\_CA\_CERTS had been successfully set. yet it did not seem to have any effects. the access to the server was denied because of security.

so my question: can anyone please provide an example on how to utilize the variable 'NODE\_EXTRA\_CA\_CERTS'?

https://stackoverflow.com/questions/tagged/node.js

https://stackoverflow.com/questions/tagged/angular

https://stackoverflow.com/questions/tagged/ssl

https://stackoverflow.com/questions/tagged/ionic2

https://stackoverflow.com/questions/tagged/tls1.2

https://stackoverflow.com/q/44459971

Improve this question

https://stackoverflow.com/posts/44459971/edit

asked Jun 9, 2017 at 14:09

George Wang

https://stackoverflow.com/users/4749366/george-wang

834 2 2 gold badges 14 14 silver badges 30 30 bronze badges

Add a comment

https://stackoverflow.com/questions/44459971/nodejs-environment-variable-node-extra-ca-certs

2 Answers 2

Reset to default

https://stackoverflow.com/questions/44459971/nodejs-environment-variable-node-extra-ca-certs?answertab=scoredesc#tab-top

Highest score (default)

Trending (recent votes count more)

Date modified (newest first)

Date created (oldest first)

https://stackoverflow.com/posts/45325822/timeline

So the env variable you are talking about is provided at a "system" level so you shouldn't need to define the variable locally in the env file.

If you wanna access the variable, you should use the following configuration on dotenv-webpack:

Dotenv({
  systemvars: true
})

This will allow you to access the system-level variables. To access the variable you will use the variable:

process.env.NODE\_EXTRA\_CA\_CERTS

stores information about the node process running.

stores all the environment variables (that get populated by

dotenv-webpack

You can read more about the

global variables here:

https://nodejs.org/api/process.html

https://nodejs.org/api/process.html

https://stackoverflow.com/a/45325822

Improve this answer

https://stackoverflow.com/posts/45325822/edit

answered Jul 26, 2017 at 11:37

https://stackoverflow.com/users/4787734/matt

139 3 3 bronze badges

Sign up to request clarification or add additional context in comments.

Add a comment

https://stackoverflow.com/posts/79018986/timeline

NODE\_EXTRA\_CA\_CERTS

must be set in the environment when Node starts. By the time

loads your env file it is too late to change it.

documentation

https://nodejs.org/dist/latest-v20.x/docs/api/cli.html#node\_extra\_ca\_certsfile

NODE\_EXTRA\_CA\_CERTS

environment variable is only read when the Node.js process is first launched. Changing the value at runtime using

process.env.NODE\_EXTRA\_CA\_CERTS

has no effect on the current process.

https://github.com/nodejs/node/issues/51426

https://github.com/nodejs/node/issues/51426

for discussion about possibly changing that behavior.

https://stackoverflow.com/a/79018986

Improve this answer

https://stackoverflow.com/posts/79018986/edit

answered Sep 24, 2024 at 14:07

Jason Kohles

https://stackoverflow.com/users/3443454/jason-kohles

932 1 1 gold badge 9 9 silver badges 13 13 bronze badges

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

https://stackoverflow.com/users/login?ssrc=question\_page&returnurl=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F44459971%2Fnodejs-environment-variable-node-extra-ca-certs%23new-answer

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

https://stackoverflow.com/questions/tagged/angular

https://stackoverflow.com/questions/tagged/ssl

https://stackoverflow.com/questions/tagged/ionic2

https://stackoverflow.com/questions/tagged/tls1.2

See similar questions with these tags.

The Overflow Blog

Connecting the dots for accurate AI

https://stackoverflow.blog/2026/05/12/connecting-the-dots-for-accurate-ai/

Observability and human intuition in an AI world

https://stackoverflow.blog/2026/05/15/observability-and-human-intuition-in-an-ai-world/

Featured on Meta

(Almost) One year of Challenges

https://meta.stackexchange.com/questions/418261/almost-one-year-of-challenges

Policy: Generative AI (e.g., ChatGPT) is banned

https://meta.stackoverflow.com/questions/421831/policy-generative-ai-e-g-chatgpt-is-banned

https://stackoverflow.com/questions/77534939/why-the-ca-root-certificate-cannot-work-in-some-environment

Why the CA root certificate cannot work in some environment?

https://stackoverflow.com/questions/77534939/why-the-ca-root-certificate-cannot-work-in-some-environment?noredirect=1

https://stackoverflow.com/questions/21855035/ssl-error-cert-untrusted-while-using-npm-command

SSL Error: CERT\_UNTRUSTED while using npm command

https://stackoverflow.com/questions/21855035/ssl-error-cert-untrusted-while-using-npm-command

https://stackoverflow.com/questions/32966878/error-ssl-issue-npm-windows

Error SSL Issue npm WIndows

https://stackoverflow.com/questions/32966878/error-ssl-issue-npm-windows

https://stackoverflow.com/questions/39243446/ionic-gives-prompt-acquire-a-developer-license-install-the-signing-certificate

Ionic gives prompt: Acquire a developer license, Install the signing certificate

https://stackoverflow.com/questions/39243446/ionic-gives-prompt-acquire-a-developer-license-install-the-signing-certificate

https://stackoverflow.com/questions/47680191/ionic-3-node-js-self-signed-certificate-in-certificate-chain-how-to-disable

ionic 3 / node.js - Self signed certificate in certificate chain (how to disable strict-ssl?)

https://stackoverflow.com/questions/47680191/ionic-3-node-js-self-signed-certificate-in-certificate-chain-how-to-disable

https://stackoverflow.com/questions/48606923/unable-to-verify-the-first-certificate-when-ionic-start-using-command-prompt

Unable to verify the first certificate when ionic start using command prompt

https://stackoverflow.com/questions/48606923/unable-to-verify-the-first-certificate-when-ionic-start-using-command-prompt

https://stackoverflow.com/questions/54840830/httpclient-cannot-ignore-or-bypass-self-signed-certificate-error

HttpClient cannot ignore or bypass self signed certificate error

https://stackoverflow.com/questions/54840830/httpclient-cannot-ignore-or-bypass-self-signed-certificate-error

https://stackoverflow.com/questions/58003508/err-ssl-protocol-error-when-i-try-to-connect-with-localhost

ERR\_SSL\_PROTOCOL\_ERROR when i try to connect with localhost

https://stackoverflow.com/questions/58003508/err-ssl-protocol-error-when-i-try-to-connect-with-localhost

https://stackoverflow.com/questions/63033478/still-receiving-ssl-error-cert-has-expired-after-setting-node-extra-ca-certs

Still receiving SSL error "CERT\_HAS\_EXPIRED" after setting NODE\_EXTRA\_CA\_CERTS

https://stackoverflow.com/questions/63033478/still-receiving-ssl-error-cert-has-expired-after-setting-node-extra-ca-certs

https://stackoverflow.com/questions/70198705/how-can-i-set-node-extra-ca-certs-on-node

How can I set NODE\_EXTRA\_CA\_CERTS on node

https://stackoverflow.com/questions/70198705/how-can-i-set-node-extra-ca-certs-on-node

https://stackoverflow.com/questions/74727582/how-to-set-envnode-extra-ca-certs-to-default-value

How to set $env:NODE\_EXTRA\_CA\_CERTS to "default" value?

https://stackoverflow.com/questions/74727582/how-to-set-envnode-extra-ca-certs-to-default-value

Hot Network Questions

https://stackexchange.com/questions?tab=hot

Poynting vector of point charge in uniform motion

https://physics.stackexchange.com/questions/872302/poynting-vector-of-point-charge-in-uniform-motion

In Acts 2:2, why would an immaterial "spirit" make the sound of wind blowing?

https://hermeneutics.stackexchange.com/questions/116409/in-acts-22-why-would-an-immaterial-spirit-make-the-sound-of-wind-blowing

Why my calculations don't seem to match with LTspice simulation despite modeling the MOSFET as simple as possible

https://electronics.stackexchange.com/questions/768928/why-my-calculations-dont-seem-to-match-with-ltspice-simulation-despite-modeling

Books with multiple proofs of one statement

https://math.stackexchange.com/questions/5136771/books-with-multiple-proofs-of-one-statement

A criterion of cyclic group

https://mathoverflow.net/questions/511247/a-criterion-of-cyclic-group

renewcommand Gamma into itGamma in unicode-math

https://tex.stackexchange.com/questions/762771/renewcommand-gamma-into-itgamma-in-unicode-math

Transfer from Frankfurt airport to train station

https://travel.stackexchange.com/questions/203718/transfer-from-frankfurt-airport-to-train-station

TerminatedEvaluation\["RecursionLimit"\] for Series in version 13

https://mathematica.stackexchange.com/questions/319407/terminatedevaluationrecursionlimit-for-series-in-version-13

Does the F-16 experience ground effect?

https://aviation.stackexchange.com/questions/115245/does-the-f-16-experience-ground-effect

Why isn't C mode indenting this code properly?

https://emacs.stackexchange.com/questions/85764/why-isnt-c-mode-indenting-this-code-properly

Was John the Baptist an Essene and was he a vegetarian?

https://christianity.stackexchange.com/questions/113829/was-john-the-baptist-an-essene-and-was-he-a-vegetarian

How can a curved bow shock be considered a normal shock?

https://aviation.stackexchange.com/questions/115238/how-can-a-curved-bow-shock-be-considered-a-normal-shock

How to turn "Alt+l+e+up-key+enter" combination into a shortcut?

https://askubuntu.com/questions/1566755/how-to-turn-altleup-keyenter-combination-into-a-shortcut

Ubuntu 26 / gnome 50 default image-viewer is not closing with esc key

https://askubuntu.com/questions/1566728/ubuntu-26-gnome-50-default-image-viewer-is-not-closing-with-esc-key

How do I fix these edges/faces from intersectiong in Geometry nodes

https://blender.stackexchange.com/questions/346685/how-do-i-fix-these-edges-faces-from-intersectiong-in-geometry-nodes

Licensing rights of an only contributor into a No-license github repository, created by another user

https://opensource.stackexchange.com/questions/15766/licensing-rights-of-an-only-contributor-into-a-no-license-github-repository-cre

Remember coordinate in nested tikzpicture with listings

https://tex.stackexchange.com/questions/762759/remember-coordinate-in-nested-tikzpicture-with-listings

How to figure the basis for this redemption?

https://money.stackexchange.com/questions/169576/how-to-figure-the-basis-for-this-redemption

One Thought per Sentence

https://writing.stackexchange.com/questions/72461/one-thought-per-sentence

Picking the right preposition after a verb

https://english.stackexchange.com/questions/639720/picking-the-right-preposition-after-a-verb

Need a way to physically bookmark adventure books

https://rpg.stackexchange.com/questions/219317/need-a-way-to-physically-bookmark-adventure-books

the problem of balls dropped from a skyscraper

https://math.stackexchange.com/questions/5136844/the-problem-of-balls-dropped-from-a-skyscraper

How can I present a highly interdisciplinary PhD talk in 15 minutes / 30 minutes?

https://academia.stackexchange.com/questions/226684/how-can-i-present-a-highly-interdisciplinary-phd-talk-in-15-minutes-30-minutes

SQL Login Audit stop applications from connecting to DB?

https://dba.stackexchange.com/questions/350262/sql-login-audit-stop-applications-from-connecting-to-db

more hot questions

https://stackoverflow.com/questions/44459971/nodejs-environment-variable-node-extra-ca-certs

Question feed

https://stackoverflow.com/feeds/question/44459971

Subscribe to RSS

Question feed

To subscribe to this RSS feed, copy and paste this URL into your RSS reader.

https://stackoverflow.com/feeds/question/44459971

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

