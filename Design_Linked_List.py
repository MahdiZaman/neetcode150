class MyLinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

    def get(self, index: int) -> int:
        current = self
        for i in range(index):
            if current is None:
                return -1
            current = current.next
        return current.val
        

    def addAtHead(self, val: int) -> None:
        temp = self
        self = MyLinkedList(val, self)
        # self.val, self.next = node.val, node.next
        # self = node

    def addAtTail(self, val: int) -> None:
        current = self
        while current:
            current = current.next
        current.next = MyLinkedList(val)

    def addAtIndex(self, index: int, val: int) -> None:
        current = self
        for i in range(index-1):
            current = current.next
        temp = current.next
        current.next = MyLinkedList(val, temp)
        # current.next.next = temp 

    def deleteAtIndex(self, index: int) -> None:
        current = self
        for i in range(index):
            current = current.next
        current.next = current.next.next
        

def printll(obj):
    current = obj
    while(current.next):
        print(current.val)
        current = current.next

if __name__=='__main__':
    obj = MyLinkedList()

    obj.addAtHead(1)
    printll(obj)
    
    # obj.addAtTail(3)
    # printll(obj)

    # obj.addAtIndex(1, 2)
    # printll(obj)

    # print(obj.get(1))

    # obj.deleteAtIndex(1)
    # printll(obj)
    # print(obj.get(1)) # should return 1
    
