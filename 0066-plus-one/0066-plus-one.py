class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # Traverse the digits array from right to left
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        # If all digits were 9, we need an extra digit at the beginning
        return [1] + digits