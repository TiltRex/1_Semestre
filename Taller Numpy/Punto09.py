import numpy as np

x = np.ones((3,3))

print(f"\nLista original --->\n{x}\n")
x = np.pad(x, pad_width=1, mode='constant', constant_values=0)
print(f"Lista de 1 rodeado por 0 --->\n{x}")