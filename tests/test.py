import gallows
import pytest
import mock
import builtins


word = 'BLA'
guessed_letters = []

@pytest.mark.parametrize("guessed_letters", [['B'], ['L'], ['A']])
def test_display_word(guessed_letters):
    result = gallows.display_word(word, guessed_letters)
    assert guessed_letters[0] in result

@pytest.mark.parametrize("guessed_letters", [[], ['N']])
def test_display_word_empty_wrong_guessed_letters(guessed_letters):
    assert gallows.display_word(word, guessed_letters) == '___'

def test_letter_in_word_correct_letter():
    with mock.patch('builtins.input', side_effect='l'):
        assert gallows.get_letter('BLA', ['B'], 0) == "L"

def test_letter_in_word_wrong_letter():
    with mock.patch('builtins.input', side_effect='n'):
        assert gallows.get_letter(word, [], 0) == False

def test_letter_in_word_incorrecnt_input():
    with mock.patch('builtins.input', side_effect='_'):
        assert gallows.get_letter(word, [], 0) == None

def test_main(capsys):
    with mock.patch('builtins.input', side_effect=['B', 'L', 'A']):
        gallows.main(word)
        captured = capsys.readouterr()
        assert 'Congratulations! You win!' in captured.out
               