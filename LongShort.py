n=int(input('enter the number of trades'))
a=0
b=0
while n>0:
    y=input('Long or Short')
    y=(y.upper())
    if y == 'LONG':
        a+=1
        n-=1
    elif y == 'SHORT':
        b+=1
        n-=1
    else:
        print('enter a valid input')
print('Long=',a)
print('Short=',b)
    
    
