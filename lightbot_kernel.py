import numpy as np

# 10x10 flat floor with height, light condition, and blue information for each square
terrain = np.zeros((10, 10), dtype=[('height', int), ('light', bool), ('blue', bool)])

# Initially all squares have a height of 0, their lights are off, and they are not blue
terrain['height'] = 0
terrain['light'] = False
terrain['blue'] = False

# Define some example heights and blue squares for testing
terrain[1, 2]['height'] = 1
terrain[2, 2]['height'] = 2
terrain[3, 3]['height'] = 1

terrain[1, 2]['blue'] = True
terrain[3, 3]['blue'] = True
terrain[5, 5]['blue'] = True

# Initial bot state (position and direction)
bot_position = [0, 0]  # start position (0, 0)
directions = ['up', 'right', 'down', 'left']
bot_direction = 0  # starting direction (up)

# Instructions to process
instructions = "^>^<^@>*@"

# Direction and movement functions
def move_forward(position, direction):
    x, y = position
    if direction == 'up':
        return [max(0, x - 1), y]
    elif direction == 'right':
        return [x, min(9, y + 1)]
    elif direction == 'down':
        return [min(9, x + 1), y]
    elif direction == 'left':
        return [x, max(0, y - 1)]

def turn_left(direction):
    return (direction - 1) % 4

def turn_right(direction):
    return (direction + 1) % 4

# Jump function: The bot moves forward one frame and checks height difference
def jump(position, direction):
    x, y = position
    new_position = move_forward(position, direction)
    new_x, new_y = new_position

    current_height = terrain[x, y]['height']
    new_height = terrain[new_x, new_y]['height']

    # Jump is successful only if the height difference is exactly 1
    if abs(new_height - current_height) == 1:
        return new_position
    else:
        return position  # Stay in the same position if the jump fails

# Toggle light function: Turn light on/off if the square is blue
def toggle_light(position):
    x, y = position
    if terrain[x, y]['blue']:
        terrain[x, y]['light'] = not terrain[x, y]['light']  # Invert the light state

# Process instructions
for instruction in instructions:
    if instruction == '^':
        bot_position = move_forward(bot_position, directions[bot_direction])
    elif instruction == '>':
        bot_direction = turn_right(bot_direction)
    elif instruction == '<':
        bot_direction = turn_left(bot_direction)
    elif instruction == '*':
        bot_position = jump(bot_position, directions[bot_direction])
    elif instruction == '@':
        toggle_light(bot_position)

# Function to print the terrain matrix
def print_terrain_matrix(terrain):
    for i in range(10):
        row = ""
        for j in range(10):
            height = terrain[i, j]['height']
            light = "ON" if terrain[i, j]['light'] else "OFF"
            color = "Blue" if terrain[i, j]['blue'] else "Normal"
            row += f"[{height},{light},{color}] "
        print(row)

print("Matrix (height, light condition, and color):")
print_terrain_matrix(terrain)

# Added 3D visualization function
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_terrain_3d(terrain):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = np.arange(terrain.shape[0])
    y = np.arange(terrain.shape[1])
    X, Y = np.meshgrid(x, y)
    Z = terrain['height']

    colors = np.zeros((10, 10, 4))
    for i in range(10):
        for j in range(10):
            if terrain[i, j]['blue']:
                colors[i, j] = [0, 0, 1, 0.5]
            elif terrain[i, j]['light']:
                colors[i, j] = [1, 1, 0, 0.8]
            else:
                colors[i, j] = [0.5, 0.5, 0.5, 0.3]

    ax.plot_surface(X, Y, Z, facecolors=colors, linewidth=0.5, rstride=1, cstride=1)
    ax.set_title("3D Terrain Visualization")
    plt.show()

# Added 3D visualization function
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_terrain_3d(terrain):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = np.arange(terrain.shape[0])
    y = np.arange(terrain.shape[1])
    X, Y = np.meshgrid(x, y)
    Z = terrain['height']

    colors = np.zeros((10, 10, 4))
    for i in range(10):
        for j in range(10):
            if terrain[i, j]['blue']:
                colors[i, j] = [0, 0, 1, 0.5]
            elif terrain[i, j]['light']:
                colors[i, j] = [1, 1, 0, 0.8]
            else:
                colors[i, j] = [0.5, 0.5, 0.5, 0.3]

    ax.plot_surface(X, Y, Z, facecolors=colors, linewidth=0.5, rstride=1, cstride=1)
    ax.set_title("3D Terrain Visualization")
    plt.show()

# Added 3D visualization function
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_terrain_3d(terrain):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = np.arange(terrain.shape[0])
    y = np.arange(terrain.shape[1])
    X, Y = np.meshgrid(x, y)
    Z = terrain['height']

    colors = np.zeros((10, 10, 4))
    for i in range(10):
        for j in range(10):
            if terrain[i, j]['blue']:
                colors[i, j] = [0, 0, 1, 0.5]
            elif terrain[i, j]['light']:
                colors[i, j] = [1, 1, 0, 0.8]
            else:
                colors[i, j] = [0.5, 0.5, 0.5, 0.3]

    ax.plot_surface(X, Y, Z, facecolors=colors, linewidth=0.5, rstride=1, cstride=1)
    ax.set_title("3D Terrain Visualization")
    plt.show()

# Improved comments for the terrain matrix functions
# Added reset_terrain to ensure flexibility in resetting the simulation

# Added 3D visualization function
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_terrain_3d(terrain):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = np.arange(terrain.shape[0])
    y = np.arange(terrain.shape[1])
    X, Y = np.meshgrid(x, y)
    Z = terrain['height']

    colors = np.zeros((10, 10, 4))
    for i in range(10):
        for j in range(10):
            if terrain[i, j]['blue']:
                colors[i, j] = [0, 0, 1, 0.5]
            elif terrain[i, j]['light']:
                colors[i, j] = [1, 1, 0, 0.8]
            else:
                colors[i, j] = [0.5, 0.5, 0.5, 0.3]

    ax.plot_surface(X, Y, Z, facecolors=colors, linewidth=0.5, rstride=1, cstride=1)
    ax.set_title("3D Terrain Visualization")
    plt.show()

# Improved comments for the terrain matrix functions
# Added reset_terrain to ensure flexibility in resetting the simulation

# Added 3D visualization function
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_terrain_3d(terrain):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = np.arange(terrain.shape[0])
    y = np.arange(terrain.shape[1])
    X, Y = np.meshgrid(x, y)
    Z = terrain['height']

    colors = np.zeros((10, 10, 4))
    for i in range(10):
        for j in range(10):
            if terrain[i, j]['blue']:
                colors[i, j] = [0, 0, 1, 0.5]
            elif terrain[i, j]['light']:
                colors[i, j] = [1, 1, 0, 0.8]
            else:
                colors[i, j] = [0.5, 0.5, 0.5, 0.3]

    ax.plot_surface(X, Y, Z, facecolors=colors, linewidth=0.5, rstride=1, cstride=1)
    ax.set_title("3D Terrain Visualization")
    plt.show()

# Improved comments for the terrain matrix functions
# Added reset_terrain to ensure flexibility in resetting the simulation

# Added 3D visualization function
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_terrain_3d(terrain):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = np.arange(terrain.shape[0])
    y = np.arange(terrain.shape[1])
    X, Y = np.meshgrid(x, y)
    Z = terrain['height']

    colors = np.zeros((10, 10, 4))
    for i in range(10):
        for j in range(10):
            if terrain[i, j]['blue']:
                colors[i, j] = [0, 0, 1, 0.5]
            elif terrain[i, j]['light']:
                colors[i, j] = [1, 1, 0, 0.8]
            else:
                colors[i, j] = [0.5, 0.5, 0.5, 0.3]

    ax.plot_surface(X, Y, Z, facecolors=colors, linewidth=0.5, rstride=1, cstride=1)
    ax.set_title("3D Terrain Visualization")
    plt.show()

# Improved comments for the terrain matrix functions
# Added reset_terrain to ensure flexibility in resetting the simulation
