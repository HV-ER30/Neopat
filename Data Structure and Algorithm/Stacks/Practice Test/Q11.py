# Questions :
# Write a program to convert an infix expression into a postfix expression using stack concept.

# Input format :
#    Input consists of an infix expression

# Output format
#    Output displays the postfix expression of the input

# Sample testcases :
#      Input 1                Output 1
#      (a+b)*(a-b)            ab+ab-
#      Input 2                Output 2
#      A+(B+C-(D/E^F)*G)*H    ABC*DEF^/G*-H*+

# Program code :
Operators = set(['+', '-', '*', '/', '(', ')', '^'])  

Priority = {'+':1, '-':1, '*':2, '/':2, '^':3}
def infixToPostfix(expression): 
    stack = [] 
    output = '' 
    for character in expression:
        if character not in Operators:  
            output+= character
        elif character=='(':  
            stack.append('(')
        elif character==')':
            while stack and stack[-1]!= '(':
                output+=stack.pop()
            stack.pop()
        else: 
            while stack and stack[-1]!='(' and Priority[character]<=Priority[stack[-1]]:
                output+=stack.pop()
            stack.append(character)
    while stack:
        output+=stack.pop()
    return output

expression = input()
print(infixToPostfix(expression))