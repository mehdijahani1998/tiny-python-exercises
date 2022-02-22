lines = int(input())

numbers_array = []
answers_array = []

for i in range(lines):
    command, number = input().split()
    number = int(number)
    
    if command == "Add":
        numbers_array.append(number)
        numbers_array.sort()
    if command == "Ask":
        answers_array.append(numbers_array[number])
        
for element in answers_array:
    print(element)