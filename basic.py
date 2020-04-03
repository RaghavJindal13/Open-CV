import cv2
input = cv2.imread('./images/flower.jpg')
cv2.imshow('Flower', input)
cv2.waitKey()
cv2.destroyAllWindows()