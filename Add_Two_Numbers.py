# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def newNode(current, value):
    node = ListNode(val = value)
    current.next = node
    return node

def addCarry(current):
    current.val += 1
    return False

def needCarry(current):
    current.val = current.val % 10
    return True

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry = False
        head = None
        current = None

        while l1 and l2:
            if not head:
                current = ListNode()
                head = current
            else:
                current = newNode(current, 0)

            current.val = l1.val + l2.val

            if carry:
                carry = addCarry(current)
            if current.val >= 10:
               carry = needCarry(current)
            
            l1 = l1.next
            l2 = l2.next
        
        while l1 or l2:
            current = newNode(current, 0)
            if l1:
                current.val += l1.val
                l1 = l1.next
            else:
                current.val += l2.val
                l2 = l2.next

            if carry:
                carry = addCarry(current)
            if current.val >= 10:
                carry = needCarry(current)

        if carry:
            current = newNode(current, 1)

        return head