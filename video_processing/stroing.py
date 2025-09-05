import cv2 
camera=cv2.VideoCapture(0)
famee_widht=int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
famee_height=int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
codec=cv2.VideoWriter_fourcc(*'XVID')
recorder=cv2.VideoWriter("recorded.avi",codec,20,(famee_widht,famee_height))
while True:
    ret,frame=camera.read()
    if not ret:
        break
    recorder.write(frame)
    cv2.imshow("video",frame)
    if cv2.waitKey(1)& 0xFF==ord('q'):
        print("quitting")
        break
camera.release()
recorder.release()
cv2.destroyAllWindows()

