# ----------------------------------------------------------------
# Práctica 12: Menú con todas las prácticas
# Asignatura: Seguridad en Sistemas Informáticos
# Fecha de entrega: 26/05/2022
# Autor:
# - Adrián González Galván
# - alu0101321219@ull.edu.es
# ----------------------------------------------------------------
# En este fichero se incluye el desarrollo del menú de la práctica.
# ----------------------------------------------------------------

import os

# Limpia la pantalla de la terminal
def cleanTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Obtenemos la ruta de los archivos de las distintas prácticas
dirname = os.path.dirname(__file__)
p1 = os.path.join(dirname, 'P1-Vernam\\')
p2 = os.path.join(dirname, 'P2-RC4\\')
p3 = os.path.join(dirname, 'P3-ChaCha20\\')
p4 = os.path.join(dirname, 'P4-CA_de_GPS\\')
p5 = os.path.join(dirname, 'P5-Mult_SNOW3G_AES\\')
p6 = os.path.join(dirname, 'P6-AES\\')
p7 = os.path.join(dirname, 'P7-CBC\\')
p8 = os.path.join(dirname, 'P8-DH_ElGamal\\')
p9 = os.path.join(dirname, 'P9-RSA\\')
p12 = os.path.join(dirname, 'P12-Feige_Fiat_Shamir\\')

# Importamos los dierctorios obtenidos
import sys
sys.path.insert(0, p1)
sys.path.insert(1, p2)
sys.path.insert(2, p3)
sys.path.insert(3, p4)
sys.path.insert(4, p5)
sys.path.insert(5, p6)
sys.path.insert(6, p7)
sys.path.insert(7, p8)
sys.path.insert(8, p9)
sys.path.insert(9, p12)

import vernam, rc4, chacha20, CAdeGPS, mult_SNOW3G_AES, aes, cbc, dh_ElGamal, rsa, feige_fiat_shamir

# Menú a implementar
def show_menu():
  print('   [1] Práctica 1: Entrega Vernam')
  print('   [2] Práctica 2: Entrega RC4')
  print('   [3] Práctica 3: Entrega ChaCha20')
  print('   [4] Práctica 4: Entrega C/A de GPS')
  print('   [5] Práctica 5: Entrega Multiplicación en SNOW 3G y AES')
  print('   [6] Práctica 6: Entrega AES')
  print('   [7] Práctica 7: Entrega Modos de Cifrado en Bloque')
  print('   [8] Práctica 8: Entrega DH y Cifrado de ElGamal')
  print('   [9] Práctica 9: Entrega RSA')
  print('   [10] Práctica 12: Protocolo de Feige-Fiat-Shamir')
  print('   [exit] Salir ')

# Main
option = ''
while (option != 'exit'):
  cleanTerminal()
  print("\n PRÁCTICA 12: Menú con todas las prácticas de la asignatura\n")
  show_menu()
  option = input('\n      >> ')
  if (option == '1'):
    vernam.p1Vernam()
  elif (option == '2'):
    rc4.p2RC4()
  elif (option == '3'):
    chacha20.p3Chacha20()
  elif (option == '4'):
    CAdeGPS.p4CAdeGPS()
  elif (option == '5'):
    mult_SNOW3G_AES.p5Mult_SNOW3G_AES()
  elif (option == '6'):
    aes.p6AES()
  elif (option == '7'):
    cbc.p7CBC()
  elif (option == '8'):
    dh_ElGamal.p8ElGamal()
  elif (option == '9'):
    rsa.p9RSA()
  elif (option == '10'):
    feige_fiat_shamir.p12FeigeFiatShamir()
  elif (option == 'exit'):
    break
  else:
    print('\nOpción incorrecta...')
  if (option != 'exit'):
    input('\nPresiona Enter para continuar...')