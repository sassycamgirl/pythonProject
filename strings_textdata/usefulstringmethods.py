"""
useful string methods
"""

message = 'Welcome to Python!'
messagetwo = 'welcome to Python!'
print(message)

# methods are a way to seperate code
# prints in upper case
print(message.upper())
# prints in lower case
print(message.lower())
# prints the first letter of messagetwo with a capital letter
print(messagetwo.capitalize())
# counts the number of the letter o
print(message.count('o'))
# checks to see if last letter is a
print(message.endswith('a'))
# checks if message is a digit
print(message.isdigit())