#
from gevent import socket
import gevent
import sys
from gevent import monkey;
monkey.patch_select()
monkey.patch_sys()

import select
import string 
import random
import logging

def raw_input2(message):
    #sys.stdout.write(message)

    #select.select([sys.stdin], [], [])
    #return sys.stdin.readline()
    return raw_input()

def MethodWrap(*types):
    def M1(f):
        def NEWF(*args):
            if len(types)==len(args):
                raise 
            pass
        return NEWF
    return M1 
class MyClient(object):
    def __init__(self):
        self.sock = gevent.socket.create_connection(('192.168.12.21',6000))
        self.userinputstr = ''
        pass
    
    def helloWorld(self):
        
        pass
    def getinput(self):
        k = 0
        while 1:
            #self.userinputstr = raw_input2('')
            k+=1
            self.sock.send('%d,%s\n'%(k,raw_input()))

    def loop(self):
        pre = 0
        cur = 0
        while 1:
            #gevent.sleep(1)
            #gevent.spawn(self.worker)
            #raw_input
            data = self.sock.recv(1024)
            if data:
                print 'data:%s,len:%d\n'%(data,len(data))
                try :
                    cur = string.atoi(data)
                    print 'diff:%d'%(cur-pre,)
                    pre = cur
                except Exception,e:
                    pass

from tcpServer import TestProtocolException,TestProtocol,RPCSocket

class SocketRPCClient(object):
    """ RPClient for the above Server.
        Automaticaly reconnects to the target server (with "reconnect=True") 
        but looses any results which hasn't been transfered on reconnect.
    """

    ## START Reconnecting feature,
    # shameless borrowed from 
    # twisted.i.p.ReconnectingClientFactory (Rene)
    maxDelay = 3600
    initialDelay = 1.0
    factor = 2.7182818284590451
    jitter = 0.11962656472

    delay = initialDelay
    retries = 0
    maxRetries = None

    continueTrying = True
    isTrying = False
    ## END Reconnecting

    def __init__(self, address, rpctype,prototype, timeout=None, source_address=None, reconnect=False):
        self.sock_args = [address, timeout, source_address]
        self.rpctype=rpctype
        self.prototype=prototype
       

        self.continueTrying = reconnect

       

        # Start connecting
        self.connect()
    def main_loop(self):
        gevent.event.Event().wait()
    def connect(self):
        # Protocol specific
        try:
            self.socket = gevent.socket.create_connection(*self.sock_args)
            self.rpc = self.rpctype(self.prototype,self.socket)
            
            self.address = self.socket.getpeername()

            gevent.spawn(self.rpc._read)
        except Exception, e:
            print e
            self.connection_failed(e)

    def connection_failed(self, reason):
        #logging.error('Connection to %s:%s failed: %s' % (self.sock_args[0][0], self.sock_args[0][1], reason))

        if self.continueTrying and not self.isTrying:
            self._retry()

    def connection_made(self):
        logging.info('Connected to %s:%s' % self.address)

    def connection_lost(self):
        logging.info('Lost connection to %s:%s' % self.address)

        if self.continueTrying and not self.isTrying:
            self._retry()
    
    def helloworld(self):
        return self.rpc.helloto_c().get()
    def _retry(self):
        self.isTrying = True

        if self.connected.is_set():
            self.isTrying = False
            self.delay = self.initialDelay
            self.retries = 0

            if self.debug:
                logging.debug("Successfully reconnected to %s:%s" % self.sock_args[0])
            return

        if not self.continueTrying:
            if self.debug:
                logging.debug("Abandoning connecting to %s:%s on explicit request" % self.sock_args[0])
            return

        self.retries += 1
        if self.maxRetries is not None and (self.retries > self.maxRetries):
            if self.debug:
                logging.debug("Abandoning %s:%s after %d retries." % (self.sock_args[0][0], self.sock_args[0][1], self.retries))
            return

        self.delay = min(self.delay * self.factor, self.maxDelay)
        if self.jitter:
            self.delay = random.normalvariate(self.delay,
                                              self.delay * self.jitter)

        if self.debug:
            logging.debug("%s:%s will retry in %d seconds" % (self.sock_args[0][0], self.sock_args[0][1], self.delay,))

        self.connect()

        gevent.spawn_later(self.delay, self._retry)
     
if __name__ == '__main__':
    client = SocketRPCClient(('192.168.12.21',6000),RPCSocket,TestProtocol)
    print client.helloworld()
    #print ('!!!!!!!!!!!!!!!!!!!')
    gevent.sleep(0)
    #mc = MyClient()
    
    #gevent.joinall([gevent.spawn(mc.loop),gevent.spawn(mc.getinput)])
    #gevent.joinall([gevent.spawn(mc.loop),gevent.spawn(mc.getinput)])