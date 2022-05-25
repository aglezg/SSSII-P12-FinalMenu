# ----------------------------------------------------------------------------------------
# Práctica 1: Cifrado de Vernam
# Asignatura: Seguridad en Sistemas Informáticos
# Fecha de entrega: 24/02/2022
# Autor:
# - Adrián González Galván
# - alu0101321219@ull.edu.es
# ----------------------------------------------------------------------------------------
# En este fichero se encuentran las funciones utilizadas para el desarrollo de la práctica.
# ----------------------------------------------------------------------------------------

import os

# Limpia la pantalla de la terminal
def cleanTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Comprueba si una variables es un string
def isString(mystring):
    if (type(mystring) == str):
        return True
    else:
        return False

# Convertir de string a binario
def stringToBinary(mystring):

    if (isString(mystring)):
        # join: Unifica varias cadenas con el separador asignado, en este caso ''
        # format: Cambia el formato a otro especificado, en nuestro caso de string a conjuntos de 8 bits
        return ''.join(format(ord(i), '08b') for i in mystring)
    else:
        return None

# Comprueba si un string es una cadena binaria
def isABinaryString(bstring):

    if (not(isString(bstring))):
        return False

    for letter in bstring:
        if (letter != '1' and letter != '0'):
            return False
    return True

# Transforma una cadena binaria en un array de cadenas binarias de cierta longitud
def stringToArrayOfStringS(mystring, long):
    
    myarray = []
    aux_string = ""

    if(isABinaryString(mystring)):
        for letter in mystring:
            aux_string += letter
            if (len(aux_string) == long):
                myarray.append(aux_string)
                aux_string = ''

        return myarray
    
    else:
        return None

# Convertir una cadena binaria en cadena ascii
def binaryStringToASCIIString(bstring):

    ascii_string = ''

    if (isABinaryString(bstring)):
        binary_array = stringToArrayOfStringS(bstring, 8)
        ascii_string = ''
        for element in binary_array:
            ascii_string += chr(int(element,2))
    else:
        return None

    return ascii_string

# Operación XOR entre cadenas de binario
def bStringXORBString(bstring1, bstring2):

    if (isABinaryString(bstring1) and isABinaryString(bstring2)):
        # Operador XOR en Python: ^ (opera con 2 int)
        # int(string, base): convierte un string en un entero de base 2(binaria)
        numeric_result = int(bstring1, 2) ^ int(bstring2, 2)
        # {0:b} = formato binario
        binary_result = '{0:b}'.format(numeric_result)
        while (len(binary_result) != len(bstring1) or len(binary_result) != len(bstring2)):
            binary_result = '0' + binary_result
        return binary_result
    else:
        return None
