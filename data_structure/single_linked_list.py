# definition of ListNode, ListNode: value + link to the next element
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0) # sentinel node as pseudo-head

    def get(self, index:int):
        # if index is invalid
        if index < 0 or index >= self.size:
            return -1

        curr = self.head

        # index steps needed to move from sentinel node to wanted index
        for _ in range(index + 1):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val:int) -> None:
        # if index is greater than the length, the node will not be inserted
        if index > self.size:
            return

        # if index is negative, the node will be inserted at the head of the list
        if index < 0:
            index = 0

        self.size += 1

        # find predecessor of the node to be added
        pred = self.head
        for _ in range(index):
            pred = pred.next

        # node to be added
        to_add = ListNode(val)
        # insertion itself
        to_add.next = pred.next
        pred.next = to_add

    def deleteAtIndex(self, index: int) -> None:
        # if the index is invalid, do nothing
        if index < 0 or index >= self.size:
            return

        self.size -= 1

        # find predecessor of the node to be deleted
        pred = self.head
        for _ in range(index):
            pred = pred.next

        # delete pred.next
        pred.next = pred.next.next
