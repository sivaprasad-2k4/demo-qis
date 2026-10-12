# Assignment 7 - Logging Decorator
#     Build a Python program using a custom login_required decorator to control access to different functions based onuser authentication.
#     Requirements:
# ●	Create a login_required decorator that checks whether the user is logged in before allowing access to a function.
# ●	Use the username “quest” and password “quest123” as the valid login credentials.
# ●	Create a login function that accepts the username and password from the user.
# ●	If the credentials are correct, display a login successful message and allow access to protected functions.
# ●	Create functions such as Home, About, and Profile.
# ●	Apply the login_required decorator only to functions that require authentication.
# ●	A function without the login_required decorator should work normally without login.
# ●	A function with the login_required decorator should not execute unless the user has successfully logged in.
# ●	If an unauthenticated user tries to access a protected function, display an appropriate access denied/login required message.
# ●	Demonstrate the difference between normal functions and decorator-protected functions.
# ●	Use a menu-driven program to allow the user to access the available functions.

# logged_in = False


# def login_required(function):
#     def wrapper():
#         if logged_in:
#             function()
#         else:
#             print("Access Denied! Please login first.")
#     return wrapper


# def login():
#     global logged_in

#     username = input("Enter username: ")
#     password = input("Enter password: ")

#     if username == "quest" and password == "quest123":
#         logged_in = True
#         print("Login successful!")
#     else:
#         print("Invalid username or password.")


# def Home():
#     print("Welcome to Home")


# @login_required
# def About():
#     print("Welcome to About")


# @login_required
# def Profile():
#     print("Welcome to Profile")


# while True:
#     print("\n--------- MENU ---------")
#     print("1. Login")
#     print("2. Home")
#     print("3. About")
#     print("4. Profile")
#     print("5. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         login()

#     elif choice == 2:
#         Home()

#     elif choice == 3:
#         About()

#     elif choice == 4:
#         Profile()

#     elif choice == 5:
#         print("Thank you!")
#         break

#     else:
#         print("Invalid choice.")


username = "quest"
password = "quest123"
is_logged_in = False


def login_required(fun):
    def wrapper():
        if not is_logged_in:
            print("Login first")
            return
        return fun()
    return wrapper


def login_fun():
    global is_logged_in

    entered_username = input("Username: ")
    entered_password = input("Password: ")
    is_logged_in = (
        entered_username == username and entered_password == password
    )

    if is_logged_in:
        print("Login successful.")
    else:
        print("Wrong Credentials")

    return is_logged_in


def home():
    while True:
        print("Welcome Home")
        n = int(input("1.Login\n2.Profile\n3.About\n4.Home:\n Choose an option: "))
        if n == 1:
            login_fun()
        elif n == 2:
            profile()
        elif n == 3:
            about()
        elif n == 4:
            home()
        else:
            print("Invalid input")
            return "Thank You"


@login_required
def profile():
    global username, password

    print("Profile")
    while True:
        n = int(input("1.Change username\n2.Change password\n3.Exit\n"))
        if n == 1:
            username = input("New username: ")
        elif n == 2:
            password = input("New password: ")
        else:
            break
    return 0


def about():
    print("About")
    print("This an about page.")
    n = input("Enter H or h to reach home, any key to exit. ")
    if n == "H" or n == "h":
        home()
    else:
        return "Thank You"


print(home())