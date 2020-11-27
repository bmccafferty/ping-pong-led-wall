#!/usr/bin/python3
# LED Wall Snow
import time
import board
import neopixel
import random

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 256

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)


def let_it_snow(red, green, blue, SparkleDelay, SpeedDelay):

    # Set Background
    pixels.fill((red, green, blue))

    # Pick the snow sparkle Pixel
    sparkle = 0
    no_sparkle = 20
    while sparkle <= no_sparkle:
        pixels[random.randint(0, num_pixels)] = (255, 255, 255)
        sparkle = sparkle + 1
    pixels.show()
    time.sleep(SparkleDelay)
    pixels.fill((red, green, blue))
    pixels.show()
    time.sleep(SpeedDelay)


# Main Display Loop
while True:
    let_it_snow(10, 10, 10, 0.1, 0.5)
