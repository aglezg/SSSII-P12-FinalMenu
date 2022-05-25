# ----------------------------------------------------------------------------------------
# Práctica 3: Cifrado RC4
# Asignatura: Seguridad en Sistemas Informáticos
# Fecha de entrega: 10/03/2022
# Autor:
# - Adrián González Galván
# - alu0101321219@ull.edu.es
# ----------------------------------------------------------------------------------------
# En este fichero se encuentran las funciones utilizadas para el desarrollo de la práctica.
# ----------------------------------------------------------------------------------------

from ctypes import sizeof
from operator import mod
import os

# Limpia la pantalla de la terminal
def cleanTerminal():
  os.system('cls' if os.name == 'nt' else 'clear')

# Intercambiar 2 elementos de un vector
def swap(vec: list, pos1: int, pos2: int): 
  if (pos1 < 0 or pos1 >= len(vec)):
     return None
  if (pos2 < 0 or pos2 >= len(vec)):
     return None
  value1 = vec[pos1]
  vec[pos1] = vec[pos2]
  vec[pos2] = value1
  return vec

# Inicialización (Key Scheduling Algorithm, KSA)
def KSA(key: list):
  S: list(int) = []
  for i in range(256):
    S.append(i)
  
  j: int = 0
  for i in range(256):
    j = mod(j + S[i] + key[i % len(key)], 256) 
    S = swap(S, i, j)

  return S

# Generación de secuencia cifrante (PRGA)
def PRGA(S: list, generations: int):
  if (generations < 0 or generations > 256):
     return None
  if (len(S) != 256):
    return None
  i: int = 0
  j: int = 0
  it: int = 0
  result: list(int) = []
  while (it < generations):
    i = mod(i + 1, 256)
    j = mod(j + S[i], 256)
    S = swap(S, i, j)
    t: int = mod(S[i] + S[j], 256)
    result.append(S[t]) 
    it+= 1
  return result

# Generación de texto cifrado
def encode(codedSequence: list, message: list):
  if (len(codedSequence) < len(message)):
    return None
  
  result: list(int) = []
  for i in range(len(message)):
    result.append(codedSequence[i] ^ message[i])

  return result

# Pruebas . . .
S = KSA([2, 5])
P = PRGA(S, 2)
print(encode(P, [1, 34]))