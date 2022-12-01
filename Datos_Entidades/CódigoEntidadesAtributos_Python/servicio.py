# -*- coding: utf-8 -*-
"""Servicio

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yxSCen89yX4NzbJJ9KzcwthWgmJWkg7F

**Proyecto Final: Unidad 1**

**Entidad: Servicio**
"""

#Faker es un paquete de Python que genera datos falsos.
!pip install Faker

#Librerías necesarias para la generación de datos.
import pandas as pd
import uuid
import random
from faker import Faker
import datetime

#Librerías para generar cadena de numeros
import random as r
from random import seed

#Librerías para generar fechas
import string
from random import randint
from datetime import datetime

#Variable asignada para el tamaño del conjunto de datos. 
num_iess = 10000

"""- id_servicio: una cadena de números para identificar en este caso un servicio
     - nombre_servicio:tipo de cadena con un nombre de servicio
     - tipo_servicio: tipo de cadena que define el tipo de servicio
     - detalle_servicio: tipo de cadena que describe el servicio
     - id_afiliacion:una cadena de números para identificar en este caso un tipo de afilicion

Se ingresan los atributos como una lista para inicializar un marco de datos de Pandas:
"""

#Lista de 5 características (Atributos)
features = [
    "id_servicio",
    "nombre_servicio",
    "tipo_servicio",
    "detalle_servicio",
    "id_afiliacion",
]# Creando un DF para estas características
df = pd.DataFrame(columns=features)

"""**id_servicio**"""

#Biblioteca uuid para generar cadena aleatoria de datos para id_perfil.
df['id_servicio'] = [uuid.uuid4().hex for i in range(num_iess)]

#Genera identificaciones únicas para cada usuario. Si todas las ID en el conjunto de datos son únicas, devuelve True.
print(df['id_servicio'].nunique()==num_iess)

"""**nombre_servicio**"""

#Los diferentes nombres de servicios.
nombre_servicio= ['Atención médica','Jubilación','Préstamo','Mortuorio']
#Creacion de los permisos para cada una de las filas
df['nombre_servicio'] = random.choices(
  nombre_servicio, 
    weights=(40,10,10,5), 
    k=num_iess
)

"""**tipo_servicio**"""

#Los diferentes nombres de roles.
tipo_servicio = ['Cita','Web','CallCenter','Ventanilla']
#Creacion de los permisos para cada una de las filas
df['tipo_servicio'] = random.choices(
  tipo_servicio, 
    weights=(30,40,20,5), 
    k=num_iess
)

"""**detalle_servicio**"""

#Importaomos las librerias necesarias
import string
import random
#Creamos la variale para la descripción de tipo string junto con su longitud de 
#cadena de caracteres
bio=[]
length_of_string = 20

for i in range(0, num_iess):#Creamos la descripcion de la universidad
  random.seed(datetime.now())
  #La descripcion contendra todo tipo de caracteres.
  bio=(''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for i in range(length_of_string)))
  #Guardamos la descripcion en el atributo DescripcionUn
  df.detalle_servicio[i] =bio

"""**id_afiliacion**"""

#Biblioteca uuid para generar cadena aleatoria de datos para id_perfil.
df['id_afiliacion'] = [uuid.uuid4().hex for i in range(num_iess)]

#Genera identificaciones únicas para cada usuario. Si todas las ID en el conjunto de datos son únicas, devuelve True.
print(df['id_afiliacion'].nunique()==num_iess)

#Visualizar en la tabla los datos generados antes de descargar el excel.
df.head(5)

#Generar excel de los datos.
df.to_csv('Servicio.csv')