from PIL import Image
import math
import webcolors


img = Image.open('mount.jpg')
maxRow = img.height
maxCol = img.width
if maxRow > 676:
    maxRow = 675
if maxCol > 676:
    maxCol = 675

rgb = webcolors.rgb_to_hex(img.getpixel((0, 0)))
strrgb = str(rgb)
argbrgb = '00' + strrgb[1: ]

Image.Image.close(img)


print(rgb)
print(strrgb)
print(argbrgb)



