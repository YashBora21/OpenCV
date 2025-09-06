import cv2
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
img=cv2.imread("images_m.jpeg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
for (x,y,w,h)in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    faces_roi=gray[y:y+h,x:x+w]
    """_,thresh=cv2.threshold(faces_roi,240,255,cv2.THRESH_BINARY)
    contour,heirarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img[y:y+h,x:x+w],contour,-1,(0,255,0),3)"""
cv2.imshow("Face Contours", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

