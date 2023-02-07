import random

board1 = ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-']

def display_board():

    print('\n' * 100)
    print(f" {board1[7]} {board1[8]} {board1[9]} \n"
          f" {board1[4]} {board1[5]} {board1[6]} \n"
          f" {board1[1]} {board1[2]} {board1[3]} \n")


def win_check(board1, mark):

    return ((board1[7] == mark and board1[8] == mark and board1[9] == mark) or  # across the top
            (board1[4] == mark and board1[5] == mark and board1[6] == mark) or  # across the middle
            (board1[1] == mark and board1[2] == mark and board1[3] == mark) or  # across the bottom
            (board1[7] == mark and board1[4] == mark and board1[1] == mark) or  # down the middle
            (board1[4] == mark and board1[5] == mark and board1[6] == mark) or
            (board1[8] == mark and board1[5] == mark and board1[2] == mark) or  # down the middle
            (board1[9] == mark and board1[6] == mark and board1[3] == mark) or  # down the right side
            (board1[7] == mark and board1[5] == mark and board1[3] == mark) or  # diagonal
            (board1[9] == mark and board1[5] == mark and board1[1] == mark))  # diagonal


def replay():

    return ('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

print('Welcome to Tic Tac Toe!')
while True:

    play_game = input('Are you ready to play? Enter Yes or No.')
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    turns = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    marker = ""
    turn = random.randint(0, 1)

    while game_on:
        while marker != "X" and marker != "O":
            marker = input("Player 1, choose X or O: ")
        player1 = marker
        display_board()
        if player1 == "X":
            player2 = "O"
        else:
            player2 = "X"

        while sum(turns) != 0:
            if turn == 1:
                X = int(input('PLease enter a number for X '))
                if turns[X] != 0:
                    board1[X] = "X"
                    display_board()
                    turn -= 1
                    turns[X] = 0
                    if win_check(board1, player1):
                        print('Congratulations! You have won the game!')
                        game_on = False
                        break
                    elif sum(turns) == 0:
                        display_board()
                        print('The game is a draw!')
                        break
                else:
                    print("This space on board already changed try another space")
                    continue

            elif turn ==0:
                O = int(input('PLease enter a number for O '))
                if turns[O] != 0:
                    board1[O] = "O"
                    display_board()
                    turn += 1
                    turns[O] = 0
                    if win_check(board1, player2):
                        print('Player 2 has won!')
                        game_on = False
                        break
                    elif sum(turns) == 0:
                        display_board()
                        print('The game is a draw!')
                        break
                else:
                    print("This space on board already changed try another space")
                    continue
            else:
                turns.clear()
                # Reset the board
    replay()
    board1 = ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-']
    turns = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("End of Game")