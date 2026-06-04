---
sourceFile: "I have created a Certificate already. I just don't know what to do after that. Like it said in the post just pasted the command and ran but getting this error. Please help : r/TizenTube - Reddit"
exportedBy: "Kortex"
exportDate: "2026-05-20T06:50:17.398Z"
---

# I have created a Certificate already. I just don't know what to do after that. Like it said in the post just pasted the command and ran but getting this error. Please help : r/TizenTube - Reddit

97c67814-8b42-4979-82f9-06e3ef386e45

I have created a Certificate already. I just don't know what to do after that. Like it said in the post just pasted the command and ran but getting this error. Please help : r/TizenTube - Reddit

2f62cbb7-7f3e-464b-8ac8-81930682cc98

https://www.reddit.com/r/TizenTube/comments/1i8hzui/i\_have\_created\_a\_certificate\_already\_i\_just\_dont/

I have created a Certificate already. I just don't know what to do after that. Like it said in the post just pasted the command and ran but getting this error. Please help : r/TizenTube

Skip to main content

https://www.reddit.com/r/TizenTube/comments/1i8hzui/i\_have\_created\_a\_certificate\_already\_i\_just\_dont/#main-content

I have created a Certificate already. I just don't know what to do after that. Like it said in the post just pasted the command and ran but getting this error. Please help : r/TizenTube

Open navigation

https://www.reddit.com/

Go to Reddit Home

r/TizenTube

https://www.reddit.com/register/

Sign up for Reddit

https://www.reddit.com/login/

Log in to Reddit

Expand user menu

Open settings menu

Skip to Navigation

https://www.reddit.com/r/TizenTube/comments/1i8hzui/i\_have\_created\_a\_certificate\_already\_i\_just\_dont/#left-sidebar-container

Skip to Right Sidebar

https://www.reddit.com/r/TizenTube/comments/1i8hzui/i\_have\_created\_a\_certificate\_already\_i\_just\_dont/#right-sidebar-container

Go to TizenTube

https://www.reddit.com/r/TizenTube/

r/TizenTube

https://www.reddit.com/r/TizenTube/

Soft\_Couple\_4962

https://www.reddit.com/user/Soft\_Couple\_4962/

Locked post

Stickied post

Archived post

I have created a Certificate already. I just don't know what to do after that. Like it said in the post just pasted the command and ran but getting this error. Please help

Upvote 2 Downvote 10 Go to comments Share

Sort by: Best

Open comment sort options

Controversial

Search Comments Expand comment search

Comments Section

Pure\_Force8771

https://www.reddit.com/user/Pure\_Force8771/

https://www.reddit.com/r/TizenTube/comments/1i8hzui/comment/m9ordd3/

Do not create Tizen certificate, but Samsung instead, in a process you will have to sign in to the Samsung account and then the certificate will be created.

tizen package -t wgt -s "name of the Samsung certificate" -o ./resigned -- "C:\Users\XXX\Downloads\TizenBrewStandalo

ne-Old.wgt"

tizen install -n ./resigned/TizenBrewStandalone-Old.wgt

now the app is installed on your TV/Smart Monitor

go to the apps again, to the bottom, apps settings, type 12345 and click done, change IP to

http://127.0.0.1/

run the TizenBrew

and i am not sure but just run TizenTube you will see on screan after some time and app restart

Soft\_Couple\_4962

https://www.reddit.com/user/Soft\_Couple\_4962/

https://www.reddit.com/r/TizenTube/comments/1i8hzui/comment/m9ou9oz/

I have already created a samsung certificate using samsung account. Can you tell what name I need to put? Profile name or name of certificate and what location should I put certificate in?

More replies

https://www.reddit.com/r/TizenTube/comments/1i8hzui/comment/m9ou9oz/?force-legacy-sct=1

Pure\_Force8771

https://www.reddit.com/user/Pure\_Force8771/

https://www.reddit.com/r/TizenTube/comments/1i8hzui/comment/m9p1fkd/

Download the

file which is the package you'll need.

#### Steps to Resign TizenBrew:

#### Open a Command-Line Interface:

Use Command Prompt (Windows) or Terminal (Linux).

#### Resign the Package:

Navigate to the directory of the TizenBrew package.

#### Run the resignation command:

tizen package -t wgt -s <profile\_name> -o ./resigned -- path/to/TizenBrewStandalone.wgt

<profile\_name>

with your Samsung certificate profile name and adjust the path to the TizenBrew

package accordingly.

tizen package -t wgt -s MyCertificate -o ./resigned -- /Downloads/TizenBrewStandalone.wgt

#### Install the Resigned Package:

#### Run the installation command:

tizen install -n TizenBrewStandalone.wgt

#### Additional Setup:

#### Configure Host PC IP Address:

Set the host PC IP address on your TV to

https://developer.samsung.com/tv/develop/getting-started/setting-up-your-network

if needed to ensure proper configuration.

#### Launch TizenBrew on Your TV:

Once installed, navigate to your TV's apps and launch TizenBrew.

https://www.reddit.com/user/FoxReis/

Arbiterandrea

https://www.reddit.com/user/Arbiterandrea/

https://www.reddit.com/r/TizenTube/comments/1i8hzui/comment/maddwlt/

Hey, I follow this guide, 1 and 2 are done but now I am stuck at step 3. I keep getting the error tizen isn't a command. I don't get what I doing wrong

More replies

https://www.reddit.com/r/TizenTube/comments/1i8hzui/comment/maddwlt/?force-legacy-sct=1

https://www.reddit.com/user/tristobal/

https://www.reddit.com/r/TizenTube/comments/1i8hzui/comment/mbx4w19/

That means that you certificate is not releated with the DUID of your TV. I had the same problem because I had created the certificate wrong as I skipped a step in installation of tizen studio. In this

https://developer.samsung.com/smarttv/develop/getting-started/setting-up-sdk/installing-tv-sdk.html

I have skipped the "Install the requitred extension" when you install it you will be abled to create the certificate specially for your DUID. (

https://developer.samsung.com/smarttv/develop/getting-started/setting-up-sdk/creating-certificates.html

https://developer.samsung.com/smarttv/develop/getting-started/setting-up-sdk/creating-certificates.html

I hope it helps you.

Upvote 1 Downvote Reply Award Share

https://www.reddit.com/user/Gamerz\_X90/

https://www.reddit.com/r/TizenTube/comments/1i8hzui/comment/o4bslig/

To add to this, make sure to choose to create a new Distributor Certificate while being connected to the TV, It will automatically detect the DUID and then it can install properly

Upvote 1 Downvote Reply Award Share

Double-Birthday-6507

https://www.reddit.com/user/Double-Birthday-6507/

https://www.reddit.com/r/TizenTube/comments/1i8hzui/comment/mvvz4hc/

I I have the same certificate error. I followed all the guidelines. Can someone help.

Upvote 1 Downvote Reply Award Share

New to Reddit?

Create your account and connect with a world of communities.

Continue with Email

https://www.reddit.com/register/

Continue with Phone Number

https://www.reddit.com/login/

By continuing, you agree to our

User Agreement

https://www.redditinc.com/policies/user-agreement

and acknowledge that you understand the

Privacy Policy

https://www.redditinc.com/policies/privacy-policy

Related Answers Section

Related Answers

Top apps for enhancing streaming experience

https://www.reddit.com/answers/f781bee1-6437-49d2-98ce-877aa21ea15d/?q=Top+apps+for+enhancing+streaming+experience&source=PDP

Best software for video editing on Tizen

https://www.reddit.com/answers/be7935fc-65d0-4fd5-a171-b23803713f0d/?q=Best+software+for+video+editing+on+Tizen&source=PDP

Latest trends in streaming technology

https://www.reddit.com/answers/d14bea62-08dd-4ec5-90a3-693ce38cd92d/?q=Latest+trends+in+streaming+technology&source=PDP

Must-have features in streaming apps

https://www.reddit.com/answers/bce7cc3f-08f3-4f36-9e93-bad6de33d227/?q=Must-have+features+in+streaming+apps&source=PDP

Innovative uses of Tizen in smart devices

https://www.reddit.com/answers/d93d606d-d55b-402d-b199-ff470bfffbc5/?q=Innovative+uses+of+Tizen+in+smart+devices&source=PDP

Edited a Word Doc sent as an attachment, saved, and now I can't access it because 'directory name is invalid'

https://www.reddit.com/r/techsupport/comments/1gtj4vm/edited\_a\_word\_doc\_sent\_as\_an\_attachment\_saved\_and/

r/techsupport

https://www.reddit.com/r/techsupport/

Edited a Word Doc sent as an attachment, saved, and now I can't access it because 'directory name is invalid'

\](https://www.reddit.com/r/techsupport/comments/1gtj4vm/edited\_a\_word\_doc\_sent\_as\_an\_attachment\_saved\_and/) 1 upvote · 4 comments

An error has occurred. Please let again later. If the problem persists, please make a note of the error code and visit support.nintendo.com.

https://www.reddit.com/r/PokemonHome/comments/1gaqprz/an\_error\_has\_occurred\_please\_let\_again\_later\_if/

r/PokemonHome

https://www.reddit.com/r/PokemonHome/

An error has occurred. Please let again later. If the problem persists, please make a note of the error code and visit support.nintendo.com.

\](https://www.reddit.com/r/PokemonHome/comments/1gaqprz/an\_error\_has\_occurred\_please\_let\_again\_later\_if/) 2 comments

Jai+ update: site restored after security incident + domain change

https://www.reddit.com/r/googleplus/comments/1slwka0/jai\_update\_site\_restored\_after\_security\_incident/

r/googleplus

https://www.reddit.com/r/googleplus/

- 1mo ago \[

Jai+ update: site restored after security incident + domain change

\](https://www.reddit.com/r/googleplus/comments/1slwka0/jai\_update\_site\_restored\_after\_security\_incident/) 9 upvotes · 10 comments

I tried to run bloodborne once after watching a tutorial on shadps4, and it crashed almost immediately after i started a new game. noww the emulator wont open and i get an error message. i need help please

https://www.reddit.com/r/shadps4/comments/1htgetm/i\_tried\_to\_run\_bloodborne\_once\_after\_watching\_a/

https://www.reddit.com/r/shadps4/

I tried to run bloodborne once after watching a tutorial on shadps4, and it crashed almost immediately after i started a new game. noww the emulator wont open and i get an error message. i need help please

\](https://www.reddit.com/r/shadps4/comments/1htgetm/i\_tried\_to\_run\_bloodborne\_once\_after\_watching\_a/) 1 upvote · 1 comment

Activation error anyway I can fix

https://www.reddit.com/r/LegacyJailbreak/comments/1sdz2vf/activation\_error\_anyway\_i\_can\_fix/

r/LegacyJailbreak

https://www.reddit.com/r/LegacyJailbreak/

- 1mo ago \[

Activation error anyway I can fix

\](https://www.reddit.com/r/LegacyJailbreak/comments/1sdz2vf/activation\_error\_anyway\_i\_can\_fix/)

2 14 upvotes · 18 comments

Update 26.0.6.0291 – “Can't find valid format” / “Unknown error” fixed

https://www.reddit.com/r/4kdownloadapps/comments/1rldmnm/update\_26060291\_cant\_find\_valid\_format\_unknown/

r/4kdownloadapps

https://www.reddit.com/r/4kdownloadapps/

- 3mo ago \[

Update 26.0.6.0291 – “Can't find valid format” / “Unknown error” fixed

\](https://www.reddit.com/r/4kdownloadapps/comments/1rldmnm/update\_26060291\_cant\_find\_valid\_format\_unknown/) 29 upvotes · 26 comments

Can't install update 30.90

https://www.reddit.com/r/SmartTubeNext/comments/1rh8xvb/cant\_install\_update\_3090/

r/SmartTubeNext

https://www.reddit.com/r/SmartTubeNext/

- 3mo ago \[

Can't install update 30.90

\](https://www.reddit.com/r/SmartTubeNext/comments/1rh8xvb/cant\_install\_update\_3090/) 6 upvotes · 18 comments

Am I fucked?

https://www.reddit.com/r/mahindrabe6/comments/1sfoknv/am\_i\_fucked/

r/mahindrabe6

https://www.reddit.com/r/mahindrabe6/

- 1mo ago \[

Am I fucked?

\](https://www.reddit.com/r/mahindrabe6/comments/1sfoknv/am\_i\_fucked/)

2 13 upvotes · 19 comments

Any fix for this?

https://www.reddit.com/r/SmartTubeNext/comments/1rzwstm/any\_fix\_for\_this/

r/SmartTubeNext

https://www.reddit.com/r/SmartTubeNext/

- 2mo ago \[

Any fix for this?

\](https://www.reddit.com/r/SmartTubeNext/comments/1rzwstm/any\_fix\_for\_this/)

5 upvotes · 9 comments

Error fetching release asset

https://www.reddit.com/r/TizenTube/comments/1p5kwkc/error\_fetching\_release\_asset/

r/TizenTube

https://www.reddit.com/r/TizenTube/

- 6mo ago \[

Error fetching release asset

\](https://www.reddit.com/r/TizenTube/comments/1p5kwkc/error\_fetching\_release\_asset/)

9 upvotes · 8 comments

Latest update broke it

https://www.reddit.com/r/SmartTubeNext/comments/1shyolg/latest\_update\_broke\_it/

r/SmartTubeNext

https://www.reddit.com/r/SmartTubeNext/

- 1mo ago \[

Latest update broke it

\](https://www.reddit.com/r/SmartTubeNext/comments/1shyolg/latest\_update\_broke\_it/) 18 upvotes · 19 comments

Is anyone else experiencing these issues?

https://www.reddit.com/r/MorpheApp/comments/1tdxa7o/is\_anyone\_else\_experiencing\_these\_issues/

r/MorpheApp

https://www.reddit.com/r/MorpheApp/

Is anyone else experiencing these issues?

\](https://www.reddit.com/r/MorpheApp/comments/1tdxa7o/is\_anyone\_else\_experiencing\_these\_issues/) 25 upvotes · 15 comments

I usually dont like asking for help like this but i am so frustrated right now. I am trying to learn animation and i'm having issues with cyclic modifier. at least i think i do?

https://www.reddit.com/r/blenderhelp/comments/1gdh5v6/i\_usually\_dont\_like\_asking\_for\_help\_like\_this\_but/

r/blenderhelp

https://www.reddit.com/r/blenderhelp/

I usually dont like asking for help like this but i am so frustrated right now. I am trying to learn animation and i'm having issues with cyclic modifier. at least i think i do?

\](https://www.reddit.com/r/blenderhelp/comments/1gdh5v6/i\_usually\_dont\_like\_asking\_for\_help\_like\_this\_but/) 1 upvote · 3 comments

Update not happening

https://www.reddit.com/r/SmartTubeNext/comments/1t56x59/update\_not\_happening/

r/SmartTubeNext

https://www.reddit.com/r/SmartTubeNext/

- 14d ago \[

Update not happening

\](https://www.reddit.com/r/SmartTubeNext/comments/1t56x59/update\_not\_happening/)

24 upvotes · 41 comments

Facebook won't work and i don't know what to do. look at text below for more info

https://www.reddit.com/r/facebook/comments/1i5vbvm/facebook\_wont\_work\_and\_i\_dont\_know\_what\_to\_do/

https://www.reddit.com/r/facebook/

Facebook won't work and i don't know what to do. look at text below for more info

\](https://www.reddit.com/r/facebook/comments/1i5vbvm/facebook\_wont\_work\_and\_i\_dont\_know\_what\_to\_do/)

2 2 upvotes · 3 comments

I don't know how to reset this ONN. Tablet.

https://www.reddit.com/r/techsupport/comments/1ho9tbq/i\_dont\_know\_how\_to\_reset\_this\_onn\_tablet/

r/techsupport

https://www.reddit.com/r/techsupport/

I don't know how to reset this ONN. Tablet.

\](https://www.reddit.com/r/techsupport/comments/1ho9tbq/i\_dont\_know\_how\_to\_reset\_this\_onn\_tablet/) 4 upvotes · 54 comments

This is gonna be my first ever preorder and the most expensive I ever paid for a game. Wish me luck

https://www.reddit.com/r/indotech/comments/1tds7jf/this\_is\_gonna\_be\_my\_first\_ever\_preorder\_and\_the/

https://www.reddit.com/r/indotech/

This is gonna be my first ever preorder and the most expensive I ever paid for a game. Wish me luck

\](https://www.reddit.com/r/indotech/comments/1tds7jf/this\_is\_gonna\_be\_my\_first\_ever\_preorder\_and\_the/)

100 upvotes · 100 comments

Please help urgent!

https://www.reddit.com/r/LaptopDealsIndia/comments/1tcakrp/please\_help\_urgent/

r/LaptopDealsIndia

https://www.reddit.com/r/LaptopDealsIndia/

Please help urgent!

\](https://www.reddit.com/r/LaptopDealsIndia/comments/1tcakrp/please\_help\_urgent/)

42 upvotes · 32 comments

650 installs in a month

https://www.reddit.com/r/googleplayconsole/comments/1r6e3ud/650\_installs\_in\_a\_month/

r/googleplayconsole

https://www.reddit.com/r/googleplayconsole/

- 3mo ago \[
650 installs in a month

\](https://www.reddit.com/r/googleplayconsole/comments/1r6e3ud/650\_installs\_in\_a\_month/)

27 upvotes · 20 comments

I tried to download Just Cause 3 and don't know what to do

https://www.reddit.com/r/FitGirlRepack/comments/1gss9pk/i\_tried\_to\_download\_just\_cause\_3\_and\_dont\_know/

r/FitGirlRepack

https://www.reddit.com/r/FitGirlRepack/

I tried to download Just Cause 3 and don't know what to do

\](https://www.reddit.com/r/FitGirlRepack/comments/1gss9pk/i\_tried\_to\_download\_just\_cause\_3\_and\_dont\_know/)

Update: They rip!

https://www.reddit.com/r/telemark/comments/1psbigr/update\_they\_rip/

https://www.reddit.com/r/telemark/

- 5mo ago \[

Update: They rip!

\](https://www.reddit.com/r/telemark/comments/1psbigr/update\_they\_rip/)

58 upvotes · 74 comments

Am I cooked ?

https://www.reddit.com/r/GalaxyS20FE/comments/1somht5/am\_i\_cooked/

r/GalaxyS20FE

https://www.reddit.com/r/GalaxyS20FE/

- 1mo ago \[

Am I cooked ?

\](https://www.reddit.com/r/GalaxyS20FE/comments/1somht5/am\_i\_cooked/)

29 upvotes · 22 comments

My devices, since new, have all been jailbroken 😊

https://www.reddit.com/r/LegacyJailbreak/comments/1s5v7al/my\_devices\_since\_new\_have\_all\_been\_jailbroken/

r/LegacyJailbreak

https://www.reddit.com/r/LegacyJailbreak/

- 2mo ago \[

My devices, since new, have all been jailbroken 😊

\](https://www.reddit.com/r/LegacyJailbreak/comments/1s5v7al/my\_devices\_since\_new\_have\_all\_been\_jailbroken/)

2 73 upvotes · 12 comments

Me and the Bill back at it

https://www.reddit.com/r/Creality\_k2/comments/1t1k861/me\_and\_the\_bill\_back\_at\_it/

r/Creality\_k2

https://www.reddit.com/r/Creality\_k2/

- 18d ago \[

Me and the Bill back at it

\](https://www.reddit.com/r/Creality\_k2/comments/1t1k861/me\_and\_the\_bill\_back\_at\_it/)

49 upvotes · 6 comments

I coded my first program, and it has some errors idk how to resolve

https://www.reddit.com/r/learnpython/comments/1ghi4vv/i\_coded\_my\_first\_program\_and\_it\_has\_some\_errors/

r/learnpython

https://www.reddit.com/r/learnpython/

I coded my first program, and it has some errors idk how to resolve

\](https://www.reddit.com/r/learnpython/comments/1ghi4vv/i\_coded\_my\_first\_program\_and\_it\_has\_some\_errors/) 19 comments

View Post in

https://www.reddit.com/r/TizenTube/comments/1i8hzui/i\_have\_created\_a\_certificate\_already\_i\_just\_dont/?tl=hi

Português (Brasil)

https://www.reddit.com/r/TizenTube/comments/1i8hzui/i\_have\_created\_a\_certificate\_already\_i\_just\_dont/?tl=pt-br

https://www.reddit.com/r/TizenTube/comments/1i8hzui/i\_have\_created\_a\_certificate\_already\_i\_just\_dont/?tl=fr

https://www.reddit.com/r/TizenTube/comments/1i8hzui/i\_have\_created\_a\_certificate\_already\_i\_just\_dont/?tl=zh-hans

https://www.reddit.com/r/TizenTube/comments/1i8hzui/i\_have\_created\_a\_certificate\_already\_i\_just\_dont/?tl=ja

https://www.reddit.com/r/TizenTube/comments/1i8hzui/i\_have\_created\_a\_certificate\_already\_i\_just\_dont/?tl=ru

See more See fewer

https://www.reddit.com/r/TizenTube/comments/1i8hzui/i\_have\_created\_a\_certificate\_already\_i\_just\_dont/?tl=sv

https://www.reddit.com/r/TizenTube/comments/1i8hzui/i\_have\_created\_a\_certificate\_already\_i\_just\_dont/?tl=hu

https://www.reddit.com/r/TizenTube/comments/1i8hzui/i\_have\_created\_a\_certificate\_already\_i\_just\_dont/?tl=nl

https://www.reddit.com/r/TizenTube/comments/1i8hzui/i\_have\_created\_a\_certificate\_already\_i\_just\_dont/?tl=th

https://www.reddit.com/r/TizenTube/comments/1i8hzui/i\_have\_created\_a\_certificate\_already\_i\_just\_dont/?tl=pl

Español (Latinoamérica)

https://www.reddit.com/r/TizenTube/comments/1i8hzui/i\_have\_created\_a\_certificate\_already\_i\_just\_dont/?tl=es-419

Community Info Section

r/TizenTube

https://www.reddit.com/r/TizenTube/

The official subreddit for TizenTube https://github.com/reisxd/TizenTube

Anyone can view, post, and comment to this community

Reddit reReddit: Top posts of January 23, 2025

https://www.reddit.com/posts/2025/january-23-1/global/

Reddit reReddit: Top posts of January 2025

https://www.reddit.com/posts/2025/january/global/

Reddit reReddit: Top posts of 2025

https://www.reddit.com/posts/2025/global/

Reddit Rules

https://www.redditinc.com/policies/content-policy

Privacy Policy

https://www.reddit.com/policies/privacy-policy

User Agreement

https://www.redditinc.com/policies/user-agreement

Your Privacy Choices

https://support.reddithelp.com/hc/articles/43980704794004

Accessibility

https://support.reddithelp.com/hc/sections/38303584022676-Accessibility

Reddit, Inc. © 2026. All rights reserved.

https://redditinc.com/

Expand Navigation

Expand Navigation

Collapse Navigation

Collapse Navigation

0cAFcWeA5PlODYoXxotvMCjiyAqVxnyhkgKs4vCWCAzA9YQX-TegCp35cuW49RUJwh59\_UVgK6XSXEX4m8iSqVY8h70ey93E1fB2MUc7Fph4aL\_o2r0IoBZsWPG9BsAoerv3xKC4\_3uX\_ho7qOn9FDgGj5hIDf3ZkyosWnM2KLNk3xG96PUpmVGTBSM\_fgzw6ArpvhHLtM9q04IKQ\_eNnbvpYYcc9G-xUXLp5L0Yg-iGb3BTiPEismepPLf-bExLLdncezVZBENeEKdJHVXLIrBq5C9RbLPE0nm5j4uVZajR1o2DuZrIROCrigjEGqzSs0ajQN7TuANPolzLecxWeTN8pNiN-Psso0e9ESZW4oAmeZ6FLPx2QyVNsE01UUiEAHy\_T4vj0vv-AyUIhNN2vqm88eyTkh2NyAwBD0rdJGwbgYGdpkcjimpEAYpWTCVvoUYUNFq2Oy4B9n1dRhQFHybv63QSXn6pfPqDsNoVHPsxuqzz8J5cDcMhuZPZTBimlOmRj5XZoevF9mJDUmXiTks2kALWYw\_aSy1P7Z-udWrpmLlHKlZZmYT2cECHkw-PF0hC4MVYrDs7X5tSWch1HQyZ4AbqxrZ9jwWNaxRO82De5lC6\_j1rTuissYms3rl1ypl6p1QpdKukUO3AlxGHBsgSz80IQ1zls9aOPAa9oTph6sYuk6VMME4oGRPGP0BQ8DF\_-zUo30xrE1LGKDJVZxQVS06TKLLv1tOsOEcnnTS-4VFK6S17Msn9zv83aLuZ4VZMIBZ54L-jTPekiOi1gMlyHqMZ6XCMTAN9z\_1O4KOVBR4zgZpY\_iVZkWDunpNdwx2vp4UVn-uPf-JgW8hBJDiBbJlU9hzlD9SERisZKqHWj0s3f1QKkwV\_gVv-PTIG353qMp7Rf2uuWt1D-Uf5tSlhtx1Ud-wcHNUYKKQDQgD2LeO0nTXo1GDr0Muu6iN-cU7r5ZLDAksxap0DXsXNJSNZu\_f7604pUQ7l-YFOW-mnlmZd3EeoILVTDIimEI1liJFGQ56NjcdSCPAVbN9vfzifvLAxOPOKWcNPb4h5U8kLTQs9tOrP\_HAwUq-QMFOhGuR8gRh-gjcwzcPGWIzqTrz30lStOBUDefRM6JcBIypgcuNPZJsfnyqw16eXGFrWrBYDeCuUcEUjpXFPsUEZvGWYA8P4mqU5xKClY4bFTZ3u-I\_qwUoaURzoDtifCFbTx5N7PEBpjGChgJaSCgx8puzCgA4FE30LrMuwJj-\_dnmHxziflk3oCh-WVN4d8JF8rM2ulVtEuep2yYlIt0RZgp6lrkWwpfh0du510h-DxTTUOtfaOFruGzhnfi0J5uC8ScRoqRvqR0liE1RjNzwqrzJvHRWPU55eqrt8VGh558mDCVachgS-xoMNflXElSX2l8k5eqh113kc2vpftjfuXrUGMB6sdKFgAq2IZ-NwRnldfr-UrP2GQpia1YpnZ7j199NAFTto43B3vOeaEfAJkYyUoTGi4H7AzeaZbEupGrWk5Ec7ftXPbVgih2zalgMU-uVJtaATFlq3T7vYiql0DDUZDMrmV\_WF0mdO6WvQD0xlaWymFa8BUeeuSi5Ofqo8OFEW0\_jVG1XqB19j4naOphjLaxdd6np57U8I98WzHhgnA3lfvuQfi9Hmox\_D0PoPwqtB-ahjvXc\_2pBcHtchq0qtjzTq8wTxSmIoGyzRZ1BWIX8kOlz7BCsIPKcKroUWEuCCHBV8ZaLN9DBLUTfou3xxGcVaX5avNuadXFCJ0KBoSg0UpM5nntechlcgfw8xy5O45bpKMmC5oRlMam4CPd64K7tehq5vSmtEeWVYEnYD1SFc3OGzmXphQ3SD-u0NXKM0cfZU3Yu5BgQjki92mi7CrckDqbkdQsUMk6ACWk2OT2HuRHw\_xt-OhKhmLPiLAM7-5Dzh5clMeZ\_2Qq92yV\_ddom1uO6CH-7eFbaJ87qhNMgwwbqSzvr\_phGD5qIOymhvE9mkLj5xFbGEXFsBXBrsCfSNtbjKPYyLUyraTzI62fMiH55LC1I27ZJeBrdlrDIqwi8T9A79k0E22CAX2mnAHcDUSj59\_ZUH7cNTkd5cWvT4F7ieyNLhEW4fYmUqBfQ4SvDiOj53NR6Ayt8oXO2osWfSWRHcdgXHgMcKWEi6YF8pl1IxR4gEHv-PRsxsLTYHanYljKVjgu

