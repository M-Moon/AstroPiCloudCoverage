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
