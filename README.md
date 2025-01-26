# M2_Scripting (Matematicas)

# Cálculo de Raíces Cuadráticas y Manejo de Números

Este proyecto consiste en un programa que permite al usuario ingresar tres números para calcular una raíz cuadrática de una ecuación cuadrática. Además, el programa permite ingresar cinco números, los ordena y utiliza algunos de ellos para realizar un segundo cálculo de raíz cuadrática.

## Contenido

- Descripción del programa
- Cómo funciona
- Cómo ejecutar el código

## Descripción del Programa

El programa realiza las siguientes operaciones:

1. **Cálculo de la raíz cuadrática**:
   - El usuario ingresa tres números: `a`, `b` y `c`.
   - Se verifica que `a` no sea cero, ya que esto es necesario para evitar una división por cero.
   - Se calcula la raíz cuadrática utilizando la fórmula de la ecuación cuadrática: 
     \[
     x = \frac{-b + \sqrt{b^2 - 4ac}}{2a}
     \]

2. **Ingreso y ordenamiento de números**:
   - El usuario ingresa cinco números.
   - Los números se almacenan en una lista, que luego se ordena.
   - Se seleccionan el número menor, el mayor y el segundo número menor para realizar un segundo cálculo de raíz cuadrática.

## Cómo Funciona

1. **Cálculo de la raíz cuadrática**:
   - El programa solicita al usuario que ingrese tres números.
   - Si el primer número (`a`) es diferente de cero, se procede a calcular la raíz cuadrática.
   - Si `a` es cero, se muestra un mensaje de error.

2. **Ingreso de números**:
   - El programa solicita al usuario que ingrese cinco números.
   - Los números se almacenan en una lista y se ordenan.
   - Se seleccionan los números necesarios para realizar un segundo cálculo de raíz cuadrática.

## Cómo Ejecutar el Código

1. Asegúrate de tener instalado Python en tu sistema.
2. Copia el código en un archivo Python (por ejemplo, `calculo_raiz.py`).
3. Ejecuta el archivo en tu terminal o entorno de desarrollo preferido.

```bash
python calculo_raiz.py

