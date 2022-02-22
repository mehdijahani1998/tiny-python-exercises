n,k = list(map(int, input().split()))
array = list(map(int, input().split()))

start_index = 0
current_index = 0
answers_array = []

for index in range(n):
    while(start_index <= n-k and current_index < n):

        if (current_index == n-1):
            if (current_index - start_index + 1 >= k):
                for i in range(current_index-start_index-k+2):
                    answers_array += [start_index+i,start_index+k-1+i]
            current_index = n

        if (current_index < n-1 and array[current_index+1] >= array[current_index]):
            current_index +=1
        
        if (current_index < n-1 and array[current_index+1] < array[current_index]):

            if(current_index - start_index + 1 < k):
                start_index = current_index + 1
                current_index = start_index

            else:
                for i in range(current_index-start_index-k+2):
                    answers_array += [start_index+i,start_index+k-1+i]
                start_index = current_index+1
                current_index = start_index


#print(answers_array)
index = 0
while (index < len(answers_array)):
    print("{} to {}".format(answers_array[index],answers_array[index+1]))
    index += 2


        

