def detect_repetition(string, query):
    k = len(query)
    n = len(string)

    rep_number = 0

    for i in range(n-k+1):
        if(string[i:i+k] == query):
            rep_number += 1
    
    return rep_number

m, n = list(map(int, input().split()))

table = [input() for i in range(m)]

query = input()

total_rep_number = 0

for i in range(m):
    total_rep_number += detect_repetition(table[i], query)
    
for j in range(n):
    current_col = []
    for i in range(m):
        current_col.append(table[i][j])
    total_rep_number += detect_repetition(''.join(current_col), query)
    

print(total_rep_number)