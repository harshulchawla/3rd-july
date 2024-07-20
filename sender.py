import socket
import datetime

# Define log file name
log_file = "message_log.txt"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
target_ip = "127.0.0.1"
port_no = 2525 
target_add = (target_ip, port_no)

condition = True
while condition:
    message = input("Please write your message here: ")
    
    # Get current date and time
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Append date and time to the message
    message_with_time = f"{current_time}: {message}"
    
    # Log the message to a file
    with open(log_file, 'a') as f:
        f.write(f"Sent at {current_time}: {message}\n")
    
    encrypt_message = message_with_time.encode('ascii')
    s.sendto(encrypt_message, target_add)

    # Receive a response from the server (receiver)
    response, server_address = s.recvfrom(100)
    
    # Decode and print the received response
    decrypted_response = response.decode('ascii')
    print(decrypted_response)
    
    # Log the response to a file
    with open(log_file, 'a') as f:
        f.write(f"Received at {current_time}: {decrypted_response}\n")
