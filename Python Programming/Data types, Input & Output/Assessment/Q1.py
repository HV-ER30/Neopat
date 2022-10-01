# Question :
# Vikram buys an old scooter for Rs. 
# A and spends Rs. 
# B on its repairs. 
# If he sells the scooter for Rs. C , what is his gain %?
# Write a program to compute the gain %.
# Output value should be displayed correct to 2 decimal places. (Use .2f method)

# Input format
# The first input is an integer which corresponds to Cost price. 
# The second input is an integer which corresponds to repair cost. The third input corresponds to the Selling price.

# Output format
# Refer sample input and output for formatting specifications.
# The float values are displayed correct to 2 decimal places (Use .2f method)

# Sample testcases
#      Input 1             Output 1
#      4700                5.45
#      800
#      5800

# Answer :
A = int(input())
B = int(input())
C = int(input())
gain = float(((C-A-B)/(A+B))*100)
print("%.2f"%gain)