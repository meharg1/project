class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        parens = {
            ")" : "(", 
            "]" : "[",
            "}" : "{"
        }
        for i in s:
            if i not in parens:
                lst.append(i)
            else:
                if not lst:
                    return False
                last = lst.pop()
                if last != parens[i]:
                    return False
        return not lst
