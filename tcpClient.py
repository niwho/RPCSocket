#
from gevent import socket
import gevent
import sys
from gevent import monkey;
monkey.patch_select()
monkey.patch_sys()

import select
import string 

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
    
    @xx
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
                
            
if __name__ == '__main__':
    mc = MyClient()
    
    #gevent.joinall([gevent.spawn(mc.loop),gevent.spawn(mc.getinput)])
    gevent.joinall([gevent.spawn(mc.loop),gevent.spawn(mc.getinput)])