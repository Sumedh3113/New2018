"""
Tic Tac Toe 
Sumedh Deshpande
"""
import random

def display_board(board):
	print('\n'*100)# to clear the screen before new output
	print('Available   TIC-TAC-TOE\n'+
			   '  moves\n\n  '+
			  '7' + '|'+ '8' + '|'+ '9' +'        '+board[7]+'|'+board[8]+'|'+board[9]+'\n  '+
			  '-----        -----\n  '+
			  '4'+'|'+ '5' +'|'+ '6' +'        '+board[4]+'|'+board[5]+'|'+board[6]+'\n  '+
			  '-----        -----\n  '+
			  '1' +'|'+ '2' +'|'+ '3' +'        '+board[1]+'|'+board[2]+'|'+board[3]+'\n')
'''
def display_board(board):
    print('\n'*100)# to clear the screen before new output
    print(' '+board[7]+' | '+board[8]+' | '+board[9]+' ')
    print('------------')
    print(' '+board[4]+' | '+board[5]+' | '+board[6]+' ')
    print('------------')
    print(' '+board[1]+' | '+board[2]+' | '+board[3]+' ')
'''
'''lst = ['']*10
display_board(lst)
'''

def player_input():
	marker = ''
	while marker != 'X' and marker != 'O':
		marker = input('Player1,Select X or O: ').upper()
		player1= marker
		if player1 == 'X':
			player2 = 'O'
		elif player1 == 'O':
			player2 = 'X'
		else:
			continue
	return (player1,player2)

'''player_input()
'''
    
'''position = int(input("Enter Position between 1-9 \nwhere 1 is bottom left corner and 9 is top right corner\t"))
'''
def fill_place(board, marker,position):
	board[position]= marker
	

'''
fill_place(lst, '$', position)
display_board(lst)
'''
def result(board, mark):
	return((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
	
'''result(lst,'$')
'''
def choose_first():
    if random.randint(0, 1) == 0:# choose value between 0 and 1 randomly
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):
    
    return board[position] == ' '
		
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):# means board has free spaces left
            return False
    return True
'''
This is the imp function
'''
#This function is used so that the player should not give the character as input
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

def play_again():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')	
	
print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            fill_place(theBoard, player1_marker, position)

            if result(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            fill_place(theBoard, player2_marker, position)

            if result(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not play_again():
        break