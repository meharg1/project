class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            pointer = (left + right) // 2
            if target == nums[pointer]:
                return pointer
            elif target > nums[pointer]:
                left = pointer + 1
            else:
                right = pointer - 1
        return -1
