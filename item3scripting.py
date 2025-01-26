#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

num = [] # Definimos el Array o Arreglo

    
for i in range(5): # Recorremos 5 veces el Proceso
    
    valoresAIngresar = int(input(f"Ingrese número {i+1}: "))# Mensaje que arroja por pantalla solictando el ingreso de numeros
    
    num.append(valoresAIngresar) # Alimentamos el Array almac¿enando la información
    
    num.sort() # Ordenamos los numeros de menor a mayor

a = num[0]  # En el arreglo damos la orden de seleccionar el numero menor
b = num[-1]  # En el arreglo damos la orden de seleccionar el numero mayor
c = num [1] # En el arreglo damos la orden de seleccionar el segundo numero menor

aux = b**2 - 4 * a * c # Generamos el primero Calculo
aux2 = math.sqrt(aux) # Generamos el segundo calculo
temp1 = -b + aux2 # Generamos el tercer calculo
x1 = temp1 / (2*a) # Almacenamos el resultado final en la variable x1

print ("Número 1:",a) # Mostrar por pantalla la variable a
print ("Número 2:",b) # Mostrar por pantalla la variable b
print ("Número 3:",c) # Mostrar por pantalla la variable c
print ("El Resultado es:",x1) # Mostrar por pantalla el resultado final 


# In[ ]:




