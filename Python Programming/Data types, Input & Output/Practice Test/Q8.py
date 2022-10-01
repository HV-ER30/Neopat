# Question :
# The price P of an item is passed as the input.
# The program must print the value of P,formatting it upto 2 places after decimal point.
# The output of the program must be "The price is p"

# Input format
# Input consist of floating number.

# Output format
# Output prints the number.

# Sample testcases
#           Input 1           Output 1
#           24.59123          The price is 24.59

# Answer :

price = float(input())
print("The price is",round(price,2))