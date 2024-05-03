import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5];

plt.boxplot(x, color='purple');
plt.xlabel('X-axis');
plt.ylabel('Y-axis');
plt.title('Box Plot');
plt.show();