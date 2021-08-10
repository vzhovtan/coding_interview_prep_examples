"""
Merge two sorted linked list and keep the resulted linked list sorted
"""

class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  

class LinkedList: 
    def __init__(self): 
        self.head = None
  
    def printList(self): 
        temp = self.head 
        while temp: 
            print(temp.data, end=" ") 
            temp = temp.next
  
    def addToList(self, newData): 
        newNode = Node(newData) 
        if self.head is None: 
            self.head = newNode 
            return
  
        last = self.head 
        while last.next: 
            last = last.next  
        last.next = newNode 
  
def mergeLists(headA, headB): 
    dummyNode = Node(0) 
    tail = dummyNode 
    while True: 
        # If any of the list gets completely empty directly join all the elements of the other list 
        if headA is None: 
            tail.next = headB 
            break
        if headB is None: 
            tail.next = headA 
            break
  
        # Compare the data of the lists and whichever is smaller is appended to the last of the merged list and the head is changed 
        if headA.data <= headB.data: 
            tail.next = headA 
            headA = headA.next
        else: 
            tail.next = headB 
            headB = headB.next
  
        # Advance the tail 
        tail = tail.next
  
    # Returns the head of the merged list 
    return dummyNode.next
  
# driver code
listA = LinkedList() 
listB = LinkedList() 

listA.addToList(5) 
listA.addToList(10) 
listA.addToList(15) 
  
listB.addToList(2) 
listB.addToList(3) 
listB.addToList(20) 

listA.head = mergeLists(listA.head, listB.head) 
print("Merged Linked List is:") 
listA.printList()
print()