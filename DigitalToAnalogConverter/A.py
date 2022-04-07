import RPi.GPIO as gpio



def decimal2binary(value): 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


gpio.setmode(gpio.BCM)
dacPins = [10,9,11,5,6,13,19,26]
dacPins = dacPins[::-1]
gpio.setup(dacPins,gpio.OUT,initial = 1)
try:
    num = input()
    while num!='q':
        if not num.isnumeric():
            print("Введено не числовое значение")
        else:
            num = int(num)
            if num<0 or num>255:
                print("Введите число от 0 до 255")
            else:
                print('Будет подано напряжение около: '+str(3.3*num/255))
                for i,val in enumerate(decimal2binary(num)):
                    gpio.output(dacPins[i],val)
        num = input()
finally:
    gpio.output(dacPins,0)
    gpio.cleanup()