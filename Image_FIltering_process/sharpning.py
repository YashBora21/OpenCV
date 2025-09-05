import cv2
import numpy as np
img=cv2.imread("download.jpeg")
sharpen_kernel=np.array([
    [0,-1,0],
    [-1,6,-1],
    [0,-1,0]
])

sharp_image=cv2.filter2D(img,-1,sharpen_kernel)#as kernel inc blur inc it is matrix
cv2.imshow("orignal",img)
cv2.imshow("sharp_image",sharp_image)
cv2.waitKey(0)
cv2.destroyAllWindows()