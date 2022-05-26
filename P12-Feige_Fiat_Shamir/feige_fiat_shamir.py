# ----------------------------------------------------------------
# Práctica 12: Menú con todas las prácticas
# Asignatura: Seguridad en Sistemas Informáticos
# Fecha de entrega: 26/05/2022
# Autor:
# - Adrián González Galván
# - alu0101321219@ull.edu.es
# ----------------------------------------------------------------
# En este fichero implementa el protocolo de Feige-Fiat-Shamir.
# ----------------------------------------------------------------

from tabnanny import verbose
from feige_fiat_shamir_functions import *
import sys

# Main()
def p12FeigeFiatShamir():
  cleanTerminal()
  print('\n PRÁCTICA 12 - Feige-Fiat-Shamir\n')

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

  # n
  n = p * q

  # Número de secretos a utilizar
  number_of_secrets= input (' ¿Número de secretos a utilizar? > ')
  if (number_of_secrets.isnumeric() == False):
    sys.exit('El parámetro introducido no es un número positivo...')
  number_of_secrets = int(number_of_secrets)

  # Identificación secreta de A (s)
  s = []
  for i in range(number_of_secrets):
    value = input('   s[' + str(i + 1) + '] >> ')
    if (value.isnumeric() == False):
      sys.exit('El valor de los secretos debe ser un número positivo...')
    mcd, e = extendedEuclides(int(value), n)
    if (mcd != 1):
      sys.exit('Los valores de "s" deben ser primos con n = ' + str(n) + '...')
    if (int(value) <= 0 or int(value) > n):
      sys.exit('ERROR: 0 < secreto < n')
    s.append(int(value))

  # Identificación pública de A
  v = []
  for value in s:
    v.append(quickExp(value, 2, n))

  # Compromiso secreto de A
  r = input(' Entero aleatorio >> ')
  if (r.isnumeric() == False):
    print('El entero aleatorio debe ser un dígito numérico...')
  r = int(r)

  sign = input('  Signo aleatorio >> ')
  if (sign.lstrip('-+').isdigit() == False):
    sys.exit('El signo debe ser un número...')
  if (int(sign) != 1 and int(sign) != -1):
    sys.exit('El signo debe ser "+1" o "-1"...')
  sign = int(sign)

  # Testigo: A envía a B
  x = sign * quickExp(r, 2, n)


  # Reto: B envía a A
  bits = [0] * number_of_secrets
  i = 0
  while (i < number_of_secrets):
    value = input(' bit[' + str(i) + '] >> ')
    if (value != '0' and value != '1'):
      print('El valor introducido no es correcto, por favor introduzca un bit...')
    else:
      bits[i] = int(value)
      i+= 1

  # Respuesta: A envía a B
  y = r
  for i in range(number_of_secrets):
    y *= quickExp(s[i], bits[i], n)
  y = y % n

  # Verificación
  ySquared = quickExp(y, 2, n)
  verification = x
  for i in range(number_of_secrets):
    verification *= quickExp(v[i], bits[i], n)
  verification = verification % n

  # Resultados
  print('\n  Resultados!')
  print('   * n (p * q) == ' + str(n))
  print('   * Identificación secreta de A == ' + str(s))
  print('   * Identificación pública de A == ' + str(v))
  print('   * Compromiso secreto de A:')
  print('      >> entero aleatorio = ' + str(r))
  print('      >> signo aleatorio = ' + str(sign))
  print('   * Testigo: A envía a B (x) == ' + str(x))
  print('   * Reto: B envía a A (bits) == ' + str(bits))
  print('   * Respuesta: A envía a B (y) == ' + str(y))
  print('   * Verificación == ' + str(ySquared == verification))
  print('       >> y ^ 2 (mod ' + str(n) + ') = ' + str(ySquared))
  print('       >> verification = ' + str(verification))