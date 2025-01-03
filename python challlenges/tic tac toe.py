board = {'1': ' ' , '2': ' ' , '3': ' ' , '4': ' ', '5': ' ', '6':' ', '7':' ', '8': ' ', '9':' '}
board_keys = []
for i in board:
    board_keys.append(i)
def print_board(board):
    print(board['7'] + '|'+ board['8'] + '|', board['9'])
    print('-+-+-')
    print(board['4'] + '|'+ board['5'] + '|', board['6'])
    print('-+-+-')
    print(board['1'] + '|'+ board['2'] + '|', board['3'])

def game():
    turn = 'x'
    count = 0
    for i in range(10):
        print_board(board)
        print("its your turn", turn)
        move = input("where do you want to move? : ")
        if board[move] == ' ':
            board[move] = turn
            count += 1
        else:
            print("this place is taken") 
        if count >= 5:
            if board['1'] == board['2'] == board['3'] != ' ':
                print(f"{turn} wins")
                break
            elif board['4'] == board['5'] == board['6'] != ' ':
                print(f"{turn} wins")
                break
            elif board['9'] == board['7'] == board['8'] != ' ':
                print(f"{turn} wins")
                break
            elif board['7'] == board['5'] == board['3'] != ' ':
                print(f"{turn} wins")
                break
            elif board['9'] == board['5'] == board['1'] != ' ':
                print(f"{turn} wins")
                break
            elif board['7'] == board['4'] == board['1'] != ' ':
                print(f"{turn} wins")
                break
            elif board['8'] == board['5'] == board['2'] != ' ':
                print(f"{turn} wins")
                break
            elif board['9'] == board['6'] == board['3'] != ' ':
                print(f"{turn} wins")
                break
        if count>9:
            print("game is a draw")

        if turn == 'o':
            turn = 'x'
        else:
            turn = 'o'
    a = input("do you want to play again(y/n): ")
    if a == 'y':
        for e in board:
            board[e]= " "
            game()

game()