# Question :
# Bala distribute C chocolates to school N students every Friday.
# The C chocolate are distributed among N students equally and the remaining chocolates R are given back to Bala
# As an example if C=100 and N=40,each students receives 2 chocolates and the balance 100-40*2=20 is given back

# Input format
# The first line denotes C
# The second line denotes N

# Output format
# The first line denotes R-the number of chocolate to be given back

# Sample testcases 
#      Input 1                  Output 1
#      300                      30
#      45

# Answer :
C = int(input())
N = int(input())
Q = int(C/N)
R = C - (N*Q)
print(R)