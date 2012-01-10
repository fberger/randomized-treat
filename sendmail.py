#!/usr/bin/env python

from email.mime.text import MIMEText
import logging
import os
import smtplib

import settings

logging.basicConfig(level=logging.INFO,
                    filename=os.path.join(settings.CWD, 'treat.log'),
                    format='%(asctime)s %(message)s' )

def main(email, treat):
    logging.info('Sending treat "%s" to %s', treat, email)
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(settings.EMAIL_SENDER_ADDRESS, settings.EMAIL_SENDER_PASSWORD)
    message = MIMEText('Enjoy your %s.' % treat)
    message['Subject'] = 'Treat granted!'
    smtp.sendmail(settings.EMAIL_SENDER_ADDRESS, email, message.as_string())

if __name__ == '__main__':
    import sys
    main(*sys.argv[1:])
