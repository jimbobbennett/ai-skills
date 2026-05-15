---
title: 'Clicking on the real world with iBeacon and Eddystone'
conference: 'unknown (deck source only)'
year: 2016
source: 'Apple Keynote deck'
source_file: '~/Desktop/Clicking on the real world with iBeacon and Eddystone.key'
deck_mtime: '2016-09-24'
context: 'Era: Jim at EROAD New Zealand, doing mobile/IoT talks. Pre-AI, pre-Arize.'
paired_transcripts: []
pairing_note: 'No YouTube transcript in the corpus for this talk. Useful for style-drift signal — 2016 voice, more written, less hand-raise-trap.'
---

_Source: Apple Keynote deck. No video / no timestamps. Structured by slide number. Each slide section captures the on-slide text (title + body) and Jim's presenter notes — the notes are the spoken narration._

## Slide 1 — Clicking on the real world with iBeacon and Eddystone

**Title (verbatim):**
Clicking on the real world
with iBeacon and Eddystone

**Body:**
Jim Bennett
              Mobile Application Developer at EROAD in      
              New Zealand
http://eroad.com
@JimBobBennett
http://JimBobBennett.io

**Notes:**
Initial setup - QuickTime if needed, XS

This talk is about bluetooth beacons, context aware apps, changing the way we interact with the real world.
Look at iBeacon and write a quick app
Look at Eddystone/google physical web (but not time to code)
But mostly about coffee
## Slide 2 — Buying coffee is not as easy as it could be…

**Notes:**
Coffee - hard, millions buy coffee every day with the same actions, queue, pay, loyalty card, collect, no seats left, distraction from twitter or cat videos
Better if it knew I was in the shop for auto order, knew where I was to bring me my coffee
Can’t use GPS - not accurate enough (e.g. coffee auto order when walking past)
## Slide 3 — We click on apps all the time…

**Body:**
Our phone has become an extension of our physical selves

But to interact with the real world we have to find the virtual representation of the world on our phones

**Notes:**
Phone is disconnected from the world - we have maps but that’s about it
Would be better if our phones could understand our context and respond accordingly, make the real world talk to our phone
## Slide 4 — …but can we ‘click’ on the real world?

**Body:**
Can our phone intuitively show a link to the app for the coffee shop we are in?

Can the act of walking into a coffee shop ‘click’ the buy button on their app?

Can sitting down in the coffee shop send the app our seat location?

**Notes:**
Click on the real world - use our phone to cause a real world interaction, or have a real world interaction happen to our phone
## Slide 5 — Yes - using bluetooth beacons

**Body:**
Bluetooth Low Energy Beacons transmit an Id to any device that is listening

Apple created iBeacon - focus on proximity/indoor location and notifications to installed apps

Google created the Physical Web using Eddystone beacons and iBeacon - focus on attaching URLs or messages to physical locations and interacting with them on demand
## Slide 6 — iBeacon on iOS

**Body:**
Transmits an Id (128bit GUID), major and minor version (16bit int), transmission power indicator

iOS apps can monitor for an Id/version even when terminated, and be woken up

Once awake the app can range all found beacons to get distance based off transmission power

Lock screen icons when in range of beacons

Built into the Core Location iOS APIs and needs user location permissions

Any app can monitor or range any iBeacon id’s

**Notes:**
Region - one or more beacons with the same id, major, minor
Monitoring - detect beacon, wake app up, once per region
Ranging - detect all beacons and get distances, continuous stream of data
Authorisation - in use/always
No updates since launch a few years ago
## Slide 7 — iOS iBeacon Hands-On Coding Demo

**Notes:**
Show code to monitor an iBeacon and wake the app up
Show code to range an iBeacon and see the signal strength
Coffee shop - auto order when walking in, location to bring coffee to me
## Slide 8 — Google’s open source beacon standard and part of the Physical Web - attaching URLs or messages to physical objects  Eddystone UID transmits a 10 byte namespace and 6 byte instance  Eddystone EID is like UID but with a rotating, secure ID  Eddystone URL transmits a compressed URL  All formats also include a TLM packet for telemetry (e.g. remaining battery life)  Google have published a configuration GATT service

**Title (verbatim):**
Google’s open source beacon standard and part of the Physical Web - attaching URLs or messages to physical objects

Eddystone UID transmits a 10 byte namespace and 6 byte instance

Eddystone EID is like UID but with a rotating, secure ID

Eddystone URL transmits a compressed URL

All formats also include a TLM packet for telemetry (e.g. remaining battery life)

Google have published a configuration GATT service

**Notes:**
All recent - since june last year with EID/configuration GATT service announced a week ago
## Slide 9 — Eddystone UID/EID

**Body:**
Beacons are registered using the Proximity API to a project so can’t be shared between different apps

Interact with UID using Nearby Messages API from Google Play Services

Messages can include a latitude, longitude, floor location or Place Id for use with the Places API

Requires internet connection 

Passive interaction - will not wake your device up

EID - same as UID except using a secure, rotating ID

**Notes:**
Lots of configuration via proximity API
Recently released an app to help
iOS and Android
Passive - android has lock screen notification
Not going to show code - would be a whole talk in itself - see me after or my GitHub for a demo
## Slide 10 — Eddystone URL

**Body:**
Compressed URL embedded in the BLE packet

Only 17 ASCII characters available but they have shortcuts for http://, https://, www, .com etc.

Chrome or Google Physical Web app can show these links on Android lock screen or iOS Chrome today widget

No SDK available - just code examples based on raw BLE interactions

**Notes:**
If you have Chrome on your lock screen or an Android device check now
Good for customer engagement - coffee shop app on your lock screen
## Slide 11 — Which one to use? Depends!

**Body:**
iBeacon for waking your app up and for indoor location

Nearby Messages API helps with crowdsourced location data from Places API

Nearby Messages API works on iOS and Android with Eddystone and iBeacon

Vendor SDK’s are blurring the lines - they support iBeacon like functionality on Android

Newer beacons can broadcast both iBeacon and Eddystone at the same time
## Slide 12 — Where to get beacons?

**Body:**
Plenty of vendors providing hardware
Vendors have proprietary API’s with extra functionality and back end management systems

**Notes:**
Few estimote beacons to give out to first 5 people to find me
## Slide 13 — Questions?

**Body:**
@JimBobBennett
jim@JimBobBennett.io
