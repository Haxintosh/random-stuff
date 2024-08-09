# BAD CODE WARNING!!!!!!!!!
# USE PID INSTEAD OF THIS HORRIBLE METHOD!!!!!

import time
import board
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import busio
import digitalio
import math

THERMISTOR_NOMINAL = 100000
TEMP_NOMINAL = 25

B_COEFFICIENT = 3950
N_SAMPLES = 3

SERIES_RESISTOR = 100000
VCC = 3.3

MAX_TEMP = 260
BUFFER_TIME = 5
SSR_PIN = board.GP11

SSR = digitalio.DigitalInOut(SSR_PIN)
SSR.direction = digitalio.Direction.OUTPUT

def voltage_to_c(voltage):
    resistance = (SERIES_RESISTOR/(voltage/VCC))-SERIES_RESISTOR
    temp = (1/(math.log(resistance/THERMISTOR_NOMINAL)*(1/B_COEFFICIENT)+(1/(TEMP_NOMINAL+273.15))))-273.15
    print(temp)
    return temp

def sampled_read(samples, delay):
    s = 0
    for i in range(samples):
        s += round(chan.voltage, 4)
        time.sleep(delay)
    return s/samples

i2c = busio.I2C(board.GP15, board.GP14)    # Pi Pico RP2040
ads = ADS.ADS1015(i2c)
chan = AnalogIn(ads, ADS.P0)

while True:
    temp = voltage_to_c(sampled_read(3, 0.01))
    if temp < MAX_TEMP:
        SSR.value = True
    else:
        SSR.value = False
