#Escribe un programa que pida al usuario una lista de números y luego imprima la suma de los números pares en la lista
def suma_num_pares(lista):
    suma = 0
    for num in lista:
        if num % 2 == 0:
            suma += num
    return suma

def main():
    numeros = input("Ingrese una lista de números separados por espacios: ").split()
    numeros = [int(numero) for numero in numeros]  

    suma_pares = suma_num_pares(numeros)
    print("La suma de los números pares en la lista es:", suma_pares)

if __name__ == "__main__":
    main()
