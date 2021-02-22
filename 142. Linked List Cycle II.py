# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        tortoise = head
        hare = self.startNodeforHare(head)
        if not hare: return None
        
        return self.getCycleStartNode(tortoise, hare)
        
    def startNodeforHare(self, head):
        tortoise = head
        hare = head
        while hare is not None and hare.next is not None:
            tortoise = tortoise.next
            hare = hare.next.next
            if hare == tortoise:
                return hare
            
        return None
    
    def getCycleStartNode(self, tortoise, hare):
        
        while hare != tortoise:
            hare = hare.next
            tortoise = tortoise.next
            
        return hare
