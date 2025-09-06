import cv2
import numpy as np

im1=np.zeros((300,300),np.uint8)
im2=np.zeros((300,300),np.uint8)
img1=cv2.imread("image.png",0)#183, 275,
img2=cv2.imread("eagle-close-up-clipart-desktop-wallpaper.jpg",0)
img2=cv2.resize(img2,(275,183))

"""cv2.circle(im1,(150,150),100,255,-1)
cv2.rectangle(im2,(100,100),(250,250),(255,0,0),-1)
bit_and=cv2.bitwise_and(im1,im2)
bit_or=cv2.bitwise_or(im1,im2)
bit_not=cv2.bitwise_not(im1)
cv2.imshow("image1",im1)
cv2.imshow("image2",im2)
cv2.imshow("and",bit_and)
cv2.imshow("or",bit_or)
cv2.imshow("not",bit_not)"""
bit_and=cv2.bitwise_and(img1,img2)
bit_or=cv2.bitwise_or(img1,img2)
bit_not=cv2.bitwise_not(img1)
cv2.imshow("image1",img1)
cv2.imshow("image2",img2)
cv2.imshow("and",bit_and)
cv2.imshow("or",bit_or)
cv2.imshow("not",bit_not)
cv2.waitKey(0)
cv2.destroyAllWindows()
