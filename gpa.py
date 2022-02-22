from numpy import number


def gpa_equiv(score):
    if score < 20 and score >= 16:
        return 4
    elif score >= 14:
        return 3
    elif score >= 12:
        return 2
    elif score >= 10:
        return 1
    else:
        return 0

total_score = 0
total_units = 0

while(True):
    a = input().split(" ")
    if a[0] == "end":
        break
    else:
        score = float(a[0])
        unit = float(a[1])
        total_score += gpa_equiv(score)*unit
        total_units += unit

print(total_score, total_units)
print("gpa is: ", total_score/total_units)