import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.title("horizontal bar")
plt.bar(x, y, width=0.6)

plt.subplot(1, 2, 2)
plt.title("vertical bar")
plt.barh(x, y, height=0.5)

plt.show()
