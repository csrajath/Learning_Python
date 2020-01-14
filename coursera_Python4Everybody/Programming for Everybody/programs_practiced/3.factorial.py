'''num = int(input('Enter a number:''\n'))
fact = 1
if num < 0:
    print('Enter a positive number.')
elif num == 0:
    print(fact)
else:
    for i in range(1,num+1):
        fact = fact*i
    print(fact)'''
def factorial(x):
    fact=1
    if x==0:
        print(fact)
    elif x < 0:
        print('enter a positive value')
    else:
        for i in range(1,num+1):
            fact = fact*i
        print(fact)
num = int(input('number:'))
print(factorial(num))
