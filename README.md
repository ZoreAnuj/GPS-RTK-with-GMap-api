# Map Visualization with OpenCV and Google Static Maps API

This Python script provides real-time map visualization by reading GPS coordinates from a serial device and displaying them on a map fetched from the Google Static Maps API using OpenCV. The coordinates are plotted on the map, which updates dynamically as new data is received.

## Results:

![image](https://github.com/ZoreAnuj/GPS-RTK-Sparkfun-/assets/95142805/15adb7e0-8cdb-4d76-8eb3-fa3e4bb82a18)


## Setup (Arduino & Sensor)

# Arduino (SDA & SCL connections)

![WhatsApp Image 2024-05-11 at 14 33 56_aaec9670](https://github.com/ZoreAnuj/GPS-RTK-Sparkfun-/assets/95142805/3c446e95-d004-4406-a0cb-b44a40316a63)


# Antenna and Tripod

![WhatsApp Image 2024-05-11 at 14 33 55_aea2ba09](https://github.com/ZoreAnuj/GPS-RTK-Sparkfun-/assets/95142805/35a5962a-1e98-4e91-80d6-54abc5074381)


## Requirements

- Python 3.x
- OpenCV-Python
- NumPy
- Requests
- PySerial

Install the required Python packages using pip:

```bash
pip install opencv-python numpy requests pyserial
Triggering update for day: Fri Mar  7 01:10:03 UTC 2025
Triggering update for day: Wed Mar 12 00:56:51 UTC 2025
Triggering update for day: Thu Mar 20 01:20:10 UTC 2025
Triggering update for day: Mon Mar 24 01:22:30 UTC 2025
Triggering update for day: Sun Mar 30 00:53:38 UTC 2025
Triggering update for day: Thu Apr 24 01:24:51 UTC 2025
Triggering update for day: Sun Apr 27 00:54:41 UTC 2025
Triggering update for day: Fri May  2 01:14:47 UTC 2025
Triggering update for day: Thu May 15 01:25:22 UTC 2025
Triggering update for day: Sun May 18 00:56:48 UTC 2025
Triggering update for day: Wed May 21 01:03:21 UTC 2025
Triggering update for day: Thu Jun  5 01:37:20 UTC 2025
Triggering update for day: Fri Jun  6 01:17:18 UTC 2025
Triggering update for day: Sun Jun 15 00:59:50 UTC 2025
Triggering update for day: Tue Jun 17 01:11:59 UTC 2025
Triggering update for day: Sat Jun 28 01:13:16 UTC 2025
Triggering update for day: Mon Jun 30 01:43:11 UTC 2025
Triggering update for day: Tue Jul  1 01:20:15 UTC 2025
Triggering update for day: Fri Jul  4 01:18:58 UTC 2025
Triggering update for day: Thu Jul 10 01:41:44 UTC 2025
Triggering update for day: Fri Jul 11 01:21:45 UTC 2025
Triggering update for day: Sat Aug  2 01:17:43 UTC 2025
Triggering update for day: Thu Aug  7 01:49:19 UTC 2025
Triggering update for day: Sun Aug 17 00:59:27 UTC 2025
Triggering update for day: Mon Aug 18 01:45:09 UTC 2025
Triggering update for day: Tue Aug 19 01:10:00 UTC 2025
Triggering update for day: Tue Aug 26 01:08:53 UTC 2025
Triggering update for day: Sun Aug 31 00:54:08 UTC 2025
Triggering update for day: Mon Sep  8 01:24:24 UTC 2025
Triggering update for day: Sun Sep 14 00:52:34 UTC 2025
Triggering update for day: Tue Sep 23 01:03:29 UTC 2025
Triggering update for day: Tue Oct  7 01:04:25 UTC 2025
