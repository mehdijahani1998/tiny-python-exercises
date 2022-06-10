MOD = 1000000007

n = int(input())
numbers = list(map(int, input().split()))


if 1 not in numbers:
    product = 1
    for num in numbers:
        product = (product * num) % MOD

print(product)