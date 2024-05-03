import matplotlib.pyplot as plt

x = [1, 2, 3];
y = ['A', 'B', 'C'];

plt.pie(x, labels=y, colors=['red', 'green', 'blue']);
plt.xlabel('X-axis');
plt.ylabel('Y-axis');
plt.title('Pie Chart');
plt.show();