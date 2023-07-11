class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1
        while n > 1:
            one, two = one + two, one
            n -= 1
        return one
