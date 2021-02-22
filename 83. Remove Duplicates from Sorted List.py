# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return head
        prev = head
        curr = head.next
        
        while curr:
            if curr.val == prev.val:
                curr = curr.next
                continue
                
            prev.next = curr
            prev = curr
            curr = curr.next
            
        prev.next = curr
        return head
