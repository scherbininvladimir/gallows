import re
# import os
import random


def main(word):
    guessed_letters = []
    pentaly_points = 0
    while pentaly_points < 4:
        if '_' in display_word(word, guessed_letters):
            letter = get_letter(word, guessed_letters, pentaly_points)
            if letter is None:
                continue
            if not letter:
                pentaly_points += 1
            else:
                guessed_letters.append(letter)
            continue
        else:
            print(word)
            print("Congratulations! You win!")
            return
    print(word)
    print("You lose!")


def get_letter(word, guessed_letters, pentaly_points):
    print("{}\t\tPentaly points: {}".format(display_word(word, guessed_letters), pentaly_points))
    test_letter = (input("Input letter: ")).upper()
    if len(test_letter) == 1 and re.search('[a-zA-Z]', test_letter):
        if test_letter in word:
            return test_letter
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


# def clean_screen():
    # if os.name == 'nt': 
    #     _ = os.system('cls') 
    # else: 
    #     _ = os.system('clear') 

if __name__ == '__main__':
    word = random.choice(['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage'])
    main(word.upper())
