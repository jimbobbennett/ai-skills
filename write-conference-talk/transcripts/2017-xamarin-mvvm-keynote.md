---
title: 'Cross-platform Xamarin apps with MVVM'
conference: 'unknown (deck source only)'
year: 2017
source: 'Apple Keynote deck'
source_file: '~/Desktop/CrossPlatformXamarinAppsWithMvvm.key'
deck_mtime: '2017-02-26'
context: 'Era: Jim at EROAD, author of Xamarin in Action (Manning). Slide 1 title text reads ''marin'' (a truncated ''Xamarin'' from extraction).'
paired_transcripts: []
pairing_note: 'No YouTube transcript. Possibly related to the NDC ''Fabulous'' transcript (`ndc-fabulous-Hm4EDPNXQqY.md`) since both are Xamarin-era — but Fabulous is F#-specific so probably a different talk. Useful for 2017 voice baseline.'
---

_Source: Apple Keynote deck. No video / no timestamps. Structured by slide number. Each slide section captures the on-slide text (title + body) and Jim's presenter notes — the notes are the spoken narration._

## Slide 1 — marin

**Body:**
Making your native apps even more cross-platform using MVVM
## Slide 2 — Jim Bennett

**Body:**
Mobile Developer at EROAD

@JimBobBennett
https://JimBobBennett.io
https://github.com/jimbobbennett
## Slide 3 — Author of Xamarin in Action

**Body:**
Learn how to build production-quality Xamarin apps using MVVM to increase the amount of cross-platform code



Now available as part of the Manning Early Access Program
## Slide 4 — Why do we use Xamarin?
## Slide 5 — Common languages and framework

**Body:**
One language for multiple platforms (C# or F#)
Core libraries (collections, simple types, LINQ, Task)
Access to other shared code (NuGet packages)

**Notes:**
One language for multiple platforms (C# or F#)
Core libraries (collections, simple types, LINQ, Task)
Access to other shared code (NuGet packages)
## Slide 6 — Code can be shared across platforms

**Body:**
Xamarin wrappers for the OS SDKs can only be used on one platform
All other code can be shared between platforms
Common to build all business logic in shared cross-platform code

**Notes:**
Xamarin wrappers for the OS SDKs can only be used on one platform
All other code can be shared between platforms
Common to build all business logic in shared cross-platform code
## Slide 7 — Xamarin Cross-Platform apps

**Body:**
Xamarin apps are native apps
Code written using the core libraries can be shared across all platforms using PCLs
Only the platform specific stuff is not cross platform
## Slide 8 — MVVM increases the amount of testable shared code in your apps
## Slide 9 — Example - TipCalc

**Body:**
Less code mean less bugs, and fewer places to fix them
More shared code makes it easier to keep platform features in line
The less you write, the faster you get to market
## Slide 10 — Business logic - in shared code in a PCL

**Body:**
Less code mean less bugs, and fewer places to fix them
More shared code makes it easier to keep platform features in line
The less you write, the faster you get to market
## Slide 11 — UI - in platform-specific code in iOS/Android app projects

**Body:**
Less code mean less bugs, and fewer places to fix them
More shared code makes it easier to keep platform features in line
The less you write, the faster you get to market
## Slide 12 — UI is wired up to business logic in platform-specific code

**Body:**
Less code mean less bugs, and fewer places to fix them
More shared code makes it easier to keep platform features in line
The less you write, the faster you get to market
## Slide 13 — Only the business logic can be unit tested

**Body:**
Unit tests can be written against the cross-platform business logic code
Unit tests cannot be written against the platform-specific code - it is too dependent on the UI

**Notes:**
Unit tests can be written against the cross-platform business logic code
Unit tests cannot be written against the platform-specific code - it is too dependent on the UI
Less unit tests = more manual tests, more time for developers and testers to test, more risk
## Slide 14 — Only the business logic is cross-platform

**Body:**
The business logic is written once
The wiring from the business logic to the UI has to be written twice

**Notes:**
The business logic is written once
The wiring from the business logic to the UI has to be written twice
## Slide 15 — The more cross-platform code the better

**Body:**
Cross-platform code has no dependency on the UI so can be unit tested
Less code mean less bugs, and fewer places to fix them
More shared code makes it easier to keep platform features in line
The less you write, the faster you get to market

**Notes:**
Cross-platform code has no dependency on the UI so can be unit tested
Less code mean less bugs, and fewer places to fix them
More shared code makes it easier to keep platform features in line
The less you write, the faster you get to market
## Slide 16 — MVVM FTW!
## Slide 17 — What is MVVM?

**Body:**
Design pattern used for building UI based apps - originally invented by Microsoft for WPF 
Model is business logic
View is pure UI, no logic
View Model is UI logic
Binding wires up view to view model
## Slide 18 — Model layer is business logic

**Body:**
Written using cross-platform code
Can be unit tested
TipCalculator would be part of the model layer
## Slide 19 — View layer is pure UI

**Body:**
Written using platform-specific code
Cannot be unit tested
iOS ViewController/Storyboard and Android Activity/layout would be part of the view layer
## Slide 20 — ViewModel layer and bindings are where all the magic is
## Slide 21 — Each view is backed by a view model

**Body:**
Less code mean less bugs, and fewer places to fix them
More shared code makes it easier to keep platform features in line
The less you write, the faster you get to market
## Slide 22 — State comes from properties

**Body:**
When these properties change an event is raised
The binding layer listens to this event and updates the UI
Can be used for data, or properties that define the UI
Value converters can be used to change the type
## Slide 23 — Behaviour comes from commands

**Body:**
Commands are objects that wrap actions
Commands can control if they can be executed
The binding layer listens to UI events and executes commands
If the commands cannot be execute the binding layer can update the UI to reflect this
## Slide 24 — View models can also handle navigation

**Body:**
Each view has one view model
Navigation is from view model to view model
The MVVM framework finds the right view for a view model and shows it
## Slide 25 — Xamarin Cross-Platform apps with MVVM

**Body:**
Business logic and UI logic can be in platform specific code
Commands and property notifications provide a cross-platform way to interact with the UI
Some application logic is shared
Less platform specific code
## Slide 26 — Demo time!
## Slide 27 — MVVM Frameworks

**Body:**
Some MVVM features (e.g. property change notifications) are part of the .Net framework
Binding comes from third-party frameworks
Frameworks also provide other features such as navigation and easy to use UI widgets

**Notes:**
Some features like INotifyPropertyChanged come from .Net framework
Others come from frameworks
Binding comes from frameworks, as do bindable UI controls
## Slide 28 — What about Xamarin Forms?
## Slide 29 — Xamarin Forms was built for MVVM!
## Slide 30 — MVVM increases the amount of testable shared code in your apps
## Slide 31 — Jim Bennett

**Body:**
Mobile Application Developer at EROAD

@JimBobBennett
https://JimBobBennett.io

Sample code at:
https://github.com/jimbobbennett/CrossPlatformSummit
## Slide 32 — Author of Xamarin in Action

**Body:**
Learn how to build production-quality Xamarin apps using MVVM to increase the amount of cross-platform code



Now available as part of the Manning Early Access Program
