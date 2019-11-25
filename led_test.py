import board
import neopixel

NUM_LEDS = 300

pixels = neopixel.NeoPixel(board.D18, NUM_LEDS)

num_cycles = 5
colors = [(255,0,0), (0,255,0), (0,0,255)]

for i in range(0, num_cycles):
    for color in colors:
        for pixel in range(0,NUM_LEDS):
           pixels[pixel] = color

