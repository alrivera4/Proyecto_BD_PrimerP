# -*- coding: utf-8 -*-
"""Persona.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aZafyz6eGtf7Fuiw0esMuv2airpw29DG

**Proyecto Final: Unidad 1**

**Entidad: hijo**
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
from random import randint
from datetime import datetime

#Variable asignada para el tamaño del conjunto de datos. 
num_iess = 10000

#Lista de 7 características (Atributos)
features = [
    "ci_persona",
    "nombre_persona",
    "tel_persona",
    "genero_persona",
    "fecha_nac_persona",
    "correo_persona",
    "direccion_persona",
]# Creando un DF para estas características
df = pd.DataFrame(columns=features)

"""**nombre_persona**"""

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
df['nombre_persona'] = [name_gen(i) for i in df['genero']]

"""**ci_persona**"""

cedula=[]
#Cantidad de números para la cadena..
size = 10
for i in range(0, num_iess):
  random.seed(datetime.now())
  #Números opcionales para formar la cadena.
  valores = [0,1,2,3,4,5,6,7,8,9]
  cedula=(''.join([str(random.choice(valores)) for i in range(size)]))
  #Se guarda los números en telefonocallcenter.
  df.ci_persona[i]=cedula

"""**tel_persona**"""

numero=[]
#Cantidad de números para la cadena..
size = 10
for i in range(0, num_iess):
  random.seed(datetime.now())
  #Números opcionales para formar la cadena.
  valores = [0,1,2,3,4,5,6,7,8,9]
  numero=(''.join([str(random.choice(valores)) for i in range(size)]))
  #Se guarda los números en telefonocallcenter.
  df.tel_persona[i]=numero

"""**genero_persona**"""

genders = ["Hombre", "Mujer"]

df['genero_persona'] = random.choices(
    genders, 
    weights=(47,47), 
    k=num_iess
)
df.genero_persona[i]=genders

"""**fecha_nac_persona**"""

def fecha_nac_persona(start, end, n):
    #Formato de marca de tiempo (año, mes, dia)
    frmt = "%Y-%m-%d"

    #Formateo de los dos períodos de tiempo.
    stime = datetime.strptime(start, frmt)
    etime = datetime.strptime(end, frmt)
    
    #Se crea el grupo para tiempos aleatorios.
    td = etime - stime
    
    #Se genera una lista con los tiempos aleatorios.
    times = [(random.random() * td + stime).strftime(frmt) for _ in range(n)]
    return times
df['fecha_nac_persona'] = fecha_nac_persona("1980-01-01", "2006-01-01", num_iess)

"""**correo_persona**"""

def emailGen(name, duplicateFound=False):
    """
    Genera una dirección de correo electrónico aleatoria basada en el nombre dado.
    Agrega un número al final si se encuentra una dirección duplicada.
    """
    #Nombre de dominio falso para usar.
    dom = "@fakemail.com"
    
    #Minúsculas y división.
    name = name.lower().split(" ")
    
    #Carácter aleatorio para insertar en el nombre.
    chars = [".", "_"]
    
    new_name = name[0] + random.choice(chars) + name[1] 
    
    #Distinguir aún más el correo electrónico si se encontró un duplicad.
    if duplicateFound:
        
        #Número aleatorio para insertar al final.
        num = random.randint(0,100)
        
        #Insertando al final.
        new_name = new_name + str(num)
        
    #Devolver la dirección de correo electrónico con el nombre de dominio adjunto.
    return new_name + dom

emails = []

for name in df['nombre_persona']:
    
    # Generating the email
    email = emailGen(name)
    
    # Looping until a unique email is generated
    while email in emails:
        
        # Creating an email with a random number
        email = emailGen(name, duplicateFound=True)
    
    # Attaching the new email to the list
    emails.append(email)
    
df['correo_persona'] = emails

"""**direccion_persona**"""

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
  df.direccion_persona[i] =bio

#Eliminar genero, no es necesaerio para esta entidad.
del(df['genero'])

#Visualizar en la tabla los datos generados antes de descargar el excel.
df.head(5)

#Generar excel de los datos.
df.to_csv('persona.csv')