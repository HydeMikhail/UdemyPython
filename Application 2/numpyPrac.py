#!/usr/bin/env python
'''
DOCSTRING
'''
import cv2
import numpy

img = cv2.imread("E:\\Documents\\Scripts\\Udemy Classes\\UdemyPython\\Application 2\\Imgs\\smallgray.png", 0)

print(img)

img_g = cv2.imread("U:\\Documents\\GitCode\\UdemyPython\\Application 2\\Imgs\\smallgray.png", 0)
img_c = cv2.imread("U:\\Documents\\GitCode\\UdemyPython\\Application 2\\Imgs\\smallgray.png", 1)

#Write an img file based on pixel/color array
'''
cv2.imwrite("U:\\Documents\\GitCode\\UdemyPython\\Application 2\\Imgs\\newimg.png", img_c)

print(img_g)
print(img_c)
'''

#Accessing Numpy Indecies
'''
print(img_g)
print("\n")
print(img_g[0:2,2:4])
'''

#Iterating Numpy Arrays
'''
#Rows
for i in img_g:
    print(i)
print("\n")

#Columns
for i in img_g.T:
    print(i)
print("\n")

#One by one row to column
for i in img_g.flat:
    print(i)
'''

#Splitting and Stacking Numpy Arrays
'''
#Horizontal Stack
imst_h = numpy.hstack((img_g, img_g)) #Be sure to pass Tuple
print(imst_h)

#Vertical Stack
imst_v = numpy.vstack((img_g, img_g))
print(imst_v)

#Horizontal Split
imsp_h = numpy.hsplit(imst_h, 5)
print(imsp_h)

#Vertical Split
imsp_v = numpy.vsplit(imst_v, 3)
print(imsp_v)
'''

