#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if not nums or n < 3:   return []
        nums.sort() # in-place operation
        ans = []
        for i in range(n - 2):
            if nums[i] > 0:   return ans
            else:
                j, k = i+1, len(nums)-1
                while j < k:
                    if nums[j] + nums[k] + nums[i] == 0:
                        ans.append([nums[i], nums[j], nums[k]])
                        k-=1
                        while j<k and nums[k] == nums[k-1]: k-=1
                        j+=1
                        while j<k and nums[j] == nums[j+1]: j+=1
                    elif nums[j] + nums[k] + nums[i] > 0:
                        k-=1
                        while j<k and nums[k] == nums[k+1]: k-=1
                    else:
                        j+=1
                        while j<k and nums[j] == nums[j-1]: j+=1
        return ans


# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         n=len(nums)
#         res=[]
#         if(not nums or n<3):
#             return []
#         nums.sort()
#         res=[]
#         for i in range(n):
#             if(nums[i]>0):
#                 return res
#             if(i>0 and nums[i]==nums[i-1]):
#                 continue
#             L=i+1
#             R=n-1
#             while(L<R):
#                 if(nums[i]+nums[L]+nums[R]==0):
#                     res.append([nums[i],nums[L],nums[R]])
#                     while(L<R and nums[L]==nums[L+1]):
#                         L=L+1
#                     while(L<R and nums[R]==nums[R-1]):
#                         R=R-1
#                     L=L+1
#                     R=R-1
#                 elif(nums[i]+nums[L]+nums[R]>0):
#                     R=R-1
#                 else:
#                     L=L+1
#         return res

# @lc code=end

