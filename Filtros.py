import tkinter
import cv2
import time
import numpy as np

cap = cv2.VideoCapture(0)

ventana = tkinter.Tk()
ventana.geometry("460x460")

etiqueta = tkinter.Label(ventana, text="Filtros", bg= "blue", font= "Helvetica 20")
#etiqueta.pack(fill = tkinter.X)
def saludo():
	while cap.isOpened():
        
        #BGR image feed from camera
        	success,img = cap.read()    
        
	        if not success:
	            break
	        if img is None:
	            break
	        img_RGB=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)    
	        
	        cv2.imshow("Output", img_RGB)

	        k = cv2.waitKey(10)
	        if k==27:
	            break


	#cap.release()
	cv2.destroyAllWindows()
def saludos():
	while cap.isOpened():
        
        #BGR image feed from camera
        	success,img = cap.read()    
        
	        if not success:
	            break
	        if img is None:
	            break
	        img_RGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)    
	        
	        cv2.imshow("Output", img_RGB)

	        k = cv2.waitKey(10)
	        if k==27:
	            break


	#cap.release()
	cv2.destroyAllWindows()
	
def saludoss():
	while cap.isOpened():
        
        #BGR image feed from camera
        	success,img = cap.read()    
        
	        if not success:
	            break
	        if img is None:
	            break
	        img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #RGB
        	cv2.GaussianBlur(img_gray,(21,21),0,img_gray)
        	edges=cv2.Canny(img_gray,10,20,apertureSize = 3)   
	        
	        cv2.imshow("Output", edges)

	        k = cv2.waitKey(10)
	        if k==27:
	            break


	#cap.release()
	cv2.destroyAllWindows()	


def sobel():
	while cap.isOpened():
        
        #BGR image feed from camera
        	success,img = cap.read()    
        
	        if not success:
	            break
	        if img is None:
	            break
	        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
        	imgSobel1=cv2.Sobel(img,cv2.CV_8U,0,1,ksize=3)   
	        
	        cv2.imshow("Output", imgSobel1)

	        k = cv2.waitKey(10)
	        if k==27:
	            break
	cv2.destroyAllWindows()

def lapla():
	while cap.isOpened():
        
        #BGR image feed from camera
        	success,img = cap.read()    
        
	        if not success:
	            break
	        if img is None:
	            break
	        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
        	LaplacianIMG=cv2.Laplacian(img,cv2.CV_8U)   
	        
	        cv2.imshow("Output", LaplacianIMG)

	        k = cv2.waitKey(10)
	        if k==27:
	            break

	#cap.release()
	cv2.destroyAllWindows()	

def cannyv2():
	while cap.isOpened():
        
        #BGR image feed from camera
        	success,img = cap.read()    
        
	        if not success:
	            break
	        if img is None:
	            break
	        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
        	Canny=cv2.Canny(img,50,240)   
	        
	        cv2.imshow("Output", Canny)

	        k = cv2.waitKey(10)
	        if k==27:
	            break

	#cap.release()
	cv2.destroyAllWindows()	




boton1= tkinter.Button(ventana, text= "B&W", padx = 40, pady= 40, command = saludo,width = 9, height = 5)
boton2= tkinter.Button(ventana, text= "RGB", padx = 40, pady= 40, command = saludos,width = 9, height = 5)
boton3=tkinter.Button(ventana, text= "Canny", padx =40, pady=40, command= saludoss, width = 9, height = 5)
boton4= tkinter.Button(ventana, text= "Sobel", padx = 40, pady= 40, command = sobel,width = 9, height = 5)
boton5= tkinter.Button(ventana, text= "Laplacian", padx = 40, pady= 40, command = lapla,width = 9, height = 5)
boton6= tkinter.Button(ventana, text= "Canny_V2", padx = 40, pady= 40, command = cannyv2,width = 9, height = 5)

boton1.grid(row=0, column= 0)
boton2.grid(row=0, column= 1)
boton3.grid(row=0, column= 2)
boton4.grid(row=1, column= 0)
boton5.grid(row=1, column= 1)
boton6.grid(row=1, column= 2)
ventana.mainloop()