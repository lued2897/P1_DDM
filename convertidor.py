def main():
    print("Convertidor de bases numéricas")
    input("Presiona Enter para continuar...")
    base1 = int(input("Ingresa la base de origen: "))
    base2 = int(input("Ingresa la base de destino: "))
    numero = str(input("Ingresa el número a convertir: "))

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
    
def encontrarNumeroDigitos(numero, base):
    valor = 0
    digitos = -1
    while numero > valor:
        digitos += 1
        valor = (base ** digitos) * (base - 1)
        print(f"Valor: {valor}")
    
    return digitos

#convertirBaseADecimal("AFF7CD901", 16, 2)
#encontrarNumeroDigitos()

base = int(input("Hola indica la base jajaja: "))
numero = float(input("Hola indica el numero jajaja: "))

print(convertirDecimalABase(numero, base))


