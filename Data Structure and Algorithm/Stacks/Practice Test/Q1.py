# Question :
# Write a program to delete the top element in a stack and display the stack elements.

# Input format: 
#    Number of elements in first line
#    Stack elements in second line seperated by space

# Output Format: 
#    Deleted elements in the stack   
#    Stack elements are shown in sample output 

# Sample Testcase:
#  Input 1                   Output 1
#  5                         Deleted element is 8
#  3 6 4 9 8                 The elements in stack 
#                            9
#                            4 
#                            6 
#                            3

# Program code: 
stack =[]
n = int(input())
for i in range(n): 
    a = int(input())
    stack.append(a)
print("Deleted element is ",stack.pop())
print("The elements in the stack ")
for i in range(n-1):
    print(stack.pop())


