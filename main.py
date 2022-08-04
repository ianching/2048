import TZFE2048
import Wordle

game = ["2048", "Wordle"]
for i in range(len(game)): print(game[i] + ":" + str(i + 1))
def start():
    inp = input("Game pin:")
    if inp == "1": TZFE2048.StartGame(4)
    elif inp == "2": Wordle.StartGame()
    # elif inp == "3": .StartGame()
    start()
if __name__ == "__main__": start()
