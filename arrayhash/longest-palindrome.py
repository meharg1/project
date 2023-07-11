class Solution:
    def longestPalindrome(self, s: str) -> int:
        my_dict = Counter(s)
        answer = 0
        for i in my_dict.values():
            answer += int(i / 2) * 2
            if answer % 2 == 0 and i % 2 == 1:
                answer += 1
        return answer
