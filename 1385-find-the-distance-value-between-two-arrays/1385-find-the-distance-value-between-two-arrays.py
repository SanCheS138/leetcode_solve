class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        distance_value = 0
        
        for x in arr1:
            # Use binary search to find the insertion point for x in sorted arr2
            import bisect
            idx = bisect.bisect_left(arr2, x)
            
            # Check the closest elements in arr2 (to the left and right of x)
            valid = True
            if idx < len(arr2) and abs(arr2[idx] - x) <= d:
                valid = False
            if idx > 0 and abs(arr2[idx - 1] - x) <= d:
                valid = False
                
            if valid:
                distance_value += 1
                
        return distance_value