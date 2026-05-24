class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # We can solve this by deviding into subproblem
        # str1, str2
        # if str1[0] == str2[0]
        #    srt1[0] + longestCommonSubsequence(str1[1:], srr2[1:])
        # else str1[0] != str2[0]
        #    max(
        #        longestCommonSubsequence(str1, srr2[1:]), 
        #        longestCommonSubsequence(str1[1:], str2),
        #    )

        # memo = {}
        # def dfs(i, j) -> int:
        #     res = None
        #     if (i, j) in memo: return memo[(i, j)]
        #     elif i == len(text1) or j == len(text2):
        #         res = 0
        #     elif text1[i] == text2[j]:
        #         res = 1 + dfs(i + 1, j + 1)
        #     else:
        #         res = max(
        #             dfs(i + 1, j),
        #             dfs(i, j + 1)
        #         )
        #     memo[(i, j)] = res
        #     return res
        # return dfs(0, 0)

        # dp
        # dp[i][j]: the length of the longest common subsequence between text[:i] and text[:j]
        # dp[i][j] = 
        #  if text[i] == text[j]: dp[i - 1][j - 1] + 1
        #  else: max(dp[i][j - 1], dp[i - 1][j])

        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[len(text1)][len(text2)]