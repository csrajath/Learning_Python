# General
1. A python script is a text file storing lines of instructions writing according to python programming language and saved with the extension *.py*
2. *’!’* is called as *‘bang’*
3. *>>>* is called as the *chevron* prompt
### New Line
1. Represented by ***\n***
2. ***\n*** is also a character, a single character
3. While reading the contents of the file, the file handler considers the ***'enter'*** key stroke equivalent to newline character
1. White spaces that we dont see but exists
### Importing
```
    from functiondoc import *
```
1. Anything after ‘from’ is the name of the python file and anything after ‘import’ is the method being considered.
### Understanding *print()* function
1. by default considers a new line charcter, that is as soon as something is printed out to the console, the cursor of print function points to the new line i.e the immediate next.
    1. *end=''* is used to remove the newline character that print function takes by default
        1. Example:
            1. ```print('Hi',end='w')```
1. As we know that print by default takes a new line, Adding new line to the print function will actually skip one line and print on the third line.
            ```print('hello','\n')```
1. print function vs return statement 
    1. *return()*  sends the value whereas *print()* is to display message for human understanding.
    2. If a function does not return anything the function dies there and cannot be re-used at any other part.'
        1. Example:
            ```
            def function_that_prints():
                print("I printed")
            def function_that_returns():
                return "I returned"
            f1 = function_that_prints()
            f2 = function_that_returns()
            print("Now let us see what the values of f1 and f2 are")
            print(f1)
            print(f2)
            ```
            ```
            OUTPUT:
            I printed                                                           
            Now let us see what the values of f1 and f2 are                     
            None                                                            
            I returned  
            ```
    3. return basically sends the value obtained to the object that calls the function.
    4. It is good practice to ensure that the function or a method always returns something.
### Difference between '==' and is keyword:
   ##### ***Note***: Works on limited data structures, like lists, tuple and dictionaries
   1. ***==***
        1. checks for *equality*
   1. ***is***
        1. checks for identity of the object in memory\
 Understanding the concept with real world example:
            1. Me and my brother each having a bottle of coke means that we both are holding two same or equal items but they are two in number that is he is having his own and I am holding my own.\
            Programmatically, equality symbol (**==**) checks for the content of the variables where as **is** checks if the same address is present in the in object holding that content.\
            In our above example: Me holding coke and my brother holding coke are two different entities hence *me is brother* returns *false*.\
            *Code Example:*
            ```python
            l1 = [1,2,3,4,5]
            l2 = [1,2,3,4,5]
            if l1 is l2:
               print(True)
            else:
               print(False)
           *****************************************************************************************************
           The below code returns False because *l1* variable as its own address in the memory and *l2* as its own
           ******************************************************************************************************
            l1 = [1,2,3,4,5]
            l1 = [1,2,3,4,5]
            l2 = [1,2,3,4,5]
            if l1 = l2:
               print(True)
            else:
               print(False)
           *****************************************************************************************************
           The above code returns True as both variables hold same.
           ```

# Basic Introduction
## Reserved Words

1. There are around 33 of them. They can’t be used to name a variable. Reserved words have pre-defined or in-built functionality
1. To read more about keywords/reserved words and the rules that they are bound by which makes/creates an identifier: click (here)[https://www.programiz.com/python-programming/keywords-identifier]

## Format Specifiers in Python


## Expressions
Append this doc by reading the below documentation.
(here)[https://docs.python.org/3.8/reference/expressions.html#conditional-expressions]
## Constants
1. Something that doesn’t change
	1. Numeric Constant
	1. String Constant

## Variables – 
1. Basically, used to allocate a value and assign a memory to it. The value can change based on further instructions.
	1. Ex: sum = 0
		1. This mean the variable ‘sum’ is assigned the value of 0
1. Can be anything but to be bound by naming rules
	1. Naming Rules:
        1.  Is case sensitive
        2.  NUM’ is different from ‘num’
        3.  Can start with character or underscore (best to avoid underscore)
        4.  Cannot start with numeric or special character
        5.  Cannot consist of a special character in between
            1. Ex: num.ber = 5
                1. Wrong variable name declaration
        6. .	Best practice for using variable names is to use something that is pneumonic than gibberish
## Operator and Operation
1. *‘/’* operator is for division purpose and it provides floating point result.
1. *‘//’* operator is for division purpose and it provides integer output.
2. *=* is an assignment operator, which says assign some value to a variable holding a place/address in your memory
	1. ex: x = 2
        1. *x* is a variable holding a place in memory (RAM) and 2 is the value allocated to that memory
1. In python3, when division operation occurs, the result by default is a float unless explicitly type casted.
1. *%* is the modulo operator that returns the result of a division
    1. Modulo operator can be used in many situations, like:
    	1. even odd calculation
        1. throwing a random value (example: take a huge number and module with 6(no. of throws in die) to get a random die output
    ### Precedence of Operations
    1. Expression evaluation in python is from left to write after following BODMAS
        1. Also, basically just the left to write is followed when - we have nothing but just multiplication division or addition subtraction
    ### Bitwise Operator and Operations
    ### Others:
        1. Python cannot manipulate or perform operation on two different data types
		    1. example: x = 'hi' + 1
			    1. this would result in typeerror
			    2. 
## Type Conversions

## Conditional Statements
1. One can write any number of consecutive conditional statements, same or otherwise
	1. Example:  
        if can be followed by another if
    	elif can be followed by another elif
    	if can be followed by else
    	else cannot have condition attached to it
1. Even if there are multiple if and/or else-if blocks and multiple of them satisfy the condition, the execution will provide only one output.
	1. Classic example:
	```
    if x <2:
		print(‘ok’)
	elif x<5:
		print(‘Sure’)
	else:
		print(‘bye’)
	```
    1. Now, in the above example, if the user input for x is 1, then both ‘if’ and ‘elif’ condition matches/satisfies but still the output will be only ‘ok’ because after one condition satisfy the condition comes out of the block and stops. The agenda of elif or nested ifs is to ensure that only if primary condition fails to check the conditions mapped to them. Also, in the above example it is not mandatory to have else. Without else, the program would look like below:
	```if x <2:
		print(‘ok’)
	elif x<5:
		print(‘Sure’)
	print(‘bye’)```
if user input for x is 20, it would directly print ‘bye’ after checking for if and elif

## Exception Handling
### TRY
1. Acts as a checker.
### EXCEPT
1. If what we have checked in TRY isn’t satisfied then what ever is under EXCEPT will be executed.
1. If we don’t need any operation to occur after EXCEPT we can use quit()
## Functions
   1. Functions act like '*store and re-use*' pattern
   1. Functions work on DRY principles, Dont repeat yourself. i.e functions are used to avoid repetetive tasks
        1. ***def*** is the key word used to define a function\
        1. from the below syntax we can note that functions in python3 follow a general structure:\       
            ```python
             def function_name():
            ```             
            1. keyword def is followed by the name of the function which is followed by braces and a colon.
         1. functions can be called or invoked.
         1.  anything written/passed inside the braces of the function are called *parameters or arguments* 
                1. in the below example, *name* is a parameter passed to the function 
         ```python
            def function(name):
          ```
## Loops
   1. Looping is all about repetitive conditional checks.
   1. There are two types of loops in python:\
    1. ***while***
        1. These are in-definite loops, keeps going/iterating until the condition fails.
        1. *while* syntax:
        ```python
         while expression:
              what ever the statements
        ```
      The variable used in the expressions in the above syntax is called as an iteration variable.\
    2. ***for***
        1. This is a definite loop
        1. for loop statement assumes that there exists a list of items that it needs to loop through
        1. for basically checks for range of values/objects
        1. *for* syntax:
        ```python
         for variable in expression:
              what ever the statements
        ```
        1. Variable here is the iteration variable\
	  1. Expression is usually a collection like files, lists etc
	        1. for example:
                ```python
                      for i in [1,2,3,4,5]:
                            print(i)
                ```
        1. *range* function:
            1. built in function used to iterate over a sequence of elements (be it integer or string)
            1. it is passed as an expression to for loop
            example:
                ```python
                  for i in range(0,5):
               ```
               the above example means that the variable *i* is looped over the range 0,1,2,3,4
            1. *range()* three parameters: 
                1. the starting boundary (which is inclusive)
                1. the closing boundary (which is exclusive i.e in the above example 5 is not printed)
                1. step value used to create increments
                    ```python
                   for i in range(10, 100, 30):
                    ```          
                   the output of the above statement will be in the increments of 30 starting from 10 i.e. 10, 40, 70
## Statements
1. ***break***:
    1. when *break* is encountered, it forcefully runs out of the loop.
    1. after *break*, anything that is de-indented in the loop block will be executed.\
    Example:
    ```python
    while True:
       if n == 2:
           break
       print('HI')
    print('BYE') 
   ```
   1. If user input is 2 then BYE will be executed else 'HI' will be printout to console.
1. ***continue***
    1. it basically means - quit on the current iteration and go to next iteration.
	1. *continue* does not completely abort the loop, it just skips the current iteration and proceeds further i.e goes back to the top of the loop.
2. ***pass***
    1. does absolutely nothing
1. ***with***
    1.  
## Problems Practiced for loops 

# Data Types
## Lists
1. These are collection holding more than one value in a variable.
1. Lists is a data structure which holds more than one element in a single variable.
2. Square brackets are used to create a list
3. It is not mandatory to hold similar type of data within a list.
    1. Example:
        1. A list can be like below, holding an integer, floating point and a string.
            1. name = ['name',1,23.3]
4. A list can internally hold a list.
    1. Example: 
        1. fruits = ['mango',['banana',chiku],'apple']
5. Each element in a list can be looked up using their index, that is to say: Elements in list are bound by index values starting from zero.
6. Lists are mutable whereas strings are immutable. That is, the value of an element in a list can be changed where as the value of a character in a string cannot be.
7. The range function, *range()*, actually returns a list. 
    1. Example:
        1. print(range(4))
            1. the above python statement would throw the result of : [0, 1, 2, 3]
    1. Thus, range function is used to loop through the indexes of a list.
1. It is important to note that, in python whenever we are accessing any elements in a list through an index we use the square brackets.
2. Anything present within the list is a string.
3. Another way to create a new list is by assigning the *list()* constructor to a variable and that variable will be of list type.
    ### Operations on Lists
    1. All the operations that can be performed on a list can be known by printing the below python code which displays all the methods that are pre-built to the *list()* function
    ```python
    dir(list())
    ```
    2. Concatenation:
        1. Irrespective of the type of elements in the list, two lists can be added using the *+ (plus)* operator.
            1. Example: 
                1. ```python
                    name = [1,'d','sdf']
                    number = ['asd',2,5,4]
                    full = name + number
                    print(full)
                    ```
    1. Slicing
        1. *':'* inside a *[]* is used to perform slicing operation on lists
        ```python
        name = [1,'d','sdf']
        print(name[1:3]) #print the range, 3 is exclusive
        print(name[:]) #print the complete list
        print(name[0:]) #print everything from the first element
        print(name[:2]) # print till the second element, note that 2 does not represent second element. 2 is exclusive. 
        print(name[-3:-1]) # printing list elements using negative numbers which accesses lists in reverse order, where -1 points to the last element
        ```
## Dictionaries 
1. Python does not have an in-built switch functions, instead it is suggested to use Associate Arrays or what can be called as DictionaryMapping.
1. 
### OrderedDict
1. Used to store the order in which the elements were entered but it does not order the current elements.
### Notes/Info
1. Dictionaries cannot hold more than one same key, it can have multiple same values.
	1. If there exists same keys within dictionaries then the latest one overrides the previous.
		1. Example:
			```python
			check = {'a':23,'b':23,'a':234}
			print(check)
			```
		prints only ```{'b':23,'a':234}```
## Tuples
1. Tuples are immutable
1. There are few things that cannot be done with tuple.
    1. Tuples do not have in-built *sort* method and *append* method.
    3. Difficult to reverse a tuple.
1. The items() method of a dictionary returns a tuple.
1. Tuples are comparable, i.e.:
    1. the values present within two or more tuples can be compared with each other.
    2. Tuples can compare both integer values and string values but not each other.
    3. Also, tuple comparison is based on index by index. That is, if the first index comparison is true it returns true or false if false. Only if that respective positional indexes are same on both the sides then the comparison shifts to next index.
### Problems Practiced:
1. Reverse a tuple.
2. Top Ten most common words in a file.
## Files
Python interacting with files means that the program is ommunicating with other files on hard disk or cloud.\
Flat files - files with plain textual data that does not link to other files and contain data that is structured using delimiters.
### File Operations / Processing
1. Opening a file:
    1. Before reading the file contents one most open the file.
    2. In Python, *open()* function is used to open a file.
    3. *open()* function returns a file handlers or a file pointer used to perform file operations.
    4. Syntax:
        1. 
    5. If the mode is not defined, by default it will take 'r' read mode.
    5. Example:
        1. open_file = open('example.txt','w')
        2. In the above example, open_file is the file handler
        3. If a for loop is executed on the above file handler, then the for loops runs through the file line by line.
1. Error Handling in Files:
    1. 
### Errors
1. If we try to open a file that is not present we get a ***FileNotFoundError***
2. If the file cannot be opened we get a ***OSError***

# Data Structures
## LinkedList
Learning the basics of linkedlist in python from one of the Medium blog [here](https://medium.com/@kojinoshiba/data-structures-in-python-series-1-linked-lists-d9f848537b4d).\
Learning the implementation knowledge of LinkedList using this blog [here](https://medium.com/inefficient-code/https-medium-com-inefficient-code-building-a-linkedlist-class-in-python-1450aa30a343)

### Introduction
1. Linked list is a chain of values connected with pointers.
2. Linked list consists of nodes.
3. Each node consists of a value and a pointer to another node. 

    #### Advantanges of LinkedList
    1. The main reason for using linked list is because the elements are dynamically allocated unlike arrays where the size is fixed.
    1. Linked list nodes can live anywhere in the memory. Whereas an array requires a sequence of memory to be initiated
    1. Its easier to add or delete elements at/from any position as compared to array.
		1. In an array, every element as to be moves X number of positions to add an element to that position but in listed list its just mixing and matching the head and tail
    #### Dis-advantanges of LinkedList
    1. Linear search time - O(n)    
    
    #### Features of Linked List
    1. LinkedList does not feature by default in python.
    #### Types of Linked List
     1. Singly linkedList
        1. Each node in a singly linked list has one connecting nodes that is the next one.
     2. Doubly LinkedList
        1. Each node in a doubly linked list has two nodes: one pointing to the next node and one pointing to the previous node.
     3. Circular Linked list
    #### Applications of Linked List
    1. Navigating backward and forward in a web browser
    2. Undo/Redo in text editors
    1. Git commits, each commit points to a parent commit
    1. Lets say a teacher takes 25 students to movie, the teacher can remember the seat number of all the 25 students only if it is in sequential order or some specific progression.
       But if all the 25 students are allocated seats in random way, then the only way for teacher to remember the seat numbers for all of them are by using linked list concept.
       That is, the teacher only remembers the seat number of the first student and the first student holds pointer/address to second. This way teacher can reach all the students.
    #### Important Points
    1. Its important to keep track of head (in most of the cases).
    1. If the node points to null/none then we know its the last element in the list
    1. If a node at the first or last position is to be deleted or added, then equally the head or the tail needs to be moved
    ##### Most Probable Interview Questions
    
##TODO:
**LinkedList Practice Problem.**\
 *Problem Statement:*\
1.  https://medium.com/inefficient-code/https-medium-com-inefficient-code-building-a-linkedlist-class-in-python-1450aa30a343\
1.  https://github.com/kojino/data-structures-algorithms/tree/master/linked_list
    - add a node
    - print all node values
    - return number of nodes in a list
    - locate node by position
    - search for node by value
    - insert node after another node
    - insert node at given index
    - insert node at end
    - replace node
    - remove node
    
# Object Oriented Programming
## Class
1. Class is the blue print of the program depicting program’s behavior.
1. An object is an instance of a class.
1. Attribute is the feature of an object.
    1. example: object name can of type float. Hence, float is the attribute
1. *self* is the representation of the object inside the class.
    1. Layman Example: at home whenever someone calls us how can we recognize that it was him/her only (dad,mom or bro,sis only). Because we recognize their voice. Similarly, when a method is called by an object, the self-parameter acts as a voice by telling the method that this the object that is calling you.
1. 	In python2, classes were defined using below syntax:\n 
    ```class class_name(object):```
    The equivalent in python3 is:
        ```class class_name:```
    1. In python2, object basically meant that: this is the base class and we are in-turn not inheriting any other class

## Methods
### init method
1. ```__init__``` is the right way to use init method, is means initialization. 
1. init is a constructor and a reserved method.
1. Whenever an instance of a class is created, init method is called and the instance argument is passed to init method.
1. It is not mandatory to call the init method, however is considered a good practice because instances of a class usually store some sort of state information and the methods of the class offer a way to manipulate that state information. ```__init__``` allows us to initialize this state information while creating an instance of the class.
```
class Bank(object):
    def __init__(self, deposit):
        self.amount = deposit
    def withdrawl(self, amount):
        self.amount -= amount
    def deposit(self, amount):  
        self.amount += amount
    def balance(self):
        return self.amount
b = Bank(10000)
print(b.balance())
b.withdrawl(1000)
print(b.balance())
b.deposit(2000)
print(b.balance())
```
### Practiced
1. printing first n even number
1. Factorial Program
1. Program to count the total number of words and print the word with highest frequency and its count	
1. Factors of a given number problem
1. Write a python program to read delimited data from a flat file and print appropriate message using it. A similar python implimentation of the example seen [here](https://www.computerhope.com/jargon/f/flatfile.htm)
2. Open a file and loop through each line to print the total count of lines in that file.
1. Sorting hat problem in python
3. Read the whole file and print the total count of characters. Also, print the first 10 characters of the file
4. Open a file, if it is not present create it and print all lines that starts with 'In'. Also, ensure to eliminate blank lines. Also, demonstrate this using rstrip() function.
5. Ask for the file name from user and open that file, if the user enters incorrect file name perform error handling. Print the total number of lines if the file name is correct.