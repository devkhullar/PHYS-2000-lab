import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('discharge.xlsx')

# data_array = df.to_numpy()
# transposed_array = data_array.transpose()
# x1 = np.array(transposed_array[0])
# y1 = np.array(transposed_array[1])
x1 = np.array([1,2,3,4])
y1 = np.array([1,2,3,4])
plt.plot(x1, y1)
plt.show()
