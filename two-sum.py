from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 1
        numlen = len(nums)
        while i < numlen - 1 and j < numlen:
            sum: int = nums[i] + nums[j]
            if sum == target:
                return [i, j]
            j += 1
            if j == numlen:
                i += 1
                j = i + 1

solution: Solution = Solution()
nums = [2,7,11,15]
target = 9
result = solution.twoSum(nums, target)
print(result)
