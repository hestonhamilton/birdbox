# birdbox

## Introduction
This README provides guidance for building a BirdNET Pi Real-Time Acoustic Bird ID Station using a Raspberry Pi.

## Materials
- Raspberry Pi (4B/3B+/0W2) - [Search for approved Pi resellers here](https://www.raspberrypi.com/resellers/?q=)
- Waterproof Project Box - [Example used in project](https://www.amazon.com/dp/B085QCT543)
- MicroSD Card (The bigger the better if you intend to store bird recordings on it long-term) - [Example used in project](https://www.amazon.com/dp/B09W9XYQCQ)
  OR/AND
- SSD (Can either be used to supplement storage of recordings or as the primary boot drive replacing the microSD)
- Heatsink with Fan - [Example used in project](https://www.amazon.com/dp/B07Z3Q417K)
- Waterproof/Outdoor Ethernet Connector - [Example used in project](https://www.amazon.com/dp/B07PH4GL2F)
- Waterproof/Outdoor USB 3.0 Cable - [Example used in project](https://www.amazon.com/dp/B079957VC3)
- USB Microphone - [Example used in project](https://www.amazon.com/dp/B06XCKGLTP)
- PoE to USB-C Adapter - [Example used in project](https://www.amazon.com/dp/B087F4QCTR)

## Setup Steps 
1. Install compatible OS on the microSD card or other boot device. *WARNING:* Due to https://github.com/mcguirepr89/BirdNET-Pi/issues/1055 "Raspberry Pi OS (Legacy, 64-bit) Lite" must be selected during imaging.
2. Install fans/heatsinks on the Raspberry Pi if using them.
4. Mount the Raspberry Pi onto the backplate of the box.
5. Plan your layout with all internal hardware and cables, marking positions where needed.
6. Measure holes for the external USB and Ethernet adapters.
7. Remove all hardware from the box.
8. Drill or cut the holes for the USB and Ethernet adapters.
9. Install the external USB and Ethernet adapters, managing USB cable as needed.
10. Attach SSD to the backplate alongside Pi if using one.
11. Connect SSD to the Pi using SATA to USB adapter.
12. Place backplate into the box.
13. Attach POE adaptor to side of box using double-sided tape or hook and loop tape.
14. Connect external ethernet adapter to the POE adapter.
15. Connect the PoE adapter's Ethernet and USB-C cables to the Raspberry Pi.
16. Connect the external USB adapter's cable to the Pi.
17. Close and mount box somewhere you want to record birdsong and have access to POE.
18. Connect POE Ethernet to external port and wait for device to become available over SSH.
20. Connect to the Pi using SSH credentials set during imaging
21. Install BirdNET-Pi software on the micro SD card. Official installation guide [here](https://github.com/mcguirepr89/BirdNET-Pi/wiki/Installation-Guide).
- Due to https://github.com/mcguirepr89/BirdNET-Pi/issues/1055 "Raspberry Pi OS (Legacy, 64-bit) Lite" must be selected during imaging.


## Usage
The system records and analyzes audio using BirdNET-Lite for bird identification and supports live streaming and BirdWeather integration.
Instructions for requesting a BirdWeather ID to join the BirdWeather network can be found in the installation guide.

Credits for the original inspiration and source for this project go to this [PixCams article](https://pixcams.com/building-a-birdnet-pi-real-time-acoustic-bird-id-station/).
Consider supporting BirdWeather by purchasing their official BirdWeather PUC [here](https://www.birdweather.com/).
