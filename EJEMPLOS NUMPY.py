import numpy as np

"""
a = np.array([1,2,3], dtype='int32')
print(a)


######OTRO EJEMPLO############

b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)


###### EJEMPLO  DIMENSION DEL ARREGLO############


print(a.ndim)
print(b.ndim)


###### EJEMPLO FORMA DEL ARREGLO############

print(b.shape)


###### EJEMPLO EL TIPO DE DATOS DEL ARREGLO A############

print(a.dtype)


###### EJEMPLO EL TAMAÑO DEL ARREGLO A############

print(a.itemsize)

print(a.nbytes)

print(a.size)
"""

######################################


a = np.array([[1,2,3,4,5,6,7,],[8,9,10,11,12,13,14]])
print(a[1,5])#### que me muestre lo que esta en la fila 1 columna 5
print(a[0,:])#### que me muestre todo lo que esta solo en la fila 0###
print(a[:,2]) #### no importa la fila pero que me muestre lo que haya en la columna 2 del arreglo###


##REEMPLAZAR VALORES####


a[1,5]=20   ### se reemplaza el 13 de esa posicion por el 20   fila 1 columna 5###

a[:,2] = [1,2] ### se reemplaza lo que hay en fila 0 y 1 lo que haya en sus columnas 2###
print(a)



#VALORES ALEATORIOS#######


print (np.random.rand(4,2))








