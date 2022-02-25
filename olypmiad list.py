number = int(input())

lines = [[] for i in range(number)]

def sort_lines_sex(line):
    return line[0]

def sort_lines_name(line):
    return line[1].lower()

for i in range(number):
    lines[i] = list(input().split("."))
    lines[i][1] = lines[i][1].lower()
    lines[i][1] = lines[i][1].title()
lines.sort(key=lambda x: (sort_lines_sex(x), sort_lines_name(x)))

for i in range(number):
    print("{} {} {}".format(lines[i][0],lines[i][1],lines[i][2]))