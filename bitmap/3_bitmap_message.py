import sys
# check Pillow version number
import PIL

print('Pillow Version:', PIL.__version__)

# load and show an image with Pillow
from PIL import Image
from numpy import asarray

# Open the image form working directory
image = Image.open('bitmap/Max.jpg')
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

print(data)

bitmap = """
....................................................................
  ************** * *** ** * ******************************
  ********************* ** ** * * ****************************** *
 **      ***************** ******************************
 ************* ** * **** ** ************** *
 ********* ******* **************** * *
 ******** *************************** *
 * * **** *** *************** ****** ** *
 **** * *************** *** *** *
 ****** ************* ** ** *
 ******** ************* * ** ***
 ******** ******** * *** ****
 ********* ****** * **** ** * **
 ********* ****** * * *** * *
 ****** ***** ** ***** *
 ***** **** * ********
 ***** **** *********
 **** ** ******* *
 *** * *
 ** * *
 ...................................................................."""
print('Enter the message to display with the bitmap.')

message = input('> ')
if message == '':
    sys.exit()

# Loop over each line in the bitmap:
for line in bitmap.splitlines():
    for i, bit in enumerate(line):
        if bit == ' ':
            print(' ', end='')
        else:
            print(message[i % len(message)], end='')
    print()
