'''
LC-629: K inverse Pairs of Array  

For an integer array nums, an inverse pair is a pair of integers 
[i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].

Given two integers n and k, return the number of different arrays consist 
of numbers from 1 to n such that there are exactly k inverse pairs. 
Since the answer can be huge, return it modulo 10**9 + 7.

'''

# DP Solution with Sliding window approach
n = 3
k = 1


MOD = 10**9 + 7

prev = [0] * (k+1)
prev[0] = 1

for N in range(1, n+1):
    cur = [0] * (k+1)
    total = 0
    for K in range(0, k+1):
        if K >= N:
            total -= prev[K-N]   
        total = (total + prev[K])%MOD
        cur[K] = total

    prev=cur

print(prev[k])