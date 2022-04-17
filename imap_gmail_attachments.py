import imaplib,email,smtplib
import os

detach_dir = '.'
if 'attachments' not in os.listdir(detach_dir):
    os.mkdir("attachments")

user='anil.macharla25@gmail.com'
pwd="ur password"
# imap_url='imap.gmail.com'
con= imaplib.IMAP4_SSL('imap.gmail.com')
con.login(user, pwd)
con.select('INBOX')
# type, data=con.uid('search', None, '(HEADER Subject "invoice")')
typ, data = con.search(None, '(SUBJECT "invoice")')
# type, data = con.search(None, 'ALL')
mail_ids = data[0]
# id_list = mail_ids.split()
for msgId in data[0].split():
    typ, messageParts = con.fetch(msgId, '(RFC822)')
    if typ != 'OK':
            print ('Error fetching mail.')
            raise

    emailBody = messageParts[0][1]
    # print(emailBody)
    
    mail = email.message_from_bytes(emailBody)
    for part in mail.walk():
            if part.get_content_maintype() == 'multipart':
                # print(part.as_string())
                continue
            if part.get('Content-Disposition') is None:
                # print (part.as_string())
                # print("done")
                continue
            fileName = part.get_filename()
            print('done')
            if bool(fileName):
                filePath = os.path.join(detach_dir, 'attachments', fileName)
                if not os.path.isfile(filePath) :
                    print (fileName)
                    fp = open(filePath, 'wb')
                    fp.write(part.get_payload(decode=True))
                    fp.close()
    
