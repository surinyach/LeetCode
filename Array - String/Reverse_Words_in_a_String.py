class Solution:
    def appendWord(self, aux: str, solution: str):
        if aux != "":
            if solution != "":
                solution += " "
            solution += aux
        return solution

    def reverseWords(self, s: str) -> str:
        solution = ""
        aux = ""

        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            if c == " ":
                solution = self.appendWord(aux, solution)
                aux = ""
            elif i == 0:
                aux = c + aux
                solution = self.appendWord(aux, solution)
                aux = ""
            else:
                aux = c + aux

        return solution