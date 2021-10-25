import numpy as np

x = np.array([1,2,3], dtype=np.float64)
print(f"Tamaño de la lista ---> {x.size}")
print(f"Longitud de un elemento de la lista en bytes ---> {x.itemsize}")
print(f"Numero total de bytes consumidos por los elementos de la lista ---> {x.nbytes}")
