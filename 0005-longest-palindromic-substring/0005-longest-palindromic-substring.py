class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start, max_len = 0, 0

        def expand_around_center(left: int, right: int) -> tuple[int, int]:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        for i in range(len(s)):
            l1, r1 = expand_around_center(i, i)
            if r1 - l1 + 1 > max_len:
                start, max_len = l1, r1 - l1 + 1

            
            l2, r2 = expand_around_center(i, i + 1)
            if r2 - l2 + 1 > max_len:
                start, max_len = l2, r2 - l2 + 1

        return s[start : start + max_len]