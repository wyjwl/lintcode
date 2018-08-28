# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    result = ListNode(0)
    p = l1
    q = l2
    curr = result
    carry = 0
    while p is not None or q is not None:
        x = p.val if p is not None else 0
        y = q.val if q is not None else 0
        sum = x + y + carry
        carry = int(sum/10)
        curr.next = ListNode(sum % 10)
        curr = curr.next
        p = p.next if p is not None else p
        q = q.next if q is not None else q

    if carry > 0:
        curr.next = ListNode(carry)

    return result.next


