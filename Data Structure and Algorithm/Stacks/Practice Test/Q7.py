# Question :
# Write a program to insert elements in the stack and display the topmost element

# Input format :
#     Number of stack elements in first line
#     Stack elements in second line seperated by space

# Output format :
#     Topmost element in the stack

# Sample Testcase :
#       Input 1          Output 1
#       5                6
#       3 9 4 7 6 

# Program code :
stack =[]
n = int(input())
for i in range(n): 
    a = int(input())
    stack.append(a)
print(stack.pop())