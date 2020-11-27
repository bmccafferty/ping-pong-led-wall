#!/usr/bin/python3
# LED Wall Snow
import time
import board
import neopixel

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
	px_sparkle = random(num_pixels)
	pixels[px_sparkle] = (0, 0, 0)
	pixels.show()
	time.sleep(SparkleDelay)
	pixels[px_sparkle] = (red, green, blue)
	pixels.show()
	time.sleep(SpeedDelay)

def clear_all_pixels():
	px_no = 0
	while px_no <= num_pixels:
		pixels[px_no] = (0, 0, 0)
		pixels.show()

# Main Display Loop
while True:
	let_it_snow(10, 10, 10, 20, random(100,1000))