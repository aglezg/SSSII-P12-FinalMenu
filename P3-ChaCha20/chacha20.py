# ----------------------------------------------------------------
# Práctica 3: Generador Chacha20.
# Asignatura: Seguridad en Sistemas Informáticos
# Fecha de entrega: 17/03/2022
# Autor:
# - Adrián González Galván
# - alu0101321219@ull.edu.es
# ----------------------------------------------------------------
# En este fichero se incluye el desarrollo del menú de la práctica.
# ----------------------------------------------------------------
from chacha20_functions import *
import sys

# Main
def p3Chacha20():

  cleanTerminal()

  # Menú principal  y lectura de opciones
  print("\n PRÁCTICA 3: Generador Chacha20\n")

  print("  Introduzca la clave:")
  key = [None] * 8
  for i in range(8):
    hexaDigit = input ("   [" + str(i + 1) + "] >> ")
    if (isValidKeyElement(hexaDigit)):
      key [i] = hexaDigit
    else:
      sys.exit("\n  Algún elemento introducido para la clave es incorrecto, revíselo.")
    
  count = input ("\n  Introduzca el contador: ")
  if (isValidKeyElement(count) == False):
    sys.exit("\n  El contador introducido es incorrecto, revíselo.")

  nonce = [None] * 3
  print("\n  Introduzca el nonce:")
  for i in range(3):
    nonce_element = input ("   [" + str(i + 1) + "] >> ")
    if (isValidKeyElement(nonce_element)):
      nonce [i] = nonce_element
    else:
      sys.exit("\n  Algún elemento introducido para la clave es incorrecto, revíselo.")

  # Ejecución del programa
  state = createInitialState(key, count, nonce)
  print("\n ESTADO INICIAL:\n")
  printState(state)

  final_state = chachaBlock(state, True)
  print("\n\n ESTADO FINAL DE SALIDA DEL GENERADOR:\n")
  printState(final_state)