import cv2
import numpy as np
import face_recognition
#install cmake
#install visual c++ tools for cmake
#install dlib
#and install face_recognition

rostro = face_recognition.load_image_file("Misael.jpeg")
encoding = face_recognition.face_encodings(rostro)[0]

rostros_registrados = [encoding]
nombres_registrados = ["Yo"]

cap = cv2.VideoCapture(0)
fuente = cv2.FONT_HERSHEY_TRIPLEX
reduccion = 5

while True:

    coordenadas = [] 
    registro = []
    nombres_rostros = []
    nombre = ""

    ret, img = cap.read()
    if not ret:
        break

    img_rgb = img[:, :, ::-1]
    img_rgb = cv2.resize(img_rgb, (0, 0), fx = 1.0/reduccion, fy = 1.0/reduccion)
 
    loc_rostros = face_recognition.face_locations(img_rgb)
    registro = face_recognition.face_encodings(img_rgb, loc_rostros)

    for i in registro:
        rostros = face_recognition.compare_faces(rostros_registrados, i)
        if True in rostros:
            nombre = nombres_registrados[rostros.index(True)]
        else:
            nombre = "???"
        nombres_rostros.append(nombre)

    for (top, right, bottom, left), nombre in zip(loc_rostros, nombres_rostros):
        top = top * reduccion
        right = right * reduccion
        bottom = bottom * reduccion
        left = left * reduccion

        if nombre == "???":
            color = (0, 0, 255)
        else:
            color = (0, 255, 0)

        cv2.rectangle(img, (left, top), (right, bottom), color, 2)
        cv2.rectangle(img, (left, bottom - 20), (right, bottom), color, -1)
        cv2.putText(img, nombre, (left, bottom - 6), fuente, 0.6, (0,0,0), 1)

    cv2.imshow("Camara", img)

    k = cv2.waitKey(10)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
