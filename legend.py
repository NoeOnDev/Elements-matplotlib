import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, label='My data')

plt.legend(loc='upper right',
           fontsize=12,
           title='Legend',
           title_fontsize='large',
           shadow=True,
           fancybox=True,
           frameon=True,
           edgecolor='black')
plt.show()