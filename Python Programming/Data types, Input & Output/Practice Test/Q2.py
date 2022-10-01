# Question
# Be it a last minute get together, a birthday party or corporate events, the "Pine Tree" Event Management Company helps you plan and execute it better and faster. 
# Nikhil, the founder of the company wanted the Pineaxe Event Management System to get and display the event details from his Customers for every new order of the Company.
# Write a program that will get the input of the event details like name of the event, type of the event, number of people expected, a string value (Y/N) telling whether the event is going to be a paid entry and the projected expenses (in lakhs) for the event. 
# The program should then display the input values as a formatted output.

# Input format :
# First input is a string that corresponds to the name of the event. Assume the maximum length of the string as 50.
# Second input is a string that corresponds to the type of the event. Assume the maximum length of the string as 50.
# Third input is an integer that corresponds to the number of people expected for the event.
# Fourth input is a character that corresponds to Y/N telling whether the event is going to be a paid entry or not.
# Fifth input is a double value that corresponds to the projected expenses (in lakhs) for the event.

# Output format :
# Output should display the event details as given in the sample output.
# All double values need to be displayed correct to 1 decimal place
# Refer sample input and output for formatting specifications.

# Code constraints :
# Use round function to round off up-to 1 decimal place.

# Sample testcases: 
#        Input 1                               Output 1 
#        Food Fest 2017                        Event Name : Food Fest 2017
#        Public                                Event Type : Public 
#        5000                                  Expected Count : 5000
#        Y                                     Paid Entry : Y
#        5.7                                   Projected Expense : 5.7L

# Answer :
a = input()
b = input()
c = int(input())
d = input()
e = float(input())
print("Event Name :",a)
print("Event Type :",b)
print("Expected Count :",c)
print("Paid Entry :",d)
print("Projected Expense :",round(e,1),end = "L")