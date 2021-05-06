import cv2
import numpy as np

cap= cv2.VideoCapture(0)
while True:
    ret,img=cap.read()
    
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgSobel=cv2.Sobel(img,cv2.CV_8U,1,0,ksize=3)
    imgSobel1=cv2.Sobel(img,cv2.CV_8U,0,1,ksize=3)
    laplacianIMG=cv2.Laplacian(img,cv2.CV_8U)
    Canny=cv2.Canny(img,50,240)
    
    cv2.imshow("imagen1",imgSobel1)
    cv2.imshow("Laplacian",laplacianIMG)
    cv2.imshow("Canny",Canny)
    
    if cv2.waitKey(1)==27:
        break
cap.release()
    