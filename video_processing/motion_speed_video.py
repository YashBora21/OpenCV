import cv2 
cap=cv2.VideoCapture("recorded.avi")
while True:
    ret,frame=cap.read()
    
    if not ret:
        break
    cv2.imshow("video",frame)
# as wait time incerses video speed decreases as wait time decreases video playback spped increases form normal it 25-35
    if cv2.waitKey(20)& 0xFF==ord('q'):
        print("quitting")
        break
cap.release()
cv2.destroyAllWindows()
