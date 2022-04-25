import RPi.GPIO as gpio
import time
import datetime
def decimal2binary(value): 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]
def analogVoltage(num):
    global dacPins
    for i,val in enumerate(decimal2binary(num)):
                    gpio.output(dacPins[i],val)
def adc()->float:
    global dacPins,compPin
    left,right =0,255
    for _ in range(8):
        volt = left + (right-left)//2
        analogVoltage(volt)
        time.sleep(0.07)
        if not gpio.input(compPin):
            right = volt
        else:
            left = volt
    return    left + (right-left)//2  
            

  

gpio.setmode(gpio.BCM)
dacPins = [26,19,13,6,5,11,9,10]
gpio.setup(dacPins,gpio.OUT,initial = 0)
compPin = 4
gpio.setup(compPin,gpio.IN)
potVoltage = 17
gpio.setup(potVoltage,gpio.OUT)
timeData = []
voltageData = []
counter = 0
startTime = datetime.datetime.now()
gpio.output(potVoltage,1)
try:
    while True:
        nowVoltage = adc()
        print(nowVoltage)
        nowTime = datetime.datetime.now() - startTime
        voltageData.append(nowVoltage)
        timeData.append(nowTime.seconds+nowTime.microseconds/(10**6))
        if nowVoltage >= 252:
            print("Разряжаем конденсатор")
            gpio.output(potVoltage,0)
finally:
    gpio.output(dacPins,0)
    gpio.cleanup()
    with open('data2.txt','w') as f:
        for i in range(len(timeData)):
            outStr = str(timeData[i])+' '+str(voltageData[i])+'\n'
            f.write(outStr)
    
