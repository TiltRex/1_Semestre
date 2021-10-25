import numpy as np

x = np.ones((5,5))

print(f"\nLista original --->\n{x}\n")
x[1:-1,1:-1] = 0
print(f"Lista de 0 rodeado por 1 --->\n{x}")