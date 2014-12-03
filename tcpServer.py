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
import gevent.event
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
            data = sock.recv(1024) #socke断开这里会有异常抛出
            if data:
                print (data)
            #dispatch
            
                
    def writer(self,sock):# 这个函数不需要while
        k = 0
        while 1:
            sock.send("%d\n"%(k,))#socke断开这里会有异常抛出
            k+=1
            gevent.sleep(10)
            pass
        
    def echo(self,socket, address):
        print('New connection from %s:%s' % address)
        socket.sendall('Welcome to the echo server! Type quit to exit.\r\n')
        # using a makefile because we want to use readline()
        try:
            gevent.spawn(self.reader,socket)
            gevent.spawn(self.writer,socket)
        finally:
            #del(users[name])
            #broadcast('## %s left the chat.' % name)
            print ('close',socket,self.socks[socket])
            self.socks.pop(socket)

class TestProtocolException(Exception):
    def __init__(self):
        pass
class TestProtocol(object):
    def __init__(self,socket):
        self.socket = socket
        pass
    def _readSized(self,size):
        
        #获取特定长度数据
        data = self.socket.recv(size)
        l = len(data)
        while l<size:
            part=self.socket.recv(size-l)
            l+=len(part)
            data+=part
        return data
    
    def _sendSized(self,data):
        size= len(data)
        sended=0
        while sended<size:
            sended+=self.socket.send(data[sended:])#gevent 在连接失去时，这个接口仍出异常？
            
    def readStream(self):
        try:
            #网络字节序，
            #获取特定长度数据 head头:长度，请求码，流水号,{relpycode|methodnamelen},[methodname],param
            headlen=struct.calcsize('!IBIi')
            datalen,reqcode,seqcode,replyormethlen= struct.unpack('!IBIi',self._readSized(headlen))
            datalen-=headlen
            if datalen<1:
                raise TestProtocolException()
            data = self._readSized(datalen)
            
            if reqcode == 0:
                #调用结果返回  0s也行
                formatstr='!%ds'%(datalen,)
                (params,) = struct.unpack(formatstr,data)
                return (reqcode,seqcode,replyormethlen,params)
                pass
            elif reqcode == 1 or reqcode == 2:
                #同步调用（获取结果）或异步调用
                formatstr='!%ds%ds'%(replyormethlen,datalen-replyormethlen)
                (methodname,params) = struct.unpack(formatstr,data)
                return (reqcode,seqcode,methodname,params)
                pass
           
            else :
                raise TestProtocolException()
        except Exception,e:
            print(e)
            raise TestProtocolException()
        
        
        pass
    
    def writeStream(self,fmat,*parms):
        try:
            pass
            data = struct.pack(fmat,*parms)
            self._sendSized(data)
        except Exception,e:
            print(e)
            raise TestProtocolException()
        pass
    
class RPCSocket(object):
    def __init__(self,protoclass,socket):
        try:
            self.proto = protoclass(socket)
            self.socket = socket
        
            self.seqcall={}
            self.seqid = 0
        except Exception,e:
            print(e)
            
    

            
    def isConnected(self):
        return False
    
    def _read(self):
        
        while True:
            try:
                (reqcode,seqcode,relpycode_or_methodname,params) = self.proto.readStream()
                if reqcode ==0:
                    self.OnReply(seqcode, relpycode_or_methodname, params)
                    pass
                elif reqcode == 1:
                    print(seqcode,relpycode_or_methodname,params)
                    self.OnCall(seqcode,relpycode_or_methodname,params)
                    pass
                else:
                    print('无法识别的请求码')
            except TestProtocolException,ee:
                print(ee)
                break
            except Exception:
                print(ee)
                break
                pass
            #派发请求（可能是结果通知）
        pass
    
    #这个接口是否有存在必要性 noneed
    #def _write(self,*args):
    #    
    #    while True:
    #        self.proto.writeStream(*args)
    #    pass
    
    #call 有2中，一种是调用write（发送请求），一种是被调用read（接受请求）
    def OnCall(self,seqcode,methodname,params):
        if not hasattr(self,methodname):
            pass
        try:
            bounded_func = getattr(self,methodname)
            #bounded_func.seqcode=seqcode
            self.seqcode=seqcode
            print (params)
            bounded_func()
           
        except Exception,e:
            print(e,'函数调用失败')
            pass
    
    #发送处理结果write
    def OnReply(self,seqcode,relpycode,params):
        
        self.seqcall[seqcode].set((relpycode,params))
        del self.seqcall[seqcode]
        pass
    
    def call(self):
        
        pass
    
    def reply(self):
        
        pass
    ###methods####
    #call
    def helloworld_s(self):
        print('hello world! from %s'%(self.socket.getsockname(),))
        data='hello reply from %s'%(self.socket.getsockname(),)
        fmat='!IBIi%ds'%(len(data),)
        self.proto.writeStream(fmat,13+len(data),0,self.seqcode,0,data)
    
    #posting or not posting 由调用端确定  不影响服务器端
    def helloworldserver(self):
        print('hello from clinet')
        
    #method 
    def helloto_c(self):
        try:
            self.seqid=self.seqid%100+1
            data='hello call from %s'%(self.socket.getsockname(),)
            fmat='!IBIi%ds%ds'%(len('helloworld_s'),len(data))
            self.proto.writeStream(fmat,13+len(data)+len('helloworld_s'),1,self.seqid,len('helloworld_s'),'helloworld_s',data)
            syncFin = gevent.event.AsyncResult()
            self.seqcall[self.seqid] = syncFin
            
        except Exception,e:
            print(e)
            return (-1,)
        return syncFin
    
    #post method
    def hello_c_posting(self):
        try:
            self.seqid=self.seqid%100+1
            data='hello call from %s'%(self.socket.getsockname(),)
            fmat='!IBIi%ds%ds'%(len(self.hellotoinvoker.__name__),len(data))
            self.proto.writeStream(fmat,13+len(data),1,self.seqid,len('helloworld_s'),'helloworld_s',data)
        except Exception,e:
            print (e)
            return (-1,)
        return (0,)
    
class SocketRPCServer(StreamServer):
    def __init__(self, listener, rpctype,prototype, backlog=None, spawn='default'):
        StreamServer.__init__(self, listener, backlog=backlog, spawn=spawn)
        self.rpcmodel = rpctype
        self.proto =prototype

    def handle(self, socket, address):
        """ Start the socket handlers
            self.protocol.handle_write and
            self.protocol.handle_read.
        """
        realrpc=self.rpcmodel(self.proto,socket)
        print("connection from %s"%(str(address),))
        realrpc._read()


if __name__ == '__main__':
    # to make the server use SSL, pass certfile and keyfile arguments to the constructor
    server = SocketRPCServer(('0.0.0.0', 6000), RPCSocket,TestProtocol)
    # to start the server asynchronously, use its start() method;
    # we use blocking serve_forever() here because we have no other jobs
    print('Starting server on port 6000')
    server.serve_forever()
