import math

string = input()

number_array = [int(a) for a in string]
number_array.reverse()

break_index = [0,0]

flag = False
for i in range(len(number_array)-1):
    if number_array[i] > number_array[i+1]:
        flag = True
        break

calculate = flag
i = 0
while(i < len(number_array) and calculate):
    for j in range(len(number_array)-i):
        if number_array[i]>number_array[i+j]:
            number_array[i], number_array[i+j] = number_array[i+j], number_array[i]
            break_index = [i,i+j]
            calculate = False
            break

#print (break_index, number_array[break_index[0]], number_array[break_index[1]])

if not flag:
    print(0)
else:
    temp_array = number_array[:break_index[1]]
    temp_array.sort()
    temp_array.reverse()
    new_number_array = temp_array + number_array[break_index[1]:]

    number = 0
    for i in range(len(new_number_array)):
        number += pow(10,i)*new_number_array[i]


    print(number)
