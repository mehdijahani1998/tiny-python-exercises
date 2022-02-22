def cases(n):
    if n == 0:
        return (0,0)
    elif n == 1:
        return (1,1)
    elif n == 2:
        return (2,2)
    elif n == 3:
        return (3,4)
    else:
        return(cases(n-1)[1]+cases(n-2)[1],cases(n-1)[0]+cases(n-1)[1])
        
n = int(input())

print(cases(n)[0]+cases(n)[1])