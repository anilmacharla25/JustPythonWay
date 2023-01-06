import imaplib
import sys

# Connect to the server and log in #993
imap_server = imaplib.IMAP4('mail server ip')
obj=imap_server.login('amacharla@mds.com', 'pwd')
print(obj)

# Select the INBOX and search for unread messages
imap_server.select()
status, messages = imap_server.search(None, 'SEEN')

# Split the list of message IDs into a list
message_ids = messages[0].split()

# Fetch the subject lines for the unread messages
for message_id in message_ids:
    status, data = imap_server.fetch(message_id, '(BODY[HEADER.FIELDS (SUBJECT)])')
    subject = data[0][1]
    subject=subject.decode('utf-8')
    
    print(subject)

# Log out and close the connection
imap_server.logout()
