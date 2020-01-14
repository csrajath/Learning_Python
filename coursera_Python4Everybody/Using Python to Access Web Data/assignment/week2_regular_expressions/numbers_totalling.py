'''
Program to read the file and find the sum of all integers by using regular expression
@author: rajathcs
'''
import re
sum=0
fname = 'regex_sum_340388.txt'
fopen = open(fname)
fread = fopen.read()
numCheck = re.findall('[0-9]+',fread)
lst=list()
for i in numCheck:
    lst.append(i)
print(lst)
for k in lst:
    k1 = int(k)
    sum = sum+k1
print(sum)