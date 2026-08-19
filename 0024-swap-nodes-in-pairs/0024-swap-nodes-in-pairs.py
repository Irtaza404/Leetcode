# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None :
            return head
        dummy=ListNode(0,head)
        temp=dummy
        while temp.next!=None and temp.next.next!=None:
            n1=temp.next
            n2=temp.next.next
            n1.next=n2.next
            n2.next=n1
            temp.next=n2
            temp=temp.next.next
        return dummy.next


        