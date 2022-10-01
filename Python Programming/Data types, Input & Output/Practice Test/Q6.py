# Question 
# In ABC corporation,a program must accept the name of an employee,his age and his salary and print them as output with a line containing 2 asterisks separating them(refer sample input and output)

# Input format
# The first line of the input consist of string.
# The second line of the input consist of integer.
# The third line of the input consist of float

# Output format
# Output prints the details.(refer sample output)

# Sample output
#       Input 1              Output 1
#       Ramesh               Ramesh
#       25                   **
#       15670                25
#                            **
#                            15670

# Answer :
name = input()
age = int(input())
salary = float(input())
print(name)
print("**")
print(age)
print("**")
print(salary)