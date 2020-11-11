#Braden's Simple Login System
while True:
    username = "username"
    password = "password"

    a = input("Enter your username: ")
    b = input("Enter your password: ")

    command1 = "quit"

    if (username + password) == (a + b):
        print("Login successful!")
        print("Enter a command: ")
        commandscanner = input()
        if commandscanner == command1:
            print("Logged out.")

        username = "username"
        password = "password"

        a = input("Enter your username: ")
        b = input("Enter your password: ")

        command1 = "quit"
        if (username + password) != (a + b):
            print("Your username and/or password was incorrect.")
    continue
