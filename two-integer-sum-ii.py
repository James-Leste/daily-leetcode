from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = 1
        numlen = len(numbers)
        while i < numlen-1 and j < numlen:
            sum: int = numbers[i] + numbers[j]
            if sum == target:
                return [i+1, j+1]
            if j != numlen - 1:
                j += 1
            else:
                i += 1
                j = i + 1

    def twoSumEnhanced(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i != j:
            sum: int = numbers[i] + numbers[j]
            if sum > target:
                j -= 1
            elif sum < target:
                i += 1
            else:
                return [i + 1 , j + 1]



solution: Solution = Solution()
numbers = [-5,-3,0,2,4,6,8]
target = 5
arr = solution.twoSum(numbers, target)
print(arr)

