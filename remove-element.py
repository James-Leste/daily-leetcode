from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        print(nums)
        print(i)
        return i

li1: List[int] = [0,1,2,2,3,0,4,2]
li2: List[int] = [3,2,2,3]
val1 = 2
val2 = 3


solution: Solution = Solution()
solution.removeElement(li1, val1)
solution.removeElement(li2, val2)

