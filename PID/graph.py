#%%

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# intializes numpy array
x = np.array([1, 2, 3, 4])
y = np.array([1, 2, 3, 6])
# plt.plot(x, y) #np.sin(x)
# plt.show()


x = np.append(x, [10])
y = np.append(y, 10)
plt.plot(x, y)
plt.show()

