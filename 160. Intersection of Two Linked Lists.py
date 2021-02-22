# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB: return
        l1 = headA
        l2 = headB
        
        lastElement = None
        while True:
            
            if l1 == l2:
                return l2
            
            if l1.next != None:
                l1 = l1.next
            else:
                if lastElement is None: lastElement = l1
                elif lastElement != l1: break
                l1 = headB
                
            if l2.next != None:
                l2 = l2.next
            else:
                if lastElement is None: lastElement = l2
                elif lastElement != l2: break
                l2 = headA

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        len1, len2 = 0, 0
        temp = headA
        while temp: temp, len1 = temp.next, len1 + 1
        temp = headB
        while temp: temp, len2 = temp.next, len2 + 1
        
        long = headA if len1 > len2 else headB
        short = headB if len1 > len2 else headA
        
        diff = abs(len1 - len2)
        while diff > 0:
            long = long.next
            diff -= 1
        
        while short and long != short:
            long = long.next
            short = short.next
        
        return short
