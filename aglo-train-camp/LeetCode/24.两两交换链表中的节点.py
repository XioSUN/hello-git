#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
    #     self._change2ele(head)
    #     return head

    # def _change2ele(self, cur):
    #     if not cur: return cur
    #     if not cur.next:    return cur.next
    #     cur.next, cur = cur, cur.next
    #     return self._change2ele(cur.next.next)

        # 迭代（遍历）
        cur = head
        while cur and cur.next:
            temp = cur.next.next
            cur, cur.next, cur.next.next = cur.next, cur.next.next, cur
            cur = temp
        return head
# @lc code=end

