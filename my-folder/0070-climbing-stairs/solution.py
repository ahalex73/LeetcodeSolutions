class Solution:
    def climbStairs(self, n: int) -> int:  
        # Dynamic programming solution - Bottom up tabulation
        # Time: O(n)
        # Space: O(n)
        
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 2

        # UNOPTIMAL SPACE COMPLEXITY considering we know we only have two subproblems possible
        # dp = [0]*(n + 1) # Stores solutions to sub-problems in dynamic programming
        # dp[1] = 1
        # dp[2] = 2

        # for i in range(3, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]

        # return dp[n]

        # OPTIMAL SPACE COMPLEXITY #
        # would result when we just realize we already know the answers to the subproblems in this case
        # n == 0, n == 1, and n == 2 wouldn't need to be stored in a table, they can just be two variables
        first = 1   # dp[i - 2]
        second = 2  # dp[i - 1]

        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third

        return second
        


