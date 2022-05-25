# ----------------------------------------------------------------------------------------
# Práctica 4: Generador C/A de GPS
# Asignatura: Seguridad en Sistemas Informáticos
# Fecha de entrega: 24/03/2022
# Autor:
# - Adrián González Galván
# - alu0101321219@ull.edu.es
# ----------------------------------------------------------------------------------------
# En este fichero se encuentran las funciones utilizadas para el desarrollo de la práctica.
# ----------------------------------------------------------------------------------------

import os
from operator import xor

LSFR1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
LSFR2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# TAPS del satélite G2
G2Taps = [(2, 6), (3, 7), (4, 8), (5, 9), (1, 9), (2, 10), (1, 8), (2, 9),
  (3, 10), (2, 3), (3, 4), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (1, 4),
  (2, 5), (3, 6), (4, 7), (5, 8), (6, 9), (1, 3), (4, 6), (5, 7), (6, 8),
  (7, 9), (8, 10), (1, 6), (2, 7), (3, 8), (4, 9)]

# Limpia la pantalla de la terminal
def cleanTerminal():
  os.system('cls' if os.name == 'nt' else 'clear')

# Define un 'G' genérico al que se le deberán especificar:
# - La lista de bits que debe tratar
# - Los índices sobre los que operar
# Devuelve el valor de la realimentación.
def G (bitArray: list, indexes: list):
  if (max(indexes) > len(bitArray) or min(indexes) < 1):
    return -1
  else:
    XORresult = bitArray[indexes[0] - 1]
    for index in indexes[1:]:
      XORresult = xor(XORresult, bitArray[index - 1])
    return XORresult

# Retroalimenta un vector de bits con un elemento dado
def feedback(bitArray: list, feed: int):
  result = bitArray.copy()
  result.pop()
  result.insert(0, feed)
  return result

# Dado un ID de un satélite, calcula los TAPS correspondientes
def getG2Taps(PRNid: int):
  if (PRNid > 0 and PRNid <= len(G2Taps)):
    return G2Taps[PRNid - 1]
  return 0

# Dado una tupla TAPS y una lista de bits:
# Calcula la operacion XOR correspondiente
def PRN(taps: tuple, bitArray: list):
  return xor(bitArray[taps[0] - 1], bitArray[taps[1] - 1])