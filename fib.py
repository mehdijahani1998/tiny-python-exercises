def fib(n, array):
    if(n == 1):
        if(array[n] == 0):
            array[n] = 1
        return array[n]
    if(n == 2):
        if(array[n] == 0):
            array[n] = 2
        return array[n]
    if(array[n] == 0):
        array[n] = fib(n - 1, array) + fib(n - 2, array)
    return array[n]

n = int(input())
array = [0 for i in range(100)]
answer = []

current_index = 1

for i in range(n):
    if i+1 == fib(current_index, array):
        answer.append("+")
        current_index += 1
    else:
        answer.append("-")
        
for element in answer:
    print(element, end='')

print("\n")
        

