def kata_1(seq):
    result = read_rpn(seq.split(' '))
    return result

def read_rpn(seq):
    stack = []
    for i in seq:
        print("i = " + i)
        try:
            stack.append(int(i))
        except:
            if (i == "+") or (i == "-") or (i == "*") or (i == "/"):
                stack = basic_op(stack, i)
            elif (i == "max" or i == "min"):
                stack = minmax(stack, i)
            else:
                raise Exception("Erreur: cet opérande est inconnu!")
    return stack[0]

            
def basic_op(stack, op):
    if len(stack) <= 1:
        raise Exception("Erreur: vous avez besoin de plus d'un chiffre pour cette opération!")
    for i in range(1, len(stack)):
        if op == "+":
            stack[0] = stack[0] + stack[i]
        elif op == "-":
            stack[0] = stack[0] - stack[i]
        elif op == "*":
            stack[0] = stack[0] * stack[i]
        elif op == "/":
            if stack[i] == 0:
                raise Exception("Erreur: division par 0 temptée!")
            stack[0] = stack[0] / stack[i]
            
    return stack[:1]

def minmax(stack, op):
    if op == "max":
        stack[0] = max(stack)
    elif op == "min":
        stack[0] = min(stack)
    return stack[:1]