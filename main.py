def refact(n):
    if n==0:
        return 1
    else:
        p = n * refact(n-1)
    
    return p

num = int(input("Enter an integer: "))
fact = refact(num)
print(f'Factorial Value for {num} is {fact}.')