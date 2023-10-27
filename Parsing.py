import sys

token = ''
position = 0

# recursive sir(main function)
def expr():
    global token, position
    temp = term()
    while position < len(token) and token[position] in ('+', '-'):
        if token[position] == '+':
            position += 1
            temp += term()
        elif token[position] == '-':
            position += 1
            temp -= term()
    return temp

def term():
    global token, position
    temp = factor()
    while position < len(token) and token[position] == '/':
        position += 1
        temp /= factor()
    while position < len(token) and token[position] == '*':
        position += 1
        temp *= factor()
 
    return temp

def factor():
    global token, position
    if position < len(token) and token[position] == '(':
        position += 1
        temp = expr()
        if position < len(token) and token[position] == ')':
            position += 1
        else:
            error()
    elif position < len(token) and token[position].isdigit():
        start = position
        while position < len(token) and token[position].isdigit():
            position += 1
        temp = int(token[start:position])

    return temp

# error if token not found sir
def error():
    sys.stderr.write("Error\n")
    sys.exit(1)

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def parse_expression(expression):
    tokens = expression.split('+')
    return build_parse_tree(tokens)

def build_parse_tree(tokens):
    if len(tokens) == 1:
        return Node(tokens[0])
    else:
        operator = '+'
        return Node(operator, build_parse_tree(tokens[:1]), build_parse_tree(tokens[1:]))

def print_parse_tree(node, level=0):
    if node:
        print(" " * (level * 4) + str(node.value))
        print_parse_tree(node.left, level + 1)
        print_parse_tree(node.right, level + 1)
        
if __name__ == "__main__":
    result = 0
    print("A RECURSIVE-DESCENT CALCULATOR.")
    print("\t the valid operations are +, - and *")
    print("Enter the calculation string, e.g. '34+6*56'")
    expression = input("Enter an expression: ")
    expression = ''.join(expression.split())
    
    print("This is what you input",expression)
    parse_tree = parse_expression(expression)
    print_parse_tree(parse_tree)
    
    token = expression + ' '  

    try:
        result = expr()
        if position == len(token) - 1:
            print(f"Result = {result}")
        else:
            error()
    except:
        print("Early Error")

        # error()
        