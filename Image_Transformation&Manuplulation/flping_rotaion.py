import cv2
img=cv2.imread("image.png")
if img is not None:
    print("loaded")
else:
    print("error")

h,w,c=img.shape
center_point =(w//2,h//2)
m=cv2.getRotationMatrix2D(center_point,45,0.5)
rotated=cv2.warpAffine(img,m,(w,h))
flipped_horizontal=cv2.flip(img,0)
flipped_vertical=cv2.flip(img,1)
flipped_both=cv2.flip(img,-1)
cv2.imshow("original",img)
cv2.imshow("h",flipped_horizontal)
cv2.imshow("v",flipped_vertical)
cv2.imshow("both",flipped_both)

cv2.imshow("rotated",rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()