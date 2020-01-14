'''write a program to accept integer user input and print all numbers before it,
also break the loop if the user inputs a specific number of your choice
this program clearlt demonstrates the use of break statement'''
number = int(input('Enter a number:'))
while number > 0:
    if number == 0:
        break
    else:
        number = number -1
        print(number)
print('enter a number grater than 0')