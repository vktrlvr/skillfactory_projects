board = [[' ',' ',' '] for i in range (3)]
def board_creation(): #рисуем таблицу
    print()
    print("  | 0 | 1 | 2 |")
    for i in range(3):
        print("-" * 15)
        print(f"{i} | {board[i][0]} | {board[i][1]} | {board[i][2]} |")

def check_for_x(x): #проверка для 'X'
    while len(x)!= 2 or any([x[0]>2, 
                             x[0]<0, 
                             x[1]>2, 
                             x[1]<0]):
        print('Неверно ввели данные, пожалуйста попробуйте еще раз')   
        x = list(map(int, input("Игрок 'X': Введите поле (сначала номер строки, а потом столбца через пробел): ").split()))
    if board[x[0]][x[1]] == ' ':
        board[x[0]][x[1]] = 'X'
    else: 
        print('Это поле уже занято, выберите другое.')
        x = list(map(int, input("Игрок 'Х': Введите поле (сначала номер строки, а потом столбца через пробел): ").split()))
        check_for_x(x)

def check_for_o(x): #проверка для 'O'
    while len(x)!= 2 or any([x[0]>2, 
                             x[0]<0, 
                             x[1]>2, 
                             x[1]<0]):
        print('Неверно ввели данные, пожалуйста попробуйте еще раз')   
        x = list(map(int, input("Игрок 'O': Введите поле (сначала номер строки, а потом столбца через пробел): ").split()))
    if board[x[0]][x[1]] == ' ':
        board[x[0]][x[1]] = 'O'
    else: 
        print('Это поле уже занято, выберите другое.')
        x = list(map(int, input("Игрок 'O': Введите поле (сначала номер строки, а потом столбца через пробел): ").split()))
        check_for_o(x)

def winner_var(board): #варианты победы
    for i in range(3):
        if any([all([board[0][i] == board[1][i] == board[2][i] == 'X']),
                all([board[i][0] == board[i][1] == board[i][2] == 'X']),
                all([board[0][0] == board[1][1] == board[2][2] == 'X']),
                all([board[2][0] == board[1][1] == board[0][2] == 'X'])]):
            print("Игрок 'X' победил!")
            return True
            break
        elif any([all([board[0][i] == board[1][i] == board[2][i] == 'O']),
                  all([board[i][0] == board[i][1] == board[i][2] == 'O']),
                  all([board[0][0] == board[1][1] == board[2][2] == 'O']),
                  all([board[2][0] == board[1][1] == board[0][2] == 'O'])]):
            print("Игрок 'O' победил!")
            return True
            break
    
def game(): #ход игры
    cnt = 0
    while not winner_var(board):
        x1 = list(map(int, input("Игрок 'X': Введите поле (сначала номер строки, а потом столбца через пробел): ").split()))
        check_for_x(x1)
        board_creation()
        if winner_var(board):
            break
        cnt += 1
        if cnt == 9:
            print('Ничья.')
            break
        x2 = list(map(int, input("Игрок 'O': Введите поле (сначала номер строки, а потом столбца через пробел): ").split()))
        check_for_o(x2)
        board_creation()
        cnt += 1
        
board_creation() #рисуем таблицу
game() #начинаем игру
