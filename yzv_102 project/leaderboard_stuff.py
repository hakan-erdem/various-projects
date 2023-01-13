def see_leaderboard():
    # some adjustments for visualization
    print("\n\nTOP-10 Leaderboard according to the adjusted wpm.")
    print("\n # | username | wpm | accuracy | adj. wpm | adj. cpm | adj. spm |")
    print("=" * 66)

    with open("user_data.txt", "r") as file:
        # reading the lines and sorting the lines according to the third element of the lines
        lines = file.readlines()

        # making each element of the lines list a sublist for sorting the sublists
        lines = [item.strip().split(", ") for item in lines]

        # sorting according to adjusted wpm
        lines.sort(key=lambda x: x[3], reverse=True)

        # printing the first 10 lines in a proper way for a good looking leaderboard
        i = 1   # for users place in the leaderboard
        for line in lines[:10]:
            a, b, c, d, e, f = [item for item in line]

            # cutting and adding two dots at the end of the username if the username is too long
            a = f'{a[:6]}..' if len(a) > 8 else a

            print(f" {i}.  {a.ljust(8)}  {b.rjust(5)}{c.rjust(9)}{d.rjust(11)}{e.rjust(11)}{f.rjust(10)}")
            i += 1


    while True:     # getting an input from the user when he wants to exit or delete the leaderboard data
        print("\nEnter:\n\
 - q if you want to return to main page.\n\
 - d if you want to delete leaderboard data.")
        user_quit = input("\nEnter: ")

        if user_quit == "d":    # delete_leaderboard function is called if the user wants to delete the leaderboard.
            delete_leaderboard()
            break

        elif user_quit == "q":
            break


def delete_leaderboard():

    while True:
        try:
            # the program wants a password from the user
            print("\n(Enter q if you want to exit)")
            admin = input("Enter the admin password: ")

            if admin == "q":
                break

            # raises an error if its entered incorrect
            assert admin == "itu_yzv", "You entered wrong password"

            # if it is entered correct, the data in the file is deleted.
            with open("user_data.txt", "w", encoding="utf-8") as file:
                file.truncate()

            print("\n  Leaderboard data is deleted.")

            break

        except Exception as error:
            print(f"\n  {error}")


def high_score_updater(lst):
    lst = [str(item) for item in lst]
    name = lst[0]
    value = lst[3]

    with open("user_data.txt", "r", encoding="utf-8") as file:
        data = file.readlines()

    # edited list contains every users' data
    # edited will be used in updating the data and writing the file again
    edited = [item.strip().split(", ") for item in data]
    users = [item[0] for item in edited]

    # first it checks whether user in the file or not
    if name in users:
        # finds the user's place in order to compare the correct element in the edited list.
        row = users.index(name)

        # if the user's adjusted wpm is greater than before
        if float(edited[row][3]) < float(value):
            print("Wow! You have set a new high score!")
            # updates the users data with users statistics after typing test
            edited[row] = lst.copy()

        # if the user's adjusted wpm is not greater than before
        elif float(edited[row][3]) >= float(value):
            # the motivation message :)
            print("Don't give up you can beat your high score.")

    # in case the user not in the file.
    elif name not in users:
        print("Wow! You have set a new high score!")
        # adds the user statistics to the edited list
        edited.append(lst)

    # finally writes the updated users data, which is edited list,on the users_data file
    with open("user_data.txt", "w", encoding="utf-8") as file:
        for item in edited:
            item = ", ".join(item)
            file.write(f"{item}\n")
