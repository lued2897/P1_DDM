from decimal import *
from numpy import float128 as float128

def main():
    print("Convertidor de bases numéricas")
    input("Presiona Enter para continuar...")
    base1 = int(input("Ingresa la base de origen: "))
    base2 = int(input("Ingresa la base de destino: "))
    numero = string(input("Ingresa el número a convertir: "))

def convertirAlfabeticoADecimal(caracter, base):
    valor_ascii = ord(caracter) - 55
    if valor_ascii >= base:
        raise ValueError(f"El valor {caracter} no pertenece a la base {base}")
    if valor_ascii > 9 and valor_ascii <= 35:
        return valor_ascii
    else:
        raise ValueError(f"El valor {caracter} no se encuentra entre [A - Z]")


def convertirBaseADecimal(numero, base):
    numero_decimal = float128(0)
    posicion_punto = 0
    numero_temporal = float128(0)
    if '.' in numero:
        posicion_punto = numero.index('.')
        posicion = posicion_punto - 1
        
    else:
        posicion = len(numero) - 1

    for digito in numero:
        if digito.isalpha():
            digito = convertirAlfabeticoADecimal(digito, base)
        elif digito == '.':
            continue
        else:
            digito = float128(digito)
        numero_temporal = float128(digito) * (float128(base) ** float128(posicion))
        numero_decimal = numero_decimal + numero_temporal
        posicion -= 1

    return numero_decimal


def convertirDecimalABase(numero, base):
    #Separar el numero en parte entera y parte decimal
    parte_entera = int(numero)
    parte_decimal = numero - parte_entera
    if(parte_decimal > 0):
        print("Se indicara con 11 digitos de precision en el punto")
    
    
    #Trabaja con la parte entera
    numero_base = ""
    while parte_entera > 0:
        residuo = parte_entera % base
        if residuo > 9:
            residuo = chr(residuo + 55)
        numero_base = str(residuo) + numero_base
        parte_entera = parte_entera // base
        
    #Trabaja con la parte decimal
    numero_base += "."
    contador = 0
    while parte_decimal > 0 and contador < 11:
        parte_decimal *= base
        parte_entera = int(parte_decimal)
        if parte_entera > 9:
            parte_entera = chr(parte_entera + 55)
        numero_base += str(parte_entera)
        parte_decimal -= int(parte_decimal)
        contador += 1
        
    return numero_base

def convertir(numero, base1, base2):
    numero_decimal = convertirBaseADecimal(numero, base1)
    numero_base = convertirDecimalABase(numero_decimal, base2)
    return numero_base

