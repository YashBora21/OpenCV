import cv2

   
while True:
    opt=int(input("for catureing video press 1\n for saving video press 2:\n for exit press 0  "))

    if opt==0:break 
    elif opt==1:
        cap=cv2.VideoCapture(0)
        while True:
            ret,frame=cap.read()
            if not ret:
                break
            cv2.imshow("video",frame)
            if cv2.waitKey(1) & 0xFF==ord('q'):
                print('quitting...')
                break
        cap.release()
        cv2.destroyAllWindows()
    elif opt==2:
        cap=cv2.VideoCapture(0)
        frame_height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        frame_widht=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        codec=cv2.VideoWriter_fourcc(*'X264')
        recorder=cv2.VideoWriter("storedvideo.mp4",codec,20,(frame_widht,frame_height))
        while True:
            ret,frame=cap.read()
            if not ret:
                break
            recorder.write(frame)
            cv2.imshow("video",frame)
            if cv2.waitKey(1) & 0xFF==ord('q'):
                print('quitting...')
                break
        cap.release()
        recorder.release()
        cv2.destroyAllWindows()
    
        
