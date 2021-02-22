    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        dummy = ListNode(0, head)
        pred = dummy
        
        while head:
            if head.val == val:
                pred.next = head.next
            
            pred.next = head
            pred = pred.next
            head = head.next
            
        pred.next = head
        return dummy.next
