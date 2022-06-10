n = int(input())

sof = input()

javab = True

for i in range(n):
    if sof[i] == "S" and sof[i+n] == "S":
        javab = False
    elif sof[i] == "F" and sof[i+n] == "F":
        javab = False


if javab:
    print("YES")
else:
    print("NO")

