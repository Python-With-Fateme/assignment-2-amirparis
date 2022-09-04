import math
a=float(input( ' enter your first number : '))
b=input( ' * , / , ** , + , - : ')

if b=='+' or b=='-' or b=='*' or b=='/' or b=='**' :
    c=float(input(' enter your second number : '))

if b=='*' :
    print(a*c)
elif b=='/':
    print(a/c or c/a)
elif b=='**' :
    print(a**c or c**a)
elif b=='+' : 
    print(a+c)
elif b=='-' :
    print(a-c or c-a)

if b=='sin' :
    print(math.sin(a))

if b=='fabs' :
    print(math.fabs(a))

if b=='sqrt' :
    print(math.sqrt(a))