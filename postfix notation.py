import math
import operator
ops = {'+':operator.add,
       '-':operator.sub,
       '*':operator.mul,
       '/':operator.truediv,
       '^':operator.pow,
       'sin':math.sin,
       'tan':math.tan,
       'cos':math.cos,
       'pi':math.pi}

postfix = []
temp = []
operator = -10
operand = -20
leftparentheses = -30
rightparentheses = -40
empty = -50


def precedence(s):
    if s is '(':
        return 0
    elif s is '+' or s is '-':
        return 1
    elif s is '*' or s is '/' or s is '%':
        return 2
    else:
        return 99


def typeof(s):
    if s is '(':
        return leftparentheses
    elif s is ')':
        return rightparentheses
    elif s is '+' or s is '-' or s is '*' or s is '%' or s is '/':
        return operator
    elif s is ' ':
        return empty
    else:
        return operand

def convert (self, l):
        l.reverse ()
        for e in l:
            self.push (e)
        return self.stack.pop ()

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

def calculate(equation):
    stack = []
    result = 0
    for i in equation:
        if is_number(i):
            stack.insert(0,i)
        else:
            if len(stack) < 2:
                print ('Error: insufficient values in expression')
                break
            else:
                print ('stack: %s' % stack)
                if len(i) == 1:
                    n1 = float(stack.pop(1))
                    n2 = float(stack.pop(0))
                    result = ops[i](n1,n2)
                    stack.insert(0,str(result))
                else:
                    n1 = float(stack.pop(0))
                    result = ops[i](math.radians(n1))
                    stack.insert(0,str(result))
    return result

def main():
    running = True
    while running:
        equation = input("Enter the infix notation : ")
        for i in equation:
            type = typeof(i)
            if type is leftparentheses:
                temp.append(i)
            elif type is rightparentheses:
                next = temp.pop()
                while next is not '(':
                    postfix.append(next)
                    next = temp.pop()
            elif type is operand:
                postfix.append(i)
            elif type is operator:
                p = precedence(i)
                while len(temp) is not 0 and p <= precedence(temp[-1]):
                    postfix.append(temp.pop())
                temp.append(i)
            elif type is empty:
                continue
        while len(temp) > 0:
            postfix.append(temp.pop())
        print("Postfix notation : ")
        print("".join(postfix))
        answer = calculate(postfix)
        print ('RESULT: %f' % answer)
        again = input('\nEnter another? ')[0].upper()
        if again != 'Y':
            running = False

if __name__ == '__main__':
    main()