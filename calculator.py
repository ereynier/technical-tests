from sys import argv

def negative(s):
    i = 0
    while i < len(s):
        if s[i] == "":
            del s[i]
            i -= 1
        if s[i] == "-" and (i == 0 or ord(s[i - 1][-1]) < 48 or ord(s[i - 1][-1]) > 57):
            s[i] = f"-{str(s[i + 1])}"
            del s[i + 1]
        i += 1
    return (s)

def calculator(s):
    s = "".join(s.split(" "))
    i = 0
    #print(s)
    for c in s:
        if (ord(c) < 48 or ord(c) > 57) and c != "." and c != "(" and c != ")" and c != "+" and c != "-" and c != "*" and c != "/" and c != "%":
            return("Error")
    while i < len(s):
        if s[i] == "(":
            j = i + 1
            new_par = 0
            while s[j] != ")" or new_par > 0:
                if s[j] == "(":
                    new_par += 1
                elif s[j] == ")":
                    new_par -= 1
                j += 1
            result = calculator(s[i + 1:j])
            s = s[:i] + str(result) + s[j + 1:]
        i += 1
    splitted_s = []
    j = 0
    for i in range(len(s)):
        if (ord(s[i]) < 48 or ord(s[i]) > 57) and s[i] != ".":
            splitted_s.append(s[j:i])
            splitted_s.append(s[i])
            j = i + 1
    splitted_s.append(s[j:])
    s = splitted_s

    s = negative(s)

    i = 0
    while i < len(s):
        if s[i] == "*" or s[i] == "/" or s[i] == "%":
            #print(s)
            if s[i] == "*":
                result = float(s[i - 1]) * float(s[i + 1])
            elif s[i] == "/":
                result = float(s[i - 1]) / float(s[i + 1])
            elif s[i] == "%":
                result = float(s[i - 1]) % float(s[i + 1])
            s = s[:i - 1] + [str(result)] + s[i + 2:]
            s = negative(s)
            i -= 1
        i += 1
    i = 0
    while i < len(s):
        if s[i] == "+" or s[i] == "-":
            if s[i] == "+":
                result = float(s[i - 1]) + float(s[i + 1])
            elif s[i] == "-":
                result = float(s[i - 1]) - float(s[i + 1])
            s = s[:i - 1] + [str(result)] + s[i + 2:]
            s = negative(s)
            i -= 1
        i += 1
    return (s[0])


if __name__ == "__main__":
    if len(argv) != 2:
        print("Error")
    else:
        print(calculator(argv[1]))