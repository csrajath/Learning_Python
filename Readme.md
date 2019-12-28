# Basic Introduction
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
      
  
                
              
#Data Structures
## LinkedList
Learning the basics of linkedlist in python from one of the Medium blog [here](https://medium.com/@kojinoshiba/data-structures-in-python-series-1-linked-lists-d9f848537b4d).\
Learning the implementation knowledge of LinkedList using this blog [here](https://medium.com/inefficient-code/https-medium-com-inefficient-code-building-a-linkedlist-class-in-python-1450aa30a343)

###Introduction
1. Linked list is a chain of values connected with pointers.
2. Linked list consists of nodes.
3. Each node consists of a value and a pointer to another node. 

    ##### Advantanges of LinkedList
    1. The main reason for using linked list is because the elements are dynamically allocated unlike arrays where the size is fixed.
    1. Linked list nodes can live anywhere in the memory. Whereas an array requires a sequence of memory to be initiated
    1. Its easier to add or delete elements at/from any position as compared to array.
		1. In an array, every element as to be moves X number of positions to add an element to that position but in listed list its just mixing and matching the head and tail
    ##### Dis-advantanges of LinkedList
    1. Linear search time - O(n)    
    
    ##### Features of Linked List
    1. LinkedList does not feature by default in python.
    ##### Types of Linked List
     1. Singly linkedList
        1. Each node in a singly linked list has one connecting nodes that is the next one.
     2. Doubly LinkedList
        1. Each node in a doubly linked list has two nodes: one pointing to the next node and one pointing to the previous node.
     3. Circular Linked list
    ##### Applications of Linked List
    1. Navigating backward and forward in a web browser
    2. Undo/Redo in text editors
    1. Lets say a teacher takes 25 students to movie, the teacher can remember the seat number of all the 25 students only if it is in sequential order or some specific progression.
       But if all the 25 students are allocated seats in random way, then the only way for teacher to remember the seat numbers for all of them are by using linked list concept.
       That is, the teacher only remembers the seat number of the first student and the first student holds pointer/address to second. This way teacher can reach all the students.
    ##### Important Points
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

    
 
      