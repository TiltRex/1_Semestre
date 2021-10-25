import numpy as np

x = [10, 20, 30]
print(f"Lista original ---> {x}")
x = np.append(x, [[40, 50, 60], [70, 80, 90]])
print(f"Lista luego de agregar valores al final ---> {x}")
