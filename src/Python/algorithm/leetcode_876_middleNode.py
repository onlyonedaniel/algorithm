from .utils import ListNode


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        mid = 0
        len_ = 1
        temp = head
        while temp.next:
            temp = temp.next
            len_ += 1
        mid = int(len_ / 2)
        index = 0
        while index != mid:
            head = head.next
            index += 1

        return head
