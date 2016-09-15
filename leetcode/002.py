class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        i = 0
        root = ListNode(None)
        c = root
        while l1 or l2:
            if l1:
                i += l1.val
                l1 = l1.next
            if l2:
                i += l2.val
                l2 = l2.next
            c.next = ListNode(i % 10)
            i /= 10
            c = c.next
        while i:
            c.next = ListNode(i % 10)
            i /= 10
        return root.next


def test():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    r = Solution().addTwoNumbers(l1, l2)
    assert r.val == 7
    assert r.next.val == 0
    assert r.next.next.val == 8


if __name__ == '__main__':
    test()
