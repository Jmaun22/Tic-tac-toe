

class Scorechecker():

    def __init__(self):
        super().__init__()


    def three_in_row(self, remaining_choices):
        if remaining_choices[0] == remaining_choices[4] == remaining_choices[8]:
            game_on = False

            print('end_game')
            return game_on

        elif remaining_choices[2] == remaining_choices[4] == remaining_choices[6]:
            print('end_game')
            game_on = False
            return game_on
        elif remaining_choices[0] == remaining_choices[3] == remaining_choices[6]:
            print('end_game')
            game_on = False
            return game_on

        elif remaining_choices[1] == remaining_choices[4] == remaining_choices[7]:
            print('end_game')
            game_on = False
            return game_on

        elif remaining_choices[2] == remaining_choices[5] == remaining_choices[8]:
            print('end_game')
            game_on = False
            return game_on

        else:
            print("keep playing")#make it a return while loop true false
            game_on = True
            return game_on



