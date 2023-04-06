from sys import argv

def fileNorm(file):
    try:
        file = file.split("\n")
        info = file[0]
        laby = file[1:]
        if laby[-1] == "":
            del laby[-1]
        out_c = info[-1]
        in_c = info[-2]
        road_c = info[-3]
        empty_c = info[-4]
        wall_c = info[-5]
        y = int(info[:-5].split("x")[0])
        x = int(info[:-5].split("x")[1])

        if len(laby) != y:
            return ("Error 1")
        nb_in = 0
        for line in laby:
            if len(line) != x:
                return ("Error 2")
            for c in line:
                if c != out_c and c != in_c and c != empty_c and c != wall_c:
                    return ("Error 3")
                if c == in_c:
                    nb_in += 1
        if nb_in != 1:
            return ("Error 4")
        return (None)
    except Exception as e:
        return (f"Error 5: {e}")

def pathfinding(laby, empty_c, in_c, out_c, max_x, max_y, road_c):
    for i in range(len(laby)):
        for j in range(len(laby[i])):
            if laby[i][j] == in_c:
                in_x = i
                in_y = j
    for i in range(len(laby)):
        laby[i] = list(laby[i])

    done = False
    places = [(in_x, in_y)]
    out_place = (-1,-1)
    distance = 0
    while not done:
        new_places = []
        explore = 0
        for place in places:
            if done:
                break
            for i in [-1, 1]:
                if place[0] + i >= 0 and place[0] + i < max_x:
                    if laby[place[0] + i][place[1]] == empty_c:
                        laby[place[0] + i][place[1]] = distance
                        new_places.append((place[0] + i, place[1]))
                        explore += 1
                    if laby[place[0] + i][place[1]] == out_c:
                        out_place = (place[0], place[1])
                        done = True
                        break
                if place[1] + i >= 0 and place[1] + i < max_y:
                    if laby[place[0]][place[1] + i] == empty_c:
                        laby[place[0]][place[1] + i] = distance
                        new_places.append((place[0], place[1] + i))
                        explore += 1
                    if laby[place[0]][place[1] + i] == out_c:
                        out_place = (place[0], place[1])
                        done = True
                        break
        if not done and explore == 0:
            print("Labyrinthe is impossible")
            return
        places = new_places.copy()
        distance += 1
    done = False
    if laby[out_place[0]][out_place[1]] == in_c:
        done = True
    while not done:
        for i in [-1, 1]:
            if out_place[0] + i >= 0 and out_place[0] + i < max_x:
                if laby[out_place[0] + i][out_place[1]] == laby[out_place[0]][out_place[1]] - 1:
                    laby[out_place[0]][out_place[1]] = road_c
                    out_place = (out_place[0] + i,out_place[1])
                    break
                elif laby[out_place[0] + i][out_place[1]] == in_c:
                    laby[out_place[0]][out_place[1]] = road_c
                    done = True
                    break
            if out_place[1] + i >= 0 and out_place[1] + i < max_x:
                if laby[out_place[0]][out_place[1] + i] == laby[out_place[0]][out_place[1]] - 1:
                    laby[out_place[0]][out_place[1]] = road_c
                    out_place = (out_place[0],out_place[1] + i)
                    break
                elif laby[out_place[0]][out_place[1] + i] == in_c:
                    laby[out_place[0]][out_place[1]] = road_c
                    done = True
                    break
    for i in range(len(laby)):
        for j in range(len(laby[i])):
            if isinstance(laby[i][j], int):
                laby[i][j] = empty_c

    for line in laby:
        for i in range(len(line)):
            print(line[i], end="")
        print()
    print(f"Done in {distance - 1} moves")

def labyrinthe(file):
    err = fileNorm(file)
    if err != None:
        print(err)
        return
    file = file.split("\n")
    info = file[0]
    laby = file[1:]
    if laby[-1] == "":
        del laby[-1]
    out_c = info[-1]
    in_c = info[-2]
    road_c = info[-3]
    empty_c = info[-4]
    wall_c = info[-5]
    x = int(info[:-5].split("x")[0])
    y = int(info[:-5].split("x")[1])
    pathfinding(laby, empty_c, in_c, out_c, x, y, road_c)

if __name__ == "__main__":
    if len(argv) != 2:
        print("Error arg")
    else:
        with open(argv[1], "r") as f:
            file = f.read()
        labyrinthe(file)
        try:
            pass
        except Exception as e:
            print(f"Error {e}")