
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(val=None)
        current = head
        
        # O(n + m)
        while l1 and l2:
            if l1.val <= l2.val:
                next_node = ListNode(l1.val)
                l1 = l1.next
            else:
                next_node = ListNode(l2.val)
                l2 = l2.next
            current.next = next_node
            current = next_node
        
        # O(n)
        while l1:
            next_node = ListNode(l1.val)
            l1 = l1.next
            current.next  = next_node
            current = next_node
        
        # O(m)
        while l2:
            next_node = ListNode(l2.val)
            l2 = l2.next
            current.next = next_node
            current = next_node
        return head.next
