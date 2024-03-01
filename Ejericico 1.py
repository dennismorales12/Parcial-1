# Escribe una función en Python que reciba una lista como parámetro y devuelva la suma de todos los elementos de la lista.
def suma_lista(lista):
    suma = 0
    for elem in lista:
        suma += elem
    return suma

lista_dada = [1, 2, 3, 4, 5]
res = suma_lista(lista_dada)
print("La suma de los elementos de la lista es:", res)
