from sys import argv

def rectangle(a, b):
    try:
        a = int(a)
        b = int(b)
    except:
        print ("Error")
        return
    if a <= 0 or b <= 0:
        print ("Error")
        return
    for i in range(b):
        for j in range(a):
            if (i == 0 or i == b - 1) and (j == 0 or j == a - 1):
                print ("o", end="")
            elif i == 0 or i == b - 1:
                print ("-", end="")
            elif j == 0 or j == a - 1:
                print ("|", end="")
            else:
                print (" ", end="")
        print ("\n", end="")

if __name__ == '__main__':
    if len(argv) != 3:
        print ("Error")
    else:
        rectangle(argv[1], argv[2])