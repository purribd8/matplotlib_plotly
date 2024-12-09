import matplotlib.pyplot as plt

plt.style.available # shows different styles available use print()

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn-v0_8')# to use styles avaiable call before subplots()
fig, ax = plt.subplots() # fig represents entire chart, ax is the variable representing 1 of many possible plots
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize =24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of ticks labels
ax.tick_params(labelsize=10)

plt.show()