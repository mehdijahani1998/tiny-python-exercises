def show_number(n):
    if n!=0:
        m = int(input())
        show_number(m)
        print(n)

show_number(int(input()))
