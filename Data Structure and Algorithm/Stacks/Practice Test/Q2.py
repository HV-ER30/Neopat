# Question:
# Write a program to print all the factor of a number using stack through arrray implementation.

# Input format:
#    Format line of the input is a number

# Output format:
#    Print all the facotrs of the number separated by space.

# Code constraint:
#   0<N<999999

# Sample Testcase:
#     Input 1                Ouput 1
#     5                      5 1 
#     Input 2                Output 2
#     -1                     Wrong input  

# Program code :
num = int(input())
i = 1
if (num <= 0):
    print("Wrong input")
else :
    while(i <= num):
        if(num % i == 0):
            print(" ",i)
        i+=1
