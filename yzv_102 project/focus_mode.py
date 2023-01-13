import random
import time
import os

easy_words = ["hostage", "pottery", "trivial", "concert", "scholar", "pumpkin", "deficit", "freight", "culture",
              "undress", "serious", "inspire", "history", "process", "attract", "monster", "warrant", "respect",
              "impound", "justify", "evening", "prosper", "glasses", "bathtub", "privacy", "outlook", "bedroom",
              "harmony", "tourist", "partner", "auction", "applied", "archive", "quarter", "strange", "tension"]

medium_words = ["reputation", "possession", "excavation", "philosophy", "population", "federation", "illustrate",
                "memorandum", "government", "chauvinist", "substitute", "censorship", "separation", "profession",
                "goalkeeper", "earthquake", "initiative", "democratic", "hypnothize", "prediction", "vegetarian",
                "simplicity", "transition", "projection", "mainstream", "background", "overcharge", "confession"]

hard_words = ["environmental", "supplementary", "constellation", "embarrassment", "contradiction", "strikebreaker",
              "understanding", "demonstration", "consideration", "communication", "concentration", "consciousness",
              "inappropriate", "qualification", "confrontation", "preoccupation", "investigation", "revolutionary",
              "comprehensive", "entertainment", "representative", "characteristic", "superintendent", "administration",
              "discrimination", "responsibility", "infrastructure", "constitutional", "recommendation",
              "rehabilitation", "disappointment", "correspondence", "identification"]

# shuffling the word lists
random.shuffle(easy_words)
random.shuffle(medium_words)
random.shuffle(hard_words)

# THE PART ABOVE FROM HERE IS NOT ADDED IN THE REPORT

def focus_level(lst, level_score, life, n, goal):
    while True:
        try:
            os.system('cls||clear')  # for clearing the terminal
            print(f"\nWelcome to LEVEL-{n}.\n")
            print("Can you type 20 words to complete the level?\n")

            user_okay = input("Wanna Start (y/q): ")

            # raising errors if user enters invalid inputs
            assert user_okay in "y q", "Please enter a valid operation"
            assert user_okay != "", "Please enter a valid operation"

            # if user decides to start
            if user_okay == "y":
                # taking the shuffled list elements until the level goal is reached
                for item in lst:
                    # level goal condition
                    if level_score < goal:
                        # printing the game interface
                        os.system('cls||clear')  # for clearing the terminal
                        print("   -----------")
                        print(f"  | Score: {str(level_score).rjust(2)} |")
                        print(f"  | Lives: {str(life).rjust(2)} |")
                        print("   -----------")
                        print("\n   ---------")
                        print("  | Focus.. |")
                        print("   ---------\n")

                        # waiting a random time before the word is printed
                        time.sleep(random.randint(1, 5))

                        print(f" > {item}")

                        # timer starts for taking the users type time
                        start = time.time()

                        #user enters the word
                        user_typed = input(" > ")

                        # timer stops
                        took = time.time() - start

                        # if user typed slower than the limit regardless of whether it's typed true or not
                        if took > (6 - level_score * 0.1):  # in every word you need to be 0.1 seconds faster
                            print(f"\n  Sorry, you wrote it in {took:.2f} seconds")
                            print(f"\n  You need to be {(took - (6 - level_score * 0.1)):.2f} seconds faster")

                            # user life is decreased by one
                            life -= 1

                            # if the user has no more lives
                            if life <= 0:
                                print("\n  You ran out of your lives.")

                                # returns False, user's score and user's life
                                return False, level_score, life

                            time.sleep(2)

                        # if user typed faster than the limit
                        elif took <= (6 - level_score * 0.1):  # in every word you need to be 0.1 seconds faster
                            # if user typed wrong
                            if user_typed != item:
                                print("\n  Sorry, you wrote it wrong :(")

                                # user life is decreased by one
                                life -= 1

                                # if the user has no more lives
                                if life <= 0:
                                    print("\n  You ran out of your lives.")

                                    # returns False, user's score and user's life
                                    return False, level_score, life

                                time.sleep(1)

                            # if user typed correct, level score is increased by one
                            elif user_typed == item:
                                level_score += 1

                    # if the level goal is reached
                    elif level_score == goal:
                        print(f"\n  Congrats you have beaten LEVEL-{n}.")
                        time.sleep(2)

                        # returns True, user's score and user's life
                        return True, level_score, life

            # if user decides to return to main page
            elif user_okay == "q":
                # returns False, user's score and user's life
                return False, level_score, life

        # printing errors
        except Exception as error:
            print(f"\n  {error}")
            time.sleep(1)


def focus_score_checker(user_name, user_score):
    # reads the focus_score file and gathers the high score holder user and its score
    with open("focus_score.txt", "r", encoding="utf-8") as file:
        line = file.readlines()

        # if there is a score in the file
        if len(line) != 0:
            name, high_score = "".join(line).split(", ")

            # if the user beats the high score
            if user_score > int(high_score):
                # file is written again with the new high score and a message is printed
                with open("focus_score.txt", "w", encoding="utf-8") as f:
                    f.write(f"{user_name}, {user_score}")

                print(f"  \nYou have beaten {name}'s high score!")

        # if there is no score in the file, user's score is written in the file
        elif len(line) == 0:
            with open("focus_score.txt", "w", encoding="utf-8") as f:
                f.write(f"{user_name}, {user_score}")


def take_focus(name):

    # users statistics
    score = 0
    lives = 3

    print("\nWelcome to Focus Mode. In this game mode you will have 6 seconds to type a word.")
    print("The higher score you get, less time you will have.\n")

    # printing the record holder
    with open("focus_score.txt", "r", encoding="utf-8") as file:
        line = file.readlines()

        if len(line) != 0:
            name, high_score = "".join(line).split(", ")

            print(f"Current record holder: {name} - {high_score}\n")

        elif len(line) == 0:
            print(f"Current record holder: -\n")

    # THE GAME
    while True:
        user_start = input("Are you ready: (y/q): ")

        # if user decides to start
        if user_start == "y":

            # for getting to the next level
            allow_level_2 = False
            allow_level_3 = False

            # LEVEL-1
            if score == 0 and lives > 0:
                # focus_level(word list, score, lives, level number, level goal)
                beaten, points, new_lives = focus_level(easy_words, score, lives, 1, 20)

                # score and lives are updated
                score = points
                lives = new_lives

                # if user beats the level, focus_level function returns True and user can enter LEVEL-2
                if beaten:
                    allow_level_2 = True

                # user level is not beaten, stats of the user is printed and high score is checked
                elif not beaten:
                    print(f"\nFinal score: {score}")
                    focus_score_checker(name, score)

                    # allows user to exit whenever he wants
                    while True:
                        user_quit = input("\nEnter q if you want to return to main page: ")

                        if user_quit == "q":
                            break

                    break

            # LEVEL-2
            # if user beats LEVEL-1, he can enter LEVEL-2
            if allow_level_2:
                # focus_level(word list, score, lives, level number, level goal)
                beaten, points, new_lives = focus_level(medium_words, score, lives, 2, 40)

                # score and lives are updated
                score = points
                lives = new_lives

                # if user beats the level, focus_level function returns True and user can enter LEVEL-3
                if beaten:
                    allow_level_3 = True

                # user level is not beaten, stats of the user is printed and high score is checked
                elif not beaten:
                    print(f"\nFinal score: {score}")
                    focus_score_checker(name, score)

                    # allows user to exit whenever he wants
                    while True:
                        user_quit = input("\nEnter q if you want to return to main page: ")

                        if user_quit == "q":
                            break

                    break

            # LEVEL-3
            # if user beats LEVEL-2, he can enter LEVEL-3
            if allow_level_3:
                # focus_level(word list, score, lives, level number, level goal)
                beaten, points, new_lives = focus_level(hard_words, score, lives, 3, 60)
                score = points
                lives = new_lives

                # it is impossible to beat LEVEL-3, because if score 60 the limit is 0 seconds
                # so there is no need to check if the level is beaten or not
                print(f"\nFinal score: {score}")
                focus_score_checker(name, score)

                # allows user to exit whenever he wants
                while True:
                    user_quit = input("\nEnter q if you want to return to main page: ")

                    if user_quit == "q":
                        break

                break

        # if user decides to return to main page
        elif user_start == "q":
            break
