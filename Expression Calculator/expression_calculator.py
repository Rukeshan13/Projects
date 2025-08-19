# Expression Calculator (Infix to Postfix + Evaluation)

# Function to set precedence of operators
def precedence(op):
    if op == '^':
        return 3
    if op in ('*', '/'):
        return 2
    if op in ('+', '-'):
        return 1
    return 0

# Function to convert infix expression to postfix
def infix_to_postfix(expression):
    stack = []
    postfix = []
    
    for token in expression:
        if token.isdigit():  # operand
            postfix.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  # remove '('
        else:  # operator
            while stack and precedence(stack[-1]) >= precedence(token):
                postfix.append(stack.pop())
            stack.append(token)

    while stack:
        postfix.append(stack.pop())
    
    return postfix

# Function to evaluate postfix expression
def evaluate_postfix(postfix):
    stack = []
    for token in postfix:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+': stack.append(a + b)
            elif token == '-': stack.append(a - b)
            elif token == '*': stack.append(a * b)
            elif token == '/': stack.append(a // b)  # integer division
            elif token == '^': stack.append(a ** b)
    return stack[0]

# Main function
def expression_calculator(expression):
    expression = expression.replace(" ", "")  # remove spaces
    postfix = infix_to_postfix(expression)
    print("Postfix:", " ".join(postfix))
    result = evaluate_postfix(postfix)
    print("Result:", result)
    return result

# Example usage
if _name_ == "_main_":
    expr = input("Enter an expression (e.g. 3+5*(2-8)): ")
    expression_calculator(expr)