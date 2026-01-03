from PIL import Image
import numpy as np
from collections import Counter

def decode(filename="output.png"):
    img = Image.open(filename).convert("L")
    arr = np.array(img)
    height, width = arr.shape
    mid = height // 2
    row = arr[mid] < 128

    # First pass: collect all white run lengths
    white_runs = []
    i = 0
    while i < width:
        if not row[i]:
            white_run = 0
            while i < width and not row[i]:
                white_run += 1
                i += 1
            white_runs.append(white_run)
        else:
            i += 1

    # Find the most common white run (between letters) and the next largest (between words)
    if white_runs:
        run_counts = Counter(white_runs)
        most_common = run_counts.most_common()
        letter_gap = most_common[0][0]
        # Find a gap at least twice as big as letter_gap (likely a space)
        space_gap = max([run for run in white_runs if run > letter_gap * 1.5], default=letter_gap * 2)
        threshold = (letter_gap + space_gap) // 2
    else:
        threshold = 3  # fallback

    # Second pass: decode
    result = ""
    i = 0
    while i < width:
        if row[i]:
            w = 0
            while i < width and row[i]:
                w += 1
                i += 1
            if 1 <= w <= 26:
                result += chr(ord("a") + (w - 1))
            else:
                result += "?"
        else:
            white_run = 0
            while i < width and not row[i]:
                white_run += 1
                i += 1
            if white_run >= threshold:
                result += " "

    print("Decoded text:", result)
    return result

if __name__ == "__main__":
    decode("output.png")
    