# This is my signature purple crown as seen on the PiCast Show
import time
import board
import neopixel
 
 
# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D21
 
# The number of NeoPixels
num_pixels = 256
 
# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB
 
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.3, auto_write=False, pixel_order=ORDER
)

PURPLE = 0x800080
crown2 = [0,14,15,16,18,28,31,32,36,42,47,48,53,59,63,64,67,77,79,80,81,93,95,96,99,107,110,111,112,114,117,121,124,127,128,129,132,135,137,140,143,144,146,149,155,158,159,160,163,173,175,176,177,189,191,192,195,203,207,208,213,218,223,224,228,236,239,240,242,254,255]

pink = 0xff6ec7

for i in crown2:
    pixels[i] = PURPLE
pixels.show()
time.sleep(2)

