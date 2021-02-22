# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        prev = head
        current = head.next
        prev.next = None
        while current != None:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        
        return prev
            
        
