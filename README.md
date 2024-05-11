# Map Visualization with OpenCV and Google Static Maps API

This Python script provides real-time map visualization by reading GPS coordinates from a serial device and displaying them on a map fetched from the Google Static Maps API using OpenCV. The coordinates are plotted on the map, which updates dynamically as new data is received.

## Setup (Arduino & Sensor)

# Arduino (SDA & SCL connections)

![WhatsApp Image 2024-05-11 at 14 33 56_aaec9670](https://github.com/ZoreAnuj/GPS-RTK-Sparkfun-/assets/95142805/520ab4ab-4bf2-4e54-b800-635250e664e7)

# Antenna and Tripod

![WhatsApp Image 2024-05-11 at 14 33 55_aea2ba09](https://github.com/ZoreAnuj/GPS-RTK-Sparkfun-/assets/95142805/4e61700c-4985-4442-8c2c-b4ae63c848d1)

## Requirements

- Python 3.x
- OpenCV-Python
- NumPy
- Requests
- PySerial

Install the required Python packages using pip:

```bash
pip install opencv-python numpy requests pyserial
