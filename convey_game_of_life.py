# Convey game of life:
import random,time,copy
width = 10
height = 10
# Create a list of list for the cells:
next_cell = []
for x in range(width):
    # Create a new column:
    column = []
    for y in range(height):
        if (random.randint(0,1) == 0):
            # Add a living cell:
            column.append("#")
        else:
            # Add a dead cell:
            column.append(" ")
        # Next cell is a list of column list:
    next_cell.append(column)
# Main program loop:
while True:
    # Seperate each steps with new line:
    print("\n\n\n\n\n")
    current_cell = copy.deepcopy(next_cell)
    # Print current cell on the screen: 
    for y in range(height):
        for x in range(width):
            # Will print the # or " ":
            print(current_cell[x][y],end=" ")
        # Print the newline at the end of a row:
        print()
    # Calculate the next step's cells based on current step's cells:
    for x in range(width):
        for y in range(height):
            # Get neighbouring coordinates:
            # "% WIDTH" ensures leftCoord is always between 0 and WIDTH - 1:
            leftCoord = (x - 1) % width
            rightCoord = (x + 1) % width
            aboveCoord = (y - 1) % height
            belowCoord = (y + 1) % height
            # Count number of living neighbour:
            num_neighbors = 0
            if current_cell[leftCoord][aboveCoord] == '#':
                # Top-left neighbor is alive:
                num_neighbors += 1 
            if current_cell[x][aboveCoord] == '#':
                # Top neighbor is alive:
                num_neighbors += 1 
            if current_cell[rightCoord][aboveCoord] == '#':
                # Top-right neighbor is alive:
                num_neighbors += 1 
            if current_cell[leftCoord][y] == '#':
                # Left neighbor is alive:
                num_neighbors += 1 
            if current_cell[rightCoord][y] == '#':
                # Right neighbor is alive:
                num_neighbors += 1 
            if current_cell[leftCoord][belowCoord] == '#':
                # Bottom-left neighbor is alive:
                num_neighbors += 1 
            if current_cell[x][belowCoord] == '#':
                # Bottom neighbor is alive:
                num_neighbors += 1 
            if current_cell[rightCoord][belowCoord] == '#':
                # Bottom-right neighbor is alive:
                num_neighbors += 1 
            # Set cell based on Conway's Game of Life rules:
            if current_cell[x][y] == "#" and (num_neighbors == 2 or num_neighbors == 3):
            # Living cells with 2 or 3 neighbors stay alive:
                next_cell[x][y] = "#"
            elif current_cell[x][y] == " " and num_neighbors == 3:
            # Dead cells with 3 neighbors become alive:
                next_cell[x][y] = "#"
            else:
            # Everything else dies or stays dead:
                next_cell[x][y] = " "
    # Add a 1-second pause to reduce flickering:
    time.sleep(1) 


