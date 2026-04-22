# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry = False
        head = ListNode(l1.val + l2.val)
        current = head
        
        if head.val >= 10:
            head.val = head.val % 10
            carry = True
            
        l1 = l1.next
        l2 = l2.next
        
        
        while carry or l1 or l2:
            node = ListNode(0)
            if l1:
                node.val += l1.val
                l1 = l1.next
            if l2:
                node.val += l2.val
                l2 = l2.next
            if carry:
                node.val += 1
                carry = False
            if node.val >= 10:
                carry = True
                node.val = node.val % 10
            current.next = node
            current = node
            
        return head