st = str(input('Enter: ')).replace(' ', '')

# ERRORS
alla = ['+', '-', '*', '/', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

def error_han(lin):
    i = 0
    n = 0
    while i < len(lin):
        if lin[i] != '+' and lin[i] != '-' and lin[i] != '*' and lin[i] != '/' and lin[i] != '0' and lin[i] != '1' and lin[i] != '2' and lin[i] != '3' and lin[i] != '4' and lin[i] != '5' and lin[i] != '6' and lin[i] != '7' and lin[i] != '8' and lin[i] != '9':
            print('Error! Given string contains character/characters that are not one of these:')
            print(alla)
            quit()
        elif (lin[i] == '+' or lin[i] == '-' or lin[i] == '*' or lin[i] == '/') and (lin[i + 1] == '+' or lin[i + 1] == '-' or lin[i + 1] == '*' or lin[i + 1] == '/'):
            print("Error! Given string have two or more operators that don't have number between them!")
            quit()
        elif lin[0] == '+' or lin[0] == '-' or lin[0] == '*' or lin[0] == '/':
            print("Error! Given string doesn't begins with number")
            quit()
        elif lin[len(lin) - 1] == '+' or lin[len(lin) - 1] == '-' or lin[len(lin) - 1] == '*' or lin[len(lin) - 1] == '/':
            print("Error! Given string doesn't ends with number")
            quit()
        elif lin[0] == '0' and i != len(lin) - 1 and (lin[1] != '+' and lin[1] != '-' and lin[1] != '*' and lin[1] != '/'):
            print("Error! Given string contains number/numbers that stars with '0'")
            quit()
        elif lin[i] == '+' or lin[i] == '-' or lin[i] == '*' or lin[i] == '/':
            n += 1
        i = i + 1
    if n == 0:
        print("Error! Given string doesn't contains any operators")
        quit()

error_han(st)



# MAKE LIST
# Makes list
l = 0
arr = []
while l < len(st):
    arr.append(st[l])
    l = l + 1

# Marges string numbers
o = 0;
j = []
while o < len(arr):
    sw = ''
    b = 1
    if (arr[o] != '+' and arr[o] != '-' and arr[o] != '*' and arr[o] != '/') and (arr[o - 1] == '+' or arr[o - 1] == '-' or arr[o - 1] == '*' or arr[o - 1] == '/' ):#or (arr[o] is arr[0])
        sw += arr[o]
     
        while o + b < len(arr) and (arr[o + b - 1] != '+' and arr[o + b - 1] != '-' and arr[o + b - 1] != '*' and arr[o + b - 1] != '/') and (arr[o + b] != '+' and arr[o + b] != '-' and arr[o + b] != '*' and arr[o + b] != '/'):
            sw += arr[o + b]
            b = b + 1
        j.append(sw)    
    elif arr[o] == '+' or arr[o] == '-' or arr[o] == '*' or arr[o] == '/':
        sw += arr[o]
        j.append(sw)   
    
    o = o + 1

# Add first number
hu = []
hi = 0

while hi < len(st):
    if st[hi] == '+' or st[hi] == '-' or st[hi] == '*' or st[hi] == '/':
        co = st[:st.index(st[hi])]
        hu.append(co)
        hi = len(st) - 1
    hi = hi + 1
    
j.insert(0, hu[0]) 



# CALCULATION
t = 0

# Turn number strings to numbers
ba = 0
while ba < len(j):
    if j[ba] != "+" and j[ba] != "-" and j[ba] != "*" and j[ba] != "/":
        j[ba] = int(j[ba])
    ba = ba + 1

# Devide and multiply
while t < len(j):
    if j[t] == '*':
        j[t - 1] = j[t - 1] * j[t + 1]
        j.pop(t + 1)
        j.pop(t)
        t = 0
    elif j[t] == '/':
        j[t - 1] = j[t - 1] / j[t + 1]
        j.pop(t + 1)
        j.pop(t)
        t = 0
    t = t + 1


# Add and subtract
p = 0
while p < len(j):
    if j[p] == '+':
        j[p - 1] = j[p - 1] + j[p + 1]        
        j.pop(p + 1)
        j.pop(p)
        p = 0
    elif j[p] == '-':
        j[p - 1] = j[p - 1] - j[p + 1]
        j.pop(p + 1)
        j.pop(p)
        p = 0
    p = p + 1


print('Answer:', j[0])
