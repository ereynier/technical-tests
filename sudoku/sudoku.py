from sys import argv

def arrayCopy(a):
    dup = []
    for i in range(len(a)):
        dup.append([])
        for j in range(len(a[i])):
            dup[i].append(a[i][j])
    return (dup)
def gridNorm(grid):
    if len(grid) != 9:
        print ("Error")
        return (False)
    for i in range(9):
        if len(grid[i]) != 9:
            print ("Error")
            return (False)
        for j in range(9):
            if grid[i][j] != "." and (ord(grid[i][j]) < 49 or ord(grid[i][j]) > 57):
                print ("Error")
                return (False)
    return (True)

def checkVal(grid, x, y, val):
    for i in range(9):
        if grid[x][i] == val or grid[i][y] == val:
            return (False)
    for i in range((x - x%3), (x - x%3) + 3):
        for j in range((y - y%3), (y - y%3) + 3):
            if grid[i][j] == val:
                return(False)
    return (True)

def searchVal(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == ".":
                for val in range(1,10):
                    val = str(val)
                    if checkVal(grid, i, j, val):
                        tmp_grid = arrayCopy(grid)
                        tmp_grid[i][j] = val
                        next = searchVal(tmp_grid)
                        if next == -2:
                            return (tmp_grid)
                        elif next != -1:
                            return (next)
                return(-1)
    return(-2)

def sudoku(grid):
    grid = grid.split("\n")
    for i in range(len(grid)):
        grid[i] = list(grid[i])
    if gridNorm(grid) == False:
        return
    new_grid = searchVal(grid)
    if new_grid == -2:
        print("Grid is already complete")
    elif new_grid == -1:
        print("This grid is not correct")
    else:
        for line in new_grid:
            for i in line:
                print(i, end="")
            print()

if __name__ == '__main__':
    if len(argv) != 2:
        print ("Error")
    else:
        try:
            with open(argv[1], "r") as f:
                grid = f.read()
            sudoku(grid)
        except Exception as e:
            print (f"Error: {e}")