import cv2
import numpy as np
import face_recognition
"""
For installing library 'face_recognition', first install library cmake with 'pip install cmake', then install the
'visual c++ tool for cmake' with the next link https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community&rel=15# ,
after that install dlib with 'pip install dlib' and finally install face_recognition 'pip install face_recognition'.
"""

face = face_recognition.load_image_file("example.jpeg") #Load the image with the face
encoding = face_recognition.face_encodings(face)[0] #Get the encondings that characterize the face

registered_faces = [encoding] #Array with all the encodings
registered_names = ["Yo"] #Array with all the names

font = cv2.FONT_HERSHEY_TRIPLEX #Define a font for the name
reduction = 5 #Reduce video size for minimize the delay (recommended 5)

cap = cv2.VideoCapture(0) #Start capturing the video from the default camera

while True:

    coords= [] #Lozalization of the faces in the video
    register = [] #Encoding of the faces
    names = [] #Names of the people localizated

    ret, img = cap.read() #Capture the image from the webcam
    if not ret: #Verify if the image is not valid
        break

    img_rgb = img[:, :, ::-1] #Change the image from BGR to RGB
    img_rgb = cv2.resize(img_rgb, (0, 0), fx = 1.0/reduction, fy = 1.0/reduction) #Reduce the image size
 
    loc_faces = face_recognition.face_locations(img_rgb) #Localize each face in the video
    encodings = face_recognition.face_encodings(img_rgb, loc_faces) #Find the encodings of each face

    name = "" #Variable to save the name
    for i in encodings:
        #Verify coincidences between the encodings found and the encodings registered
        faces = face_recognition.compare_faces(registered_faces, i) 
        if True in faces: #If there is a match
            name = registered_names[faces.index(True)] #Save the registered name in the variable
        else:
            name = "???" #Otherwise, the encoding found and name are unknown
        names.append(name) #Append the name to an array

    for (top, right, bottom, left), name in zip(loc_faces, names):
        #Undo the reduction for getting coordinates 
        top = top * reduction
        right = right * reduction
        bottom = bottom * reduction
        left = left * reduction

        #Verify if the name is unknown the square color is red, otherwise the square color is green
        if name == "???":
            color = (0, 0, 255)
        else:
            color = (0, 255, 0)

        #Draw a square around each identified face 
        cv2.rectangle(img, (left, top), (right, bottom), color, 2)
        cv2.rectangle(img, (left, bottom - 20), (right, bottom), color, -1)
        #Write the name below the square and with the font specified
        cv2.putText(img, name, (left, bottom - 6), font, 0.6, (0,0,0), 1)

    cv2.imshow("Facial_Recognition", img) #Show the result in a window

    #End the program by pressing "Esc"
    k = cv2.waitKey(10)
    if k == 27:
        break

#Release the camera and destroy the windows opened by the program
cap.release()
cv2.destroyAllWindows()