import cv2
import numpy as np
image = cv2.imread('./images/flower.jpg')
cv2.imshow('Flower', input)
cv2.waitKey()
#-------------------------------------------------------------
#grayscale
image = cv2.imread('./images/flower.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', gray_image)
cv2.waitKey()
#Another method faster method
img = cv2.imread('./images/flower.jpg',0)
cv2.imshow('Grayscale', img)
cv2.waitKey()
#------------------------------------------------------------
image = cv2.imread('./images/flower.jpg')
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV image', hsv_image)
cv2.imshow('Hue channel', hsv_image[:, :, 0])
cv2.imshow('Saturation channel', hsv_image[:, :, 1])
cv2.imshow('Value channel', hsv_image[:, :, 2])
cv2.waitKey()
#---------------------------------------------------------------
image = cv2.imread('./images/flower.jpg')
B, G, R = cv2.split(image) 
zeros = np.zeros(image.shape[:2], dtype = "uint8")
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
cv2.waitKey(0)
#-------------------------------------------------------------------
#adding Text
image = np.zeros((512,512,3), np.uint8)
cv2.putText(image, 'Hello World!', (75,290), cv2.FONT_HERSHEY_COMPLEX, 2, (100,170,0), 3)
cv2.imshow("Hello World!", image)
cv2.waitKey(0)
#-------------------------------------------------------------------
#sharpening
image = cv2.imread('./images/flower.jpg')
cv2.imshow('Original', image)
kernel_sharpening = np.array([[-1,-1,-1], 
                              [-1,9,-1], 
                              [-1,-1,-1]])
sharpened = cv2.filter2D(image, -1, kernel_sharpening)
cv2.imshow('Image Sharpening', sharpened)
cv2.waitKey(0)

cv2.destroyAllWindows()