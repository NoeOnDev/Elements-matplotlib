import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

plt.hist(x, bins=50, color='orange');
plt.xlabel('X-axis');
plt.ylabel('Y-axis');
plt.title('Histogram');
plt.show();