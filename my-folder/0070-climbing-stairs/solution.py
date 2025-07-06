class Solution:
    def climbStairs(self, n: int) -> int:  
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 2

        dp_memo = [0]*(n + 1)
        dp_memo[1] = 1
        dp_memo[2] = 2

        for i in range(3, n + 1):
            dp_memo[i] = dp_memo[i - 1] + dp_memo[i - 2]
        
        print(dp_memo)
        return dp_memo[n]

