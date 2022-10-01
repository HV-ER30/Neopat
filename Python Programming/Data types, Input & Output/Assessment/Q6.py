# Question :
# Write a program to print the sum of the first K natural numbers.

# Input format
# Input consists of an Integer K.

# Output format
# Output the sum of first k natural numbers.

# Sample testcases
#     Input 1        Output 1
#     5              15

# Answer :
K = int(input())
sum = int((K*(K+1))/2)
print(sum)