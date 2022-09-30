# Question :
# Write a program to implement a stack and search for an element in a stack

# Input format :
#     Number of stack elements in first time
#     Stack elements in second line seperated by space
#     Element to be searched in third line 

# Output format :
#     Output prints whether the element is found or not

# Sample Testcases :
#      Input 1          Output 1
#      5                Element found
#      1 2 3 4 5

# Program code :
stack =[]
n = int(input())
for i in range(n): 
    a = int(input())
    stack.append(a)
num = int(input("Enter the element you wanna search :"))
count = -1
for i in range(n):
    b = stack.pop()
    if (b == num):
        count = 1
if count == 1:
    print(" Element found")
else :
    print("Element not found")
    
