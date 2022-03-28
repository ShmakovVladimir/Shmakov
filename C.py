import RPi.GPIO as gpio


def decimal2binary(value): 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

gpio.setmode(gpio.BCM)
pinNum = 23
gpio.setup(pinNum,gpio.OUT)
pwm = gpio.PWM(pinNum,1000)
pwm.start(0)
try:
    num = input()
    while num!='q':
        num = int(num)
        pwm.start(num)
        num = input()
finally:
    pwm.stop()
    gpio.output(pinNum,0)
    gpio.cleanup()

