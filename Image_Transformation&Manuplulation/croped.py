import cv2
img=cv2.imread("eagle-close-up-clipart-desktop-wallpaper.jpg")
if img is not None:
    print("loaded")
else:
    print("error")
cropped=img[100:199,50:149]
cv2.imshow("orignal_img",img)
cv2.imshow("corpped_image",cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
