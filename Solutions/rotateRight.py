
class ListNode:

    def __init__(self, val=0, next = None):

        self.val = val
        self.next = next

    def __repr__(self):

        if self:
        
            return f"{self.val} -> {self.next}"

class Solution:

    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        if not head or not head.next:
            return head

        n, cur = 1, head
        while cur.next:

            cur = cur.next
            n +=1

        cur.next = head

        cur, tail = head, cur

        for _ in range(n - k % n):

            tail = cur
            cur = cur.next

        tail.next = None

        return cur



if __name__ == '__main__':

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print(head)
    print(Solution().rotateRight(head, 2))