from sys import argv

def finder(t, s, all = ""):
    i = 0
    table = []
    try:
        with open(t, "r") as f:
            for line in f:
                table.append(line)
        shape = []
        with open(s, "r") as f:
            for line in f:
                shape.append(line)
    except Exception as e:
        return(f"Error: {e}")
    for i in range(len(table)):
        table[i] = table[i].replace("\n", "")
    for i in range(len(shape)):
        shape[i] = shape[i].replace("\n", "")

    for i in range(len(table)):
        if len(table[i]) != len(table[0]):
            print("Error")
            return
    for i in range(len(shape)):
        if len(shape[i]) != len(shape[0]):
            print("Error")
            return
        
    sl = len(shape[0])
    sh = len(shape)
    for i in range(len(table) - sh + 1):
        for j in range(len(table[i]) - sl + 1):
            not_found = False
            for k in range(i, i + sh):
                if not_found:
                    break
                for l in range(j, j + sl):
                    if table[k][l] != shape[k - i][l - j] and shape[k - i][l - j] != " ":
                        not_found = True
                        break
            if not not_found:
                print(f"Found at {j}, {i}")
                for x in range(len(table)):
                    for y in range(len(table[0])):
                        if x >= i and x < i + sh and y >= j and y < j + sl and shape[x - i][y - j] != " ":
                            print(shape[x - i][y - j], end="")
                        else:
                            print("-", end="")
                    print()
                if all != "-a":
                    return
    return("Not found")

            

if __name__ == "__main__":
    if len(argv) < 3:
        print("Error")
    else:
        if len(argv) == 4:
            finder(argv[1], argv[2], argv[3])
        else:
            finder(argv[1], argv[2])