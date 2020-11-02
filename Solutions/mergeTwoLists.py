
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        if not l1: return l2
        elif not l2: return l1

        if l1.val < l2.val:

            l1.next = self.mergeTwoLists(l1.next, l2)
            
            return l1

        else:

            l2.next = self.mergeTwoLists(l1, l2.next)

            return l2 


if __name__ == '__main__':

    l1, l2 = [1,2,4], [1,3,4]

    Solution().mergeTwoLists(l1, l2)