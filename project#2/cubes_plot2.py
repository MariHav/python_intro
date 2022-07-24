import matplotlib.pyplot as plt

x_values = range(1,501)
y_values = [x**3 for x in x_values]

plt.style.use('bmh')
fig, ax = plt.subplots()
#ax.scatter(x_values, y_values, c = (0.2,0.2,0.5), s = 5)
ax.scatter(x_values, y_values, c = x_values, cmap = plt.cm.Blues, s = 5)

ax.set_title('Cubes', fontsize = 15, color = 'blue')
ax.set_xlabel('Value', fontsize = 15)
ax.set_ylabel('Cube of Value', fontsize = 15)
ax.tick_params(axis='both', which = 'major', labelsize = 10)

ax.axis([0,510,0,125000000])

plt.show()