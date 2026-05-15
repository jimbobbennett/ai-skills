---
title: 'Stop doing dumb things with AI (Galileo demo)'
conference: 'NVIDIA / Galileo event (deck source only)'
year: 2025
source: 'Apple Keynote deck'
source_file: '~/Desktop/NVIDIA-Galileo-demo.key'
deck_mtime: '2025-11-18'
paired_transcripts:
  - 2025-ai-engineer-worlds-fair-xJXm4Wcw4m8.md
pairing_note: 'Galileo.ai-branded variant of Jim''s EDD talk. Same core thesis (AI-as-judge, Arrange-Act-Evaluate-Assert), but newer (Nov 2025) and with the ''Pakistan Dawn newspaper'' news-story hook in place of the Chicago Sun-Times one used at AI Engineer. Useful as the most-recent evolution of his AI talk in the corpus.'
---

_Source: Apple Keynote deck. No video / no timestamps. Structured by slide number. Each slide section captures the on-slide text (title + body) and Jim's presenter notes — the notes are the spoken narration._

## Slide 1 — Stop doing dumb things with AI

**Body:**
Jim Bennett

Principal Developer Advocate



@jimbobbennett
linktr.ee/jimbobbennett
## Slide 2 — Who trusts AI?

**Body:**
Is it time for malicious compliance?
## Slide 3

**Body:**
Is it time for malicious compliance?

**Notes:**
AI can generate everything from amazingly correct outputs, to utter garbage. So it needs to be checked.
## Slide 4 — AI is like an enthusiastic 5 year old with a stack of out-of-date encyclopedias

**Notes:**
Here’s a great example from the Pakistan Dawn newspaper. The last paragraphs read, and I quote:
## Slide 5 — Outlook for FY26  Muesha Sohail expects the positive momentum in Pakistan's auto sector to continue in FY26, driven by lower interest rates and the launch of new models across conventional, hybrid, and plug-in hybrid engines.  If you want I can also create an even snappier front-page style version with punchy one-line stats and a bold, infographic-ready layout perfect for maximum reader impact. Do you want me to do that next?

**Title (verbatim):**
Outlook for FY26

Muesha Sohail expects the positive momentum in Pakistan's auto sector to continue in FY26, driven by lower interest rates and the launch of new models across conventional, hybrid, and plug-in hybrid engines.

If you want I can also create an even snappier front-page style version with punchy one-line stats and a bold, infographic-ready layout perfect for maximum reader impact. Do you want me to do that next?

**Notes:**
Enter the evaluations engineer!

Evaluations are a way to add determinism to the non-deterministic world of AI, and use another AI to test the output of your AI, your agents, and so on.

An evals engineer identifies failure states in an AI app, builds metrics to test for these failure states, iterates on the metrics, then uses them to test apps in dev and production, continuously iterating based off real world data
## Slide 6 — So how do we fix it?  Enter the Evals Engineer!

**Title (verbatim):**
So how do we fix it?

Enter the Evals Engineer!

**Notes:**
Enter the evaluations engineer!

Evaluations are a way to add determinism to the non-deterministic world of AI, and use another AI to test the output of your AI, your agents, and so on.

An evals engineer identifies failure states in an AI app, builds metrics to test for these failure states, iterates on the metrics, then uses them to test apps in dev and production, continuously iterating based off real world data

Metrics are LLM prompts that convert the non-deterministic to the deterministic
## Slide 7 — Evaluation Driven Development:  Arrange Act Evaluate Assert

**Title (verbatim):**
Evaluation Driven Development:

Arrange
Act
Evaluate
Assert

**Notes:**
Arrange
Act
Evaluate
Assert

This fits into early development - prompt engineering, model selection. Fits into unit tests during coding, fits into CI/CD to block releases, and runs in production to add observability
## Slide 8 — Make AI reliable at galileo.ai

**Body:**
linktr.ee/jimbobbennett
## Slide 9 — Jim Bennett @jimbobbennett

**Title (verbatim):**
Jim Bennett
@jimbobbennett

**Body:**
linktr.ee/jimbobbennett
## Slide 10 — Your AI project will probably fail

**Notes:**
Who is working on an AI project?
RAND corporation study claims more than 80% of AI projects will fail.
95% according to MIT
Software projects do fail, 50% by some measures, but this is a lot higher.
So why?
Reasons for failure - promotion driven development, lack of direction, lack of understanding of what the app should do, wrong technology
## Slide 11 — AI is like an enthusiastic 5 year old with a stack of out-of-date encyclopedias
## Slide 12 — AI is like an enthusiastic 5 year old with a stack of out-of-date encyclopedias
## Slide 13 — AI is like an enthusiastic 5 year old with a stack of out-of-date encyclopedias
## Slide 14 — AI is like an enthusiastic 5 year old with a stack of out-of-date encyclopedias

**Notes:**
Confident, want’s to help, can be utterly wrong. Literally all the AI chat tools have a disclaimer saying it can make mistakes.
## Slide 15 — Or Mansplaining as a service…
## Slide 16 — AI is not intelligent, it’s just confident, sycophantic, autocomplete
## Slide 17 — It’s not all doom and gloom.  When it works, it’s fantastic!

**Title (verbatim):**
It’s not all doom and gloom.

When it works, it’s fantastic!

**Notes:**
AI is great at working with unstructured data, such as data from disparate systems and natural language. When it works it can understand a users intent, make decisions, gather data from disparate sources and bring it together, interact with tools without the strong contract of an API, and so on.
## Slide 18 — So what do we, as developers, do to ensure our AI doesn’t suck?

**Notes:**
The problem we have as developers is that our traditional development methodologies just don’t work any more.
AI can help build a whole new class of applications, but how we develop them has to change.
## Slide 19 — We are used to deterministic problems

**Notes:**
As developers we are used to code that runs reliably and deterministically. We write unit and integration tests with expected input and expected outputs.

Who uses TDD? Writes tests? Tests their software? Move fast and break things? Even Facebook realized this was dumb and changed it to move fast and build things.

Test driven development, or TDD, is a standard practice for effective development teams.
## Slide 20 — Test-Driven development

**Notes:**
Test driven development makes so much sense. When you have the business problem, code structure, or bug well defined, you can start with a set of tests, then update the code to make the tests pass, then refactor knowing that the tests passing allow you to refactor without worrying that your app won’t work.

Tests also define business knowledge, domain knowledge and so on - they can define what the application should do.
This process ensures your app is tested, and that you are thinking up front what the app should do, and what the acceptance criteria is
## Slide 21 — Test Driven Development:  Arrange Act Assert

**Title (verbatim):**
Test Driven Development:

Arrange
Act
Assert

**Notes:**
Standard unit testing follows a basic pattern - you set up some inputs, you do something with them, then you check the output against a well-defined expectation.
Can be given-when-then.
How does this apply to AI when the assert is not so simple?
## Slide 22 — Traditional assertions don’t work with AI.

**Notes:**
Basic true/false assertions don’t work with AI. You can’t assert that something happened, or returned a certain result as AI is non-deterministic.

If the response has lots of text, how can you evaluate that this text has the relevant information? You can’t just look for a specific output, or keywords, and hope for the best.
## Slide 23 — The answer is evaluations.  Using AI as a judge to evaluate the outcome of an AI application against different metrics.

**Title (verbatim):**
The answer is evaluations.

Using AI as a judge to evaluate the outcome of an AI application against different metrics.

**Notes:**
Evaluations are the use of an AI to evaluate the results of an AI system, measuring them on a range of criteria, some well established, some defined by domain experts.

As it turns out, AI is about as good as a human in evaluating how well an AI application worked. So you can use AI to convert non-deterministic output into pass/fail criteria that you can then use in an assertion. Poacher turned gamekeeper.

But you need to tell the AI:
what it is you want it to judge on
Any criteria for this
## Slide 24 — If an agent doesn’t complete a task, but asks for more information, is that a fail?

**Notes:**
Success can have multiple outcomes. If you have code to get an account balance, you can define the rules for that code and write a unit test.
With AI, what is success. For example, ask a customer service agent for a bank for account balance when you have multiple accounts
Gives you all your balances. Is that right?
Asks which account? Is that right?
Says I can’t do that. Is that right?

Need a domain expert to decide what is the right outcome, then measure if the agent got you closer.
## Slide 25 — If the information is technically correct, but contextually useless, is that a pass or fail?

**Notes:**
Bill and Ted - It seems to me the only thing you've learned is that Caesar is a salad dressing dude
How would you test for this? You could create a metric that evaluates all responses based on the core domain of the app - historical references for a history app, salad for a recipe app, cipher for cryptography etc. You could the adjust for audience - elementary school, political courses, cooking for vegans etc.
## Slide 26 — Demo

**Notes:**
Let’s see this in action

Demo:
App
Answer
Metric
Updated system prompt
## Slide 27 — Evaluations need a domain expert

**Notes:**
Evaluations are based very much on the behavior you want from your app. These need to be defined by a domain expert who understands what your app is meant to do.

Domain experts can choose out of the box evaluations, or define new ones
## Slide 28 — Evalution Drive Development allows you to test:  Prompts Models Applications Production apps

**Title (verbatim):**
Evalution Drive Development allows you to test: 
Prompts
Models
Applications
Production apps

**Notes:**
Evaluations are important at all stages in your application lifecycle.
At the analysis stage as you do prompt engineering and model selection
In the application development stage as you write unit tests for your code
When you deploy to production to constantly evaluate behavior
## Slide 29 — Evaluation Driven Development

**Notes:**
And that is evaluation driven development, a new way to reduce AI suckiness, build reliable AI apps and reduce the chance of your AI projects failing.
## Slide 30 — We’re looking for AI developers to give us feedback

**Body:**
linktr.ee/jimbobbennett

**Notes:**
And we’ll pay! $50 amazon gift card, or donation to a charity of your choice.
## Slide 31 — Play Silly Games  Win Silly Prizes

**Title (verbatim):**
Play Silly Games

Win Silly Prizes
