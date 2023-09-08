import random

from machine import I2C, Pin
from time import sleep

adresa_ATmegy = 0x10
sda_pin = Pin(2, Pin.OUT, Pin.PULL_UP)
sdc_pin = Pin(3, Pin.OUT, Pin.PULL_UP)
i2c = I2C(1, sda=sda_pin, scl=sdc_pin, freq=400000)

def posli_buffer_mono(buffer):
    zprava = []
    
    
    zprava.append(int(buffer[0][0][0] or buffer[0][0][1] or buffer[0][0][2]))
    zprava.append(int(buffer[0][1][0] or buffer[0][1][1] or buffer[0][1][2]))
    zprava.append(int(buffer[0][2][0] or buffer[0][2][1] or buffer[0][2][2]))
    zprava.append(int(buffer[0][3][0] or buffer[0][3][1] or buffer[0][3][2]))
    zprava.append(int(buffer[0][4][0] or buffer[0][4][1] or buffer[0][4][2]))
    zprava.append(int(buffer[0][5][0] or buffer[0][5][1] or buffer[0][5][2]))
    zprava.append(int(buffer[0][6][0] or buffer[0][6][1] or buffer[0][6][2]))
    zprava.append(int(buffer[0][7][0] or buffer[0][7][1] or buffer[0][7][2]))
    
    
    
    zprava.append(int(buffer[1][0][0] or buffer[1][0][1] or buffer[1][0][2]))
    zprava.append(int(buffer[1][1][0] or buffer[1][1][1] or buffer[1][1][2]))
    zprava.append(int(buffer[1][2][0] or buffer[1][2][1] or buffer[1][2][2]))
    zprava.append(int(buffer[1][3][0] or buffer[1][3][1] or buffer[1][3][2]))
    zprava.append(int(buffer[1][4][0] or buffer[1][4][1] or buffer[1][4][2]))
    zprava.append(int(buffer[1][5][0] or buffer[1][5][1] or buffer[1][5][2]))
    zprava.append(int(buffer[1][6][0] or buffer[1][6][1] or buffer[1][6][2]))
    zprava.append(int(buffer[1][7][0] or buffer[1][7][1] or buffer[1][7][2]))
    
    
    
    zprava.append(int(buffer[2][0][0] or buffer[2][0][1] or buffer[2][0][2]))
    zprava.append(int(buffer[2][1][0] or buffer[2][1][1] or buffer[2][1][2]))
    zprava.append(int(buffer[2][2][0] or buffer[2][2][1] or buffer[2][2][2]))
    zprava.append(int(buffer[2][3][0] or buffer[2][3][1] or buffer[2][3][2]))
    zprava.append(int(buffer[2][4][0] or buffer[2][4][1] or buffer[2][4][2]))
    zprava.append(int(buffer[2][5][0] or buffer[2][5][1] or buffer[2][5][2]))
    zprava.append(int(buffer[2][6][0] or buffer[2][6][1] or buffer[2][6][2]))
    zprava.append(int(buffer[2][7][0] or buffer[2][7][1] or buffer[2][7][2]))
    
    
    
    zprava.append(int(buffer[3][0][0] or buffer[3][0][1] or buffer[3][0][2]))
    zprava.append(int(buffer[3][1][0] or buffer[3][1][1] or buffer[3][1][2]))
    zprava.append(int(buffer[3][2][0] or buffer[3][2][1] or buffer[3][2][2]))
    zprava.append(int(buffer[3][3][0] or buffer[3][3][1] or buffer[3][3][2]))
    zprava.append(int(buffer[3][4][0] or buffer[3][4][1] or buffer[3][4][2]))
    zprava.append(int(buffer[3][5][0] or buffer[3][5][1] or buffer[3][5][2]))
    zprava.append(int(buffer[3][6][0] or buffer[3][6][1] or buffer[3][6][2]))
    zprava.append(int(buffer[3][7][0] or buffer[3][7][1] or buffer[3][7][2]))
    
    
    
    zprava.append(int(buffer[4][0][0] or buffer[4][0][1] or buffer[4][0][2]))
    zprava.append(int(buffer[4][1][0] or buffer[4][1][1] or buffer[4][1][2]))
    zprava.append(int(buffer[4][2][0] or buffer[4][2][1] or buffer[4][2][2]))
    zprava.append(int(buffer[4][3][0] or buffer[4][3][1] or buffer[4][3][2]))
    zprava.append(int(buffer[4][4][0] or buffer[4][4][1] or buffer[4][4][2]))
    zprava.append(int(buffer[4][5][0] or buffer[4][5][1] or buffer[4][5][2]))
    zprava.append(int(buffer[4][6][0] or buffer[4][6][1] or buffer[4][6][2]))
    zprava.append(int(buffer[4][7][0] or buffer[4][7][1] or buffer[4][7][2]))
    
    
    
    zprava.append(int(buffer[5][0][0] or buffer[5][0][1] or buffer[5][0][2]))
    zprava.append(int(buffer[5][1][0] or buffer[5][1][1] or buffer[5][1][2]))
    zprava.append(int(buffer[5][2][0] or buffer[5][2][1] or buffer[5][2][2]))
    zprava.append(int(buffer[5][3][0] or buffer[5][3][1] or buffer[5][3][2]))
    zprava.append(int(buffer[5][4][0] or buffer[5][4][1] or buffer[5][4][2]))
    zprava.append(int(buffer[5][5][0] or buffer[5][5][1] or buffer[5][5][2]))
    zprava.append(int(buffer[5][6][0] or buffer[5][6][1] or buffer[5][6][2]))
    zprava.append(int(buffer[5][7][0] or buffer[5][7][1] or buffer[5][7][2]))
    
    
    
    zprava.append(int(buffer[6][0][0] or buffer[6][0][1] or buffer[6][0][2]))
    zprava.append(int(buffer[6][1][0] or buffer[6][1][1] or buffer[6][1][2]))
    zprava.append(int(buffer[6][2][0] or buffer[6][2][1] or buffer[6][2][2]))
    zprava.append(int(buffer[6][3][0] or buffer[6][3][1] or buffer[6][3][2]))
    zprava.append(int(buffer[6][4][0] or buffer[6][4][1] or buffer[6][4][2]))
    zprava.append(int(buffer[6][5][0] or buffer[6][5][1] or buffer[6][5][2]))
    zprava.append(int(buffer[6][6][0] or buffer[6][6][1] or buffer[6][6][2]))
    zprava.append(int(buffer[6][7][0] or buffer[6][7][1] or buffer[6][7][2]))
    
    
    
    zprava.append(int(buffer[6][0][0] or buffer[7][0][1] or buffer[7][0][2]))
    zprava.append(int(buffer[7][1][0] or buffer[7][1][1] or buffer[7][1][2]))
    zprava.append(int(buffer[7][2][0] or buffer[7][2][1] or buffer[7][2][2]))
    zprava.append(int(buffer[7][3][0] or buffer[7][3][1] or buffer[7][3][2]))
    zprava.append(int(buffer[7][4][0] or buffer[7][4][1] or buffer[7][4][2]))
    zprava.append(int(buffer[7][5][0] or buffer[7][5][1] or buffer[7][5][2]))
    zprava.append(int(buffer[7][6][0] or buffer[7][6][1] or buffer[7][6][2]))
    zprava.append(int(buffer[7][7][0] or buffer[7][7][1] or buffer[7][7][2]))
    
    
    i2c.writeto(adresa_ATmegy, bytearray(zprava))

buf = [
    [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[1,0,0],[0,0,0],[0,0,0],[1,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[1,0,0],[0,0,0],[0,0,0],[1,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[1,0,0],[0,0,0],[0,0,0],[1,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[1,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[1,0,0],[0,0,0]],
    [[0,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    ]

posli_buffer_mono(buf)

while True:
    buf[random.randint(0,7)][random.randint(0,7)][0] = random.randint(0,1)
    posli_buffer_mono(buf)
    sleep(0.1)
