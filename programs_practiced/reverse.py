'''def reverse(s):
    str =""
    for i in s:
        str = i + str
    return str
s = 'rajath'
print(reverse(str))
#print(reverse(str))'''
def reverse(string):
    string = string[::2]
    return string
s = '1234567898'
print(reverse(s))