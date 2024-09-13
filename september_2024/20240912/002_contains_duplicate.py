from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for i in range(len(nums)):
            nums_set.add(nums[i])
        return len(nums_set) != len(nums)


my_solution = Solution()
result = my_solution.containsDuplicate([1,1,1,2,2,3])
print(result)