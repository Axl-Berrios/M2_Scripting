#!/usr/bin/env python
# coding: utf-8

# ## RESOLUCIÓN DE ECUACIÓN DE SEGUNDO GRADO
# * el valor a debe ser distinto a cero
# 

# In[1]:


# a :COEFICIENTE DEL TERMINO CUADRATICO
# b :COEFICIENTE DEL TERMINO LINEAL
# c :TERMINO INDEPENDIENTE
# aux: VARIABLE AUXILIAR PARA GUARDAR EL COMPONENTE DE LA ECUACION
# Temp1: Aqui aplicamos el tercer calculo y lo guardamos en la variable temp1
# x1: Como el resultado esta en la variable x1, mostramos el resultado en la variable x1 por pantalla
# x2: basicamente lo que hace es calcular la raiz del resultado de aux


# In[6]:


import math

a = float(input("Ingrese número 1: ")) # Estas lineas de codigos definimos el ingreso de numeros por pantalla
b = float(input("Ingrese número 2: ")) # Estas lineas de codigos definimos el ingreso de numeros por pantalla
c = float(input("Ingrese número 3: ")) # Estas lineas de codigos definimos el ingreso de numeros por pantalla


if a != 0: # Como dice el ejercicio la variable a no tiene que ser 0, 
    # entonces aqui indicamos que la variable a sea distinto a 0
    
    aux = b**2 - 4 * a * c # Aqui calcula la discriminante de la ecuacion
    aux2 = math.sqrt(aux) # Aqui aplicamos el segundo calculo y lo guardamos en la variable aux2
    temp1 = -b + aux2 # Aqui aplicamos el tercer calculo y lo guardamos en la variable temp1
    x1 = temp1 / (2*a) # Aqui aplicamos el cuarto y ultimo calculo y lo guaramos en la variable x1
    print(x1) # Como el resultado esta en la variable x1, mostramos el resultado en la variable x1 por pantalla
    
else: # Else quiere decir si el IF no cumple con la condicion que le entregamos vamos a retornar un else.
    
    print("El número 1 debe ser mayor a 0")


# In[2]:


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





# In[ ]:




