import numpy as np
from scipy.interpolate import UnivariateSpline
import scipy.stats as stats
from matplotlib import pyplot as plt

N = 1000
n = N//10
s = np.random.normal(size=N)   # generate your data sample with N elements
p, x = np.histogram(s, bins=n) # bin it into n = N//10 bins
x = x[:-1] + (x[1] - x[0])/2   # convert bin edges to centers
f = UnivariateSpline(x, p, s=n)
plt.axis('off')
plt.plot(x, f(x))
plt.show()

h = np.arange(-50, 50)
fit = stats.norm.pdf(h, np.mean(h), np.std(h))
plt.axis('off')
plt.plot(h,fit)
plt.show()