from collections import defaultdict

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        dic = defaultdict(int)
        answer = 0

        for word in words:
            reverse = word[::-1]
            if dic[reverse] > 0:
                answer += 4
                dic[reverse] -= 1
                if dic[reverse] == 0:
                    del dic[reverse]
            else:
                dic[word] += 1

        for word in dic:
            if dic[word] > 0 and word[0] == word[1]:
                answer += 2
                break
        return answer