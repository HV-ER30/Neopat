# Question :
# Kabali is a brave warrior who with his group of young ninjas moves from one place to another to fight against his opponents. 
# Before Fighting he just calculates one thing, the difference between his ninja number and the opponent's ninja number. 
# From this difference he decides whether to fight or not. 
# Kabali's ninja number is never greater than his opponent. 
# The input contains two numbers in every line. 
# These two numbers in each line denotes the number ninjas in Kabali's clan and his opponent's clan . 
# Print the difference of number of ninjas between Kabali's clan and his opponent's clan. 
# Each output should be in seperate line.

# Input format
# First line of input contains an integer representing number of ninjas in Kabali's team
# Second line of input contains an integer representing number of ninjas in opponents team

# Output format
# Output displays the difference between two input values.

# Sample testcases
#       Input 1             Output 1
#       100                 100
#       200
#       Input 2             Output 2
#       200                 100
#       100

# Answers :
a = int(input())
b = int(input())
if(a>b):
    diff = a - b
else:
    diff = b - a
print(diff)