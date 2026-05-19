class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Represent permutation of s1 with a 26 length list
        # Sliding window method

        if len(s1) > len(s2): return False

        # target permutation rep
        target = [0] * 26
        for c in s1:
            target[ord(c) - ord('a')] += 1

        # current permutation
        cur = [0] * 26
        l, r = 0, len(s1)
        for c in s2[l:r]:
            cur[ord(c) - ord('a')] +=1 
        if cur == target: return True
        while r < len(s2):
            cur[ord(s2[l]) - ord('a')] -= 1
            cur[ord(s2[r]) - ord('a')] += 1
            l += 1
            r += 1
            if target == cur:
                return True
        return False