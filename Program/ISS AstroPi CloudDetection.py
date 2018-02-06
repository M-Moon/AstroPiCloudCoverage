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
  if len(image.shape) == 3:
    show_image_rgb(image)
  else:
    show_image_gray(image)

def show_image_rgb(image):
  plt.imshow(image)
  plt.show()

def show_image_gray(image):
  plt.imshow(image, cmap= plt.cm.Greys_r)
  plt.show()

def choose_image(count):
  image = os.listdir('testimages/')[count]
  return image

def validate_image(image):
  mask = circle_outer(image)
  if average_colour(image, mask) > 100:
    return False
  return True

def average_colour(img, _mask = None):
  if _mask is None:
    print("Meh")
  else:
    maskedImg = np.ma.array(img, mask = _mask)
    return maskedImg.mean()

def gray_image(im, weights = np.c_[0.2989, 0.587, 0.114]): #not working
  """
    Transforms a colour image to a greyscale image by
    taking the mean of the RGB values, weighted
    by the matrix weights
    """
  tile = np.tile(weights, reps=(im.shape[0],im.shape[1],1))
  return np.sum(tile * im, axis=2)

def circle_center(image):
  lx, ly = image.shape
  X, Y = np.ogrid[0:lx,0:ly]

  mask = (X - lx / 2) ** 2 + (Y - ly / 2) ** 2 > lx * ly / 5
  
  image[mask] = 0

  return image

def circle_outer(image):
  lx, ly = image.shape
  X, Y = np.ogrid[0:lx,0:ly]

  mask = (X - lx / 2) ** 2 + (Y - ly / 2) ** 2 < lx * ly / 3
  
  return mask

def count_cloud(image):
  total, largest, goodPix = 0, 1, 0
  for x in range(640):
    for y in range(480):
      total += image[y][x]
      if int(image[y][x]) != 0:
        goodPix += 1

      if image[y][x] != 0 and image[y][x] > largest:
        largest = float(image[y][x])

  return ((total/goodPix)/255) * 100

def main():
  for i in range(len(os.listdir('testimages/'))):

    img = choose_image(i)
    img = read_image(img)
    img = gray_image(img)
    if validate_image(img):
      img = circle_center(img)
      cloudPercent = count_cloud(img)
      print(int(cloudPercent), "%", os.listdir('testimages/')[i])

  #show_image(img)

main()
