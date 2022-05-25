# ----------------------------------------------------------------
# Práctica 4: Generador C/A de GPS
# Asignatura: Seguridad en Sistemas Informáticos
# Fecha de entrega: 24/03/2022
# Autor:
# - Adrián González Galván
# - alu0101321219@ull.edu.es
# ----------------------------------------------------------------
# En este fichero se incluye el desarrollo del menú de la práctica.
# ----------------------------------------------------------------
from cmath import nan
from CAdeGPS_functions import *
import sys

# Main
def p4CAdeGPS():

  cleanTerminal()

  # Menú principal  y lectura de opciones
  print("\n PRÁCTICA 4: Generador C/A de GPS\n")

  id = input("  ID del satélite: ")
  if (id.isnumeric() == False or int(id) < 1 or int(id) > 32):
    sys.exit('La ID de satélite introducida no es correcta, inténtelo de nuevo...')
  sequence_leng = input('  Longitud de la secuencia de salida: ')
  if (sequence_leng.isnumeric() == False):
    sys.exit('Longitud de secuencia introducida incorrecta, inténtelo de nuevo...')
  print()

  # Vectores a iterar
  LSFR1copy = LSFR1.copy()
  LSFR2copy = LSFR2.copy()

  # Generamos secuencia C/A Code
  print('LFSR1\t\trealimentacion\t\tLSFR2\t\trealimentacion\t\tSecuencia C/A PRN1')
  for i in range(int(sequence_leng)):
    # LSFR1
    print(''.join(map(str, LSFR1copy)), end='')
    print('\t', end='')
    
    # Realimentacion LSFR1
    feed1 = G(LSFR1copy, [3, 10])
    print(feed1, end='')
    print('\t\t\t', end='')

    # LSFR2
    print(''.join(map(str, LSFR2copy)), end='')
    print('\t', end='')

    # Realimentacion LSFR2
    feed2 = G(LSFR2copy, [2, 3, 6, 8, 9, 10])
    print(feed2, end='')
    print('\t\t\t', end='')

    # Secuencia C/A PRN1
    taps = getG2Taps(int(id))
    tapsResult = PRN(taps, LSFR2copy)
    print(str(xor(LSFR1copy[len(LSFR1copy) - 1], tapsResult)))

    # Retroalimentacion
    LSFR1copy = feedback(LSFR1copy, feed1)
    LSFR2copy = feedback(LSFR2copy, feed2)