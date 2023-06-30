class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict = {}
        for i in s:
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1
        dict_two = {}       
        for i in t:
            if i in dict_two:
                dict_two[i] += 1
            else:
                dict_two[i] = 1
        return my_dict == dict_two
