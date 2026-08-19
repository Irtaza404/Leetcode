# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l3=ListNode()
        temp=l3
        while list1 is not None or list2 is not None:
            v1= list1.val if list1!=None else 200
            v2= list2.val if list2!=None else 200
            minv=min(v1,v2)
            if minv==v1:
                node=list1
                list1=list1.next
            else:
                node=list2
                list2=list2.next
            node.next=None
            temp.next=node
            temp=temp.next
        return l3.next