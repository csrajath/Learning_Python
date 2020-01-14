'''
Program to read the file and find the sum of all integers by using regular expression and list comprehension
@author: rajathcs
'''
import re
sum = 0
fname = 'regex_sum_340388.txt'
fopen=open(fname)
fread=fopen.read()
check = re.findall('[0-9]+',fread)
roll = [int(i) for i in check]
for k in roll:
    sum+=k
print(sum)
