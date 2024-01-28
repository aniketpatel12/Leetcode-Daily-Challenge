'''
LC-629: K inverse Pairs of Array  

For an integer array nums, an inverse pair is a pair of integers 
[i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].

Given two integers n and k, return the number of different arrays consist 
of numbers from 1 to n such that there are exactly k inverse pairs. 
Since the answer can be huge, return it modulo 10**9 + 7.

'''

# Recursive-Memoization Solution
n = 3
k = 1

M = 10**9 + 7

cache = {}
def count(n, k):
    
    # base case
    if n == 0:
      return 1 if k == 0 else 0
    if k < 0:
      return 0
    if (n,k) in cache:
      return cache[(n,k)]
    
    cache[(n,k)] = 0
  
    # recursive-call 
    for i in range(n):
        cache[(n,k)] = (
          (cache[(n,k)] + count(n-1, k-i)% M) 
        )
      
    return cache[(n,k)]

print(count(n, k))