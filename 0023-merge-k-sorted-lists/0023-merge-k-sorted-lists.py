# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        for i,Node in enumerate(lists):
            if Node:
                heapq.heappush(heap,(Node.val,i,Node))
        dummy=ListNode()
        temp=dummy
        while heap:
            value,i,Node=heapq.heappop(heap)
            temp.next=Node
            temp=temp.next
            if Node.next:
                heapq.heappush(heap,(Node.next.val,i,Node.next))
        return dummy.next