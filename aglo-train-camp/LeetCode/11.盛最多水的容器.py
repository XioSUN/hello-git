#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    # @functools.lru_cache(100)
    def maxArea(self, height: List[int]) -> int:
        maxA = 0
        for i, m in enumerate(height):
            for j, n in enumerate(height[i+1:]):
                if maxA < min(m, n) * (j+1):
                    maxA = min(n, m) * (j+1)
        return maxA
# @lc code=end

