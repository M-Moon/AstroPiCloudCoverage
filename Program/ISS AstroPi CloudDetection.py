from scipy import misc
import skimage
import matplotlib.pyplot as plt
import numpy as np
import os

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
    pass

def grey_image(im, weights = np.c_[0.2989, 0.587, 0.114]): #not working
    """
    Transforms a colour image to a greyscale image by
    taking the mean of the RGB values, weighted
    by the matrix weights
    """
    tile = np.tile(weights, reps=(im.shape[0],im.shape[1],1))
    return np.sum(tile * im, axis=2)

def getCircleInnerMask(image):
    lx, ly = image.shape
    X, Y = np.ogrid[0:lx,0:ly]
    mask = (X - lx / 2) ** 2 + (Y - ly / 2) ** 2 > lx * ly / 5
    return mask

def getCircleOuterMask(image):
    lx, ly = image.shape
    X, Y = np.ogrid[0:lx,0:ly]
    mask = (X - lx / 2) ** 2 + (Y - ly / 2) ** 2 < lx * ly / 3
    return mask

def averageColour(img, _mask = None):
    maximum = 255
    if _mask is None:
        mean = img.mean()
        darkestColour = np.min(img)
    else:
        maskedImg = np.ma.array(img, mask = _mask)
        mean = maskedImg.mean()
        darkestColour = np.min(maskedImg)
    # Linear Interpolation of mean, bounded between the darkest colour and pure white
    normalisedMean = (mean - darkestColour) / (maximum - darkestColour)
    return normalisedMean

def main():
    img = choose_image(10)
    img = read_image(img)
    img = grey_image(img)
    mask = getCircleInnerMask(img)
    invMask = getCircleOuterMask(img)

    print("Inner Mask:", averageColour(img, mask))
    print("Outer Mask:", averageColour(img, invMask))

    show_image(img)

main()
