class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0 
        end = len(s) - 1
        while start < end:
            #s[start] =  , s[end] = a
            print(s[start], s[end])
            if not(97 <= ord(s[start].lower()) <= 122 or 48 <= ord(s[start].lower()) <= 57):
                start += 1
            elif not(97 <= ord(s[end].lower()) <= 122 or 48 <= ord(s[end].lower()) <= 57):
                end -= 1
            elif s[start].lower() != s[end].lower():
                return False
            else:
                start, end = start + 1, end - 1
        return True
