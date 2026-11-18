class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # 1. Find the rightmost index i where nums[i] < nums[i + 1]
        pivot = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break

        # If no such pivot exists, nums is in descending order; reverse to smallest
        if pivot == -1:
            nums.reverse()
            return

        # 2. Find the rightmost element greater than nums[pivot] to swap with
        for j in range(n - 1, pivot, -1):
            if nums[j] > nums[pivot]:
                nums[pivot], nums[j] = nums[j], nums[pivot]
                break

        # 3. Reverse the suffix after pivot so it becomes ascending (smallest possible)
        left, right = pivot + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1