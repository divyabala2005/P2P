import socket
import os

# Function to send a file to the receiver
def send_file(filename, receiver_ip, receiver_port):
    # Create socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the receiver
    s.connect((receiver_ip, receiver_port))
    
    # Get the file size
    file_size = os.path.getsize(filename)
    s.send(f"{filename}|{file_size}".encode())

    # Open file to send
    with open(filename, 'rb') as file:
        while True:
            # Read the file in chunks of 1024 bytes
            data = file.read(1024)
            if not data:
                break  # End of file
            s.send(data)

    print(f"File {filename} has been sent successfully!")
    s.close()

# Main function to take user input for file transfer
def main():
    receiver_ip = input("Enter receiver's IP address: ")
    receiver_port = int(input("Enter receiver's port number: "))
    filename = input("Enter the file name to send: ")

    # Call the send file function
    send_file(filename, receiver_ip, receiver_port)

if __name__ == "__main__":
    main()
