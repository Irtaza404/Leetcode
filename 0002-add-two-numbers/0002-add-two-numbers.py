# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ghost=ListNode()
        temp=ghost
        carry=0
        while l1 is not  None or l2 is not None:
            v1= 0 if l1 is None else l1.val
            v2= 0 if l2 is None else l2.val
            add=v1+v2+carry
            carry=add//10
            temp.next=ListNode(add%10)
            temp=temp.next
            if l1 is not None :
                l1=l1.next
            if l2 is not None :
                l2=l2.next
        if carry != 0:
            temp.next=ListNode(carry)
        return ghost.next

