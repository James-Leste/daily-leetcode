from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        numlen: int = len(nums)
        relist: list[list[int]] = []

        for p in range(0, numlen-1):
            i = p + 1
            j = numlen - 1

            if p != 0 and nums[p - 1] == nums[p]:
                continue
            prei: int | None = None
            prej: int | None = None
            while i < j:
                sum: int = nums[i] + nums[j] + nums[p]
                if sum < 0:
                    prei = nums[i]
                    i += 1
                    continue
                elif sum > 0:
                    prej = nums[j]
                    j -= 1
                    continue
                else:
                    if prei == nums[i]:
                        prei = nums[i]
                        i += 1
                        continue
                    if prej == nums[j]:
                        prej = nums[j]
                        j -= 1
                        continue
                    relist.append([nums[i], nums[j], nums[p]])
                    prei = nums[i]
                    prej = nums[j]
                    i += 1
                    j -= 1
        return relist

solution: Solution = Solution()
nums=[-1,0,1,2,-1,-4]

result: List[List[int]] = solution.threeSum(nums)
print(result)
