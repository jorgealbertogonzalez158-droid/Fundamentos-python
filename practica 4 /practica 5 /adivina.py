import random

def tirar_dados():
    return random.randint(2, 12)

def pedir_respuestas():
    print("Ingresar tu predicción")
    print("1. par")
    print("2. impar")
    print("3. salir del juego")

    return int(input())

def imprimir_resultado(numero, prediccion):
    pass

while True:
    numero = tirar_dados()
    predicción = pedir_respuestas()
    if predicción == 3:
        break
    imprimir_resultado(numero, predicción)

    print("Gracias por jugar")

    #print("Tiro de datos:", tirar_datos())
