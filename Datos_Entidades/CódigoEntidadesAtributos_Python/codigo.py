# -*- coding: utf-8 -*-
"""Codigo

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bKP6FSvZDxp7IUpqwDAH0wueOIPum0Zw

**Proyecto Final: Unidad 1**

**Entidad: Codigo**
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

"""- id_codigo: una cadena de números para identificar en este caso un codigo
     - nombre_codigo:tipo de cadena con un nombre de un codigo
     - artículo: cadena de números para representar números
     - estado_codigo: tipo de cadena que describe estado de actividad o no actividad
     - detalle_codigo:una cadena de caracteres para simular información

Se ingresan los atributos como una lista para inicializar un marco de datos de Pandas:
"""

#Lista de 5 características (Atributos)
features = [
    "id_codigo",
    "nombre_codigo",
    "articulo",
    "estado_codigo",
    "detalle_codigo",
    "id_base_legal",
]# Creando un DF para estas características
df = pd.DataFrame(columns=features)

"""**id_codigo**"""

#Biblioteca uuid para generar cadena aleatoria de datos para id_perfil.
df['id_codigo'] = [uuid.uuid4().hex for i in range(num_iess)]

#Genera identificaciones únicas para cada usuario. Si todas las ID en el conjunto de datos son únicas, devuelve True.
print(df['id_codigo'].nunique()==num_iess)

"""**nombre_codigo**"""

#Los diferentes nombres de codigos.
nombre_codigo= ['Código del Trabajo','Código Cívil','Código Orgánico Integral','Código de Comercio']
#Creacion de los permisos para cada una de las filas
df['nombre_codigo'] = random.choices(
  nombre_codigo, 
    weights=(40,10,10,5), 
    k=num_iess
)

"""**articulo**"""

articulos=[]
#Cantidad de números para la cadena..
size = 2
for i in range(0, num_iess):
  random.seed(datetime.now())
  #Números opcionales para formar la cadena.
  valores = [0,1,2,3,4,5,6,7,8,9]
  articulos=(''.join([str(random.choice(valores)) for i in range(size)]))
  #Se guarda los números 
  df.articulo[i]=articulos

"""**estado_codigo**"""

#Los diferentes nombres de servicios.
estado_codigo= ['Activo','Inactivo']
#Creacion de los permisos para cada una de las filas
df['estado_codigo'] = random.choices(
  estado_codigo, 
    weights=(40,10), 
    k=num_iess
)

"""**detalle_codigo**"""

#Creamos la variale para la descripción de tipo string junto con su longitud de 
#cadena de caracteres
bio=[]
length_of_string = 20

for i in range(0, num_iess):#Creamos la descripcion de la universidad
  random.seed(datetime.now())
  #La descripcion contendra todo tipo de caracteres.
  bio=(''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for i in range(length_of_string)))
  #Guardamos la descripcion en el atributo DescripcionUn
  df.detalle_codigo[i] =bio

"""**id_base_legal**"""

#Biblioteca uuid para generar cadena aleatoria de datos para id_perfil.
df['id_base_legal'] = [uuid.uuid4().hex for i in range(num_iess)]

#Genera identificaciones únicas para cada usuario. Si todas las ID en el conjunto de datos son únicas, devuelve True.
print(df['id_base_legal'].nunique()==num_iess)

#Visualizar en la tabla los datos generados antes de descargar el excel.
df.head(5)

#Generar excel de los datos.
df.to_csv('Codigo.csv')