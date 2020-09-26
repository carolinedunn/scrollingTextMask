#!/usr/bin/env python3
import time
import sys
import board
import neopixel
from colorsys import hsv_to_rgb
from PIL import Image, ImageDraw, ImageFont
from flask import Flask, jsonify, request, redirect, render_template, url_for

app = Flask(__name__)

pixel_pin = board.D21
num_pixels = 256
display_width = 32
display_height = 8
matrixbrightness = 0.2
scrollSpeed = 0.12 #adjust the scrolling speed here, smaller number=faster scroll
TextColor = (255,255,255) #set the color of your text here in RGB, default is white
repeats = 2 #number of times the text will scroll across the matrix

ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=matrixbrightness, auto_write=False, pixel_order=ORDER)
rotation = 0

#load your font
font = ImageFont.truetype("LiberationMono-Regular.ttf", 8)
#5x7.ttf font is easier to read and available for download for personal use from the Internet
#font = ImageFont.truetype("5x7.ttf", 8)

#for the Adafruit NeoMatrix grid
def getIndex(x, y):        
    x = display_width-x-1    
    return (x*8)+y

#use for the flex grid
def getIndex2(x, y):
    x = display_width-x-1
    if x % 2 != 0:
        return (x*8)+y
    else:
        return (x*8)+(7-y)

if len(sys.argv) > 1:
    try:
        rotation = int(sys.argv[1])
    except ValueError:
        print("Usage: {} <rotation>".format(sys.argv[0]))
        sys.exit(1)

def scrollText(text):
# Measure the size of our text, we only really care about the width for the moment
# but we could do line-by-line scroll if we used the height
    text_width, text_height = font.getsize(text)

# Create a new PIL image big enough to fit the text
    image = Image.new('P', (text_width + display_width + display_width, display_height), 0)
    draw = ImageDraw.Draw(image)
# clear grid
    pixels.fill((0,0,0))
    pixels.show()
    time.sleep(.001)
# Draw the text into the image
    draw.text((display_width, -1), text, font=font, fill=255)
    image.save("img.png", "PNG")
    offset_x = 0
    for i in range(repeats):
        while True:        
            for x in range(display_width):
                for y in range(display_height):                    
                    if image.getpixel((x + offset_x, y)) == 255:
                        pixels[getIndex2(x,y)] = TextColor                        
                    else:
                        pixels[getIndex2(x,y)] = (0, 0, 0)                               

            offset_x += 1
            if offset_x + display_width > image.size[0]:
                offset_x = 0
                break

            pixels.show()
            time.sleep(scrollSpeed) #scrolling text speed
        
    
@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        text_content = request.form['content']
        scrollText(text_content)
        text_content = " "
        return render_template('index.html')
    else:
        return render_template('index.html')
    
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
