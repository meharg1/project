class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num = 0
        while num < len(nums):
            tally = 0
            for i in nums:
                if i == nums[num]:
                    tally +=1
            if tally > 1:
                return True
            num += 1

        return False
