# encode.py
from PIL import Image
import numpy as np

def encode(text):
    width, height = 800, 400
    step = 9
    img = np.ones((height, width), dtype=np.uint8) * 255  # white canvas

    x = 0
    for ch in text:
        if ch == ' ':
            bar_width = 1
            top, bottom = 150, 250
        else:
            pos = ord(ch.lower()) - ord('a')
            bar_width = pos + 1
            top, bottom = 10, 350

        img[top:bottom, x:x+bar_width] = 0
        x += bar_width + step

    Image.fromarray(img).save('output.png')
    print("Barcode saved as output.png")

# Run example
encode("Syeda Sara Afzaal")
