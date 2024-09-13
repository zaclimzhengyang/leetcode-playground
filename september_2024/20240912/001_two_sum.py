from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index: List[List[int]] = []
        for index, value in enumerate(nums):
            num_index.append([value, index])
        num_index.sort()

        left: int = 0
        right: int = len(nums) - 1
        while left < right:
            if num_index[left][0] + num_index[right][0] < target:
                left += 1
            elif num_index[left][0] + num_index[right][0] > target:
                right -= 1
            else:
                return [num_index[left][1], num_index[right][1]]

my_solution = Solution()
nums = [3,5,7,3,4]
target = 6
result = my_solution.twoSum(nums, target)
print(result)