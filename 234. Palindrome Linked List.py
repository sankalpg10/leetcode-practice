# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        if not head: return True
        dummy = head
        n = 0
        while head: head, n = head.next, n+1 # find length of list
        if n == 1: return True # if len is 1 return true
        
        head = dummy
        prev = head
        head = head.next
        prev.next = None
        
        currInd = 1
        # invert the first half of the list
        while currInd < n // 2:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
            currInd += 1
        
        # if n is odd then ignore centre number
        if n % 2 == 1:
            head = head.next
        invHead = prev
        # palindrome check
        while head:
            if head.val != invHead.val:
                return False
            head = head.next
            invHead = invHead.next
            
        return True
