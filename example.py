import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI

import ST7789 as TFT
import datetime
import os
import time
from gif import AnimatedGif

from PIL import Image, ImageDraw, ImageFont, ImageColor

import numpy as np

RST = 22            # Set GPIO pin# 15 (BCM 22) as reset control
DC  = 17            # Set GPIO pin# 11 (BCM 17) as DATA/command (NOT MOSI!)
LED = 27            # Set GPIO pin# 13 (BCM 27) as backlight control
SPI_PORT = 0
SPI_DEVICE = 0
SPI_MODE = 0b11
SPI_SPEED_HZ = 40000000
disp = TFT.ST7789(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=SPI_SPEED_HZ),
       mode=SPI_MODE, rst=RST, dc=DC, led=LED)

# Initialize display.
disp.begin()

# Clear display.
disp.clear()

def expand2square(pil_img, background_color):
    width, height = pil_img.size
    if width == height:
        return pil_img
    elif width > height:
        result = Image.new(pil_img.mode, (width, width), background_color)
        result.paste(pil_img, (0, (width - height) // 2))
        return result
    else:
        result = Image.new(pil_img.mode, (height, height), background_color)
        result.paste(pil_img, ((height - width) // 2, 0))
        return result

# Clear output and display a purple background
image1 = Image.new("RGB", (disp.width, disp.height), "PURPLE")
draw = ImageDraw.Draw(image1)
disp.display(image1)

gif_player = AnimatedGif(disp, width=240, height=240, folder=".")
