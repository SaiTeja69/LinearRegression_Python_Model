import matplotlib.pyplot as plt
import numpy as np
def ploting(weight,slope):
 x = np.array(range(10))
 y = x * weight +slope[0]
 plt.plot(x,y)
 plt.show()
