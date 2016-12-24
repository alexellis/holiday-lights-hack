import time
from neopixel import Adafruit_NeoPixel
from sensors import PIR
import random

LED_COUNT      = 64      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 128     # Set to 0 for darkest and 255 for brightest
LED_CHANNEL    = 0       # PWM channel
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

def PIR_triggered(name):
    global alive
    print (name, "fired sensor")
    alive = 0

def light(v):
    brightness = random.randrange(128,255)
    ws2812.setBrightness(brightness)
    for index in range(0,16):
        r=0
        g=0
        b=0
        if (index +1) % 2 == v:
            r=255
            g=0
            b=0
        else:
            r=0
            g=0
            b=0
        ws2812.setPixelColorRGB(index, r, g, b)
        ws2812.show()

ws2812 = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
ws2812.begin()

brightness = 255
ws2812.setBrightness(brightness)

pause = 0.5
alive = 0

pir1 = PIR(17, "PIR1", PIR_triggered)
turnoff_timeout = 60 * 5

while (True):
    if(alive >= turnoff_timeout):
        for index in range (0,8):
            ws2812.setPixelColorRGB(index, 0, 0, 0)
        ws2812.show()
        time.sleep(1)    
    else:
        light(0)
        time.sleep(pause)
        light(1)
        time.sleep(pause)
    alive += 1
