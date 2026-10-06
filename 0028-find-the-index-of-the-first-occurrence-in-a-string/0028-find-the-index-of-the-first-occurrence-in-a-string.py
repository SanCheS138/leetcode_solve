class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        
        # Iterate through all positions where needle can fit
        for i in range(n - m + 1):
            # Check if the substring matches the needle
            if haystack[i : i + m] == needle:
                return i
                
        return -1
        