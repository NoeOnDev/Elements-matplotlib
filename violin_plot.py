import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

plt.violinplot(x, showmedians=True, showmeans=False, showextrema=False); plt.xlabel('X-axis');
plt.ylabel('Y-axis');
plt.title('Violin Plot');
plt.show();