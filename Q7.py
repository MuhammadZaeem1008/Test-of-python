def fibonacci_sequence(n):
    a=0
    b=1
    c=b
    count=1
    while count <= n:
        print(c, end=" ")
        count += 1
        a,b=b,c
        c=a+b
fibonacci_sequence(5)
        