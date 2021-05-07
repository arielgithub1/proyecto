import cv2
import os

os.chdir(r'C:\Users\mafer_ijqyjv9\Desktop\Filtro_Python')

cap = cv2.VideoCapture(0)

cont = 0

while True:
    ret, img = cap.read()
    
    if ret:
        name = 'frame'+str(cont)+'.jpg'
        print('Creating...' + name)
        
        if 0<=cont<=5:
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.GaussianBlur(img_gray, (21,21), 0, img_gray)
            edges = cv2.Canny(img_gray,10,20,apertureSize = 3)
            cv2.imwrite(name,edges)
        
        elif 5<cont<=10:
            img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            cv2.imwrite(name,img_gray)

        elif 10<cont<=15:
            img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            cv2.imwrite(name, img_HSV)
        
        elif 15<cont<=20:
            img_Blur = cv2.GaussianBlur(img, (21,21), 0, img_gray)
            cv2.imwrite(name,img_Blur)
            
        else:
            break
        
        cont += 1
        
cap.release()
cv2.destroyAllWindows()