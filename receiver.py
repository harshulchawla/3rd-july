import socket
import datetime

# Define log file name
log_file = "message_log.txt"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_add = "127.0.0.1"
port_no = 2525
complete_address = (ip_add, port_no)
s.bind(complete_address)

print("Hey, I'm receiving your message")
while True:
    # Receive a message from the sender (client)
    message, sender_address = s.recvfrom(100)
    
    # Decode the received message from bytes to string
    decrypted_message = message.decode('ascii')
    
    # Extract date and time from the received message
    message_parts = decrypted_message.split(': ', 1)
    if len(message_parts) == 2:
        received_time = message_parts[0]
        actual_message = message_parts[1]
        
        # Print the received message with date and time
        print(f"Received message at {received_time} from sender: {actual_message}")
        
        # Log the received message to a file
        with open(log_file, 'a') as f:
            f.write(f"Received at {received_time}: {actual_message}\n")
        
        # Prompt the user (receiver) to enter a response message
        response_message = input("Please write your response here: ")
        
        # Get current date and time for the response
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Append date and time to the response message
        response_with_time = f"{current_time}: {response_message}"
        
        # Encode the response message from string to bytes
        encrypted_response = response_with_time.encode('ascii')
        
        # Send the encoded response message back to the sender
        s.sendto(encrypted_response, sender_address)
        
        # Log the response message to a file
        with open(log_file, 'a') as f:
            f.write(f"Sent at {current_time}: {response_message}\n")
