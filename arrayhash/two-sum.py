class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #for i in range(len(nums)):
         #   for x in range(i+1, len(nums)):
          #      if i != x and nums[i] + nums[x] == target:
           #         return [i, x]
        #hash = set()
        #for i in range(len(nums)):
         #   if target - nums[i] in hash:
          #      return [i, nums.index(target-nums[i])]
           # else:
            #    hash.add(nums[i])
        hashdict = {}
        for i in range(len(nums)):
            if target - nums[i] in hashdict:
                return [i, hashdict[target - nums[i]]]
            else:
                hashdict[nums[i]] = i
