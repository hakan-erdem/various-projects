import time


def sign_in(user, pass_word):
    with open("users.txt", "r", encoding="utf-8") as file:
        # reading the lines and gathering each users' data
        lines = file.readlines()
        users_data = [item.strip() for item in lines]

        # usernames and passwords are gathered from the users.txt file
        names = [item.split(", ")[0] for item in users_data]
        passwords = [item.split(", ")[1] for item in users_data]

        # the users and passwords are stored in a dictionary for making the check easier.
        data_dict = {x: y for x, y in zip(names, passwords)}

    # if the user enters a valid username
    if user in names:

        # the wrong written password case
        if data_dict[user] != pass_word:
            print("\n  You entered your password wrong, please try again.")

            time.sleep(1.5)

            return False    # returns False and the program can not access further steps

        # correct login case
        elif data_dict[user] == pass_word:
            print(f"\n  Hello again {user}!")
            print("  You have logged in successfully")

            time.sleep(2)

            return True     # returns True and the program can access further steps

    # username doesn't exist case
    elif user not in users_data:
        print(f"\n  There is no user called {user}\n  Do you want to sign up first?")

        time.sleep(2)

        return False    # returns False and the program can not access further steps


def sign_up(user, pass_word):
    with open("users.txt", "r", encoding="utf-8") as file:
        # reading the lines and gathering each users' data
        lines = file.readlines()
        users_data = [item.strip() for item in lines]

        # gathering usernames from the users.txt file
        names = [item.split(", ")[0] for item in users_data]

        # user enters a already existed username case
        if user in names:
            print("\n  This username is already taken, please choose another.")

            time.sleep(1.5)

            return False    # returns False and the program can not access further steps

        # user enters a valid username case
        elif user not in names:
            with open("users.txt","a", encoding="utf-8") as file:
                # if username doesn't exist in the file, username and password is added in the file
                file.write(f"{user}, {pass_word}\n")

                print(f"\n  Sign up successful! Welcome {user}!")

                time.sleep(2)

                return True     # returns True and the program can access further steps
