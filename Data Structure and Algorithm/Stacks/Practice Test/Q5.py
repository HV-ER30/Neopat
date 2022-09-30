# Question:
# Write a program to reverse the string s using stack

# Input format
#    First line of input is string

# Output format
#    Display the reversed string

# Code constraint
#    1 <= s <= 100

# Sample Testcase
#       Input 1              Output 1
#       kumar                rumak
#       Input 2              Output 2
#       Sample input         elpmas tupni

# Program Code :
 
def createStack():
    stack = []
    return stack

def size(stack):
    return len(stack)
 
def isEmpty(stack):
    if size(stack) == 0:
        return true

def push(stack, item):
    stack.append(item)
 
def pop(stack):
    if isEmpty(stack):
        return
    return stack.pop()

def reverse(string):
    n = len(string)
    stack = createStack()
    for i in range(0, n, 1):
        push(stack, string[i])
    string = ""
    for i in range(0, n, 1):
        string += pop(stack)
 
    return string

string = input("Enter the string")
string = reverse(string)
print("Reversed string is " + string)

