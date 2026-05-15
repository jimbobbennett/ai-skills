---
title: 'Evaluation-Driven Development of AI apps'
conference: 'unknown (deck source only)'
year: 2026
source: 'Apple Keynote deck'
source_file: '~/Desktop/evaluation-driven-development.key'
deck_mtime: '2026-03-06'
paired_transcripts:
  - 2025-ai-engineer-worlds-fair-xJXm4Wcw4m8.md
pairing_note: 'Same thesis as the AI Engineer 2025 talk (''Taming Rogue AI Agents'') — TDD → EDD, AI-as-judge, demo of fixed code via evals. Deck has more material (41 slides vs 16m talk). Likely a longer-slot evolution of the same talk; could be the canonical source the spoken AI Engineer version was cut down from.'
---

_Source: Apple Keynote deck. No video / no timestamps. Structured by slide number. Each slide section captures the on-slide text (title + body) and Jim's presenter notes — the notes are the spoken narration._

## Slide 1 — Evaluation-Driven Development of AI apps

**Title (verbatim):**
Evaluation-Driven
Development of AI apps

**Body:**
Jim Bennett

Principal Developer Experience Engineer



@jimbobbennett
linktr.ee/jimbobbennett
## Slide 2 — Who trusts AI?

**Body:**
Is it time for malicious compliance?

**Notes:**
Let’s start by being really negative about AI
## Slide 3 — Your AI project will probably fail

**Notes:**
Who is working on an AI project?
RAND corporation study claims more than 80% of AI projects will fail.
95% according to MIT
Software projects do fail, 50% by some measures, but this is a lot higher.
So why?
Reasons for failure - promotion driven development, lack of direction, lack of understanding of what the app should do, wrong technology
## Slide 4 — 🌶️ Spicy take time…

**Body:**
Is it time for malicious compliance?
## Slide 5 — AI is like an enthusiastic 5 year old with a stack of out-of-date encyclopedias
## Slide 6 — AI is like an enthusiastic 5 year old with a stack of out-of-date encyclopedias
## Slide 7 — AI is like an enthusiastic 5 year old with a stack of out-of-date encyclopedias
## Slide 8 — AI is like an enthusiastic 5 year old with a stack of out-of-date encyclopedias
## Slide 9 — AI is like an enthusiastic 5 year old with a stack of out-of-date encyclopedias

**Notes:**
Confident, want’s to help, can be utterly wrong. Literally all the AI chat tools have a disclaimer saying it can make mistakes.
## Slide 10 — AI is not intelligent, it’s just confident, sycophantic, autocomplete
## Slide 11 — It’s also completely non-deterministic.  It’ll work one day, and not work of give different results the next.

**Title (verbatim):**
It’s also completely non-deterministic.

It’ll work one day, and not work of give different results the next.

**Notes:**
Especially where inputs are natural language. You almost have to ‘argue’ with it sometimes to get it to work. The mansplaining picture - it first refused as the image would reinforce a negative stereotype. I clarified it would be used in a presentation to illustrate the concept, and the AI then complied.
## Slide 12 — It’s not all doom and gloom.  When it works, it’s fantastic!

**Title (verbatim):**
It’s not all doom and gloom.

When it works, it’s fantastic!

**Notes:**
AI is great at working with unstructured data, such as data from disparate systems and natural language. When it works it can understand a users intent, make decisions, gather data from disparate sources and bring it together, interact with tools without the strong contract of an API, and so on.

Not saying AI is all bad - my take is that I am an AI cynic, I’ve seen the bad side of AI so always take the view that AI is wrong till proven otherwise. For example, I don’t trust AI generated code without at least some understanding of what it should do, and having tests in place to verify.
## Slide 13 — Demo

**Notes:**
Let’s see a quick demo of AI getting things wrong
Demo HR chatbot giving random numbers for vacation days.

In a real HR system, there would be a RAG system that extracts this information and sends it to the LLM to be used in the output, but if that fails - for example the database is down, or is not set up correctly, you many not know as the HR system appears to be working!
## Slide 14 — So what do we, as developers, do to ensure our AI doesn’t suck?

**Notes:**
The problem we have as developers is that our traditional development methodologies just don’t work any more.
AI can help build a whole new class of applications, but how we develop them has to change, particularly ow we test them.

An app can be failing under the hood, but appear to work due to the LLM hallucinating. Our dummy HR chatbot gives a number of days most of the time, despite not actually having any relevant information.

There’s too much variability in both the inputs, if we have a chatbot UI, and the output from the AI if it is text. We are used to deterministic systems, and testing them deterministically. Suddenly we are building non-deterministic systems, as randomness is built into the models.

What you have just seen is a simple example of just asking an LLM. Imaging a multi-agent system with tool calls, different LLMs and so on. Add in a huge range of inputs that a user might ask and the problem space explodes.
## Slide 15 — We are used to deterministic problems

**Notes:**
As developers we are used to code that runs reliably and deterministically. We write unit and integration tests with expected input and expected outputs.

Who uses TDD? Writes tests? Tests their software? Move fast and break things? Even Facebook realized this was dumb and changed it to move fast and build things.

Test driven development, or TDD, is a standard practice for effective development teams.
## Slide 16 — Test-Driven development

**Notes:**
Test driven development makes so much sense. When you have the business problem, code structure, or bug well defined, you can start with a set of tests, then update the code to make the tests pass, then refactor knowing that the tests passing allow you to refactor without worrying that your app won’t work.

Tests also define business knowledge, domain knowledge and so on - they can define what the application should do.
This process ensures your app is tested, and that you are thinking up front what the app should do, and what the acceptance criteria is
## Slide 17 — Test Driven Development:  Arrange Act Assert

**Title (verbatim):**
Test Driven Development:

Arrange
Act
Assert

**Notes:**
Standard unit testing follows a basic pattern - you set up some inputs, you do something with them, then you check the output against a well-defined expectation.
Can be given-when-then.
How does this apply to AI when the assert is not so simple?
## Slide 18

**Body:**
How many vacation days do I get each year?
How many holiday days have I already taken?
How many PTO days do I still have left?
Can you tell me my total annual leave and what remains?
I need my vacation summary: total, used, and left.
What's my current vacation balance?
Please check my leave entitlement for this year.
Vacation days left?
How much PTO have I used so far in 2026?
Could you confirm how many annual leave days I'm entitled to?
Need a quick leave count: total allotment vs consumed days.
Based on my profile, what's my vacation allowance and remaining days?
Give me my PTO totals in numbers only.
I want to plan time off. How many days have I got left exactly?
Tell me annual leave taken and available.
Before I request leave, what are my total and used vacation days?
What's my PTO situation right now?
Please provide my vacation entitlement details for this leave year.
How many paid leave days are still available to me?
In one line: total leave, leave used, leave remaining.

**Notes:**
Here’s the problem with AI - you can’t just arrange-act-assert and assume the inputs and outputs will be the same. The same input run multiple times will give a different output, as we have already seen.

Here’s 20 ways to ask the same basic question. Different countries have different ways to describe paid time off - holiday, PTO, vacation, so for global systems there is a massive amount of variety in the language you might send to a chatbot.
## Slide 19

**Body:**
You have 30 days vacation a year
You have thirty days holiday per year
You have 6 weeks holiday per year with 1 week and 2 days remaining
You have 12 days remaining
Out of 30 days you have used 6
You have 25 days holiday and 8 lieu days this year, with 6 remaining
You have taken 18 days already
Out of your twenty five days, you have nine remaining

**Notes:**
Same with responses - words, numbers, different combinations of days available, days taken, days remaining
## Slide 20 — Traditional assertions don’t work with AI.

**Notes:**
Basic true/false assertions don’t work with AI. You can’t assert that something happened, or returned a certain result as AI is non-deterministic.

If the response has lots of text, how can you evaluate that this text has the relevant information? You can’t just look for a specific output, or keywords, and hope for the best.
## Slide 21 — The answer is evaluations.  Using AI as a judge to evaluate the outcome of an AI application against different metrics.

**Title (verbatim):**
The answer is evaluations.

Using AI as a judge to evaluate the outcome of an AI application against different metrics.

**Notes:**
Evaluations are the use of an AI to evaluate the results of an AI system, measuring them on a range of criteria, some well established, some defined by domain experts.

As it turns out, AI is about as good as a human in evaluating how well an AI application worked. So you can use AI to convert non-deterministic output into pass/fail criteria that you can then use in an assertion. Poacher turned gamekeeper.

But you need to tell the AI:
what it is you want it to judge on
Any criteria for this
## Slide 22

**Notes:**
Let’s add evals to our app. In this case we’re going to use Phoenix, an open source LLM observability tracing and evaluation platform.

I have this running locally, it’s available as a docker container which you can run anywhere, or a cloud offering.
## Slide 23 — Demo - observability

**Notes:**
Step 1 is to add Phoenix for observability to capture everything that is happening with our LLM interactions.
Show phoenix running locally
Show code change, talk about open inference and OTel in app.py
Run the chatbot and look at the trace
## Slide 24 — Demo - evals

**Notes:**
Now we can add an eval - using an LLM to check the results of our chatbot.
In this case we are going to use an eval called Faithfulness. This is built into Phoenix and checks for how faithful the output is to the input. In this case, does the output contain a number of days that is reflected in the input.

Show the code for the evals.py
Show the annotated result in Phoenix
## Slide 25 — Demo - fixed code

**Notes:**
Now we’ve identified that there is an issue, we can fix it.
## Slide 26 — So how does this fit into an SDLC for AI engineers?

**Notes:**
So yay for evals, but what does this mean for our application development?

It means we need to add evals into our TDD strategy. We cannot assert on the outputs, but we can assert on the eval.
Combine this with a massive dataset of inputs to build a wide testing space, and suddenly we can add testability to our AI engineering SDLC.
TDD -> EDD, eval driven development
## Slide 27 — Eval Driven Development:  Arrange Act Evaluate Assert

**Title (verbatim):**
Eval Driven Development:

Arrange
Act
Evaluate
Assert

**Notes:**
Now we have a different flow:
Arrange
Act
Evaluate
Assert
## Slide 28 — Demo - EDD

**Notes:**
Lets now build this into a unit test, using a slightly more advanced example with a tool call.
## Slide 29 — Beware though - AI makes mistakes!

**Notes:**
Remember, AI makes mistakes. So there is a chance the evaluation will fail.

You need to define a pass rate that is ideally around 90% or above that is acceptable, not an all must pass
## Slide 30 — This is a simple eval.  In the real world, you need to build complex evals using custom prompts

**Title (verbatim):**
This is a simple eval.

In the real world, you need to build complex evals using custom prompts

**Notes:**
This eval is a simplistic one designed to be generic and support all manner of inputs.
In a real world system, you would spend time building more custom evals
## Slide 31 — You also need a huge dataset of inputs to test against

**Notes:**
Unlike TDD where you have a small test space, you need a huge test space for EDD, to cover a diverse set of user inputs.
## Slide 32 — And be aware evals cost money in tokens!

**Notes:**
Unlike TDD where you have a small test space, you need a huge test space for EDD, to cover a diverse set of user inputs.
## Slide 33 — What makes a good eval?

**Notes:**
So what makes a good eval? How do you know if you are measuring the right thing? It depends!
## Slide 34 — If an agent doesn’t complete a task, but asks for more information, is that a fail?

**Notes:**
Success can have multiple outcomes. If you have code to get an account balance, you can define the rules for that code and write a unit test.
With AI, what is success. For example, ask a customer service agent for a bank for account balance when you have multiple accounts
Gives you all your balances. Is that right?
Asks which account? Is that right?
Says I can’t do that. Is that right?

Need a domain expert to decide what is the right outcome, then measure if the agent got you closer.
## Slide 35 — If the information is technically correct, but contextually useless, is that a pass or fail?

**Notes:**
Bill and Ted - It seems to me the only thing you've learned is that Caesar is a salad dressing dude
How would you test for this? You could create a metric that evaluates all responses based on the core domain of the app - historical references for a history app, salad for a recipe app, cipher for cryptography etc. You could the adjust for audience - elementary school, political courses, cooking for vegans etc.
## Slide 36 — Evaluations need a domain expert

**Notes:**
Evaluations are based very much on the behavior you want from your app. These need to be defined by a domain expert who understands what your app is meant to do.

Domain experts can choose out of the box evaluations, or define new ones
## Slide 37

**Notes:**
A note on the tools.
Phoenix is an open source LLM observability and evaluation platform. It comes from Arize, the folks behind OpenInference, an extension for Otel for tracing LLM applications.
Like most open source companies, there is an open source version, and a hosted version. Phoenix is the open source version, and is free, with a hosted version called Phoenix cloud.
They also offer AX, a more complete paid tier, with features like an agent that can build evals for you.
## Slide 39 — Build                    vs                    Buy

**Notes:**
Here’s a slide from Arize with the comparison.
## Slide 40 — Evaluation Driven Development

**Notes:**
And that is evaluation driven development, a new way to reduce AI suckiness, build reliable AI apps and reduce the chance of your AI projects failing.
## Slide 41 — Jim Bennett @jimbobbennett

**Title (verbatim):**
Jim Bennett
@jimbobbennett

**Body:**
linktr.ee/jimbobbennett
