from PIL import Image
import sys
import os

# CONSTANTS//GLOBALS
EPSILON = sys.float_info.epsilon
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
COLORS = [BLUE, RED]
PICTURE = Image.open('scatter.png')


def get_image(rsrp_value):
    width, height = PICTURE.size
    new_color, name = generate_color(rsrp_value)
    picture_name = "{}.png".format(name)
    picture_path = os.path.join(os.getcwd(),'images', picture_name)
    if os.path.exists(picture_path):
        return picture_path
    new_image = Image.new('RGBA', (width, height))
    pixels = new_image.load()
    for x in range(width-1):
        for y in range(height-1):
            color = PICTURE.getpixel( (x, y) )
            if color != 0:
                pixels[x,y] = (new_color)

    new_image.save(picture_path)

    return picture_path


def generate_color(val, minval=-50, maxval=20, colors=COLORS):
    i_f = float(val-minval) / float(maxval-minval) * (len(colors)-1)
    i, f = int(i_f // 1), i_f % 1
    if f < EPSILON:
        r,g,b = colors[i]
        rgb = '0x' + ''.join('{:02X}{:02X}{:02X}'.format(r, g, b))
        return (r,g,b), rgb
    else:
        (r1, g1, b1), (r2, g2, b2) = colors[i], colors[i+1]
        r,g,b = int(r1 + f*(r2-r1)), int(g1 + f*(g2-g1)), int(b1 + f*(b2-b1))
        rgb = '0x' + ''.join('{:02X}{:02X}{:02X}'.format(r,g,b))
        return (r,g,b), rgb


if __name__ == '__main__':
    pass