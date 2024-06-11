class Solution:
    # Common Interview Question
    # Once start with open parenthesis can add as many open parenthesis after
    # we have to eventually close them
    # as we add closing that matches, then remove them from consideration
    # each time a pair closes we can remove from the list
    # if at end we have an empty list, then can return true
    # alwasy removing from top of stack or list
    # use stack data structure
    # closing parenthesis matches most recent open parenthesis
    # we have to hash map to figure out if closing and open parenthsis match
    # O(n) because we only have to go through every input charafcter once
    # O(n) memeory becasue stack can be up to the size of the input
    # want to make sure stack not empty, can't add closing parenthesis to emtpy stack
    # have to make sure item at top of stack matches the closing parenthesis

    def isValid(self, s: str) -> bool:
        closeToOpen = { ")": "(", "]": "[", "}": "{"}
        stack = []
        for char in s:
            # if get closing parenthesis
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            # case if we get open parenthesis
            # add as many to stack
            else:
                stack.append(char)
        # can only return true if stack is empty
        return True if not stack else False
