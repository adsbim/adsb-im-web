---
title: Downloads
hide:
  - navigation
---

# Downloads

There are three principal ways to use this software:

1. Using one of the fully integrated images.
2. Using it as an integrated app on any DietPi system.
3. Using it as a standalone application that can be installed on most Debian-based systems.

This page is trying to point you at the right image to install if you want to take the first approach. Initially this project supported a large number of SBCs, but it turned out that almost everyone was running the software on a Raspberry Pi, with some using x86 virtualization (which does cause issues with MLAT for most users). Due to this, the number of images offered has gone down accordingly.

Note: Only use the configuration options from various *imaging* programs on images that support this (which usually is only the Raspbian images).

At this point we offer the following images:

<div class="grid cards" markdown>

-   __Raspberry Pi__

    ---

    [Raspbian based image for all 64bit capable Raspberry Pi](https://github.com/dirkhh/adsb-feeder-image/releases/download/{latest_release}/adsb-im-raspberrypi64-pi-2-3-4-5-{latest_release}.img.xz){ .md-button }

-   __Libre Computing LePotato__

    ---

    [Raspbian image for Libre Computing LePotato](https://github.com/dirkhh/adsb-feeder-image/releases/download/{latest_release}/adsb-im-lepotato-{latest_release}.img.xz){ .md-button }  
    [Armbian based image for Libre Computing LePotato (no WiFi support)](https://github.com/dirkhh/adsb-feeder-image/releases/download/{latest_release}/adsb-im-lepotato-raspbian-{latest_release}.img.xz){ .md-button }

-   __Odroid__

    ---

    [Armbian based image for Odroid C4](https://github.com/dirkhh/adsb-feeder-image/releases/download/{latest_release}/adsb-im-odroidc4-{latest_release}.img.xz){ .md-button }  
    [Armbian based image for Odroid xu4](https://github.com/dirkhh/adsb-feeder-image/releases/download/{latest_release}/adsb-im-odroidxu4-{latest_release}.img.xz){ .md-button }

-   __NanoPi__

    ---

    [DietPi based image for NanoPi NEO3](https://github.com/dirkhh/adsb-feeder-image/releases/download/{latest_release}/adsb-im-nanopi-neo3-dietpi-{latest_release}.img.xz){ .md-button }

-   __Orange Pi__

    ---

    [DietPi based image for Orange Pi 3 LTS](https://github.com/dirkhh/adsb-feeder-image/releases/download/{latest_release}/adsb-im-orangepi-3lts-dietpi-{latest_release}.img.xz){ .md-button }  
    [DietPi based image for Orange Pi Zero 3](https://github.com/dirkhh/adsb-feeder-image/releases/download/{latest_release}/adsb-im-orangepi-zero3-dietpi-{latest_release}.img.xz){ .md-button }  
    [DietPi based image for Orange Pi 5 Plus](https://github.com/dirkhh/adsb-feeder-image/releases/download/{latest_release}/adsb-im-orangepi-5plus-dietpi-{latest_release}.img.xz){ .md-button }

-   __x86-64 Systems__

    ---

    [DietPi based image for installation directly on x86-64 systems ("native")](https://github.com/dirkhh/adsb-feeder-image/releases/{latest_release}){ .md-button }

-   __x86-64 Virtual Machines__

    ---

    [VirtualBox (also works with VMware)](https://github.com/dirkhh/adsb-feeder-image/releases/download/{latest_release}/adsb-im-x86-64-vm-{latest_release}-VirtualBox-x86_64.ova.xz){ .md-button }  
    [Proxmox](https://github.com/dirkhh/adsb-feeder-image/releases/download/{latest_release}/adsb-im-x86-64-vm-{latest_release}-proxmox.tar.xz){ .md-button }  
    [Hyper-V](https://github.com/dirkhh/adsb-feeder-image/releases/download/{latest_release}/adsb-im-x86-64-vm-{latest_release}-Hyper-V-x86_64.vhdx.xz){ .md-button }

</div>

!!! warning "Note for ProxMox Users"
    Please see the instructions in the [ProxMox section](https://github.com/dirkhh/adsb-feeder-image?tab=readme-ov-file#for-advanced-users-wanting-to-run-this-image-on-x86-under-proxmox) of the README for details.

    ---

    :fontawesome-brands-youtube:{ style="color: #EE0F0F" }
    __[Adding an SDR to your ADS-B Feeder under Proxmox]__ – :octicons-clock-24:
    1.5m – Learn how to map your SDR to your ADS-B guest in a way that improves your chances of success.

    [Adding an SDR to your ADS-B Feeder under Proxmox]: https://www.youtube.com/watch?v=awr8wOI0Txg

    ---

!!! note
    
    The x86-64 images generally assume BIOS systems and have not been tested—or are unlikely to work—in UEFI environments. The VM images also assume SATA disks.

<script type="text/javascript">
window.addEventListener('load', function() {
    fetch('https://api.github.com/repos/dirkhh/adsb-feeder-image/releases/latest')
      .then(function(response) {
          return response.json();
      })
      .then(function(data) {
          const latestTag = data.tag_name;
          const anchors = document.querySelectorAll('a[href*="{latest_release}"]');
          anchors.forEach(function(anchor) {
              const rawHref = anchor.getAttribute('href');
              const newHref = rawHref.replace(/{latest_release}/g, latestTag);
              anchor.setAttribute('href', newHref);
          });
      })
      .catch(function(error) {
          console.error('Error fetching latest release:', error);
      });
});
</script>
