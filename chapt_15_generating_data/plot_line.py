import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# The function plt.subplots() can generate one or more plots in the same figure.
fig, ax = plt.subplots()

# set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# set size of tick labes
ax.tick_params(labelsize=14)

# the ax.plot() method, which tries to plot the data it’s given in a meaningful way
ax.plot(input_values, squares, linewidth=3)



# The function plt.show() opens Matplotlib’s viewer and displays the plot
plt.show()