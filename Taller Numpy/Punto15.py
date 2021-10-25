import numpy as np

x = np.sqrt([1+0j])
y = np.sqrt([0+1j])
print(f"Primera lista --->{x}")
print(f"Segunda lista --->{y}")
print("Parte real de las listas:")
print(x.real)
print(y.real)
print("Parte imaginaria de las listas:")
print(x.imag)
print(y.imag)