#!/usr/bin/env python

# Interface to FLIR AX8 camera

import urllib
import urllib2
import base64

# Reverse engineering...
#
# wget --post-data 'action=set&resource=.resmon.action.snapshot&value=true'  http://192.168.15.6/res.php
#
# wget --post-data 'action=get&resource=.image.services.store.filename' http://192.168.15.6/res.php

class Flir:
    def __init__(self, baseURL='http://192.168.15.6/'):
        self.baseURL = baseURL

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

