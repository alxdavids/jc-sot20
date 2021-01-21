import numpy as np
from matplotlib import pyplot as plt

def laplace(x, mu, b):
    coeff = (np.divide(1, 2*b))
    return coeff*(np.exp(-np.divide(np.absolute(x - mu), b)))
    
x = np.arange(-100, 100)
xDec = np.divide(x, 10)
epsilons = [1, 0.5, 0.25, 0.1, 0.01]
for e in epsilons:
    p = laplace(x, 0, np.divide(1, e))
    axes = plt.gca()
    axes.set_ylim(0, 0.6)
    axes.text(3, 0.5, "ε = {}".format(e), fontsize=25)
    plt.plot(xDec, p)
    plt.show()