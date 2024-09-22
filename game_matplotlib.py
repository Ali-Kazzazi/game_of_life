import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set the size of the world
WORLD_SIZE = 100

# Initialize the world with random live (1) and dead (0) cells
world = np.random.choice([0, 1], WORLD_SIZE*WORLD_SIZE, p=[0.8, 0.2]).reshape(WORLD_SIZE, WORLD_SIZE)

# Function to calculate the next gen of the world
def update(world):
    new_world = world.copy()
    for i in range(WORLD_SIZE):
        for j in range(WORLD_SIZE):
            # Count the number of live neighbors
            live_neighbors = np.sum(world[i-1:i+2, j-1:j+2]) - world[i, j]
            # rules of the Game of Life
            if world[i, j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                new_world[i, j] = 0
                
            elif world[i, j] == 1 and (live_neighbors == 3 or live_neighbors == 2):
                new_world[i, j] = 1
                
            elif world[i, j] == 0 and live_neighbors == 3:
                new_world[i, j] = 1
                
    return new_world

# Function to animate the Game of Life
def animate(frame):
    global world
    world = update(world)
    mat.set_data(world)
    return [mat]

# Set up the animation
fig, ax = plt.subplots(figsize=(6, 6))
mat = ax.matshow(world, cmap='GnBu')
ax.set_xticks([])
ax.set_yticks([])

ani = animation.FuncAnimation(fig, animate, frames=200, interval=100, save_count=50)

plt.show()




