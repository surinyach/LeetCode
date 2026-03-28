class Solution:
    def partitionString(self, s: str) -> int:
        substrings = 0
        visited = set()

        for r in range(0, len(s)):
            if s[r] in visited:
                substrings += 1
                visited.clear()
            
            visited.add(s[r])
        
        if (bool(visited)): substrings += 1
        
        return substrings