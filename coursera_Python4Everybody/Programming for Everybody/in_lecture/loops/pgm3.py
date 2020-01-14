'''write a program to demonstrate break and continue statements'''
#continue
numbers = [1,2,3,4,5,0,6,7,8,9]
for i in numbers:
    if i == 0:
        continue
    print(i)
print('End!!!')
#break
number = [1,2,3,4,5,0,6,7,8,9]
for i in number:
    if i == 0:
        break
    print(i)
print('End!!!')