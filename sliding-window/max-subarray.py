class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_one = max_two = nums[0]
        for i in nums[1:]:
            max_one = max(i, max_one + i)
            max_two = max(max_two, max_one)
        return max_two
            
