import socket
import os

# Function to receive the file
def receive_file(receiver_port):
    # Create socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind socket to IP and port
    s.bind(('0.0.0.0', receiver_port))
    s.listen(1)
    print(f"Listening for incoming connections on port {receiver_port}...")
    
    # Accept a connection
    client_socket, client_address = s.accept()
    print(f"Connection from {client_address} established!")

    # Receive the file info (filename and size)
    file_info = client_socket.recv(1024).decode()
    filename, file_size = file_info.split('|')
    file_size = int(file_size)

    # Open the file to write the received data
    with open(filename, 'wb') as file:
        bytes_received = 0
        while bytes_received < file_size:
            data = client_socket.recv(1024)
            file.write(data)
            bytes_received += len(data)

    print(f"File {filename} received successfully!")
    client_socket.close()

# Main function to start receiving the file
def main():
    receiver_port = int(input("Enter the port number to listen on: "))
    receive_file(receiver_port)

if __name__ == "__main__":
    main()
