import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5];
y = [2, 3, 5, 7, 11];

errors = [0.5, 0.5, 0.5, 0.5, 0.5];

plt.errorbar(x, y, yerr=errors, fmt='o', color='black');
plt.xlabel('X-axis');
plt.ylabel('Y-axis');
plt.title('Error Bars');
plt.show();