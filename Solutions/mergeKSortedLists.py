class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def mergeKLists(self, lists):

        qeue = [] 

        for idx in range(len(lists)):

            while lists[idx]:

                qeue += lists[idx],
                lists[idx] = lists[idx].next

        root = cur = ListNode(0)

        for i in sorted(qeue, key=lambda x: x.val):

            cur.next = cur = i

        return root.next


if __name__ == '__main__':

    lists = [[1,4,5],[1,3,4],[2,6]]
    Solution().mergeKLists(lists)

