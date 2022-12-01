# -*- coding: utf-8 -*-
"""Base_Legal

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Yir98cXLsK4aGKus04QyHpFEl3FAwZL4

**Proyecto Final: Unidad 1**

****Entidad: Base_Legal****
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
import string

#Librerías para generar fechas
from random import randint
from datetime import datetime

#Variable asignada para el tamaño del conjunto de datos. 
num_iess = 10000

#Lista de 7 características (Atributos)
features = [
    "id_base_legal",
    "descripcion_base_legal",
    "decreto_base_legal",
    "estado_base_legal",
    "id_afiliacion",
]# Creando un DF para estas características
df = pd.DataFrame(columns=features)

"""**id_base_legal**"""

#Biblioteca uuid para generar cadena aleatoria de datos para id_base_legal.
df['id_base_legal'] = [uuid.uuid4().hex for i in range(num_iess)]

#Genera identificaciones únicas para cada base_legal. Si todas las ID en el conjunto de datos son únicas, devuelve True.
print(df['id_base_legal'].nunique()==num_iess)

"""**descripcion_base_legal**"""

#Creamos la variale para la descripción de tipo string junto con su longitud de 
#cadena de caracteres
bio=[]
length_of_string = 20

for i in range(0, num_iess):#Creamos la descripcion de la universidad
  random.seed(datetime.now())
  #La descripcion contendra todo tipo de caracteres.
  bio=(''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for i in range(length_of_string)))
  #Guardamos la descripcion en el atributo DescripcionUn
  df.descripcion_base_legal[i] =bio

"""**decreto_base_legal**"""

#Los diferentes nombres de roles.
decreto_base_legal = ['Ley Orgánica del Sistema Nacional de Contratación Pública','Ley de Seguridad Social','Norma Creación','Normal de Regulación']
#Creacion de los permisos para cada una de las filas
df['decreto_base_legal'] = random.choices(
  decreto_base_legal, 
    weights=(30,40,20,5), 
    k=num_iess
)

"""**estado_base_legal**"""

#Los diferentes nombres de roles.
estado_base_legal = ['Activo','Inactivo']
#Creacion de los permisos para cada una de las filas
df['estado_base_legal'] = random.choices(
  estado_base_legal, 
    weights=(40,10), 
    k=num_iess
)

"""**id_afiliacion**"""

#Biblioteca uuid para generar cadena aleatoria de datos para id_perfil.
df['id_afiliacion'] = [uuid.uuid4().hex for i in range(num_iess)]

#Genera identificaciones únicas para cada usuario. Si todas las ID en el conjunto de datos son únicas, devuelve True.
print(df['id_afiliacion'].nunique()==num_iess)

#Visualizar en la tabla los datos generados antes de descargar el excel.
df.head(5)

#Generar excel de los datos.
df.to_csv('Base_Legal.csv')