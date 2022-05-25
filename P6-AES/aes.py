# ----------------------------------------------------------------
# Práctica 6: AES
# Asignatura: Seguridad en Sistemas Informáticos
# Fecha de entrega: 07/04/2022
# Autor:
# - Adrián González Galván
# - alu0101321219@ull.edu.es
# ----------------------------------------------------------------
# En este fichero se incluye el desarrollo del menú de la práctica.
# ----------------------------------------------------------------

from aes_functions import *
from aesOperations import *
import sys

# Transforma una cadena de 16 bytes en una matriz
def stringToMatrix(string):
  matrix = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]
  vector = list(string)
  i = 0
  j = 0
  it = 0
  while (i < len(matrix)):
    while (j < len(matrix[i])):
      matrix[j][i] = vector[it] + vector[it + 1]
      j += 1
      it += 2
    j = 0
    i += 1
  return matrix

# Main
def p6AES():

  cleanTerminal()

  # Lectura de opciones
  print("\n PRÁCTICA 7: AES\n")

  key = input("  Clave: ")
  if (len(key) != 32 or isHexadecimalString(key) == False):
    sys.exit('La clave introducida no es correcta...')
  text = input('  Bloque de texto original: ')
  if (len(text) != 32 or isHexadecimalString(text) == False):
    sys.exit('El texto introducido no es correcta...')
  print()

  # Transformamos las cadenas leídas en matrices
  key_matrix = stringToMatrix(key)
  text_matrix = stringToMatrix(text)

  # Etapa inicial
  print(' # Etapa inicial:\n')
  print('Key:' + matrixToString(key_matrix))
  text_matrix = addRoundKey(text_matrix, key_matrix)
  print('\n  > ' + matrixToString(text_matrix))
  print()

  # 9 iteraciones
  print(' # 9 iteraciones (SubBytes-ShiftRows-MixColumns-AddRoundKey):\n')
  for i in range(9):
    key_matrix = keyExpansion(key_matrix, i)
    print('SubKey ' + str(i + 1) + ': ' + matrixToString(key_matrix))
    text_matrix = subBytes(text_matrix)                # SubBytes
    text_matrix = shiftRow(text_matrix)                # ShiftRows
    text_matrix = mixColumns(text_matrix)              # MixColumns
    text_matrix = addRoundKey(text_matrix, key_matrix) # AddRoundKey
    print('\n        > ' + matrixToString(text_matrix))
    print()

  # Etapa final
  print(' # Etapa final:\n')
  key_matrix = keyExpansion(key_matrix, 9)
  print('SubKey 10: ' + matrixToString(key_matrix))
  text_matrix = subBytes(text_matrix)                # SubBytes
  text_matrix = shiftRow(text_matrix)                # ShiftRows
  text_matrix = addRoundKey(text_matrix, key_matrix) # AddRoundKey
  print('\nBloque de texto cifrado: ' + matrixToString(text_matrix))
  print()