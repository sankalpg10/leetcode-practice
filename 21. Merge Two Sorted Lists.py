# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        elif not l2: return l1
        elif not l1 and not l2: return None
        p1, p2 = l1, l2
        mergeList = ListNode()
        head = ListNode(next = mergeList)
        
        while p1 or p2:
            if p1 and p2:
                if p1.val < p2.val:
                    mergeList.val = p1.val
                    p1 = p1.next
                else:
                    mergeList.val = p2.val
                    p2 = p2.next
            elif p1:
                mergeList.val = p1.val
                p1 = p1.next
            else:
                mergeList.val = p2.val
                p2 = p2.next
            if p1 or p2:
                mergeList.next = ListNode()
                mergeList = mergeList.next
        
        return head.next
