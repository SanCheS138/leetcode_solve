class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        
        # Sorting helps prune the search tree early
        candidates.sort()
        
        def backtrack(remain: int, combo: list[int], start: int):
            # Base case: if remaining target is exactly 0, we found a valid combination
            if remain == 0:
                result.append(list(combo))
                return
            
            for i in range(start, len(candidates)):
                # Pruning: if the current candidate is larger than the remainder, 
                # no subsequent candidates will work either because the array is sorted.
                if candidates[i] > remain:
                    break
                
                # Make a choice
                combo.append(candidates[i])
                
                # Explore further (we pass 'i' as the start index instead of 'i + 1' 
                # because we can reuse the same element multiple times)
                backtrack(remain - candidates[i], combo, i)
                
                # Undo choice (backtrack)
                combo.pop()
        
        backtrack(target, [], 0)
        return result
        