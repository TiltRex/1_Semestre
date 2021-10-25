import numpy as np

##Tipos de Array en NumPy##
#Array unidimensional#
a = np.array((1,2,3))

#Array multidimensional#
a = np.array([1,2],[10,20])

"""--------------------------------------------"""

##Arrays en NumPy##
#Array unidimensional sin ningun elemento#
np.empty(2)

#Array multidimensional sin ningun elemento#
np.empty([2,3])

#Array unidimensional con ceros#
np.zeros(2)

#Array multidimensional con ceros#
np.zeros([2,3])

#Array unidimensional con unos#
np.ones(2)

#Array multidimensional con unos#
np.ones([2,3])

#Array unidimensional con rangos de elementos#
np.arange(3)

#Array multidimensional con rangos de elementos#
np.arange([2,7])

#Array con elementos aleatorios#
np.random.rand(3,2)

"""--------------------------------------------"""

##Añadir y eliminar elementos##
#Añadir#
a= np.array((1,2,3))
np.append(a,(4,5))

#Eliminar#
a= np.array((1,2,3))
np.delete(a,(1))