class Solution:
    def firstUniqChar(self, s: str) -> str:
        di = {}
        for i in range(0,len(s)):
            if s[i] not in di :
                di[s[i]] = 1
            else:
                di[s[i]] += 1
        for i in range(0,len(s)):
            if di[s[i]]== 1:
                return s[i]
        return ' '