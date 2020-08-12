import numpy as np
from PIL import Image, ImageDraw, ImageFont



def annotate_image(im, annotation, pos):
    _, h, _           = im.shape
    im                = Image.fromarray(im)
    draw              = ImageDraw.Draw(im)
    font_h            = round(h / 32)
    font              = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', font_h)
    draw.text(pos, annotation, (255, 255, 255), font=font)

    return np.array(im)