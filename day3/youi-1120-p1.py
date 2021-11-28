class Solution:
    def replaceSpace(self, s: str) -> str:
        while s.find(' ') is not -1:
            i = s.find(' ')
            s = s[:i]+"%20"+s[i+1:]
        return s