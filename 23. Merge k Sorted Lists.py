# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import *
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return None
        k = len(lists)
        
        mergedList = ListNode()
        head = ListNode(next=mergedList)
        heap = []
        deadNodes = 0
        for i in range(k):
            if lists[i]:
                heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
                
        if not heap: return None
        while heap:
            elem, lastNode = heappop(heap)
            mergedList.val = elem

            if lists[lastNode]:
                heappush(heap, (lists[lastNode].val, lastNode))
                lists[lastNode] = lists[lastNode].next
            
            if not heap: break
            mergedList.next = ListNode()
            mergedList = mergedList.next

        
        return head.next
