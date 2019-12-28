class Linkedlist:
    def __init__(self,val):
        self.val = val
        self.next = None
    def traverse(self):
        node = self
        while node:
            print(node.val)
            node = node.next
        #print('Bye')
    def reverse(self):
        node = self
        prev = None
        while node:
            temp = node
            node = node.next
            temp.next = prev
            prev = temp
            #print(prev.val)
        print(prev)

node1 = Linkedlist(1)
node2 = Linkedlist(2)
node3 = Linkedlist(3)
node4 = Linkedlist(4)
node1.next = node2
node2.next = node3
node3.next = node4

#node1.remove_duplicates()
node1.traverse()
node1.reverse()

