def kata_1(seq):
    result = read_rpn(seq.split(' '))
    return result

def kata_input():
    seq = input("input your RPN code here: ")
    seq = seq.split(' ')
    kata_1(seq)

def read_rpn(seq):
    stack = []
    for i in seq:
        print("i = " + i)
        try:
            stack.append(int(i))
        except:
            if (i == "+") or (i == "-") or (i == "*") or (i == "/"):
                stack = basic_op(stack, i)
    return stack[0]

            
def basic_op(stack, op):
    for i in range(1, len(stack)):
        if op == "+":
            stack[0] = stack[0] + stack[i]
        elif op == "-":
            stack[0] = stack[0] - stack[i]
        elif op == "*":
            stack[0] = stack[0] * stack[i]
        elif op == "/":
            if stack[i] != 0:
                stack[0] = stack[0] / stack[i]
    return stack[:1]

kata_1("20 20 20 +")