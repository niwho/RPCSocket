## -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
#import wx.xrc
import gevent.socket
import struct
import re
import win32api
import socket
from gevent import monkey
gevent.monkey.patch_socket()
###########################################################################
## Class MyPanel2
###########################################################################

class MyPanel2 ( wx.Panel ):
    
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 584,230 ), style = wx.TAB_TRAVERSAL )
        
        bSizer11 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
        
        bSizer14 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"IP地址", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )
        bSizer14.Add( self.m_staticText12, 0, wx.ALL, 5 )
        
        
        bSizer13.Add( bSizer14, 1, wx.EXPAND, 5 )
        
        bSizer15 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_text_ip = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer15.Add( self.m_text_ip, 0, wx.ALL, 5 )
        
        
        bSizer13.Add( bSizer15, 2, wx.EXPAND, 5 )
        
        bSizer16 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"端口号", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText13.Wrap( -1 )
        bSizer16.Add( self.m_staticText13, 0, wx.ALL, 5 )
        
        
        bSizer13.Add( bSizer16, 1, wx.EXPAND, 5 )
        
        bSizer17 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_text_port = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer17.Add( self.m_text_port, 0, wx.ALL, 5 )
        
        
        bSizer13.Add( bSizer17, 2, wx.EXPAND, 5 )
        
        bSizer18 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_bt_connect = wx.Button( self, wx.ID_ANY, u"连接", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer18.Add( self.m_bt_connect, 0, wx.ALL, 5 )
        
        
        bSizer13.Add( bSizer18, 1, wx.EXPAND, 5 )
        
        
        bSizer11.Add( bSizer13, 0, 0, 5 )
        
        bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
        
        fgSizer2 = wx.FlexGridSizer( 6, 4, 0, 0 )
        fgSizer2.SetFlexibleDirection( wx.BOTH )
        fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"每纬圈数(1-10)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )
        fgSizer2.Add( self.m_staticText8, 0, wx.ALL, 5 )
        
        self.m_text_quan = wx.TextCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer2.Add( self.m_text_quan, 0, wx.ALL, 5 )
        
        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"织机转速(300-1000)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )
        fgSizer2.Add( self.m_staticText9, 0, wx.ALL, 5 )
        
        self.m_text_speed = wx.TextCtrl( self, wx.ID_ANY, u"300", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer2.Add( self.m_text_speed, 0, wx.ALL, 5 )
        
        self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"C1模式(1/0)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )
        fgSizer2.Add( self.m_staticText10, 0, wx.ALIGN_CENTER|wx.ALIGN_RIGHT|wx.ALL, 5 )
        
        self.m_text_c1_mode = wx.TextCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer2.Add( self.m_text_c1_mode, 0, wx.ALL, 5 )
        
        self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"C2模式(1/0)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )
        fgSizer2.Add( self.m_staticText11, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_text_c2_mode = wx.TextCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer2.Add( self.m_text_c2_mode, 0, wx.ALL, 5 )
        
        self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"C1延时(1-5)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText14.Wrap( -1 )
        fgSizer2.Add( self.m_staticText14, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_text_c1_delay = wx.TextCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer2.Add( self.m_text_c1_delay, 0, wx.ALL, 5 )
        
        self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"C2延时(1-5)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText15.Wrap( -1 )
        fgSizer2.Add( self.m_staticText15, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_text_c2_delay = wx.TextCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer2.Add( self.m_text_c2_delay, 0, wx.ALL, 5 )
        
        self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"C1预绕圈数(10-100)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )
        fgSizer2.Add( self.m_staticText16, 0, wx.ALL, 5 )
        
        self.m_text_c1_prequan = wx.TextCtrl( self, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer2.Add( self.m_text_c1_prequan, 0, wx.ALL, 5 )
        
        self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"C2预绕圈数(10-100)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText17.Wrap( -1 )
        fgSizer2.Add( self.m_staticText17, 0, wx.ALL, 5 )
        
        self.m_text_c2_prequan = wx.TextCtrl( self, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer2.Add( self.m_text_c2_prequan, 0, wx.ALL, 5 )
        
        self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"C1速度比例(1-100)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText18.Wrap( -1 )
        fgSizer2.Add( self.m_staticText18, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_text_c1_speedrate = wx.TextCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer2.Add( self.m_text_c1_speedrate, 0, wx.ALL, 5 )
        
        self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"C2速度比例(1-100)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText19.Wrap( -1 )
        fgSizer2.Add( self.m_staticText19, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_text_c2_speedrate = wx.TextCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer2.Add( self.m_text_c2_speedrate, 0, wx.ALL, 5 )
        
        
        bSizer1.Add( fgSizer2, 3, wx.EXPAND, 5 )
        
        bSizer4 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_bt_test = wx.Button( self, wx.ID_ANY, u"测试", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.m_bt_test, 0, wx.ALL, 5 )
        
        self.m_bt_read = wx.Button( self, wx.ID_ANY, u"读取", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.m_bt_read, 0, wx.ALL, 5 )
        
        self.m_bt_send = wx.Button( self, wx.ID_ANY, u"发送", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.m_bt_send, 0, wx.ALL, 5 )
        
        self.m_bt_quit = wx.Button( self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.m_bt_quit, 0, wx.ALL, 5 )
        
        
        bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )
        
        
        bSizer11.Add( bSizer1, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer11 )
        self.Layout()
        
        # Connect Events
        self.m_bt_connect.Bind( wx.EVT_BUTTON, self.m_bt_connectOnButtonClick )
        self.m_bt_test.Bind( wx.EVT_BUTTON, self.m_bt_testOnButtonClick )
        self.m_bt_read.Bind( wx.EVT_BUTTON, self.m_bt_readOnButtonClick )
        self.m_bt_send.Bind( wx.EVT_BUTTON, self.m_bt_sendOnButtonClick )
        self.m_bt_quit.Bind( wx.EVT_BUTTON, self.m_bt_quitOnButtonClick )
    
        self.m_text_quan.Bind( wx.EVT_CHAR, self.m_text_quanOnChar )
        self.m_text_quan.Bind( wx.EVT_LEAVE_WINDOW, self.m_text_quanOnLeaveWindow )
        self.m_text_speed.Bind( wx.EVT_CHAR, self.m_text_speedOnChar )
        self.m_text_speed.Bind( wx.EVT_LEAVE_WINDOW, self.m_text_speedOnLeaveWindow )
        self.m_text_c1_mode.Bind( wx.EVT_CHAR, self.m_text_c1_modeOnChar )
        self.m_text_c1_mode.Bind( wx.EVT_LEAVE_WINDOW, self.m_text_c1_modeOnLeaveWindow )
        self.m_text_c2_mode.Bind( wx.EVT_CHAR, self.m_text_c2_modeOnChar )
        self.m_text_c2_mode.Bind( wx.EVT_LEAVE_WINDOW, self.m_text_c2_modeOnLeaveWindow )
        self.m_text_c1_delay.Bind( wx.EVT_CHAR, self.m_text_c1_delayOnChar )
        self.m_text_c1_delay.Bind( wx.EVT_ENTER_WINDOW, self.m_text_c1_delayOnEnterWindow )
        self.m_text_c2_delay.Bind( wx.EVT_CHAR, self.m_text_c2_delayOnChar )
        self.m_text_c2_delay.Bind( wx.EVT_LEAVE_WINDOW, self.m_text_c2_delayOnLeaveWindow )
        self.m_text_c1_prequan.Bind( wx.EVT_CHAR, self.m_text_c1_prequanOnChar )
        self.m_text_c1_prequan.Bind( wx.EVT_LEAVE_WINDOW, self.m_text_c1_prequanOnLeaveWindow )
        self.m_text_c2_prequan.Bind( wx.EVT_CHAR, self.m_text_c2_prequanOnChar )
        self.m_text_c2_prequan.Bind( wx.EVT_LEAVE_WINDOW, self.m_text_c2_prequanOnLeaveWindow )
        self.m_text_c1_speedrate.Bind( wx.EVT_CHAR, self.m_text_c1_speedrateOnChar )
        self.m_text_c1_speedrate.Bind( wx.EVT_LEAVE_WINDOW, self.m_text_c1_speedrateOnLeaveWindow )
        self.m_text_c2_speedrate.Bind( wx.EVT_CHAR, self.m_text_c2_speedrateOnChar )
        self.m_text_c2_speedrate.Bind( wx.EVT_LEAVE_WINDOW, self.m_text_c2_speedrateOnLeaveWindow )
        
        self.buttonDisable()
        
    def __del__( self ):
        pass
    
    
    def buttonEnable(self):
        self.m_bt_test.Enable()
        self.m_bt_read.Enable()
        self.m_bt_send.Enable()
    
    def buttonDisable(self):
        self.m_bt_test.Disable()
        self.m_bt_read.Disable()
        self.m_bt_send.Disable()
        
    def isBettwen(self,val,min,max,flag=False):
        if not flag:
            return  val<=max       
        return  val>=min and val<=max       
    def m_bt_connectOnButtonClick( self, event ):
        try:
            ipstr = self.m_text_ip.GetValue().strip()
            if not re.match(r'(?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))$',
                     ipstr):
                raise Exception('ip不对')
            port = int(self.m_text_port.GetValue().strip())
            self.conn = Client()
            self.conn.setserveipp((ipstr,port),1)
            self.buttonEnable()
        except gevent.socket.Timeout,e:
            print e
            wx.MessageDialog(self,e.message,u'通知',style=wx.OK|wx.CENTRE).ShowModal()
            
        except Exception,e:
            #print e
            wx.MessageDialog(self,e.message,u'通知',style=wx.OK|wx.CENTRE).ShowModal()
            
    def m_bt_testOnButtonClick( self, event ):
        struct.calcsize('!2B10H')
        try:
            data = struct.pack('!2s','\x40\x01')
            self.conn._sendSized(data)
            data = self.conn._readSized(-1)
            wx.MessageDialog(self,data.encode('hex'),u'通知',style=wx.OK|wx.CENTRE).ShowModal()
      
            
        except Exception,e:
            print e
            wx.MessageDialog(self,str(e),u'通知',style=wx.OK|wx.CENTRE).ShowModal()
            self.buttonDisable()
        
    
    def m_bt_readOnButtonClick( self, event ):
         try:
            data = struct.pack('!2s','\x40\x02')
            self.conn._sendSized(data)
            data = self.conn._readSized(-1)
            if not data:
                wx.MessageDialog(self,data.encode('hex'),u'通知',style=wx.OK|wx.CENTRE).ShowModal()
            else:
                wx.MessageDialog(self,'nothing got back',u'通知',style=wx.OK|wx.CENTRE).ShowModal()
      
            
         except Exception,e:
            print e.message
            wx.MessageDialog(self,e.message,u'通知',style=wx.OK|wx.CENTRE).ShowModal()
            self.buttonDisable()
    
    def m_bt_sendOnButtonClick( self, event ):
        
         try:
            data = struct.pack('!2s','\x40\x03')
            self.conn._sendSized(data)
            data = self.conn._readSized(-1)
            wx.MessageDialog(self,data.encode('hex'),u'通知',style=wx.OK|wx.CENTRE).ShowModal()
      
            
         except Exception,e:
            print e
            wx.MessageDialog(self,e.message,u'通知',style=wx.OK|wx.CENTRE).ShowModal()
            self.buttonDisable()
    
    def m_bt_quitOnButtonClick( self, event ):
        wx.MessageDialog(self,u'关闭',u'通知',style=wx.OK|wx.CENTRE).ShowModal()
        self.Parent.Destroy()
    
    def m_text_quanOnChar( self, event ):
        print dir(event)
        print event.GetKeyCode(),event.GetUnicodeKey()
        print event.IsKeyInCategory(wx.WXK_CATEGORY_CUT|wx.WXK_CATEGORY_NAVIGATION|wx.WXK_CATEGORY_TAB)
        self.validate(self.m_text_quan,event,1,10)
        
    def m_text_quanOnLeaveWindow( self, event ):
        if not self.m_text_quan.GetValue().strip():
            self.m_text_quan.SetValue('1')
            return 
        val = int(self.m_text_quan.GetValue().strip())
        if not self.isBettwen(val, 1,10, True):
            self.m_text_quan.SetValue('1')
            #self.m_text_quan.Refresh()
            #self.m_text_quan.SelectAll()
            
    def m_text_speedOnChar( self, event ):
        self.validate(self.m_text_speed,event,300,1000)
    
    def m_text_speedOnLeaveWindow( self, event ):
        if not self.m_text_speed.GetValue().strip():
            self.m_text_speed.SetValue('1')
            return 
        val = int(self.m_text_speed.GetValue().strip())
        if not self.isBettwen(val, 300,1000, True):
            self.m_text_speed.SetValue('300')
    
    def m_text_c1_modeOnChar( self, event ):
        self.validate(self.m_text_c1_mode,event,0,1)
    
    def m_text_c1_modeOnLeaveWindow( self, event ):
        if not self.m_text_c1_mode.GetValue().strip():
            self.m_text_c1_mode.SetValue('1')
            return 
        val = int(self.m_text_c1_mode.GetValue().strip())
        if not self.isBettwen(val, 0,1, True):
            self.m_text_c1_mode.SetValue('1')
    
    def m_text_c2_modeOnChar( self, event ):
        self.validate(self.m_text_c2_mode,event,0,1)
    
    def m_text_c2_modeOnLeaveWindow( self, event ):
        if not self.m_text_c2_mode.GetValue().strip():
            self.m_text_c2_mode.SetValue('1')
            return 
        val = int(self.m_text_c2_mode.GetValue().strip())
        if not self.isBettwen(val, 0,1, True):
            self.m_text_c2_mode.SetValue('1')
    
    def m_text_c1_delayOnChar( self, event ):
        self.validate(self.m_text_c1_delay,event,1,5)
    
    def m_text_c1_delayOnEnterWindow( self, event ):
        if not self.m_text_c1_delay.GetValue().strip():
            self.m_text_c1_delay.SetValue('1')
            return 
        val = int(self.m_text_c1_delay.GetValue().strip())
        if not self.isBettwen(val, 1,5, True):
            self.m_text_c1_delay.SetValue('1')
    
    def m_text_c2_delayOnChar( self, event ):
        self.validate(self.m_text_c2_delay,event,1,5)
    
    def m_text_c2_delayOnLeaveWindow( self, event ):
        if not self.m_text_c2_delay.GetValue().strip():
            self.m_text_c2_delay.SetValue('1')
            return 
        val = int(self.m_text_c2_delay.GetValue().strip())
        if not self.isBettwen(val, 1,5, True):
            self.m_text_c2_delay.SetValue('1')
    
    def m_text_c1_prequanOnChar( self, event ):
        self.validate(self.m_text_c1_prequan,event,10,100)
    
    def m_text_c1_prequanOnLeaveWindow( self, event ):
        if not self.m_text_c1_prequan.GetValue().strip():
            self.m_text_c1_prequan.SetValue('10')
            return 
        val = int(self.m_text_c1_prequan.GetValue().strip())
        print val
        if not self.isBettwen(val, 10,100, True):
            self.m_text_c1_prequan.SetValue('10')
    
    def m_text_c2_prequanOnChar( self, event ):
        self.validate(self.m_text_c2_prequan,event,10,100)
    
    def m_text_c2_prequanOnLeaveWindow( self, event ):
        if not self.m_text_c2_prequan.GetValue().strip():
            self.m_text_c2_prequan.SetValue('10')
            return 
        val = int(self.m_text_c2_prequan.GetValue().strip())
        if not self.isBettwen(val, 10,100, True):
            self.m_text_c2_prequan.SetValue('10')
    
    def m_text_c1_speedrateOnChar( self, event ):
        self.validate(self.m_text_c1_speedrate,event,1,100)
    
    def m_text_c1_speedrateOnLeaveWindow( self, event ):
        if not self.m_text_c1_speedrate.GetValue().strip():
            self.m_text_c1_speedrate.SetValue('1')
            return 
        val = int(self.m_text_c1_speedrate.GetValue().strip())
        if not self.isBettwen(val, 1,100, True):
            self.m_text_c1_speedrate.SetValue('1')
    
    def m_text_c2_speedrateOnChar( self, event ):
        self.validate(self.m_text_c2_speedrate,event,1,100)
    
    def m_text_c2_speedrateOnLeaveWindow( self, event ):
        if not self.m_text_c2_speedrate.GetValue().strip():
            self.m_text_c2_speedrate.SetValue('1')
            return 
        val = int(self.m_text_c2_speedrate.GetValue().strip())
        if not self.isBettwen(val, 1,100, True):
            self.m_text_c2_speedrate.SetValue('1')
        
    def validate(self,ctrl,event,min,max):
        if event.IsKeyInCategory(wx.WXK_CATEGORY_CUT):
            event.Skip()
            return
        try:
            te = ctrl.GetValue()
            te+=chr(event.GetKeyCode())
            val = int(te)
            if self.isBettwen(val, min, max):
                ctrl.AppendText(chr(event.GetKeyCode()))
        except Exception,e:
            print e
            #wx.MessageDialog(self,u'无效值',u'错误',style=wx.OK|wx.CENTRE).ShowModal()
###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 580,250 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.SYSTEM_MENU )
        exeName = win32api.GetModuleFileName(win32api.GetModuleHandle(None))
        self.icon = wx.Icon(exeName, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon) 
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        panel= MyPanel2(self)
        self.Centre( wx.BOTH )
    
    def __del__( self ):
        pass
    
class Client(object):
    def __init__(self):
        self.isconnected = False
        pass
    
    def setserveipp(self,ipp,timeout):
        try:
            self.serveipp = ipp
            ipstr = ipp[0]
            if not re.match(r'(?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))$',
                     ipstr):
                raise Exception(u'ip不对')
            port = ipp[1]
            self.socket = gevent.socket.create_connection((ipstr,port),timeout)
            self.isconnected = True
            
        except Exception,e:
            print e
            raise Exception(u'连接失败')
        
    def isConnected(self):
        return self.isconnected    
    
    def reconnect(self):
        if not self.isconnected:
            self.setserveipp(self.serveipp,1)
        pass
    # Virtual event handlers, overide them in your derived class
    def _readSized(self,size):
        try:
            #获取特定长度数据
            if size<0:
                data = self.socket.recv(256)
            else:
                data = self.socket.recv(size)
            l = len(data)
            while l<size:
                part=self.socket.recv(size-l)
                l+=len(part)
                data+=part
            return data
        except gevent.Timeout,e:
            print 1
        except socket.timeout,e:
            print 2
        except Exception,e:
            print 3,e,type(e)
            self.isconnected = False
            raise Exception(u'连接断开')
    
    def _sendSized(self,data):
        try:
            size= len(data)
            sended=0
            while sended<size:
                sended+=self.socket.send(data[sended:])#gevent 在连接失去时，这个接口仍出异常？    
        except gevent.Timeout,e:
            print 1
        except socket.timeout,e:
            print 2
        except Exception,e:
            self.isconnected = False
            raise Exception('连接断开')
        
if __name__=='__main__':
    app = wx.App(False)
    fram=MyFrame1(None)
    fram.Show()
    app.MainLoop()

