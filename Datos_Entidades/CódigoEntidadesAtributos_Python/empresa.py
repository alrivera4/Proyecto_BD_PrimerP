# -*- coding: utf-8 -*-
"""Empresa.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18Q4u-YNxM1oLWynoencumS5JfvRmPCzV

**Proyecto Final: Unidad 1**

**Entidad: empresa**
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

#Lista de 5 características (Atributos)
features = [
    "id_empresa",
    "nombre_empresa",
    "detalle_empresa",
    "direccion_empresa",
    "responsable_empresa",
]# Creando un DF para estas características
df = pd.DataFrame(columns=features)

"""**id_empresa**"""

#Biblioteca uuid para generar cadena aleatoria de datos para id_perfil.
df['id_empresa'] = [uuid.uuid4().hex for i in range(num_iess)]

#Genera identificaciones únicas para cada usuario. Si todas las ID en el conjunto de datos son únicas, devuelve True.
print(df['id_empresa'].nunique()==num_iess)

"""**nombre_empresa**"""

#Variable para los géneros para la creación de los nombres.
genero = ["female", "male"]

#Nombres.
df['genero']= random.choices(
    genero, 
    weights=(30,30), 
    k=num_iess)

#Instancia Faker
faker = Faker()
#Función.
def name_gen(genero):
    #Para masculino
    if genero=='male':
        return faker.name_male()
    #Para femenino
    elif genero=='female':
        return faker.name_female()
    #Genera los nombres
    return faker.name()
df['nombre_empresa'] = [name_gen(i) for i in df['genero']]

"""**detalle_empresa**"""

#Variale tipo string junto con su longitud de cadena de caracteres.
bio=[]
length_of_string = 25
#Crea el detalle del rol.
for i in range(0, num_iess):
  random.seed(datetime.now())
  #La descripcion tiene todo tipo de caracteres.
  bio=(''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for i in range(length_of_string)))
  #Se guarda el detalle dle rol.
  df.detalle_empresa[i] =bio

"""**direccion_empresa**"""

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
  df.direccion_empresa[i] =bio

"""**responsable_empresa**"""

#Instancia Faker
faker = Faker()
#Función.
def name_gen(genero):
    #Para masculino
    if genero=='male':
        return faker.name_male()
    #Para femenino
    elif genero=='female':
        return faker.name_female()
    #Genera los nombres
    return faker.name()
df['responsable_empresa'] = [name_gen(i) for i in df['genero']]

#Eliminar genero, no es necesaerio para esta entidad.
del(df['genero'])

#Visualizar en la tabla los datos generados antes de descargar el excel.
df.head(5)

#Generar excel de los datos.
df.to_csv('empresa.csv')