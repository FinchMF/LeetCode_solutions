# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        dum = ListNode(0)
        dum.next = head
        arr = [dum]

        while head:

            arr.append(head)
            head = head.next

        for _ in range(n + 1):

            pre = arr.pop()
        pre.next = pre.next.next

        return dum.next


if __name__ == '__main__':

    head, n = [1,2,3,4,5], 2

    Solution().removeNthFromEnd(head, n)
        