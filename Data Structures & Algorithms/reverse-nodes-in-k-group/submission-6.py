from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f'ListNode: {self.val} -> '


def reverse_list(start, end):
    curr = start
    prev = None
    while curr:
        brk = False
        if curr is end:
            brk = True
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
        if brk:
            break
    # reversed list head, right next
    return prev, curr


"""
Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6
Output: 3 -> 2 -> 1 -> 6 -> 5 -> 4

1 -> 2 -> 3 

3 -> 2 -> 1 -> X     6 -> 5 -> 4 -> X

"""


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr, last_curr = head, None
        result = None
        while curr:
            kth = self.get_kth(curr, k)
            if kth is None:
                if last_curr:
                    last_curr.next = curr
                break
            next = kth.next
            reversed_head, _ = reverse_list(curr, kth)
            if last_curr:
                last_curr.next = reversed_head
            if result is None:
                result = reversed_head
            last_curr = curr
            curr = next
        return result

    def get_kth(self, node: ListNode, k: int):
        while k > 1:  # to get to the kth we need to make k - 1 steps because `node` is part of the space
            if node is None:
                return None
            node = node.next
            k -= 1
        return node


def main():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    curr = head


if __name__ == '__main__':
    main()
