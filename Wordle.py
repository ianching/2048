from random import randint
from WordForWordle import word_lst
from colorama import init, Fore, Style
init(autoreset=True)

class AnswerFunction:
    def __init__(self):
        self.answer = word_lst[randint(0, len(word_lst))]

class CheckAnswer:
    def __init__(self, answer):
        self.answer = answer
        self.error_type = None

    def have_error(self, w):
        # Invalid syntax check
        abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]
        abc2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                "U", "V", "W", "X", "Y", "Z"]
        for i in w:
            if i not in abc:
                if i not in abc2:
                    self.error_type = "Invalid Syntax"
                    return True

        # Length error check
        if len(w) != 5:
            self.error_type = "Length error"
            return True

        # Not in Word List check
        if w.lower() not in word_lst:
            self.error_type = "Not in word list"
            return True
        return False

    def chk_letters(self, w):
        result = ""
        cnt = 0
        w.title()
        for i in self.answer:
            if w[cnt] == i:
                result = result + Fore.LIGHTGREEN_EX + (w[cnt]).lower()
            elif w[cnt] in self.answer:
                result = result + Fore.LIGHTYELLOW_EX + (w[cnt]).lower()
            else:
                result = result + Fore.LIGHTBLACK_EX + (w[cnt]).lower()
            cnt += 1
        return result

    def ans_result(self, w):
        w.replace(" ", "")
        if self.have_error(w):
            return self.error_type
        elif str(w).lower() == self.answer:
            return "Correct"
        else:
            return self.chk_letters(w)

class StartGame:
    def __init__(self):
        self.answer = AnswerFunction().answer
        print("""\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                  \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n""")
        print(Fore.LIGHTGREEN_EX + "Wo" + Fore.LIGHTYELLOW_EX + "rd" + Fore.LIGHTGREEN_EX + "le"
              + Fore.RESET + "\n\n\n______________________________________________________")
        self.chk_ans = CheckAnswer(self.answer)
        self.tries = 1
        self.left_tries = 10
        self.previous_guess = []
        self.input = input(Fore.RESET + "Type S when ready:").lower()
        while self.input != "s":
            self.input = input("Type S when ready:").lower()
        print("""\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                          \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n""")
        print("Start!")
        self.guess = input("Enter 5 letters word:")
        self.control(self.guess)

    def control(self, guess):
        if self.chk_ans.ans_result(guess) == "Correct":
            self.previous_guess.append(Fore.LIGHTGREEN_EX + guess.lower())
            print("""\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
            \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n""")
            for i in range(len(self.previous_guess)):
                print(self.previous_guess[i])
            print(Fore.RESET + "Correct!\nUsed tries:" + str(self.tries))
        elif self.chk_ans.ans_result(guess) == "Invalid Syntax":
            new_guess = input(Fore.RED + Style.BRIGHT + "Cannot contain any symbol, number or spacing:")
            self.control(new_guess)
        elif self.chk_ans.ans_result(guess) == "Length error":
            new_guess = input(Fore.RED + Style.BRIGHT + "Only input 5 letters english word:")
            self.control(new_guess)
        elif self.chk_ans.ans_result(guess) == "Not in word list":
            new_guess = input(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Not in word list:")
            self.control(new_guess)
        else:
            self.previous_guess.append(self.chk_ans.ans_result(guess))
            print("""\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
                        \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n""")
            for i in range(len(self.previous_guess)):
                print(self.previous_guess[i])
            self.tries += 1
            new_guess = input("Enter 5 letters word:")
            self.control(new_guess)
