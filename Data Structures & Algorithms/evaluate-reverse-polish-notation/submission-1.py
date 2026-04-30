class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+","-","*","/"]
        operands = []
        for i in tokens:
            if i in operators:
                op1 = operands.pop()
                op2 = operands.pop()
                if i == "+":
                    result = op2 + op1
                elif i == "-":
                    result = op2 - op1
                elif i == "*":
                    result = op2 * op1
                elif i == "/":
                    result = int(op2/op1)
                operands.append(result)
            else:
                operands.append(int(i))
        return operands.pop()