import socket
import cv2
import pyautogui
import numpy as np
import struct
import logging
import sys

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_client_socket(host_ip, port):
    """Create and return a connected client socket."""
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host_ip, port))
        logging.info(f"Connected to {host_ip}:{port}")
        return client_socket
    except Exception as e:
        logging.error(f"Failed to connect to {host_ip}:{port} - {e}")
        sys.exit(1)

def capture_screen():
    """Capture a screenshot and return it as a frame."""
    screen = pyautogui.screenshot()
    frame = np.array(screen)
    return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

def send_frame(client_socket, frame):
    """Encode the frame and send it over the socket."""
    try:
        _, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
        message = struct.pack(">L", len(buffer)) + buffer.tobytes()
        client_socket.sendall(message)
    except Exception as e:
        logging.error(f"Failed to send frame: {e}")
        client_socket.close()
        sys.exit(1)

def main():
    host_ip = '127.0.0.1'  # Use localhost
    port = 9999

    # Create a socket connection
    client_socket = create_client_socket(host_ip, port)
    
    try:
        while True:
            frame = capture_screen()
            send_frame(client_socket, frame)
    except KeyboardInterrupt:
        logging.info("Stopped by user.")
    finally:
        client_socket.close()
        logging.info("Connection closed.")

if __name__ == "__main__":
    main()
