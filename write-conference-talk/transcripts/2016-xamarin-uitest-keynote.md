---
title: 'Xamarin UITest in the real world'
conference: 'unknown (deck source only)'
year: 2016
source: 'Apple Keynote deck'
source_file: '~/Desktop/UITestInTheRealWorld.key'
deck_mtime: '2016-09-20'
context: 'Era: Jim at EROAD, co-presented with a colleague (Andrew). Notes mention ''Andrew giving some real world examples''.'
paired_transcripts: []
pairing_note: 'No YouTube transcript. Pre-AI mobile-testing talk. 12 slides, much tighter and more telegraphic than current voice — useful for style-drift signal.'
---

_Source: Apple Keynote deck. No video / no timestamps. Structured by slide number. Each slide section captures the on-slide text (title + body) and Jim's presenter notes — the notes are the spoken narration._

## Slide 1 — Xamarin UITest in the real world

**Body:**
Jim Bennett

            Mobile Application Developer at EROAD

@JimBobBennett
https://JimBobBennett.io

**Notes:**
About me
I’m giving an overview of UI test
Andrew giving some real world examples
## Slide 2 — Xamarin In Action

**Body:**
Jim Bennett

            Mobile Application Developer at EROAD

@JimBobBennett
http://JimBobBennett.io

**Notes:**
About me
I’m giving an overview of UI test
Andrew giving some real world examples
## Slide 3

**Notes:**
Three types of tests - unit (lots), component (less), UI (less again)
Unit and component - easy to write lots, can be automated as part of CI, getting to be a normal part of most developers workflow
UI normally done by hand
## Slide 4 — Manual testing is not always the best way

**Body:**
It’s done by humans, so prone to error
Humans are bad at remembering what they did to reproduce a bug
Humans get bored 
Hard to track test scenarios (excel spreadsheets are evil)
Humans are expensive
Manual testing takes a long time

**Notes:**
Manual testing - multiple devices. If regression takes a day, then regression on Android and iOS is 2 days.
Add Nougat, Marshmallow, Lollipop, iOS 9, iOS 10, tablet, phone, phablet, landscape, portrait… Lots of days
## Slide 5 — Rise of the machines!

**Body:**
Computers are better than humans for repetitive tasks
If a computer can do the job of a tester it becomes more reliable
Computers don’t get bored and claim tests pass just to bunk off early
Computer tests can be in code tracked in source control
Computers are cheaper to scale and can run 24/7
## Slide 6 — Xamarin UITest

**Notes:**
Key takeaway!
Reliable - they follow the instructions with no shortcuts
Repeatable - run them as often as you like on any device
Reproducible - if a test fails you can run it locally and get the same result
## Slide 7 — What is UITest

**Body:**
New project type
NuGet providing an API to run an app on a device or a simulator and interact with it as if you were a human tester
Has a REPL to allow you to inspect your app
Write code in C# or F# to run and use your app
Write more code in C# or F# to verify what is on screen
## Slide 8 — Lets REPL

**Notes:**
Example in XS - New MVVM Cross app, add UITest,
## Slide 9 — Xamarin TestCloud

**Notes:**
Data center in denmark
Thousands of real devices to run tests on - means coverage of many devices and OS’s without purchasing lots of devices
Coming soon - live debugging on remote devices
Expensive!
## Slide 10 — EROAD TestCloud

**Notes:**
Lego board in Albany - less devices than Xamarin test cloud, more lego!
UI tests now part of every ticket - DOD
Runs quick smoke test on 3 devices every PR, Runs longer tests on 3 devices daily
Use spec flow so tests are documentation of behaviour in English
Test role has changed - smaller manual testing for edge cases, interactions with other tools, test reviews and writing - more test engineer than manual tester
Not available to rent time on
## Slide 11 — You still need people!

**Notes:**
Automated testing cannot test UX!
## Slide 12 — Xamarin UITest

**Notes:**
Key takeaway!
Reliable - they follow the instructions with no shortcuts
Repeatable - run them as often as you like
Reproducible - if a test fails you can run it locally and get the same result
