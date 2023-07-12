class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        canidate = 0
        for i in nums:
            if count == 0:
                canidate = i

            if i == canidate:
                count += 1
            else:
                count -=1
        return canidate
