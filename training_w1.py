def greet_user(name):
    message = "Hello " + name
    return message

name = input("Enter your name: ")

result = greet_user(name)

if name == "":
    print("You did not enter a name")
else:
    print(result)