import cv2
img=cv2.imread("eagle-close-up-clipart-desktop-wallpaper.jpg")
if img is not None:
    print("loaded")
else:
    print("error")
resized_mg=cv2.resize(img,(300,300))
cv2.imshow("orignal img",img)
cv2.imshow("resized image",resized_mg)

cv2.imwrite("resizedimg.png",resized_mg)
cv2.waitKey(0)
cv2.destroyAllWindows()

