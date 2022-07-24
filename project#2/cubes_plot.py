import matplotlib.pyplot as plt

x_values = [1,2,3,4,5]
y_values = [1,8,27,64,125]

plt.style.use('_classic_test_patch')
fig, ax = plt.subplots()
ax.plot(x_values,y_values,linewidth = 3)

ax.set_title('Cubes', fontsize = 20)
ax.set_xlabel('Value', fontsize = 20)
ax.set_ylabel('Cube of Value', fontsize = 20)

ax.tick_params(axis='both', labelsize = 10)

plt.show()

