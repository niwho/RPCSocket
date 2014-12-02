#coding=gbk
#!/usr/bin/env python
"""Simple server that listens on port 6000 and echos back every input to the client.
Connect to it with:
  telnet localhost 6000
Terminate the connection by terminating telnet (typically Ctrl-] and then 'quit').
"""
from __future__ import print_function
from gevent.server import StreamServer
import gevent
import struct

class MyHandler(object):
# this handler will be run for each incoming connection in a dedicated greenlet
    def __init__(self):
        self.socks = {}
        
    def __call__(self,socket, address):
        self.socks[socket]=address
        self.echo(socket,address)
        
    def reader(self,sock):
        while 1: 
            data = sock.recv(1024) #socke�Ͽ���������쳣�׳�
            if data:
                print (data)
            #dispatch
            
                
    def writer(self,sock):# �����������Ҫwhile
        k = 0
        while 1:
            sock.send("%d\n"%(k,))#socke�Ͽ���������쳣�׳�
            k+=1
            gevent.sleep(10)
            pass
        
    def echo(self,socket, address):
        print('New connection from %s:%s' % address)
        socket.sendall('Welcome to the echo server! Type quit to exit.\r\n')
        # using a makefile because we want to use readline()
        try:
            r = gevent.spawn(self.reader,socket)
            w = gevent.spawn(self.writer,socket)
            gevent.joinall([r, w])
        finally:
            #del(users[name])
            #broadcast('## %s left the chat.' % name)
            print ('close',socket,self.socks[socket])
            self.socks.pop(socket)

class ISCMProtocolException(Exception):
    def __init__(self):
        pass
class ISCMProtocol(object):
    def __init__(self,socket):
        self.socket = socket
        pass
    def _readSized(self,size):
        
        #��ȡ�ض���������
        data = self.socket.recv(size)
        l = len(data)
        while l<size:
            part=self.socket.recv(size-l)
            l+=len(part)
            data+=part
        return data
    
    def readStream(self):
        try:
            #�����ֽ���
            #��ȡ�ض��������� headͷ:���ȣ������룬��ˮ��,{relpycode|methodnamelen},[methodname],param
            headlen=struct.calcsize('!IBIi')
            datalen,reqcode,seqcode,replyormethlen= struct.unpack('!IBIi',self._readSized(headlen))
            datalen-=headlen
            if datalen<1:
                raise ISCMProtocolException()
            data = self._readSized(datalen)
            
            if reqcode == 0:
                #���ý������  0sҲ��
                formatstr='!%ds'%(datalen,)
                (params,) = struct.unpack(formatstr,data)
                return (reqcode,seqcode,replyormethlen,params)
                pass
            elif reqcode == 1 or reqcode == 2:
                #ͬ�����ã���ȡ��������첽����
                formatstr='!%ds%ds'%(replyormethlen,datalen-replyormethlen)
                (methodname,params) = struct.unpack(formatstr,data)
                return (reqcode,seqcode,methodname,params)
                pass
           
            else :
                raise ISCMProtocolException()
        except Exception,e:
            print(e)
            raise ISCMProtocolException()
        
        
        pass
    
    def writeStream(self,**kw):
        try:
            pass
        except Exception:
            pass
        pass
    
class RPCSocket(object):
    def __init__(self,protoclass,socket):
        self.proto = protoclass(socket)
        self.socket = socket
        pass
    
    def _read(self):
        
        while True:
            try:
                (reqcode,seqcode,relpycode_or_methodname,params) = self.proto.readStream()
                if reqcode ==0:
                    self.OnReply(seqcode, relpycode_or_methodname, params)
                    pass
                elif reqcode == 1:
                    self.OnCall(seqcode,relpycode_or_methodname,params)
                    pass
                elif reqcode == 2:
                    self.OnPostingCall(seqcode,relpycode_or_methodname,params)
                    pass
                else:
                    print('�޷�ʶ���������')
            except ISCMProtocolException,ee:
                print(ee)
            except Exception:
                pass
            #�ɷ����󣨿����ǽ��֪ͨ��
        pass
    
    #����ӿ��Ƿ��д��ڱ�Ҫ��
    def _write(self,*args):
        
        while True:
            self.proto.writeStream(*args)
        pass
    
    #call ��2�У�һ���ǵ���write���������󣩣�һ���Ǳ�����read����������
    def OnCall(self,seqcode,methodname,params):
        if not hasattr(self,methodname):
            pass
        
        pass
    
    #ͬ��
    def OnPostingCall(self,seqcode,methodname,params):
        pass
    
    #���ʹ�����write
    def OnReply(self,seqcode,relpycode,params):
        pass
    
    ###methods####
    def helloworld(self):
        print('hello world!')
    
if __name__ == '__main__':
    # to make the server use SSL, pass certfile and keyfile arguments to the constructor
    server = StreamServer(('0.0.0.0', 6000), MyHandler())
    # to start the server asynchronously, use its start() method;
    # we use blocking serve_forever() here because we have no other jobs
    print('Starting echo server on port 6000')
    server.serve_forever()
