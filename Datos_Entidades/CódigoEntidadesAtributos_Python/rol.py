# -*- coding: utf-8 -*-
"""Rol.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19pLu3p67_ipSRENWQ9KinO5SGqXgiYiN

**Proyecto Final: Unidad 1**

**Entidad: Rol**
"""

#Faker es un paquete de Python que genera datos falsos.
!pip install Faker

#Librerías necesarias para la generación de datos.
import pandas as pd
import uuid
import random
from faker import Faker
import datetime

#Librerías necesarias para el detalle o la descripción.
import string
import random
from random import seed
from datetime import datetime

#Variable asignada para el tamaño del conjunto de datos. 
num_iess = 10000

#Lista de 3 características (Atributos)
features = [
    "cod_Rol",
    "nombre_Rol",
    "detalle_Rol",
]# Creando un DF para estas características
df = pd.DataFrame(columns=features)

"""**cod_Rol**"""

#Biblioteca uuid para generar cadena aleatoria de datos para cod_Rol.
df['cod_Rol'] = [uuid.uuid4().hex for i in range(num_iess)]

#Genera identificaciones únicas para cada usuario. Si todas las ID en el conjunto de datos son únicas, devuelve True.
print(df['cod_Rol'].nunique()==num_iess)

"""**nombre_Rol**"""

#Los diferentes nombres de roles.
Nombre_Rol = ['Pensionista','Afiliado']
#Creacion de los permisos para cada una de las filas
df['nombre_Rol'] = random.choices(
  Nombre_Rol, 
    weights=(25,25), 
    k=num_iess
)

"""**detalle_Rol**"""

#Variale tipo string junto con su longitud de cadena de caracteres.
bio=[]
length_of_string = 25
#Crea el detalle del rol.
for i in range(0, num_iess):
  random.seed(datetime.now())
  #La descripcion tiene todo tipo de caracteres.
  bio=(''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for i in range(length_of_string)))
  #Se guarda el detalle dle rol.
  df.detalle_Rol[i] =bio

#Visualizar en la tabla los datos generados antes de descargar el excel.
df.head(5)

#Generar excel de los datos.
df.to_csv('rol.csv')