import board
import neopixel

NUM_LEDS = 300

pixels = neopixel.NeoPixel(board.D18, NUM_LEDS)

num_cycles = 5
colors = [(255,0,0), (0,255,0), (0,0,255)]

##
# upper_bound and lower_bound are inclusive
##
def keep_val_in_bounds(val, upper_bound, lower_bound):
    if val > upper_bound:
        return lower_bound
    elif val < lower_bound:
        return upper_bound
    else:
        return val

def alternating_flow():
    for i in range(0, num_cycles):
        for color in colors:
            for pixel in range(0,NUM_LEDS):
               pixels[pixel] = color

##
# switch between two colors
##
def switching_colors(start_col, other_col):
    r_val = start_col[0]
    g_val = start_col[1]
    b_val = start_col[2]
    
    x = 0
    arr = [x%2 for x in range(0,300)]
    cols = [start_col if x==1 else other_col for x in arr]
    pixels[0:NUM_LEDS] = cols[0:NUM_LEDS]
    
switching_colors((255,0,0), (0,255,0))