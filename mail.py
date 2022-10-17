import smtplib

SERVER = "localhost"

FROM = "gintaku@gintaku.xyz"
TO = ["gintaku@gintaku.xyz"] # must be a list

SUBJECT = "Hello!"

TEXT = "This message was sent with Python's smtplib."

# Prepare actual message

message = "hellllllllllllloooooooooooo"

# Send the mail

server = smtplib.SMTP('192.168.1.2:25')
server.login('gintaku@gintaku.xyz','kagura12')
server.sendmail(FROM, TO, message)
server.quit()