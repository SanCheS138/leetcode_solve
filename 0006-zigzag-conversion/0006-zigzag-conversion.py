class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
      
        # Initialize a list of empty lists, one for each row
        rows = [[] for _ in range(numRows)]
      
        # current_row: tracks which row we're currently adding to
        # direction: determines if we're moving down (1) or up (-1) in the zigzag
        current_row = 0
        direction = -1
      
        # Iterate through each character in the string
        for char in s:
            # Add current character to the appropriate row
            rows[current_row].append(char)
          
            # Change direction when we reach the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                direction = -direction
          
            # Move to the next row based on current direction
            current_row += direction
      
        # Concatenate all rows together to form the final string
        # Using list comprehension to join each row, then join all rows
        return ''.join(''.join(row) for row in rows)
        