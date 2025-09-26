class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            else:
                if not stack: return False  
                top = stack.pop()
                if top == "(" and char != ")": return False
                elif top == "[" and char != "]": return False
                elif top == "{" and char != "}": return False
        
        if stack: return False
        else: return True