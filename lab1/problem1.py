

def computeGCD(x, y):
 
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
             
    return gcd
 
a = input('Choose a number')
b = input('Choose a number again')

# prints 12
print (computeGCD(60,48))
