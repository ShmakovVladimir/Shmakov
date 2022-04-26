from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as interp
def readData(path: str):
    time = []
    voltage = []
    data = open(path)
    for line in data:
        t,v = map(float,line.split())
        v = (v+0.5)*(3.3/255)
        if t<=80:
            voltage.append(v)
            time.append(t)
    return voltage,time

dataPath = 'meagurement/data.txt'
voltage,time = readData(dataPath)
xAx = np.arange(0,80.1,0.01)
yAx = 3.3*(1-np.exp(-xAx/10))
f = interp.interp1d(time,voltage)
fiveTauDot = f(50)
fig,axes = plt.subplots()
axes.set_title("Эксперимент 1: $C = 10 \mu F$, $R = 1MoM$")
plt.xlabel(r"Время $с$")
plt.ylabel("Напяжение $V$")
#Сетка по оси y - пять шагов квантования АЦП
plt.yticks(np.linspace(0,3.3,255//5))
#По оси x - 0.5 tau
plt.xticks([0,10,20,30,40,50,60,70,80],["0",r"$1 \tau$",r"$2 \tau$",r"$3 \tau$",r"$4 \tau$",r"$5 \tau$",r"$6 \tau$",r"$7 \tau$",r"$8 \tau$"])
plt.grid()
#время измерения АЦП - O(0.007*8) секунд(алгоритм поразрядного уравновешивания)
#погрешноть по оси y - половина шага квантования 
plt.errorbar(time[::5],voltage[::5],yerr = [3.3/(255*2) for _ in time[::5]],xerr = [0.007*8 for _ in time[::5]],fmt='_',label='данные эксперимента(каждое пятое измерение)')
plt.plot(time,voltage,label = 'Линейная интерполяция')
plt.plot(xAx,yAx,':',label = r'''Теоретическая модель: $U_c = \mathcal{E} \cdot \left( 1 - e^{-t / \tau} \right) $, где $\tau = RC = \cdot 1 MoM \cdot 10 \mu F = 10 c$''')
plt.annotate(r"Время $5 \tau$, напряжение на конденсаторе: "+str(round(100*fiveTauDot/3.3,1))+"$\%$"+" от максимального", xy=(50, fiveTauDot), xytext=(44, 3),color = 'purple')
plt.plot([50],[fiveTauDot],'o',color = 'purple')
axes.legend(loc = 'lower right')
plt.show()

