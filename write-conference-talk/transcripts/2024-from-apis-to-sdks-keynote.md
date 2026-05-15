---
title: 'From APIs to SDKs — elevating your Developer Experience with automated SDK generation'
conference: 'APIWorld 2023 / Nordic APIs 2024 (deck source)'
year: 2024
source: 'Apple Keynote deck'
source_file: '~/Desktop/from apis to sdks.key'
deck_mtime: '2024-03-12'
paired_transcripts:
  - 2023-api-world-kKOu_4TYHII.md
  - 2024-nordicapis-austin-2-DfK5a8b79K0.md
pairing_note: 'Source deck for the APIWorld 2023 and Nordic APIs Austin 2024 SDK talks. Voice-vote opener pattern (''API folks — you are wrong'') and the math-it-out scaling argument (10 microservices × 10 teams = 100 wrappers) are the structural backbone.'
---

_Source: Apple Keynote deck. No video / no timestamps. Structured by slide number. Each slide section captures the on-slide text (title + body) and Jim's presenter notes — the notes are the spoken narration._

## Slide 1 — From APIs to SDKs   Elevating your Developer Experience with automated SDK generation

**Title (verbatim):**
From APIs to SDKs
 
Elevating your Developer Experience with automated SDK generation

**Body:**
Jim Bennett

Principal developer advocate
liblab

**Notes:**
VS Code
Llama store demos in container
Llama store DB reset
Llama store running
Docs in a browser
Login to liblab
## Slide 2

**Body:**
Who creates APIs?

**Notes:**
Question for the audience - who works for a SaaS company that sells and API based product? Who creates APIs that their paying customers use?
Who creates APIs for internal use, such as building out microservices?
## Slide 3

**Body:**
Who consumes APIs?

**Notes:**
Another question for the audience - who works with APIs from third parties or internal teams?
## Slide 4

**Body:**
APIs vs SDKs
Vote now!

**Notes:**
Final question for now - would you rather consume an API directly making REST calls, or use an SDK for the language you use?
API folks - you are wrong.
## Slide 5 — Hi, I’m Jim

**Body:**
He/Him

Principal developer advocate
liblab

@jimbobbennett
linktr.ee/jimbobbennett

**Notes:**
I’m Jim
Describe
You can find me on social at JimBobBennett - connect and say hello
## Slide 6

**Body:**
Let’s look at the
developer experience with APIs

**Notes:**
Let’s take a look at the developer experience with APIs and see some of the pitfalls
## Slide 7

**Body:**
Demo time!

**Notes:**
Show Llama store liblab docs
Compare llama store REST - create user, api token, list llamas
## Slide 8

**Body:**
Too many magic strings

**Notes:**
To me there are too many ways to make mistakes.
For example, all the JSON fields are magic strings - strings you just have to know from the docs
Knowing the field is email instead of user name for example.
I’m a fan of type safety, and this just doesn’t give me that.
## Slide 9

**Body:**
Too easy to make silly mistakes

**Notes:**
It’s too easy to make silly mistakes - like not setting the header on every call.
I want a compiler or linter to tell me when I’ve done something dumb, not find out when my app crashes at run time
## Slide 10

**Body:**
How do devs normally fix this?

**Notes:**
How is this normally fixed? Add a layer of abstraction of course
This can be objects that replicate the JSON objects, or wrappers around API calls with retry logic.
And the best later of abstraction?
## Slide 11

**Body:**
SDKs

**Notes:**
An SDK! A complete wrapper for your entire API with objects to represent the requests and responses, and services to call all your endpoints, managing everything for you from auth to retries and more.[
To improve developer experience, the answer is to create an SDK. Build SDKs for all your microservices.
## Slide 12

**Body:**
That’s great Jim but
I have questions…

**Notes:**
This is great - much nicer developer experience.
But - there are 2 obvious questions…
## Slide 13

**Body:**
Should I really bother?

**Notes:**
The first obvious question - should I really bother?
This is a great question. From the example earlier developers could just look at the API docs and keep trying right?
The answer is yes! Your users want a better developer experience, and an SDK adds this.
It also doesn’t take anything away from those users who want a REST API.
Gives the ability for experts to control the wrapper.
Remember - your users care about what they want, not the amount of effort it takes you.
## Slide 14

**Body:**
es! Your customers want a
better developer experience

**Notes:**
Recent survey - the majority of developers want an SDK over an API. So you need both.
Yes - there is a a type on that tweet, should be re tweet for reach, not trash!
## Slide 15

**Body:**
We live in a time of better DevEx

**Notes:**
Currently we live in a time where better developer experience is a huge focus. There are new tools on an almost daily basis that focus on driving productivity. Frameworks, IDEs, AI powered coding, it’s all helping us to be more productive.
A great developer experience allows you to focus less on boilerplate, and more on solving the really hard problems such as proving to the world that pineapple is perfectly acceptable on pizza.
Your customers expect a better developer experience, and you should give it to them so they don’t go anywhere else.
This is also true for internal APIs. Anyone here asked another team for an API spec and got sent an out of date word document by a BA? Yup, welcome to enterprise software.
## Slide 16

**Body:**
SDKs mean boilerplate code is provided

**Notes:**
SDKs mean boilerplate code is provided, and every user doesn’t need to develop it.
## Slide 17

**Body:**
Authentication
Retry strategies
Object mapping
URL management
…

**Notes:**
Every time you use a REST API you need to build out auth, retry strategies, JSON to object mapping, URL management and more!
## Slide 18

**Body:**
Doesn’t it take ages to build
an SDK?

**Notes:**
The second obvious question - doesn’t it take ages to build an SDK?
Thinking of all the different programming languages you need to support.
It can, if you do it all manually, especially updating it when the API changes.
But why would you do it manually?
## Slide 19

**Body:**
Let’s do some math…

**Notes:**
Lets do some math to see how hard it is to do manually
## Slide 20

**Body:**
Imagine you have 10 microservices
used by 10 teams

**Notes:**
Imagine you have 10 microservices, with 10 teams using them. Users, identity, orders, accounts, things like that that everyone uses
## Slide 21

**Body:**
5 teams use TypeScript
3 teams use Java
2 teams use Go

**Notes:**
These 10 teams are self forming teams using the language they prefer
So 5 are using TypeScript
3 are using Java
2 use go
## Slide 22

**Body:**
If there are no SDKs then:

Each team will probably build a wrapper over every microservice

**Notes:**
If there are no SDKs then most likely each team will build some kind of a wrapper or layer of abstraction over the REST API to manage auth, retry strategies, mapping etc.
Based of my experience in large companies, teams don’t often talk to each other and share code
Especially in this situation as who will own the code? If one team needs something another doesn’t then who builds it?
## Slide 23

**Body:**
10 teams, 10 microservices
= 100 wrappers to build and maintain

**Notes:**
This is a lot of code - most of it repeated.
This eats a lot of developer time which could be better spent on other things
## Slide 24

**Body:**
Now scale this up to 70 microservices…

**Notes:**
Now scale this up to 70 microservices. That’s a lot of code to be built, maintained and supported.
## Slide 25

**Body:**
Or add another language…

**Notes:**
Or add another team using another programming language…
## Slide 26

**Body:**
I’m lazy, I automate all the things!

**Notes:**
Now I’m lazy. Anyone else lazy? The special kind of developer lazy who spends a week automating a job that would only take an hour if it was done manually?
## Slide 27

**Body:**
Introducing liblab

**Notes:**
In my case, I use liblab to automate my SDK generation.
Liblab is a tool that creates developer friendly SDKs for your APIs. It’s not just any old ‘SDK generator’ that produces poor quality SDKs, we focus on developer experience so your SDKs are the best they can be.
Let’s see it in action
## Slide 28

**Body:**
Demo time!

**Notes:**
Show using liblab to generate an SDK
Show the OpenAPI spec
Show the config file
Generate the SDK from the llama store
Show the SDK that is generated
Show it in use
## Slide 29

**Body:**
SDKs generated in record time!

**Notes:**
SDKs can be generated in record time
This is a demo, so it is fast as I’ve preconfigured everything, but it really doesn’t take that long to set up.
Create your config file, configure things like auth and some language options, generate your SDK, evaluate, tweak the configuration, repeat until done.
Everything is in a configuration file, so no need to add annotations to your spec - which is great if your spec is auto generated, or if you want an SDK for an API from a third party, such as another team in your company.
This is not just for SDKs for your customers or users, but you can use it as a developer when consuming APIs as well.
## Slide 30

**Body:**
Demo time!

**Notes:**
Demo using the SDK with the example file
## Slide 31

**Body:**
Once generated, publish the SDK

**Notes:**
Once your SDK is generated, you can publish it with a single command. This will raise a pull request against your repo with the SDK code in it. One review and your code is done, and you can publish to npm, PyPi, internal package managers, wherever.
## Slide 32

**Body:**
I’m lazy, I automate all the things!

**Notes:**
Once again, I am lazy so I automate all the things. In this case I can automate the SDK generation using a GitHub action. You put the config file in a repo, and then trigger a build and a publish when the spec changes.
It’ll then raise a PR with just the changes for you to review and approve.
## Slide 33

**Body:**
Demo time!

**Notes:**
Show action
Show SDK
## Slide 34

**Body:**
Let’s do some math…

**Notes:**
Some more math - this time using SDKs
## Slide 35

**Body:**
10 microservices
5 teams use TypeScript
3 teams use Java
2 teams use Go

**Notes:**
Same 10 microservices and 10 teams
## Slide 36

**Body:**
10 SDKs to generate

**Notes:**
Now just 10 SDKs to generate. all shared by client teams. These can be created once by the microservices teams, or a client team. Every micro service update means a new API spec, and an autogenerated SDK
## Slide 37

**Body:**
Scaling up is less effort

**Notes:**
70 microservices or adding another language? Less effort! New language is another entry in a config file and maybe some tweaks.
Centralized SDK management
## Slide 38

**Body:**
Maximum developer experience, minimum developer effort.

**Notes:**
Using an SDK generator allows you to make it easier to consume your microservices, with a consistent experience for everyone
## Slide 39

**Body:**
Don’t just publish APIs
Publish amazing SDKs

**Notes:**
My ask to you - don’t just publish microservices, publish amazing SDKs that your users will love, and autogenerate them to allow you to deliver in record time and focus on the real problems.
## Slide 40

**Body:**
Don’t just publish microservices
Publish amazing SDKs

**Notes:**
My ask to you - don’t just publish microservices, publish amazing SDKs that your users will love, and autogenerate them to allow you to deliver in record time and focus on the real problems.
## Slide 41

**Body:**
liblab.com/join
