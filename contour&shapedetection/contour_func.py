import cv2

img=cv2.imread(r"C:\Users\Lenovo\OneDrive\Desktop\dataScience\Open CV\triangle.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh=cv2.threshold(gray,240,255,cv2.THRESH_BINARY)# _ use as placeholder for anoher term we cannot waste maemory

#find contours
contour,heirarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for con in contour:
    approx=cv2.approxPolyDP(con,0.12*cv2.arcLength(con,True),True)
    corners=len(approx)
    if corners==3:
        shape_name="triangle"
    elif corners==4:
        shape_name="rectangle"
    elif corners>5:
       shape_name="circle"
    else:
        shape_name="unkmown"
    cv2.drawContours(img,[approx],0,(255,0,0),2)
    x=approx.ravel()[0]
    y=approx.ravel()[1]-10
    cv2.putText(img,shape_name,(x,y),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.6,(0,0,255),2)
cv2.imshow("contour",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


