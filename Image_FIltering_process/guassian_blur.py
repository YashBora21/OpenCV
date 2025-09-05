import cv2
img=cv2.imread(r"assignment\flag.png")
img=cv2.resize(img,(700,500))

blured_imag=cv2.GaussianBlur(img,(11,11),3)#as kernel inc blur inc it is matrix
cv2.imshow("orignal",img)
cv2.imshow("blured",blured_imag)
cv2.waitKey(0)
cv2.destroyAllWindows()