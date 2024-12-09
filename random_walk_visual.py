import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Keep making new walks, as long as the program is active. May need to be run in a dedicated terminal if it wont run otherwise. 
while True:

    # Make a random walk.
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots()  # Creates a new figure for each walk
    ax.scatter(rw.x_values, rw.y_values, s=15)
    ax.set_aspect('equal')

    plt.show()  # Display the plot
   

    # Ask the user if they want to make another walk
    keep_running = input('Make another walk (y,n): ')
    if keep_running.lower() == 'n':  # Ensure it handles uppercase input
        break