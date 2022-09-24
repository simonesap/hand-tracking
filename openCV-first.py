import cv2 as cv

# Open img
img = cv.imread('./assets/img/1664017473528.jpg')

cv.imshow('Cat', img)

cv.waitKey(0)