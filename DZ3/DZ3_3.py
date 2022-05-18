# Создайте программу для игры в "Крестики-нолики".

def draw_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-------------")

def win(board):
    global win_coord
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for line in win_coord:
        if board[line[0]] == board[line[1]] == board[line[2]]:
            return True
    return False

def botMove(board):
    for line in win_coord:
        if board[line[0]] == board[line[1]] and str(board[line[2]]) not in 'XO':
            board[line[2]] = 'O'
            print('Бот выбрал', line[2] + 1)
            return
        if board[line[0]] == board[line[2]] and str(board[line[1]]) not in 'XO':
            board[line[1]] = 'O'
            print('Бот выбрал', line[1] + 1)
            return
        if board[line[1]] == board[line[2]] and str(board[line[0]]) not in 'XO':
            board[line[0]] = 'O'
            print('Бот выбрал', line[0] + 1)
            return
    else:
        for i in board:            
            if str(i) not in 'XO':
                board[i-1] = 'O'
                print('Бот выбрал', i)
                return

def playerMove(board):
    while not win(board):
        player = input('Куда поставим X ')
        if player.isdigit() and 0 < int(player) < 10:
            if str(board[int(player)-1]) not in 'XO':
                board[int(player)-1] = 'X'
                return
            else:
                print('Клетка занята')
        else:
            print('Некорректный ввод. Введите число поля от 1 до 9')
            continue

board = list(range(1,10))
print(board)
draw_board(board)
while True:
    playerMove(board)
    draw_board(board)
    if win(board) == True:
        print('Вы выиграли')
        break
    botMove(board)
    draw_board(board)
    if win(board) == True:
        print('Выиграл Бот')
        break
    if board.count('X')+ board.count('O') == 9:
        print('Ничья')
        break