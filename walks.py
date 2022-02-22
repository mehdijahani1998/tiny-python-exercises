dis, half, full = list(map(int, input().split()))

if(dis < min(half + full)):
   print(-1)


for i in range((dis // full)+1):
    if ((dis - i*full)%half == 0):
        print((dis - i*full)//half, i)
        break

print(-1)
