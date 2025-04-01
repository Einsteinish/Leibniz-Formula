import numpy as np
import matplotlib.pyplot as plt

n = 100
terms = (-1)**np.arange(n) / (2 * np.arange(n) + 1)
partial_sums = np.cumsum(terms)
plt.plot(partial_sums, label='Leibniz Series')
plt.axhline(np.pi/4, color='r', linestyle='--', label='π/4')
plt.legend()
plt.title('Leibniz Formula Converging to π/4')
plt.xlabel('Terms')
plt.ylabel('Sum')
plt.show()
