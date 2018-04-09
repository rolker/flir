#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import flir.flir
import json

class FlirPublisher:
    def __init__(self):
        self.flir = flir.flir.Flir()
        
    def run(self):
        pub = rospy.Publisher('flir_engine',String,queue_size=10)
        rospy.init_node('flir_engine_node')
        while not rospy.is_shutdown():
            status = self.flir.getBoxes()
            pub.publish(json.dumps(status))
            
if __name__ == '__main__':
    try:
        fp = FlirPublisher()
        fp.run()
    except rospy.ROSInterruptException:
        pass
    