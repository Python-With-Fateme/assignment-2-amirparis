a=int(input(' enter first grade : '))
b=int(input(' enter second grade : '))
c=int(input(' enter third grade : '))
d=int(input(' enter fourth grade : '))
e=int(input(' enter fifth grade : '))
m=(a+b+c+d+e)/5
if m>=17:
    print=(m)
    print(' student is the best ')
if m<17 and m>=12:
    print(m)
    print(' student is normal ')
if m<12 :
    print(m)
    print(' student is failed ')