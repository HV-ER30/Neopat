# Question :
# A integer value H denoting number of hours is passed as the input.
# Also an integer value M denoting the minutes is passed as the input.
# The program must print the sum of the seconds present in H and M

# Input format
# The first line denotes the value of H.
# The second line denotes the value of M.

# Output format
# The first line denotes the value of seconds in H+M

# Sample testcases
#         Input 1              Output 2
#         2                    8100
#         15

# Answer :
H = int(input())
M = int(input())
sum = (H*60*60)+(M*60)
print(sum)