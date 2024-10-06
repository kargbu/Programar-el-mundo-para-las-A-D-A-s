# Sumar de sublistas
#
# Programa una lista de números y que calcule la suma de una sublista específica por usuario

lista = [-5,-6,-7,-8,-9,0,9,8,7,6,5]
indice1 = int(input("Ingresa la primera posición de la sublista a sumar "))
indice2 = int(input("Ingresa la posición final de la sublista a sumar "))
sublista = lista[indice1:indice2+1]
suma = sum(sublista)
print(f" La suma de los números de la lista es: {suma}")
