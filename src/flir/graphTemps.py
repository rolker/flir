#!/usr/bin/env python

import flir
import matplotlib.pyplot as plt
import datetime

f = flir.Flir()

data = {'t':[],'min':[],'avg':[],'max':[]}

plt.ion()

while True:
    b = f.getBox(1)
    print b['minT'],b['avgT'],b['maxT']
    data['t'].append(datetime.datetime.utcnow())
    data['min'].append(float(b['minT'].strip('"')[:-1]))
    data['avg'].append(float(b['avgT'].strip('"')[:-1]))
    data['max'].append(float(b['maxT'].strip('"')[:-1]))
    plt.plot(data['t'],data['min'])
    plt.plot(data['t'],data['avg'])
    plt.plot(data['t'],data['max'])
    plt.pause(0.1)
    