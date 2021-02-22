class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if not head: return head
        
        prev = ListNode(next=head)
        nxt = head.next
        dummyhead = prev
        dupFlag = False
        while nxt:
            if head.val == nxt.val:
                nxt = nxt.next
                dupFlag = True
                continue
            if dupFlag:
                head = nxt
                nxt = nxt.next
                prev.next = head
                dupFlag=False
                continue
            prev = head
            head = nxt
            nxt = nxt.next
        
        if dupFlag: prev.next = None
        return dummyhead.next
        
 # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#  [1,1,2,3,3,4,4,5]
#       
#

# Same solution but more elegant code
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        dummy = ListNode(0, head)
        pred = dummy
        
        while head:
            
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                pred.next = head.next
            else:
                pred = pred.next
                
