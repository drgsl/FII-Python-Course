def isPalindrome(s):
    return s == s[::-1]

def spiralOrder(matrix):
    ans = []
 
    if (len(matrix) == 0):
        return ans
 
    m = len(matrix)
    n = len(matrix[0])
    seen = [[0 for i in range(n)] for j in range(m)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    x = 0
    y = 0
    di = 0
 
    # Iterate from 0 to R * C - 1
    for i in range(m * n):
        ans.append(matrix[x][y])
        seen[x][y] = True
        cr = x + dr[di]
        cc = y + dc[di]
 
        if (0 <= cr and cr < m and 0 <= cc and cc < n and not(seen[cr][cc])):
            x = cr
            y = cc
        else:
            di = (di + 1) % 4
            x += dr[di]
            y += dc[di]
    return ans

def change_case(str):
    res = [str[0].lower()]
    for c in str[1:]:
        if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            res.append('_')
            res.append(c.lower())
        else:
            res.append(c)
     
    return ''.join(res)


def countvowels(string):
    num_vowels=0
    for char in string:
        if char in "aeiouAEIOU":
           num_vowels = num_vowels+1
    return num_vowels

def computeGCD(x, y):
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
             
    return gcd
 

def pb1():
    a = input('Choose a number')
    b = input('Choose a number again')

    print (computeGCD(x,y));

def pb2():
    inString = input("Please type a string")
    print(countvowels(inString))

def pb3():
    inString1 = input("first string: ")
    inString2 = input("2nd string: ")
    print(inString2.count(inString1))
     
def pb4():
    inString = input('STRING! NOW! : ')
    outString = change_case(inString)
    print(outString)

def pb5():
    a = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]
 
    for x in spiralOrder(a):
        print(x, end=" ")
    
def pb6():
    inString = input("input string: ")
    print(isPalindrome(inString))
    
def pb7():
    inString = input('write a text containing numbers')
    res = [int(i) for i in inString.split() if i.isdigit()]
    print(res[0])

def pb8():
    c = input("a number")
    # Python 10
    # print(inNumber.bit_count())
    print(bin(c))

def pb9():
    inString = input('A string, please')
    fr = {}
    for i in inString.lower():
        if i in fr:
            fr[i]+=1
        else:
            fr[i] = 1

    res = max(fr, key = fr.get)
    print(res)

def pb10():
    inString = input(' one last string i need: ')
    result = len(inString.split(',', 3))
    print("There are " + str(result) + " words.")

if __name__ == '__main__':
    
    # pb1()
    # pb2()
    # pb3()
    # pb4()
    # pb5()
    # pb6()
    # pb7()
    pb8()
    # pb9()
    # pb10()