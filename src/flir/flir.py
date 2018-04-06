#!/usr/bin/env python

# Interface to FLIR AX8 camera

import urllib
import urllib2
import base64

Reverse_engineering_notes = '''

wget --post-data 'action=set&resource=.resmon.action.snapshot&value=true'  http://192.168.15.6/res.php

wget --post-data 'action=get&resource=.image.services.store.filename' http://192.168.15.6/res.php

//Set to MSX:
.image.sysimg.fusion.fusionData.fusionMode 3

//Set to IR:
.image.sysimg.fusion.fusionData.fusionMode 1
.image.sysimg.fusion.fusionData.useLevelSpan 1

//Set to Visual:
.image.sysimg.fusion.fusionData.fusionMode 1
.image.sysimg.fusion.fusionData.useLevelSpan 0



The variable that controls the Lamp is .system.vcam.torch



In order to enable or disable a given alarm the following Boolean registers should be changed. These registers are accessible via Pass Through Object (EtherNet/IP).

.resmon.items.<alarm#>.active

.image.sysimg.alarms.measfunc.<alarm#>.active


Enabling alarm 1

.resmon.items.1.active TRUE

16 2e 72 65 73 6d 6f 6e 2e 69 74 65 6d 73 2e 31 2e 61 63 74 69 76 65 01

.image.sysimg.alarms.measfunc.1.active TRUE

26 2e 69 6d 61 67 65 2e 73 79 73 69 6d 67 2e 61 6c 61 72 6d 73 2e 6d 65 61 73 66 75 6e 63 2e 31 2e 61 63 74 69 76 65 01

 

Disabling alarm 3

.resmon.items.3.active FALSE

16 2e 72 65 73 6d 6f 6e 2e 69 74 65 6d 73 2e 33 2e 61 63 74 69 76 65 00

.image.sysimg.alarms.measfunc.3.active FALSE

26 2e 69 6d 61 67 65 2e 73 79 73 69 6d 67 2e 61 6c 61 72 6d 73 2e 6d 65 61 73 66 75 6e 63 2e 33 2e 61 63 74 69 76 65 00


See also: BasicICD.pdf


''' 



class Flir:
    def __init__(self, baseURL='http://192.168.15.6/'):
        self.baseURL = baseURL
        #authenticate with camera
	print urllib2.urlopen(self.baseURL+'/login/dologin',urllib.urlencode({'user_name':'admin','user_password':'admin'})).read()


    def takeSnapshot(self):
        urllib2.urlopen(self.baseURL+'res.php',urllib.urlencode({'action':'set','resource':'.resmon.action.snapshot','value':'true'}))
        fname = urllib2.urlopen(self.baseURL+'res.php',urllib.urlencode({'action':'get','resource':'.image.services.store.filename'})).read()
        print fname
        fname = ''.join(fname.strip('"').split('\\'))
        print fname

        #return (fname.rsplit('/',1)[1], urllib2.urlopen(self.baseURL+fname).read()) 
	return ('snapshot.jpg',urllib2.urlopen(self.baseURL+'snapshot.jpg').read())
        



if __name__ == '__main__':
    f = Flir()
    fname, jpg = f.takeSnapshot()
    open(fname,'wb').write(jpg)

