#!/usr/bin/python3

# Mi nombre es Fernando Andrés Chajud, carné C02097.
# Este programa recibe un argumento posicional y 2 opcionales.
# Este programa imprime el número de la secuencia de fibonacci según el
# argumento posicional que se introduzca, y, además, según los argumentos
# opcionales que se introduzcan, se imprimirá la duración del programa en
# ejecutarse y/o la secuencia completa hasta el índice indicado.

#  Se importan las librerías necesarias
import time
import argparse

# Declaro el objeto ArgumentParser
parser = argparse.ArgumentParser()

parser.add_argument(
    'posicion', type=int,
    help='Posicion en la secuencia de Fibonacci que debe ser calculado.'
)
parser.add_argument(
    '--tiempo',
    '-t',
    action="store_true",
    help='Imprime el tiempo transcurrido para finalizar el cálculo.'
)
parser.add_argument(
    '--completa',
    '-c',
    action="store_true",
    help='Imprime la secuencia completa.'
)

# Obtengo los argumentos y los guardo en args
args = parser.parse_args()


#  Esta variable empieza a contar cuanto tiempo dura el proceso
inicio = time.time()


def fibonacci(numero):
    """
    Esta función encuentra el número de la secuencia de fibonacci según
    el índice ingresado.
    """
    solucion = 0
    if numero == 0 or numero == 1:
        solucion = 1
    elif numero < 0:
        raise Exception('Debe ingresar números positivos o 0')
    else:
        solucion = fibonacci(numero-1) + fibonacci(numero-2)
    return solucion


#  Esta variable termina de contar cuanto tiempo dura el proceso
final = time.time()

#  Esta variable contiene la duración total de la ejecución del programa
tiempo = final - inicio

# Si solo se introduce el argumento posicional
if args.tiempo is False and args.completa is False:
    print(
        'El número de fibonacci '
        'de indice {} es: {}'
        .format(args.posicion, fibonacci(args.posicion))
     )

# Si se introduce el argumento posicional y -t o --tiempo
elif args.tiempo is True and args.completa is False:
    print(
        'El número de fibonacci '
        'de indice {} es: {}'
        .format(args.posicion, fibonacci(args.posicion))
     )
    print(
        'El tiempo total de ejecución fue: {}'
        .format(tiempo)
    )

# Si se introduce el argumento posicional y -c o -- completa
elif args.completa is True and args.tiempo is False:
    lista_fibo = range(args.posicion + 1)
    print(
        'La serie de fibonacci hasta el índice {} es: '
        .format(args.posicion))
    for i in lista_fibo:
        print(fibonacci(i))

#  Si se introducen todos los argumentos posibles.
else:
    lista_fibo = range(args.posicion + 1)
    print(
        'La serie de fibonacci hasta el índice {} es: '
        .format(args.posicion))
    for i in lista_fibo:
        print(fibonacci(i))
    print(
        'El tiempo total de ejecución fue: {}'
        .format(tiempo)
    )
