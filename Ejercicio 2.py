#Define una función llamada "inverso_palabra" que reciba una cadena como parámetro y devuelva la cadena invertida. Por ejemplo, si la entrada es "python", la salida debería ser "nohtyp".
def palabra_inversa(cadena):
    return cadena[::-1]
    
original = input("Ingrese la palabra a dar en inversa: ")
invertida = palabra_inversa(original)
print("La cadena invertida es:", invertida)
