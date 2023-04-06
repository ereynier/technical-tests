from sys import argv

def fileNorm(file):
    grid = file.split("\n")
    info = grid[0]
    grid = grid[1:]
    if grid[-1] == "":
        del grid[-1]
    try:
        nb_line = int(info[:-3])
        if nb_line < 1:
            return ("Error: Number of line is 0 or less")
    except:
        return ("Error: first info is not a number")
    if len(grid) != nb_line:
        return ("Error: number of line not match with info")
    line_len = len(grid[0])
    for line in grid:
        if len(line) < 1:
            return ("Error: Lines length is 0 or less")
        if len(line) != line_len:
            return ("Error: all the lines have not the same length")
        for i in line:
            if i != info[-2] and i != info[-3]:
                return ("Error: lines include other chars")
    return (None)

def checkObs(grid, x, y, size, obs):
    for i in range(x, x + size):
        for j in range(y, y + size):
            if grid[i][j] == obs:
                return (True)
    return (False)

def square(file):
    err = fileNorm(file)
    if err != None:
        print(err)
        return
    grid = file.split("\n")
    info = grid[0]
    grid = grid[1:]
    if grid[-1] == "":
        del grid[-1]
    empty = info[-3]
    obs = info[-2]
    max_size = 0
    x = -1
    y = -1
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            for s in range(1, min([len(grid[i]) - j + 1, len(grid) - i + 1])):
                tmp_s = s
                if checkObs(grid, i, j, s, obs):
                    tmp_s = s - 1
                    break
                tmp_s = s
            if tmp_s > max_size:
                max_size = tmp_s
                x = i
                y = j
    for i in range(len(grid)):
        grid[i] = list(grid[i])
    
    for i in range(x, x + max_size):
        for j in range(y, y + max_size):
            grid[i][j] = info[-1]
    for line in grid:
            for i in line:
                print(i, end="")
            print()

if __name__ == "__main__":
    if len(argv) != 2:
        print("Error")
    else:
        with open(argv[1], "r") as f:
            file = f.read()
        square(file)
        try:
            pass
        except Exception as e:
            print(f"Error: {e}")

