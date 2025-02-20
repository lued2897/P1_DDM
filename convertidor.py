def main():
    print("Convertidor de bases numéricas")
    input("Presiona Enter para continuar...")
    base1 = int(input("Ingresa la base de origen: "))
    base2 = int(input("Ingresa la base de destino: "))
    numero = string(input("Ingresa el número a convertir: "))

def convertirAlfabeticoADecimal(caracter):
    valor_ascii = ord(caracter) - 55
    if valor_ascii > 9 and valor_ascii <= 35:
        return valor_ascii
    else:
        raise ValueError(f"El valor {caracter} no se encuentra entre [A - Z]")

def convertirBaseADecimal(numero, base):
    numero_decimal = 0
    posicion = len(numero) - 1
    for digito in numero:
        if digito.isalpha():
            digito = convertirAlfabeticoADecimal(digito)
        else:
            digito = int(digito)
        print(f"Digito: {digito} , {digito * (base ** posicion)}")
        numero_decimal += digito * (base ** posicion)
        posicion -= 1

    print(numero_decimal)

def convertirDecimalABase(numero, base):
    numero_base = ""
    
def encontrarNumeroDigitos(numero, base):
    valor = 0
    digitos = -1
    while numero > valor:
        digitos += 1
        valor = (base ** digitos) * (base - 1)
        print(f"Valor: {valor}")
    
    return digitos

convertirBaseDecimal("AFF7CD901", 16, 2)
encontrarNumeroDigitos()