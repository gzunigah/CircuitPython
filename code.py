import time
from adafruit_circuitplayground import cp
cp.pixels.brightness = 0.1

while True:
    if cp.switch:
        for i in range(0, 10):
            time.sleep(1)
            cp.pixels[i] = (0,50,0)
    else:
        for j in range(9, -1, -1):
            time.sleep(1)
            cp.pixels[j] = (100,0,0)
