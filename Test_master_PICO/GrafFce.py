from Master_code import *
import time
import random

tts = 5

buf = [
    [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
    [[1,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    ]

# Zaplnění obrazovky
for x in range(8):
    barva = random.randint(0,2)
    buf[x][x][barva] = 1
    print("---")
    for i in range(8):
        print(buf[i])
    posli_buffer_rgb(buf)
    time.sleep(tts)
    
# Posouvání obrazovky
x = 6
narust = False
while True:
    # Řádek kde to mizí
    for i in range(8):
        buf[0][i] = [0,0,0]
        
    # Posun
    for i in range(7):
        for j in range(8):
            buf[i][j] = buf[i+1][j]
    
    # Přidání novýho
    for i in range(8):
        buf[7][i] = [0,0,0]
    barva = random.randint(0,2)
    buf[7][x][barva] = 1
    
    if narust:
        x += 1
        if x == 7:
            narust = False
    else:
        x -= 1
        if x == 0:
            narust = True
    
    posli_buffer_rgb(buf)
    time.sleep(tts)
