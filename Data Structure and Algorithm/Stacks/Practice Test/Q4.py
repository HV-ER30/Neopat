# Question:
# Write a program to sort the set of elements in descending order using stack

# Input format:
#    Number of elements in first time
#    Stack elements in second line seperated by space

# Output format:
#     Element in descending order seperated by space

# Sample testcases
#     Input 1           Output 2
#     5                 10 8 7 4 2
#     8 10 4 2 7

# Program code :

def sortedInsert(s, element):
    if len(s) == 0 or element > s[-1]:
        s.append(element)
        return
    else:
        temp = s.pop()
        sortedInsert(s, element)
        s.append(temp)
 
def sortStack(s):
 
    # If stack is not empty
    if len(s) != 0:
 
        # Remove the top item
        temp = s.pop()
 
        # Sort remaining stack
        sortStack(s)
 
        # Push the top item back in sorted stack
        sortedInsert(s, temp)
 
def printStack(s):
    for i in s[::-1]:
        print(i, end=" ")
    print()
 

if __name__ == '__main__':
    n = int(input())
    s = []
    for i in range(n):
        a = int(input())
        s.append(a)
    sortStack(s)
    printStack(s)