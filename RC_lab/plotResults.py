import matplotlib.pyplot as plt
import numpy as np

def readData(path: str):
    time = []
    voltage = []
    data = open(path)
    for line in data:
        t,v = map(float,line.split())
        v*=(3.3/255)
        voltage.append(v)
        time.append(t)
    return voltage,time

dataPath = 'meagurement/data.txt'
voltage,time = readData(dataPath)
xAx = np.arange(0,300,0.01)
yAx = 3.3*(1-np.exp(-xAx/10))
#plt.errorbar(time,voltage,yerr = [3.3/(255*2) for _ in time],xerr = [0.0001 for _ in time],fmt='_')
plt.plot(time,voltage)
plt.plot(xAx,yAx,':')
plt.show()

