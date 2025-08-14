MOD = 1_000_000_007

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        # n = target number
        # x = power number
        # Time: O(m * n)
        # Space: O(n)

        # Return the number of ways n can be expressed as the sum of the x-th power of unique positive integers.
        # In other words, the number of sets of unique integers[n1, n2, ..., nk] where n = n1^x + n2^x + ... nK^x
        # since the result can be really large, return modulo 10^9 + 7

        # precomputer powers
        powers = []
        i = 1
        while True:
            p = pow(i, x)
            if p > n:
                break
            powers.append(p)
            i += 1
        
        dp = [0] * (n + 1)
        dp[0] = 1
        for p in powers:
            for s in range(n, p - 1, -1):
                dp[s] = (dp[s] + dp[s - p]) % MOD

        return dp[n]
