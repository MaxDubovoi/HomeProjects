import sys
# check Pillow version number
import PIL
import numpy as np

print('Pillow Version:', PIL.__version__)

# load and show an image with Pillow
from PIL import Image
from numpy import asarray

# Open the image form working directory
try:
    image = Image.open('bitmap/Max.jpg')
except FileNotFoundError:
    print("File Not Found")
# summarize some details about the image
print(image.format)
print(image.size)
print(image.mode)

# convert image to numpy array
data = asarray(image)
print(type(data))
# summarize shape
print(data.shape)

# create Pillow image
image2 = Image.fromarray(data)
print(type(image2))

# summarize image details
print(image2.mode)
print(image2.size)

im = np.array(image.convert('L'))  # you can pass multiple arguments in single line
print(type(im))

gr_im = Image.fromarray(im).resize((50, 50)).save('bitmap/gr_max.png')
print(np.mean(im))
bl_im = im <= np.mean(im)
print(bl_im)

print('Enter the message to display with the bitmap.')

message = input('> ')
if message == '':
    sys.exit()

# Loop over each line in the bitmap:
for line in bl_im:
    for i, bit in enumerate(line):
        if bit:
            print(message[i % len(message)], end='')

        else:
            print(' ', end='')
    print()
