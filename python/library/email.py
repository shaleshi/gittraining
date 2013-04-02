#import pdb;pdb.set_trace()
#from email.message import Message
#from email.header import Header
#msg = Message()
#h = Header('p\xf6stal', 'iso-8859-1')
#msg['Subject'] = h
#print msg.as_string()
# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
fp = open(textfile, 'rb')
# Create a text/plain message
msg = MIMEText(fp.read())
fp.close()

me == 'hsadashiv@zeomega.com' #the sender's email address
you == 'hsadashiv@zeomega.com' #the recipient's email address
msg['Subject'] = 'The contents of %s' % textfile
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP()
s.sendmail(me, [you], msg.as_string())
s.quit()
#json  JSON encoder and decoder
import json
#mailcap  Mailcap file handling
import mailcap
#mhlib  Access to MH mailboxes
import mhlib
#mimetools  Tools for parsing MIME messages
import mimetools
#mimetypes  Map filenames to MIME types
import mimetypes
#MimeWriter  Generic MIME file writer
import MimeWriter
#mimify  MIME processing of mail messages
import mimify
#multifile  Support for files containing distinct parts
import multifile
#rfc822  Parse RFC 2822 mail headers
import rfc822
#base64 =  RFC 3548: Base16, Base32, Base64 Data Encodings
#binhex  Encode and decode binhex4 files
#binascii  Convert between binary and ASCII
#quopri  Encode and decode MIME quoted-printable data
#uu  Encode and decode uuencode files
