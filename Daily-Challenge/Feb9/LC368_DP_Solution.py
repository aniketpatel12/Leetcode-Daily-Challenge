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
# DP SOLUTION

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[n] for n in nums]
        ans = []

        for i in reversed(range(len(nums))):
            for j in range(i+1, len(nums)):
                if nums[j] % nums[i] == 0:
                    temp = [nums[i]] + dp[j]
                    dp[i] = temp if len(temp) > len(dp[i]) else dp[i]
            ans = dp[i] if len(dp[i]) > len(ans) else ans

        return ans