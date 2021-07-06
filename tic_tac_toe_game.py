from typing import Optional


board = {
    '1': ' ', '2': ' ', '3': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '7': ' ', '8': ' ', '9': ' '
}

player = 1          # to initialise first player
total_moves = 0     # to count the moves
end_check = 0
name1=input("Enter player one name-->")
name2=input("Enter player second name-->")

def check():
    # checking the moves of player one
    # for horizontal(start)
    if board['1'] == 'X' and board['2'] == 'X' and board['3'] == 'X':
        print('Congratulation :):):):):):):):)')
        print('Player ' + name1 + ' Won!!')
        
        return 1
    if board['4'] == 'X' and board['5'] == 'X' and board['6'] == 'X':
        print('Congratulation :):):):):):):):)')
        print('Player ' + name1 + ' Won!!')
        
        return 1
    if board['7'] == 'X' and board['8'] == 'X' and board['9'] == 'X':
        print('Congratulation :):):):):):):):)')
        print('Player '+ name1 +' Won!!')
        
        return 1
    # for horizontal(end)
    # for diagonal(start)
    if board['1'] == 'X' and board['5'] == 'X' and board['9'] == 'X':
        print('Congratulation :):):):):):):):)')
        print('Player ' + name1 + ' Won!!')
        
        return 1
    # for diagonal(end)
    # for vertical(start)
    if board['1'] == 'X' and board['4'] == 'X' and board['7'] == 'X':
        print('Congratulation :):):):):):):):)')
        print('Player ' + name1 + ' Won!!')
        
        return 1
    if board['2'] == 'X' and board['5'] == 'X' and board['8'] == 'X':
        print('Congratulation :):):):):):):):)')
        print('Player ' + name1 + ' Won!!')
        
        return 1
    if board['3'] == 'X' and board['6'] == 'X' and board['9'] == 'X':
        print('Congratulation :):):):):):):):)')
        print('Player ' + name1 + ' Won!!')
        
        return 1
    # for vertical(end)

    # checking the moves of player two
    if board['1'] == 'O' and board['2'] == 'O' and board['3'] == 'O':
        print('Congratulation :):):):):):):):)')
        print('Player ' + name2 + ' Won!!')
        
        return 1  # used to end the game
    if board['4'] == 'O' and board['5'] == 'O' and board['6'] == 'O':
        print('Congratulation :):):):):):):):)')
        print('Player ' + name2 + ' Won!!')
        
        return 1
    if board['7'] == 'O' and board['8'] == 'O' and board['9'] == 'O':
        print('Congratulation :):):):):):):):)')
        print('Player ' + name2 + ' Won!!')
        
        return 1
    if board['1'] == 'O' and board['5'] == 'O' and board['9'] == 'O':
        print('Congratulation :):):):):):):):)')
        print('Player ' + name2 + ' Won!!')
        
        return 1
    if board['1'] == 'O' and board['4'] == 'O' and board['7'] == 'O':
        print('Congratulation :):):):):):):):)')
        print('Player ' + name2 + ' Won!!')
        
        return 1
    if board['2'] == 'O' and board['5'] == 'O' and board['8'] == 'O':
        print('Congratulation :):):):):):):):)')
        print('Player ' + name2 + ' Won!!')
        
        return 1
    if board['3'] == 'O' and board['6'] == 'O' and board['9'] == 'O':
        print('Congratulation :):):):):):):):)')
        print('Player ' + name2 + ' Won!!')
        
        return 1
    return 0

 

print("                                                            WELCOME TO DEV GAMEWORLD\n\n")
print('                                                                ****************')
print('                                                                * 1  |  2 |  3 *')
print('                                                                *----|----|----*')
print('                                                                * 4  |  5 |  6 *')
print('                                                                *----|----|----*')
print('                                                                *  7 |  8 |  9 *')
print('                                                                ****************')

print('\n\n\nThis is game pattern player choose number for there o/x to give place\n\n')

while True:
    print('                                                            ****************')
    print('                                                            * '+board['1'] + '  | ' + board['2'] + '  |  ' + board['3']+' *')
    print('                                                            *----|----|----*')
    print('                                                            * '+board['4'] + '  | ' + board['5'] + '  |  ' + board['6']+' *')
    print('                                                            *----|----|----*')
    print('                                                            * '+board['7'] + '  | ' + board['8'] + '  |  ' + board['9']+' *')
    print('                                                            ****************')
    end_check = check()
    if total_moves == 9 or end_check == 1:
        break
    while True:     # input from players
        if player == 1:  # choose player
            p1_input = input('player '+name1 +' Turn-->')
            if p1_input.upper() in board and board[p1_input.upper()] == ' ':
                board[p1_input.upper()] = 'X'
                player = 2
                break
            # on wrong input
            else:
                print('Invalid input, please try again')
                continue
        else:
            p2_input = input('player '+name2+' Turn-->')
            if p2_input.upper() in board and board[p2_input.upper()] == ' ':
                board[p2_input.upper()] = 'O'
                player = 1
                break
            else:  # on wrong input
                print('Invalid input, please try again')
                continue
    total_moves += 1
    print('***************************')
    print()


