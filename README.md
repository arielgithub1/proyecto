# Proyecto Herramientas computacionales: el arte de la programacion

Material utilizado para el curso TC1001S.2

## Creado por

María Fernanda Velázquez Vergara A01634117

Enrique Espinosa Acebes A01378997

Ariel Iván Ochoa Ramírez A01640097

Misael Octavio Rodríguez Macías A01639786

Alan Ricardo Vilchis Arceo A01640260

## Instalar dependencias necesarias

Despues de clonar este repositorio, es necesario instalar:

-Python3

-OpenCV

-Cmake

-Dlib

-Facial_Recognition

-Imutils

De igual manera, en la terminal hay que poner para poder usarlos:

```pip install opencv-python```

```pip install cmake```

```pip install dlib (más indicaciones en el archivo Facial_detection.py)```

```pip install Facial_Recognition```

```pip install Imutils```

Los programas hay que abrirlos desde la terminal para que funcionen

```Filtros.py```

```black_white.py```

```bordes.py```

```facial.py```

```Facial_detection.py```

```Gorrito.py```

```Filtro_Imagenes.py```

## Función de los códigos
* Filtros.py: tenemos 6 diferentes filtros, los cuales se pueden escoger: B&W, RGB, Canny, Sobel, Laplacian y Canny_V2.

* black_white.py: nos muestra dos videos, uno a color y el otro a blanco y negro.

* bordes.py: en este tenemos 3 videos, todos nos enseñan los bordes blancos con fondo negro. Uno está muy marcado, otro apenas se ven marcados y el último se ven los bordes blancos pero no los define todos.

* facial.py: un programa que detecta el rostro o los rostros de las personas en el video y dibuja un rectangulo alrededor de esta.

* Facial_detection.py: es un programa de reconocimiento facial, el cual requiere de un imagen/foto por rostro para registrar y poder reconocer.

* Gorrito.py: es un filtro el cual te pone un gorro (viene en conjunto con el archivo 'gorro_proyecto.py').

* Filtro_Imagenes.py: este código toma 20 fotos, cada 5 fotos cambia el filtro.*** 

        ***Nota: se necesita cambiar la dirección de la carpeta donde se quiere cambiar las fotos.

## Referencias
https://programacionpython80889555.wordpress.com/2020/09/03/extraer-imagenes-de-un-video-con-python-y-opencv/

https://omes-va.com/resaltando-color-de-un-fondo-en-grises/

https://www.youtube.com/watch?v=mZGvFbrqjUU

https://es.stackoverflow.com/questions/349957/convertir-una-imagen-a-escala-de-grises-pero-conservando-los-canales-python

https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html

https://robologs.net/2020/05/05/deteccion-y-reconocimiento-facial-con-opencv-python-y-facerecognition/
