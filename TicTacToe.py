
# coding: utf-8

# In[ ]:



def display_board(board):
    print('\n'*100)
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('---|---|---')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---|---|---')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])


# In[ ]:


def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("Please pick a marker 'X' or 'O': ").upper()
    player1 = marker
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1, player2)


# In[ ]:


def place_marker(board, marker, position):
    board[position] = marker


# In[ ]:


def win_check(board, mark):
    return((board[1]==board[2]==board[3]==mark) or
           (board[4]==board[5]==board[6]==mark) or
           (board[7]==board[8]==board[9]==mark) or
           (board[1]==board[4]==board[7]==mark) or
           (board[2]==board[5]==board[8]==mark) or
           (board[3]==board[6]==board[9]==mark) or
           (board[1]==board[5]==board[9]==mark) or
           (board[7]==board[5]==board[3]==mark))


# In[ ]:


import random

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'


# In[ ]:


def space_check(board, position):
    return(board[position] == ' ')


# In[ ]:


def full_board_check(board):
    for i  in range(1,10):
        if space_check(board,i):
            return False
    return True


# In[ ]:


def player_choice(board):
    position = 0
    
    while position not in range(1,10) or not space_check(board, position):
        position = int(input('Choose your position (1-9): '))
    return position


# In[ ]:


def replay():
    return(input('Do you want to play again? (Yes/No): ').lower().startswith('y'))


# In[ ]:


print('Welcome to Tic Tac Toe!')

while True:
    theBoard = [' '] *10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Do you want to play? Yes/No: ')
    
    if play_game.lower().startswith('y'):
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            #Player1's turn
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)
            
            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations Player 1! You win!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Tie game')
                    break
                else:
                    turn = 'Player 2'
        
        else:
         # Player2's turn
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)
            
            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Congratulations Player 2! You win!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Tie game!')
                    game_on = False
                else:
                    turn = 'Player 1'
            
           

    if not replay():
        break

