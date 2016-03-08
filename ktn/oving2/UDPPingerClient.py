import time
from socket import *

# Get the server hostname and port as command line arguments                    
host = 'localhost'
port = 12000
timeout = 1

# Create UDP client socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Note the second parameter is NOT SOCK_STREAM
# but the corresponding to UDP

# Set socket timeout as 1 second
clientSocket.settimeout(timeout)

# Sequence number of the ping message
ptime = 0

# Ping for 10 times
print('Pinging 10 times!')
while ptime < 10:
    ptime += 1
    # Format the message to be sent as in the Lab description  
    data = 'Ping %d %s' % (ptime, time.ctime())

    try:
      # FILL IN START

      # Record the "sent time"
      sent = time.time() # This is the current time in seconds

      # Send the UDP packet with the ping message
      clientSocket.sendto(data,(host, port))

      # Receive the server response
      modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

      # Record the "received time"
      received = time.time()

      # Round trip time is the difference between sent and received time
      rtt = received - sent

      # Display the server response as an output
      print('Received %s after %r ms' % (modifiedMessage, rtt/1000)) # Converting seconds to milliseconds by dividing by 1k


      # FILL IN END
    except:
        # Server does not response
        # Assume the packet is lost

        print "Request timed out."
        continue

# Close the client socket
clientSocket.close()
