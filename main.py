
from Board import Board
from Player import Player
from computer import Computer
from Scorechecker import Scorechecker
from random import randint
b = Board()
p = Player()
c = Computer()
s = Scorechecker()


#draw board and assign spaces

top_board = ['_','|',' ','_ ','|','_']
middle_board = ['_','|',' ','_ ','|','_']
bottom_board = ['_','|',' ','_ ','|','_']


b.assign_spaces(top_board,middle_board, bottom_board)
zero, one, two, three, four, five, six, seven, eight = b.assign_spaces(top_board,middle_board, bottom_board)

# top_board[0] = 'x'


b.draw_board(top_board, middle_board, bottom_board)






#have player pick X or O
player_Choice = p.playerPicks()
c.computer_piece(p.player_Choice)

computer_choice = c.computer_piece(player_Choice)

#start game
print('Game is ready to start')

#loop for game

game_on = True

while game_on:

    print(one)


    r = randint(0, 8)

    player_space = input('0-8 from left to right in word you pick your move')

    possible_choices = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']

    #checks to see if player choice can be used


    if player_space in possible_choices:
        print('we can use that space')

    else:
        'Sorry! Space is taken. Try again.'

    # check to see if space is taken player
    remaining_choices = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']
    if player_space in remaining_choices:
        print('space is not taken')
        remaining_choices = p.append_player(p.player_Choice, player_space)#make function
        print(remaining_choices)
        if player_space == 'zero':
            top_board[0] = p.player_Choice
        elif player_space == 'one':
            top_board[3] = p.player_Choice
        elif player_space == 'two':
            top_board[5] = p.player_Choice
        elif player_space == 'three':
            middle_board[0] = p.player_Choice
        elif player_space == 'four':
            middle_board[3] = p.player_Choice
        elif player_space == 'five':
            middle_board[5] = p.player_Choice
        elif player_space == 'six':
            bottom_board[0] = p.player_Choice
        elif player_space == 'seven':
            bottom_board[3] = p.player_Choice
        elif player_space == 'eight':
            bottom_board[5] = p.player_Choice
        print(top_board[0])

    else:
        print('Yikes! It looks like that space is taken')
        pick() #make function make it loop once fun complete



    #check for 3 in a row
    game_on = s.three_in_row(remaining_choices)
    b.draw_board(top_board, middle_board, bottom_board)

    #computer turn
    computer_space = remaining_choices[r]
    print(computer_space)
    # check to see if space is taken computer
    #remaining_choices = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']
    if computer_space != computer_choice or computer_space != player_space:
        print('space is not taken')
        print(computer_space)
        remaining_choices[r] = computer_choice#make function
        print(remaining_choices)
        if computer_space == 'zero':
            top_board[0] = computer_choice
        elif computer_space == 'one':
            top_board[3] = computer_choice
        elif computer_space == 'two':
            top_board[5] = computer_choice
        elif computer_space == 'three':
            middle_board[0] = computer_choice
        elif computer_space == 'four':
            middle_board[3] = computer_choice
        elif computer_space == 'five':
            middle_board[5] = computer_choice
        elif computer_space == 'six':
            bottom_board[0] = computer_choice
        elif computer_space == 'seven':
            bottom_board[3] = computer_choice
        elif computer_space == 'eight':
            bottom_board[5] = computer_choice

    else:
        print('Yikes! It looks like that space is taken')


    #check for 3 in a row
    b.draw_board(top_board, middle_board, bottom_board)
    game_on = s.three_in_row(remaining_choices)



