import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
size = 100
data = np.random.random(size)
time = np.linspace(0,10,size)
func = interp1d(time,data,'cubic')
funcPlotX = np.linspace(0,10,size*100)
funcPlotData = [func(x) for x in funcPlotX]
plt.plot(funcPlotX,funcPlotData)
plt.errorbar(time,
            data,
            xerr = [0 for _ in time],
            yerr = [0.01 for _ in time],
            fmt='_')
plt.show()