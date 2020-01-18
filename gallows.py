import re
import os
import random


def main(word):
    guessed_letters = []
    pentaly_points = 0
    while pentaly_points < 4:
        if '_' in display_word(word, guessed_letters):
            # clean_screen()
            print("{}\t\tPentaly points: {}".format(display_word(word, guessed_letters), pentaly_points))
            test_letter = (input("Input letter: ")).upper()
            if letter_in_word(word, test_letter) is not None:
                if letter_in_word(word, test_letter):
                    guessed_letters.append(test_letter)
                else:
                    pentaly_points += 1
            continue
        else:
            print(word)
            print("Congratulations! You win!")
            return
    print(word)
    print("You lose!")


def letter_in_word(word, test_letter):
    if len(test_letter) == 1 and re.search('[a-zA-Z]', test_letter):
        if test_letter in word:
            return True
        else:
            return False
    return None


def display_word(word, guessed_letters):
    display_word = ''
    for i in word:
        if i in guessed_letters:
            display_word += i
        else:
            display_word += '_'
    return display_word


if __name__ == '__main__':
    word = random.choice(['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage'])
    main(word.upper())
