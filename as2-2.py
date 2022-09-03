
a=float(input( ' enter your first number : '))
b=input( ' * , / , ** , + , - : ')
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