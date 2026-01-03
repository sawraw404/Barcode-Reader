# encode.py
from PIL import Image
import numpy as np

def encode(text):
    width, height = 400, 800  # Fixed: 400 width x 800 height as per assignment
    step = 9
    img = np.ones((height, width), dtype=np.uint8) * 255  # white canvas

    x = 0
    for ch in text:
        if ch == ' ':
            bar_width = 1
            top, bottom = 150, 250
            print(f"Space: width={bar_width}, x={x}-{x+bar_width}")
        else:
            pos = ord(ch.lower()) - ord('a') + 1  # 'a'=1, 'b'=2, 'c'=3, etc.
            bar_width = pos + 1  # 'a'=2, 'b'=3, 'c'=4, etc.
            top, bottom = 10, 350
            print(f"'{ch}': position={pos}, width={bar_width}, x={x}-{x+bar_width}")

        img[top:bottom, x:x+bar_width] = 0
        x += bar_width + step

    Image.fromarray(img).save('output.png')
    print("Barcode saved as output.png")

# Run example
encode("Syeda Sara Afzaal")
