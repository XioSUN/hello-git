# test on the single-linked list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def swapPairs(head):
    # 迭代（遍历）
    cur = head
    while cur and cur.next:
        cur, cur.next, cur.next.next = cur.next, cur.next.next, cur
        cur = cur.next.next
    return head

