import cv2
import requests
import numpy as np
import serial
import time

def fetch_map_image(lat, lon, zoom=15, map_type='roadmap', api_key=' ', path=None):
    """Fetches an image from Google Static Maps API with an optional path."""
    base_url = "https://maps.googleapis.com/maps/api/staticmap?"
    path_param = ''
    if path:
        path_str = '|'.join([f"{p[0]},{p[1]}" for p in path])
        path_param = f"&path=color:red|weight:2|{path_str}"
    url = f"{base_url}center={lat},{lon}&zoom={zoom}&size=600x400&maptype={map_type}{path_param}&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        image = np.array(bytearray(response.content), dtype=np.uint8)
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        if image is None:
            print("Failed to decode image.")
        return image
    else:
        print(f"Failed to fetch image, HTTP status code: {response.status_code}")
        return None

def display_map(image, latest_coord, coords):
    """Displays the image using OpenCV and overlays current coordinates."""
    if image is not None:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = f"Latitude: {latest_coord[0]:.5f}, Longitude: {latest_coord[1]:.5f}"
        (text_width, text_height), _ = cv2.getTextSize(text, font, 0.7, 1)
        top_left_corner = (10, image.shape[0] - 30)
        bottom_right_corner = (10 + text_width, image.shape[0] - 10)
        cv2.rectangle(image, top_left_corner, bottom_right_corner, (50, 50, 50), -1)
        cv2.putText(image, text, (10, image.shape[0] - 10), font, 0.7, (0, 255, 0), 2, cv2.LINE_AA)

        for i, coord in enumerate(coords):
            x, y = lat_lon_to_pixel(coord[0], coord[1], image.shape, latest_coord)
            if i == len(coords) - 1:
                cv2.circle(image, (x, y), 5, (0, 0, 255), -1)  # Larger dot for the latest point
            else:
                cv2.circle(image, (x, y), 2, (255, 255, 0), -1)  # Smaller dots for previous points
        
        cv2.imshow('Google Map', image)
        cv2.waitKey(1)
    else:
        print("No image to display.")

def read_serial(comport, baudrate):
    coords = []
    try:
        ser = serial.Serial(comport, baudrate, timeout=1)
        print(f"Connected to {comport} at {baudrate} baud. Press Ctrl+C to stop.")
        while True:
            data = ser.readline().decode().strip()
            if data:
                lat, lon = float(data[5:12]) / 100000, float(data[21:31]) / 10000000
                coords.append((lat, lon))
                image = fetch_map_image(lat, lon, path=coords)
                display_map(image, (lat, lon), coords)

    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()
        print("Serial port closed.")
        cv2.destroyAllWindows()

def lat_lon_to_pixel(lat, lon, image_shape, latest_coord):
    # This function needs to be adjusted to map latitude and longitude to pixel coordinates correctly
    x = int((lon - latest_coord[1]) * 4000000 + image_shape[1] / 2)
    y = int((latest_coord[0] - lat) * 4000000 + image_shape[0] / 2)
    return x, y

if __name__ == '__main__':
    read_serial('COM7', 115200)
