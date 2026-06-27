---
sourceFile: "If you can't break your AI agent, do you actually control it? : r/aiagents - Reddit"
exportedBy: "Kortex"
exportDate: "2026-06-26T04:27:51.380Z"
---

# If you can't break your AI agent, do you actually control it? : r/aiagents - Reddit

b0cf5813-afe1-4375-b0bb-ee683bb24b62

If you can't break your AI agent, do you actually control it? : r/aiagents - Reddit

74b33763-3531-47db-98ca-517e544f7246

https://www.reddit.com/r/aiagents/comments/1s69fm8/if\_you\_cant\_break\_your\_ai\_agent\_do\_you\_actually/

If you can't break your AI agent, do you actually control it? : r/aiagents

Skip to main content

https://www.reddit.com/r/aiagents/comments/1s69fm8/if\_you\_cant\_break\_your\_ai\_agent\_do\_you\_actually/#main-content

If you can't break your AI agent, do you actually control it? : r/aiagents

Open navigation

https://www.reddit.com/

Go to Reddit Home

https://www.reddit.com/answers/

Find anything

https://www.reddit.com/register/

Sign up for Reddit

https://www.reddit.com/login/

Log in to Reddit

Expand user menu

Open settings menu

Skip to Sign up

https://www.reddit.com/r/aiagents/comments/1s69fm8/if\_you\_cant\_break\_your\_ai\_agent\_do\_you\_actually/#left-sidebar-container

Skip to Right Sidebar

https://www.reddit.com/r/aiagents/comments/1s69fm8/if\_you\_cant\_break\_your\_ai\_agent\_do\_you\_actually/#right-sidebar-container

Go to aiagents

https://www.reddit.com/r/aiagents/

https://www.reddit.com/r/aiagents/

Mediocre\_Cod\_7374

https://www.reddit.com/user/Mediocre\_Cod\_7374/

Locked post

Stickied post

Archived post

If you can't break your AI agent, do you actually control it?

https://www.reddit.com/r/aiagents/?f=flair\_name%3A%22Discussion%22

Hey — I've been working on something related to AI agents in production and wanted to share a thought.

A lot of current approaches to controlling agents rely (at least partially) on natural language rules — things like:

“don't delete records”

“respect transaction limits”

“don't expose sensitive data”

The issue is that these constraints can sometimes be bypassed with fairly simple semantic changes.

#### For example:

#### But allowing:

Same outcome, different phrasing.

Or transaction limits being bypassed by splitting actions into smaller steps.

This isn't really about prompt hacking for fun — it becomes more relevant when agents are actually connected to real systems (databases, payments, APIs, etc.).

Especially in regulated environments, where you need to

system robustness, not just assume it.

#### I've been building a small open-source framework to test this kind of behavior:

generates adversarial inputs

runs them against agents

evaluates outcomes

outputs structured reports

Still early, but results have been interesting (and honestly a bit concerning).

#### Curious how others here are thinking about:

adversarial testing for agents

limitations of natural language constraints

real-world failure cases

Would love to hear thoughts or similar experiences.

#### Full write-up (if anyone's interested):

https://medium.com/@gabrielgskbr/se-você-não-consegue-quebrar-seu-agente-de-ia-você-não-o-controla-c15ccba314b8

https://medium.com/@gabrielgskbr/se-voc%C3%AA-n%C3%A3o-consegue-quebrar-seu-agente-de-ia-voc%C3%AA-n%C3%A3o-o-controla-c15ccba314b8

Upvote 2 Downvote 4 Go to comments Share

Sort by: Best

Open comment sort options

Controversial

Search Comments Expand comment search

Comments Section

https://www.reddit.com/user/geofabnz/

https://www.reddit.com/r/aiagents/comments/1s69fm8/comment/od0v8i8/

Fantastic! This has been exactly what I've been thinking about, subjectively my agent has been running very well and is good at detecting and rejecting prompt injections but I have no way of knowing if that's genuinely true or if I just haven't used the right techniques

Upvote 1 Downvote Reply Award Share

Mediocre\_Cod\_7374

https://www.reddit.com/user/Mediocre\_Cod\_7374/

https://www.reddit.com/r/aiagents/comments/1s69fm8/comment/od1074q/

Exactly! that's the hard part.

a system can

robust just because it handles obvious cases well, but subtle variations are where things usually break.

that's exactly why I built this to make that kind of testing more systematic.

If you're interested, feel free to try it out and let me know what you find 👀

pip install antz-audit

Upvote 1 Downvote Reply Award Share

More replies

https://www.reddit.com/r/aiagents/comments/1s69fm8/comment/od0v8i8/?force-legacy-sct=1

Boring\_Animator3295

https://www.reddit.com/user/Boring\_Animator3295/

https://www.reddit.com/r/aiagents/comments/1s69fm8/comment/od1fl89/

Start by separating language checks from real controls. I've had better luck when the model can talk all it wants, but actions only fire through a strict gate that does static checks and policy checks. Think of the model as a planner and the gate as the doer. The gate doesn't trust text. It only trusts structured intents and schemas with typed fields, allowed values, and per capability quotas

A few things that worked for me in prod

per tool allowlists with strong schemas. reject on unknown fields. version your schema and log diffs

transactional guards. idempotency keys. dry run mode by default. flip to live only when a policy passes and a human or policy engine signs off

budget and rate limits by session and by user. plus a watchdog that halts the run on pattern matches like split transactions or repeated rephrase attempts

Now on the adversarial testing and the natural language constraint stuff. I treat it like unit tests for tools. Generate fuzzed payloads. Try synonyms. Try unicode noise. Try step splitting. Then verify outcomes at the tool layer, not the prompt. Also handy. simulate with a fake database and fake payments before touching real systems. Red teams love this because you can replay attacks and compare logs. Add auto rollbacks and alerts when drift shows up in the reports

By the way I'm building chatbase. it's a customer service agent platform that runs agents with real data and tool actions, and we've been baking in policy gates and reporting to catch these failure modes early. if you want to see how we wire the action layer and the audit trail, happy to share more or set up a quick walk through at

https://www.chatbase.co

https://www.chatbase.co/

If you post your framework repo, I can toss a few test cases I use in reviews and you can cherry pick what helps

Upvote 1 Downvote Reply Award Share

Mediocre\_Cod\_7374

https://www.reddit.com/user/Mediocre\_Cod\_7374/

https://www.reddit.com/r/aiagents/comments/1s69fm8/comment/od1j6h0/

thanks, great points!

i'm really fully agree LLM as planner + strict deterministic gate is the way to go.

my framework for adversarial testing of AI constitutions is already open-source:

https://github.com/gabbsx7/adversarial-constitution

https://github.com/gabbsx7/adversarial-constitution

it generates attacks (semantic bypass, split transactions, etc.), runs them, judges outcomes and creates audit reports.

would love to get your test cases and feedback. Feel free to drop them as issues.

and, how do you handle subtle goal reframing by the planner that passes schema checks but still violates high-level policy?

Upvote 1 Downvote Reply Award Share

More replies

https://www.reddit.com/r/aiagents/comments/1s69fm8/comment/od1fl89/?force-legacy-sct=1

People also ask about section

People also ask about

Best programming languages for AI development

https://www.reddit.com/answers/82b40a27-8dbb-4230-a452-bf638cbdcbf2/?q=Best+programming+languages+for+AI+development&source=PDP

Top AI tools for enhancing productivity

https://www.reddit.com/answers/1ac0bfea-76d8-4e20-9d1b-1764bc3bd292/?q=Top+AI+tools+for+enhancing+productivity&source=PDP

Ethical considerations in AI deployment

https://www.reddit.com/answers/1b394b0b-0422-45df-b6d3-f1a965589328/?q=Ethical+considerations+in+AI+deployment&source=PDP

Future trends in AI and machine learning

https://www.reddit.com/answers/b572b7a9-2240-4dd2-8447-586b692651b2/?q=Future+trends+in+AI+and+machine+learning&source=PDP

How AI agents can improve customer service

https://www.reddit.com/answers/21ab974c-d5fe-45a1-a095-31b1d962c8f6/?q=How+AI+agents+can+improve+customer+service&source=PDP

More posts you may like

Related posts

AI agents: 90% automation, 10% 'why is this broken again?

https://www.reddit.com/r/IndiaTech/comments/1tarm9t/ai\_agents\_90\_automation\_10\_why\_is\_this\_broken/

r/IndiaTech

https://www.reddit.com/r/IndiaTech/

- 1mo ago \[

AI agents: 90% automation, 10% 'why is this broken again?

\](https://www.reddit.com/r/IndiaTech/comments/1tarm9t/ai\_agents\_90\_automation\_10\_why\_is\_this\_broken/)

451 upvotes · 9 comments

have your ai has been acting like this?

https://www.reddit.com/r/GoogleAIGoneWild/comments/1sioui0/have\_your\_ai\_has\_been\_acting\_like\_this/

r/GoogleAIGoneWild

https://www.reddit.com/r/GoogleAIGoneWild/

- 2mo ago \[

have your ai has been acting like this?

\](https://www.reddit.com/r/GoogleAIGoneWild/comments/1sioui0/have\_your\_ai\_has\_been\_acting\_like\_this/)

81 upvotes · 12 comments

Why is everyone lying about AI agents

https://www.reddit.com/r/aiagents/comments/1rdn5hq/why\_is\_everyone\_lying\_about\_ai\_agents/

https://www.reddit.com/r/aiagents/

- 4mo ago \[

Why is everyone lying about AI agents

\](https://www.reddit.com/r/aiagents/comments/1rdn5hq/why\_is\_everyone\_lying\_about\_ai\_agents/) 408 upvotes · 274 comments

AI AGENTS today are far more DANGEROUS that you think

https://www.reddit.com/r/AIDangers/comments/1rmdrtl/ai\_agents\_today\_are\_far\_more\_dangerous\_that\_you/

r/AIDangers

https://www.reddit.com/r/AIDangers/

- 4mo ago \[

AI AGENTS today are far more DANGEROUS that you think

\](https://www.reddit.com/r/AIDangers/comments/1rmdrtl/ai\_agents\_today\_are\_far\_more\_dangerous\_that\_you/) 60 upvotes · 14 comments

Why is everyone lying about AI agents

https://www.reddit.com/r/AIDigitalStack/comments/1ss26f1/why\_is\_everyone\_lying\_about\_ai\_agents/

r/AIDigitalStack

https://www.reddit.com/r/AIDigitalStack/

- 2mo ago \[

Why is everyone lying about AI agents

\](https://www.reddit.com/r/AIDigitalStack/comments/1ss26f1/why\_is\_everyone\_lying\_about\_ai\_agents/) 64 upvotes · 41 comments

The greatest AI skill you can learn is Reverse Prompting

https://www.reddit.com/r/aiagents/comments/1rmvrjl/the\_greatest\_ai\_skill\_you\_can\_learn\_is\_reverse/

https://www.reddit.com/r/aiagents/

- 4mo ago \[

The greatest AI skill you can learn is Reverse Prompting

\](https://www.reddit.com/r/aiagents/comments/1rmvrjl/the\_greatest\_ai\_skill\_you\_can\_learn\_is\_reverse/) 337 upvotes · 33 comments

Using agent skills made me realize how much time I was wasting repeating context to AI

https://www.reddit.com/r/ContextEngineering/comments/1rnjssi/using\_agent\_skills\_made\_me\_realize\_how\_much\_time/

r/ContextEngineering

https://www.reddit.com/r/ContextEngineering/

- 4mo ago \[

Using agent skills made me realize how much time I was wasting repeating context to AI

\](https://www.reddit.com/r/ContextEngineering/comments/1rnjssi/using\_agent\_skills\_made\_me\_realize\_how\_much\_time/) 26 upvotes · 6 comments

I'm done with 'If-This-Then-That.' Are AI Agents actually ready to take over?

https://www.reddit.com/r/buildinpublic/comments/1rgw678/im\_done\_with\_ifthisthenthat\_are\_ai\_agents/

r/buildinpublic

https://www.reddit.com/r/buildinpublic/

- 4mo ago \[

I'm done with 'If-This-Then-That.' Are AI Agents actually ready to take over?

\](https://www.reddit.com/r/buildinpublic/comments/1rgw678/im\_done\_with\_ifthisthenthat\_are\_ai\_agents/) 1 upvote · 4 comments

Am I missing the point of AI agents?

https://www.reddit.com/r/POP\_Agents/comments/1tlwcca/am\_i\_missing\_the\_point\_of\_ai\_agents/

r/POP\_Agents

https://www.reddit.com/r/POP\_Agents/

- 1mo ago \[

Am I missing the point of AI agents?

\](https://www.reddit.com/r/POP\_Agents/comments/1tlwcca/am\_i\_missing\_the\_point\_of\_ai\_agents/) 29 upvotes · 24 comments

Why don't we own our own AI agents yet?

https://www.reddit.com/r/StartupNinjas/comments/1op3mdf/why\_dont\_we\_own\_our\_own\_ai\_agents\_yet/

r/StartupNinjas

https://www.reddit.com/r/StartupNinjas/

- 8mo ago \[

Why don't we own our own AI agents yet?

\](https://www.reddit.com/r/StartupNinjas/comments/1op3mdf/why\_dont\_we\_own\_our\_own\_ai\_agents\_yet/) 36 upvotes · 24 comments

My feelings about AI have shifted more than I expected

https://www.reddit.com/r/aiagents/comments/1rj4m18/my\_feelings\_about\_ai\_have\_shifted\_more\_than\_i/

https://www.reddit.com/r/aiagents/

- 4mo ago \[

My feelings about AI have shifted more than I expected

\](https://www.reddit.com/r/aiagents/comments/1rj4m18/my\_feelings\_about\_ai\_have\_shifted\_more\_than\_i/) 25 upvotes · 23 comments

How do you stop an AI agent from giving wrong answers when your help docs change weekly?

https://www.reddit.com/r/Jugl/comments/1r86fje/how\_do\_you\_stop\_an\_ai\_agent\_from\_giving\_wrong/

https://www.reddit.com/r/Jugl/

- 4mo ago \[

How do you stop an AI agent from giving wrong answers when your help docs change weekly?

\](https://www.reddit.com/r/Jugl/comments/1r86fje/how\_do\_you\_stop\_an\_ai\_agent\_from\_giving\_wrong/) 1 upvote · 2 comments

Stop building AI agents

https://www.reddit.com/r/AIforOPS/comments/1tvi9uq/stop\_building\_ai\_agents/

https://www.reddit.com/r/AIforOPS/

- 22d ago \[

Stop building AI agents

\](https://www.reddit.com/r/AIforOPS/comments/1tvi9uq/stop\_building\_ai\_agents/) 36 upvotes · 17 comments

Announcement: The AI Problem.

https://www.reddit.com/r/writingfeedback/comments/1sob9zo/announcement\_the\_ai\_problem/

r/writingfeedback

https://www.reddit.com/r/writingfeedback/

- 2mo ago \[

Announcement: The AI Problem.

\](https://www.reddit.com/r/writingfeedback/comments/1sob9zo/announcement\_the\_ai\_problem/) 267 upvotes · 131 comments

If your app “technically works” but you're scared to touch it, read this

https://www.reddit.com/r/lovablebuildershub/comments/1qkel9n/if\_your\_app\_technically\_works\_but\_youre\_scared\_to/

r/lovablebuildershub

https://www.reddit.com/r/lovablebuildershub/

- 5mo ago \[

If your app “technically works” but you're scared to touch it, read this

\](https://www.reddit.com/r/lovablebuildershub/comments/1qkel9n/if\_your\_app\_technically\_works\_but\_youre\_scared\_to/) 2 upvotes · 2 comments

I gave my AI agents email instead of better reasoning. They started fixing each other's bugs.

https://www.reddit.com/r/Agentic\_AI\_For\_Devs/comments/1tpo1sq/i\_gave\_my\_ai\_agents\_email\_instead\_of\_better/

r/Agentic\_AI\_For\_Devs

https://www.reddit.com/r/Agentic\_AI\_For\_Devs/

- 1mo ago \[

I gave my AI agents email instead of better reasoning. They started fixing each other's bugs.

\](https://www.reddit.com/r/Agentic\_AI\_For\_Devs/comments/1tpo1sq/i\_gave\_my\_ai\_agents\_email\_instead\_of\_better/) 27 upvotes · 15 comments

Are we making the same privacy mistake again with AI agents?

https://www.reddit.com/r/AIDangers/comments/1ub3583/are\_we\_making\_the\_same\_privacy\_mistake\_again\_with/

r/AIDangers

https://www.reddit.com/r/AIDangers/

Are we making the same privacy mistake again with AI agents?

\](https://www.reddit.com/r/AIDangers/comments/1ub3583/are\_we\_making\_the\_same\_privacy\_mistake\_again\_with/) 32 upvotes · 12 comments

Anyone wants to start learning agentic ai... Let's do together

https://www.reddit.com/r/aiagents/comments/1u7628w/anyone\_wants\_to\_start\_learning\_agentic\_ai\_lets\_do/

https://www.reddit.com/r/aiagents/

Anyone wants to start learning agentic ai... Let's do together

\](https://www.reddit.com/r/aiagents/comments/1u7628w/anyone\_wants\_to\_start\_learning\_agentic\_ai\_lets\_do/) 14 upvotes · 26 comments

What are you doing to break the AI?

https://www.reddit.com/r/AIRealm/comments/1qs9l3y/what\_are\_you\_doing\_to\_break\_the\_ai/

https://www.reddit.com/r/AIRealm/

- 5mo ago \[

What are you doing to break the AI?

\](https://www.reddit.com/r/AIRealm/comments/1qs9l3y/what\_are\_you\_doing\_to\_break\_the\_ai/) 11 upvotes · 21 comments

How to Actually Build an AI Agent: A Complete Step-by-Step Guide for 2026

https://www.reddit.com/r/NextGenAITool/comments/1u315jd/how\_to\_actually\_build\_an\_ai\_agent\_a\_complete/

r/NextGenAITool

https://www.reddit.com/r/NextGenAITool/

- 14d ago \[

How to Actually Build an AI Agent: A Complete Step-by-Step Guide for 2026

\](https://www.reddit.com/r/NextGenAITool/comments/1u315jd/how\_to\_actually\_build\_an\_ai\_agent\_a\_complete/) 277 upvotes · 49 comments

Vibe coding is already happening. The question is: will you control it, or will it control you?

https://www.reddit.com/r/VibeCodeDevs/comments/1rs81uv/vibe\_coding\_is\_already\_happening\_the\_question\_is/

r/VibeCodeDevs

https://www.reddit.com/r/VibeCodeDevs/

- 3mo ago \[

Vibe coding is already happening. The question is: will you control it, or will it control you?

\](https://www.reddit.com/r/VibeCodeDevs/comments/1rs81uv/vibe\_coding\_is\_already\_happening\_the\_question\_is/) 1 upvote · 11 comments

Do you trust payroll software to catch anomalies… or do you still spreadsheet it?

https://www.reddit.com/r/HRAustralia/comments/1rqxho1/do\_you\_trust\_payroll\_software\_to\_catch\_anomalies/

r/HRAustralia

https://www.reddit.com/r/HRAustralia/

- 4mo ago \[

Do you trust payroll software to catch anomalies… or do you still spreadsheet it?

\](https://www.reddit.com/r/HRAustralia/comments/1rqxho1/do\_you\_trust\_payroll\_software\_to\_catch\_anomalies/) 1 upvote

How do you check if an MCP server is “safe” before you run it?

https://www.reddit.com/r/mcp/comments/1r8ir5z/how\_do\_you\_check\_if\_an\_mcp\_server\_is\_safe\_before/

https://www.reddit.com/r/mcp/

- 4mo ago \[

How do you check if an MCP server is “safe” before you run it?

\](https://www.reddit.com/r/mcp/comments/1r8ir5z/how\_do\_you\_check\_if\_an\_mcp\_server\_is\_safe\_before/) 5 upvotes · 9 comments

Alternative to the -ai hack?

https://www.reddit.com/r/antiai/comments/1u8r692/alternative\_to\_the\_ai\_hack/

https://www.reddit.com/r/antiai/

Alternative to the -ai hack?

\](https://www.reddit.com/r/antiai/comments/1u8r692/alternative\_to\_the\_ai\_hack/) 9 upvotes · 9 comments

Why your AI agents are hallucinating (and why a bigger system prompt won't fix it)

https://www.reddit.com/r/SaaS/comments/1qpw9g7/why\_your\_ai\_agents\_are\_hallucinating\_and\_why\_a/

https://www.reddit.com/r/SaaS/

- 5mo ago \[

Why your AI agents are hallucinating (and why a bigger system prompt won't fix it)

\](https://www.reddit.com/r/SaaS/comments/1qpw9g7/why\_your\_ai\_agents\_are\_hallucinating\_and\_why\_a/) 4 upvotes · 5 comments

View Post in

https://www.reddit.com/r/aiagents/comments/1s69fm8/if\_you\_cant\_break\_your\_ai\_agent\_do\_you\_actually/?tl=fr

Português (Brasil)

https://www.reddit.com/r/aiagents/comments/1s69fm8/if\_you\_cant\_break\_your\_ai\_agent\_do\_you\_actually/?tl=pt-br

https://www.reddit.com/r/aiagents/comments/1s69fm8/if\_you\_cant\_break\_your\_ai\_agent\_do\_you\_actually/?tl=hi

See more See fewer

https://www.reddit.com/r/aiagents/comments/1s69fm8/if\_you\_cant\_break\_your\_ai\_agent\_do\_you\_actually/?tl=th

https://www.reddit.com/r/aiagents/comments/1s69fm8/if\_you\_cant\_break\_your\_ai\_agent\_do\_you\_actually/?tl=de

https://www.reddit.com/r/aiagents/comments/1s69fm8/if\_you\_cant\_break\_your\_ai\_agent\_do\_you\_actually/?tl=fil

https://www.reddit.com/r/aiagents/comments/1s69fm8/if\_you\_cant\_break\_your\_ai\_agent\_do\_you\_actually/?tl=it

Español (Latinoamérica)

https://www.reddit.com/r/aiagents/comments/1s69fm8/if\_you\_cant\_break\_your\_ai\_agent\_do\_you\_actually/?tl=es-419

Community Info Section

https://www.reddit.com/r/aiagents/

Live Apex AI Agents talk Monday Nov 20th - Evolution of the Devoxx talk, "The Awareness Layer". Zoom so sign up in advance, will pull when capped.

The Awareness Layer

https://humanrace.ai/aiagents

AI Agents may be one of the primary conceptual frameworks for humanity's deployment of applied AI. Tools, commentary and talent

Anyone can view, post, and comment to this community

https://www.reddit.com/?feed=home

https://www.reddit.com/r/popular/

https://www.reddit.com/news/

https://www.reddit.com/explore/

Best of Reddit

https://www.reddit.com/posts/2026/global/

Best of Reddit in Portuguese

https://www.reddit.com/posts/2026/tl-pt-BR/

Best of Reddit in German

https://www.reddit.com/posts/2026/tl-de/

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

Join the most real place on the internet

Continue with Apple

 Sign in with Apple

Continue with Phone Number

https://www.reddit.com/login/

Continue with Email

https://www.reddit.com/register/

By continuing, you agree to our

User Agreement

https://www.redditinc.com/policies/user-agreement

and acknowledge that you understand the

Privacy Policy

https://www.redditinc.com/policies/privacy-policy

0cAFcWeA5yHAA\_oM\_EDpnJ2wWf87qf2d5z2X3s4Do-5Z0\_w9tpDyivcmApIvmGXFT1a0OSctfqr2TgvwJGgXVm3TeNcD5-BsCxqRSD227zq8tf8zQDhVxTzpJEL2EgZIAEIqMWW3g09nL7jBnoc7KrQ6VIrwTkFs7O3dsVOvwh8wuoIZPEoLQ6CLB7ew2Cp34Y7Xw7mUm56Yf2zREAz07IDahCYvtEigiOmOrPRbdTShtiBMbfEuomgQ4Pu-Moo-BR-jvfEITImjNDNb06Hh5hWgMUuEsja7oWRpMylu7eiyRuJRtTKTiG8urSfLPKWucbpzs1X4J7rYElnz3W\_66e8X\_-f0Zi9DihPP5FsIr4McOikSG4Zac2Ne3FayVkrwxuRDGu7Xet7GmN87Bsq3X4YEHZ1WrS6lR-DBlrfuk3pD9hWj-TdBqiI4-8kaACytIk4eo66On5p\_ymTacJZ7fm\_POYFV1XDyt6GDrexlkLWs7ypUNzuob--StQ9mph9gQXv1HCZ9fIEIVKmiM5YmHDwg9ecD36-mKDMpBokECLLT49gBm2NE6VdgjD3vyi3pGTeVtguNQl5QgCiF38ICIIzgeEssZSMfkfoxeMGos4BoyGbV7rF2cvhqJRiOv4WoRFFSZg6ODR2tBTziDJpK4kGRrKbtwdBfSz0eGpGT3DCAjYy7JkVtJWoyjeQNivjBvUfp4cHlOXJmEY-vDJv4ve\_sj1oXJchHdEgEjdc1E1L5dMdR3Nmba2c1CNx0\_AW2d0eIricuJQhAfoU1kKNcXO-0DxwmuTJQNPkyuiZSVSPRDSOVZEUIkcwz7e-PXKD3kLwiYP2KCeFFj\_LtEzqc1UgTBf47ikC-N\_tp5ohbgi\_eJ5x\_BfX7Y0qX9RhD7\_wPwQH1L9d9196V\_B3eIic6mvryi945-um3\_cLnZH9-a-lHk8qsj6PyRmov5IgrQXrKQlji4d-mxhVJbjeVzPX46nVpHKWdYLpLPGBD4MQ1ZPHKX5e0PAUdS8XMWeMLMd6r9FVn4dm0L8J4YM-gBgi-43WiSqKDPcxzGDI5J4lgJ3epUqK0miUmjtSSy2gqOppHjQnXbnBNirTH3eBMqMSpIwjw16pk-Yj1yVHU\_fVchu9YD86zNW74JlGymLrMPpnSo3Jpc9bLdC\_AvLl2GOpMuF1IMe5FdEooWEWQSY7yqK2AOKgq\_NtqDv5r6ryeLpEWdlA9dcbuc9KVc6YVYmPefdKzaqK6oADYv80QFpuKifS-fix9cu8oX4z2um0XgXp6DnLT4tBr4voc7ei5ysNgDs41-anBt8xHoWde6DqKa\_\_D1Yt3HGkySZfz18I-qXK2OPsMAdJim8jzP3N\_JOQHQs23ad8lbjaAxKzOku8Tl0TAwiffGyw68bYY3VRGTRmUK\_qfWxEH5FUHer3CKRjX0tEQGUx4Ij9FuHcG4Ovxl-MeZOznsnZQJtCZg6UMWvLeZyIErZWwRb0uG8r0zCDYftNDBZevWbGo8I2jU0PNJyRqxxMxTPEHomKQVdiV8MPWqgYSA2CmKNFBL66ZDT6GQ\_IihyoSjPPo3NIZVl4VZlnhMyYMKo9tDsSeo5cJ2Aug5zkYnewv-RLQPI5KIq\_L2sf6ZHi88W3DHui-pGgOBEi0KKQXIMM-Sr9ULWXt6IVPDEU01NYqNfyv1TByWmj7ggsOEAhS6za7Ax5OmEz2FOfjXmmvlOcdlqG4dauugYg7bSs0VIOaxlxPPK-AIft2fT0N-nKN8F9xYTB6kd8JJxSKC8fFQ4ea9kOMH4Y3RzFTh8yneWAyijh6TT43VaUXKusyRZpJtcjdpblxlCmVi2YhTpzgPNZbM84GL0K5me2HD8R1x\_iFXSdnaexq3FKOQW7tN5UqfO-CP80ehzGfDdzZvlNCioVit-6xdgFvB3X3J-Zg21yx5PHs59iiju0tNrkJi9wyTR5w9cvJ5Gu-cqdqXOcgtK4hFHFOC862eOAqc8TVIB75wT0MnwNDnpYxJj-ckr2-mzolspbIYxv7eCpUoEiyMxDUt15hzOzm7Io5CwzBhSzfhNbSqR88yWT8iZtJUqj6dMGYH05N0MbA79Jin4LiIF1A9VSQX81un8IwawAjmH3GUd3xz1sAA2IkRY1tEEw0ARVrNGPa4OxyvqC8BPR4Pk-vT668i34h0exbs\_mhFRrunh-v\_CAckihL0BEhWTAsygmhNNNA

