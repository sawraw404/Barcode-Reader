from PIL import Image
import numpy as np

def decode(filename="output.png"):
    # 1. Load image
    img = Image.open(filename).convert("L")  # convert to grayscale
    arr = np.array(img)
    height, width = arr.shape
    scan_row = 200  # Fixed: scan at row 200 as per assignment
    row = arr[scan_row] < 128  # True for black pixels

    print(f"Image size: {width}x{height}")
    print(f"Scanning row: {scan_row}")
    print(f"Black pixels found: {np.sum(row)}")

    # 2. Decode by measuring consecutive black pixel runs
    result = ""
    i = 0
    bar_count = 0
    while i < width:
        if row[i]:  # black pixel
            w = 0
            while i < width and row[i]:
                w += 1
                i += 1
            bar_count += 1
            print(f"Bar {bar_count}: width = {w}")
            if w == 1:
                result += " "
                print(f"  -> Added space")
            else:
                pos = w - 1  # width = pos + 1, so pos = width - 1
                if 1 <= pos <= 26:  # 'a'=1, 'b'=2, ..., 'z'=26
                    char = chr(ord("a") + pos - 1)  # Convert back: pos 1 -> 'a', pos 2 -> 'b', etc.
                    result += char
                    print(f"  -> Added character: {char}")
                else:
                    result += "?"  # unexpected width
                    print(f"  -> Added ? (unexpected width: {w})")
        else:
            i += 1  # skip white pixels

    print("Decoded text:", result)
    return result
if __name__ == "__main__":
    decode("output.png")
