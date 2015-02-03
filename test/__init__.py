from PIL import Image, ImageFilter
from imgStat import *

try:
    original = Image.open("D:/workspace01/150130_scrapers/img/Google_building+on+sloped+land_0.JPEG")
except:
    print "Unable to load image"

print "The size of the Image is: "
print(original.format, original.size, original.mode)

# Blur the image
blurred = original.filter(ImageFilter.CONTOUR)


rgb_im = original.convert('RGB')
gr_im = original.convert('LA').convert('RGB')

print greeness(rgb_im, 150)
print whiteness(rgb_im, 255)
print likeness_img(rgb_im, (0,0,0), 0.8)