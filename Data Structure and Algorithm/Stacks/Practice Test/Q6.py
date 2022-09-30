# Question :
# Write a program to check whether the given expression has balanced paranthesis or not

# Input format : 
#    First line of input constraints an expression with paranthesis

# Output format :
#    Display the given expression in first line
#    Print BALANCED or NOT BALANCED in next line

# Code constraints :
#    Expression length <= 100

# Sample Testcase :
#       Input 1           Output 1
#       (f+d){            (f+d){
#                          NOT BALANCED 
#       (d+f)             (d+f)
#                          BALANCED

# Program code :

class Stack:
    def __init__(obj):
        obj.element = []
    def empty(obj) :
        return obj.element == []
    def push(obj, item):
        obj.element.append(item)
    def pop(obj):
        return obj.element.pop()
    def check(obj,lst):
        d={'(':')','{':'}','[':']'}
        for item in lst:
            if( item == '(' or item == '{' or item == '[' ):
                Stk.push(item)
            elif( item == ')' or item == '}' or item == ']' ):
                value = Stk.pop()
                if d[value] != item :
                    return 'Not Balanced'
            else:
                continue
        if Stk.empty():
            return 'Balanced'
        else:
            return 'Not Balanced'
Stk = Stack()
lst = list(input())
print(Stk.check(lst))

   