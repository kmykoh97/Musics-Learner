# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 19:48:17 2018

@author: kmykoh
"""

import numpy as np
from scipy import imread, imsave, imresize

# read an JPEG image into a numpy array
img = imread('download.jpg')
print(img.dtype, img.shape)  # Prints "uint8 (400, 248, 3)"