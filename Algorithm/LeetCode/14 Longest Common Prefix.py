class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ''
        strs.sort(key = lambda x: len(x))
        n = len(strs[0])
        print(n)
        for i in range(n):
            for j in range(1, len(strs)):
                if strs[0][i] != strs[j][i]:
                    return strs[0][:i]
        return strs[0]