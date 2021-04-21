def Recurse(n):
    if n==0:
        return 1
    else:
        p = n * Rescurse(n-1)
    
    return p

num = int(input("Enter an integer: "))
fact = Rescurse(num)
print(f'Factorial Value for {num} is {fact}.')
