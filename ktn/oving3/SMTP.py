from socket import *

# Message to send
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Our mail server is smtp.stud.ntnu.no
mailserver = 'smtp.stud.ntnu.no'

# Create socket called clientSocket and establish a TCP connection 
# (use the appropriate port) with mailserver
clientSocket = create_connection((gethostbyname(mailserver), 25))

recv = clientSocket.recv(1024)
print recv
if recv[:3] != '220':
  print '220 reply not received from server.'

def sendPrintResponse(msg):
  clientSocket.send(msg)
  recv1 = clientSocket.recv(1024)
  print 'Sent: %s\nReceived: %s' % (msg.strip(), recv1.strip())
  if recv1[:3] != '250' and recv1[:3] != '354' and recv1[:3] != '221':
    print '250 reply not received from server.'

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
sendPrintResponse(heloCommand)

# Send MAIL FROM command and print server response.
sendPrintResponse('MAIL FROM:<such@ntnu.no>\r\n')


# Send RCPT TO command and print server response.
sendPrintResponse('RCPT TO:<aajonass@stud.ntnu.no>\r\n')

# Send DATA command and print server response.
sendPrintResponse('DATA\r\n')

# Send message data.
clientSocket.send("""Date: Thu, 21 May 2008 05:33:29 -0700
From: Such KTN <such@wow.no>
Subject: KTN is a lot of fun
To: aajonass@stud.ntnu.no

Hei Alexander,
KTN er kjempemoro
//Such Wow
""")
print('Message data sent!')

# Message ends with a single period.
sendPrintResponse('\r\n.\r\n')

# Send QUIT command and get server response.
sendPrintResponse('QUIT\r\n')
