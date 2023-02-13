# RECURSION

def num(n):
    print(n)
    if n <= 1:
        return #base case
    else:
        num(n-1) #recursive case

def fact(n):
    print(n,end=" ")
    if n == 1: #base case
        return 1
    else:
        return n*fact(n-1)#recursive case

num(5)
print(fact(5))