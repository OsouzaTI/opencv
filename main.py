import cv2, numpy as np

img = cv2.imread('D:\Computer_Science\Python\opencv\pau45.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bitwise_not(gray)
cv2.imshow('gray', gray)

coords = np.column_stack(np.where(gray > 0))
angle = cv2.minAreaRect(coords)[-1]
print(angle)

cv2.waitKey(0)
cv2.destroyAllWindows()
