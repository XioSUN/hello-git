#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 29 17
        # cur, prev = head, None
        # while cur != None:
        #     temp = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = temp
        # head = prev
        # return head

        # 90 17
        # cur, prev = head, None
        # while cur != None:
        #     cur.next, cur, prev = prev, cur.next, cur
        # head = prev
        # return head

        # 54% 20%
        # array, cur = [], head
        # while cur != None:
        #     array.append(cur.val)
        #     cur = cur.next
        # cur = head
        # while cur != None:
        #     cur.val = array.pop()
        #     cur = cur.next
        # return head

        # if head is None or head.next is None: # 处理特例，若空或仅一个元素，直接返回头索引。
        #     return head
        # newhead = self.reverseList(head.next)
        # head.next.next = head  # 指向队列头
        # head.next = None
        # return newhead
        return self._reverse(head)

    def _reverse(self, node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self._reverse(n, node)

# @lc code=end

