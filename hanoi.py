def hanoi(src , dst , aux , n):
    if n == 1:
        return [src, dst]
    elif n == 2:
        return [src, aux, src, dst, aux, dst]
    else:
        temp = hanoi(src, aux, dst, n-1)
        temp2 = []
        
        for element in temp:
            if element == 'A':
                temp2.append('C')
            elif element == 'B':
                temp2.append('A')
            elif element == 'C':
                temp2.append('B')
        return temp + [src, dst] + temp2

n = int(input())

def hanoei(n):
    if n == 1:
        return ['A', 'B']
    else:
        temp = hanoei(n-1)
        temp2 = []
        temp3 = []
        
        for element in temp:
            if element == 'A':
                temp2.append('A')
            elif element == 'B':
                temp2.append('C')
            elif element == 'C':
                temp2.append('B')
               
        for element in temp2:
            if element == 'A':
                temp3.append('C')
            elif element == 'B':
                temp3.append('A')
            elif element == 'C':
                temp3.append('B')
        
        return temp2 + ['A','B'] + temp3
        
answer = hanoei(n)

print("this is answer: ", answer, "\n")

for i in range(len(answer)//2):
    print(i + 1," ",answer[2*i]," ",answer[2*i+1])
    
    