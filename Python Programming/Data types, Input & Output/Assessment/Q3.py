# Question 
# WonderWorks Magic Show
# The Magic Castle, the home of the Academy of Magical Arts at California has organized the great ‘WonderWorks Magic Show’. 
# 3 renowned magicians were invited to mystify and thrill the crowd with their world’s spectacular magic tricks. 
# At the end of each of the 3 magicians’ shows, the audience were requested to give their feedback in a scale of 1 to 10. 
# Number of people who watched each show and the average feedback rating of each show is known. 
# Write a program to find the average feedback rating of the WonderWorks Magic show.

# Input format
# First line of the input is an integer value that corresponds to the number of people who watched show 1.
# Second line of the input is a float value that corresponds to the average rating of show 1.
# Third line of the input is an integer value that corresponds to the number of people who watched show 2.
# Fourth line of the input is a float value that corresponds to the average rating of show 2.
# Fifth line of the input is an integer value that corresponds to the number of people who watched show 3.
# Sixth line of the input is a float value that corresponds to the average rating of show 3.

# Output format
# Output should display the overall average rating for the show. Display the rating correct to 2 decimal places.
# (Use the key word round to round off the decimal places).
# Refer sample input and output for formatting specifications.

# Code constraints
# 0<=Average rating <=10

# Sample testcases
#    Input 1              Output 1
#    400                  9.22
#    9.8
#    500
#    9.6
#    100 
#    5

# Answer :
PS1 = int(input())
ARS1 = float(input())
PS2 = int(input())
ARS2 = float(input())
PS3 = int(input())
ARS3 = float(input())
RS1 = PS1*ARS1
RS2 = PS2*ARS2
RS3 = PS3*ARS3
PS = PS1+PS2+PS3
RS = RS1+RS2+RS3
Average = RS/PS
print(round(Average,2))