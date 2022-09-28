#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Jun 14 12:31:04 2022

@author: inderjeet
"""

# import the necessary file
import cv2



# load the image from disk via "cv2.imread" and then spatial
# dimensions, including width, height, and number of channels
image=cv2.imread("/home/inderjeet/Desktop/Opencv/data/image1.jpeg")
(h,w,c)=image.shape[:3]



# display the image width, height,  and number of channels
print("width : {} pixels".format(w))
print("height : {} pixels".format(h))
print("channels : {} ".format(c))

# show the image and wait for a keypress
cv2.imshow("Image",image)
cv2.waitKey(0)

# save the image back to disk (opencv handle converting image filetypes automatically)
cv2.imwrite("newimage.jpg",image)

