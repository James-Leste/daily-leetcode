class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        s = s.lower()
        while i <= j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            print(f'i: {s[i]} | j: {s[j]}')
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

solution: Solution = Solution()
result: bool = solution.isPalindrome("Madam, in Eden, I'm Adam")
print(result)

