grid = [['.', '.', '.', '.', '.', '.'], # 9x5 grid
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
# Printing grid as it is: 
for i in range(len(grid)):
    for j in range(len(grid[0])):
        print(grid[i][j],end=" ")
    print()
# To print pattern on 90 degree clockwise:
for i in range(len(grid[0])): # Column
    for j in range(len(grid)): # Row
        print(grid[j][i],end=" ")
    print()
# To print pattern 90 degree anticlockwise: 
for i in range(len(grid[0])-1,-1,-1):
    for j in range(len(grid)-1,-1,-1):
        print(grid[j][i],end=" ")
    print()
# To print pattern 180 degree clockwise: 
for i in range(len(grid)):
    for j in range(len(grid[0])-1,-1,-1):
        print(grid[i][j],end=" ")
    print()
    
