#!/usr/bin/env python

import logging
import os
import random
import subprocess

import settings

logging.basicConfig(level=logging.INFO,
                    filename=os.path.join(settings.CWD, 'treat.log'),
                    format='%(asctime)s %(message)s' )

def main(email, treat, probability, delay):
    logging.info('Determining treat grant')
    if random.random() > float(probability):
        logging.info('No %s for %s', treat, email)
        return
    delay = int(random.uniform(0, int(delay)))
    logging.info('%s will get %s  with a %s minute delay', email, treat, delay)
    command = ['at', 'now', '+', str(delay), 'min']
    at_process = subprocess.Popen(command, stdin=subprocess.PIPE)
    print >> at_process.stdin, 'sendmail.py %s %s' % (email, treat)
    at_process.stdin.close()

if __name__ == '__main__':
    import sys
    main(*sys.argv[1:])
