class Solution:
    def countAndSay(self, n: int) -> str:
         # Initialize with the first term of the sequence
        current_term = '1'
      
        # Generate each subsequent term up to the nth term
        for _ in range(n - 1):
            # Index to traverse the current term
            index = 0
            # List to build the next term
            next_term_parts = []
          
            # Process all characters in the current term
            while index < len(current_term):
                # Find the end of the current run of identical digits
                run_end = index
                while run_end < len(current_term) and current_term[run_end] == current_term[index]:
                    run_end += 1
              
                # Count of consecutive identical digits
                count = run_end - index
                # The digit being counted
                digit = current_term[index]
              
                # Append count and digit to build the next term
                next_term_parts.append(str(count))
                next_term_parts.append(digit)
              
                # Move to the next different digit
                index = run_end
          
            # Join all parts to form the next term
            current_term = ''.join(next_term_parts)
      
        return current_term

        