from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        current_indices = []
        for i in range(0, len(nums)):
            current_indices.append(i)
        return current_indices


indices_1 = Solution()
x = [2, 7, 15, 10]
print(indices_1.twoSum(x, 9))