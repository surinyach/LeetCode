# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        first = True
        head = None
        while list1 or list2:
            if first:
                head = ListNode(0)
                current = head
                first = False
            else:
                current.next = ListNode(0)
                current = current.next
                
            if list1 and list2:
                if list1.val < list2.val:
                    current.val = list1.val
                    list1 = list1.next
                else:
                    current.val = list2.val
                    list2 = list2.next
            elif list1:
                current.val = list1.val
                list1 = list1.next
            else:
                current.val = list2.val
                list2 = list2.next

        return head