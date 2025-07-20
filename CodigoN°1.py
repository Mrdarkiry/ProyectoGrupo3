from collections import deque
class Calculadora:
    def __init__(self):
        self.historial_resultados = deque(maxlen=5)

    def menu(self):
        print("\n--- BIENVENIDOS ---")
        print("1- SUMA") 
        print("2- RESTA")
        print("3- MULTIPLICACION")
        print("4- DIVISION")
        print("5- FACTORIALES")
        print("6- POTENCIAS") 
        print("7- OPERACIONES CON VECTORES")
        print("8- SALIR")

    def ejecutar(self):
        while True:
            self.menu()
            try:
                opcion = int(input("Ingrese la opción deseada: "))
            except ValueError:
                print("Por favor, ingrese un número válido.")
                continue

            if opcion in [1, 2, 3, 4, 5, 6]:
                val1 = float(input("Ingrese la primera variable: "))
                val2 = float(input("Ingrese la segunda variable: ")) if opcion in [1, 2, 3, 4, 6] else None

                resultado = self.realizar_operacion(opcion, val1, val2)
                if resultado is not None:
                    self.historial_resultados.append(resultado)

            elif opcion == 7:
                resultado_vector = self.operaciones_vectores()
                self.historial_resultados.append(resultado_vector)

            elif opcion == 8:
                print("Gracias por usar la calculadora. ¡Hasta luego!")
                break

            else:
                print("Opción no válida.")

            print("Historial de últimos 5 resultados:", list(self.historial_resultados))

            continuar = input("¿Desea continuar? [1] Sí / [2] No: ")
            if continuar != "1":
                break

    def realizar_operacion(self, opcion, val1, val2=None):
        if opcion == 1:
            return self.suma(val1, val2)
        elif opcion == 2:
            return self.resta(val1, val2)
        elif opcion == 3:
            return self.multiplicacion(val1, val2)
        elif opcion == 4:
            return self.division(val1, val2)
        elif opcion == 5:
            return self.factorial(val1)
        elif opcion == 6:
            return self.potencia(val1, val2)
   
    def suma(self, val1, val2):
        return val1 + val2
    
    def resta(self, val1, val2):
        return val1 - val2
    
    def multiplicacion(self, val1, val2):
        return val1 * val2
    
    def division(self, val1, val2):
        if val2 == 0:
            return "Error: División por cero"
        return val1 / val2
    
    def factorial(self, val1):
        if val1 < 0:
            return "Error: Factorial de un número negativo no está definido"
        resultado = 1
        for i in range(1, int(val1) + 1):
            resultado *= i
        return resultado
    def potencia(self, val1, val2):
        return val1 ** val2

    def operaciones_vectores(self):
        vector1 = [0, 0, 0]
        vector2 = [0, 0, 0]
        resultado = [0, 0, 0]

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
            resultado[i] = vector1[i] + vector2[i]
        print("Resultado de la suma de vectores:",resultado)
        return resultado

if __name__ == "__main__":
    calculadora = Calculadora()
    calculadora.ejecutar()