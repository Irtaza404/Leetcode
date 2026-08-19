class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevTail = dummy   # tail of the last correctly-linked group
        temp = head
        
        while temp:
            # check if there are at least k nodes left
            fast = temp
            for _ in range(k):
                if not fast:
                    return dummy.next
                fast = fast.next
            
            # reverse this group [temp ... fast)
            curr = temp
            prev = None
            while curr != fast:
                nextnode = curr.next
                curr.next = prev
                prev = curr
                curr = nextnode
            
            # prevTail was pointing at 'temp' (old head) — now link it to 'prev' (new head)
            prevTail.next = prev
            # 'temp' is now the tail of this reversed group — link it forward to next segment
            temp.next = fast
            
            # advance: this group's old head becomes the new prevTail
            prevTail = temp
            temp = fast
        
        return dummy.next