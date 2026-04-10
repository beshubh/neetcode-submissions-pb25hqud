# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



def reverse_list(head, tail):
    curr = head
    prev = None
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        if curr is tail:
            curr = nxt
            break 
        curr = nxt
    return prev, curr

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = left = head
        count = 0
        result = last_left = None
        while curr:
            count += 1
            if count % k == 0:
                # reverse the group
                t, nxt = reverse_list(left, curr)
                if not result:
                    result = t
                if last_left:
                    last_left.next = t
                last_left = left
                left.next = nxt # join the tail pointer with next set of elements
                left = left.next # move left forward
                curr = nxt
            else:
                curr = curr.next
        return result
        