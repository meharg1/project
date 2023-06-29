class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mydict = {}
        for i in magazine:
            if i in mydict:
                mydict[i] += 1
            else:
                mydict[i] = 1
        for x in ransomNote:
            if x not in mydict or mydict[x] == 0:
                return False
            mydict[x] -= 1
        return True
