#write a program to take array of numbers from a user and output how many numbers were input and its respective sum.
count =0
sum=0
numbers = input('enter numbers seperated by comma:')
num = map(int,numbers.split(','))
print(num)
for i in num:
	count+=1
	sum = sum+i
print('count=',count)
print('count=',sum)



