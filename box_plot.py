import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]

bp = plt.boxplot(x, patch_artist=True)
for box in bp['boxes']:
    box.set(color='purple', linewidth=2)
    box.set(facecolor = 'purple' )

plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Box Plot')
plt.show()