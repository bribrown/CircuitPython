import adafruit_thermistor
import board
import time
import neopixel

thermistor = adafruit_thermistor.Thermistor(board.TEMPERATURE, 10000, 10000, 25, 3950)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.2)

while True:
    print("Temperature is: %f C and %f F" % (thermistor.temperature,
                                    (thermistor.temperature*9/5+32)))
    

    if (thermistor.temperature*9/5+32) >= 75:
        for i in range(len(pixels)):
            pixels[i] = (0,0,0)
        pixels[0] = (255,0,0)
    else:
        for i in range(len(pixels)):
            pixels[i] = (0,0,0)
        pixels[1] = (0,0,255)

    time.sleep(1)
