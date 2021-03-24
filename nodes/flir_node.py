#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import flir.flir
import json

class FlirPublisher:
    def __init__(self):
        pass
        
    def run(self):
        pub = rospy.Publisher('flir_engine',String,queue_size=10)
        rospy.init_node('flir_engine_node')
        baseURL = rospy.get_param('~baseURL')
        f = flir.flir.Flir(baseURL)

        while not rospy.is_shutdown():
            status = f.getBoxes()
            pub.publish(json.dumps(status))
            
if __name__ == '__main__':
    try:
        fp = FlirPublisher()
        fp.run()
    except rospy.ROSInterruptException:
        pass
    