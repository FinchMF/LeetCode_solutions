class ListNode:

    def __init__(self, x):

        self.val = x
        self.next = next

class Solution:

    def swapPairs(self, head: ListNode) -> ListNode:

        if not head or not head.next: return head
        
        first = head.next
        second = head
        second.next = self.swapPairs(first.next)
        first.next = second

        return first


if __name__ == '__main__':

    head = [1,2,3,4]
    Solution().swapPairs(head)


