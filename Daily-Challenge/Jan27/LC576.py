'''
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn].
You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid 
crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball 
out of the grid boundary. Since the answer can be very large, return it modulo 10**9 + 7.
'''
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        M = 1000000000 + 7
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1
        ways = 0

        for moves in range(1, maxMove+1):
            temp = [[0] * n for _ in range(m)]

            for i in range(m):
                for j in range(n):
                    if i == m-1:
                        ways = (ways + dp[i][j]) % M
                    if j == n-1:
                        ways = (ways + dp[i][j]) % M
                    if i == 0: 
                        ways = (ways + dp[i][j]) % M
                    if j == 0:
                        ways = (ways + dp[i][j]) % M
                    
                    temp[i][j] = (
                        ((dp[i-1][j] if i > 0 else 0) + (dp[i+1][j] if i < m-1 else 0)) % M +
                        ((dp[i][j-1] if j > 0 else 0) + (dp[i][j+1] if j < n-1 else 0)) % M
                    ) % M
            dp = temp
        return ways
        


