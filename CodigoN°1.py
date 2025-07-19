from collections import deque

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
  return resultado

def resta(val1, val2):
  resultado = val1 - val2
  print(f"El resultado de {val1} - {val2} es: {resultado}")
  return resultado

def multiplicacion(val1, val2):
  resultado = val1 * val2
  print(f"El resultado de {val1} * {val2} es: {resultado}")
  return resultado

def division(val1, val2):
  if val2 == 0:
    print("No se puede dividir por cero.")
    return None
  else:
    resultado = val1 / val2
    print(f"El resultado de {val1} / {val2} es: {resultado}")
    return resultado

def factorial(val1):
  r = 1
  for i in range(2, int(val1) + 1):
    r *= i
  print(f"El resultado del factorial de {int(val1)} es: {r}")
  return r

def potencias(val1 , val2):
  resultado = val1 ** val2
  print(f"El resultado de {val1} elevado a {val2} es: {resultado}")
  return resultado

# INICIO DEL PROGRAMA
historial_resultados = deque(maxlen=5)

while True:
  menu()

  try:
    opcion = int(input("Ingrese la opción deseada: "))
  except ValueError:
    print("Por favor, ingrese un número válido.")
    continue

  if opcion in [1, 2, 3, 4, 5, 6]:
    val1 = float(input("Ingrese la primera variable: "))
    if opcion in [1, 2, 3, 4, 6]:
      val2 = float(input("Ingrese la segunda variable: "))
    if opcion == 1:
      resultado = suma(val1, val2)
      historial_resultados.append(resultado)
    elif opcion == 2:
      resultado = resta(val1, val2)
      historial_resultados.append(resultado)
    elif opcion == 3:
      resultado = multiplicacion(val1, val2)
      historial_resultados.append(resultado)
    elif opcion == 4:
      resultado = division(val1, val2)
      if resultado is not None:
        historial_resultados.append(resultado)
    elif opcion == 5:
      resultado = factorial(val1)
      historial_resultados.append(resultado)
    elif opcion == 6:
      resultado = potencias(val1, val2)
      historial_resultados.append(resultado)

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
    historial_resultados.append(Rvector)

  elif opcion == 8:
    print("Gracias por usar la calculadora. ¡Hasta luego!")
    break

  else:
    print("Opción no válida.")

  print("Historial de últimos 5 resultados:", list(historial_resultados))

  continuar = int(input("¿Desea continuar? [1] Sí / [2] No: "))
  if continuar == 2:
    break

