import cv2
import socket
import numpy as np
import struct

def receive_all(sock, count):
    """Receive the exact number of bytes from the socket."""
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf:
            return None
        buf += newbuf
        count -= len(newbuf)
    return buf

def setup_server_socket(host_ip, port):
    """Setup and bind the server socket."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host_ip, port))
    server_socket.listen(5)
    print(f"Listening at {host_ip}:{port}")
    return server_socket

def handle_client_connection(client_socket):
    """Handle the client connection and display the received frames."""
    cv2.namedWindow('Received', cv2.WINDOW_NORMAL)  # Initialize window
    
    try:
        while True:
            # Receive the size of the incoming message
            message_size = receive_all(client_socket, struct.calcsize(">L"))
            if not message_size:
                break
            
            message_size = struct.unpack(">L", message_size)[0]
            # Receive the frame data
            frame_data = receive_all(client_socket, message_size)
            if not frame_data:
                break

            # Convert the byte data into a numpy array and decode the image
            frame = np.frombuffer(frame_data, dtype=np.uint8)
            frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)

            # Display the received image
            cv2.imshow('Received', frame)

            # If 'q' is pressed, exit the loop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        cv2.destroyAllWindows()

def main():
    host_ip = '0.0.0.0'  # Listens on all network interfaces
    port = 9999

    # Set up server socket
    server_socket = setup_server_socket(host_ip, port)

    try:
        while True:
            # Accept a new client connection
            client_socket, addr = server_socket.accept()
            print(f"Connection from: {addr}")
            handle_client_connection(client_socket)
    except KeyboardInterrupt:
        print("Server stopped by user.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
