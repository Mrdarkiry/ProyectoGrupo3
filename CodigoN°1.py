# FUNCIONES DEFINIDAS FUERA DEL BUCLE
def menu():
    print("\n-BIENVENIDOS ")
    print("1- SUMA")    
    print("2- RESTA")
    print("3- MULTIPLICACION")
    print("4- DIVISION")
    print("5- FACTORIALES")
    print("6- POTENCIAS")    
    print("7- OPERACIONES CON VECTORES")
    print("8- SALIR")

def suma(val1, val2):
    resultado = val1 + val2
    print(f"El resultado de {val1} + {val2} es: {resultado}")

def resta(val1, val2):
    resultado = val1 - val2
    print(f"El resultado de {val1} - {val2} es: {resultado}")

def multiplicacion(val1, val2):
    resultado = val1 * val2
    print(f"El resultado de {val1} * {val2} es: {resultado}")

def division(val1, val2):
    if val2 == 0:
        print("No se puede dividir por cero.")
    else:
        resultado = val1 / val2
        print(f"El resultado de {val1} / {val2} es: {resultado}")

def factorial(val1):
        r=1
        i = 2
        while i <= val1:
            r *= i
            i += 1
        return r
        Resultado = factorial(val1)
        print(f"el resultado es del factorial {val1} es : {Resultado}")

# INICIO DEL PROGRAMA
while True:
    menu()

    opcion = int(input("Ingrese la opción deseada: "))

    if opcion in [1, 2, 3, 4, 5]:
        val1 = float(input("Ingrese la primera variable: "))
        if opcion != 5 :
         val2 = float(input("Ingrese la segunda variable: "))

        if opcion == 1:
            suma(val1, val2)
        elif opcion == 2:
            resta(val1, val2)
        elif opcion == 3:
            multiplicacion(val1, val2)
        elif opcion == 4:
            division(val1, val2)
        elif opcion == 5 :
            val1 = int(input("ingrese el factorial: "))
            factorial(val1)
       
    elif opcion == 6:
        vector1 = [0, 0, 0]
        vector2 = [0, 0, 0]
        Rvector = [0, 0, 0]

        while True:
            vector1[0] = int(input("Ingrese los valores del vector 1 [x]: "))
            vector1[1] = int(input("Ingrese los valores del vector 1 [y]: "))
            vector1[2] = int(input("Ingrese los valores del vector 1 [z]: "))
            print("Este es su vector1:", vector1)
            confirmacion = int(input("¿Es correcto? [1] Sí / [2] No: "))
            if confirmacion == 1:
                break

        while True:
            vector2[0] = int(input("Ingrese los valores del vector 2 [x]: "))
            vector2[1] = int(input("Ingrese los valores del vector 2 [y]: "))
            vector2[2] = int(input("Ingrese los valores del vector 2 [z]: "))
            print("Este es su vector2:", vector2)
            confirmacion = int(input("¿Es correcto? [1] Sí / [2] No: "))
            if confirmacion == 1:
                break

        for i in range(3):
            Rvector[i] = vector1[i] + vector2[i]
        print("Resultado de la suma de vectores:", Rvector)

    elif opcion == 6:
        print("Gracias por usar la calculadora. ¡Hasta luego!")
        break

    else:
        print("Opción no válida.")

    continuar = int(input("¿Desea continuar? [1] Sí / [2] No: "))
    if continuar == 2:
        break

