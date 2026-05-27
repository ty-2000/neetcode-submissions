class Solution:
    def longestPalindrome(self, s: str) -> str:
        # the longest palindrome s[i] ... s[j] is
        # if s[i] == s[j] and s[i + 1]...s[j - 1] is palindrome -> s[i] ... s[j] itself
        # Otherwises either s[i] ... s[j - 1] or s[i + 1] ... s[j]
        # Using this method, implement Dynamic Programming

        l = len(s)
        dp = [[0] * l for _ in range(l)]
        is_palindrome = [[False] * l for _ in range(l)]

        longest = [0, 0]
        for i in range(l):
            dp[i][i] = 1 # A single char is always one palindrome
            is_palindrome[i][i] = True
        
        # (0, 1), (1, 2) ..., (0, 2), ..., ...., (0, l - 1)
        for size in range(1, l):
            for i in range(l - size):
                j = i + size
                if s[i] == s[j] and size == 1:
                    is_palindrome[i][j] = True
                    dp[i][j] = 2
                    longest = [i, j]
                elif s[i] == s[j] and is_palindrome[i + 1][j - 1]:
                    is_palindrome[i][j] = True
                    dp[i][j] = dp[i + 1][j - 1] + 2
                    if j - i > longest[1] - longest[0]:
                        longest = [i, j]

        return s[longest[0]:longest[1] + 1]