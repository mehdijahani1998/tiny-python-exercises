number_of_lines = int(input())

dick = {}

for i in range(number_of_lines):
    line = input().split()
    dick.update({line[1]:line[0]})
    dick.update({line[2]:line[0]})
    dick.update({line[3]:line[0]})

sentence = input().split()

for i in range(len(sentence)):
    if (dick.get(sentence[i])!=None):
        sentence[i] = dick.get(sentence[i])

for word in sentence:
    print(word, end=" ")
