from login_stuff import sign_in, sign_up
from leaderboard_stuff import see_leaderboard
from test_and_twister import take_test, take_twister
from focus_mode import take_focus
import time
import os   # used for clearing the terminal in the program


def get_help():
    # prints the README.txt file without the admin password information.
    with open("README.txt", "r", encoding="utf-8") as file:
        lines = file.read().split("\n")

    # passing the admin password part
    for item in lines[4:]:
        print(item)

    # after the users reads what he wants, he can exit by entering q
    while True:
        user_quit = input("Enter q if you want to return to main page: ")

        if user_quit == "q":
            break


def about():
	
    print("\nThis project is made by Hakan Erdem.")
    print("\nIt is the term project of Introduction to Data Science (Python) course.")

    print("\nTyphon is a typing calculator/game for finding your typing skills. You can select 3 different levels for typing and find your:\
     \n\n - Typing speed\n - Accuracy\n - Statistics of your typing\n - Skill among the other players via a leaderboard")

    print()
    while True:
        user_quit = input("Enter q if you want to return to main page: ")

        if user_quit == "q":
            break

# # # # # # # # #
# THE INTERFACE #
# # # # # # # # #

while True:
    os.system('cls||clear')     # for clearing the terminal

    print("\n\t|'''\     WELCOME TO TYPHON     /'''|\n\t|::=- - - - - - - - - - - - - - -=::|")
    print("\nEnter:\n\
    1 for sign in\n\
    2 for sign up\n\
    quit for quiting.")

    user_input = input("\n Enter what you want to do: ")

    ticket = False  # think the ticket as a real ticket
                    # if the user signs in or signs up successfully, he gets a ticket and enters the program

    username = None

    # SIGNING IN SECTION
    if user_input == "1":
        while True:
            os.system('cls||clear')     # for clearing the terminal

            print("\n(If you want to get back to home page, write quit in username.)")
            try:
                username = input("Enter your username: ")

                # if user wants to return back, he enters quit in username and loop breaks
                if username == "quit":
                    break

                password = input("Enter your password: ")

                # raising errors in unwanted cases, such as empty input or input that contains blanks
                assert username != "", "Please enter a username"
                assert " " not in username, "Username can't include blanks"
                assert password != "", "Please enter a password"
                assert " " not in password, "Password can't include blanks"

                # calls sign in function if username and password is entered valid.
                valid = sign_in(username, password)

                # sign in function returns True or False

                # if user enters correct inputs in sign in function, sign in function returns True
                # if the user doesnt enter proper input, sign in function returns False

                # if sign in function returns True, user gets a ticket
                if valid:
                    ticket = True  # ticket is for entering the program
                    break

            except Exception as error:
                print(f"\n  {error}")
                time.sleep(1)

    # SIGNING UP SECTION
    elif user_input == "2":
        while True:
            os.system('cls||clear')     # for clearing the terminal

            print("\n(If you want to get back to home page, write quit in username.)")
            try:
                username = input("Enter your username: ")

                # if user wants to return back, he enters quit in username and loop breaks
                if username == "quit":
                    break

                password = input("Enter your password: ")

                # raising errors in unwanted cases, such as empty input or input that contains blanks
                assert username != "", "Please enter a username"
                assert " " not in username, "Username can't include blanks"
                assert password != "", "Please enter a password"
                assert " " not in password, "Password can't include blanks"

                # calls sign up function if username and password is entered valid.
                valid = sign_up(username, password)

                # sign up function returns True or False

                # if user enters correct inputs in sign up function, sign up function returns True
                # if the user doesnt enter proper input, sign up function returns False

                # if sign up function returns True, user gets a ticket
                if valid:
                    ticket = True  # ticket is for entering the program
                    break

            except Exception as error:
                print(f"\n  {error}")
                time.sleep(1)

    # if the user wants to quit the program
    elif user_input == "quit":
        print("\n  Hope to see you again soon!")
        quit()

    # if the user enters an invalid operation
    else:
        print("\n  Please enter a valid operation.")

        time.sleep(1)


    # if the user signs in or signs up successfully, he gets a ticket basically and enters the program.
    if ticket:
        while True:
            os.system('cls||clear')     # for clearing the terminal

            print("\nSo what do you want to do? Enter:\n- 1 for taking easy test\n- 2 for taking medium test\
            \n- 3 for taking hard test\n- 4 for focus mode\n- 5 for tongue twister mode\
            \n- l for to look at the leaderboard\n- h for help\n- a for about\
            \n- q for logging out\n- quit for exiting program.")

            try:
                operation = input("\nEnter what you want to do: ")

                # in case the users enters invalid input, an exception is raised
                assert operation in "1 2 3 4 5 l h a q quit", "Please enter a valid operation."
                assert operation != "", "Please enter a valid operation."

                # easy test
                if operation == "1":
                    take_test(username, "easy")

                # medium test
                elif operation == "2":
                    take_test(username, "medium")

                # hard test
                elif operation == "3":
                    take_test(username, "hard")

                # focus mode
                elif operation == "4":
                    os.system('cls||clear')     # for clearing the terminal
                    take_focus(username)

                # tongue twister mode
                elif operation == "5":
                    os.system('cls||clear')     # for clearing the terminal
                    take_twister()

                # printing leaderboard
                elif operation == "l":
                    os.system('cls||clear')     # for clearing the terminal
                    see_leaderboard()

                # printing the rules of the typhon
                elif operation == "h":
                    os.system('cls||clear')     # for clearing the terminal
                    get_help()

                # printing the aim and features of typhon
                elif operation == "a":
                    os.system('cls||clear')     # for clearing the terminal
                    about()

                # returning the login page
                elif operation == "q":
                    print("\n  You have logged out.")
                    break

                # quiting the program
                elif operation == "quit":
                    print("\n  Hope to see you again soon!")
                    quit()

            # printing the exceptions
            except Exception as error:
                print(f"\n  {error}")
                time.sleep(1)
