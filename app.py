#!/usr/bin/env python3
from PIL import Image, ImageOps
import matplotlib.pyplot as plt

img = Image.open( "./data/good-apple/9.jpg", "rb" )
print( "This is size of original image: ", img.size(), "\n" )
