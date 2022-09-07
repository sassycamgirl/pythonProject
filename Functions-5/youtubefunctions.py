"""
def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


greet("Mosh", "Hamedani")
print("\n")
greet("John", "Smith")
"""

def greet(name):
    print(f"Hi {name}")

def get_greeting(name):
    return f"Hi {name}"

get_greeting("Mosh")

message = get_greeting("Mosh")
file = open("content.txt", "w")
file.write(message)
