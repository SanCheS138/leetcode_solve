class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = [abs(x) for x in nums]
        nums.sort()
        n = len(nums)
        low, high = 0, n - 1
        sol = 0
        
        while low < high:
            sol += nums[high] ** 2 - nums[low] ** 2
            low += 1
            high -= 1
            
        if low == high:
            sol += nums[low] ** 2
            
        return sol