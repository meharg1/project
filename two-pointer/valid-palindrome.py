class Solution:
    def isPalindrome(self, s: str) -> bool:
        pointer_one = 0
        pointer_two = len(s) - 1
        string = s.lower()
        while pointer_one < pointer_two:
            if not(97 <= ord(string[pointer_one]) <= 122 or 48 <= ord(string[pointer_one]) <= 57):
                pointer_one += 1
            elif not(97 <= ord(string[pointer_two]) <= 122 or 48 <= ord(string[pointer_two]) <= 57):
                pointer_two -= 1
            elif string[pointer_one] != string[pointer_two]:
                return False
            else:
                pointer_one += 1
                pointer_two -= 1
        return True

# O(n) time complexity
# O(1) memory
# ord gives ascii value of character
# have to greater than or equal to and less than or equal to becasue of the not
# two pointers strategy
# lower() to make it lowercase
