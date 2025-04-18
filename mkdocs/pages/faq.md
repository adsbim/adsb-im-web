---
title: FAQ
hide:
  - navigation
---

# Frequently Asked Questions

??? question "What's your privacy and data policy?"
    It's simple—no data of yours is stored for more than 60 seconds. The full details are, of course, in our [Privacy Policy](privacy.md).

??? question "What hardware is supported?"
    See the [Supported Hardware page](supported-hw.md).

??? question "What about boards with 512MB like the Raspberry Pi 3 Model A+ or Pi Zero 2 W?"
    With current versions of the feeder image, 512MB is no longer a huge problem—you can feed several aggregators.
    However, the Raspberry Pi 3 and Pi Zero 2 tend to be less reliable than the Pi 4.
    If you plan to feed many account‑based aggregators, consider a [two stage setup](stage2.md).

??? question "How do I run this image?"
    There are several ways to run the image. If you just want to set up a simple feeder that connects to aggregators:
    
    - A Raspberry Pi 4 with 1G or 2G of memory is a good starting point.
    - The Raspberry Pi 3 can work but may cause occasional MLAT hiccups.
    - For boards with less than 1G of RAM or a slower CPU, a two‑stage setup might be best.
    
    Detailed guidance is available on our [Howto](howto.md) page.

??? question "Troubleshooting"
    First, check your power supply—this is the most common cause of issues.
    
    - A USB charger or cable from a powered hub is usually not enough.
    - Follow the instructions carefully—ensure you have a good power supply and a quality SD-card.
    
    If problems persist, try re-imaging your SD card, be patient on boot-up, and if still unresolved, ask for help on our [Discord channel](https://discord.gg/vqvJXRAkJ4) (`#adsb-dot-im`).

??? question "Running the Feeder Image in a VM"
    We provide an OVA for each release, which you can use with VMware, ProxMox, or other hypervisors.
    
    **Important:** When opening the OVA in VMware, you may receive an error on the first attempt. Click "Retry" to import successfully.
    
    Make sure to pass your SDR through to the VM—consult your hypervisor's documentation.
    
    Note: Running the feeder in a VM may cause MLAT issues due to USB passthrough challenges.

??? question "WiFi Support"
    WiFi is fully supported on Raspberry Pi boards and some DietPi‑based images (for example, for OrangePi boards).
    We strongly recommend setting up WiFi using the [Hotspot](hotspot.md) feature.

    ---

    :fontawesome-brands-youtube:{ style="color: #EE0F0F" }
    __[Setting up the ADS-B Feeder Image for WiFi, using the built-in hotspot]__ – :octicons-clock-24:
    1m – Learn how to set up WiFi for the ADSB.im image in a step-by-step guide.

    [Setting up the ADS-B Feeder Image for WiFi, using the built-in hotspot]: https://www.youtube.com/watch?v=-Q1B-g2kTf4

    ---

??? question "Can I run the ADS‑B Feeder and expose it directly to the internet?"
    The ADS‑B Feeder is designed to run within a local network behind a firewall. Many components of the system 
    would be unsafe if exposed directly to the Internet (for example, installing SSH keys without proper security).
    
    Please ensure your feeder is protected and not directly accessible from hostile networks.

??? question "How can I migrate to adsb.im from a different setup?"
    You can transfer your Sharing/API/Feeder Key/ID to adsb.im during the setup. Just note them down before switching off your current feeder. For various aggregators, use the following commands or steps:
    
    - **FlightAware:** `piaware-config -show feeder-id`
    - **FlightRadar24:** `cat /etc/fr24feed.ini | grep fr24key`
    - **RadarBox:** Either run `rbfeeder --showkey --no-start` or use `grep key= /etc/rbfeeder.ini`
    - **Plane.Watch:** Log into your account, go to "Feeders", and click the search icon next to your feeder.
    - **PlaneFinder:** Log into your account and check "Your Receivers" for your share code.
    - **ADSBHub:** Log into your account, click on your station's name under "Settings", and copy the station dynamic IP update ckey.
    - **OpenSky Network:** Log into your account and check for your receiver's serial number.
    - **RadarVirtuel:** Your feeder key will be emailed to you.
    - **1090MHz UK:** Your sharing key is emailed to you when you sign up.

??? question "How to set up Zerotier?"
    1. Create a Zerotier account and network via their [documentation website](https://docs.zerotier.com/).
    2. When you create the network, note the 16‑character hex string assigned to it.
    3. Enter that string on the expert page of the ADS‑B Feeder.
    4. After a few moments, accept the feeder on the Zerotier website and note its assigned IP.
    5. Set up Zerotier on any device you wish to use to access your feeder using the same network credentials.


    ---

    :fontawesome-brands-youtube:{ style="color: #EE0F0F" }
    __[Remotely connect to your ADS-B Feeder using Zerotier]__ – :octicons-clock-24:
    3m – Learn how to set up Zerotier for integration with the ADSB.im image in a step-by-step guide.

    [Remotely connect to your ADS-B Feeder using Zerotier]: https://www.youtube.com/watch?v=xlABhbnNrfI

    ---


??? question "How does this compare to running the ADS‑B feeder scripts from an aggregator directly on my system?"
    The ADS‑B Feeder Image is Docker‑based and runs a Python/Flask app for the web UI. This introduces some overhead compared to a minimal installation directly on the SBC OS.
    
    - **Pros:**  
      - Provides an easy-to-use interface.
      - Simplifies connection to multiple aggregators.
    
    - **Cons:**  
      - Uses slightly more memory than an optimized direct installation.
      
    For most users, the difference is minor, and the ease of use outweighs the added resource usage.