class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """ The Brute force method would check each number with every other number in the 
        array. This would result in time complexity of o(n^2) because n is the size fo array. No extra 
        memory so memory complexity is o(1). Can we do better? yes."""
        """ we can sort, this will make all the duplicates adjacent. Then shift pointers.
        all the way till end. One pass will take o(n), but sorting takes extra time complexity.
        so the time complexity will be o(nlogn). The space complexity is still o(1)."""
        """if we use some more memory, we can get better time complexity."""
        hashset = set()
        # Allows us to insert elements in o(1) time.
        # Can ask if set contain the value
        # we don't have to check every other element in the array.
        # Each operation was o(1) and did that for every element, so time complexity is o(n)
        # did sacrifice some space, for hashset the memeory can be up to size of the array, so it is o(n)
        for n in nums:
            if n in hashset:
                return True
            else:
                hashset.add(n)
        return False


         
