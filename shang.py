def detect_repetition(string, query):
    k = len(query)
    n = len(string)

    rep_number = 0

    for i in range(n-k+1):
        if(string[i:i+k] == query):
            rep_number += 1
    
    return rep_number

shang = input()
mehrdad = input()

string = shang

while(len(string)<len(mehrdad)*2):
    string += shang
    
print("\n",string,"\n")
if (detect_repetition(string, mehrdad)>0):
    print("Yes")
else:
    print("No")
    

    