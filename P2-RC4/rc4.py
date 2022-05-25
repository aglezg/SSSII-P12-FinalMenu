# ----------------------------------------------------------------
# Práctica 3: Cifrado RC4.
# Asignatura: Seguridad en Sistemas Informáticos
# Fecha de entrega: 10/03/2022
# Autor:
# - Adrián González Galván
# - alu0101321219@ull.edu.es
# ----------------------------------------------------------------
# En este fichero se incluye el desarrollo del menú de la práctica.
# ----------------------------------------------------------------

from rc4_functions import *

# Main
def p2RC4():

  cleanTerminal()

  # Menú principal  y lectura de opciones
  print("\n PRÁCTICA 3: CIFRADO RC4\n")
  keySeed = input("  Semilla de clave:")
  message = input("  Texto original:")
      
  # Convertimos a array las entradas para operar con ellas
  keySeedArray = keySeed.replace(' ', '').split(',')
  messageArray = message.replace(' ', '').split(',')

  # Las transformamos en arrays de enteros
  intKeySeedArray: list = []
  for element in keySeedArray:
    if (element.isdigit() and int(element) >= 0):
      intKeySeedArray.append(int(element))
    else:
      print("\n La clave introducida es incorrecta. Finalizando el programa...")
      quit()

  intMessageArray: list = []
  for element in messageArray:
    if (element.isdigit() and int(element) >= 0):
      intMessageArray.append(int(element))
    else:
      print("\n El mensaje introducido es incorrecto. Finalizando el programa...")
      quit()

  # Cifrado RC4
  cypherMessage = encode(PRGA(KSA(intKeySeedArray), len(intMessageArray)), intMessageArray)
  stringCypherMessage: list = []
  for element in cypherMessage:
    stringCypherMessage.append(str(element))
  print("\n  > Texto cifrado = "   + ' '.join(stringCypherMessage))