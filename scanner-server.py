#!/usr/bin/python3

from datetime import datetime
import asyncore
from smtpd import SMTPServer
import email

SMB_PATH = '/smb/scans/'

accepted_content_types = {
        'image/jpeg': 'jpg',
        'application/pdf': 'pdf'}

class ScannerServer(SMTPServer):
    no = 0
    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):

        msg = email.message_from_string(data)
        
        if msg.is_multipart():
            payload = msg.get_payload()

            for index in range(1, len(payload)):
                if payload[index].get_content_type() in list(accepted_content_types.keys()):
                    
                    filename = '%s_%d.%s' % ( 
                            datetime.now().strftime('%Y-%m-%d--%H-%M-%S'),
                            index,
                            accepted_content_types[payload[index].get_content_type()])

                    filename = SMB_PATH + filename

                    with open(filename, 'wb') as f:
                        f.write(payload[index].get_payload(decode=True))
                        print('MSG: Wrote file ' + filename)
                else:
                    print('ERROR: Message content was not an accepted type.')
        else:
            print('ERROR: Messgage was not multipart')


def run():
    scannerServer = ScannerServer(('192.168.1.4', 25), None)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    run()

