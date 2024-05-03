import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(10, 10);
plt.imshow(x, cmap='hot');
plt.xlabel('X-axis');
plt.ylabel('Y-axis');
plt.title('Heatmap');
plt.show();