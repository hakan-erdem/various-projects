from text_finder import easy_text_finder, medium_text_finder, hard_text_finder, tongue_twister_finder
from leaderboard_stuff import high_score_updater
import os   # used for clearing the terminal in the program
import time


def take_test(name, difficulty):
    text = None
    sentences = None

    while True:
        os.system('cls||clear')     # for clearing the terminal

        # easy text case
        if difficulty == "easy":
            text, sentences = easy_text_finder()

        # medium text case
        elif difficulty == "medium":
            text, sentences = medium_text_finder()

        # hard text case
        elif difficulty == "hard":
            text, sentences = hard_text_finder()

        print("\n\nThis is your text:\n")
        print(text)

        warning = "If you want a new text, just press any other button than y and q."
        offer = "Wanna start (yes or quit)? (y/q): "
        user_test = input(f"\nYour text will be given sentence by sentence once you start.\n{warning}\n\n{offer}")

        # starting the text if user enters y
        if user_test == "y":
            os.system('cls||clear')     # for clearing the terminal

            # timer starts
            start = time.time()

            # some variables to calculate user stats
            wrong_word_count = 0
            typed_words_count = 0
            not_written_words = 0
            wrong_word_lst = []

            wrong_sentences_count = 0
            typed_sentences_count = len(sentences)

            wrong_chars_count = 0
            typed_char_count = 0

            # printing and getting inputs from user sentence by sentence
            for item in sentences:
                words = item.split()

                print(f"\n{item[1:]}")

                # the user's entry
                typed = input()
                typed_char_count += len(typed)

                # CHECKING SENTENCES
                if typed != item[1:]:
                    # if sentence is not the same wrong written sentence value is increased by 1
                    wrong_sentences_count += 1

                # CHECKING WORDS AND CHARS
                typed_words_count += len(typed.split())

                # if the user ends the sentence earlier and misses remaining words
                missed = len(words) - len(typed.split())
                if missed > 0:
                    not_written_words += missed
                    missed_chars = "".join(words[len(typed.split()):])
                    wrong_chars_count += len(missed_chars)

                # finding wrong written words for showing to the user after test
                for j, k in zip(words, typed.split()):
                    if j != k:
                        wrong_word_lst.append(j)

                        # finding wrong chars
                        for a, b in zip(j, k):
                            if a != b:
                                wrong_chars_count += 1

            # wrong written word count is: (missed words after the sentence) + (wrong typed words)
            wrong_word_count += not_written_words + len(wrong_word_lst)

            # timer stops
            took = time.time() - start

            # # # # # # # # # # #
            # WORD CALCULATIONS #
            # # # # # # # # # # #
            wpm = typed_words_count / took * 60  # words per minute

            # adding a condition if word accuracy is calculated negative
            if typed_words_count > 0 and typed_words_count - wrong_word_count > 0:
                word_accuracy = (typed_words_count - wrong_word_count) / typed_words_count * 100
            else:
                word_accuracy = 0

            # adding a condition if adjusted wpm is calculated negative
            adjusted_wpm_calculation = (typed_words_count - wrong_word_count) / took * 60
            adjusted_wpm = adjusted_wpm_calculation if adjusted_wpm_calculation > 0 else 0

            # # # # # # # # # # # # #
            # SENTENCE CALCULATIONS #
            # # # # # # # # # # # # #
            spm = typed_sentences_count / took * 60  # sentences per minute

            # adding a condition if sentence accuracy is calculated negative
            if typed_sentences_count > 0 and typed_sentences_count - wrong_sentences_count > 0:
                sentence_accuracy = (typed_sentences_count - wrong_sentences_count) / typed_sentences_count * 100
            else:
                sentence_accuracy = 0

            # adding a condition if adjusted spm is calculated negative
            adjusted_spm_calculation = (typed_sentences_count - wrong_sentences_count) / took * 60
            adjusted_spm = adjusted_spm_calculation if adjusted_spm_calculation > 0 else 0

            # # # # # # # # # # # # # #
            # CHARACTER CALCULATIONS  #
            # # # # # # # # # # # # # #
            cpm = typed_char_count / took * 60  # chars per minute

            # adding a condition if character accuracy is calculated negative
            if typed_char_count > 0 and typed_char_count - wrong_chars_count > 0:
                char_accuracy = (typed_char_count - wrong_chars_count) / typed_char_count * 100
            else:
                char_accuracy = 0

            # adding a condition if adjusted cpm is calculated negative
            adjusted_cpm_calculation = (typed_char_count - wrong_chars_count) / took * 60
            adjusted_cpm = adjusted_cpm_calculation if adjusted_cpm_calculation > 0 else 0

            # # # # # # # # # # # #
            # PRINTING THE STATS  #
            # # # # # # # # # # # #

            # storing the user statistics
            user_stats = [name, f"{wpm:.1f}", f"{word_accuracy:.1f}", f"{adjusted_wpm:.1f}",
                          f"{adjusted_cpm:.1f}", f"{adjusted_spm:.1f}"]

            print("\nRESULTS:\n")

            # calling the high_score_updater function with user statistics
            high_score_updater(user_stats)
            time.sleep(0.5)

            print(f"\nIt took {took:.2f} seconds to write\n")
            time.sleep(0.5)

            print(f"WORD STATS:\n\
            - wrong words: {', '.join(wrong_word_lst) if len(wrong_word_lst)<8 else ', '.join(wrong_word_lst[:8]) + ' ...'}\n\
            - Your wpm: {wpm:.2f} words per minute\n\
            - Words counted as wrong: {wrong_word_count}\n\
            - Your accuracy in words: {word_accuracy:.2f}%\n\
            - Your adjusted wpm: {adjusted_wpm:.2f} words per minute\n")

            time.sleep(2)

            print(f"CHARACTER STATS:\n\
            - Your cpm: {cpm:.2f} characters per minute\n\
            - Characters counted as wrong: {wrong_chars_count}\n\
            - Your accuracy in characters: {char_accuracy:.2f}%\n\
            - Your adjusted cpm: {adjusted_cpm:.2f} characters per minute\n")

            time.sleep(2)

            print(f"SENTENCE STATS:\n\
            - Your spm: {spm:.2f} sentences per minute\n\
            - Sentences counted as wrong: {wrong_sentences_count}\n\
            - Your accuracy in sentences: {sentence_accuracy:.2f}%\n\
            - Your adjusted spm: {adjusted_spm:.2f} sentences per minute\n")

            time.sleep(2)

            while True:
                user_quit = input("Enter q if you want to return to main page: ")

                if user_quit == "q":
                    break

            break

        # returning to main page if user enters q
        elif user_test == "q":
            break


def take_twister():

    while True:
        os.system('cls||clear')  # for clearing the terminal
        twister, sentences = tongue_twister_finder()

        print("\nThis is your tongue twister:\n")
        for line in sentences:
            print(line[1:])

        warning = "If you want a new twister, just press any other button than y and q."
        offer = "Wanna start (yes or quit)? (y/q): "
        user_test = input(f"\nYour twister will be given sentence by sentence once you start.\n{warning}\n\n{offer}")

        # starting the game if user enters y
        if user_test == "y":
            os.system('cls||clear')  # for clearing the terminal

            # timer starts
            start = time.time()

            # some variables to calculate user stats
            wrong_word_count = 0
            typed_words_count = 0
            not_written = 0
            wrong_word_lst = []


            # printing and getting inputs from user sentence by sentence
            for item in sentences:
                words = item.split()

                print(f"\n{item[1:]}")
                typed = input()

                typed_words_count += len(typed.split())

                # if the user ends the sentence earlier and misses remaining words
                missed = len(words) - len(typed.split())

                if missed > 0:
                    not_written += missed

                # finding wrong written words for showing the user after test
                for j, k in zip(words, typed.split()):
                    if j != k:
                        wrong_word_lst.append(j)

            # wrong written word count is: (missed words after the sentence) + (wrong typed words)
            wrong_word_count += not_written + len(wrong_word_lst)

            # timer stops
            took = time.time() - start

            # WORD CALCULATIONS
            wpm = typed_words_count / took * 60  # words per minute

            # adding a condition if word accuracy is calculated negative
            if typed_words_count > 0 and typed_words_count - wrong_word_count > 0:
                word_accuracy = (typed_words_count - wrong_word_count) / typed_words_count * 100
            else:
                word_accuracy = 0

            # adding a condition if adjusted wpm is calculated negative
            adjusted_wpm_calculation = (typed_words_count - wrong_word_count) / took * 60
            adjusted_wpm = adjusted_wpm_calculation if adjusted_wpm_calculation > 0 else 0

            print("\nRESULTS:")

            time.sleep(0.5)

            print(f"\nIt took {took:.2f} seconds to write\n")
            time.sleep(0.5)

            print(f"WORD STATS:\n \
            - wrong words: {wrong_word_lst}\n \
            - Your wpm: {wpm:.2f} words per minute\n \
            - Words counted as wrong: {wrong_word_count}\n \
            - Your accuracy in words: {word_accuracy:.2f}%\n \
            - Your adjusted wpm: {adjusted_wpm:.2f} words per minute\n")

            while True:
                user_quit = input("Enter q if you want to return to main page: ")

                if user_quit == "q":
                    break

            break

        # returning to main page if user enters q
        elif user_test == "q":
            break
