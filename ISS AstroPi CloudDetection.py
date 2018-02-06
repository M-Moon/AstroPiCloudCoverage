from scipy import misc
import matplotlib.pyplot as plt
import numpy as np
import os
f = open("Data.txt","w")

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




def validate_image(image):    
    pass




def count_cloud(image):
    total = 0
    largest = 1
    goodPix = 0
    for x in range(640):
        for y in range(480):
            total+= image[y][x]
            if int(image[y][x]) != 0:
                goodPix+=1
            
            if image[y][x] !=0 and image[y][x] > largest :
                largest = float(image[y][x])
                
    return (total/goodPix)/(255)



def gray_image(im, weights = np.c_[0.2989, 0.587, 0.114]):
  tile = np.tile(weights, reps=(im.shape[0],im.shape[1],1))
  return np.sum(tile * im, axis=2)



def circle_center(image):
  lx, ly = image.shape[:-1]
  X, Y = np.ogrid[0:lx,0:ly]

  mask = (X-lx/2)**2 + (Y-ly/2)**2 > (lx * ly) / 5
  
  image[mask] = 0

  return image



def main():
    img = os.listdir('testimages/')[17]
    img = read_image(img)
    img = circle_center(img)
    img = gray_image(img)
    print(count_cloud(img))
    show_image(img)
main()
