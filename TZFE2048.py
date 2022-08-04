from random import randint
from colorama import Fore
import colorama
colorama.init(autoreset=True)

class BoardFunction:
    def __init__(self, size):
        self.size = size
        self.board = [[0 for _ in range(self.size)] for _ in range(self.size)]

    def print_board(self, board):
        print("""\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                          \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n""")
        for i in board:
            print(" | ".join([str(j) for j in i]))

    def generate_random_num(self, board):
        lst0 = []
        for y, i in enumerate(board):
            for x, a in enumerate(i):
                if a == 0:
                    lst0.append((x, y))
        c = randint(0, len(lst0) - 1)
        x, y = lst0[c]
        if randint(1, 100) > 20:
            board[y][x] = 2
        else:
            board[y][x] = 4
        return board

class BoardOperation:
    @staticmethod
    def merge(board):
        merged = []
        for line in board:
            lst = []
            line_final = []
            for i in line:
                if i != 0: lst.append(i)
            lis = lst[:]

            while len(lis) > 1:
                if lis[0] == lis[1]:
                    line_final.append(2 * lis[0])
                    lis.pop(0)
                    lis.pop(0)
                else:
                    line_final.append(lis[0])
                    lis.pop(0)
            if len(lis) == 1: line_final.append(lis[0])
            for y in range(0, len(line) - len(line_final)):
                line_final.append(0)
            merged.append(line_final)
        return merged

    @staticmethod
    def flip(board):
        flipped = []
        for line in board:
            a = list(reversed(line))
            flipped.append(a)
        return flipped

    @staticmethod
    def transpose(board):
        new_board = []
        for i in range(len(board[0])):
            line = [board[y][i] for y in range(len(board))]
            new_board.append(line)
        return new_board

class StartGame:
    def __init__(self, board_size=None):
        self.move = None
        if board_size is None:
            self.board_size = 4
        else:
            self.board_size = board_size
        self.gb_function = BoardFunction(self.board_size)
        self.gb_operation = BoardOperation()
        self.board = BoardFunction(int(self.board_size)).board
        self.flag = 0
        self.gb_function.generate_random_num(self.board)
        print("""\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                          \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n""")
        print("2048\n\n\n______________________________________________________")
        self.input = input("Type S when ready:").lower()
        while self.input != "s":
            self.input = input("Type S when ready:").lower()
        print("""\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                                      \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n""")
        print("Start!")
        self.control()

    def chk_input_error(self):
        if self.move == "W" or self.move == "A" or self.move == "S" or self.move == "D":
            return False
        else:
            return True

    def merge_up(self):
        new_board = self.gb_operation.transpose(self.board)
        new_board = self.gb_operation.merge(new_board)
        new_board = self.gb_operation.transpose(new_board)
        return new_board

    def merge_down(self):
        new_board = self.gb_operation.transpose(self.board)
        new_board = self.gb_operation.flip(new_board)
        new_board = self.gb_operation.merge(new_board)
        new_board = self.gb_operation.flip(new_board)
        new_board = self.gb_operation.transpose(new_board)
        return new_board

    def merge_left(self):
        new_board = self.gb_operation.merge(self.board)
        return new_board

    def merge_right(self):
        new_board = self.gb_operation.flip(self.board)
        new_board = self.gb_operation.merge(new_board)
        new_board = self.gb_operation.flip(new_board)
        return new_board

    def do_merge(self):
        if self.move == "W":
            new_board = self.merge_up()
            if self.board != new_board:
                self.flag = 1
            return new_board
        elif self.move == "A":
            new_board = self.merge_left()
            if self.board != new_board:
                self.flag = 1
            return new_board
        elif self.move == "S":
            new_board = self.merge_down()
            if self.board != new_board:
                self.flag = 1
            return new_board
        elif self.move == "D":
            new_board = self.merge_right()
            if self.board != new_board:
                self.flag = 1
            return new_board

    def winning(self):
        for i in self.board:
            for x in i:
                if str(x) == "2048":
                    return True
        return False

    def losing(self):
        if self.board != self.merge_up() or self.board != self.merge_down():
            return False
        elif self.board != self.merge_left() or self.board != self.merge_right():
            return False
        return True

    def control(self):
        self.gb_function.print_board(self.board)
        self.move = str.upper(input("Move(W/A/S/D):"))
        while self.chk_input_error():
            self.move = str.upper(input(Fore. LIGHTRED_EX + "Enter W/A/S/D:"))
        self.board = self.do_merge()
        if self.flag == 1:
            self.gb_function.generate_random_num(self.board)
        self.flag = 0
        if self.winning():
            self.gb_function.print_board(self.board)
            print("You win!")
            return
        elif self.losing():
            self.gb_function.print_board(self.board)
            print("You lose")
            return
        self.control()
