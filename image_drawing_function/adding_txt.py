import cv2
imag=cv2.imread("image.png")
if imag is not None:
    print("loaded")
else:
    print("error")

cv2.putText(imag,"this is SQUERIAL",(50,20),cv2.FONT_HERSHEY_COMPLEX_SMALL,1.0,(255,0,0),1)
cv2.imshow("image",imag)
cv2.waitKey(0)
cv2.destroyAllWindows()