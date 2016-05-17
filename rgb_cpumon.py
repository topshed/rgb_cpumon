from gpiozero import RGBLED
import psutil, colorsys, time

myled = RGBLED(14,18,15)
            
while True:
    cpu = psutil.cpu_percent()
    r = cpu / 100.0 
    g = (100 - cpu)/100.0
    b = 0
    myled.color = (r,g,b)
    time.sleep(0.1)
