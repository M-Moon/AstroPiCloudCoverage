#from scipy import misc
#f = misc.face()
#misc.imsave('face.png', f) # uses the Image module (PIL)
#
#import matplotlib.pyplot as plt
#plt.imshow(f)
#plt.show()

""" Firstly, file gathering will have to be written. The pictures folder is
separate, and one level above. Will have to be a small part of the code to
access that specific folder.

Them, the picture needs to be scanned as a whole while mostly considering the
edges. If the edges are too light, maybe not even requring grayscale but it
may still make it easier just to compare it (as a side, if it's a comparison
there may be problems concerning the middle. If both the porthole to see the
Earth is lit up, along with around the edges, the edges will appear comparatively
dark to the system; therefore, allowing the picture to be used as valid data.

"""

from scipy import misc
import matplotlib.pyplot as plt
import numpy as np
import os

#print(type(f), f.shape, f.dtype)

def read_image(image):
  f = misc.imread('testimages/{}'.format(image))
  return f

def show_image(image):
  plt.imshow(image)
  plt.show()

def choose_image(count):
  image = os.listdir('testimages/')[count]
  return image

def gray_image(image): #not working
  image = image.face(gray=True)
  return image

def circle_center(image): #not working
  face = misc.face(gray=True)
  lx, ly = face.shape
  X, Y = np.ogrid[0:lx,0:ly]

  mask = (X - lx / 2) ** 2 + (Y - ly / 2) ** 2 > lx * ly / 4
  face[mask] = 0

  return image[range(400), range(400)] == 255

img = choose_image(0)
img = read_image(img)
#img = gray_image(img)
#img = circle_center(img)
show_image(img)

