import cv2
image=cv2.imread('eagle-close-up-clipart-desktop-wallpaper.jpg',1)# reding image
if image is not None :
    #cv2.imshow("egale",image)#showing image 
    #cv2.waitKey(0)#wait time for image window until any key press
    #cv2.destroyAllWindows()#release the resources
  #  cv2.imwrite("output.png",image)#save the image
    h,w,c=image.shape
    print(f"image dimension:\nheight:{h}\nwidht:{w}\nchannel:{c}") #(2160, 3840, 3) if it's 3 para is 0 then img is grey scale 
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow("grey_scale",gray) 
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(gray.shape)#(2160, 3840) as it gray_scale
else:
    print("error")

