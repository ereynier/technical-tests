from sys import argv
from random import choices

def generator(x,y,density):
    if density > 100:
        density = 100
    if density < 0:
        density = 0
    print(f"{x}.xo")
    for i in range(x):
        for j in range(y):
            print(choices([".","x"], weights=(100-density, density), k=1)[0], end="")
        print()

if __name__ == "__main__":
    if len(argv) == 4:
        x = int(argv[1])
        y = int(argv[2])
        density = int(argv[3])
        generator(x,y,density)