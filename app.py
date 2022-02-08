#!/usr/bin/env python3
from PIL import Image, ImageOps
import matplotlib.pyplot as plt

#hours_a_day = [ 4,   6,   8,  12,  16, 20, 22 ]      #time elapsed to the projects per day (max 24 ours, min != 0)   x = hours_a_day = [0;24]
#success     = [ 100, 100, 95, 75,  50, 20, 0  ]      # % syccessfully completed projects                             y = success = [0; 100]
#plt.plot( hours_a_day, success, color = 'red',  linestyle = 'solid', linewidth = 1, marker = '.' )
#plt.show()

img = Image.open( "./data/good-apple/9.jpg" )
print( "This is size of original image: ", img.size, "\n" )
plt.figure()
plt.imshow( img, interpolation = "nearest" )
plt.show()
