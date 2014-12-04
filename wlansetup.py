#coding=utf-8
from distutils.core import setup

import py2exe
includes=[]#['chardet']
options = {"py2exe": 
{   "compressed":1, 
    "optimize": 2, 
    "includes": includes, 
    "bundle_files":1,
    "dll_excludes": [ "MSVCP90.dll", "mswsock.dll", "powrprof.dll","w9xpopen.exe"
                  'API-MS-Win-Core-ErrorHandling-L1-1-0.dll',
                  'API-MS-Win-Core-File-L1-1-0.dll',
                  'API-MS-Win-Core-IO-L1-1-0.dll',
                  'API-MS-Win-Core-LibraryLoader-L1-1-0.dll',
                  'API-MS-Win-Core-Handle-L1-1-0.dll',
                  'API-MS-Win-Core-Heap-L1-1-0.dll',
                  'API-MS-Win-Core-Interlocked-L1-1-0.dll',
                  'API-MS-Win-Core-Localization-L1-1-0.dll',
                  'API-MS-Win-Core-Memory-L1-1-0.dll',
                  'API-MS-Win-Core-Misc-L1-1-0.dll',
                  'API-MS-Win-Core-ProcessThreads-L1-1-0.dll',
                  'API-MS-Win-Core-Profile-L1-1-0.dll',
                  'API-MS-Win-Core-String-L1-1-0.dll',
                  'API-MS-Win-Core-Synch-L1-1-0.dll',
                  'API-MS-Win-Core-SysInfo-L1-1-0.dll',
                  'API-MS-Win-Core-ErrorHandling-L1-1-0.dll'
                  ]
} 
} 
setup(version = "1.0.0", 
      description = u"Made by niwho", 
      name = "wlan", 
      options = options, 
      zipfile = None ,
      #data_files = [('', ['about.md'])],
      windows=[{'script':'wlan.gui.py'
                ,'icon_resources': [(1, r'D:\bi4Al31dN8\workspace\Pyproj\13_e.ico')]
                #,'dll_excludes': [ "mswsock.dll", "powrprof.dll" ]
                }])