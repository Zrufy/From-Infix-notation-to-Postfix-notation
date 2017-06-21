def set_tokenPrec(token):
    # If the token is * or / then precedence value of 3
    if token == "*" or token == "/":
        return float(3)
    # If the token is + or - then precedence value of 2
    elif token == "+" or token == "-":
        return float(2)
    # If the token is ( or ) then the precedence value of 1
    elif token == "(" or token == ")":
        return float(1)

def infixExpressionConvert(infixExpr):
    # Create empty stack called opstack for the operators
    opstack = []
    # Create empty list for output
    outList = []
    # Convert the infix string to a list by using the string method split
    tokens = infixExpr.split()
    # Scan the token list left to right
    for token in tokens:
    # If the token is an operand: append it to the end of the output list
        if token.isdigit() or token.isalpha():
            outList.append(token)
    # If the token is (: push it on the opstack
        elif token == '(':
            opstack.append(token)
    # If the token is ): pop the opstack until matching ( is removed
    #   and append each operator to the end of the output list
        elif token == ')':
            specialtoken = opstack.pop()
            while specialtoken != '(':
                outList.append(specialtoken)
                specialtoken = opstack.pop()
    # If the token is an operator * / + - push it on the opstack
    #   but first remove any operators already on the opstack that have
    #   higher or equal precedence and append them to the output list
        else:
            while (len(opstack) != 0 ) and ( (set_tokenPrec(opstack[0])) >= (set_tokenPrec(token)) ):
                outList.append(opstack.pop())
            opstack.append(token)
    # when input expression completely traversed, check opStack
    #   if any operators still on stack, remove them and append to end
    #   of output list
    while len(opstack) != 0:
        outList.append(opstack.pop())
    # returns result as a string
    return " ".join(outList)


def postfix_evaluation(s):
    s = s.split()
    n = len(s)
    stack = []
    for i in range(n):
        if s[i].isdigit():
            # append function is equivalent to push
            stack.append(float(s[i]))
        elif s[i] == "+":
            a = stack.pop()
            b = stack.pop()
            stack.append(float(a) + float(b))
        elif s[i] == "*":
            a = stack.pop()
            b = stack.pop()
            stack.append(float(a) * float(b))
        elif s[i] == "/":
            a = stack.pop()
            b = stack.pop()
            stack.append(float(b) / float(a))
        elif s[i] == "-":
            a = stack.pop()
            b = stack.pop()
            stack.append(float(b) - float(a))
    return stack.pop()

s = "20 * 30"
c = infixExpressionConvert(s)
print("Infix : "+c)
val = postfix_evaluation(c)
print("Result :" + str(val))
