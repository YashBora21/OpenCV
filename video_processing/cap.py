import cv2
cap=cv2.VideoCapture(0)#internal webcam
while True:
    ret,frame=cap.read()#either return true or false frame
    if not ret:
        print("error")
        break
    cv2.imshow("webcam",frame)
    #wait until each 1 msec if user press q stop video and close program this is use get the right ascii key and ord it give the ascii value
    if cv2.waitKey(1)& 0xFF==ord('q'): 
        print('quitting')
        break
cap.release()
cv2.destroyAllWindows()
