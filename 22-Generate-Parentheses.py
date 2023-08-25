class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = []
        res = []

        def myFunction(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                myFunction(openN+1, closedN)
                stack.pop()
            
            if closedN < openN:
                stack.append(")")
                myFunction(openN, closedN+1)
                stack.pop()
        
        myFunction(0,0)
        return res
