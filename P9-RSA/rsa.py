# ----------------------------------------------------------------
# Práctica 9: Cifrado RSA
# Asignatura: Seguridad en Sistemas Informáticos
# Fecha de entrega: 05/05/2022
# Autor:
# - Adrián González Galván
# - alu0101321219@ull.edu.es
# ----------------------------------------------------------------
# En este fichero se incluye el desarrollo del menú de la práctica.
# ----------------------------------------------------------------

from rsa_functions import *
import sys

#### Alfabetos a emplear
alphMin = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphMax = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#### Comprueba si una cadena pertenece a un alfabeto
def belongsToAlphabet(string, alphabet):
  for element in string:
    if ((element in alphabet) == False):
      return False
  return True

### Main
def p9RSA():
  cleanTerminal()
  print("\n PRÁCTICA 9: RSA\n")

  ### Lectura de opciones
  # Texto original
  text = input("  text >> ")
  text = text.replace(' ', '')
  if (belongsToAlphabet(text, alphMin) == False and belongsToAlphabet(text, alphMax) == False):
    sys.exit('La cadena introducida no es correcta')

  # Alfabeto utilizado
  alphabet = []
  nullLetter = ''
  if ((belongsToAlphabet(text.replace(' ', ''), alphMin))):
    alphabet = alphMin
    nullLetter = 'x'
  else:
    alphabet = alphMax
    nullLetter = 'X'

  # p
  p = input("  p >> ")
  if (p.isnumeric() == False):
    sys.exit('El parámetro "p" introducido no es correcto...')
  if (lehmanPeralta(int(p), 100) == False):
    sys.exit('El parámetro "p" introducido no es un número primo...')
  p = int(p)

  # q
  q = input("  q >> ")
  if (q.isnumeric() == False):
    sys.exit('El parámetro "q" introducido no es correcto...')
  if (lehmanPeralta(int(q), 100) == False):
    sys.exit('El parámetro "q" introducido no es un número primo...')
  q = int(q)

  # d
  d = input("  d >> ")
  if (d.isnumeric() == False):
    sys.exit('El parámetro "d" introducido no es correcto...')
  d = int(d)

  # n
  n = p * q

  # fi(n)
  fiN = (p -1) * (q - 1)

  # mcd, d
  mcd, e = extendedEuclides(d, fiN)
  if (mcd != 1):
    sys.exit('El parámetro "d" no es primo con fi(n) = ' + str(fiN) + '...')

  # Tamaño de bloques
  blockTam = numOfBlocksToDivide(len(alphabet), n)

  # Pasamos cada bloque a decimal
  decimalBlocks = blocksToDecimal(text, blockTam, alphabet, nullLetter)

  # Ciframos los bloques
  cipherBlocks = encodeMessage(decimalBlocks, e, n)

  ### Resultados
  print('\n  RESULTADOS:')
  print('  >> Los números "p" y "q" son primos')
  print('  >> El número "d" es primo con "fi(n) = ' + str(fiN))
  print('  >> Se calcula e = ' + str(e))
  print('  >> Como n = ' + str(n) + ', se divide el texto en bloques de ' + str(blockTam))
  print('  >> Texto convertido a decimal: ' + str(decimalBlocks))
  print('  >> Texto cifrado en decimal: ' + str(cipherBlocks))