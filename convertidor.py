from decimal import *
from numpy import float64 as float128
import streamlit as st

def main():
    st.title("Convertidor de bases numéricas")
    num = st.text_input("Ingresa el número a convertir:")
    from_base = st.number_input("Ingresa la base de origen::", min_value=2, max_value=34, value=10)
    to_base = st.number_input("Ingresa la base de destino:", min_value=2, max_value=34, value=2)

    st.sidebar.markdown('# Tarea 1 DDM')
    st.sidebar.markdown('## Autores:')
    st.sidebar.markdown('- Ortega Guerrero Moises')
    st.sidebar.markdown('- Ospino Merida Emilio Sebastian')
    st.sidebar.markdown('- Perez Nava Francisco Javier	')
    st.sidebar.markdown('- Perez Osorio Luis Eduardo')

    if st.button("Convertir"):
        try:
            resultado = convertirBaseADecimal(num,from_base)
            resultado = convertirDecimalABase(resultado,to_base)

            print(resultado)
            st.success(f"Resultado: {resultado}")
        except ValueError:
            st.error("Entrada no válida")


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
            print(digito)
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
        print("Se indicara con 16 digitos de precision en el punto")
    
    
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
    while parte_decimal > 0 and contador < 16:
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

if __name__ == '__main__':
    main()

