from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # for i in range(len(s2)-len(s1)+1):
        #     if Counter(s1) == Counter(s2[i:i+len(s1)]):
        #         return True
        l1 = list(map(lambda x: ord(x) - ord('a'), s1))
        l2 = list(map(lambda x: ord(x) - ord('a'), s2))

        target = [0] * 26
        for x in l1:
            target[x] += 1

        window = [0] * 26
        
        for i, x in enumerate(l2):
            window[x] += 1
                    
            if i >= len(l1):
                window[l2[i - len(l1)]] -= 1
                
            if target == window:
                return True
            
        return False