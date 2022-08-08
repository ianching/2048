from random import randint
from colorama import Fore, Style
import colorama
from WordForHangman import *
colorama.init(autoreset=True)


class AnswerFunction:
    def __init__(self):
        self.answer = six_letters_words[randint(0, len(six_letters_words))].lower()

class CheckAnswer:
    def __init__(self, answer):
        self.answer = str(answer)
        self.error_type = None

    def have_error(self, guess):
        # Invalid syntax check
        abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]
        abc2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                "U", "V", "W", "X", "Y", "Z"]
        for i in guess:
            if i not in abc:
                if i not in abc2:
                    self.error_type = "Invalid Syntax"
                    return True

        # Length error check
        if len(guess) != 6 and len(guess) != 1:
            self.error_type = "Length inappropriate"
            return True
        return False

    def chk_letters(self, guess):
        if guess in self.answer:
            return "No problem"
        else:
            return "Can't find alphabet"

    def ans_result(self, guess):
        if self.have_error(guess):
            return self.error_type
        elif str(guess).lower() == self.answer:
            return "Correct"
        elif len(str(guess).lower()) == 6:
            return "Incorrect"
        else:
            return self.chk_letters(guess)

class StartGame:
    def __init__(self):
        self.difficulty = 1
        self.ans_function = AnswerFunction()
        self.answer = AnswerFunction().answer
        self.check_ans = CheckAnswer(self.answer)
        self.wrong_time = 0
        self.result = "______"
        self.not_in_ans = []
        self.status_index = 0
        self.status = ['''
    +---+
        |
        |
        |
       ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
    |   |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
    |   |
   / \  |
       ===''']
        print("Hangman")
        print("_________")
        inp = input("Type S when ready:")
        while inp.lower() != "s":
            inp = input("Type S when ready:")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(self.status[self.status_index])
        self.guess = input("Guess an alphabet or 6 letter word:")
        self.control(self.guess)

    def lose(self):
        if self.status_index == 7:
            return True
        return False

    def win(self, guess):
        if self.result == self.answer or self.check_ans.ans_result(guess) == "Correct":
            return True
        return False

    def double_letters_check(self, guess):
        fake_result = list(self.result)
        a = list(self.answer)
        x = 0
        while a.count(guess) > 0:
            fake_result[a.index(guess) + x] = guess
            x += 1
            a.pop(a.index(guess))
        temp = ""
        for i in fake_result:
            temp = temp + i
        return temp


    def control(self, guess):
        if self.lose():
            print(Fore.LIGHTRED_EX + "Lose! The answer is " + Fore.RESET + "\"" +
                  self.answer.title() + "\".\nGood luck next time!")
            return
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
        if self.check_ans.ans_result(guess) == "Incorrect":
            self.wrong_time += 1
            print(Fore.LIGHTYELLOW_EX + "Incorrect!")
        self.status_index += 1
        if self.check_ans.ans_result(guess) == "Invalid Syntax":
            new_guess = input(Fore.RED + Style.BRIGHT + "Cannot contain any symbol, number or spacing:")
            self.control(new_guess)
        elif self.check_ans.ans_result(guess) == "Length inappropriate":
            new_guess = input(Fore.RED + Style.BRIGHT + "Only input ALPHABET or 6 LETTER WORDS:")
            self.control(new_guess)
        else:
            if self.check_ans.ans_result(guess) == "Can't find alphabet":
                print(Fore.LIGHTYELLOW_EX + "Not in word!")
                self.wrong_time += 1
                self.not_in_ans.append(guess)
                print(self.result)
            else:
                self.result = self.double_letters_check(guess)
                self.status_index += -1
                print(self.result)
            print(self.status[self.status_index])
            if self.win(guess):
                print(self.answer)
                print(Fore.LIGHTGREEN_EX + "Correct!" + Fore.RESET + " Wrong time : " + str(self.wrong_time))
                return
            new_guess = input("Guess an alphabet or 6 letter word:")
            self.control(new_guess)





StartGame()
