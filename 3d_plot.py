import matplotlib.pyplot as plt;

x = [1, 2, 3, 4, 5];
y = [2, 3, 5, 7, 11];
z = [3, 5, 7, 11, 13];

fig = plt.figure();
ax = fig.add_subplot(111, projection='3d'); ax.scatter(x, y, z, c=z, cmap='viridis');
ax.set_xlabel('X-axis');
ax.set_ylabel('Y-axis');
ax.set_zlabel('Z-axis'); ax.set_title('3D Plot');
plt.show();