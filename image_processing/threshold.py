import cv2
img=cv2.imread('image.png',0)
ret,thres_img=cv2.threshold(img,80,255,cv2.THRESH_BINARY)
cv2.imshow("image",img)
cv2.imshow("threshold image",thres_img)

cv2.waitKey(0)
cv2.destroyAllWindows()