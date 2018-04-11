#!/usr/bin/env python

import rospy
from std_msgs.msg import String, Float32
import json

pubs = {}

def callback(data):
    global pubs
    #print data
    boxes = json.loads(data.data)
    for b in boxes:
        bn = b['boxNumber']
        if not bn in pubs:
            pubs[bn] = {}
            pubs[bn]['minT'] = rospy.Publisher('flir_engine/'+str(bn)+'/minT',Float32,queue_size=10)
            pubs[bn]['avgT'] = rospy.Publisher('flir_engine/'+str(bn)+'/avgT',Float32,queue_size=10)
            pubs[bn]['maxT'] = rospy.Publisher('flir_engine/'+str(bn)+'/maxT',Float32,queue_size=10)
        #print b
        if b['active'] == '"true"':
            pubs[bn]['minT'].publish(float(b['minT'].strip('"')[:-1]))
            pubs[bn]['avgT'].publish(float(b['avgT'].strip('"')[:-1]))
            pubs[bn]['maxT'].publish(float(b['maxT'].strip('"')[:-1]))



if __name__ == '__main__':
    rospy.init_node('flir_decode', anonymous=False)
    rospy.Subscriber('/udp/flir_engine', String, callback)
    rospy.spin()