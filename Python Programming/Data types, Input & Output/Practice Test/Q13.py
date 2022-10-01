# Question :
# Anbu runs a shop near a school and hence sells a lot of pencils.
# Anbu wants to write a program to find the number of pencils sold everyday.
# The program will accept the number of pencil at N the beginning of the day and the number of pencils E at the end of the day(N>=E).
# The program must print the number of pencils sold on that particular day.

# Input format
# The first line denotes N
# The second line denotes E

# Output format
# The first line denotes the number of pencils sold on that day.

# Sample testcases
#          Input 1        Output 1
#          40             28
#          12

# Answer :
N = int(input())
E = int(input())
print(N-E)