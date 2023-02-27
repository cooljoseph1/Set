import glob

from PIL import Image
import numpy as np

cards = [np.array(Image.open(file).convert("RGB")) / 255 for file in glob.glob("cards/*.png")]
blank = np.ones(cards[0].shape)

height, width, _ = blank.shape

for i in range(0, len(cards), 8):
    group = cards[i:i+8]
    group = group + [blank] * (8 - len(group))
    sheet = np.zeros((height*4, width*2, 3))
    for y in range(4):
        for x in range(2):
            sheet[height*y:height*(y+1), width*x:width*(x+1)] = group[y+4*x]

    image = Image.fromarray((sheet * 255).astype("uint8"))
    image.save("sheets/" + str(i//8 + 1) + ".png")
