
#! python
import numpy as np
import matplotlib.pyplot as plt

xvals = np.arange(-2, 1, 0.01)
yvals = np.cos(xvals)

newyvals = 1 - 0.5 * xvals ** 2
plt.plot(xvals, newyvals, '--r')

plt.plot(xvals, yvals)
# plt.show()

plt.figure()
xlist = np.linspace(-2.0, 1.0, 100)
print(xvals.__len__())
input()

