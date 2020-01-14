#program to print the largest positive number by taking series of inputs from the user
#NOTE: the same program can be implimented using functions
largest =-1
numbers = input('Enter the number with comma:')
num = map(int,numbers.split(','))
print(num)
for i in num:
	if i>largest:
		largest=i
	print(largest,i)
print('largest is:',largest)