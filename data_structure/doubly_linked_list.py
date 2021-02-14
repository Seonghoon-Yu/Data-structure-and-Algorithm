# Doubly Linked List Implement

# define ListNode
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prec = None
        
class MyLinkedList:
    def __init__(self):
        self.size = 0
        # pseudo-head and pseudo-tail
        self.head, self.tail = ListNode(0), ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, index):
        # if index is invalid
        if index < 0 or index >= self.size:
            return -1
            
        # choose the fastest way : to move from the head or to move from the tail
        if index + 1 < self.size - index:
            curr = self.head
            for _ in range(index + 1):
                curr = curr.next
                
        else:
            curr = self.tail
            for _ in range(self.size - index + 1):
                curr = curr.prev
        
        return curr.val    
        
    def addAtHead(self, val):
        pred, succ = self.head, self.head.next
        
        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add
        
    def addAtTail(self, val):
        succ, prev = self.tail, self.tail.prev
        
        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add
        
    def addAtIndex(self,index,val):
        # if index is greater than the length
        # the node will not be inserted
        if index > self.size:
            return
            
        # if index is negative
        # the node will be inserted at the head of the list
        if index < 0:
            index = 0
            
        # find predecessor and successor of the node to be added
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next
        else:
            succ = self.tail
            for _ in range(self.size - index):
                succ = succ.prev
            pred = succ.prev
        
        # insertion
        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add
    
    def deleteAtIndex(self, index):
        # if the index is invalid, do nothing
        if index < 0 or index >= self.size:
            return
            
        # find predecessor and successor of the node to be deleted
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = prev.next.next
        else:
            succ = self.tail
            for _ in range(self.size - index - 1):
                succ = succ.prev
            pred = succ.prev.prev
        
        # delete pred.next
        self.size -= 1
        succ.prev = pred
        pred.next = succ
