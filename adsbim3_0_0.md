adsb.im 3.0 Documentation
Top Left Header

Home [ADS-B Feeder text]
Map [Button]
ACARS [Button]
AIS [Button]
HFDL [status unknown]
Sonde [status unknown]
VDL Mode 2 [status unknown]

Top Right Menu

# Target (for maps/sharing)
## Combined
## XX (XX is the feeder number)
# Maps
## Live Traffic
### [add blurb about what this shows and how it works]
## Heatmap
### [add blurb about what this shows and how it works]
## Tracks
### [add blurb about what this shows and how it works]
## Replay
### [add blurb about what this shows and how it works]
## Options
### Apply Settings - Take Me To The Feeder Homepage
### Apply Settings - Take Me To This Map
### Use Route API to show flight routes when known.
### HeyWhat'sThat is an incredibly cool web service that allows you to discover what you should be able to see from the location of your antenna - including estimates for how far away you should be able to detect planes (depending on their altitude - and assuming there are no other obstructions).
### The tar1090 map maintains an outline for the area around your feeder where planes have been observed; sometimes it may be desirable to reset that (for example after you changed location). Select the checkbox and submit below to clear that range outline.
## ACARS Hub
### links directly to ACARS Hub interface
## AIS Catcher
### links directly to AIS interface
# Data Sharing
## Select the ACARS (including VDL2 / HFDL) aggregators you want to feed:
### Airframes.io is an unbiased and unfiltered transportation aggregation service for data sources such as ACARS, VDL, HFDL, and SATCOM. Most people interested in tracking this kind of data want to feed this aggregator.
### AcarsDrama is a rather different type of aggregator. They are mainly focused on picking out things that are funny (or drama) from the large amount of ACARS data that's available. The volunteers behind AcarsDrama request that you please send email to them to let them know that you are feeding them data and give them an approximate location of your feeder.
### adsb.lol is focused on dumping the raw data into a publicly available github repository.
### AVDelphi is another aggregator for ACARS data. Note that you need to claim your feed on their website before you are allowed to feed them.
## Select the AIS aggregators you want to feed:
### Airframes.io is an unbiased and unfiltered transportation aggregation service that also supports AIS.
### AIS Catcher is a community of AIS enthusiasts dedicated to maritime tracking.  Get a Sharing Key by registering your station.  2e72bbde-45eb-4eaa-9b36-6e456b30b482
### AIS Friends is volunteer AIS network aggregating data.
### AISHub is a free AIS data sharing community.
### HPRadar is a free aggregator for AIS (and ADS-B) data.
### sdrmap is a German community aggregator for AIS (and ADS-B) data.
### MarineTraffic is is a British commercial aggregator for AIS data.
### MyShipTracking is is a Greek commercial aggregator for AIS data.
### pocketmariner / BoatBeacon is a British commercial AIS data sharing company.
### shipfinder is a British commercial aggregator for AIS data and pictures.
### ShippingExplorer is a Spanish commercial aggregator for AIS data.
### ShipXplorer is a US commercial aggregator for AIS data, part of AirNav Radar.
### VesserFinder is is a Bulgarian commercial aggregator for AIS data.
	
# Setup
## Basic
### If you are re-installing the ADS-B Feeder Image and have made a backup of your configuration, you can also simply restore those settings. [RESTORE PREVIOUS BACKUP Button]

### Station Name (shows up on public maps if enabled later)
### Latitude (-90 .. +90 -- please use 5 decimals, e.g. 45.12345)
### Longitude (-180 .. +180 -- please use 5 decimals , e.g. -122.12345)
### Altitude above mean sea level, rounded to whole meters

### Timezone [UPDATE TIMEZONE Button]
### ADS-B: Which account-less aggregators do you want to feed? There is a separate data sharing page for aggregators that require an account. 
### If you only want to share ACARS / AIS / SONDE data, please check "None (no ADS-B)" 
### All 
### Aggregators with privacy policy 
### Pick individually None (micro feeder) 
### None (nano feeder) 
### None (no ADS-B) 
### Stage 2 setup (select these later)
### With this option the image will be set up as a micro feeder, minimizing memory use and disabling many features. This is designed to work with a second stage image that uses this feeder as its input and creates the map, feeds the aggregators, etc.
## SDR
### [CHECK SDRS Button]
#### Type
#### Serial
#### Use For
#### Gain
#### biastee
### [TOGGLE LSUSB OUTPUT Button]
#### If needed, you can change the serial number of an RTLSDR on a separate page. Please do that before making assignments as those are tracked by serial number.
## Expert
### Additional Ultrafeeder Arguments
### Add Arguments To Map URLs
### Don’t Show Config Link On Map Page
### Docker Pull: Disable Concurrent Downloads
### Enable NON-ADS-B Containers
#### First ACARS
#### Second ACARS
#### VDL Mode 2
#### 
#### hfdlobserver
#### acars2pos
#### AIS / Shipfeeder
#### Show Ships on ADS-B Map
#### adio Sonde
### Add Environment Variables To Containers
### DHT22 Temperature Sensor
### CSS Theme
# System
## Logs
### Dozzle
## Support Info
### Please cut and paste (or provide a screenshot of) this data when asking for help.
### Current: v3.0.0
### Board: 
### Base: 
### Kernel: 
### Power: 
### Journal: 
### DNS: 
### IPv6: 
### Netdog reboots: Network/IP: 
### Containers:
#### SDR(s):
#### SDR(type: 'rtlsdr' address: '003:002', serial: 'acarshub', purpose: 'acars', gain: '-10', biastee: False)
#### SDR(type: 'rtlsdr' address: '001:003', serial: 'aiscatcher', purpose: 'ais', gain: 'auto', biastee: False)
#### SDR(type: 'airspy' address: '001:002', serial: '35AC63DC2D95364F', purpose: '1090', gain: 'auto', biastee: True)
### Ultrafeeder args:
### Env variables:
### Memory:
### Storage:
### Top:
## Share Diagnostics
### This will create an anonymized log that removes IP addresses, locations, and any aggregator keys and other secrets from your logs and upload them to a website for easier sharing with the developers.
### After you click the button, this will display a link that you can share on one of the support forums (and that you can review first to make sure no personal data is included).
### Please note, we offer multiple ways to upload these because the services tend to not reliably work from every location and at all times. So if you get an error, please try one of the other options.
#### [UPLOAD LOGS TO 0X0.ST (CURL POST) Button]
#### [UPLOAD LOGS TO TERMBIN.COM (NETCAT) Button]
#### [DOWNLOAD LOGS Button]
#### [VIEW LOGS Button]
### For help and questions, please go to the adsb-feeder-image Zulip channel or (if you prefer Discord) the #adsb-dot-im channel on this Discord server.
## Management
### Install SSH Credentials
### Secure Feeder System
### System Log Persistence Toggle
### Update Feeder Software
### Add Zerotier
### Reconfigure WiFi
### Generate New Root Password
### Shutdown/Reboot
### System Update Settings
### Restart / Recreate Containers
### Add Tailscale
## Backup
### Config Backup: creates a zip file with your configuration settings Config + Graphs Backup: adds the data used to generate the statistical graphs (roughly +15MB) Full Backup: adds on top of all that the replay / heatmap data
### Depending on the amount of historic replay / heatmap data you have, a Full Backup can take a signficant amount of time and result in a very large archive to be downloaded. If you want to limit the data retained on disk, you can use MAX_GLOBE_HISTORY=365 in the environment variables on the expert page to only retain a year of data, this setting will not impact graph data.
### [Config Backup Button]
### [Config + Graphs Backup Button]
### [Full Backup Button]
## Restore
### If you have a configuration backup file, please upload it here:
### [Upload Button]
## Stats
### ADS-B Message Rate
### ADS-B Aircraft Seen / Tracked
### ADS-B Tracks Seen
### ADS-B Range
### ADS-B Signal Level
### ADS-B Maxima
### ADS-B Message Rate / Aircraft
### ADS-B CPU Utilization
### Airspy RSSI
### Airspy SNR
### Airspy Noise
### Airspy Misc
### DF Counts
### Overall CPU Utilization
### Maximum Temperature
### Memory Utilization
### Bandwidth Usage (wireless & ethernet)
### Disk Usage ( / )
### Disk I/O - IOPS
### Disk I/O - Bandwidth
