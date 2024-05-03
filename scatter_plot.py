import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5];
y = [2, 3, 5, 7, 11];

plt.scatter(x, y, color='red', s=50);
plt.xlabel('X-axis');
plt.ylabel('Y-axis');
plt.title('Scatter Plot');
plt.show();