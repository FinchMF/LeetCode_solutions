class ListNode:

    def __init__(self, x):

        self.val = x
        self.next = next

class Solution: 

    def reverseKGroup(self, head, k):

        dum = last = ListNode(0)
        cur = head

        while cur:

            first, cnt = cur, 1
            while cnt < k and cur:

                cur, cnt = cur.next, cnt + 1

            if cnt == k and cur:
                cur, prev = first, None

                for _ in range(k):

                    prev, cur.next, cur = cur, prev, cur.next
                last.next, last = prev, first

            else:

                last.next = first

        return dum.next


if __name__ == '__main__':

    head, k = [1,2,3,4,5], 2
    Solution().reverseKGroup(head, k)

    head, k = [1,2,3,4,5], 3
    Solution().reverseKGroup(head, k)


