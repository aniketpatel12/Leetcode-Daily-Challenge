'''
368. Largest Divisible Subset

Given a set of distinct positive integers nums, return the largest subset answer such that 
every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]

'''

# MEMOIZATION SOLUTION (OPTIMIZED)
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        cache = {}

        def dfs(i):
            if i == len(nums): return []
            if i in cache: return cache[i]

            res =  [nums[i]]
            for j in range(i+1, len(nums)):
                if nums[j] % nums[i]==0:
                    temp = [nums[i]] + dfs(j)
                    if len(temp) > len(res): res = temp
            cache[i] = res

            return res

        ans = []
        for i in range(len(nums)):
            temp = dfs(i)
            if len(temp) > len(ans): ans=temp
        
        return ans
       