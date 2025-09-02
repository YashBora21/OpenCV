import cv2
img_path=input(("enter the the path of image: "))
img=cv2.imread(img_path)
if img is not None:
    gray_scaled_img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    choice=input("for showing image press:1: \n for saving press:2: ")
    if choice=="1":
        cv2.imshow("flag",gray_scaled_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif choice=="2":
        cv2.imwrite("output.png",gray_scaled_img)
    else:
        exit(0)
   


        

