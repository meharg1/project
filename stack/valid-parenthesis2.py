class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                lst.append(i)
            else:
                if not lst:
                    return False
                last = lst.pop()
                if (last == '(' and i != ')') or (last == '{' and i != '}') or (last == '[' and i != ']'):
                    return False
        return not lst
