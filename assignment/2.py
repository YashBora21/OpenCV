import cv2
img_path=input("enter the address of image")
img=cv2.imread(img_path)
color=(0,0,255)
if img is not None:

    
        while True:
            opt=int(input("enter\n1:to draw line\n2:to draw circle\n3:to draw rectangle\n4:to add a text\n0:to exit:"))
            if opt==0:break
            if(opt==1):
                widht,height=map(int,input("enter the widht and height repectively seprating by comma for point one:").split(','))
                widht1,height1=map(int,input("enter the widht and height repectively seprating by comma for point two:").split(','))
                thickness=int(input("enter the thickness:"))
                cv2.line(img,(widht,height),(widht1,height1),color,thickness)
                cv2.imshow("image of operation",img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            elif(opt==2):
                widht,height=map(int,input("enter the widht and height repectively seprating by comma for center:").split(','))
                radius=int(input("eneter the radius of circle:"))
                thickness=int(input("enter the thickness:"))
                cv2.circle(img,(widht,height),radius,color,thickness)
                cv2.imshow("image of operation",img)

                cv2.waitKey(0)
                cv2.destroyAllWindows()
            elif(opt==3):
                widht,height=map(int,input("enter the widht and height repectively seprating by comma for top left most point:").split(','))
                widht1,height1=map(int,input("enter the widht and height repectively seprating by comma for bottom rightmost poin:").split(','))
                thickness=int(input("enter the thickness:"))
                cv2.rectangle(img,(widht,height),(widht1,height1),color,thickness)
                cv2.imshow("image of operation",img)

                cv2.waitKey(0)
                cv2.destroyAllWindows()
            elif opt==4:
                text=input("enter the dext that you want to on image:")
                font_scale=int(input("enter the font scale"))
                widht,height=map(int,input("enter the widht and height repectively seprating by comma for orgin fo text:").split(','))
                cv2.putText(img,text,(widht,height),cv2.FONT_HERSHEY_SIMPLEX,1,color,2)
                cv2.imshow("image of operation",img)

                cv2.waitKey(0)
                cv2.destroyAllWindows()

            

