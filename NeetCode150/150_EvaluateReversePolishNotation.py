# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 150. Evaluate Reverse Polish Notation -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: June - 09 - 2023
# URL: https://leetcode.com/problems/evaluate-reverse-polish-notation/
# ====================================================================

# T - O(n)
# S - O(n)
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif token == "/":
                a = stack.pop()
                b = stack.pop()
                f = b / a
                stack.append(int(float(b)/ float(a)))
            else:
                stack.append(int(token))
        

        return stack[0]

        
