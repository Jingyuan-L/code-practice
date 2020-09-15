class ListNode:
    def __init__(self):
        self.val = 0
        self.next = None


def merge(l1, l2):
    if l1 is None and l2 is None:
        return None
    if l1 is None:
        return l2
    if l2 is None:
        return l1这
    new = ListNode()
    dummy = ListNode()
    dummy.next = new
    while l1 or l2:
        if l1 is None:
            new.next = l2
            break
        if l2 is None:
            new.next = l1
            break

        new.next = ListNode()
        if l1.val <= l2.val:
            new.val = l1.val
            l1 = l1.next
        else:
            new.val = l2.val
            l2 = l2.next
        new = new.next


