class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window method
        # Initialize l, r as zero, Keep s[l:r] has no duplicate chars
        # Use hash map to map from the char inside the substring to the index of the char inside the substring
        # Increament r by one for each iteration. If the substring already has s[r] char, update l to the next index of the existing char
        total_length = 0
        hash_map = {}
        l = r = 0
        while r < len(s):
            r += 1
            if hash_map.get(s[r - 1], -1) >= l:
                l = hash_map[s[r - 1]] + 1
            hash_map[s[r - 1]] = r - 1
            total_length = max(r - l, total_length)
        return total_length