class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash = set()
        
        for num in nums:
            if num in hash:
                return True
            
            hash.add(num)
