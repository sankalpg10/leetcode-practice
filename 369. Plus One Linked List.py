# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        
        dummy = ListNode(0, head)
        notNine = dummy
        
        while head:
            if head.val != 9:
                notNine = head
            head = head.next
        
        notNine.val += 1
        notNine = notNine.next
        while notNine:
            notNine.val = 0
            notNine = notNine.next
            
        return dummy if dummy.val == 1 else dummy.next
        
