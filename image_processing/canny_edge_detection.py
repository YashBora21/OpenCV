import cv2
img=cv2.imread('image.png',0)
edges=cv2.Canny(img,50,150)
cv2.imshow("image",img)
cv2.imshow("edges",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()