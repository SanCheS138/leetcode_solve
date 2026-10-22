class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        
        def backtrack(current_string, open_count, close_count):
            # Base case: if the string length is 2 * n, we have a valid combination
            if len(current_string) == 2 * n:
                res.append(current_string)
                return
            
            # We can add an opening parenthesis if we haven't used all n of them
            if open_count < n:
                backtrack(current_string + "(", open_count + 1, close_count)
                
            # We can add a closing parenthesis if it won't exceed the number of open parentheses
            if close_count < open_count:
                backtrack(current_string + ")", open_count, close_count + 1)
                
        backtrack("", 0, 0)
        return res
        