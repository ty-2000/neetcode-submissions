class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Since chars in s is one of the 26 aphabets chars
        # Keep substring[l:r] such like after performing at most k replacements, it can contain only one distict char
        # Track each char count with the 26-length list
        total = 0
        count = [0] * 26
        l = r = 0
        while r < len(s):
            r += 1
            count[ord(s[r - 1]) - ord('A')] += 1
            # length of the substring must be lower than or equal to max(count) + k
            # Move l such like that
            if max(count) + k < r - l: # while the substring is larger than the possible conditioning substr:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1
            total = max(r - l, total)
        return total