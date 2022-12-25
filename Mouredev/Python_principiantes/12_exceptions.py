### Exception Handling ###

numberOne, numberTwo = 5, "1"

try:
    # Prueba a ejecutar el código
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    # En caso de error, salta aquí
    print("Se ha producido un error")
else: # Opcional
    # En caso de no haber error, ejecuta else
    print("La ejecución continúa correctamente")
finally: # Opcional
    # Se ejecuta siempre (con o sin error)
    print("La ejecución continúa")

# Excepciones por tipo

try:
    # Prueba a ejecutar el código
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except TypeError:
    # En caso de TypeError, salta aquí
    print("Se ha producido un TypeError")
except ValueError:
    # En caso de ValueError, salta aquí
    print("Se ha producido un ValueError")

# Captura de la información de la excepción

try:
    # Prueba a ejecutar el código
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error:
    # Captura el error en la variable "error"
    print(error)
except Exception as exception:
    print(exception)

print("Hola")
