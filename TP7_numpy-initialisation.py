import numpy as np
from numpy import int8

r = int(input("nombre de rangées: "))
c = int(input("nombre de colonnes: "))
def initialisation(m, n):
    # np.random.seed(0)
    tab = np.random.randn(m, n)
    # col = np.ones((m, 1), dtype=int8)
    # print(col)
    tab = np.concatenate((tab, np.ones((tab.shape[0], 1), dtype=int8)), axis=1)
    return tab


print(initialisation(r, c))
