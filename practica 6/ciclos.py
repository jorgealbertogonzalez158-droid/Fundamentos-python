#ciclo, iteración bucle

#while
i = 0
while i < 10:
    if i < 5:
        print("El numero", i, "es menor a 5")
    else:
        print("El numero", i, "es mayor o igual a 5")

        i + 1

        print("Terminó la iteración")
        

       # for x in range (1, 11):
               #print(x)
    while True:
        print("Escribe la opción deseada")
        print("1: saludar")
        print("2: salir")


    respuesta = int(input())

    if respuesta == 1:
        print("saludos terricola!")
    elif respuesta == 2:
        break

    print("Terminado programa")
