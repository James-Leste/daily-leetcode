class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ssort = sorted(s)
        tsort = sorted(t)

        for i in range(0, len(s)):
            if ssort[i] == tsort[i]:
                continue
            else:
                return False
        return True
