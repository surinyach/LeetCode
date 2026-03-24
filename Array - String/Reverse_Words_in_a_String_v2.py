class Solution:
    # String split() method:
    #   Split the string into a list where each word is a list item

    # String join() method:
    #   Join all items of a list into a string, using a given character as separator

    # Python String slicing syntax:
    #   Structure of [start:stop:step]
    #   This: words[len(words)-1:0:-1] would give you everything backwards except the element in [0]
    
    def reverseWords(self, s: str) -> str:
        words = s.split()
        return " ".join(words[::-1])