#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    # @functools.lru_cache(100)
    # def climbStairs(self, n: int) -> int:
    #     if n == 1:
    #         return 1
    #     elif n == 2:
    #         return 2
    #     else:
    #         return self.climbStairs(n-1) + self.climbStairs(n-2)

    # 这都不是第一？38.15%
    # def climbStairs(self, n: int) -> int:
    #     a = [1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765,10946,17711,28657,46368,75025,121393,196418,317811,514229,832040,1346269,2178309,3524578,5702887,9227465,14930352,24157817,39088169,63245986,102334155,165580141,267914296,433494437,701408733,1134903170,1836311903]
    #     return a[n-1]

    # 使用DP
    # 95% 20%
    def climbStairs(self, n: int) -> int:
        hashmap = {}
        hashmap[1], hashmap[2] = 1, 2
        for i in range(3, n + 1):
            hashmap[i] = hashmap[i-1] + hashmap[i-2]
        return hashmap[n]

# @lc code=end

