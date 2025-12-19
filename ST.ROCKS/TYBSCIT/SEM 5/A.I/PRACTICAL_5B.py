import os
import time

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player = 1
Win = 1
Draw = -1
Running = 0
Stop = 1
Game = Running
Mark = 'X'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def DrawBoard():
    print(" %c | %c | %c " % (board[1], board[2], board[3]))
    print("||_")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("||_")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))
    print("   |   |   ")

def CheckPosition(x):
    return board[x] == ' '

def CheckWin():
    global Game
    if (board[1] == board[2] == board[3] != ' ' or
        board[4] == board[5] == board[6] != ' ' or
        board[7] == board[8] == board[9] != ' '):
        Game = Win
    elif (board[1] == board[4] == board[7] != ' ' or
          board[2] == board[5] == board[8] != ' ' or
          board[3] == board[6] == board[9] != ' '):
        Game = Win
    elif (board[1] == board[5] == board[9] != ' ' or
          board[3] == board[5] == board[7] != ' '):
        Game = Win
    elif all(space != ' ' for space in board[1:]):
        Game = Draw
    else:
        Game = Running

print("Name: Shekhar Suman")
print("Roll No: 47\n")
print("Tic-Tac-Toe Game")
print("Player 1 [X] --- Player 2 [O]\n")
print("Please Wait...")
time.sleep(1)

while Game == Running:
    clear_screen()
    DrawBoard()
    if player % 2 != 0:
        print("Player 1's turn")
        Mark = 'X'
    else:
        print("Player 2's turn")
        Mark = 'O'

    try:
        choice = int(input("Enter position [1-9]: "))
        if choice < 1 or choice > 9:
            print("Invalid choice! Pick between 1–9.")
            time.sleep(1)
            continue
    except ValueError:
        print("Please enter a valid number.")
        time.sleep(1)
        continue

    if CheckPosition(choice):
        board[choice] = Mark
        player += 1
        CheckWin()
    else:
        print("Position already taken!")
        time.sleep(1)

clear_screen()
DrawBoard()
if Game == Draw:
    print("Game Draw")
elif Game == Win:
    player -= 1
    if player % 2 != 0:
        print("Player 1 Won 🎉")
    else:
        print("Player 2 Won 🎉")
