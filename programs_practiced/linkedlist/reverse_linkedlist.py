class Linkedlist:
    def __init__(self,head):
        self.head = head
        self.next = None
    def reverse(self,head):
        self.head = head
        prev = None
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        print(prev)
node1 = Linkedlist(2)
node2 = Linkedlist(3)
node3 = Linkedlist(4)
node4 = Linkedlist(5)
node1.next = node2
node2.next = node3
node3.next = node4
node1.reverse(head)

