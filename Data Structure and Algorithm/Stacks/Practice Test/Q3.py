# Question: 
# Write a program to check whether the string is a pallindrome or not using stack.

# Input format:
#    Input consists of string

# Ouput format:
#    Ouput prints whehter the string is pallindrom or not
#    Refer sample out for exact format.

# Sample Testcase:
#    Input 1                  Output 1
#    malayalam                malayamam is a pallindrome
#    Input 2                  Output 2
#    racer                    racer is not a pallindrome

# Program code :

class Stack:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def push(self, data):
        self.items.append(data)
 
    def pop(self):
        return self.items.pop()
  
s = Stack()
text = input()
 
for character in text:
    s.push(character)
 
reversed_text = ''
while not s.is_empty():
    reversed_text = reversed_text + s.pop()
 
if text == reversed_text:
    print(text,'is a palindrome.')
else:
    print(text,'is not a palindrome.')
    