---
title: 'Prove going for a walk makes you more productive by measuring CO2 with an IoT device'
conference: 'NDC London (and other 2025 venues)'
year: 2025
source: 'Apple Keynote deck'
source_file: '~/Desktop/CO2 measurement.key'
deck_mtime: '2025-01-30'
paired_transcripts:
  - 2025-ndc-london-upEgSfqDTIg.md
pairing_note: 'Source deck for the NDC London 2025 talk. Read the deck (slide titles + presenter notes) alongside the YouTube transcript to see how Jim translates written notes into spoken delivery — the deck is much tighter than the 55-minute spoken version.'
---

_Source: Apple Keynote deck. No video / no timestamps. Structured by slide number. Each slide section captures the on-slide text (title + body) and Jim's presenter notes — the notes are the spoken narration._

## Slide 1 — Prove going for a walk makes you more productive by measuring CO2 with an IoT device

**Body:**
Jim Bennett

Head of developer advocacy



@jimbobbennett
linktr.ee/jimbobbennett

**Notes:**
Open:
Edge with portal
Code in VS Code, ssh to Pi
Camera
Start sensor and monitor
## Slide 2 — Who has almost fallen asleep in a meeting?
## Slide 3 — Or during a conference talk?
## Slide 4 — Did you know the solution is actually to go for a walk?  Or at least go outside…
## Slide 5 — The culprit?  CO2
## Slide 6 — Produced by animals breathing or burning fossil fuels.  Feeds plants.  Kills meetings, classrooms, and the planet

**Title (verbatim):**
Produced by animals breathing or burning fossil fuels.

Feeds plants.

Kills meetings, classrooms, and the planet
## Slide 7

**Body:**
Demo

**Notes:**
Show Pi with lights
Breathe on the sensor and show the lights going red
## Slide 8 — CO2 levels and health

**Notes:**
What do these numbers mean? They are parts per million, so 400 ppm means out of every 1 million molecules in the air, 400 are CO2, so about 0.04%.

High CO2 levels directly affect how well you think. Research from Harvard found that cognitive scores decrease by 21% when CO2 levels reach 945 ppm compared to 550 ppm. This means slower response times and less accurate decision-making​. This is why in long meetings with lw ventilation people make dumb decisions. Short meetings, or going outside makes us smarter!

At levels around 1,000 ppm, people often lose focus and productivity. Imagine all these kids in school with high CO2 levels!
## Slide 9 — CO2 levels and disease

**Notes:**
CO2 levels also correlate to an increase in the spread of infectious diseases 
High CO2 levels are an indication of ventilation - higher levels mean airborne diseases can stick around more.
CO2 monitors are a cheap way to determine risk
A paper published in Nature in April 2024 showed an increase in COVID aerostability with increased CO2 levels
## Slide 10 — The easiest way to get away from high CO2 concentrations  is to go outside!
## Slide 11 — What do we have here?

**Notes:**
Demo using camera - RPi, SSD, Grove hat, CO2 sensor, lights
No need for details - comes later
## Slide 12 — This is an IoT device - Internet of Things

**Notes:**
Define IoT - hardware and software combined
Define sensors and actuators
Example - watering system
## Slide 13 — At its core - a Raspberry Pi.  The Thing!

**Title (verbatim):**
At its core - a Raspberry Pi.

The Thing!

**Notes:**
Raspberry Pi - single board computer. Fully featured linux computer, quad code 2.4GHz ARM processor, 8GB of RAM in mine.
I also added an active cooler and a 256GB SSD.
Runs Raspberry Pi OS - a Debian port, but can also run Ubuntu and other linux distros. About 75 for the RPi, less for less RAM
Raspberry Pis are use a lot in IoT scenarios when powerful devices are needed - they even do a compute board with the same specs but on a modular platform designed to go into electronics like industrial IoT control systems.
RPI has GPIO pins - general purpose input output so you can attach hardware
Because it is linux, it runs any software that linux can run
## Slide 14 — Sensor is a Grove SCD41 CO2 sensor

**Notes:**
The sensor is a SCD41 CO2, temperature and humidity sensor. It uses photo acoustic NDIR to get the CO2 concentration. This using IR at a wavelength of about 4.2 micrometers which is a wavelength that CO2 absorbs. The CO2 absorbs this causing molecular vibration that is released as a pressure wave that is measured with microphone.

Essentially firing a laser at CO2 till it screams, and measuring how loud the screams are
## Slide 15 — Sensor is a Grove SCD41 CO2 sensor

**Notes:**
It’s connected to the RPi using a Grove hat from Seeed Studio just to make wiring easier.
## Slide 16 — SCD41 uses I2C

**Notes:**
Connection is over I2C, or inter integrated circuit. It’s a bus where you can connect many devices to the same connection on the RPi and each device has an address that can be used to identify it, usually hard coded on the device. Only one device can send or receive data at a time - it becomes a controller, sends or receives data, then gives up the controller status so another device can be used.
## Slide 17

**Body:**
Demo

**Notes:**
Lets get some CO2 measurements from this
Show a stream of sensor measurements

This is overkill - but a good platform to demonstrate this. Expensive, large power drain, but fun!
You can do the same with a low cost microcontroller run off a coin cell battery
## Slide 18 — .NET IoT

**Notes:**
.NET IoT allows you to run .NET applications on single board computer style IoT devices, such as Raspberry Pis. The RPi runs linux, so .NET runs as if it was on any linux device, and you can use libraries that provide hardware abstractions over sensors, actuators, and other components.

For the SCD41, there is a device binding in the .NET IoT nuget package we can use to access it
## Slide 19

**Body:**
// Connect to the CO2 sensor
I2cConnectionSettings settings = new(1, Scd4x.DefaultI2cAddress);
I2cDevice device = I2cDevice.Create(settings);
Scd4x sensor = new(device);

// Get the CO2 volume
(VolumeConcentration? co2, _, _) = await sensor.ReadPeriodicMeasurementAsync();
Console.WriteLine($"CO2: {co2.Value.PartsPerMillion} ppm");

**Notes:**
This code uses an I squared C connection to connect to the SCD41 sensor
It then pulls back the values. Fun thing about the .NET IoT library - it uses UnitsNet to apply strongly typed physical units where possible. For example, the CO2 measurement is in parts per million
## Slide 20 — Lets add the Internet part!

**Notes:**
The I in IoT stands for Internet, so lets add the internet part - let’s get the CO2 data off the device and send it to the cloud.
## Slide 21 — MQTT  Message Queuing Telemetry Transport

**Title (verbatim):**
MQTT

Message Queuing Telemetry Transport

**Notes:**
MQTT, or message queuing telemetry transport is the industry standard for IoT devices. It’s a lightweight protocol designed by Andy Stanford-Clark at IBM in 1999 for sending sensor data in oil pipelines.

You have an MQTT broker, and multiple clients can connect to this broker to publish and subscribe. Messages are sent and received on different named topics.

A standard IoT architecture is to have a MQTT broker in the cloud somewhere. You then have multiple clients connected - devices with sensors that capture data and publish it to the broker, and services that subscribe to data. These subscribers can be things like analytics services to monitor for certain situations, or IoT devices that react the data.

It’s not really a message queue as such, though can act like one depending on how the clients are broker are set up. The name comes from being part of the IBM MQ product line.
## Slide 22 — Azure IoT Services are a bit of a mess…

**Notes:**
I used to do a lot with the Microsoft IoT stack, but it is a bit of a mess at the moment.

They used to have:
IoT Hub as a way to connect and manage devices
IoT Central as a SaaS platform to connect and manage devices, and visualize them

IoT Hub is pretty good, but generally used its own SDKs for devices to connect. It could sort of work with standards, but wasn’t truly standards compliant - you could use MQTT to send data, but it was a hack. Might be going away soon.
IoT Central was great, but is being deprecated. Again, not standards compliant.

They’ve now added Azure IoT Operations which is a fully featured powerful scalable IoT solution that has an MQTT broker, uses Kubernetes, Azure Arc, and all the lovely buzzwords for a huge, expensive solution. Overkill for what we are doing. Good luck spinning one of these up for a test with the $200 of Azure credit you get on the free trial. Great for a large factor deployment, terrible for trying things out.
## Slide 23 — So what’s a good place to start?  Azure Event Grid

**Title (verbatim):**
So what’s a good place to start?

Azure Event Grid

**Notes:**
Azure event grid is a great place to start. It’s a pub/sub message broker with all the usual cloud scalability capabilities. It has an MQTT broker, and you can start with this, then scale up to Azure IoT Operations if you need to. Cost is $1 per million operations, with 1M free per month. Than about $1 a day to keep it running.

Despite the joke that the S in IoT stands for security, MQTT can be secured. You can authenticate using a username and password, or X.509 certificates. You can also use authorization to limit things like which devices can access which topics.

By using Azure Event Grid, you get all of this from Azure - for example you can use x.509 certificates for clients to connect and publish, then RBAC using Entra to manage access for servers to subscribe to data.
## Slide 24

**Body:**
Demo

**Notes:**
So lets look at a setup. I’m not going to create one from scratch as it takes too much time.

Demo event grid, MQTT broker, certificates, topics
## Slide 25 — Create an Azure Resource Group Create an Azure Event Grid namespace, and turn MQTT on Create a topic space with a topic Create clients - you many need to create certificates for these clients Create a permission binding for client groups to topic spaces to publish Create a permission binding for client groups to topic spaces to subscribe

**Title (verbatim):**
Create an Azure Resource Group
Create an Azure Event Grid namespace, and turn MQTT on
Create a topic space with a topic
Create clients - you many need to create certificates for these clients
Create a permission binding for client groups to topic spaces to publish
Create a permission binding for client groups to topic spaces to subscribe
## Slide 26 — Now we can connect from our device!

**Notes:**
There is MQTTNet, an MQTT library from .NET that we can use to connect to event grids and send messages
## Slide 27

**Body:**
Demo

**Notes:**
Demo sending data to MQTT
Show data being received in Event Grids
## Slide 28 — What do we do with the data?

**Notes:**
Data goes in to event grids, so what do we do with it?
Other systems can then subscribe to the same topic to get data out.
From there - it’s up to you what you do!
Multiple systems can subscribe, it’s not a one to one setup.

For example, you can have an alert system subscribed to respond straight away and give warning of high levels, and also a reporting system that tracks historical data. And yes, you can add AI to analyze the data to look for patterns.

On my Pi I have also added a monitoring process that lights the lights - this subscribes to the same topic. Once device means less for me to carry around… Could be one, could be multiple sensors, or multiple lights

Logitech spot
## Slide 29

**Body:**
Demo

**Notes:**
Demo receiving data
## Slide 33 — CO2 is bad You can monitor it with low cost hardware Technologies like MQTT are designed for IoT devices to send data Services like Azure Event Grid can act as an MQTT broker You can expand IoT systems by adding more services Going for a walk is good!

**Title (verbatim):**
CO2 is bad
You can monitor it with low cost hardware
Technologies like MQTT are designed for IoT devices to send data
Services like Azure Event Grid can act as an MQTT broker
You can expand IoT systems by adding more services
Going for a walk is good!
## Slide 34

**Body:**
Build this yourself

github.com/jimbobbennett/co2sensor

**Notes:**
Demo receiving data
## Slide 35 — Thank you

**Body:**
Jim Bennett

Head of developer advocacy



@jimbobbennett
linktr.ee/jimbobbennett
