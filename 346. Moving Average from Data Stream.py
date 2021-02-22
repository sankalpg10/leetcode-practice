class DLNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None
        
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.capacity = size
        self.head = DLNode()
        self.tail = DLNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.sum = 0
        self.size = 0

    def next(self, val: int) -> float:
        
        if self.size == self.capacity:
            removed_elem = self.del_top()
            print(removed_elem, val)
            self.sum -= removed_elem
            self.size -= 1
        self.sum += val
        self.size += 1
        newelem = DLNode(val)
        self.add_bottom(newelem)
        return self.sum/self.size
    
    def del_top(self):
        removedNode = self.head.next
        self.head.next = removedNode.next
        removedNode.next.prev = self.head
        return removedNode.val
    
    def add_bottom(self, node):
        self.tail.prev.next = node
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev = node
        

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
