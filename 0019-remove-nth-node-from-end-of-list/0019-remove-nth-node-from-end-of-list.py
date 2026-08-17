# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        slow=fast=dummy
        for _ in range(n+1):
            fast=fast.next
        
        while fast!=None:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return dummy.next













        # if head is None:
        #     return head
        # dummy = ListNode(0, head)
        # l=0
        # temp=head
        # while temp is not None:
        #     l+=1
        #     temp=temp.next
    
        # temp = dummy   
        # t = 0
        # while t != (l - n):  
        #     t += 1
        #     temp = temp.next
        # temp.next = temp.next.next
        # return dummy.next  



