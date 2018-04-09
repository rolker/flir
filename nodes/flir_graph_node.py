#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import matplotlib.pyplot as plt
import datetime
import json

tempData = {'t':[],'min':[],'avg':[],'max':[]}

plt.ion()


def callback(data):
    #print data
    boxes = json.loads(data.data)
    b = boxes[0]
    print b['minT'],b['avgT'],b['maxT']
    tempData['t'].append(datetime.datetime.utcnow())
    tempData['min'].append(float(b['minT'].strip('"')[:-1]))
    tempData['avg'].append(float(b['avgT'].strip('"')[:-1]))
    tempData['max'].append(float(b['maxT'].strip('"')[:-1]))
    plt.plot(tempData['t'],tempData['min'])
    plt.plot(tempData['t'],tempData['avg'])
    plt.plot(tempData['t'],tempData['max'])
    plt.pause(0.1)
    
if __name__ == '__main__':
    rospy.init_node('flir_graph', anonymous=True)
    rospy.Subscriber('flir_engine', String, callback)
    rospy.spin()
    