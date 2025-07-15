# CREANDO LAS CLASES PARA LA CALCULADORA 
class  Calculadora:
#creacion de los distintos tipos de operadores de la calculadora
    def sumar(self, a, b):
        return a + b 

    def restar(self , a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b 
    
    def dividir (self, a , b):
        if b == 0 :
         return print("ERROR : No se puede divir por 0 ")
        return a / b
    def potencia(self, a, b):
        return a ** b
    def factorial(self,numero):
        if numero < 0:
            return print("ERROR : No se puede calcular el factorial de un numero negativo")
        return #nse como hacer un factorial


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
#se creo el objeto operacion para trabajar con los metodos de la calculadora 
Operacion = Calculadora()
# INICIO DEL PROGRAMA
while True:
    menu()

    opcion = int(input("Ingrese la opción deseada: "))

    if opcion in [1, 2, 3, 4, 5, 6]:
        val1 = float(input("Ingrese la primera variable: "))
        
        if opcion in [1, 2, 3, 4, 6]:
            val2 = float(input("Ingrese la segunda variable: "))
        if opcion == 1:
            print(f"El resultado de la suma entre {val1} + {val2} es de {Operacion.sumar(val1,val2)}")
        if opcion == 2:
            print(f"El resultado de la resta entre {val1} - {val2} es de {Operacion.restar(val1,val2)}")
        if opcion == 3:
            print(f"El resultado de la multiplicar entre {val1} * {val2} es de {Operacion.multiplicar(val1,val2)}")
        if opcion == 4:
            print(f"El resultado de la dividir entre {val1} / {val2} es de {Operacion.dividir(val1,val2)}")
        #se deshabilito temporalmente los factoriales 
        if opcion == 6:
            print(f"El resultado de elevar {val1} a la {val2} es de {Operacion.potencia(val1,val2)}")


    elif opcion == 7:
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

    elif opcion == 8:
        print("Gracias por usar la calculadora. ¡Hasta luego!")
        break

    else:
        print("Opción no válida.")

    continuar = int(input("¿Desea continuar? [1] Sí / [2] No: "))
    if continuar == 2:
        break

