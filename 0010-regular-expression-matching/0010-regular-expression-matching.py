class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        # dp[i][j] represents whether s[0...i-1] matches p[0...j-1]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Empty string and empty pattern match
        dp[0][0] = True
        
        # Patterns like "a*b*c*" can match an empty string
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
                
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # 1. Zero occurrences of the preceding element
                    dp[i][j] = dp[i][j - 2]
                    # 2. One or more occurrences if preceding element matches s[i-1]
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                        
        return dp[m][n]