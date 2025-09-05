import cv2
imag=cv2.imread("image.png")
if imag is not None:
    print("loaded")
else:
    print("error")

print(imag.shape)#(183, 275, 3)
h,w,c=imag.shape
center=(w//2,h//2)
pt1=(50,75)
pt3=(50,75)
pt4=(250,20)
pt2=(250,75)
pt5=(250,125)
color=(255,0,0)
thickness=4
#to draw line
"""cv2.line(imag,pt1,pt2,color,thickness)
cv2.line(imag,pt3,pt4,color,thickness)"""
"""cv2.rectangle(imag,pt5,pt3,color,thickness)"""
cv2.circle(imag,center,50,color,thickness)
cv2.imshow("line drwa",imag)
cv2.waitKey(0)
cv2.destroyAllWindows()