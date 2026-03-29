class Solution:
    def partitionString(self, s: str) -> int:
        substrings = 0
        visited = []

        for r in range(0, len(s)):
            if s[r] in visited:
                substrings += 1
                visited = []
            
            visited.append(s[r])
        
        if (bool(visited)): substrings += 1
        
        return substrings