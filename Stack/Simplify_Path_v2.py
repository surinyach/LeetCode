from collections import deque

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        clean_path = deque()
        section = ""

        for c in path + "/":
            if c == "/":
                if section == "..":
                    if clean_path: clean_path.pop()
                elif section != "." and section != "":
                    clean_path.append("/" + section)
                section = ""
            else:
                section += c
       
        return "".join(clean_path) if clean_path else "/"
    
    # Time Complexity: O(n) -> Where n are the number of characters in path
    
    # Space Complexity = O(k) -> Where k are the number of characters in the clean path
    # Since all the characters of the clean path will be inserted on the array