class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Maps a character to its last seen index
        char_map = {}
        left = 0
        max_len = 0
        
        for right, char in enumerate(s):
            # If the character is already in the window, move the left pointer
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
                
            # Update the last seen position of the character
            char_map[char] = right
            
            # Calculate the current window size and update max_len
            max_len = max(max_len, right - left + 1)
            
        return max_len
