#!/usr/bin/env python
# coding: utf-8

# In[2]:


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


# In[ ]:




