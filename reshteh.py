def detect_repetition(string, query):
    k = len(query)
    n = len(string)

    rep_number = 0

    for i in range(n-k+1):
        if(string[i:i+k] == query):
            rep_number += 1
    
    return rep_number

number_of_cmds = int(input())

strings_array = ['' for i in range(100)]
answers = []
queries = []
print(strings_array)

for i in range(number_of_cmds):
    command, index, length, query = list(input().split())
    command = int(command)
    index = int(index) - 1 
    queries.append(query)
    if command == 1:
        strings_array[index]+=query
    
    if command == 2:
        answers.append(detect_repetition(strings_array[index], query))

print("this is queries ",queries)

print("this is strings_array ", strings_array)

print(answers)

for element in answers:
    print(element)





