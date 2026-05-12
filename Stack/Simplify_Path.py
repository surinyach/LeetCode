from collections import deque

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        clean_path = []

        for i in range(0, len(path)):
            c = path[i]
            if c == "/":
                i += 1
                section = "/"
                while i < len(path) and path[i] != "/":
                    section += path[i]
                    i += 1
    
                if section == "/..":
                    if len(clean_path) > 0: clean_path.pop()
                elif section != "/." and section != "/":
                    clean_path.append(section)
                    
        return "".join(clean_path) if len(clean_path) > 0 else "/"
    
    # Time Complexity: O(n) -> Where n are the number of characters in path
    # Internal loop does not make it exponential since adds the iteration variable of the outter loop and nevers goes back
    
    # Space Complexity = O(k) -> Where k are the number of characters in the clean path
    # Since all the characters of the clean path will be inserted on the array