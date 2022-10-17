from __future__ import print_function
from datetime import datetime
import asyncore
from smtpd import SMTPServer
import sys

class EmlServer(SMTPServer):
    no = 0
    def process_message(self, peer, mailfrom, rcpttos, data):
        filename = '%s-%d.eml' % (datetime.now().strftime('%Y%m%d%H%M%S'),
                self.no)
        f = open(filename, 'w')
        f.write(data)
        f.close
        print('%s saved.' % filename)
        self.no += 1


def run():
    # start the smtp server on localhost:1025
    foo = EmlServer(('192.168.1.3', 25), None)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    print(sys.getsizeof(run))