import RPi.GPIO as gpio
import time


def decimal2binary(value): 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

gpio.setmode(gpio.BCM)
dacPins = [10,9,11,5,6,13,19,26]
dacPins = dacPins[::-1]
gpio.setup(dacPins,gpio.OUT,initial = 1)
period = float(input("Введите значение периода в сек"))
try:
    counter = 0
    while True:
        for i,val in enumerate(decimal2binary(counter%256)):
                    gpio.output(dacPins[i],val)
        time.sleep(period/(2*256))
        counter+=1

finally:
    gpio.output(dacPins,0)
    gpio.cleanup()
gpio.setmode(gpio.BCM)
dacPins = [10,9,11,5,6,13,19,26]